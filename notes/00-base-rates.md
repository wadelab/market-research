# 00 — Base rates: how often does an asset return 10x within 24 months, and what did the ones that did have in common?

**Date:** 2026-09-24  **Author:** research agent  **Status:** draft, search-summary based (see "Method and limits")

**One-paragraph answer.** No published study measures "10x within 24 months" directly for either
stocks or tokens. Everything below is triangulated from (a) peer-reviewed work on the skewness of
stock returns, (b) practitioner screens over 5–10 year windows, (c) aggregator counts of extreme
gainers in specific years, and (d) verified single-name examples. The triangulation says: over a
*decade*, roughly 1–3% of US large-cap stocks and ~7–10% of S&P 500/Nasdaq constituents in an
unusually good decade rise 10x [16][19][20][22]; over *five* years the count in the Russell 3000 was
about 20 names, i.e. <1% [18]; over *two* years the count is not measured anywhere I could find, and my
estimate is **~0.1–1% of listed US operating companies in a favourable window, and near zero in an
unfavourable one** (see §1.4 — an estimate, not a measurement). In crypto the numerator is larger
in a bull cycle but the denominator is dominated by tokens that die: >50% of all tokens tracked
since 2021 were dead by end-2025 [80][81], and ~98% of new Solana memecoins never even reach a
liquid market [84][85]. Almost every celebrated 10x is measured trough-to-peak, which is not a
return anyone earns from a random start date.

Evidence-quality tags used throughout: **[A]** peer-reviewed or primary document with the exact
figure; **[B]** reputable secondary source or practitioner study with a stated method; **[C]**
aggregator, press or search-summary figure that I could not open and check; **[M]** from memory,
not verified in this session. Anything tagged [C] or [M] should be re-checked before it is used
in a decision.

---

## Method and limits

- Only web *search* was available; no page could be opened. Figures are as reported in search
  summaries of the cited pages. Where the summary was internally inconsistent I say so.
- The session's search budget ran out before I could verify several single-name price paths
  (AppLovin, Palantir, SMCI's 2023 low, Oklo, Robinhood, Hyperliquid, Zcash, SanDisk, AXT) and
  before I could find any academic survival analysis of tokens or Bessembinder's Part IV findings.
  These are listed in §7 and tagged [M] or [C] in the text.
- "10x" here means price multiple ≥10 (i.e. ≥ +900%). Where a source says "1,000%" I treat it as
  11x; the difference does not matter for base rates.

---

## 1. Equities

### 1.1 Skewness: the structural reason 10x is rare (Bessembinder)

**Bessembinder (2018, *J. Financial Economics* 129:440–457), "Do stocks outperform Treasury bills?"**
[1][2][3] — CRSP, all US common stocks 1926–2016, ~26,000 stocks. Findings as reported [A]:

- Four in seven stocks have a lifetime buy-and-hold return below one-month T-bills [1][4].
- The median stock's lifetime return is negative (≈ −3.7% as quoted in [106], a secondary
  summary; the paper's own figure should be checked against [2]) [B].
- The best-performing ~4% of stocks account for the entire net wealth creation of the US market
  over T-bills; 0.33% (≈90 firms) account for over half of it [1][2][106].
- Of the ~26,000 stocks, 9,187 were delisted, with a median lifetime buy-and-hold return of
  −91.95% (figure as reported in the search summary of [1]/[2]) [B]. This is the relevant number
  for the *failure* side: the modal fate of a listed stock that leaves the exchange is near-total loss.

**Bessembinder, Chen, Choi & Wei (2023, *Financial Analysts Journal* 79(3):33–63), "Long-term
shareholder returns: evidence from 64,000 global stocks"** [5][6][7] — Jan 1990–Dec 2020 [A]:

- 55.2% of US and 57.4% of non-US stocks underperformed one-month US T-bills over the sample.
- The top 2.4% of firms (1,526 companies, per the URL slug of [105]) account for all $75.7 trillion
  of net global wealth creation; outside the US, 1.41% of firms account for all $30.7 trillion.

**Bessembinder (2024, SSRN 4897069), "Which US stocks generated the highest long-term returns?"**
[8][9] — 29,078 stocks, Dec 1925–Dec 2023 [A]:

- 51.6% had negative cumulative returns over their lives.
- 17 stocks returned >5,000,000% (>$50,000 per $1); Altria is the top at 265,000,000%.
- Highest *annualised* compound return for any stock with ≥20 years of data: NVIDIA, 33.38%/yr.
  Note what this implies: the single best long-run compounder in a century did ~33%/yr; a 10x in
  24 months is 216%/yr. Two-year 10x events are not "compounding"; they are re-ratings.

**"Extreme Stock Market Performers" I–IV (2020, SSRN 3657604/09/11/12)** [10][11][12][13] — decade
horizons, all US stocks since 1950 [A for the findings quoted; I could not retrieve Part IV's
results, see §7]:

- Part I: among the 100 most successful stock-decades, shareholders sat through an average
  drawdown of 32.5% lasting 10 months *during* the winning decade, and an average drawdown of
  51.6% lasting 22 months in the *preceding* decade (Netflix: −79.9% in the 2010s) [10].
  Implication: "left for dead first" is a genuine statistical regularity, not just folklore.
- Part II: technology stocks are *more* likely to appear on the worst-performer lists than the
  best; telecom, healthcare/pharma and energy are over-represented among best decade performers
  (sample through 2019) [11]. The "it must be tech" prior is not supported historically.
- Part III: extreme performers show rapid asset growth, strong cash accumulation, higher
  profitability despite higher R&D, and — most important — high net-income growth; top performers
  by *rate of return* are younger and more volatile than ordinary firms; monthly return skewness
  has no explanatory power for who ends up extreme [12][108].

Baillie Gifford's summary of this body of work [14] and the Robeco interview [15] are convenient
secondary sources; they add no new numbers.

### 1.2 Frequency of 10x over 5–10 years (practitioner screens)

| Window | Universe | Count / share that did ≥10x | Source | Quality |
|---|---|---|---|---|
| Apr 2013–Apr 2023 (10y) | Russell 1000 | 33 names (~3.3%); top: NVDA +8,833%, TSLA +6,304%, PLUG +5,477% | Bespoke [16][17] | B |
| 2016–2025 (~9y) | Russell 3000 | 22 names (≈0.73%) | ActivTrades citing an unnamed screen [19] | C |
| 5-year window (date not stated in summary) | Russell 3000 | 20 names | Seeking Alpha screen [18] | C |
| Decade to 2021 | NSE 500 (India) / Nasdaq Composite / S&P 500 / China | 20% (80 stocks) / 10% / 7% / 3% rose >900% | Bloomberg [22] | B |
| 20 years | NSE 500 | >50% delivered 10x (Goldman Sachs, as reported) | Business Standard [23] | C |
| 10 years, generic | S&P 500 | "only 1–2% become 10x in a decade"; 10x/10y ≈ 26% CAGR | QuantifiedStrategies [20] | C |
| unspecified | US stocks | 1 in 4,263 (0.02%) chance of a 40-bagger | MicroCapClub [21] | C |

Inconsistencies to note: the 22-of-Russell-3000 figure [19] cannot be reconciled with 33-of-Russell-1000
[16] unless the windows and constituency rules differ (they do: 2016–25 vs 2013–23, and probably
current vs. start-of-period membership). Treat all of these as order-of-magnitude: **~1–3% of
large caps per decade in a normal decade, ~7–10% in the 2011–21 bull decade, and <1% of the
full Russell 3000 over 5 years.**

The Bloomberg piece also reports fundamentals for the 80 Indian 10-baggers: ~90% grew revenue
>10% CAGR, 70% grew profit >20% CAGR, median sales CAGR 21%, median profit CAGR 31% [22] [B].
Similar figures (10x stocks' median earnings growth 39% vs 12.6% for the universe) appear in
[19]/[24] without a clear primary source [C].

### 1.3 Practitioner "multibagger" studies (what they found, and why they are biased)

**Alta Fox Capital, "The Makings of a Multibagger" (2020)** [25][26][27][31] — this exists; it is a
~645-page case study of 104 stocks that returned >350% between June 2015 and June 2020, drawn
from developed-market (North America, Western Europe, Australia) stocks with starting market cap
$150M–$10B, excluding energy, materials and financials. Average return of the set: 922% [27] [B].
Findings as reported by the study and its reviewers [27][28][29][30] [B]:

- 84% of the winners started below $2B market cap; starting market cap had the strongest
  (negative) correlation with total return of any driver examined (−0.51), ahead of revenue growth
  (+0.38), EBITDA growth (+0.28) and multiple expansion (+0.26) [29].
- Return decomposition, *mean*: EBITDA growth 59.8% of TSR, multiple expansion 44.8%, dividends
  1.6%. *Median*: EBITDA growth 33.7%, multiple expansion 65.7% [29]. So in the typical winner the
  re-rating mattered more than the earnings.
- 82% traded below 3x sales, 20x EBITDA *or* 30x P/E at the start [29] — a weak filter because of
  the "or".
- Acquisitions were a common contributor; the authors warn explicitly against relying on low
  multiples; only 32% of winners were US-listed, which they read as the US being under-represented
  relative to its share of the universe [27].

Bias: this is a study of winners only. It tells you what winners looked like, not P(win | look).
Small starting market cap being the best "predictor" among winners is partly mechanical: a 10x
from $150M needs $1.35B of new market value; from $10B it needs $90B.

**Chris Mayer, *100 Baggers* (2015)** [32][33][34][109] — 365 US stocks that returned 100x
between 1962 and 2014, extending Thomas Phelps' *100 to 1 in the Stock Market*. Median time to
100x: 16 years; median starting sales ≈ $170M, median starting market cap ≈ $500M [32][33] [B].
Screening themes: high ROE, meaningful insider ownership, long growth runways. Same winners-only
bias as Alta Fox, and the horizon (16 years) is an order of magnitude longer than ours.

**StableBread's "446 global 10-baggers"** [24] exists; I could not retrieve its method [C].

### 1.4 Actual counts of 10x in ≤2 years — what could and could not be found

No source gives a clean count of US stocks that rose 10x within a 24-month window. What exists:

- **2020:** "roughly 1 in 10 NYSE/Nasdaq stocks with market cap ≥$300M gained ≥100%" — this
  figure appeared in the search summary of a query whose results included [35]; I could not
  confirm which page it came from [C]. That is a *doubling* rate, not a 10x rate.
- **2021 (meme episode):** as of 4 Feb 2021 there were 16 stocks up ≥100% YTD, and about a third of
  the ~50 stocks on Robinhood's restricted list had doubled or more [36] [B]. GameStop and AMC are
  each described as having been up >1,000% at points in 2021 [36 and related summaries] [C];
  calendar-2021 close-to-close, GME was roughly +690% and AMC roughly +1,180% [M].
- **2023–2025 (AI cycle):** no count found. A Nasdaq/Yahoo piece in the [37] cluster reports SMCI
  "up over 800% since early 2023" [C]. The verified single names in §3 (NVDA, SMCI, CVNA, APP, PLTR,
  MSTR, plus RKLB and the quantum names from mid-2024) give a **lower bound of roughly 8–12 US
  stocks with >$1B market cap that did ≥10x within 24 months somewhere in 2023–2025**, out of
  ~4,000+ listed operating companies, i.e. ≥0.2–0.3%. The true figure including micro-caps is
  higher but unmeasured.
- **2025 calendar year:** Morningstar's best S&P 500 performers were WDC +290.7%, MU +247.7%,
  STX +224.5%, HOOD +209.8%, WBD +173.8%, NEM +173.7% [38] [B]. No S&P 500 stock did 10x in
  calendar 2025. SanDisk (spun out of WDC in Feb 2025) is reported at +692.6% YTD in one 2025
  report and "+5,000% since spin-off" in another [39] — these two figures are not consistent with
  each other unless measured at very different dates; verify [C].
- **2026 YTD to 21 Sep 2026:** StockTitan lists MGRT +1,533%, ANL +1,028%, XHLD +737% YTD [40];
  trailing 52 weeks: MGRT +2,757%, SNDK +1,529%, AXTI +1,364% [41]. Best one-year S&P 500 names:
  SNDK +536%, MRNA +399%, DELL +306%, MU +225%, STX +184% [42][43] [C]. So over the most recent
  24 months only a handful of names in the investable (>$1B, liquid) universe did 10x, and the
  top of the YTD list is occupied by tickers (MGRT, ANL, XHLD) that I could not identify or
  verify and that fit the profile of thin-float recent listings [C]. Treat those as untradeable
  at size until checked.

**Estimate (mine, not a measurement):** in a favourable two-year window (2020–21, 2023–25) perhaps
0.2–1% of US-listed operating companies achieve ≥10x trough-to-peak; from a *fixed* start date
(no trough-timing) the share is lower, plausibly 0.1–0.5%; in an unfavourable window (2022–23)
it is close to zero outside micro-caps. To turn this into a number, run the CRSP or full-history
screen described in `tools/` (not possible in this session).

---

## 2. Crypto

### 2.1 Death rates

- **CoinGecko, "How many cryptocurrencies failed?" (Jan 2026)** [80][81][82]: of ~20.2 million
  tokens tracked on GeckoTerminal from mid-2021 to end-2025, **53.2% were dead by 31 Dec 2025**;
  86.3% of all failures occurred in 2025 alone; the population grew from 428,383 (2021) to 20.2M
  (2025) [B]. The search summary also quotes "11.6 million dead", which is inconsistent with
  53.2% × 20.2M ≈ 10.7M; one of the two figures is misquoted — check [80].
- Earlier CoinGecko Q1-2025 report: nearly half of tokens launched since 2021 had died; about
  1 in 4 of them died in Q1 2025 alone [83] [B].
- CoinGecko separately says it has listed >24,000 coins since 2014 [80]; the ~50% death rate for
  that older, curated population is from an earlier CoinGecko piece [M].
- **Solana memecoins / Pump.fun:** graduation to a liquid DEX pool (the minimal bar for a token
  to be tradeable at all) runs at ~1.2–2.0% of launches: 1.4% in one January (1.7M launched,
  24,000 graduated) [84]; 1.15% [85]; 2.01% in the week of 9–15 Mar 2026, a high since Jul 2025
  [86] [B]. Two arXiv papers study this population [87][88]; I could not retrieve their return
  distributions [C].

Denominator warning: "53% of 20 million tokens died" is dominated by zero-effort launches. It is
the right base rate for "buy a random new token"; it is the wrong base rate for "buy a top-100
asset". No academic survival analysis of exchange-listed tokens was found in this session [§7].

### 2.2 Distribution of altcoin returns per cycle

- **2020–21:** CoinDesk's year-end review: most major assets posted triple-digit 2021 returns,
  BTC +66% for the year; total market cap went from <$800B (Jan) to $2.2T (Dec) [69] [B]. No
  source found that counts how many of the Jan-2021 top-100 did 10x. From memory [M]: measured
  Jan-2021 price to 2021 peak, a large minority — perhaps a third to a half — of the Jan-2021
  top-100 (e.g. SOL, ADA, DOGE, MATIC, AVAX, LUNA, FTM, AXS, SAND, BNB) reached ≥10x; measured
  Jan-2021 to Dec-2021 close, materially fewer; BTC and ETH themselves did 2.4x and ~6.7x. **This
  needs to be computed from CoinGecko history; treat as hypothesis.**
- **2023–25:** the cycle was narrower. Altcoin Season Index peaked at 88 in Dec 2024 but no
  sustained altseason followed; BTC dominance rose from 49% to 65% in 2025 [70][71][72][73] [B].
  "The top 140 tokens averaged a 58% decline from their 7 Dec 2024 peak while BTC was down 3%"
  [70 or 71, per summary] [C]. From memory [M]: from Jan-2023 prices to 2024/25 peaks, perhaps
  10–15% of the Jan-2023 top-100 reached 10x (SOL ~29x, INJ, RNDR, FET, XRP ~10x by Jan 2025,
  HBAR ~10x), while BTC did ~7.6x ($16.5k→$126k) and ETH ~4x — i.e. **Bitcoin itself did not 10x
  in the 2023–25 cycle** [M].
- **2025 calendar year:** CoinGecko's top gainer was MYX Finance +3,358% (launched 6 May 2025 at
  ~$0.097; airdrop-driven), then Zcash +573.7% [74]; BTC and ETH ended 2025 flat-to-down (BTC
  −7.96% YTD, ETH −15.25% YTD at the report date) [74][75][76] [B]. Privacy coins and gold-backed
  tokens led; the largest assets lagged.
- **2026 YTD:** as of 2 Aug 2026 the top-100 averaged −21.25% YTD with only 9% of tracked coins
  positive (52 gainers vs 504 losers) [77] [C]. The "top ROI" entry, YZY +42,730% [77], is almost
  certainly a post-collapse-low artefact (YZY launched in Aug 2025 and crashed [M]); do not use.
  Zcash +135% in September 2026 on a US spot ZEC ETF launch [78 or 79] [C]. A promotional site
  claims BTC went "$60,000 to $85,000 in two weeks" in Sep 2026 [79] [C — unverified].

**Bottom line for crypto:** in a broad altseason (2021) the 10x count among liquid tokens is high
enough that the problem is *selling*, not *finding*; in a narrow cycle (2024–25) 10x was confined
to new launches, memecoins and a few narrative names, while the majority of the top-100 lost value
in USD terms. The most recent 24 months (Sep 2024–Sep 2026) look like the narrow case.

### 2.3 Drawdown side

- "72 of the top-100 coins have fallen ≥90% from their all-time highs" [89] (bear-market piece,
  date not recovered; probably 2022) [C].
- "Over 40% of altcoins trade at or near all-time lows, worse than the previous bear's ~38%
  peak" [90]; "83% of tokens in a bear trend" [91] — 2025/26 pieces [C].

---

## 3. Documented 10x-in-<24-months examples

Multiples are trough-to-peak unless stated, which is the flattering convention. Confidence
refers to the price path as I have it, not to the narrative.

| Asset | Start (date, price) | End (date, price) | Multiple / months | Evidence | Confidence |
|---|---|---|---|---|---|
| Bitcoin | 12 Mar 2020, $3,850 | 10 Nov 2021, $68,789–$69,044 | ~18x / 20 mo | [64][65][66] | High [B] |
| Solana | Jan 2021, ~$1.50 | Nov 2021, ~$260 | ~170x / 10 mo (the summary's "17,100x" is an arithmetic slip; 17,200% = 173x) | [67][68] | High [B] |
| NVIDIA | 13 Oct 2022, ~$108 pre-split (~$10.8 post) [M] | 6 Jun 2024, $1,255.87 pre-split | ~11x / 20 mo; "900% Oct 2022–Jun 2024" per [55] | [53][54][55][56] | Medium (low verified [C], high [M]) |
| Super Micro | Jan 2023, ~$80 pre-split (~$8 post 10:1) [M] | 8 Mar 2024, $122.90 split-adj. | ~15x / 14 mo; +246% in 2023 | [57][58][59] | Medium |
| Carvana | 7 Dec 2022, $3.55 (ATL) | 31 Dec 2024 | +2,527% (26x) 1 Dec 2022–31 Dec 2024; "up >500% in a year" by Jul 2024 | [50][51][52] | High [B] |
| MicroStrategy | 31 Dec 2022 | 20 Dec 2024 | +346% (2023) then +477% (2024) ⇒ 4.46 × 5.77 ≈ 25.7x over 24 months, close-to-close | [61] | High [B] (arithmetic mine) |
| Palantir | Dec 2022/Jan 2023, ~$6 [M] | Dec 2024, ~$76 [M] | ~12x / 24 mo; +380% in 2024 alone | [60] | Medium (2024 leg verified, 2023 leg [M]) |
| AppLovin | Dec 2022, ~$9.5 [M] | Nov 2024, ~$400 [M] | ~40x / 23 mo; #1 US tech stock ≥$5B in 2024 ahead of MSTR | [61][62][63] | Medium (rank verified via [61]; prices [M]) |
| Rocket Lab | 16 Apr 2024, $3.47 (ATL) | 27 May 2026, $151.00 (ATH); +361% in 2024 | 43x / 25 mo; ≥10x was reached well inside 24 months | [48][49] | High [B] |
| Rigetti / D-Wave / QCI / IonQ | mid-Jul 2024 | ~Jul 2026 (two-year trailing) | RGTI ~+1,820%, QBTS ~+1,670%, QUBT ~+1,200%, IONQ ~+400%; from mid-Jul 2024: RGTI ~+1,200%, QBTS ~+1,500%, IONQ >4x | [44][45][46][47] | Medium-high [B] |
| Bitcoin 2022–24 (contrast) | Nov 2022, ~$15.5k [M] | Dec 2024, ~$108k [M] | ~7x — **did not 10x** | — | [M] |

Most recent 24 months (Sep 2024 → Sep 2026), from the sources above: Rocket Lab (≈$7–8 in Sep 2024
[M] → $151 May 2026), the four quantum names, SanDisk (+1,529% trailing 52 weeks to Sep 2026;
spin-off Feb 2025) [41], AXT Inc (+1,364% trailing 52 weeks) [41], and thin-float names MGRT/ANL
[40][41]. Candidates I believe also did it but could not verify [M]: Oklo (~$5–6 in Sep 2024 →
>$150 in late 2025), Robinhood (~$10 in early 2024 → ~$150 by Sep 2025), Bitmine Immersion (2025
ETH-treasury pivot), Hyperliquid's HYPE (launched ~$3–4 in Nov 2024 → ~$50–60 in 2025), Zcash
(2025 rally). Every one of these needs a price check with `tools/` before use.

Two observations that survive the verification caveats:

1. **Six of the nine equity examples first fell 66–99%.** CVNA hit $3.55 from a $370 high; RKLB's
   ATL was $3.47 after a 2021 SPAC; NVDA fell ~66% in 2022; PLTR, APP and MSTR fell 85–90% in
   2021–22 [M for the drawdown figures]. This matches Bessembinder Part I's finding that the best
   decade performers had an average 51.6% drawdown in the preceding decade [10].
2. **All the 2023–25 equity 10x-ers happened with the Fed funds rate at 5.25–5.5%** (Jul 2023–Sep
   2024) [M]. The "you need QE / rate cuts" folklore is not necessary for equities; a revenue
   inflection (NVDA data-centre revenue, SMCI servers, APP's ad engine, PLTR's AIP, CVNA's
   turnaround) or a balance-sheet lever (MSTR's BTC leverage) was sufficient.

---

## 4. Common features: evidence vs folklore

| Feature | What the evidence says | Quality | Verdict |
|---|---|---|---|
| **Small starting market cap** | 84% of Alta Fox winners started <$2B; starting cap was the strongest correlate of TSR (−0.51) [29]; Mayer's 100-baggers had median starting cap ~$500M [32][33]. Counter-example: NVDA started its 10x at ~$270B [M]. | B (winners-only) | Real but mechanical: a 10x needs 10x more new dollars for a big cap. Necessary-ish, not sufficient. |
| **Revenue / earnings inflection** | Bessembinder Part III: net-income growth the strongest characteristic of extreme performers [12]; India 10-baggers median profit CAGR 31% [22]; Alta Fox revenue-growth correlation +0.38 [29]. | A/B (ex post) | Best-supported feature. Problem: it is observed ex post; the 10x happens *while* the inflection is being recognised, not after. |
| **Multiple expansion** | Median Alta Fox winner got 66% of TSR from re-rating [29]. | B | Real and large; essentially unforecastable, which is why narrative and liquidity matter. |
| **Prior collapse ("left for dead")** | Part I: average 51.6% drawdown in the decade before a top decade [10]; 6 of 9 examples in §3. | A/B | Real. But the base rate of recovery among 90%-down stocks is low (delisted median −91.95% [1]); this feature increases payoff size, not hit rate. |
| **Narrative cluster + liquidity regime** | Descriptive only: 2020–21 (QE, retail), Dec 2024 quantum (Google Willow announcement [M]), AI 2023–25. No study found that quantifies it. | C/M | Folklore with face validity. Cannot be used as a screen; can be used as a regime check. |
| **Low float / high short interest** | Asquith–Pathak–Ritter: short-constrained stocks *underperform* by ~215 bp/month equal-weighted (1988–2002) [100]; short interest negatively predicts aggregate returns in 24 of 32 countries [101]; but highly-shorted portfolios "realise extreme gains at the onset of significant short squeezes" [102][104]; squeeze-prone stocks are small, volatile, heavily traded [102]. | A | Negative expected value with a fat right tail. It is a lottery-ticket feature, not a quality feature. |
| **Sector (tech)** | Part II: tech over-represented among *worst* decade performers; best were telecom, healthcare, energy (to 2019) [11]. 2023–25 winners were mostly AI-adjacent [§3]. | A vs C | Historical evidence says no sector prior; recent evidence says the current narrative sector. Do not extrapolate either. |
| **Youth / volatility** | Part III: rate-of-return top performers are younger and more volatile [12]. | A | Real, and it cuts both ways (the same stocks dominate the losers). |
| **Macro (rate cuts / QE)** | Not tested here. 2023–25 equity 10x-ers occurred at 5%+ policy rates [M]; 2020–21 crypto coincided with QE [M]. | M | Folklore for equities; plausible amplifier for crypto; no controlled evidence found. |
| **Acquisitions / capital allocation** | Alta Fox: acquisitions a common contributor [27]. | B | Real for 5-year multibaggers; rarely the driver of a 2-year 10x. |

The honest summary: the features with real evidence (small cap, earnings inflection, prior
collapse, youth/volatility) are **shared by the losers**. They widen the distribution; they do not
shift its mean. The only feature that shifts the mean is the earnings inflection, and it is
generally recognised by the market within the first 2–4x of the move.

---

## 5. The failure side

- **Delisted US stocks:** median lifetime buy-and-hold return −91.95% (9,187 of ~26,000 CRSP
  stocks) [1][2] [B]. 51.6% of all US stocks 1925–2023 had negative cumulative returns [8].
- **SPACs (the closest thing to a "story small cap" cohort):** market-adjusted returns to
  non-redeeming shareholders as of 1 Nov 2021: mean −64%, median −88% (Klausner & Ohlrogge,
  *A Sober Look at SPACs*) [92][93] [A]; mergers completed in 2021 and 2022 lost on average 67%
  and 59% versus the $10 reference [94 or 96, per summary] [B]; PitchBook's de-SPAC index fell
  ~80% Mar 2021–Feb 2023 [94] [B]; Kiesel et al. (2023, *Eur. Financial Mgmt*): 236 de-SPACs
  2012–Jun 2021, 1-year abnormal −14.1%, 2-year −18.0% from announcement [95] [A].
- **IPO cohorts:** ~half of the 100 largest 2021 US IPOs were below offer by Dec 2021 [97]; by
  Aug 2023 only 56 of 397 (14%) 2021 IPOs were above offer [98] [B]; "of 29 US venture-backed
  companies that listed at ≥$1B, over two-thirds were >80% below listing price" — the summary
  attributes this to the 2022 cohort, which is implausible given 173 IPOs in 2022; it is more
  likely the 2021 cohort; verify against [98] [C].
- **Tokens:** 53.2% of ~20M tokens dead by end-2025 [80][81]; ~98% of Pump.fun launches never
  graduate [84][85][86]; in a bear, 72 of the top-100 were ≥90% below ATH [89]; >40% of altcoins
  at or near ATLs in 2025/26 [90] [C].
- **The retail-favourite cohort:** Verdad's "Meme Stonks Revisited" [103] exists but I could not
  retrieve its numbers [C].

What I could *not* find: a study of "story" small caps (say, <$500M, pre-profit, narrative-driven)
giving the fraction that lose >80% within N years. The SPAC and 2021-IPO numbers (median −88%
market-adjusted; 86% below offer after ~2 years) are the best proxies and say **the modal outcome
for a narrative small cap bought at peak attention is a >60% loss, and the median is close to
−90%.** For low-cap tokens the modal outcome is death.

---

## 6. Conclusion: what a rational 10x hunt looks like given these base rates

**Expected-value arithmetic.** Let p = P(≥10x within 24 months) for a screened candidate, and
assume a miss averages a 70% loss (the SPAC/IPO/delisting numbers say this is generous). Then
EV per unit = 10p + 0.3(1−p) = 0.3 + 9.7p. To merely match a plausible 2-year index return of 1.2x
you need **p ≈ 9%**; if misses lose 90%, p ≈ 11%; if misses lose only 50%, p ≈ 7%. The unconditional
base rate is ~0.1–1% (§1.4). **A screen therefore needs to lift the hit rate by 10–100x to be
worth running.** Nothing in §4 has demonstrated that lift; the Alta Fox and Bessembinder features
describe winners, they do not give P(win | features). In practice much of the value comes from
the *middle* of the distribution — misses that return 2–5x — so track the full payoff
distribution, not the binary.

**Portfolio math.** With p = 10% per bet and independent bets, P(at least one 10x) = 1 − 0.9^N:
N = 10 → 65%, N = 20 → 88%, N = 30 → 96%; expected hits = N/10. Bets in the same narrative
(quantum, AI infra, memecoins) are not independent — they 10x together and die together — so
the effective N is the number of *distinct* theses, not tickers. Sizing: equal small positions
(1–3% each), no averaging down on kill-criteria breaches, and a pre-committed sell-down rule at
3–5x, because the historical 10x-ers were also the names that later fell 60–90% (SMCI, MSTR, the
quantum names, most 2021 altcoins) [M].

**What the process should look like.**

1. Restrict to the parts of the universe where 10x is arithmetically possible: market cap such
   that 10x implies a value the sector has actually paid before, and liquidity such that the
   position can be exited. Reject anything where 10x implies a top-5 market cap in its sector
   without a matching revenue path (README rule 2).
2. Require an observable, dated fundamental inflection that is not yet in consensus numbers
   (the one feature with A-grade evidence), plus a catalyst calendar inside 24 months.
3. Prefer names that have already been through a >60% drawdown *and* whose survival is no longer
   in question (cash runway, no going-concern) — this is where Part I's regularity and the
   delisting base rate can both be respected.
4. Treat float/short-interest and narrative regime as payoff amplifiers, not selection criteria.
5. Measure the base rate properly: run a rolling 24-month 10x count on a full US price history
   and on CoinGecko's top-100 snapshots, from fixed start dates, not troughs. Until that exists,
   every number in this note above the [A] grade should be treated as ±1 order of magnitude.

**Expected hit rate for a disciplined process:** I would not assume more than **5–10%** of
well-screened candidates reach 10x within 24 months in a favourable regime, and **1–3%** in an
unfavourable one — which means a 20–30-name portfolio should expect 0–3 hits and a
realised return dominated by how the misses are managed. Anyone claiming a higher hit rate
should be asked for their fixed-start-date, survivorship-free track record.

---

## 7. What I could not verify (needs a primary source or a data pull)

- Any published count of US stocks rising 10x within a 24-month window, for any period.
- The originating page for "1 in 10 stocks ≥$300M doubled in 2020".
- NVDA Oct-2022 low, SMCI Jan-2023 low, APP and PLTR 2022/23 lows and 2024 highs (price paths [M]).
- Oklo, Robinhood, Bitmine, Hyperliquid, Zcash, SanDisk, AXT 24-month price paths.
- Identity and float of MGRT, ANL, XHLD (2026 YTD leaders).
- Bessembinder Part IV ("Can observable characteristics forecast outcomes?") [13] — findings not retrieved.
- Any academic survival analysis of exchange-listed tokens; the arXiv memecoin papers' return
  distributions [87][88].
- Counts of top-100 tokens that did 10x in 2020–21 and 2023–25 (my [M] estimates: roughly one-third
  to one-half at peak in 2021; ~10–15% in 2023–25).
- CoinGecko's 11.6M vs 53.2%-of-20.2M discrepancy [80].
- The IPO ">80% below listing" cohort year (2021 vs 2022) [98].
- Verdad "Meme Stonks Revisited" numbers [103].
- Everything tagged [M] in §3–§4 about drawdowns and policy rates.

---

## Sources

All accessed 2026-09-24 via web search; pages could not be opened, so figures are as reported in
search summaries of these URLs.

1. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2900447 — Bessembinder, "Do Stocks Outperform Treasury Bills?" (SSRN)
2. https://wpcarey.asu.edu/sites/g/files/litvpz246/files/2021-10/do-stocks-outperform-treasury-bills.pdf — same, ASU PDF
3. https://ideas.repec.org/a/eee/jfinec/v129y2018i3p440-457.html — JFE 129(3):440–457 record
4. https://www.morningstar.com/podcasts/the-long-view/4d0b7321-0f52-421a-adb0-024dbc95a562 — Morningstar Long View interview with Bessembinder
5. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3710251 — Bessembinder, Chen, Choi, Wei, "Long-Term Shareholder Returns: Evidence from 64,000 Global Stocks" (SSRN)
6. https://www.tandfonline.com/doi/abs/10.1080/0015198X.2023.2188870 — same, FAJ 79(3)
7. https://rpc.cfainstitute.org/research/financial-analysts-journal/2023/long-term-shareholder-returns-evidence-from-64000-global-stocks — CFA Institute summary
8. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4897069 — Bessembinder, "Which U.S. Stocks Generated the Highest Long-Term Returns?" (2024)
9. https://elements.visualcapitalist.com/wp-content/uploads/2024/08/ssrn-4897069.pdf — same, PDF mirror
10. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3657604 — "Extreme Stock Market Performers, Part I: Expect Some Drawdowns"
11. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3657609 — "Part II: Do Technology Stocks Dominate?"
12. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3657611 — "Part III: What are their Observable Characteristics?"
13. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3657612 — "Part IV: Can Observable Characteristics Forecast Outcomes?"
14. https://media.bailliegifford.com/mws/affgqguh/20250512121028_lessons-from-bessembinder-pdf.pdf — Baillie Gifford, "Lessons from Bessembinder"
15. https://www.robeco.com/en-int/insights/2020/10/most-stocks-do-not-outperform-treasury-bills-in-the-long-run — Robeco interview
16. https://www.bespokepremium.com/interactive/posts/think-big-blog/10-year-10-baggers — Bespoke, "10-Year 10-Baggers" (Apr 2023)
17. https://seekingalpha.com/article/4593792-10-year-10-baggers — Bespoke piece on Seeking Alpha
18. https://seekingalpha.com/article/4824900-ten-bull-market-10-baggers — "Ten Bull Market 10-Baggers" (Russell 3000 5-year screen)
19. https://www.activtrades.com/en/news/what-are-10-bagger-stocks-and-how-to-find-them — ActivTrades (22 Russell 3000 10x 2016–2025)
20. https://www.quantifiedstrategies.com/whats-the-probability-of-a-10x-stock/ — QuantifiedStrategies
21. https://microcapclub.com/the-myth-and-math-of-10-baggers-what-investors-overlook/ — MicroCapClub
22. https://www.bloomberg.com/professional/insights/markets/chasing-multi-baggers-india-has-had-more-stocks-rising-10-fold/ — Bloomberg, India vs S&P/Nasdaq 10-baggers
23. https://www.business-standard.com/amp/markets/news/over-half-of-nse-500-stocks-deliver-10x-return-in-20-years-goldman-sachs-123060500276_1.html — Business Standard / Goldman NSE 500
24. https://stablebread.com/global-10-bagger-lessons/ — StableBread, "10 Lessons From 446 Global 10-Bagger Stocks"
25. https://altafoxcapital.squarespace.com/s/Makings-of-a-MultiBagger.pdf — Alta Fox, "The Makings of a Multibagger" (full study)
26. https://static1.squarespace.com/static/5aaacb57506fbe4636414126/t/5f85c428b4bac16b20450df0/1602602051503/Conclusion+Deck-+Makings+of+a+MultiBagger+-+FINAL-compressed.pdf — Alta Fox conclusion deck
27. https://acquirersmultiple.com/2020/11/alta-fox-makings-of-a-multibagger/ — Acquirer's Multiple summary of Alta Fox
28. https://goldmanwontcoverthis.substack.com/p/deconstructing-multibaggers-i-reviewed — review of the Alta Fox study
29. https://multibaggerideas.substack.com/p/a-masterclass-in-what-actually-drives — Alta Fox return decomposition and correlations
30. https://behindthebalancesheet.substack.com/p/what-makes-for-a-multi-bagger — Behind the Balance Sheet on multibaggers
31. https://microcapclub.com/multibagger-interview-with-alta-fox-capital/ — MicroCapClub interview with Alta Fox
32. https://microcapclub.com/book-review-100-baggers-by-chris-mayer/ — review of Mayer, *100 Baggers*
33. https://stablebread.com/chris-mayer-100-baggers-screen/ — StableBread on Mayer's data set
34. https://fifthperson.com/100-baggers-by-christopher-mayer/ — Fifth Person on *100 Baggers*
35. https://www.fool.com/investing/2021/01/02/4-growth-stocks-that-can-be-10-baggers-this-decade — Motley Fool, 2 Jan 2021 (2020 doubling context)
36. https://www.bloomberg.com/news/articles/2021-02-04/there-are-still-16-meme-stocks-with-at-least-100-gains-in-2021 — Bloomberg, 4 Feb 2021
37. https://www.nasdaq.com/articles/3-stocks-with-the-best-shot-to-10x-by-2025 — Nasdaq (SMCI +800% since early 2023 context)
38. https://www.morningstar.com/stocks/best-worst-performing-stocks-2025 — Morningstar, best/worst 2025
39. https://money.usnews.com/investing/articles/best-performing-stocks-of-the-year — US News, best-performing stocks (SanDisk figures)
40. https://www.stocktitan.net/rankings/stock-gains-ytd/2026 — StockTitan, 2026 YTD gainers
41. https://www.stocktitan.net/rankings/stock-gains — StockTitan, 52-week gainers (Sep 2026)
42. https://www.forbes.com/sites/investor-hub/article/stock-market-winners-losers-2026/ — Forbes, 2026 winners/losers, September edition
43. https://www.stl.news/five-best-performing-stocks-of-2026-so-far/ — STL.News, five best 2026
44. https://www.fool.com/investing/2026/07/22/quantum-computing-stocks-ionq-988-million-warning/ — Motley Fool, 22 Jul 2026 (two-year quantum returns)
45. https://finance.yahoo.com/markets/stocks/articles/quantum-computing-stocks-ionq-rigetti-092600203.html — Yahoo/Fool, quantum rally
46. https://finance.yahoo.com/markets/stocks/articles/ionq-rigetti-computing-d-wave-092601051.html — Yahoo/Fool, quantum (from mid-Jul 2024)
47. https://www.fastcompany.com/91465778/quantum-computing-stocks-rise-and-fall-d-wave-rigetti-ionq — Fast Company, Dec 2025 quantum moves
48. https://stockanalysis.com/stocks/rklb/ — Rocket Lab ATL/ATH
49. https://www.fool.com/investing/2025/01/04/after-soaring-361-in-2024-is-rocket-lab-stock-a-bu/ — Motley Fool, RKLB +361% in 2024
50. https://www.statmuse.com/money/ask/carvana-stock-performance-december-2022-to-2024 — StatMuse, CVNA Dec 2022–Dec 2024
51. https://fortune.com/2024/07/01/carvana-stock-up-500-top-analyst/ — Fortune, CVNA Jul 2024
52. https://www.fool.com/investing/2026/04/07/macroeconomic-factors-are-dragging-down-carvanas-s/ — Motley Fool, CVNA Apr 2026 (ATL $3.55, 7 Dec 2022)
53. https://www.forbes.com/sites/dereksaul/2024/06/10/nvidia-shares-now-trading-at-just-120-after-stock-split-in-wake-of-monstrous-run/ — Forbes, NVDA split
54. https://www.macrotrends.net/stocks/charts/NVDA/nvidia/stock-price-history — Macrotrends NVDA
55. https://nordfx.com/traders-guide/NVIDIA-stock-split — NVDA split guide (900% Oct 2022–Jun 2024 claim)
56. https://stockanalysis.com/stocks/nvda/history/ — NVDA price history
57. https://www.tradingview.com/symbols/NASDAQ-SMCI/ — SMCI ATH 8 Mar 2024
58. https://finance.yahoo.com/news/super-micro-stock-had-a-wild-ride-in-2024--heres-why-193718911.html — Yahoo, SMCI 2024
59. https://www.macrotrends.net/stocks/charts/SMCI/super-micro-computer/stock-price-history — Macrotrends SMCI
60. https://www.fool.com/investing/2024/12/27/prediction-palantir-stock-could-hit-100-year-end/ — Motley Fool, PLTR +380% in 2024
61. https://www.cnbc.com/2024/12/23/microstrategy-rides-red-sweep-to-477percent-gain-in-2024-top-tech-stock.html — CNBC, MSTR +477% 2024, +346% 2023, APP #1
62. https://stockanalysis.com/stocks/app/ — AppLovin overview
63. https://www.macrotrends.net/stocks/charts/APP/applovin/stock-price-history — Macrotrends APP
64. https://investingnews.com/daily/tech-investing/blockchain-investing/bitcoin-price-history/ — BTC history ($69,044 on 10 Nov 2021; >1,200% from Mar 2020)
65. https://en.wikipedia.org/wiki/Cryptocurrency_bubble — Wikipedia (12 Mar 2020 crash to $3,850)
66. https://techcrunch.com/2024/03/05/bitcoin-hits-new-all-time-high-passing-69k-first-time-since-november-2021/embed/ — TechCrunch
67. https://www.mexc.com/learn/article/solana-price-history-the-complete-sol-chart-from-launch-to-all-time-high/1 — SOL price history
68. https://www.coinlore.com/coin/solana/historical-data — CoinLore SOL history
69. https://www.coindesk.com/markets/2021/12/31/here-are-the-top-10-cryptocurrencies-of-2021 — CoinDesk, 2021 review
70. https://blog.bitpanda.com/en/bitcoin-vs-altcoins-which-market-phase-dominating-and-what-it-means-investors — Bitpanda, BTC vs altcoins
71. https://coingape.com/will-altcoins-continue-to-underperform-bitcoin-after-fomc/ — CoinGape
72. https://www.ccn.com/analysis/crypto/altcoin-season-2025-indicator/ — CCN altseason indicators
73. https://coinmarketcap.com/charts/altcoin-season-index/ — CMC Altcoin Season Index
74. https://www.coingecko.com/research/publications/top-crypto-gainers — CoinGecko, top gainers 2025
75. https://www.fool.com/investing/2026/01/11/best-performing-cryptocurrencies-of-2025 — Motley Fool, best cryptos 2025
76. https://finance.yahoo.com/news/were-best-performing-cryptocurrencies-2025-035800534.html — Yahoo, best cryptos 2025
77. https://www.coinlore.com/top-crypto-coins — CoinLore, top coins 2026 by ROI (top-100 avg −21.25% YTD)
78. https://altindex.com/top-crypto-performers — AltIndex, Sep 2026 gainers
79. https://mudrex.com/learn/best-crypto-short-term-gains/ — Mudrex, Sep 2026 (promotional; BTC $60k→$85k claim)
80. https://www.coingecko.com/research/publications/how-many-cryptocurrencies-failed — CoinGecko, "Dead coins" (Jan 2026)
81. https://www.coindesk.com/markets/2026/01/14/more-than-half-of-all-crypto-tokens-have-failed-and-most-died-in-2025 — CoinDesk on the CoinGecko report
82. https://www.crowdfundinsider.com/2026/01/257221-dead-coins-over-50-of-cryptocurrencies-have-failed-report-reveals/ — Crowdfund Insider
83. https://beincrypto.com/coingecko-dead-crypto-tokens-q1-2025/ — BeInCrypto on CoinGecko Q1 2025
84. https://thedefiant.io/news/defi/pump-fun-token-graduation-rate-plummets — The Defiant, Pump.fun graduation rate
85. https://www.cryptopolitan.com/pump-fun-graduating-tokens-break-to-1-15-of-new-launches/ — Cryptopolitan, 1.15%
86. https://www.bitget.com/news/detail/12560605271357 — Bitget/Dune, 2.01% week of 9–15 Mar 2026
87. https://arxiv.org/pdf/2512.11850 — "The Memecoin Phenomenon: An In-Depth Study of Solana's Blockchain Trends"
88. https://arxiv.org/pdf/2607.02823 — "Auditing Collector-Generated Graduation Labels on Pump.fun"
89. https://cryptonews.net/news/analytics/8383217/ — "72 of the top 100 coins have fallen 90% or more"
90. https://cryptopotato.com/over-40-of-altcoins-near-all-time-lows-worse-than-last-bear-market/ — CryptoPotato
91. https://cryptorank.io/news/feed/2590e-altcoin-liquidity-crunch-83-crypto-bear-trend — CryptoRank
92. https://www.yalejreg.com/bulletin/was-the-spac-crash-predictable/ — Yale J. Reg. bulletin (Klausner & Ohlrogge)
93. https://law.stanford.edu/wp-content/uploads/2022/07/2022-01-24-A-Sober-Look-At-SPACs-Yale-Journal-on-Regulation.pdf — "A Sober Look at SPACs"
94. https://www.institutionalinvestor.com/article/2bstnox9764n3ivyn8veo/portfolio/companies-that-merged-with-spacs-have-underperformed-the-s-p-500-by-a-stunning-margin-since-2018 — Institutional Investor on de-SPACs
95. https://onlinelibrary.wiley.com/doi/10.1111/eufm.12366 — Kiesel et al., "SPAC merger announcement returns and subsequent performance", EFM 2023
96. https://www.skadden.com/-/media/files/publications/2023/06/de_spac_transaction_trends_in_2023.pdf?rev=a0def9cfccae4a3fa2b31b3efc20e548 — Skadden, de-SPAC trends 2023
97. https://fortune.com/2021/12/13/ipo-market-wall-street-spacs-2022-outlook-stock-market-direct-listings/ — Fortune, Dec 2021 IPO class
98. https://news.crunchbase.com/ipo/public-market-lessons-forecast — Crunchbase, 2021/2022 IPO class performance
99. https://site.warrington.ufl.edu/ritter/files/IPO-Statistics.pdf — Ritter, IPO statistics (for the reader; no figure used)
100. https://quantpedia.com/strategies/short-interest-effect-long-short-version — Quantpedia on Asquith, Pathak & Ritter
101. https://academic.oup.com/raps/article/13/4/691/7127046 — "Short Interest and Aggregate Stock Returns: International Evidence", RAPS 13(4)
102. https://business.ku.edu/news/article/social-media-discussions-fueled-meme-stock-events-and-significant-short-squeezes-research-finds — KU School of Business
103. https://verdadcap.com/archive/meme-stonks-revisited — Verdad, "Meme Stonks Revisited"
104. https://www.aeaweb.org/conference/2026/program/powerpoint/z4ratTGB — AEA 2026 conference paper on short squeezes
105. https://www.edwardconard.com/macro-roundup/hendrik-bessembinder-finds-that-the-best-performing-1526-global-firms-2-4-of-total-accounted-for-all-of-the-75-7t-in-net-global-stock-market-wealth-creation-between-1990-and-2020/ — Edward Conard summary (1,526 firms = 2.4%)
106. https://massivemoats.substack.com/p/executive-summary-of-bessembinders — executive summary of the 2018 paper (median −3.7% figure)
107. https://www.business-standard.com/amp/article/markets/number-of-ten-baggers-on-the-rise-despite-market-volatility-shows-data-122102500831_1.html — Business Standard, ten-baggers 2022 (India; not used for a figure)
108. https://www.cxoadvisory.com/equity-premium/behaviors-and-characteristics-of-top-stocks/ — CXO Advisory on Part III
109. https://mokapucapital.com/100-baggers-chris-mayer-notes/ — notes on *100 Baggers*
