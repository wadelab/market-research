# Research log

Newest entries at the bottom. Times are UTC.

## 2026-09-24

- 13:24 Session started. Repo was empty (no commits on GitHub, no branches).
- 13:32 Brief received: find assets with a credible 10x path over 1-2 years; deep dives welcome;
  keep notes in the repo; code for deeper analysis is welcome.
- 13:35 Network check: WebSearch works. Direct HTTPS to api.coingecko.com, query1.finance.yahoo.com,
  stooq.com, sec.gov, fred.stlouisfed.org, en.wikipedia.org, api.binance.com, alphavantage.co,
  polymarket.com, fortune.com all denied by the egress proxy (403 on CONNECT). PyPI is allowed.
  Consequence: research is search-summary based; quantitative tooling cannot be run on live data here.
- 13:38 Created repo skeleton. Launched parallel research agents on: base rates, market snapshot,
  crypto, AI/semis second-order, nuclear/energy, quantum+robotics+space, biotech catalysts,
  commodities + leverage mechanics.
- 13:55 Tooling written and tested (11 synthetic-data tests pass): tools/fetch_data.py (tiered
  downloader, run locally), tenx_math.py, tenx_screener.py, btc_cycle.py, watchlist.py.
  Data policy agreed with Wade: small tiers (core, watch) are committed; the universe tier goes to
  Google Drive. First commit pushed to claude/focused-wozniak-b0ya7w.
- 14:02 Constraint hit: the session's WebSearch quota (200 calls) is exhausted. The quantum/robotics/space
  agent reported it first; confirmed directly. Effects: (a) that screen covers quantum fully, robotics
  partly, and space/defence not at all (marked [NOT FOUND] in the file with a to-do list);
  (b) the remaining agents can only finish from material already gathered. Remedy for next session:
  raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION and/or widen network egress so page fetches work.
- 14:58 Wade: always use uv for package management. Added pyproject.toml, uv.lock, CLAUDE.md
  (conventions); removed requirements.txt; all docs now use `uv run`.
- 15:25 All eight screens in. Wrote notes/03-candidates.md (verdict + scored ranking), four deep dives
  (IREN, UBTech, Centrus, Pendle), populated data/watchlist.csv (15 rows, 8 needing verification).
  Verdict: no base-case 10x; best-evidenced names carry ~3-7 % subjective P(10x); regime (Fed hiking,
  10y 5.1 %, CAPE ~41) and the crypto-cycle calendar argue for building the list now and entering in
  tranches on weakness. Options maths says LEAPS only help on <=40-50 % IV names.
- 15:50 Google Drive ruled out as the channel for the universe tier: the Drive connector returns file
  contents inline (base64) and direct Drive downloads are blocked by the egress policy. Switched the
  universe tier to Parquet (zstd; ~9 MB for 5,500 symbols x 626 weeks on synthetic data vs 20 MB gzip
  CSV) so all tiers are committed to git. Market caps for the universe now come from the Nasdaq screener
  in one request (fallback: per-symbol Yahoo). Added tools/common.py (Parquet/CSV I/O); 14 tests pass.
- 16:20 Wade's local run: Yahoo rate-limited everything (core 0 rows, watch 7/114 symbols, no market
  caps) and the universe run died on an SSL error (python.org macOS Python has no root certificates).
  Rewrote tools/fetch_data.py: US equities/ETFs from Stooq's bulk daily zip (one download, cached),
  crypto from Yahoo in small sequential batches with 2-minute back-off and resume, market caps from the
  Nasdaq screener + CoinGecko (one request each), all HTTP via requests + certifi. Split-adjustment
  check on NVDA/TSLA/SMCI. 18 tests pass.
