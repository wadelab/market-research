# Deep dive: IREN Limited (IREN, Nasdaq)

**Date:** 2026-09-24  **Price at writing:** $47.05 (2026-09-24 close, Stooq)  **Market cap:** $18.5B
(Nasdaq screener, 2026-09-24; the screen's search figure was ~$17.6B [43]). 24-month high $76.41 on
2025-11-05 (8.5x from the Sep 2024 close); now 62 % of that high. **Evidence grade:** high for operating figures (8-K, 10-K in search results),
medium for the cap.

## Thesis in one paragraph

IREN is a former Bitcoin miner converting ~3 GW of contracted power into GPU cloud capacity. It
reported $1B of operating annualised revenue (ARR) on 26 Aug 2026 [41] and has guided to $4B of
contracted ARR operational by 31 Dec 2026, ~85 % of which was under contract in Jul 2026 [43], with
Microsoft and NVIDIA among the customers [43]. If the Dec 2026 checkpoint is met and a second and
third GW are contracted with investment-grade counterparties, 2028 revenue in the $10-15B range at
~40 % EBITDA margin (Nebius's guided margin [36]) would, at the 12-15x revenue multiple the market
pays Credo and Marvell [78][85], be worth ~$120-225B. That is the only path to 10x, and it requires
the market to value IREN like a semiconductor company rather than like CoreWeave.

## What 10x implies

- Implied market cap: ~$176B (on $17.6B).
- Precedent: CoreWeave peaked in the tens of billions ($39-49B in Sep 2026 [33][35]); Nebius is
  "almost certainly in the tens of billions" on $3.0-3.4B guided revenue [36][39]. **No neocloud has
  been worth $176B.** The precedent is in semis (Marvell $190-212B [84][85]), which is why the
  thesis depends on multiple, not just growth.
- Required revenue at 12-15x: $12-15B; at CoreWeave-type multiples (~5x, [from memory, verify]):
  $35B, which is implausible by 2028.

## Catalyst timeline (next 24 months)

| Date / window | Event | Why it matters | Source |
|---|---|---|---|
| ~Nov 2026 | FY27 Q1 report | First read on ARR ramp after the Aug 2026 miss | ai-semis.md [44][45] |
| 31 Dec 2026 | $4B contracted ARR operational | The checkpoint the thesis rests on | [43] |
| 2027 | Additional GW-scale contracts | Needed for the 2028 revenue path | [101] |
| continuous | Neocloud credit (CoreWeave $51.6B debt, D/E 10.3; Nscale going-concern language) | Contagion channel | [34], ai-semis.md §2 |

## Base / bull / bear (subjective)

- **Bull (P ~5 %):** ARR checkpoint met, hyperscaler multi-year deals, semis-style multiple: 8-12x.
- **Base (P ~45 %):** ARR delivered late or partially, further equity/convert issuance, stock
  range-bound to 2x.
- **Bear (P ~50 %):** neocloud financing chain breaks (a CoreWeave/Nscale event), start-up customers
  cannot fund commitments, GPUs depreciate faster than contracts amortise: -60 to -85 %.

## Kill criteria

1. Operating ARR < $3B at 31 Dec 2026.
2. Any contract cancellation or repricing >10 % below contract.
3. Share count growth >30 % over 12 months without a matching ARR step-up.
4. A CoreWeave or Nscale credit event.

## What the sceptics say

FY26 AI-cloud revenue was only $128.8M [41]; the Q4 FY26 miss sent the stock -8 % on 28 Aug 2026
[44][45]; the customer list is start-up heavy (Perplexity, Figure, Together, Fluidstack, Fireworks,
fal, Hume [43]) and their funding is circular with the GPU vendors; the BIS 2026 report and the
depreciation argument (ai-semis.md §2) apply directly. Capex is equity/convert funded, so even a
successful build dilutes the 10x.

## Position-sizing logic

With P(10x) ~5 % and P(loss >60 %) ~50 %, `tenx_math.py ev --p10x 0.05 --ploss 0.5 --loss 0.7`
gives EV ~ +0.10 per unit and a Kelly fraction near 1 %. This is a small position or none; it is
one of the same-thesis cluster (IREN, APLD, miner conversions) and should be sized as one bet.
IV is likely 80-100 % [from memory, verify], so LEAPS add nothing over the stock.

## Open questions / data to collect

- Current price, share count, convert terms (10-Q).
- Which customers are contracted for the $4B and on what tenor.
- IV surface (to confirm options are not the instrument).

## Sources

All bracketed numbers refer to `notes/themes/ai-semis.md` Sources list.
