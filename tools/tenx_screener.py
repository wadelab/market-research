#!/usr/bin/env python3
"""
Find every instance of a >= K-fold rise within a rolling window in a long-format price file,
and estimate base rates by starting market-cap bucket.

    uv run python tools/tenx_screener.py data/universe_prices_1wk.csv.gz --window-days 730 --multiple 10 \
        --meta data/universe_meta.csv --out data/tenx_events.csv

Input: Parquet or CSV with columns date, symbol, close (long format, as written by fetch_data.py).
Optional --meta with columns symbol, shares: historical market cap is approximated as
close * shares (CURRENT shares). This ignores buybacks and dilution. For serial diluters with
reverse splits the estimate is wildly too high (split-adjusted old prices x today's inflated share
count), so a handful of micro-caps land in the >$2B buckets. Treat bucket rates as indicative and
the ALL rows (prices only) as the reliable numbers.

Method: for each symbol, for each date t, compute max(close over (t, t+window]) / close[t].
A "10x event" is any t where that ratio >= multiple. Overlapping events for the same symbol are
collapsed into one episode (first entry date to the date the max was reached).
Base rate = (symbols with >= 1 episode starting in a calendar year) / (symbols alive that year).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load_prices  # noqa: E402


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


CAP_BINS = [0, 50e6, 300e6, 2e9, 10e9, 50e9, np.inf]
CAP_LABELS = ["<50M", "50-300M", "300M-2B", "2-10B", "10-50B", ">50B"]


def fixed_start_rates(prices: pd.DataFrame, window_days: int = 730, multiples=(3, 5, 10),
                      month_day: str = "01-01", meta: pd.DataFrame | None = None) -> pd.DataFrame:
    """Base rate from FIXED start dates (not troughs): for each year's first trading date on or after
    <year>-<month_day>, the share of symbols alive on that date whose maximum close within the next
    `window_days` reaches each multiple. With `meta` (symbol, shares), also broken down by the
    approximate starting market cap (close x current shares)."""
    wide = prices.pivot_table(index="date", columns="symbol", values="close", aggfunc="last").sort_index()
    idx = pd.to_datetime(wide.index)
    wide.index = idx
    last = idx.max()
    shares = None
    if meta is not None and "shares" in meta:
        shares = meta.drop_duplicates("symbol").set_index("symbol")["shares"].reindex(wide.columns)
    rows = []
    for year in range(idx.min().year, idx.max().year + 1):
        anchor = pd.Timestamp(f"{year}-{month_day}")
        pos = idx.searchsorted(anchor)
        if pos >= len(idx) or idx[pos] > anchor + pd.Timedelta(days=14):
            continue
        start = idx[pos]
        end = start + pd.Timedelta(days=window_days)
        seg = wide.loc[(idx > start) & (idx <= end)]
        base = wide.iloc[pos]
        alive = base.notna() & (base > 0)
        if alive.sum() == 0 or seg.empty:
            continue
        ratio = seg.max() / base
        row = {"start": start.date().isoformat(), "alive": int(alive.sum()), "censored": bool(end > last),
               "median_max_ratio": float(ratio[alive].median())}
        for m in multiples:
            row[f"n_{m}x"] = int((ratio[alive] >= m).sum())
            row[f"rate_{m}x"] = row[f"n_{m}x"] / row["alive"]
        rows.append(row)
        if shares is not None:
            cap = (base * shares)[alive]
            bucket = pd.cut(cap, bins=CAP_BINS, labels=CAP_LABELS)
            for b in CAP_LABELS:
                sel = bucket == b
                if sel.sum() == 0:
                    continue
                rows.append({"start": start.date().isoformat(), "bucket": b, "alive": int(sel.sum()),
                             "censored": bool(end > last), "median_max_ratio": float(ratio[alive][sel].median()),
                             **{f"n_{m}x": int((ratio[alive][sel] >= m).sum()) for m in multiples},
                             **{f"rate_{m}x": float((ratio[alive][sel] >= m).mean()) for m in multiples}})
    out = pd.DataFrame(rows)
    if "bucket" in out:
        out["bucket"] = out["bucket"].fillna("ALL")
    else:
        out["bucket"] = "ALL"
    return out


def add_caps(events: pd.DataFrame, meta: pd.DataFrame) -> pd.DataFrame:
    m = meta[["symbol", "shares"]].dropna()
    e = events.merge(m, on="symbol", how="left")
    e["entry_mcap_approx"] = e["entry_close"] * e["shares"]
    e["cap_bucket"] = pd.cut(e["entry_mcap_approx"], bins=CAP_BINS, labels=CAP_LABELS)
    return e


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prices", type=Path)
    ap.add_argument("--window-days", type=int, default=730)
    ap.add_argument("--multiple", type=float, default=10.0)
    ap.add_argument("--meta", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--min-price", type=float, default=0.0, help="ignore entries below this price (penny-stock filter)")
    ap.add_argument("--month-day", default="01-01", help="fixed start date within each year (MM-DD)")
    ap.add_argument("--fixed-out", type=Path, help="write the fixed-start-date table here (CSV)")
    a = ap.parse_args()

    prices = load_prices(a.prices)
    if a.min_price > 0:
        prices = prices[prices["close"] >= a.min_price]
    meta = pd.read_csv(a.meta) if a.meta and a.meta.exists() else None
    events = find_events(prices, a.window_days, a.multiple)
    if meta is not None and not events.empty:
        events = add_caps(events, meta)
    rates = base_rates(prices, events, a.window_days)
    pd.set_option("display.width", 200)
    print(f"\n{len(events)} episodes of >= {a.multiple:g}x within {a.window_days} days "
          f"across {prices['symbol'].nunique()} symbols (any entry date; trough-inclusive)\n")
    print(rates.to_string(index=False))
    if "cap_bucket" in events:
        print("\nEpisodes by approximate starting market cap (close x current shares):")
        print(events["cap_bucket"].value_counts().sort_index().to_string())
    fixed = fixed_start_rates(prices, a.window_days, meta=meta, month_day=a.month_day)
    print(f"\nFixed-start-date base rates (start = first trading day on/after {a.month_day} each year):\n")
    cols = ["start", "bucket", "alive", "n_3x", "rate_3x", "n_5x", "rate_5x", "n_10x", "rate_10x",
            "median_max_ratio", "censored"]
    print(fixed[fixed["bucket"] == "ALL"][cols].to_string(index=False, float_format=lambda x: f"{x:.3f}"))
    if a.fixed_out:
        a.fixed_out.parent.mkdir(parents=True, exist_ok=True)
        fixed.to_csv(a.fixed_out, index=False)
    if a.out:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        events.to_csv(a.out, index=False)
        print(f"\nwrote {a.out}")


if __name__ == "__main__":
    main()
