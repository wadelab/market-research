#!/usr/bin/env python3
"""
Conditional base rates: does buying after a drawdown, or after a prior-year loss/gain, change the
probability of a 3x/5x/10x within 730 days? Also the buy-and-hold END value (no selling) by bucket,
which is what an investor without a sell rule actually receives.

    uv run python tools/conditional_rates.py data/universe_prices_1wk.parquet --meta data/universe_meta.csv \
        --out data/derived/conditional_rates.csv

Method: for each year's first trading day on/after 1 January (with >= 12 months of history before
and 24 months after), compute per symbol: prior 12-month return, drawdown from the 3-year high,
forward 730-day maximum / start, and 730-day end / start. Pool the years and tabulate by bucket.
Caps are approximate (close x current shares); see tenx_screener.py.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load_prices  # noqa: E402

PRIOR_BINS = [-1, -0.6, -0.3, 0, 0.5, 1.5, np.inf]
PRIOR_LABELS = ["< -60%", "-60..-30%", "-30..0%", "0..+50%", "+50..+150%", "> +150%"]
DD_BINS = [-1.01, -0.8, -0.6, -0.3, 0.0001]
DD_LABELS = ["< -80%", "-80..-60%", "-60..-30%", "-30..0%"]


def per_symbol_table(prices: pd.DataFrame, meta: pd.DataFrame | None = None, window_days: int = 730,
                     min_price: float = 1.0) -> pd.DataFrame:
    p = prices[prices["close"] >= min_price]
    wide = p.pivot_table(index="date", columns="symbol", values="close", aggfunc="last").sort_index()
    idx = pd.to_datetime(wide.index)
    wide.index = idx
    shares = None
    if meta is not None and "shares" in meta:
        shares = meta.drop_duplicates("symbol").set_index("symbol")["shares"].reindex(wide.columns)
    rows = []
    for year in range(idx.min().year, idx.max().year + 1):
        pos = idx.searchsorted(pd.Timestamp(f"{year}-01-01"))
        if pos >= len(idx):
            continue
        start = idx[pos]
        prior_idx = idx[idx <= start - pd.Timedelta(days=365)]
        fwd_idx = idx[(idx > start) & (idx <= start + pd.Timedelta(days=window_days))]
        if len(prior_idx) == 0 or len(fwd_idx) == 0 or fwd_idx[-1] < start + pd.Timedelta(days=window_days - 14):
            continue  # need a full window on both sides
        base = wide.loc[start]
        prior = wide.loc[prior_idx[-1]]
        hi3 = wide.loc[(idx > start - pd.Timedelta(days=3 * 365)) & (idx <= start)].max()
        fwd = wide.loc[fwd_idx]
        ok = base.notna() & prior.notna() & (base > 0) & fwd.max().notna()
        df = pd.DataFrame({"year": year, "prior_ret": base / prior - 1, "dd3y": base / hi3 - 1,
                           "fwd_max": fwd.max() / base, "end_ratio": fwd.iloc[-1] / base,
                           "cap": (base * shares) if shares is not None else np.nan})[ok]
        rows.append(df.reset_index().rename(columns={"index": "symbol"}))
    d = pd.concat(rows, ignore_index=True)
    d["prior_bucket"] = pd.cut(d["prior_ret"], PRIOR_BINS, labels=PRIOR_LABELS)
    d["dd_bucket"] = pd.cut(d["dd3y"], DD_BINS, labels=DD_LABELS)
    return d


def summarise(d: pd.DataFrame, key: str) -> pd.DataFrame:
    g = d.groupby(key, observed=True)
    out = pd.DataFrame({
        "n": g.size(),
        "p_max_3x": g["fwd_max"].apply(lambda x: (x >= 3).mean()),
        "p_max_5x": g["fwd_max"].apply(lambda x: (x >= 5).mean()),
        "p_max_10x": g["fwd_max"].apply(lambda x: (x >= 10).mean()),
        "median_max": g["fwd_max"].median(),
        "median_end": g["end_ratio"].median(),
        "p_end_lt_0.5x": g["end_ratio"].apply(lambda x: (x < 0.5).mean()),
        "p_end_3x": g["end_ratio"].apply(lambda x: (x >= 3).mean()),
        "p_end_10x": g["end_ratio"].apply(lambda x: (x >= 10).mean()),
    })
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prices", type=Path)
    ap.add_argument("--meta", type=Path)
    ap.add_argument("--window-days", type=int, default=730)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    meta = pd.read_csv(a.meta) if a.meta and a.meta.exists() else None
    d = per_symbol_table(load_prices(a.prices), meta, a.window_days)
    pd.set_option("display.width", 220)
    fmt = lambda x: f"{x:.4f}"
    years = sorted(d["year"].unique())
    print(f"Pooled starts {years[0]}-{years[-1]}, {len(d):,} stock-years, window {a.window_days} d\n")
    tables = []
    for label, sub in (("all", d), ("cap<300M", d[d["cap"] < 300e6]), ("cap>=2B", d[d["cap"] >= 2e9])):
        if sub.empty:
            continue
        for key in ("dd_bucket", "prior_bucket"):
            t = summarise(sub, key)
            print(f"== {label}: by {key} ==")
            print(t.to_string(float_format=fmt), "\n")
            t = t.reset_index().rename(columns={key: "bucket"})
            t.insert(0, "group", label); t.insert(1, "conditioning", key)
            tables.append(t)
    if a.out:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        pd.concat(tables, ignore_index=True).to_csv(a.out, index=False)
        print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
