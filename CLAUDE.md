# Conventions for this repo

- **Package management: always use `uv`.** Run scripts with `uv run python tools/<script>.py ...`,
  tests with `uv run pytest`, and add dependencies with `uv add <pkg>`. Do not use pip or
  requirements.txt.
- Every factual claim in `notes/` carries a dated source; unverified items are tagged
  `[NOT FOUND]` or `[from memory, verify]`. See README.md for the full ground rules.
- Keep `log.md` current: dated entries, newest at the bottom.
- Data policy: `data/core_*` and `data/watch_*` are committed; `data/universe_*` lives in
  Google Drive and is gitignored.
