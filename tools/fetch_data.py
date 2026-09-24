#!/usr/bin/env python3
"""
Download the price data the analysis scripts need, in three size tiers.

Run this LOCALLY (the research sandbox cannot reach Yahoo Finance):

    uv sync
    uv run python tools/fetch_data.py --tier core       # ~20 symbols, daily, 12y   -> commit to git (small)
    uv run python tools/fetch_data.py --tier watch      # watchlist + theme names   -> commit to git (small)
    uv run python tools/fetch_data.py --tier universe   # all US common stocks, weekly, 12y -> Google Drive (large)

Outputs go to data/ in long format (date, symbol, close[, volume]):
  core / watch : gzip CSV, daily, a few MB each            -> commit
  universe     : Parquet (zstd), weekly closes only, ~10-15 MB -> commit (refresh at most quarterly)
All three tiers live in git; no Google Drive step is needed.

Also writes data/<tier>_meta.csv with current market cap, last price and shares per symbol, so
historical market cap can be approximated as close * shares. For core/watch this comes from Yahoo
fast_info (one call per symbol). For the universe it comes from the Nasdaq stock screener in a
single request, falling back to per-symbol Yahoo calls (slow, ~40 min) if that endpoint fails.

Symbols come from tools/symbols.py (core/watch lists) and, for the universe tier, from the
Nasdaq Trader symbol directory files (nasdaqlisted.txt, otherlisted.txt), filtered to common
stocks (no ETFs, warrants, units, preferreds, test issues).
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import sys
import time
import urllib.request
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data"

sys.path.insert(0, str(HERE))
from common import write_prices  # noqa: E402
from symbols import CORE_SYMBOLS, WATCH_SYMBOLS  # noqa: E402

NASDAQ_LISTED = "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"
OTHER_LISTED = "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
NASDAQ_SCREENER = "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=0&download=true"
BROWSER_HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) research-script",
                   "Accept": "application/json, text/plain, */*"}


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


EXCHANGE_SUFFIXES = {"HK", "L", "TO", "V", "AX", "DE", "PA", "SS", "SZ", "T", "KS", "KQ", "SW", "MI",
                     "AS", "ST", "CO", "HE", "OL", "NZ", "SI", "JO", "MX", "SA", "CN", "NE", "F", "BR"}


def yahoo_symbol(sym: str) -> str:
    """Yahoo uses '-' for US share classes (BRK.B -> BRK-B) but '.' for exchange suffixes
    (9880.HK). Crypto symbols are already 'BTC-USD'."""
    if "." in sym:
        base, suffix = sym.rsplit(".", 1)
        if suffix.upper() in EXCHANGE_SUFFIXES:
            return sym
        return f"{base}-{suffix}"
    return sym


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


def _num(x) -> float | None:
    if x in (None, "", "NA", "N/A"):
        return None
    try:
        return float(str(x).replace("$", "").replace(",", "").strip())
    except ValueError:
        return None


def parse_screener_rows(rows: list[dict], asof: str | None = None) -> pd.DataFrame:
    """Turn Nasdaq screener rows into the meta schema (symbol, market_cap, last_price, shares, ...)."""
    asof = asof or dt.date.today().isoformat()
    out = []
    for r in rows:
        mc, px = _num(r.get("marketCap")), _num(r.get("lastsale"))
        out.append({"symbol": str(r.get("symbol", "")).strip().replace("/", "."),
                    "name": r.get("name"), "market_cap": mc, "last_price": px,
                    "shares": (mc / px) if (mc and px) else None,
                    "sector": r.get("sector"), "industry": r.get("industry"),
                    "ipo_year": r.get("ipoyear"), "asof": asof})
    return pd.DataFrame(out)


def nasdaq_screener_meta() -> pd.DataFrame:
    """Current market cap and last price for every US-listed stock in one request."""
    req = urllib.request.Request(NASDAQ_SCREENER, headers=BROWSER_HEADERS)
    with urllib.request.urlopen(req, timeout=120) as r:
        payload = json.load(r)
    rows = payload["data"]["rows"]
    if not rows:
        raise RuntimeError("Nasdaq screener returned no rows")
    return parse_screener_rows(rows)


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


def write_out(df: pd.DataFrame, path: Path) -> None:
    write_prices(df, path)
    print(f"wrote {path} ({path.stat().st_size / 1e6:.1f} MB, {len(df):,} rows)", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tier", choices=["core", "watch", "universe"], required=True)
    ap.add_argument("--years", type=int, default=12)
    ap.add_argument("--no-meta", action="store_true", help="skip market-cap/shares metadata")
    ap.add_argument("--meta-source", choices=["auto", "nasdaq", "yfinance"], default="auto",
                    help="universe tier only: 'nasdaq' = one screener request; 'yfinance' = per-symbol (slow)")
    ap.add_argument("--format", choices=["auto", "csv", "parquet"], default="auto",
                    help="auto = gzip CSV for core/watch, Parquet for universe")
    ap.add_argument("--keep-volume", action="store_true", help="universe tier: keep the volume column")
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

    fmt = args.format if args.format != "auto" else ("parquet" if args.tier == "universe" else "csv")
    ext = ".parquet" if fmt == "parquet" else ".csv.gz"

    print(f"downloading {len(syms)} symbols, interval={interval}, start={start}", file=sys.stderr)
    prices = download_prices(syms, start=start, interval=interval)
    if args.tier == "universe" and not args.keep_volume and "volume" in prices.columns:
        prices = prices.drop(columns=["volume"])
    write_out(prices, args.out / f"{args.tier}_prices_{interval}{ext}")

    if not args.no_meta:
        meta = None
        if args.tier == "universe" and args.meta_source in ("auto", "nasdaq"):
            print("fetching market caps from the Nasdaq screener (one request) ...", file=sys.stderr)
            try:
                meta = nasdaq_screener_meta()
                meta = meta[meta["symbol"].isin(set(syms))]
            except Exception as e:
                print(f"  screener failed ({e}); " + ("falling back to yfinance per symbol"
                      if args.meta_source == "auto" else "no meta written"), file=sys.stderr)
                if args.meta_source != "auto":
                    return
        if meta is None:
            print(f"fetching market cap / shares for {len(syms)} symbols via yfinance ...", file=sys.stderr)
            meta = fetch_meta(syms)
        meta.to_csv(args.out / f"{args.tier}_meta.csv", index=False)
        print(f"wrote {args.out / f'{args.tier}_meta.csv'} ({len(meta):,} rows)", file=sys.stderr)


if __name__ == "__main__":
    main()
