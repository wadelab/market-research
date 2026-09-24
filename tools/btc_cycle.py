#!/usr/bin/env python3
"""
Bitcoin halving-cycle table: for each halving, the pre-halving low, post-halving peak, the
subsequent bear-market low, and the timing, plus where 'today' sits in the current cycle.

    python tools/btc_cycle.py data/core_prices_1d.csv.gz [--asof 2026-09-24]

Input: long-format file with a BTC-USD symbol (as written by fetch_data.py --tier core).
Halving dates are hard-coded (block-height events): 2012-11-28, 2016-07-09, 2020-05-11, 2024-04-20.
The next is estimated at 2028-04 (block 1,050,000; date depends on hash rate).

This is descriptive. Three completed cycles is not a sample from which to forecast; the table
is here so that any claim about "where we are in the cycle" is tied to actual numbers.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

HALVINGS = ["2012-11-28", "2016-07-09", "2020-05-11", "2024-04-20"]
NEXT_HALVING_EST = "2028-04-15"


def load_btc(path: Path) -> pd.Series:
    df = pd.read_csv(path)
    df = df[df["symbol"].isin(["BTC-USD", "BTC"])]
    s = pd.Series(df["close"].to_numpy(), index=pd.to_datetime(df["date"])).sort_index()
    return s[~s.index.duplicated()]


def cycle_table(btc: pd.Series, asof: pd.Timestamp | None = None) -> pd.DataFrame:
    asof = asof or btc.index.max()
    hs = [pd.Timestamp(h) for h in HALVINGS] + [pd.Timestamp(NEXT_HALVING_EST)]
    rows = []
    for i, h in enumerate(hs[:-1]):
        nxt = hs[i + 1]
        seg = btc[(btc.index >= h) & (btc.index < min(nxt, asof))]
        if seg.empty:
            continue
        peak_date, peak = seg.idxmax(), seg.max()
        after = seg[seg.index > peak_date]
        low_date, low = (after.idxmin(), after.min()) if not after.empty else (pd.NaT, float("nan"))
        pre = btc[(btc.index < h) & (btc.index >= h - pd.Timedelta(days=548))]
        pre_low_date, pre_low = (pre.idxmin(), pre.min()) if not pre.empty else (pd.NaT, float("nan"))
        at_h = btc[btc.index <= h].iloc[-1] if (btc.index <= h).any() else float("nan")
        rows.append({
            "halving": h.date().isoformat(),
            "price_at_halving": round(at_h, 2),
            "pre_halving_low": round(pre_low, 2), "pre_low_date": _d(pre_low_date),
            "peak": round(peak, 2), "peak_date": _d(peak_date),
            "days_halving_to_peak": (peak_date - h).days,
            "peak_x_from_halving": round(peak / at_h, 2) if at_h == at_h else None,
            "post_peak_low": round(low, 2), "post_low_date": _d(low_date),
            "drawdown_from_peak_%": round(100 * (low / peak - 1), 1) if low == low else None,
            "complete": bool(nxt <= asof),
        })
    return pd.DataFrame(rows)


def where_now(btc: pd.Series, asof: pd.Timestamp | None = None) -> dict:
    asof = asof or btc.index.max()
    h = pd.Timestamp(HALVINGS[-1])
    seg = btc[(btc.index >= h) & (btc.index <= asof)]
    px = btc[btc.index <= asof].iloc[-1]
    return {"asof": asof.date().isoformat(), "price": round(px, 2),
            "days_since_halving": (asof - h).days,
            "days_to_next_halving_est": (pd.Timestamp(NEXT_HALVING_EST) - asof).days,
            "cycle_peak": round(seg.max(), 2), "cycle_peak_date": _d(seg.idxmax()),
            "drawdown_from_cycle_peak_%": round(100 * (px / seg.max() - 1), 1),
            "x_to_regain_peak": round(seg.max() / px, 2)}


def _d(ts) -> str | None:
    return None if pd.isna(ts) else pd.Timestamp(ts).date().isoformat()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prices", type=Path)
    ap.add_argument("--asof", type=str)
    a = ap.parse_args()
    btc = load_btc(a.prices)
    asof = pd.Timestamp(a.asof) if a.asof else None
    pd.set_option("display.width", 200)
    print(cycle_table(btc, asof).to_string(index=False))
    print()
    for k, v in where_now(btc, asof).items():
        print(f"{k:>28}: {v}")


if __name__ == "__main__":
    main()
