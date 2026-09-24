#!/usr/bin/env python3
"""
Download the price data the analysis scripts need, in three size tiers.

Run this LOCALLY (the research sandbox cannot reach Yahoo Finance):

    pip install yfinance pandas
    python tools/fetch_data.py --tier core       # ~20 symbols, daily, 12y   -> commit to git (small)
    python tools/fetch_data.py --tier watch      # watchlist + theme names   -> commit to git (small)
    python tools/fetch_data.py --tier universe   # all US common stocks, weekly, 12y -> Google Drive (large)

Outputs (gzip CSV, long format: date,symbol,close[,volume]) go to data/. The core and watch tiers
are a few MB at most and are safe to commit; the universe tier can be 30-60 MB and is gitignored.

Also writes data/<tier>_meta.csv with current market cap and shares outstanding per symbol
(from Yahoo fast_info), so historical market cap can be approximated as close * shares.

Symbols come from tools/symbols.py (core/watch lists) and, for the universe tier, from the
Nasdaq Trader symbol directory files (nasdaqlisted.txt, otherlisted.txt), filtered to common
stocks (no ETFs, warrants, units, preferreds, test issues).
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import io
import sys
import time
import urllib.request
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data"

sys.path.insert(0, str(HERE))
from symbols import CORE_SYMBOLS, WATCH_SYMBOLS  # noqa: E402

NASDAQ_LISTED = "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"
OTHER_LISTED = "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"


def universe_symbols() -> list[str]:
    """All US-listed common stocks per Nasdaq Trader symbol directories."""
    out: set[str] = set()

    def read(url: str) -> pd.DataFrame:
        with urllib.request.urlopen(url, timeout=60) as r:
            txt = r.read().decode("utf-8", errors="replace")
        lines = [ln for ln in txt.splitlines() if not ln.startswith("File Creation Time")]
        return pd.read_csv(io.StringIO("\n".join(lines)), sep="|")

    nq = read(NASDAQ_LISTED)
    nq = nq[(nq["Test Issue"] == "N") & (nq["ETF"] == "N")]
    for s, name in zip(nq["Symbol"], nq["Security Name"]):
        if is_common(str(s), str(name)):
            out.add(str(s))

    ot = read(OTHER_LISTED)
    ot = ot[(ot["Test Issue"] == "N") & (ot["ETF"] == "N")]
    for s, name in zip(ot["ACT Symbol"], ot["Security Name"]):
        if is_common(str(s), str(name)):
            out.add(str(s))
    return sorted(out)


def is_common(symbol: str, name: str) -> bool:
    """Heuristic filter for common stock (exclude warrants, units, preferreds, notes, rights)."""
    bad_tokens = ("Warrant", "Unit", "Preferred", "Depositary", "Note", "Right", "Debenture",
                  "Trust Preferred", "% ", "Bond", "ETN", "Fund")
    if any(tok in name for tok in bad_tokens):
        return False
    if any(ch in symbol for ch in ("$", ".", "^", "~", "=")):
        return False
    if len(symbol) == 5 and symbol[-1] in "WRUP":
        return False
    return True


def yahoo_symbol(sym: str) -> str:
    # Yahoo uses '-' for share classes (BRK.B -> BRK-B); crypto symbols are already 'BTC-USD'.
    return sym.replace(".", "-")


def download_prices(symbols: list[str], start: str, interval: str, chunk: int = 200,
                    pause: float = 1.0) -> pd.DataFrame:
    import yfinance as yf

    frames: list[pd.DataFrame] = []
    for i in range(0, len(symbols), chunk):
        batch = [yahoo_symbol(s) for s in symbols[i:i + chunk]]
        for attempt in range(3):
            try:
                raw = yf.download(batch, start=start, interval=interval, auto_adjust=True,
                                  group_by="column", threads=True, progress=False)
                break
            except Exception as e:  # network hiccup: back off and retry
                print(f"  batch {i // chunk}: attempt {attempt + 1} failed: {e}", file=sys.stderr)
                time.sleep(5 * (attempt + 1))
        else:
            continue
        frames.append(tidy(raw, batch))
        print(f"  {min(i + chunk, len(symbols))}/{len(symbols)} symbols", file=sys.stderr)
        time.sleep(pause)
    if not frames:
        return pd.DataFrame(columns=["date", "symbol", "close", "volume"])
    return pd.concat(frames, ignore_index=True)


def tidy(raw: pd.DataFrame, batch: list[str]) -> pd.DataFrame:
    """Convert a yfinance wide frame (possibly MultiIndex columns) to long format."""
    if raw is None or raw.empty:
        return pd.DataFrame(columns=["date", "symbol", "close", "volume"])
    if isinstance(raw.columns, pd.MultiIndex):
        close = raw["Close"]
        vol = raw["Volume"] if "Volume" in raw.columns.get_level_values(0) else None
    else:  # single symbol
        close = raw[["Close"]].rename(columns={"Close": batch[0]})
        vol = raw[["Volume"]].rename(columns={"Volume": batch[0]}) if "Volume" in raw else None
    long = close.stack(future_stack=True).rename("close").reset_index()
    long.columns = ["date", "symbol", "close"]
    if vol is not None:
        v = vol.stack(future_stack=True).rename("volume").reset_index()
        v.columns = ["date", "symbol", "volume"]
        long = long.merge(v, on=["date", "symbol"], how="left")
    long = long.dropna(subset=["close"])
    long["date"] = pd.to_datetime(long["date"]).dt.strftime("%Y-%m-%d")
    long["symbol"] = long["symbol"].str.replace("-", ".", regex=False).where(
        ~long["symbol"].str.endswith("-USD"), long["symbol"])
    return long.sort_values(["symbol", "date"]).reset_index(drop=True)


def fetch_meta(symbols: list[str], pause: float = 0.2) -> pd.DataFrame:
    import yfinance as yf

    rows = []
    for s in symbols:
        try:
            fi = yf.Ticker(yahoo_symbol(s)).fast_info
            rows.append({"symbol": s, "market_cap": getattr(fi, "market_cap", None),
                         "shares": getattr(fi, "shares", None),
                         "last_price": getattr(fi, "last_price", None),
                         "currency": getattr(fi, "currency", None),
                         "asof": dt.date.today().isoformat()})
        except Exception as e:
            rows.append({"symbol": s, "market_cap": None, "shares": None, "last_price": None,
                         "currency": None, "asof": dt.date.today().isoformat(), "error": str(e)[:80]})
        time.sleep(pause)
    return pd.DataFrame(rows)


def write_gz(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", newline="") as f:
        df.to_csv(f, index=False)
    print(f"wrote {path} ({path.stat().st_size / 1e6:.1f} MB, {len(df):,} rows)", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tier", choices=["core", "watch", "universe"], required=True)
    ap.add_argument("--years", type=int, default=12)
    ap.add_argument("--no-meta", action="store_true", help="skip market-cap/shares metadata")
    ap.add_argument("--out", type=Path, default=DATA)
    args = ap.parse_args()

    start = (dt.date.today() - dt.timedelta(days=365 * args.years)).isoformat()
    if args.tier == "core":
        syms, interval = CORE_SYMBOLS, "1d"
    elif args.tier == "watch":
        syms, interval = WATCH_SYMBOLS, "1d"
    else:
        print("fetching universe symbol list from nasdaqtrader.com ...", file=sys.stderr)
        syms, interval = universe_symbols(), "1wk"
        print(f"{len(syms)} common-stock symbols", file=sys.stderr)

    print(f"downloading {len(syms)} symbols, interval={interval}, start={start}", file=sys.stderr)
    prices = download_prices(syms, start=start, interval=interval)
    write_gz(prices, args.out / f"{args.tier}_prices_{interval}.csv.gz")

    if not args.no_meta:
        print("fetching market cap / shares metadata ...", file=sys.stderr)
        meta = fetch_meta(syms)
        meta.to_csv(args.out / f"{args.tier}_meta.csv", index=False)
        print(f"wrote {args.out / f'{args.tier}_meta.csv'}", file=sys.stderr)


if __name__ == "__main__":
    main()
