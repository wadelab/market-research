# data/

| File | Tier | Contents | Size | Refresh |
|---|---|---|---|---|
| `core_prices_1d.csv.gz`, `core_meta.csv` | core | 19 symbols, daily closes, 12 y | ~1 MB | monthly |
| `watch_prices_1d.csv.gz`, `watch_meta.csv` | watch | every screened name, daily, 12 y | ~4 MB | monthly |
| `universe_prices_1wk.parquet`, `universe_meta.csv` | universe | all US common stocks, weekly closes, 12 y | ~10-15 MB | quarterly at most (each refresh adds a blob to git history) |
| `watchlist.csv` | - | candidate tracker (hand-edited) | - | - |

All produced by `uv run python tools/fetch_data.py --tier <tier>` (run locally; the sandbox cannot reach the providers).
Equities come from Stooq's bulk daily database (split-adjusted, not dividend-adjusted [verify]); crypto from Yahoo;
market caps from the Nasdaq screener and CoinGecko. Only currently listed symbols are present (survivorship bias).
Long format: `date, symbol, close[, volume]`. Meta: `symbol, market_cap, last_price, shares, ...` as of the download date.
