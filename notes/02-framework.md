# Screening framework for 10x-in-24-months candidates

**Date:** 2026-09-24  **Status:** draft v1 (hypotheses H1-H5 to be checked against `00-base-rates.md`
and against `tools/tenx_screener.py` output once price data is loaded)

## 1. Hypotheses about what past 10x-ers had in common

These are stated as testable hypotheses, not facts. Each has an explicit test.

| # | Hypothesis | Test | Status |
|---|---|---|---|
| H1 | **Starting size.** Most 10x-in-24-month equities started below ~$5B market cap; most 10x tokens below ~$1B. Large-cap exceptions (NVIDIA from its Oct 2022 low, Bitcoin from Mar 2020) needed a regime-level narrative *and* a fundamental inflection. | `tenx_screener.py` cap-bucket histogram on the universe tier | untested |
| H2 | **Fundamental inflection.** Durable 10x-ers showed revenue growth acceleration (>50 %/y) or a realised adoption event; narrative-only 10x-ers (quantum late 2024, SMR developers 2024-25) gave most of it back within 12 months. | Compare drawdown-after-peak between "revenue-inflection" and "narrative-only" episodes in `tenx_events.csv` | untested |
| H3 | **Liquidity regime.** 10x episodes cluster in periods of expanding liquidity and falling rates (2020-21, 2023-24) and are rare in tightening years (2022). | Year-by-year base rate from `tenx_screener.py` vs Fed funds path | untested |
| H4 | **Reflexivity.** Low float, high short interest, heavy retail/options participation amplify moves. | Not testable with current data; qualitative | untested |
| H5 | **Entry point is the trough.** The 24-month window that contains a 10x usually opens near a sector or market low, not near a high. | Distribution of `entry_date` relative to prior 12-month drawdown in `tenx_events.csv` | untested |

## 2. Gates (a candidate must pass all)

| Gate | Rule | Rationale |
|---|---|---|
| G1 Size | Equity market cap <= $5B; token FDV <= $2B with FDV/circulating cap <= 2 | H1; and unlock overhang kills token returns |
| G2 Precedent | The implied 10x market cap has a precedent in the sector, or the note explains why not | Stops "$150B quantum software company" theses |
| G3 Inflection or dated catalyst | Either a visible fundamental inflection now, or a dated binary catalyst inside 12 months | H2 |
| G4 Balance sheet | Cash runway >= 18 months at current burn, or profitable; dilution history recorded | Dilution is how the last cycle's 10x-ers were monetised by management |
| G5 Liquidity | Tradable: average daily value > $5M (equities) / > $10M (tokens) | Must be able to exit |
| G6 Falsifiable | Kill criteria written down before entry | Discipline |

## 3. Scoring (0-3 each, total /18)

1. Size headroom (how far below the sector precedent cap)
2. Inflection evidence (reported numbers, not guidance)
3. Catalyst clarity (dated, binary, material)
4. Balance sheet / dilution risk (inverse)
5. Narrative and rotation fit (is capital already moving toward this theme, or away?)
6. Evidence quality (primary filings > financial-data sites > aggregators; nothing from memory counts)

Scores are recorded in `03-candidates.md`. A score is a ranking device, not a probability.

## 4. Portfolio arithmetic (from `tools/tenx_math.py`)

Illustrative, not a recommendation. Assume each bet has P(10x) = 8 %, P(lose 80 %) = 60 %, else flat.

```
$ python tools/tenx_math.py ev --p10x 0.08 --ploss 0.6 --loss 0.8
EV per unit staked: +0.24  (break-even P(10x) = 0.053 at P(loss)=0.6)
Kelly fraction: 0.049 of sleeve (half-Kelly 0.025)
$ python tools/tenx_math.py portfolio --n 10 --p 0.08
P(at least one 10x in 10 bets at p=0.08): 0.566
```

Reading: with those (generous) odds, expected value is positive, Kelly says ~5 % of the
speculative sleeve per bet, and a ten-bet sleeve still has a 43 % chance of containing no 10x at
all. The sleeve is money one can lose in full. If the true P(10x) is nearer 3 % (see base rates),
EV is negative and the correct position size is zero.

## 5. Process

- Re-screen each theme quarterly; re-check catalysts monthly; enforce kill criteria mechanically.
- Every entry, exit and thesis change is logged in `log.md` with a date and the evidence.
- No candidate is promoted to a deep dive without at least one primary-source figure
  (filing, exchange data, protocol dashboard) confirming the market cap and the key metric.
