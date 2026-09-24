#!/usr/bin/env python3
"""
Download the price data the analysis scripts need, in three size tiers.

Run this LOCALLY (the research sandbox cannot reach the data providers):

    uv sync
    uv run python tools/fetch_data.py --tier core       # ~20 symbols, daily, 12y   -> commit
    uv run python tools/fetch_data.py --tier watch      # watchlist + theme names   -> commit
    uv run python tools/fetch_data.py --tier universe   # all US common stocks, weekly, 12y -> commit (Parquet)

Sources (chosen to avoid per-symbol rate limits, which killed the first Yahoo-only run):
  * US equities and ETFs: Stooq's bulk daily database, ONE zip for the whole US market
    (https://stooq.com/db/h/ -> d_us_txt.zip, a few hundred MB). Downloaded once to data/.cache/
    and reused by all tiers. If the automatic download fails, download the file from that page in a
    browser and pass --stooq-zip <path>. Stooq daily data is split-adjusted but not dividend-adjusted
    [from memory, verify]; the script checks known splits (NVDA, TSLA, SMCI) and warns if unadjusted.
  * Crypto (the 'XXX-USD' symbols): Yahoo Finance via yfinance, small batches, no threads, long
    back-off on rate limits, resumable.
  * Market caps: Nasdaq stock screener (one request, all US listed) + CoinGecko (one request, crypto);
    per-symbol Yahoo only as a slow fallback for anything else (e.g. 9880.HK, OTC tickers).

Outputs go to data/ in long format (date, symbol, close[, volume]):
  core / watch : gzip CSV, daily                          -> commit
  universe     : Parquet (zstd), weekly closes only, ~10 MB -> commit (refresh at most quarterly)
plus data/<tier>_meta.csv (symbol, market_cap, last_price, shares, ...) as of the download date.

Caveat for base rates: bulk databases contain only currently listed symbols, so delisted failures are
missing and any base rate computed from this universe is an upper bound (survivorship bias).
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import sys
import time
import zipfile
from pathlib import Path

import certifi
import pandas as pd
import requests

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data"
CACHE = DATA / ".cache"

sys.path.insert(0, str(HERE))
from common import load_prices, write_prices  # noqa: E402
from symbols import COINGECKO_IDS, CORE_SYMBOLS, WATCH_SYMBOLS  # noqa: E402

NASDAQ_LISTED = "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"
OTHER_LISTED = "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
NASDAQ_SCREENER = "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=0&download=true"
STOOQ_US_DAILY = "https://static.stooq.com/db/h/d_us_txt.zip"
COINGECKO_MARKETS = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={ids}&per_page=250"
BROWSER_HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) research-script",
                   "Accept": "application/json, text/plain, */*"}

KNOWN_SPLITS = [("NVDA", "2024-06-10", 10), ("TSLA", "2022-08-25", 3), ("SMCI", "2024-10-01", 10)]


def http_get(url: str, timeout: int = 120, stream: bool = False) -> requests.Response:
    """GET with browser-like headers and certifi's CA bundle, so it works on Pythons that lack system
    root certificates (e.g. the python.org macOS installer before 'Install Certificates.command')."""
    r = requests.get(url, headers=BROWSER_HEADERS, timeout=timeout, stream=stream, verify=certifi.where())
    r.raise_for_status()
    return r


# ----------------------------------------------------------------------------- symbol helpers
def is_crypto(sym: str) -> bool:
    return sym.endswith("-USD")


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


def stooq_to_symbol(member: str) -> str | None:
    """'data/daily/us/nasdaq stocks/1/brk-b.us.txt' -> 'BRK.B'; non-US members -> None."""
    name = member.rsplit("/", 1)[-1]
    if not name.endswith(".us.txt"):
        return None
    return name[:-len(".us.txt")].upper().replace("-", ".")


def universe_symbols() -> list[str]:
    """All US-listed common stocks per Nasdaq Trader symbol directories."""
    out: set[str] = set()

    def read(url: str) -> pd.DataFrame:
        txt = http_get(url, timeout=60).text
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


# ----------------------------------------------------------------------------- Stooq bulk
def ensure_stooq_zip(path: Path | None) -> Path:
    if path and path.exists():
        return path
    CACHE.mkdir(parents=True, exist_ok=True)
    target = CACHE / "d_us_txt.zip"
    if target.exists() and target.stat().st_size > 10_000_000:
        print(f"using cached {target}", file=sys.stderr)
        return target
    print(f"downloading {STOOQ_US_DAILY} (a few hundred MB, once) ...", file=sys.stderr)
    try:
        with http_get(STOOQ_US_DAILY, timeout=900, stream=True) as r, open(target, "wb") as f:
            done = 0
            for chunk in r.iter_content(chunk_size=1 << 20):
                f.write(chunk); done += len(chunk)
                if done % (50 << 20) < (1 << 20):
                    print(f"  {done / 1e6:.0f} MB", file=sys.stderr)
    except Exception as e:
        target.unlink(missing_ok=True)
        raise SystemExit(f"Stooq bulk download failed ({e}). Download 'd_us_txt.zip' from "
                         f"https://stooq.com/db/h/ in a browser and re-run with --stooq-zip <path>.")
    print(f"saved {target} ({target.stat().st_size / 1e6:.0f} MB)", file=sys.stderr)
    return target


def parse_stooq_member(text: str, symbol: str, start: str) -> pd.DataFrame:
    """Stooq member format: <TICKER>,<PER>,<DATE>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>,<OPENINT>"""
    df = pd.read_csv(io.StringIO(text))
    df.columns = [c.strip("<>").lower() for c in df.columns]
    if "close" not in df.columns or df.empty:
        return pd.DataFrame(columns=["date", "symbol", "close", "volume"])
    out = pd.DataFrame({
        "date": pd.to_datetime(df["date"].astype(str), format="%Y%m%d").dt.strftime("%Y-%m-%d"),
        "symbol": symbol, "close": df["close"].astype(float),
        "volume": df["vol"].astype(float) if "vol" in df.columns else float("nan")})
    return out[out["date"] >= start].reset_index(drop=True)


def stooq_prices(zip_path: Path, wanted: set[str] | None, start: str, stocks_only: bool = False) -> pd.DataFrame:
    """Extract daily closes for `wanted` symbols (None = every US symbol) from the Stooq zip."""
    frames = []
    with zipfile.ZipFile(zip_path) as z:
        members = [m for m in z.namelist() if m.endswith(".us.txt")]
        if stocks_only:
            members = [m for m in members if " stocks/" in m]
        for i, m in enumerate(members):
            sym = stooq_to_symbol(m)
            if sym is None or (wanted is not None and sym not in wanted):
                continue
            with z.open(m) as f:
                frames.append(parse_stooq_member(f.read().decode("utf-8", errors="replace"), sym, start))
            if (i + 1) % 1000 == 0:
                print(f"  scanned {i + 1}/{len(members)} members", file=sys.stderr)
    if not frames:
        return pd.DataFrame(columns=["date", "symbol", "close", "volume"])
    return pd.concat(frames, ignore_index=True).sort_values(["symbol", "date"]).reset_index(drop=True)


def to_weekly(daily: pd.DataFrame) -> pd.DataFrame:
    """Last close of each week (Friday-anchored) per symbol; drops volume."""
    d = daily.copy()
    d["date"] = pd.to_datetime(d["date"])
    w = (d.set_index("date").groupby("symbol")["close"].resample("W-FRI").last()
         .dropna().reset_index())
    w["date"] = w["date"].dt.strftime("%Y-%m-%d")
    return w[["date", "symbol", "close"]].sort_values(["symbol", "date"]).reset_index(drop=True)


def check_split_adjustment(prices: pd.DataFrame) -> list[str]:
    """Warn if a known split shows up as a price discontinuity (i.e. data are unadjusted)."""
    warnings = []
    for sym, date, ratio in KNOWN_SPLITS:
        g = prices[prices["symbol"] == sym].sort_values("date")
        before = g[g["date"] < date].tail(1)
        after = g[g["date"] >= date].head(1)
        if before.empty or after.empty:
            continue
        r = float(before["close"].iloc[0]) / float(after["close"].iloc[0])
        if r > ratio * 0.7:
            warnings.append(f"{sym}: close ratio {r:.1f} across {date} looks like an unadjusted {ratio}:1 split")
    return warnings


# ----------------------------------------------------------------------------- Yahoo (crypto, fallback)
def _is_rate_limit(e: Exception) -> bool:
    return "Too Many Requests" in str(e) or "Rate limited" in str(e) or "RateLimit" in type(e).__name__


def download_yahoo(symbols: list[str], start: str, interval: str = "1d", chunk: int = 10,
                   pause: float = 3.0, out_path: Path | None = None) -> pd.DataFrame:
    """Sequential (no threads), small batches, long back-off on rate limits; resumable via out_path."""
    import yfinance as yf

    done: pd.DataFrame | None = None
    if out_path and out_path.exists():
        done = load_prices(out_path)
        have = set(done["symbol"].unique())
        symbols = [s for s in symbols if s not in have]
        print(f"  resuming: {len(have)} symbols already in {out_path.name}, {len(symbols)} to go", file=sys.stderr)
    frames = [done] if done is not None and len(done) else []
    for i in range(0, len(symbols), chunk):
        batch = symbols[i:i + chunk]
        raw = None
        for attempt in range(4):
            try:
                raw = yf.download([yahoo_symbol(s) for s in batch], start=start, interval=interval,
                                  auto_adjust=True, group_by="column", threads=False, progress=False)
                break
            except Exception as e:
                wait = 120 * (attempt + 1) if _is_rate_limit(e) else 10 * (attempt + 1)
                print(f"  batch {batch[0]}..: {type(e).__name__}: {str(e)[:80]}; waiting {wait}s", file=sys.stderr)
                time.sleep(wait)
        if raw is None:
            print(f"  giving up on {batch}", file=sys.stderr)
            continue
        got = tidy(raw, batch)
        if got.empty:
            print(f"  no rows for {batch} (rate limited silently?); waiting 120s", file=sys.stderr)
            time.sleep(120)
        frames.append(got)
        if out_path:
            write_prices(pd.concat(frames, ignore_index=True), out_path)
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


# ----------------------------------------------------------------------------- metadata
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
                    "ipo_year": r.get("ipoyear"), "asof": asof, "source": "nasdaq_screener"})
    return pd.DataFrame(out)


def nasdaq_screener_meta() -> pd.DataFrame:
    """Current market cap and last price for every US-listed stock in one request."""
    payload = http_get(NASDAQ_SCREENER, timeout=120).json()
    rows = payload["data"]["rows"]
    if not rows:
        raise RuntimeError("Nasdaq screener returned no rows")
    return parse_screener_rows(rows)


def parse_coingecko_rows(rows: list[dict], asof: str | None = None) -> pd.DataFrame:
    asof = asof or dt.date.today().isoformat()
    by_id = {v: k for k, v in COINGECKO_IDS.items()}
    out = []
    for r in rows:
        sym = by_id.get(r.get("id"))
        if not sym:
            continue
        mc, px, circ = r.get("market_cap"), r.get("current_price"), r.get("circulating_supply")
        out.append({"symbol": sym, "name": r.get("name"), "market_cap": mc, "last_price": px,
                    "shares": circ, "fdv": r.get("fully_diluted_valuation"), "asof": asof,
                    "source": "coingecko"})
    return pd.DataFrame(out)


def coingecko_meta(symbols: list[str]) -> pd.DataFrame:
    ids = ",".join(COINGECKO_IDS[s] for s in symbols if s in COINGECKO_IDS)
    if not ids:
        return pd.DataFrame()
    return parse_coingecko_rows(http_get(COINGECKO_MARKETS.format(ids=ids), timeout=60).json())


def yahoo_meta(symbols: list[str], pause: float = 2.0) -> pd.DataFrame:
    """Slow per-symbol fallback with rate-limit back-off."""
    import yfinance as yf

    rows = []
    for s in symbols:
        for attempt in range(3):
            try:
                fi = yf.Ticker(yahoo_symbol(s)).fast_info
                rows.append({"symbol": s, "market_cap": getattr(fi, "market_cap", None),
                             "shares": getattr(fi, "shares", None), "last_price": getattr(fi, "last_price", None),
                             "currency": getattr(fi, "currency", None), "asof": dt.date.today().isoformat(),
                             "source": "yahoo"})
                break
            except Exception as e:
                if _is_rate_limit(e) and attempt < 2:
                    print(f"  {s}: rate limited; waiting {120 * (attempt + 1)}s", file=sys.stderr)
                    time.sleep(120 * (attempt + 1))
                    continue
                rows.append({"symbol": s, "asof": dt.date.today().isoformat(), "source": "yahoo",
                             "error": str(e)[:80]})
                break
        time.sleep(pause)
    return pd.DataFrame(rows)


def build_meta(symbols: list[str]) -> pd.DataFrame:
    parts = []
    equities = [s for s in symbols if not is_crypto(s)]
    crypto = [s for s in symbols if is_crypto(s)]
    covered: set[str] = set()
    if equities:
        try:
            scr = nasdaq_screener_meta()
            scr = scr[scr["symbol"].isin(set(equities))]
            parts.append(scr); covered |= set(scr["symbol"])
            print(f"  nasdaq screener: {len(scr)}/{len(equities)} equities", file=sys.stderr)
        except Exception as e:
            print(f"  nasdaq screener failed: {e}", file=sys.stderr)
    if crypto:
        try:
            cg = coingecko_meta(crypto)
            parts.append(cg); covered |= set(cg["symbol"])
            print(f"  coingecko: {len(cg)}/{len(crypto)} crypto", file=sys.stderr)
        except Exception as e:
            print(f"  coingecko failed: {e}", file=sys.stderr)
    rest = [s for s in symbols if s not in covered]
    if rest and len(rest) <= 60:
        print(f"  yahoo fallback for {len(rest)} symbols (slow): {rest}", file=sys.stderr)
        parts.append(yahoo_meta(rest))
    elif rest:
        print(f"  {len(rest)} symbols without metadata (too many for the Yahoo fallback)", file=sys.stderr)
    return pd.concat([p for p in parts if len(p)], ignore_index=True) if parts else pd.DataFrame()


# ----------------------------------------------------------------------------- main
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tier", choices=["core", "watch", "universe"], required=True)
    ap.add_argument("--years", type=int, default=12)
    ap.add_argument("--stooq-zip", type=Path, help="path to a manually downloaded d_us_txt.zip")
    ap.add_argument("--equity-source", choices=["stooq", "yahoo"], default="stooq")
    ap.add_argument("--no-meta", action="store_true", help="skip market-cap metadata")
    ap.add_argument("--format", choices=["auto", "csv", "parquet"], default="auto",
                    help="auto = gzip CSV for core/watch, Parquet for universe")
    ap.add_argument("--out", type=Path, default=DATA)
    args = ap.parse_args()

    start = (dt.date.today() - dt.timedelta(days=365 * args.years)).isoformat()
    if args.tier == "core":
        syms, interval = list(CORE_SYMBOLS), "1d"
    elif args.tier == "watch":
        syms, interval = list(dict.fromkeys(WATCH_SYMBOLS)), "1d"
    else:
        try:
            print("fetching universe symbol list from nasdaqtrader.com ...", file=sys.stderr)
            syms = universe_symbols()
            print(f"  {len(syms)} common-stock symbols", file=sys.stderr)
        except Exception as e:
            print(f"  symbol directory failed ({e}); using every stock in the Stooq zip", file=sys.stderr)
            syms = []
        interval = "1wk"
    fmt = args.format if args.format != "auto" else ("parquet" if args.tier == "universe" else "csv")
    out_path = args.out / f"{args.tier}_prices_{interval}{'.parquet' if fmt == 'parquet' else '.csv.gz'}"

    equities = [s for s in syms if not is_crypto(s)]
    crypto = [s for s in syms if is_crypto(s)]
    frames = []

    if args.tier == "universe" or args.equity_source == "stooq":
        zp = ensure_stooq_zip(args.stooq_zip)
        wanted = set(equities) if equities else None
        print(f"extracting {'all US stocks' if wanted is None else f'{len(wanted)} symbols'} from {zp.name} ...",
              file=sys.stderr)
        daily = stooq_prices(zp, wanted, start, stocks_only=(args.tier == "universe"))
        print(f"  {daily['symbol'].nunique()} symbols, {len(daily):,} daily rows", file=sys.stderr)
        for w in check_split_adjustment(daily):
            print(f"  WARNING {w}", file=sys.stderr)
        missing = sorted(set(equities) - set(daily["symbol"])) if equities else []
        if missing and args.tier != "universe":
            print(f"  not in Stooq zip, trying Yahoo for: {missing}", file=sys.stderr)
            frames.append(download_yahoo(missing, start, out_path=None))
        frames.append(to_weekly(daily) if args.tier == "universe" else daily)
    elif equities:
        frames.append(download_yahoo(equities, start, out_path=out_path))

    if crypto:
        print(f"downloading {len(crypto)} crypto symbols from Yahoo (slowly) ...", file=sys.stderr)
        frames.append(download_yahoo(crypto, start, interval="1d"))

    prices = pd.concat([f for f in frames if f is not None and len(f)], ignore_index=True)
    if args.tier == "universe" and "volume" in prices.columns:
        prices = prices.drop(columns=["volume"])
    write_prices(prices, out_path)
    print(f"wrote {out_path} ({out_path.stat().st_size / 1e6:.1f} MB, {len(prices):,} rows, "
          f"{prices['symbol'].nunique()} symbols)", file=sys.stderr)
    if syms:
        got = set(prices["symbol"])
        miss = [s for s in syms if s not in got]
        if miss:
            print(f"  missing {len(miss)} symbols: {miss[:40]}{' ...' if len(miss) > 40 else ''}", file=sys.stderr)

    if not args.no_meta:
        print("fetching market caps ...", file=sys.stderr)
        meta = build_meta(syms if syms else sorted(prices["symbol"].unique()))
        meta_path = args.out / f"{args.tier}_meta.csv"
        meta.to_csv(meta_path, index=False)
        ok = int(meta["market_cap"].notna().sum()) if "market_cap" in meta else 0
        print(f"wrote {meta_path} ({len(meta)} rows, {ok} with market cap)", file=sys.stderr)


if __name__ == "__main__":
    main()
