# Consolidated candidate list

**Date:** 2026-09-24  **Status:** v1, built from the eight notes in this directory. Every number
below is copied from a theme note and carries that note's evidence grade; nothing new was sourced
here. Re-run `tools/watchlist.py --prices` once local data is pushed to replace the search-summary
prices with exchange data.

## 0. Verdict first

1. **Nothing on this list is a base-case 10x.** The best-evidenced candidates have a subjective
   P(10x by Sep 2028) of roughly 5-10 %; most are 1-3 %. That is consistent with the base rates in
   `00-base-rates.md` (unconditional 0.1-1 %/y; a disciplined screen lifts it to perhaps 5-10 % in a
   favourable regime). A 20-30-name sleeve should expect 0-3 hits and its return will be set by how
   the misses are handled.
2. **Bitcoin and NVIDIA are not candidates; they are the benchmark for what a candidate looked like
   *before* it 10x'd.** BTC at ~$85.7k (23 Sep 2026) needs ~$17T of market cap for 10x; NVIDIA at
   ~$5.4T needs ~$54T, about 4x all forecast 2027 hyperscaler capex. When they did 10x (BTC Mar 2020
   to Nov 2021, NVIDIA Oct 2022 to mid 2024) each started from a >50 % drawdown *and* had a
   fundamental inflection that consensus had not priced (ETF/institutional bid; data-centre revenue
   +200 %). The analogues today are the names in section 2, not the originals.
3. **The regime is unfavourable for the next few months and the calendar says wait.** The Fed hiked
   on 16 Sep 2026 to 3.75-4.00 % with more priced; the 10-year is 5.1 %, the highest since 2007;
   CAPE ~41; long-semis is the most crowded trade in the fund-manager survey (`01-market-snapshot.md`).
   Historical 10x cohorts started at troughs (H5 in `02-framework.md`), and the crypto cycle's
   historical bottom window is Oct 2026-Jan 2027. The evidence favours building the list now,
   entering in tranches on weakness, and keeping most of the sleeve in cash until either (a) the
   rate cycle turns or (b) a risk-asset drawdown gives the entry the base rates require.
4. **If leverage is used at all, the arithmetic says: 12-month delta 0.2-0.3 calls on a <=40-50 % IV
   name with a specific doubling thesis** (`02b-leverage-mechanics.md`, `tools/options_10x.py`).
   On 80-100 % IV names (most of this list) options add nothing over the stock; 3x ETFs and perps
   are ruled out by variance drag and liquidation probability.

## 1. Scores

Six criteria from `02-framework.md`, 0-3 each, total /18. Evidence grade is the theme note's.
Names with missing market caps or memory-only figures are listed but **not scored**.

| Rank | Asset | Theme | Mkt cap (date) | 10x implies | Size | Inflection | Catalyst | Balance sheet | Narrative | Evidence | **Total** | P(10x) subj. | Deep dive |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IREN (IREN) | AI infra / miner-to-cloud | ~$17.6B (early Sep 2026) | ~$176B | 1 | 3 | 3 | 1 | 2 | 3 | **13** | 5 % | `deep-dives/IREN.md` |
| 2 | UBTech Robotics (9880.HK) | Humanoids | HK$46.5B / ~US$6B (21 Sep 2026) | ~US$60B | 2 | 3 | 2 | 1 | 2 | 2 | **12** | 5 % | `deep-dives/UBTECH.md` |
| 2 | Centrus Energy (LEU) | Nuclear fuel | ~$3B [estimate] (23 Sep 2026) | ~$30B | 1 | 2 | 2 | 2 | 2 | 3 | **12** | 3 % (2-3x: 30 %) | `deep-dives/LEU.md` |
| 4 | Pendle (PENDLE) | DeFi yield | $415M (24 Sep 2026) | $4.2B | 3 | 1 | 1 | 2 | 2 | 2 | **11** | 7 % | `deep-dives/PENDLE.md` |
| 4 | Applied Digital (APLD) | AI data centres | $7.1B (Sep 2026) | $71B | 1 | 2 | 2 | 1 | 2 | 3 | **11** | 3 % | no (single-tenant risk; see ai-semis.md) |
| 6 | Ethena (ENA) | Stablecoins | $2.1B circ. / $3.15B FDV (23 Sep 2026) | $21B / $31.5B | 1 | 1 | 2 | 2 | 2 | 1 | **9** | 3 % | no (USDe supply unverified) |
| 6 | Quantum Computing Inc (QUBT) | Quantum | $1.91B (18 Sep 2026); cash $1.3B | $19B | 2 | 0 | 1 | 3 | 1 | 2 | **9** | 2 % | no (cash floor, no product) |
| 8 | POET Technologies (POET) | Optics/CPO | $1.29B (31 Aug 2026) | $12.9B | 2 | 0 | 1 | 1 | 2 | 2 | **8** | 2 % | no |
| 9 | Eos Energy (EOSE) | Storage | $1.17B (31 Aug 2026) | $12B | 2 | 1 | 1 | 1 | 1 | 1 | **7** | 2 % | no |
| 10 | NANO Nuclear (NNE) | SMR | $0.98B (21 Aug 2026) | $10B | 2 | 0 | 1 | 1 | 1 | 0 | **5** | 2 % | no |

**Listed, not scored (data missing or memory-only). Verification queue, in priority order:**

| Asset | Why it is interesting | What is missing |
|---|---|---|
| Cipher (CIFR), TeraWulf (WULF), Hut 8 (HUT) | $3.8-17.7B HPC contracts with Google credit support / Anthropic anchor tenant vs probably $5-15B caps; the sub-sector most likely to hold a 10x if the contracts perform (ai-semis.md §3.2) | market caps, balance sheets, contract terms (primary filings) |
| Acumen (ABOS), Cartesian (RNAC), Kyverna (KYTX), Larimar (LRMR) | Small-cap binary readouts/PDUFAs inside the window; buyout comps support 10x arithmetic (biotech.md) | all prices/caps; **2026 readout outcomes** (several may already be resolved) |
| General Fusion (GFUZ) | ~$1B SPAC; fusion peer TAE implied ~$3B on zero revenue; LM26 results | current price, redemptions, LM26 date |
| Lithium restart juniors (Core Lithium, ioneer, Sigma), PGM developers (PLG, Bravo), silver explorers (Dolly Varden, Abra), tungsten/antimony (Guardian, Larvotto) | Cyclical-trough or policy-driven set-ups where a sub-$500M developer re-rates to NAV (commodities-metals.md) | everything: all figures are from memory |
| Space / defence (AST SpaceMobile, Rocket Lab, Redwire, Intuitive Machines, drones, European defence) | SpaceX IPO proxies; European rearmament | **not researched at all** (search quota) |

## 2. What the four deep-dive names have in common, and what they do not

Common: a reported (not guided) revenue inflection or a contracted revenue step-up; a dated
checkpoint inside 15 months; a market cap where 10x has a sector precedent. Not common: none has a
clean balance sheet *and* a small cap *and* high-grade evidence at once. IREN and Centrus have the
evidence but 10x needs a very large cap; UBTech and Pendle have the size but the numbers are
second-hand.

## 3. Rejected outright (one line each; details in the theme notes)

- BTC, ETH, SOL, NVDA, Micron, SK hynix, SanDisk, Arm, Marvell, Vertiv, Bloom, CoreWeave, Credo,
  Astera, IonQ, Quantinuum, D-Wave, Rigetti, Infleqtion, Symbotic, Oklo, GE Vernova, Cameco, UEC,
  Hyperliquid, MicroStrategy, Coinbase, Robinhood, MP Materials, Sibanye, silver producers, royalty
  companies: **10x implies a market cap with no precedent or no revenue path.**
- Sprott uranium trust, oil/gas/LNG/coal/shipping, leveraged ETFs, perps, Bitcoin treasury
  companies: **instrument arithmetic rules out 10x** (needs ~$900/lb uranium; variance drag;
  liquidation; mNAV below 1).
- Serve Robotics, Richtech, Horizon Quantum, Arqit, Navitas (stale data), Ambarella (no data):
  **no inflection, or narrative already spent.**
- Compass Pathways, MindMed, uniQure, Stoke, Kailera, Capricor, Kodiak: **cap already too large for
  10x, or readout timing outside the window** (several are good 2-3x set-ups).

## 4. Kill criteria at portfolio level

- BTC weekly close < ~$58k (June 2026 low): the "shallow bear" thesis is wrong; cut crypto beta.
- A CoreWeave or Nscale credit event: contagion through the neocloud financing chain hits IREN,
  APLD and the miner conversions together (they are one thesis, not four).
- Fed funds above 4.5 % with 10-year above 5.5 %: the regime for unprofitable growth is closed; stop
  adding.
- Any candidate breaching its own kill criteria: exit, do not average down, log it.
