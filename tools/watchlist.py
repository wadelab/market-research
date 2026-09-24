#!/usr/bin/env python3
"""
Watchlist tracker. Reads data/watchlist.csv, prints each candidate's implied 10x market cap and,
if a price file is available, progress since entry.

    python tools/watchlist.py                                  # table from the CSV alone
    python tools/watchlist.py --prices data/watch_prices_1d.csv.gz   # add latest price & progress

watchlist.csv columns:
  symbol, name, theme, entry_date, entry_price, entry_mcap, target_multiple, thesis, catalysts,
  kill_criteria, status, note_file
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
WATCHLIST = ROOT / "data" / "watchlist.csv"


def load_watchlist(path: Path = WATCHLIST) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["target_multiple"] = df["target_multiple"].fillna(10.0)
    df["implied_mcap"] = df["entry_mcap"] * df["target_multiple"]
    df["target_price"] = df["entry_price"] * df["target_multiple"]
    return df


def attach_prices(df: pd.DataFrame, prices_path: Path) -> pd.DataFrame:
    p = pd.read_csv(prices_path).sort_values("date")
    last = p.groupby("symbol").tail(1).set_index("symbol")
    df = df.merge(last[["date", "close"]].rename(columns={"date": "last_date", "close": "last_price"}),
                  left_on="symbol", right_index=True, how="left")
    df["multiple_so_far"] = df["last_price"] / df["entry_price"]
    df["remaining_x"] = df["target_price"] / df["last_price"]
    return df


def _money(x: float) -> str:
    if pd.isna(x):
        return ""
    for unit, div in (("T", 1e12), ("B", 1e9), ("M", 1e6)):
        if abs(x) >= div:
            return f"{x / div:,.1f}{unit}"
    return f"{x:,.0f}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prices", type=Path)
    ap.add_argument("--watchlist", type=Path, default=WATCHLIST)
    a = ap.parse_args()
    df = load_watchlist(a.watchlist)
    if a.prices:
        df = attach_prices(df, a.prices)
    cols = ["symbol", "theme", "entry_date", "entry_price", "entry_mcap", "implied_mcap", "status"]
    if "last_price" in df:
        cols += ["last_date", "last_price", "multiple_so_far", "remaining_x"]
    show = df[cols].copy()
    for c in ("entry_mcap", "implied_mcap"):
        show[c] = show[c].map(_money)
    pd.set_option("display.width", 220)
    print(show.to_string(index=False))


if __name__ == "__main__":
    main()
