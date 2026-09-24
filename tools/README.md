# tools/

Python 3.11+. Package management is **uv**: `uv sync --all-groups` once, then prefix every
command with `uv run`. Dependencies live in `pyproject.toml`; `uv.lock` is committed.

| Script | Purpose | Needs network? |
|---|---|---|
| `fetch_data.py` | Download price histories in three tiers (core / watch / universe) to `data/` | yes (run locally) |
| `common.py` | Read/write long-format price tables (gzip CSV or Parquet) | no |
| `tenx_math.py` | Implied market cap, required CAGR, expected value and Kelly sizing for asymmetric bets | no |
| `tenx_screener.py` | Find every >=10x-within-N-days episode in a price file; base rates by year and cap bucket | no (needs data) |
| `btc_cycle.py` | Bitcoin halving-cycle table and current cycle position | no (needs data) |
| `watchlist.py` | Print the watchlist with implied caps and progress | no (prices optional) |
| `conditional_rates.py` | 3x/5x/10x rates conditioned on prior return and drawdown; buy-and-hold end values | no (needs data) |
| `options_10x.py` | Black-Scholes table: underlying move needed for 10x on long-dated calls | no |

## Data workflow (sandbox cannot reach Yahoo Finance)

1. Locally: `uv run python tools/fetch_data.py --tier core` and `--tier watch`. Both write a few MB of
   gzip CSV to `data/` and are safe to commit. The first run downloads Stooq's bulk US daily database
   (one zip, a few hundred MB) into `data/.cache/` and reuses it; only the ~13 crypto symbols go
   through Yahoo, slowly, to stay under its rate limit.
2. `uv run python tools/fetch_data.py --tier universe` (all US common stocks, weekly closes, 12 years,
   Parquet ~10 MB, built from the same zip; market caps from the Nasdaq screener in one request). Commit it.
   If the zip download fails, fetch `d_us_txt.zip` from https://stooq.com/db/h/ in a browser and pass
   `--stooq-zip <path>`. A UK zip (`d_uk_txt.zip` or `h_uk_txt.zip`) in the same place adds LSE symbols
   (`.L`) to the watch tier and, with `--include-uk`, all UK stocks to the universe tier.
3. Push. The screens can then be re-run in the sandbox:
   ```
   uv run python tools/tenx_screener.py data/universe_prices_1wk.parquet --meta data/universe_meta.csv --out data/tenx_events.csv
   uv run python tools/btc_cycle.py data/core_prices_1d.csv.gz
   uv run python tools/watchlist.py --prices data/watch_prices_1d.csv.gz
   ```

## Tests

`uv run pytest -q` (synthetic data; no network).
