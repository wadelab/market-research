# market-research

Research programme: identify assets (crypto, equities, other) with a credible path to a
**10x return within 1-2 years** from a start date of **2026-09-24**, and record the evidence
for and against each candidate.

Everything here is research, not advice. The base rate for 10x-in-24-months is low in every
asset class (see `notes/00-base-rates.md`). The goal of this repo is to make the search for
such outcomes evidence-driven and to keep an auditable record of what was believed, when, and why.

## Ground rules

1. **Every factual claim carries a source URL and a date.** Claims that could not be verified are
   marked `[UNVERIFIED]`. Numbers recalled from memory rather than a live source are marked
   `[from memory, verify]`.
2. **Every candidate states what a 10x implies** in market-cap terms, and what would have to be
   true for the market to pay that. If the implied market cap is implausible, the candidate is
   rejected regardless of narrative.
3. **Every candidate has kill criteria**: observable events that would falsify the thesis.
4. **Timestamps on everything.** Prices move; a note without a date is useless.
5. No survivorship-bias-only arguments. "NVIDIA did it" is not evidence that a given stock will.

## Layout

```
README.md                 this file
log.md                    dated running log of work done and decisions taken
notes/00-base-rates.md    what the evidence says about how often 10x-in-2-years happens
notes/01-market-snapshot.md  state of markets at the research start date
notes/02-framework.md     what past 10x-ers had in common; screening criteria
notes/03-candidates.md    consolidated candidate list with scores
notes/themes/             one screen per theme (crypto, AI/semis, nuclear, quantum, biotech, ...)
notes/deep-dives/         one file per asset that survives the screen
notes/TEMPLATE-*.md       templates for theme screens and deep dives
tools/                    Python analysis code (see tools/README.md)
data/                     cached data (CSV/JSON); large files are gitignored
```

## Environment note

This research was started from a sandboxed cloud session whose network policy allows web
*search* but blocks direct fetches from data providers (CoinGecko, Yahoo Finance, Stooq,
SEC EDGAR, FRED were all denied). Consequently:

- Notes cite search-result pages; quotations are as reported in search summaries.
- `tools/` code that downloads price data has been written and unit-tested on synthetic data
  but has **not** been run against live data in this session. Run it locally, or widen the
  environment's network access, and then re-run the screens.
