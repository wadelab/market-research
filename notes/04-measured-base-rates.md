# Measured base rates: 10x within 24 months, US common stocks 2014-2026

**Date:** 2026-09-25 (data as of 2026-09-24/25)  **Data:** `data/universe_prices_1wk.parquet`
(5,277 currently listed US common stocks, weekly closes from Stooq, split-adjusted, 2014-10 to 2026-09)
and `data/universe_meta.csv` (market cap and shares from the Nasdaq screener, 2026-09-24).
**Code:** `tools/tenx_screener.py`; outputs in `data/derived/`. Reproduce with

```
uv run python tools/tenx_screener.py data/universe_prices_1wk.parquet --meta data/universe_meta.csv \
    --min-price 1 --out data/derived/tenx_events_730d_min1usd.csv --fixed-out data/derived/fixed_start_rates_0101.csv
```

## 0. What this measures, and the two biases

For each start date, the share of stocks (close >= $1) whose **maximum weekly close within the next
730 days** reached 3x, 5x or 10x the start close. This is the base rate for "buy on a fixed date and
hold up to two years, selling at the top" — the most generous definition short of trough-picking.

1. **Survivorship.** The universe is stocks listed *today*. Companies that failed and were delisted are
   absent from the denominator, and companies acquired after a 10x are absent from the numerator.
   The first effect dominates, so **true rates are lower than the numbers below.**
2. **Market-cap buckets are approximate.** Historical cap = close x today's share count. For companies
   that diluted heavily (typically after reverse splits) this overstates the old cap by orders of
   magnitude and drops some micro-caps into the large-cap buckets. The ALL rows use prices only and
   are unaffected; the bucket rows are indicative.

## 1. Fixed-start base rates, all stocks (close >= $1)

Start = first trading day on or after 1 January.

| Start | Alive | P(>=3x) | P(>=5x) | P(>=10x) | n(10x) | Median max ratio | Censored |
|---|---|---|---|---|---|---|---|
| 2015-01-02 | 2,380 | 1.4 % | 0.1 % | **0.04 %** | 1 | 1.30 | |
| 2016-01-01 | 2,504 | 5.8 % | 1.3 % | **0.2 %** | 5 | 1.50 | |
| 2017-01-06 | 2,618 | 5.5 % | 1.5 % | **0.2 %** | 5 | 1.38 | |
| 2018-01-05 | 2,753 | 3.5 % | 0.7 % | **0.3 %** | 7 | 1.25 | |
| 2019-01-04 | 2,923 | 9.8 % | 3.1 % | **1.0 %** | 29 | 1.46 | |
| 2020-01-03 | 3,075 | 14.6 % | 6.2 % | **1.9 %** | 58 | 1.54 | |
| 2021-01-01 | 3,366 | 8.2 % | 2.5 % | **0.5 %** | 17 | 1.49 | |
| 2022-01-07 | 3,858 | 2.3 % | 0.7 % | **0.05 %** | 2 | 1.12 | |
| 2023-01-06 | 4,006 | 8.8 % | 2.6 % | **0.6 %** | 23 | 1.42 | |
| 2024-01-05 | 4,168 | 10.0 % | 3.8 % | **0.9 %** | 38 | 1.40 | |
| 2025-01-03 | 4,442 | 9.5 % | 2.9 % | 0.5 % | 24 | 1.34 | yes (window open) |
| 2026-01-02 | 4,740 | 3.5 % | 0.9 % | 0.2 % | 9 | 1.24 | yes |

**Pooled 2015-2024 (31,651 stock-years): P(10x) = 0.58 %, P(5x) = 2.4 %, P(3x) = 7.2 %.**

Starting on 24 September instead (the research start date) gives the same picture: 0.0-0.3 % in
2014-2018, 1.8 % (2019) and 1.6 % (2020), 0.03 % (2021), 0.3 % (2022), 0.9 % (2023), 1.1 % (2024,
censored). Full tables in `data/derived/fixed_start_rates_0924.csv`.

**Reading.** The unconditional base rate is about half a percent per year and never exceeded 2 % in
any start year, including the 2020-21 liquidity surge. Years starting near a market low (2019, 2020,
2023) run 3-10x higher than years starting near a high (2018, 2021, 2022). This is hypothesis H5 in
`02-framework.md`, now measured. The 2022 start (rates rising, CAPE high) produced 2 ten-baggers out
of 3,858 stocks, which is the closest analogue to a 2026 start on macro grounds.

## 2. By starting market cap (indicative; see bias 2)

Pooled 2015-2024, 1 January starts:

| Approx. starting cap | Stock-years | P(>=3x) | P(>=5x) | P(>=10x) |
|---|---|---|---|---|
| < $50M | 1,078 | 20.8 % | 7.9 % | **2.0 %** |
| $50-300M | 4,581 | 13.0 % | 4.9 % | **1.3 %** |
| $300M-2B | 10,494 | 8.4 % | 2.7 % | **0.6 %** |
| $2-10B | 8,908 | 4.2 % | 1.1 % | **0.25 %** |
| $10-50B | 4,462 | 3.1 % | 0.9 % | 0.3 % |
| > $50B | 2,010 | 3.8 % | 0.9 % | 0.2 % |

Hypothesis H1 (small caps dominate) holds: the sub-$300M rate is 5-8x the $2B+ rate. But the
small-cap rows are also where the failure rate is highest and where the survivorship bias bites
hardest; the true sub-$50M 10x rate is lower than 2 % once the delisted are counted. The $10B+
rows are contaminated by mis-estimated caps (see bias 2); the genuine large-cap 10x-ers in the
episode list are few: Palantir (from ~$18B, Feb 2023), MicroStrategy (Nov 2022), Nebius (Oct 2024),
SanDisk (Feb 2025), Western Digital (Jun 2024), Carvana, Wayfair and Roku from the March 2020 low,
Novavax 2019-21, Enphase 2019-21, and the AMC meme episode.

## 3. What happens after a 10x

1,250 trough-inclusive episodes (any entry week, 521 symbols). Median time from entry to peak
546 days; a quarter took under 343 days. Of the 951 episodes whose peak is at least 12 months old:

| Statistic | Value |
|---|---|
| Median current price / peak price | **0.17** (an 83 % give-back) |
| 25th percentile current / peak | 0.03 |
| Share still >= 10x from entry today | 22.5 % |
| Share still >= 5x from entry today | 33.6 % |
| Share below 2x from entry today | 51 % |

Half of all 10x-ers are back below 2x within a few years, and the typical one lost five-sixths of its
peak value. A 10x strategy without a sell discipline captures little of the 10x. This is the
strongest single finding in the dataset and it matches the SPAC/IPO evidence in `00-base-rates.md`.

## 4. Comparison with the literature-based estimate

`00-base-rates.md` estimated 0.1-1 % per year for a favourable window and ~0 otherwise, from
triangulation. The measured survivor-biased numbers are 0.04-1.9 % by year, 0.58 % pooled. The
estimate stands. The required screen lift for a positive-EV programme (~9 % hit rate, see
`00-base-rates.md` §6) is therefore **15x the pooled base rate and 5x the best start-year rate**,
and no feature measured here (size, year) delivers more than about 3-4x on its own.

## 5. Open items

- Delisted-stock data (CRSP via WRDS, if available through the university) would remove bias 1 and
  is the only way to get a true base rate.
- Historical share counts (quarterly 10-Q/10-K) would fix bias 2 for the names that matter.
- Repeat the analysis on the UK zip (`--include-uk`) and on a crypto top-200 history.
