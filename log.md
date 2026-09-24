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
