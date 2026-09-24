# Conventions for this repo

- **Package management: always use `uv`.** Run scripts with `uv run python tools/<script>.py ...`,
  tests with `uv run pytest`, and add dependencies with `uv add <pkg>`. Do not use pip or
  requirements.txt.
- Every factual claim in `notes/` carries a dated source; unverified items are tagged
  `[NOT FOUND]` or `[from memory, verify]`. See README.md for the full ground rules.
- Keep `log.md` current: dated entries, newest at the bottom.
- Data policy: all three data tiers are committed (`core_*`, `watch_*` as gzip CSV; the universe
  tier as Parquet, ~10-15 MB). Refresh the universe tier at most quarterly. Google Drive is not used:
  the sandbox cannot download from it.
