# Research to-do (gaps to close in the next session)

Ordered by expected value of the information. Each needs web search (budget exhausted on
2026-09-24) or a primary-source fetch (blocked by egress policy in the sandbox).

## Blocking gaps
1. **Space / defence screen** not researched at all (search budget ran out). Priorities:
   SpaceX/Starlink IPO status and timing; listed proxies; AST SpaceMobile, Rocket Lab, Planet,
   Redwire, Intuitive Machines, Firefly; drones (AeroVironment, Red Cat, Ondas, Kratos);
   European defence small caps.
2. **Primary-source confirmation** of every market cap and price used in the theme screens
   (all currently from search summaries). Once local data is pushed (`tools/fetch_data.py`),
   `tools/watchlist.py --prices` replaces the search-summary numbers.
3. **UBTech (9880.HK)** unit definition: check the H1 2026 interim report for what counts as a
   "full-size humanoid" unit (16,123 units vs RMB 590M revenue implies ~RMB 37k/unit).

## Data to load (run locally, see tools/README.md)
- `uv run python tools/fetch_data.py --tier core` and `--tier watch` -> commit.
- `uv run python tools/fetch_data.py --tier universe` -> Google Drive. Then run `tenx_screener.py` to
  replace the base-rate hypotheses in `02-framework.md` with measured rates.

## Nice to have
- Prediction-market odds (Polymarket/Kalshi) for dated catalysts on the watchlist.
- Options implied vols for the equities on the watchlist (to size LEAPS alternatives).
- Token unlock schedules for any crypto candidate (FDV/circulating overhang).
