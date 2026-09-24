#!/usr/bin/env python3
"""
Find every instance of a >= K-fold rise within a rolling window in a long-format price file,
and estimate base rates by starting market-cap bucket.

    uv run python tools/tenx_screener.py data/universe_prices_1wk.csv.gz --window-days 730 --multiple 10 \
        --meta data/universe_meta.csv --out data/tenx_events.csv

Input columns: date, symbol, close (long format, as written by fetch_data.py).
Optional --meta with columns symbol, shares: historical market cap is approximated as
close * shares (current shares; ignores buybacks/dilution, which is a real limitation for
exactly the kind of company that 10x's, so treat cap buckets as rough).

Method: for each symbol, for each date t, compute max(close over (t, t+window]) / close[t].
A "10x event" is any t where that ratio >= multiple. Overlapping events for the same symbol are
collapsed into one episode (first entry date to the date the max was reached).
Base rate = (symbols with >= 1 episode starting in a calendar year) / (symbols alive that year).
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def forward_max_ratio(close: np.ndarray, dates: np.ndarray, window_days: int) -> np.ndarray:
    """For each i, max(close[j])/close[i] for j with 0 < dates[j]-dates[i] <= window_days."""
    n = len(close)
    out = np.full(n, np.nan)
    if n == 0:
        return out
    d = dates.astype("datetime64[D]").astype(np.int64)
    j_end = np.searchsorted(d, d + window_days, side="right")  # exclusive end index
    # sparse table for range max would be faster; n per symbol is small (<= ~3000), so use a
    # simple sliding approach with a monotonic deque.
    from collections import deque
    dq: deque[int] = deque()
    j = 1
    for i in range(n):
        # extend window to j_end[i]
        while j < j_end[i]:
            while dq and close[dq[-1]] <= close[j]:
                dq.pop()
            dq.append(j)
            j += 1
        while dq and dq[0] <= i:
            dq.popleft()
        if dq and close[i] > 0:
            out[i] = close[dq[0]] / close[i]
    return out


def find_events(prices: pd.DataFrame, window_days: int, multiple: float) -> pd.DataFrame:
    events = []
    prices = prices.sort_values(["symbol", "date"])
    for sym, g in prices.groupby("symbol", sort=False):
        close = g["close"].to_numpy(dtype=float)
        dates = g["date"].to_numpy(dtype="datetime64[ns]")
        ratio = forward_max_ratio(close, dates, window_days)
        hit = ratio >= multiple
        if not hit.any():
            continue
        # collapse consecutive hits into episodes
        idx = np.flatnonzero(hit)
        starts = [idx[0]]
        for a, b in zip(idx[:-1], idx[1:]):
            if b != a + 1:
                starts.append(b)
        for s in starts:
            d = dates.astype("datetime64[D]").astype(np.int64)
            end = np.searchsorted(d, d[s] + window_days, side="right")
            seg = close[s + 1:end]
            k = s + 1 + int(np.argmax(seg))
            events.append({"symbol": sym, "entry_date": pd.Timestamp(dates[s]).date().isoformat(),
                           "entry_close": close[s], "peak_date": pd.Timestamp(dates[k]).date().isoformat(),
                           "peak_close": close[k], "multiple": close[k] / close[s],
                           "days_to_peak": int(d[k] - d[s])})
    return pd.DataFrame(events)


def base_rates(prices: pd.DataFrame, events: pd.DataFrame, window_days: int) -> pd.DataFrame:
    """Per calendar year: symbols alive at year start (with a full window ahead) vs. symbols with
    an episode starting that year."""
    prices = prices.copy()
    prices["year"] = pd.to_datetime(prices["date"]).dt.year
    last_date = pd.to_datetime(prices["date"]).max()
    alive = prices.groupby("year")["symbol"].nunique().rename("symbols_alive")
    if events.empty:
        ev = pd.Series(dtype=int, name="symbols_with_event")
    else:
        e = events.copy(); e["year"] = pd.to_datetime(e["entry_date"]).dt.year
        ev = e.groupby("year")["symbol"].nunique().rename("symbols_with_event")
    out = pd.concat([alive, ev], axis=1).fillna(0)
    out["rate"] = out["symbols_with_event"] / out["symbols_alive"]
    # years without a full forward window are censored
    cutoff = (last_date - pd.Timedelta(days=window_days)).year
    out["censored"] = out.index > cutoff
    return out.reset_index().rename(columns={"index": "year"})


def add_caps(events: pd.DataFrame, meta: pd.DataFrame) -> pd.DataFrame:
    m = meta[["symbol", "shares"]].dropna()
    e = events.merge(m, on="symbol", how="left")
    e["entry_mcap_approx"] = e["entry_close"] * e["shares"]
    bins = [0, 50e6, 300e6, 2e9, 10e9, 50e9, np.inf]
    labels = ["<50M", "50-300M", "300M-2B", "2-10B", "10-50B", ">50B"]
    e["cap_bucket"] = pd.cut(e["entry_mcap_approx"], bins=bins, labels=labels)
    return e


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prices", type=Path)
    ap.add_argument("--window-days", type=int, default=730)
    ap.add_argument("--multiple", type=float, default=10.0)
    ap.add_argument("--meta", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--min-price", type=float, default=0.0, help="ignore entries below this price (penny-stock filter)")
    a = ap.parse_args()

    prices = pd.read_csv(a.prices)
    if a.min_price > 0:
        prices = prices[prices["close"] >= a.min_price]
    events = find_events(prices, a.window_days, a.multiple)
    if a.meta and a.meta.exists() and not events.empty:
        events = add_caps(events, pd.read_csv(a.meta))
    rates = base_rates(prices, events, a.window_days)

    print(f"\n{len(events)} episodes of >= {a.multiple:g}x within {a.window_days} days "
          f"across {prices['symbol'].nunique()} symbols\n")
    print(rates.to_string(index=False))
    if "cap_bucket" in events:
        print("\nEpisodes by approximate starting market cap:")
        print(events["cap_bucket"].value_counts().sort_index().to_string())
    if a.out:
        events.to_csv(a.out, index=False)
        print(f"\nwrote {a.out}")


if __name__ == "__main__":
    main()
