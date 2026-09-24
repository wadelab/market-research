# Consolidated candidate list

**Date:** 2026-09-24, updated 2026-09-25 with exchange data  **Status:** v1.1. Section 1 still shows
the search-summary market caps the screens used; **section 1a gives the data-verified figures**
(Stooq closes, Nasdaq-screener and CoinGecko caps, 2026-09-24) and section 1b what these names
actually did over the last 24 months. See `04-measured-base-rates.md` for the measured base rates.

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

### 1a. Data-verified prices and market caps (2026-09-24 close; `data/watch_meta.csv`, `data/watchlist.csv`)

| Asset | Close | Market cap | vs. figure used in the screen | 10x implies |
|---|---|---|---|---|
| IREN | $47.05 | $18.5B | screen said ~$17.6B: consistent | $185B |
| UBTech 9880.HK | HK$78.20 | HK$39.4B (~US$5.0B) | screen said HK$46.5B (21 Sep): stock fell further | ~US$50B |
| Centrus LEU | $151.31 | $2.99B | screen estimated ~$3B: confirmed | $30B |
| Pendle | $2.55 | $443M | screen said $415M: consistent | $4.4B |
| Applied Digital APLD | $27.23 | $7.9B | screen said $7.1B | $79B |
| Ethena ENA | $0.22 | $2.2B | consistent | $22B |
| Quantum Computing QUBT | $9.12 | $2.06B | consistent | $21B |
| Cipher CIFR | $18.35 | $7.6B | was [NOT FOUND] | $76B |
| TeraWulf WULF | $16.35 | $8.2B | was [NOT FOUND] | $82B |
| Hut 8 HUT | $102.46 | $12.6B | was [NOT FOUND] | $126B |
| Acumen ABOS | $2.31 | $167M | was memory-only | $1.7B |
| Cartesian RNAC | $7.87 | $238M | was memory-only | $2.4B |
| Kyverna KYTX | $7.07 | $437M | was memory-only | $4.4B |
| Larimar LRMR | $3.87 | $402M | was memory-only | $4.0B |
| General Fusion GFUZ | $8.68 | $552M | was [NOT FOUND] | $5.5B |

Consequences: the three miner conversions are $7.6-12.6B companies, so a 10x needs $76-126B, above
every neocloud precedent; they move to the "2-3x if contracts perform" category with IREN. The four
biotech names are all in the $150-450M bucket, where the pooled measured P(10x in 24 months) is
1.3-2 % unconditionally (`04-measured-base-rates.md` §2), so their 8-12 % subjective estimates
require the catalyst to be genuinely mispriced; the readout outcomes remain unverified.

### 1b. What the 108 screened names did over the last 24 months (from 2024-09-24 close; `data/watch_prices_1d.csv.gz`)

21 of 108 touched 10x from their 24-months-ago close; 11 are still at or above 10x today. This is
**not** a base rate: these names were surfaced by the screens partly *because* they ran. Largest
maximum multiples: Rigetti 74x, AXT 68x, SanDisk 65x, D-Wave 48x, QUBT 38x, Bloom 33x, Planet 24x,
Unusual Machines 22x, Oklo 21x, Ondas 20x, Rocket Lab 20x, Lumentum 17x, Nebius 15x, Navitas 14x,
AAOI 14x, Micron 13x, Hut 8 10.6x, BlackSky 10x, Credo 10x, IonQ 10x, Ouster 10x. Median current
price of those 21 is about half their peak. Bitcoin's maximum was 1.94x, Ethereum 1.82x, Solana
1.71x; Pendle 1.65x (now 0.62x); Ethena 3.9x (now 0.68x). The four deep-dive names' own 24-month
maxima: IREN 8.5x (now 5.2x), Centrus 8.2x (now 2.9x), UBTech 1.8x (now 0.9x), Pendle 1.65x.

**Listed, not scored (data missing or memory-only). Verification queue, in priority order:**

| Asset | Why it is interesting | What is missing |
|---|---|---|
| Cipher (CIFR), TeraWulf (WULF), Hut 8 (HUT) | $3.8-17.7B HPC contracts with Google credit support / Anthropic anchor tenant; caps now known: $7.6B / $8.2B / $12.6B (1a), so 10x implies $76-126B: demoted to 2-3x candidates | balance sheets, contract terms (primary filings) |
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
