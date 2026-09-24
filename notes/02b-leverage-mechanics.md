# 02b. Leverage mechanics: turning a 2-4x underlying move into a 10x, and what it costs

**Date:** 2026-09-24  **Author:** research agent (commodities + leverage)  **Status:** draft
**Code:** `tools/options_10x.py` (Black-Scholes, leveraged-ETF drag, liquidation probabilities; `python3 tools/options_10x.py` reproduces every table; numpy + scipy).

> **Evidence status.** All tables in Sections 1-3 are *model output* from the script and are
> exact given the stated assumptions; no market data enters them. Every market-history statement
> (implied vols, ETF track records, Strategy's premium, prediction-market rules and valuations)
> is recalled from training data (cut-off ~Jun 2026), marked `[from memory, verify]`, and has no
> URL because the session's web-search budget was exhausted before this note was started. The
> academic references in the Sources section are given bibliographically (journal, volume, pages)
> for checking; none was fetched here. Figures tagged `[XREF snapshot n]` / `[XREF crypto n]` come
> from sibling notes in this repo written by agents that did have search access
> (`notes/01-market-snapshot.md`, `notes/themes/crypto.md`); *n* is the source number in that
> note, where the URL is recorded. They are search-snippet figures and were not re-checked here.

## 0. The one-line answer

Under fair pricing, **every** leveraged instrument gives roughly a 1-in-10 chance of touching 10x,
because the discounted value of a fairly priced claim is a martingale and, by optional stopping,
P(value ever reaches 10x initial) is at most 1/10 (plus whatever real drift you assume). The Monte
Carlo below finds 10-13% for every option configuration tested. Leverage does not create 10x
probability; it *concentrates* it, at the cost of a ~90% loss frequency. The only way to do better
than 1-in-10 is to be right about something the price is wrong about: the size of the move
(realised vol > implied), its direction (drift), or the probability of a discrete event.

## 1. Long-dated call options (LEAPS)

### 1.1 Set-up
Black-Scholes, r = 4% continuous (assumption), no dividends, European payoff at expiry, no bid/ask.
For each implied vol (IV) and tenor T, the strike K is solved from the target delta
(K = S0 * exp((r + IV^2/2) T - N^-1(delta) IV sqrt(T))). A 10x at expiry needs
S_T = K + 10 * premium. Probability columns use a lognormal with the *same* sigma as the IV
(i.e. the market's vol is assumed correct - no volatility risk premium) and a stated real-world
expected return of the underlying: 0%/yr (no edge) and +10%/yr (a generous premium).
"P(touch 10x MTM)" is a 20,000-path Monte Carlo of the option's Black-Scholes mark-to-market
hitting 10x the premium at any daily close before expiry, at +10% drift.

**Where current IVs sit.** Not retrieved this session. Typical ranges recalled for 2025-H1 2026,
`[from memory, verify]` before use: NVDA 40-55%; TSLA 55-75%; IBIT/BTC 45-65%; COIN 70-100%;
MSTR 80-120% (it fell as the mNAV premium compressed in late 2025). The table brackets these.
Sourced context for the date of writing: VIX 15.18 at the 23 Sep 2026 close [XREF snapshot 3];
NVDA $223.03, market cap ~$5.4 T (22-23 Sep 2026) [XREF snapshot 57-61]; BTC $85,686 (23 Sep 2026)
[XREF snapshot 42]. Single-name 12-month implied vols on that date: [NOT FOUND].

### 1.2 Main table (from `tools/options_10x.py`)

| T (yr) | IV | delta | K/S0 | premium (% of S0) | breakeven ret. | **ret. for 10x** | sigma-units of ret. | P(10x at expiry) drift 0% | P(10x at expiry) drift +10% | P(touch 10x MTM, drift +10%) | P(expire worthless, drift +10%) | E[multiple] drift +10% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 40% | 0.10 | 1.88 | 1.6% | +90% | **+104%** | 1.79 | 2.3% | 4.1% | 11.6% | 94% | 1.49x |
| 1 | 40% | 0.20 | 1.58 | 3.7% | +62% | **+95%** | 1.67 | 3.1% | 5.2% | 10.8% | 86% | 1.42x |
| 1 | 40% | 0.30 | 1.39 | 6.3% | +45% | **+102%** | 1.75 | 2.5% | 4.4% | 8.4% | 78% | 1.38x |
| 1 | 60% | 0.10 | 2.69 | 2.3% | +171% | **+191%** | 1.78 | 1.9% | 2.8% | 10.7% | 96% | 1.35x |
| 1 | 60% | 0.20 | 2.06 | 5.2% | +112% | **+158%** | 1.58 | 3.0% | 4.3% | 10.6% | 91% | 1.31x |
| 1 | 60% | 0.30 | 1.71 | 8.6% | +79% | **+157%** | 1.57 | 3.1% | 4.4% | 9.3% | 85% | 1.28x |
| 1 | 80% | 0.10 | 4.00 | 2.8% | +302% | **+328%** | 1.82 | 1.3% | 1.8% | 10.2% | 98% | 1.28x |
| 1 | 80% | 0.20 | 2.81 | 6.4% | +187% | **+245%** | 1.55 | 2.6% | 3.4% | 10.3% | 94% | 1.25x |
| 1 | 80% | 0.30 | 2.18 | 10.6% | +129% | **+224%** | 1.47 | 3.1% | 4.1% | 9.8% | 89% | 1.23x |
| 1 | 100% | 0.10 | 6.18 | 3.3% | +521% | **+551%** | 1.87 | 0.9% | 1.1% | 10.0% | 99% | 1.25x |
| 1 | 100% | 0.20 | 3.98 | 7.5% | +306% | **+373%** | 1.55 | 2.0% | 2.5% | 10.1% | 96% | 1.22x |
| 1 | 100% | 0.30 | 2.90 | 12.3% | +202% | **+312%** | 1.42 | 2.8% | 3.5% | 10.0% | 93% | 1.20x |
| 2 | 40% | 0.10 | 2.62 | 2.2% | +165% | **+184%** | 1.85 | 1.7% | 3.8% | 13.0% | 95% | 1.86x |
| 2 | 40% | 0.20 | 2.05 | 4.9% | +110% | **+154%** | 1.65 | 2.7% | 5.7% | 12.9% | 88% | 1.73x |
| 2 | 40% | 0.30 | 1.71 | 8.2% | +79% | **+153%** | 1.64 | 2.7% | 5.8% | 11.5% | 81% | 1.65x |
| 2 | 60% | 0.10 | 4.61 | 2.9% | +364% | **+390%** | 1.87 | 1.1% | 2.0% | 11.4% | 98% | 1.61x |
| 2 | 60% | 0.20 | 3.17 | 6.7% | +224% | **+284%** | 1.59 | 2.2% | 3.8% | 11.7% | 94% | 1.54x |
| 2 | 60% | 0.30 | 2.42 | 11.0% | +153% | **+252%** | 1.48 | 2.8% | 4.7% | 11.4% | 89% | 1.49x |
| 2 | 80% | 0.10 | 8.76 | 3.6% | +779% | **+812%** | 1.95 | 0.6% | 1.0% | 10.9% | 99% | 1.50x |
| 2 | 80% | 0.20 | 5.32 | 8.1% | +440% | **+513%** | 1.60 | 1.5% | 2.3% | 10.9% | 97% | 1.45x |
| 2 | 80% | 0.30 | 3.72 | 13.2% | +285% | **+404%** | 1.43 | 2.3% | 3.4% | 11.1% | 94% | 1.42x |
| 2 | 100% | 0.10 | 18.04 | 4.2% | +1708% | **+1745%** | 2.06 | 0.3% | 0.4% | 10.6% | 100% | 1.44x |
| 2 | 100% | 0.20 | 9.68 | 9.2% | +877% | **+961%** | 1.67 | 0.9% | 1.3% | 10.6% | 99% | 1.40x |
| 2 | 100% | 0.30 | 6.18 | 15.0% | +533% | **+668%** | 1.44 | 1.6% | 2.2% | 10.5% | 97% | 1.37x |

### 1.3 What the table says
1. **The underlying move needed for 10x at expiry is always ~1.4-2.1 sigma-units**, whatever the
   delta or tenor. That is the algebraic content of "fair pricing". In return terms: on a 40%-IV
   name a 12-month OTM call needs the stock to roughly **double** (+95% to +104%); at 60% IV it
   needs +157% to +191%; at 80% IV +224% to +328%; at 100% IV +312% to +551%. Two-year options
   need *larger* moves (the extra time is priced in), e.g. +153% to +184% at 40% IV.
2. **P(10x at expiry) is 1-6%**; P(touching 10x mark-to-market at some point) is **10-13%**
   for every configuration, i.e. ~1/10 as optional stopping predicts. The practical consequence:
   a 10x from options is a *take-profit* event that occurs mid-life about one time in ten, not an
   expiry outcome.
3. **P(total loss) is 78-100%.** At 80%+ IV and 2-year tenor, delta-0.10 calls expire worthless
   more than 98% of the time even with a +10%/yr drift.
4. **Expected multiples of 1.2-1.9x** at +10%/yr drift look positive, but this assumes (a) the
   drift and (b) that IV equals future realised vol. Empirically, out-of-the-money equity calls
   have had *negative* average returns because implied vol exceeds realised vol on average
   [R4]. Put the drift at 0% and expected multiples fall below 1x for most rows (not tabulated;
   run the script with `drifts=(0.0, 0.0)`).
5. **High IV is the enemy, not the friend.** On a 100%-IV name (MSTR-like), the delta-0.20
   two-year call needs the stock up ~10x to itself return 10x: the option adds nothing. On such
   names the underlying *is* the leveraged instrument; buy it, not its options.

### 1.4 If you are handed the move: multiple at expiry for +100% / +200% / +300% (T = 1 yr)

| IV | delta | K/S0 | premium (% of S0) | x on +100% | x on +200% | x on +300% |
|---|---|---|---|---|---|---|
| 40% | 0.10 | 1.88 | 1.6% | 7.2x | 69.0x | 130.7x |
| 40% | 0.20 | 1.58 | 3.7% | 11.3x | 38.0x | 64.7x |
| 40% | 0.30 | 1.39 | 6.3% | 9.7x | 25.7x | 41.6x |
| 60% | 0.10 | 2.69 | 2.3% | 0.0x | 13.8x | 57.9x |
| 60% | 0.20 | 2.06 | 5.2% | 0.0x | 18.1x | 37.4x |
| 60% | 0.30 | 1.71 | 8.6% | 3.4x | 15.0x | 26.6x |
| 80% | 0.10 | 4.00 | 2.8% | 0.0x | 0.0x | 0.1x |
| 80% | 0.20 | 2.81 | 6.4% | 0.0x | 3.0x | 18.6x |
| 80% | 0.30 | 2.18 | 10.6% | 0.0x | 7.7x | 17.2x |
| 100% | 0.10 | 6.18 | 3.3% | 0.0x | 0.0x | 0.0x |
| 100% | 0.20 | 3.98 | 7.5% | 0.0x | 0.0x | 0.2x |
| 100% | 0.30 | 2.90 | 12.3% | 0.0x | 0.8x | 9.0x |

Same for T = 2 yr (script output): at 40% IV, delta 0.20-0.30 gives 15.7-19.3x on +200% and
27.8-39.5x on +300%, but 0-3.5x on +100%; at 60% IV only the +300% column pays (12.4-14.3x);
at 80-100% IV nothing below +300% pays at all.

Reading: **the "2x underlying -> 10x" conversion exists only for ~40%-IV underlyings with
12-month delta-0.20-0.30 calls (9.7-11.3x)**. A 3x underlying converts to 10x+ up to ~60% IV.
A 4x underlying converts up to ~80% IV with delta 0.20-0.30. Beyond that, the option is a worse
bet than the stock.

### 1.5 Costs that the model omits (all reduce the numbers above)
- Bid/ask on 1-2 year single-name OTM calls: typically 5-15% of premium each way `[from memory, verify]`; on a delta-0.10 option this alone shaves the achievable multiple by ~10-25%.
- Volatility risk premium: IV > subsequently realised vol on average, so the "P(10x)" columns are upper bounds under the market's own vol [R4].
- Skew: on single stocks, OTM calls often trade at *lower* IV than ATM (negative skew), which helps the buyer slightly; on crypto and meme names calls can carry positive skew, which hurts.
- Early assignment does not apply to a long; but American-style exercise value is irrelevant to a buyer who sells to close.
- Tax: gains on options held >12 months are long-term in the US only if the contract itself was held >12 months, which forces a 13-24-month tenor if that matters.

## 2. Leveraged ETFs (daily-rebalanced 2x / 3x)

### 2.1 Mathematics
For a daily-rebalanced L-times fund, in the continuous-time limit (Cheng & Madhavan 2009 [R2];
Avellaneda & Zhang 2010 [R3]):

    ln(L_T / L_0)  =  L * ln(S_T / S_0)  -  (L^2 - L)/2 * sigma^2 * T  -  [(L-1) * funding + fee] * T

The middle term is the *variance drag*: it is path-independent given the realised variance
sigma^2 T, and it is what people call "volatility decay". For L = 2 the coefficient is 1; for L = 3
it is 3. The first term says that when the underlying trends, the fund compounds as (S_T/S_0)^L,
i.e. *more* than L times the return - a 4x underlying gives 16x for a 2x fund and 64x for a 3x fund
before drag. Leveraged ETFs are therefore convex in trends and are destroyed by round trips.

### 2.2 Variance drag alone (underlying flat, before fees/financing)

| realised vol | 2x, 1 yr | 2x, 2 yr | 3x, 1 yr | 3x, 2 yr |
|---|---|---|---|---|
| 30% | 0.91x (-9%) | 0.84x (-16%) | 0.76x (-24%) | 0.58x (-42%) |
| 40% | 0.85x (-15%) | 0.73x (-27%) | 0.62x (-38%) | 0.38x (-62%) |
| 60% | 0.70x (-30%) | 0.49x (-51%) | 0.34x (-66%) | 0.12x (-88%) |
| 80% | 0.53x (-47%) | 0.28x (-72%) | 0.15x (-85%) | 0.02x (-98%) |
| 100% | 0.37x (-63%) | 0.14x (-86%) | 0.05x (-95%) | 0.00x (-100%) |

A 3x product on an 80%-vol underlying that ends flat after two years loses ~98% of its value.
That is the MSTR-2x/3x and single-stock-3x experience in choppy markets.

### 2.3 Median outcome vs underlying move (T = 1 yr; financing 4.5% on borrowed notional, fee 1%/yr)

| underlying | realised vol | 2x ETF | 3x ETF | naive L*return |
|---|---|---|---|---|
| -50% (0.5x) | 40% | 0.20x | 0.07x | 2x: 0.0x, 3x: -0.5x |
| -50% (0.5x) | 60% | 0.17x | 0.04x | 2x: 0.0x, 3x: -0.5x |
| -50% (0.5x) | 80% | 0.12x | 0.02x | 2x: 0.0x, 3x: -0.5x |
| +0% (1.0x) | 40% | 0.81x | 0.56x | 2x: 1.0x, 3x: 1.0x |
| +0% (1.0x) | 60% | 0.66x | 0.31x | 2x: 1.0x, 3x: 1.0x |
| +0% (1.0x) | 80% | 0.50x | 0.13x | 2x: 1.0x, 3x: 1.0x |
| +100% (2.0x) | 40% | 3.23x | 4.48x | 2x: 3.0x, 3x: 4.0x |
| +100% (2.0x) | 60% | 2.64x | 2.46x | 2x: 3.0x, 3x: 4.0x |
| +100% (2.0x) | 80% | 2.00x | 1.06x | 2x: 3.0x, 3x: 4.0x |
| +200% (3.0x) | 40% | 7.26x | 15.12x | 2x: 5.0x, 3x: 7.0x |
| +200% (3.0x) | 60% | 5.94x | 8.30x | 2x: 5.0x, 3x: 7.0x |
| +200% (3.0x) | 80% | 4.49x | 3.58x | 2x: 5.0x, 3x: 7.0x |
| +300% (4.0x) | 40% | 12.90x | 35.83x | 2x: 7.0x, 3x: 10.0x |
| +300% (4.0x) | 60% | 10.57x | 19.67x | 2x: 7.0x, 3x: 10.0x |
| +300% (4.0x) | 80% | 7.99x | 8.49x | 2x: 7.0x, 3x: 10.0x |

### 2.4 Underlying multiple needed for a 10x

| realised vol | 2x, 1 yr | 2x, 2 yr | 3x, 1 yr | 3x, 2 yr |
|---|---|---|---|---|
| 40% | 3.52x | 3.92x | 2.61x | 3.17x |
| 60% | 3.89x | 4.79x | 3.19x | 4.73x |
| 80% | 4.48x | 6.34x | 4.22x | 8.28x |
| 100% | 5.36x | 9.08x | 6.05x | 17.02x |

Reading: **a 3x fund converts a ~2.6x move into 10x only on a 40%-vol underlying in a trending
year**; at 60% vol it needs ~3.2x; at 80% vol the two are close over one year (3x needs 4.2x,
2x needs 4.5x) and the 3x fund is clearly *worse* over two years (8.3x vs 6.3x). At 100% vol,
hold nothing leveraged for two years. Solving the drag equation, the crossover where a 2x fund
needs a smaller move than a 3x fund is realised vol of ~87% for a one-year hold and ~61% for a
two-year hold (script: same cost assumptions).

### 2.5 Historical examples `[from memory, verify]` - none re-sourced this session
- **TQQQ (3x Nasdaq-100):** 2022 about -79% vs QQQ about -33%; 2023 about +198% vs QQQ about +55%. Textbook: the round trip 2022-23 left TQQQ far below QQQ.
- **SOXL (3x semiconductors):** 2022 about -86%; 2023 about +230%; Jan-Apr 2025 drawdown ~-75% then a strong recovery in H2 2025. Multi-year holders who bought the 2021 top were still underwater in 2025 despite SOXX at new highs.
- **NVDL (2x NVDA, was 1.5x until 2024):** 2024 roughly +330% vs NVDA +171% - the trending case where (S_T/S_0)^2 compounding beat 2x. 2025 [NOT FOUND].
- **TSLL (2x TSLA):** Dec 2024 peak to Mar-Apr 2025 trough about -80% vs TSLA about -50%; Tesla's later recovery left TSLL well below its own peak. 2026 [NOT FOUND].
- **MSTU (T-Rex 2x MSTR, launched Sep 2024) / MSTX (Defiance, launched Aug 2024 at 1.75x, later 2x):** MSTR fell from ~$543 (21 Nov 2024) to roughly $120-160 by Dec 2025-Feb 2026 (~-75%); the 2x products lost ~95% peak-to-trough and, in Nov 2024, ran out of swap capacity at prime brokers and used call options to get exposure, which increased tracking error `[from memory, verify]`. Reverse splits [NOT FOUND].
- **CONL (2x COIN):** ~-80% peak-to-trough Dec 2024 to Apr 2025, then a large recovery into Jul 2025 as COIN joined the S&P 500 `[from memory, verify]`.
- **BITX (2x bitcoin futures, Volatility Shares):** BTC's sourced path over the last 12 months is ~$112.1k (23 Sep 2025, computed in the crypto note [XREF crypto 1]) -> ATH $126,198 (6 Oct 2025) -> ~$58k low (Jun 2026, -54% from ATH) -> $85,686 (23 Sep 2026), i.e. **-23.6% y/y** [XREF snapshot 42-48]. Applying the Section 2.1 formula to that year (gross 0.764, realised vol assumed 60%, 4.5% financing + 1% fee) gives a 2x product at **~0.39x, i.e. about -61%**, vs -24% for spot; at 80% realised vol ~0.29x (-71%). These are model numbers; BITX's actual 12-month return is [NOT FOUND]. Futures roll (contango) adds a further ~5-15%/yr `[from memory, verify]`.
- **Silver 2x (AGQ) and gold-miner 2x (NUGT/JNUG):** 2025 [NOT FOUND]; Jan 2026 silver spike and 30 Jan 2026 crash will have produced extreme path-dependence; a verification target.

### 2.6 When leveraged ETFs help and when they destroy
Help: a low-realised-vol (<=40%) underlying that trends up more than ~2.5x in a year with few
large reversals (NVDA 2023-24; SMCI H2 2023-Q1 2024). Destroy: any 50%+ drawdown en route
(a -50% underlying leg is -75% for 2x and -87.5% for 3x, before drag, and the recovery leg
must then be 4x/8x just to get back), any sideways year at >60% realised vol, and anything held
across a regime change. They have no liquidation risk and no expiry, which is their only
advantage over perps and options; that advantage is offset by the drag being paid every day.

## 3. Crypto perpetuals and margin

### 3.1 Liquidation distance
With leverage L and maintenance margin m (0.5% used here; exchanges use 0.4-1% for BTC/ETH,
more for alts `[from memory, verify]`), a long is liquidated after a price fall of ~1/L - m:
2x -49.5%, 3x -32.8%, 5x -19.5%, 10x -9.5%, 20x -4.5%. Cross-margin delays this at the cost of
the whole account.

### 3.2 Probability of being liquidated before the horizon
For a driftless lognormal, P(min S_t <= b S_0 over [0,T]) = 2 N(ln b / (sigma sqrt T))
(reflection principle). With drift mu the hitting probability is
N((ln b - mu T)/(sigma sqrt T)) + exp(2 mu ln b / sigma^2) N((ln b + mu T)/(sigma sqrt T)).

| leverage | liq. drop | vol 40%, 3m | vol 40%, 12m | vol 60%, 3m | vol 60%, 12m | vol 80%, 12m |
|---|---|---|---|---|---|---|
| 2x | -49.5% | 0% | 9% | 2% | 25% | 39% |
| 3x | -32.8% | 5% | 32% | 18% | 51% | 62% |
| 5x | -19.5% | 28% | 59% | 47% | 72% | 79% |
| 10x | -9.5% | 62% | 80% | 74% | 87% | 90% |
| 20x | -4.5% | 82% | 91% | 88% | 94% | 95% |

With a *bullish* +50%/yr expected return (you are right on direction), 12-month horizon:

| leverage | liq. drop | vol 60% | vol 80% | vol 100% |
|---|---|---|---|---|
| 2x | -49.5% | 16% | 36% | 53% |
| 3x | -32.8% | 38% | 59% | 72% |
| 5x | -19.5% | 62% | 76% | 84% |
| 10x | -9.5% | 81% | 89% | 93% |

Reading: on a 60%-vol asset (BTC in a normal year), a 3x perp held for 12 months is liquidated
about half the time even with no drift and **38% of the time when you are right and the asset is
expected to rise 50%**. A 5x is liquidated more often than not in every column. This is why
sustained leverage almost never survives a 50% drawdown path: the -50% leg liquidates every
position above 2x, and a 2x survives only if the drawdown is *exactly* under 49.5% and the
maintenance call is met.

### 3.3 Funding
Perp funding is paid every 8 h (most venues), typically +0.01%/8h at baseline (=11%/yr) and
0.03-0.10%/8h (33-110%/yr) in crowded longs `[from memory, verify]`. The cascades of the last
12 months, as recorded in the snapshot: 10 Oct 2025, ~$19 bn liquidated in a day, the largest on
record [XREF snapshot 69, 70]; January 2026, $1.7 bn [XREF snapshot 74]; "Black Sunday II",
1 Feb 2026, $2.2 bn, with gold and silver crashing the same day [XREF snapshot 73]; 4-6 Jun 2026,
>$3 bn as BTC went from ~$67k to $59.1k in 48 h [XREF snapshot 47]; 20 Aug 2026, $2.74 bn of
*shorts* liquidated, the largest short-side wipe-out ever [XREF snapshot 72]. The June move is a
-12% two-day drop: by Section 3.1 it liquidates every isolated long at 8x or more, and BTC's
2026 drawdown of -54% from ATH [XREF snapshot 46] liquidates every long at 2x or more that was
opened near the top.

| funding / 8h | annualised | cost on 3x notional (% of equity/yr) | cost on 5x |
|---|---|---|---|
| 0.01% | 11% | 33% | 55% |
| 0.03% | 33% | 99% | 164% |
| 0.05% | 55% | 164% | 274% |
| 0.10% | 110% | 328% | 548% |

At 3x with average funding of 0.03%/8h, the position must return 99% of equity per year just to
pay funding. A "10x" via 3x perps therefore needs the underlying up ~4x within a few months, and
a path with no -33% pullback. Historically BTC has had a >30% drawdown in every calendar year
since 2011 `[from memory, verify]`; 2026's was -54% peak-to-trough [XREF snapshot 46].

## 4. Bitcoin-treasury companies as embedded leverage

Mechanics: a digital-asset-treasury (DAT) company's equity = BTC held x price - debt - preferreds.
Leverage to BTC at mNAV = 1 is (BTC value)/(equity) = about 1.2-1.3x for Strategy (MSTR) with
roughly $8 bn convertible debt and a growing perpetual-preferred stack (STRK, STRF, STRD, STRC,
STRE) against ~$50-70 bn of BTC `[from memory, verify]`. The *second* source of leverage is the
premium (mNAV > 1): while it lasts, at-the-market equity issuance buys more BTC per share than
the share represents, so BTC-per-share rises ("BTC yield"), which justifies the premium - a
reflexive loop that works in both directions.

History. Sourced via the crypto note: Strategy's mNAV fell from ~3.4x (Nov 2024) to
~0.82-0.86x (Apr-Jun 2026) and **0.68x on 3 Aug 2026** [XREF crypto 14, 15]; Trefis (26 Jun 2026)
called it a "40% bitcoin discount" [XREF crypto 15]; Strategy, Satsuma, Smarter Web Company,
Sequans, Nakamoto and Empery Digital have *sold* bitcoin to repay debt, fund operations or buy
back stock (CoinDesk, 24 Jul 2026) [XREF crypto 17]; one in three treasury companies trades below
NAV [XREF crypto 18]. MSTR share price and BTC holdings in Sep 2026: [NOT FOUND] (also not found
by the crypto agent). Intermediate steps `[from memory, verify]`: MSTR ~$543 on 21 Nov 2024 at
the premium peak; ~1.5-2.0x mNAV through mid-2025; ~1.0-1.2x by Nov-Dec 2025 as BTC fell from
the 6 Oct 2025 high; Strategy added a USD cash reserve (~$1.4 bn Dec 2025, later ~$2.25 bn) to
cover preferred dividends; MSCI's Jan 2026 consultation on excluding DATs from its indices ended
without an exclusion [UNVERIFIED]; Metaplanet, Semler (merged into Strive, 2025) and most 2025
"ETH/SOL treasury" SPACs went to mNAV < 1, where issuance is dilutive and the loop reverses.

What a MSTR 10x needs from 0.68x mNAV: the equity is worth (mNAV) x (BTC NAV), so a 10x needs
the product to rise 10x: BTC ~4x (to ~$340k) *with* mNAV back to ~1.7x, or BTC ~6.8x at parity
(ignoring the ~1.2-1.3x balance-sheet leverage, which helps on the way up and forces BTC sales on
the way down [XREF crypto 17]). The discount's own mean reversion to 1.0x is a +47%, not a 10x.
Neither leg is a base case. The preferreds (8-10%
yields at issue `[from memory, verify]`) are the interesting instruments but are not 10x
candidates by construction. **Verdict: DAT equity is levered beta plus a sentiment premium that
2025-26 showed can invert into a discount (0.68x); it does not create 10x optionality that BTC
itself lacks.**

## 5. Prediction markets (Polymarket / Kalshi) as a defined-odds 10x

**Mechanics.** A binary contract priced at 10 cents pays 1 dollar if the event occurs: a 10x
with an implied probability of ~10% (after fees and spread, effectively 8-9 cents of value).
This is the cleanest possible "10x": no path dependence, no vol, no liquidation, known loss
(100%) and known frequency (~90% under fair pricing). It is exactly the martingale bound of
Section 0, made explicit.

**Which contracts pay ~10x.** Anything at 6-12 cents: long-dated macro ("Fed funds below X by
date"), technology and science milestones (model releases, launch dates, FDA decisions by a
deadline), weather (Kalshi's daily/monthly temperature and hurricane markets settle on NOAA
data), geopolitical events, election long shots, and sports futures. Deep science/tech markets
tend to be thin (five-figure, occasionally six-figure USD liquidity) `[from memory, verify]`.

**Where research edge can exist.** (1) Domain expertise on resolution criteria: many contracts
resolve on a specific data source, and the crowd often misreads the rule (2025 saw repeated
disputes on Polymarket's UMA-oracle resolutions, e.g. the Mar 2025 Ukraine minerals-deal market
`[from memory, verify]`). (2) Base-rate literacy in scientific domains (FDA PDUFA outcomes,
clinical-trial readouts, launch-cadence statistics) where the crowd extrapolates news flow.
(3) Correlated long shots that the market prices independently. Against this: the
favourite-longshot bias, documented for decades in betting markets [R5, R6] and found in
prediction markets [R7], means 10-cent contracts on average resolve YES *less* often than 10% -
the naive 10x sleeve has negative expected value before fees.

**Fees and frictions `[from memory, verify]`.** Kalshi charges a per-trade fee of roughly
0.07 x contracts x P x (1-P) dollars (max ~1.75 cents at P = 0.5; ~0.6 cents at P = 0.10) plus
spread; Polymarket historically charged no trading fee on most markets (spread and gas only), with
fees on some categories after the 2025-26 US relaunch [NOT FOUND]. Long-dated contracts also tie
up capital for months at 0% (Polymarket) or with interest on balances (Kalshi introduced
interest on cash in 2025 [UNVERIFIED]).

**Scale (sourced via the crypto note).** Sector volume ~$25.7 bn in Mar 2026, of which Kalshi
~$13 bn and Polymarket ~$10 bn [XREF crypto 62]; Polymarket's POLY token was announced for Q1 2026
alongside its US relaunch but was not live as of Mar 2026, and its Sep 2026 status is [NOT FOUND]
[XREF crypto 63]; Fortune (20 Apr 2026) covered Coinbase's and Robinhood's entry into the sector
(title only seen) [XREF crypto 64]; the crypto note also records a Jun 2026 report of prediction
protocols under investigation, sourced to a secondary blog [XREF crypto 61] - unverified.

**Regulatory status 2026 `[from memory, verify]`.** Kalshi: CFTC-registered designated contract
market; won the 2024 litigation allowing election contracts; through 2025 fought state
gaming regulators over sports event contracts (cease-and-desist letters from Nevada, New Jersey,
Maryland, Ohio, Illinois, Massachusetts and others; mixed district-court results, appeals pending
into 2026); raised at ~$11 bn valuation in Dec 2025 [UNVERIFIED]. Polymarket: barred from US
users since the 2022 CFTC settlement; acquired QCEX (Jul 2025, ~$112 m) to obtain DCM/DCO
licences; CFTC no-action relief in Sep 2025; relaunched a US-regulated venue in late 2025/early
2026; ICE (NYSE parent) invested up to ~$2 bn at ~$8 bn valuation (Oct 2025), later rounds
higher [UNVERIFIED]. CFTC leadership changed in 2025 (a new chair confirmed in Dec 2025
[UNVERIFIED]) with a stated pro-event-contract stance; state-level litigation on sports contracts
was the live legal risk in 2026. Sep 2026 status: [NOT FOUND].

**Verdict.** Prediction markets are the most *honest* 10x instrument: probability and loss
frequency are printed on the screen. They are a good place to deploy *small* capital where the
researcher has a defensible, source-based probability that differs from the market's by a factor
of two or more. They cannot absorb size, and the average 10-cent contract is overpriced.

## 6. Conclusion: which mechanism, and how often you lose

| Mechanism | Underlying move needed for 10x (12-24 m) | P(10x) under fair pricing | Loss frequency / severity | Annual carry | Survives a -50% path? | Best use |
|---|---|---|---|---|---|---|
| 12-m delta-0.2/0.3 call, 40% IV | ~2.0x (+95-104%) | ~10-13% touch, 3-5% at expiry | 78-86% expire worthless | premium 4-6% of notional, fully at risk | Yes (if held to expiry) | Low-vol underlying with a specific 12-m catalyst |
| 12-m delta-0.2/0.3 call, 60% IV | ~2.6x | ~10% touch, 3-4% at expiry | 85-91% | premium 5-9% | Yes | Same, at higher cost |
| 12-m call, 80-100% IV | 3.2-6.5x | ~10% touch, 1-4% | 89-99% | premium 6-12% | Yes | Do not use; buy the underlying |
| 2x daily ETF | 3.5x (40% vol) to 5.4x (100% vol) | n/a (continuous) | -50% underlying = -80 to -88% | 5-6% + drag 15-63% at flat | Barely, then needs 4x to recover | Trending, <=50% vol, <=12 m |
| 3x daily ETF | 2.6x (40% vol) to 6x (100% vol) | n/a | -50% underlying = -93%+ | 10-11% + drag 38-95% at flat | No (economically) | Trending, <=40% vol, <=12 m |
| 3x perp | ~4x within months, no -33% pullback | n/a | Liquidated ~50% of the time in 12 m at 60% vol (38% even with +50% drift) | 33-330% funding | No | Days-to-weeks only |
| DAT equity (MSTR) | BTC ~4x + mNAV 0.68x -> 1.7x | very low | Premium went 3.4x (Nov 2024) -> 0.68x (3 Aug 2026) [XREF crypto 14]; forced BTC sales [XREF crypto 17] | financing via prefs 8-10% | Partly (no liquidation, but dilution/BTC sales) | Not a 10x instrument; discount mean-reversion is ~1.5x at best |
| Prediction-market 10c contract | n/a (event) | ~8-10% (longshot bias) | ~90-92% total loss | none (capital lock-up) | n/a | Small size, source-based edge on resolution |

**Honest assessment.** The best *risk-adjusted* route to a 10x is a 12-month, delta 0.20-0.30
call on an underlying with implied vol at or below ~40-50% where the research supports a specific
reason for the stock to double, and the premium is sized so that its total loss (the 80-90% case)
is affordable. That instrument converts the smallest plausible move (2x) into 10x, survives any
path, has no carry beyond the premium, and pays ~10x if the doubling happens. No instrument does
better than ~1-in-10 without an informational edge, and each added layer of leverage raises the
*required* move (LETF drag, perp funding) or the *loss frequency* (liquidation) without raising
the probability. Leveraged ETFs are second-best and only for trending, low-vol underlyings; perps
are not a 12-24-month instrument at all; DATs are levered beta with a broken premium; prediction
markets are the right tool only when the edge is about an event probability rather than a price.

**Expected loss frequency for a 10x sleeve.** Under fair pricing each bet loses ~90% of the time;
with ten *independent* bets of 10% each, P(at least one 10x) = 1 - 0.9^10 = 65%, and the sleeve's
expected multiple is ~1x before costs (i.e. it is a lottery with a fair price). The bets in this
programme are not independent (all are long risk, long liquidity, long "AI/crypto/commodity"
beta), so the true probability of zero hits is materially above 35%. Kelly sizing makes the point
sharply: with net odds b = 9 and win probability p, f* = (p b - (1-p))/b; at p = 0.10 (fair)
f* = 0; at p = 0.12, f* = 2.2% of capital per bet; at p = 0.15, f* = 5.6%. An edge of two to five
percentage points of probability, which is the most any research process can honestly claim on a
10x bet, justifies single-digit position sizes [R8].

## Sources

No URLs were retrieved in this session (search budget exhausted before the first query; direct
fetch blocked). The items below are (a) the repository code that generated the tables and (b)
academic references given bibliographically for the reader to locate. Market-history statements
in Sections 2.5, 3.3, 4 and 5 are `[from memory, verify]` and have no source here.

- [R1] Black, F., & Scholes, M. (1973). The pricing of options and corporate liabilities. *Journal of Political Economy*, 81(3), 637-654. (Model in Section 1.)
- [R2] Cheng, M., & Madhavan, A. (2009). The dynamics of leveraged and inverse exchange-traded funds. *Journal of Investment Management*, 7(4), 43-62. (Variance-drag formula, Section 2.1.)
- [R3] Avellaneda, M., & Zhang, S. (2010). Path-dependence of leveraged ETF returns. *SIAM Journal on Financial Mathematics*, 1(1), 586-603. (Continuous-time LETF return, Section 2.1.)
- [R4] Coval, J. D., & Shumway, T. (2001). Expected option returns. *Journal of Finance*, 56(3), 983-1009. (Negative average returns to OTM calls, Section 1.3.)
- [R5] Thaler, R. H., & Ziemba, W. T. (1988). Anomalies: Parimutuel betting markets: racetracks and lotteries. *Journal of Economic Perspectives*, 2(2), 161-174. (Favourite-longshot bias, Section 5.)
- [R6] Snowberg, E., & Wolfers, J. (2010). Explaining the favorite-longshot bias: is it risk-love or misperceptions? *Journal of Political Economy*, 118(4), 723-746. (Section 5.)
- [R7] Page, L., & Clemen, R. T. (2013). Do prediction markets produce well-calibrated probability forecasts? *Economic Journal*, 123(568), 491-513. (Calibration of prediction markets, Section 5.)
- [R8] Kelly, J. L. (1956). A new interpretation of information rate. *Bell System Technical Journal*, 35(4), 917-926. (Sizing, Section 6.)
- [R9] `tools/options_10x.py` in this repository (Black-Scholes strike-from-delta, 10x thresholds, lognormal probabilities, 20,000-path Monte Carlo of 10x touch, LETF drag, reflection-principle liquidation probabilities). Run date 2026-09-24. Assumptions: r = 4%, maintenance margin 0.5%, LETF financing 4.5% + 1% fee.
- [X1] `notes/01-market-snapshot.md` (this repo, 2026-09-24), Sources 3, 42-48, 57-61, 69-74 - VIX, BTC path and 2026 low, NVDA price/cap, liquidation cascades. URLs recorded there; search-snippet figures.
- [X2] `notes/themes/crypto.md` (this repo, 2026-09-24), Sources 1, 14-19, 61-64 - BTC one-year change, Strategy mNAV history, DAT bitcoin sales, prediction-market volumes and POLY status.
- [R10] Implied-vol levels for NVDA/TSLA/COIN/MSTR/IBIT: [NOT FOUND] this session; the ranges quoted in Section 1.1 are `[from memory, verify]` (check any options-analytics screen for 12-month ATM IV on the date of use).
