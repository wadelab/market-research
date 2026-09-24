# Recommendations

**Date:** 2026-09-25  **Basis:** notes 00-04, `data/derived/`, `tools/`. This is research, not
personalised financial advice; it states what the evidence supports and where the author would act.

## 0. The recommendation in one paragraph

Run the 10x objective as a small, rules-based speculative sleeve, not as a portfolio strategy, and do
not deploy most of it yet. Our own data (5,277 US stocks, 2015-2024) put the unconditional chance of a
stock touching 10x within two years at 0.6 % per year. The only condition that lifts that by more than
an order of magnitude is buying names already down more than 80 % from their 3-year high (3.0 %;
4.0 % for sub-$300M caps), and buying them in a post-crash year (2019, 2020, 2023: 4-8 % for the
deep-drawdown cohort) rather than a late-cycle one (2018, 2021, 2022: 0.3-1.9 %). Even in the best
cohort, buy-and-hold **loses** money in median (end value 0.56x, 47 % lose half): the whole edge is
in selling into strength. September 2026 is a late-cycle start: the Fed hiked on 16 Sep, the 10-year is
5.1 %, CAPE is ~41, and crypto is 12 months past its top. So: build the list now, put a minority of the
sleeve into the few names that have a dated catalyst *and* a small cap *and* a deep drawdown, hold the
majority for a defined trigger, and run mechanical sell rules from day one.

## 1. The evidence that drives this (all measured, all survivor-biased upward)

| Condition at a 1 Jan start, pooled 2016-2024 | n | P(touch 3x) | P(touch 10x) | Median end value (hold 2 y) | P(end < 0.5x) |
|---|---|---|---|---|---|
| Down < 30 % from 3-y high | 15,855 | 3.1 % | 0.13 % | 1.11x | 8 % |
| Down 30-60 % | 6,089 | 8.3 % | 0.34 % | 1.02x | 17 % |
| Down 60-80 % | 2,588 | 16.2 % | 1.2 % | 0.87x | 29 % |
| **Down > 80 %** | 2,768 | **21.7 %** | **3.0 %** | **0.56x** | **47 %** |
| Down > 80 %, cap < $300M | 996 | 30.5 % | 4.0 % | | |
| Down > 80 %, cap >= $2B | 780 | 10.3 % | 1.9 % | | |

Regime matters as much as drawdown: P(10x) for the down >60 % cohort was 7.5 % (2020 start),
3.8 % (2019), 2.0 % (2024), 1.3 % (2023), but 0.3 % (2022) and ~1 % (2016-2018). Source:
`data/derived/conditional_rates.csv`, `04-measured-base-rates.md`.

## 2. Things the evidence says are bad ideas

1. **Buying Bitcoin, NVIDIA or any $10B+ name for a 10x.** P(10x) for $2B+ caps not in drawdown:
   0.08 % per two-year window. Bitcoin's peak multiple from each halving has fallen 30x, 7.9x, 1.9x.
2. **Leverage on high-volatility names.** At 80-100 % implied volatility a 12-month call needs
   +224 % to +551 % on the underlying to return 10x; 3x ETFs lose ~98 % over two flat years at 80 %
   volatility; 3x perpetuals were liquidated ~half the time within a year (`02b-leverage-mechanics.md`).
3. **Buy-and-hold in the deep-drawdown cohort.** Median outcome is a 44 % loss.
4. **Chasing the 2024-26 winners** (quantum, Bloom, SanDisk, the miner conversions). They are the
   "already 10x'd" cohort; the median post-peak outcome across 951 such episodes is 17 % of peak.
5. **Sizing any single name above a few percent of the sleeve.** Kelly at the probabilities above is
   1-5 %; at P(10x) = 5 % with 55 % chance of an 80 % loss, expected value is roughly zero.
6. **Deploying the whole sleeve in a hiking cycle at CAPE 41.** The closest analogue start (2022) had
   the worst 10x rate in the sample.

## 3. Sleeve design

- **Capital:** only money whose total loss is acceptable. Expected value is near zero before the
  sell discipline and modestly positive with it; variance is enormous either way.
- **Breadth:** 15-25 names across at least six *distinct* theses. Correlated themes (AI infrastructure,
  miner conversions, neoclouds) count as one bet; they will 10x together and die together.
- **Entry gates (all required):** cap <= $2B (prefer < $500M); down > 60 % from 3-year high; cash runway
  >= 18 months or profitable; a dated catalyst inside 12 months; a written kill criterion.
- **Tranches:** 30 % of the sleeve now (section 5), 40 % on the regime trigger (section 4), 30 % held
  for a second leg down or for names the trigger surfaces.
- **Sell rules, mechanical, written before entry:** sell one third at 3x, one third at 5x, run the
  remainder with a 40 % trailing stop from its peak; exit in full on any kill-criterion breach; never
  average down. These rules convert "touched 10x" (3-4 %) into realised gains; without them the
  measured median is a loss.
- **Accounting:** log every entry, exit and thesis change in `log.md`; compute the realised hit rate
  after 20 completed positions; stop the programme if it is below the break-even rate (~9 % of names
  reaching 10x, or the equivalent in 3-5x partial exits).

## 4. Timing: the regime trigger

Deploy tranche 2 when **any two** of the following hold; deploy tranche 3 on a further leg down:

- The Fed's first cut, or an explicit pause with the 10-year below 4.5 %.
- Russell 2000 down >= 25 % from its high, or the small-cap 3-year-drawdown cohort (down > 60 %)
  exceeding 1,500 names (it was 1,365 at the Jan 2024 start; check with `conditional_rates.py`).
- Bitcoin closing below the June 2026 low ($58,559) and then reclaiming it, inside the historical
  Oct 2026-Jan 2027 bottom window; crypto Fear & Greed below 20.
- A neocloud credit event (CoreWeave or Nscale) that reprices AI infrastructure by 50 % or more.

## 5. Specific names, tranche 1 (now), in order of conviction

Sizes are in "units"; one unit is about 3-5 % of the sleeve. Prices and caps are 2026-09-24 closes.

| # | Name | Why now | Gate before buying | Size | Kill criteria |
|---|---|---|---|---|---|
| 1 | **Pendle (PENDLE)**, $2.55, $443M | Smallest cap on the list; 10x = $4.4B, ordinary for DeFi; 63 % below its Dec 2024 high (the -80..-60 % bucket); dated catalysts (GENIUS Act 18 Jan 2027; cycle-bottom window) | Check unlock schedule and fees-vs-revenue definition (deep dive §"What 10x implies") | 1 | BTC weekly close < $58.5k; TVL < $600M or revenue < $10M for two months; a US stablecoin-yield ban |
| 2 | **UBTech (9880.HK)**, HK$78.20, ~US$5.0B | Revenue doubled, humanoid segment +1,445 %, stock 50 % below its Oct 2025 high; the only listed humanoid pure play of size | **Read the H1 2026 interim report first**: what counts as a "full-size unit" (RMB 37k/unit implied); segment gross margin; cash | 1 | Humanoid growth < +50 % in any half; negative humanoid gross margin two halves; placing at > 15 % discount; units include toys |
| 3 | **Acumen (ABOS)**, $2.31, $167M | Sub-$200M Alzheimer's antibody with a Phase 2 readout in the window; if trading near cash, the failure branch is cushioned; the reader can judge the science | Confirm cash vs cap, the ALTITUDE-AD readout date, and that the readout has not already happened | 0.5 | iADRS miss with no biomarker signal; ARIA-E >= 12 %; cash < 12 months |
| 4 | **Cartesian (RNAC)**, $7.87, $238M | mRNA CAR-T in myasthenia gravis; Phase 3 in 2026; natural buyout | **Warning:** stock is -51 % over 24 months; check whether AURORA already read out and how | 0.5 | AURORA miss; cap > $1.5B when checked |
| 5 | **Kyverna (KYTX)**, $7.07, $437M; **Larimar (LRMR)**, $3.87, $402M | Registrational/PDUFA catalysts inside the window at sub-$500M caps | Verify KYSA-8 outcome and BLA status (KYTX); BLA acceptance (LRMR) | 0.5 each | per `themes/biotech.md` |

Tranche 1 is deliberately small (about 4 units) because none of these passes every gate today: the
biotech readouts are unverified and UBTech needs the unit check.

## 6. Names for tranche 2 (on the trigger), and names to leave alone

- **IREN** ($47.05, $18.5B): the best fundamental inflection on the list ($4B contracted annualised
  revenue due by 31 Dec 2026) but 10x needs $185B. Buy only after a 40 %+ fall or once the Dec 2026
  checkpoint is met at a lower price; treat as a 2-3x with a 10x tail.
- **Applied Digital, Cipher, TeraWulf, Hut 8** ($7.6-12.6B): same thesis as IREN, worse balance
  sheets, single-tenant risk. One position at most, and only on the credit-event trigger.
- **Centrus (LEU)** ($151.31, $2.99B): high-quality 2-3x; already had its momentum 10x (8.2x to
  Oct 2025, now 35 % of that). Belongs in a quality sleeve, not this one.
- **Quantum (QUBT and peers), NANO Nuclear, General Fusion, Eos:** no product, no revenue, or no
  evidence; narrative already spent. Leave alone.
- **Bitcoin, Ethereum, Solana:** not 10x candidates; a 1.5-2x cycle play at best if the June low holds.
- **Leveraged instruments:** only 12-month delta 0.2-0.3 calls on a name with <= 40-50 % implied
  volatility and a specific doubling thesis; nothing on the list qualifies today.

## 7. How to generate tranche-2 candidates when the trigger fires

The price side is now automated. Run:

```
uv run python tools/conditional_rates.py data/universe_prices_1wk.parquet --meta data/universe_meta.csv
```

and screen the universe for: approximate cap $50-500M, down > 80 % from the 3-year high, price >= $1,
then apply the fundamental gates by hand (runway, revenue inflection, catalyst). Expect roughly 1,000
names to pass the price screen in a crash and 30-50 to pass the fundamentals; take 15-25 across
distinct theses.

## 8. What would change these recommendations

- A first rate cut with the 10-year below 4.5 %: move to tranche 2 without waiting for the other
  triggers.
- Verified positive biotech readouts: the name becomes a 2-3x follow-through, not a 10x; reduce.
- Delisted-stock data (CRSP) showing the true deep-drawdown 10x rate below 1.5 %: halve the sleeve.
- A demonstrated realised hit rate above 9 % after 20 positions: the process has an edge; scale up.

## 9. Bottom line

The single best-odds route to a 10x from here is not a stock or a coin; it is a **procedure**: wait for
the regime trigger, then buy a basket of 15-25 sub-$500M names down more than 80 % from their highs
with surviving balance sheets and live catalysts, and sell into strength mechanically. Expect one to
three of them to touch 10x, fewer than one to finish there, and the sleeve's return to be set by the
sell rules. Until the trigger, hold a small tranche 1 (Pendle; UBTech after the unit check; the
biotech names only after their readouts are verified) and keep the rest in cash.
