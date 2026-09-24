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
- 16:40 Stooq refuses the bulk zip to scripts (401). Script now looks for a browser-downloaded
  d_us_txt.zip in ~/Downloads (and copies it to data/.cache/); core/watch fall back to slow Yahoo if
  no zip is present; universe requires the zip.
- 16:55 Wade downloaded d_us_txt.zip and h_uk_txt.zip. Added UK support: '.uk.txt' members map to
  '.L' symbols, intraday files collapse to daily closes, --include-uk adds UK stocks to the universe.

## 2026-09-25

- 00:10 Data landed (core 578 KB, watch 2.1 MB, universe 8 MB Parquet, meta). Quality: split-adjusted
  (NVDA/TSLA/SMCI check pass), 12 years, 5,277 universe symbols, caps for 5,298; 7 watch symbols
  absent from Stooq/Yahoo (APT-USD, GMET.L, HYPE-USD, MNMD, NSCL, SILV, SUI-USD).
- 00:30 Fixed btc_cycle.py (peak searched within 24 months of the halving; cycles before the data
  start are skipped) and added fixed-start-date base rates to tenx_screener.py. 22 tests pass.
- 00:50 Ran the screens. Wrote notes/04-measured-base-rates.md; updated 03-candidates.md (§1a data-
  verified caps, §1b 24-month returns), 01-market-snapshot.md (measured BTC cycle numbers), the four
  deep dives, data/watchlist.csv (real entry prices/caps). Derived tables committed under data/derived/.
- 01:40 Conditional analysis (tools/conditional_rates.py): P(touch 10x in 730 d) is 3.0 % for stocks
  > 80 % below their 3-year high vs 0.13 % for those within 30 % of it (4.0 % for sub-$300M caps),
  but the same cohort's buy-and-hold median end value is 0.56x with 47 % losing half. Regime effect
  confirmed (2020 start 7.5 %, 2022 start 0.3 % for the deep-drawdown cohort).
- 01:55 Wrote notes/05-recommendations.md: small rules-based sleeve; 30/40/30 tranches on a regime
  trigger; mechanical sell rules; tranche-1 names Pendle, UBTech (after unit check), ABOS/RNAC/KYTX/LRMR
  (after readout verification); IREN and miner conversions only on the trigger; Centrus as a 2-3x.
