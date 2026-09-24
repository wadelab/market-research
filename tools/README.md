# tools/

Python 3.11+. Package management is **uv**: `uv sync --all-groups` once, then prefix every
command with `uv run`. Dependencies live in `pyproject.toml`; `uv.lock` is committed.

| Script | Purpose | Needs network? |
|---|---|---|
| `fetch_data.py` | Download price histories in three tiers (core / watch / universe) to `data/` | yes (run locally) |
| `tenx_math.py` | Implied market cap, required CAGR, expected value and Kelly sizing for asymmetric bets | no |
| `tenx_screener.py` | Find every >=10x-within-N-days episode in a price file; base rates by year and cap bucket | no (needs data) |
| `btc_cycle.py` | Bitcoin halving-cycle table and current cycle position | no (needs data) |
| `watchlist.py` | Print the watchlist with implied caps and progress | no (prices optional) |
| `options_10x.py` | Black-Scholes table: underlying move needed for 10x on long-dated calls | no |

## Data workflow (sandbox cannot reach Yahoo Finance)

1. Locally: `uv run python tools/fetch_data.py --tier core` and `--tier watch`. Both write a few MB of
   gzip CSV to `data/` and are safe to commit.
2. Optionally: `uv run python tools/fetch_data.py --tier universe` (all US common stocks, weekly closes,
   12 years; tens of MB). Do not commit; put it in Google Drive and note the path in `data/README.md`.
3. Push. The screens can then be re-run in the sandbox:
   ```
   uv run python tools/tenx_screener.py data/universe_prices_1wk.csv.gz --meta data/universe_meta.csv --out data/tenx_events.csv
   uv run python tools/btc_cycle.py data/core_prices_1d.csv.gz
   uv run python tools/watchlist.py --prices data/watch_prices_1d.csv.gz
   ```

## Tests

`uv run pytest -q` (synthetic data; no network).
