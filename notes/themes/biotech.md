# Theme: Biotech (small/mid-cap, catalyst-driven)

**Date:** 2026-09-24  **Author:** research agent  **Status:** draft (INCOMPLETE – see coverage note)

> **Coverage note (read first).** The session's WebSearch budget (200 calls, shared across all
> parallel agents) ran out after **10** of the ~45 searches planned for this screen. WebFetch and
> curl are blocked, so nothing here was read from a primary page. What *is* search-verified
> (numbers as reported in search-result summaries, attributed to the result set of the query that
> produced them): the BIO/Informa/QLS phase-success framework, XBI returns for 2025 and 2026 YTD,
> the 2026 M&A and IPO state, two event studies on stock reactions, and four catalyst dates
> (Kodiak, Capricor, Invivyd, one HCM trial). **Every price, market cap, cash balance and
> enterprise value in this note is `[NOT FOUND]`** – no quote search ran. The candidate list
> (section 3) is built from recalled knowledge with a cut-off around early 2026 and is tagged
> `[from memory, verify]` throughout; several of the 2026 binary readouts it hinges on
> (MindMed Voyage, Intellia HAELO, Kyverna KYSA-8, Compass COMP006, Capricor HOPE-3) have
> **unknown outcomes to me** and are marked `[NOT FOUND – critical]`. Treat section 3 as a
> verification queue, not a shortlist. Section 5 lists the exact queries for the second pass.

---

## 0. How to read a biotech "10x" (framing for a reader who knows trial statistics)

A small-cap biotech 10x in 24 months is almost never one event. It is a chain:

1. the pre-data market cap is small (typically < $1B, often < $500M);
2. a single pivotal or large randomised readout removes the dominant uncertainty;
3. within 6-12 months an acquirer, or a credible launch narrative, re-rates the equity to a
   multiple of the post-data cap.

Each link has a probability. If P(readout positive) ≈ 0.5 and P(re-rate to 10x | positive) ≈ 0.2,
P(10x) ≈ 0.10. The honest framing is that this is a lottery with a partly known probability;
the only edge is finding a name where the market-implied P(success) is well below the
base-rate-adjusted P(success), or where the post-success value is under-appreciated.

A sobering Kelly check: if the only two outcomes are 10x (p = 0.10) and total loss (p = 0.90),
the Kelly fraction is f* = p − (1−p)/b = 0.10 − 0.90/9 = **0**. A "10 % chance of 10x" bet with
no residual value on failure has no edge at fair odds. Positive expectancy has to come from
(a) p being higher than the market prices, or (b) partial-loss outcomes (cash floor, other
assets). This is why "trading near cash with a binary ahead" is the recurring pattern below.

---

## 1. Why this theme could produce a 10x in 1-2 years

### 1.1 Base rates by phase (the prior every candidate is measured against)

**BIO / Informa (Biomedtracker) / QLS Advisors, 2011-2020** [3][4][5]. Search-verified: 12,728
phase transitions across 9,704 programmes; overall likelihood of approval (LOA) from Phase 1 of
**5.7 % for new molecular entities (small molecules), 9.1 % for biologics, 9.7 % for vaccines**
(as reported in the CPHI summary [5]); selection biomarkers raise success at every phase; rare
disease programmes have higher LOA than chronic high-prevalence diseases; haematology has the
highest LOA from Phase 1 and oncology the lowest.
Phase-transition figures I recall from the same report, to be checked against the PDF [4]
`[from memory, verify]`: Phase 1→2 ≈ 52 %, Phase 2→3 ≈ 29 %, Phase 3→NDA/BLA ≈ 58 %,
NDA/BLA→approval ≈ 91 %, overall Phase 1→approval ≈ 7.9 % (all modalities);
neurology LOA from Phase 1 ≈ 6 %, oncology ≈ 5 %, haematology ≈ 24 %.

**Wong, Siah & Lo, *Biostatistics* 2019;20(2):273-286** [1][2]. Search-verified: 406,038 trial
entries, >21,143 compounds, Jan 2000–Oct 2015; disaggregated by disease, phase, sponsor type,
biomarker use; biomarker-selected trials have higher POS. Headline numbers I recall
`[from memory, verify against Table 2 of [1]]`: overall Phase 1→approval **13.8 %**; oncology
**3.4 %**; Phase 1→2 ≈ 66 %, Phase 2→3 ≈ 58 %, Phase 3→approval ≈ 59 %. The Wong estimate is
roughly double BIO's because of the path-by-path estimator and the earlier window; the two
agree that **Phase 2 is where most programmes die and Phase 3 is roughly a coin-flip-plus**.
A 2025 follow-up on "dynamic" success rates exists [6] – not read.

**Alzheimer's disease specifically** `[from memory, no URL retrieved]`: Cummings et al.,
*Alzheimer's Res Ther* 2014;6:37 reported a 99.6 % failure rate for AD drug candidates
2002-2012. Only three anti-amyloid antibodies have been approved since (aducanumab, withdrawn;
lecanemab; donanemab). For AD, treat any Phase 2 as P(success) ≤ 0.2 regardless of mechanism.

**What this means for pricing.** For a randomised Phase 3 with a replicated Phase 2 effect and
a validated endpoint, the base rate is ~55-60 % success and ~90 % approval given submission.
For psychiatry/neurology with subjective endpoints and functional unblinding (psychedelics,
ketamine-like agents), the effective P(success) is lower than the headline base rate because
Phase 2 effect sizes are inflated by expectancy. For single-arm registrational studies in rare
disease, the risk moves from "does it work" to "will FDA accept the evidence package".

### 1.2 What a positive readout does to a small-cap stock

- Event studies. A 2024 event study of positive Phase 3 oncology results in (mostly smaller)
  biotechs reports an average 3-day abnormal return of about **+5 %** [8]; large-cap biopharma
  show a median +0.8 % on the day (Hwang, *PLOS One* 2013 [9]); a 2022 event study of sponsor
  stock prices vs trial outcomes is at [10]. **The mean is misleading**: for a single-asset
  small cap the distribution is bimodal – most "positive" Phase 3s are expected and priced,
  and the tails are what matter.
- Tails, recent: Abivax (ABVX) had a "record NASDAQ surge" on its Phase 3 ABTECT ulcerative
  colitis induction data in July 2025 [11]; my recollection is a roughly 5-6x move in one
  session `[from memory, verify]`. Negative single-asset Phase 3s in 2024-25 (Cassava, Neumora,
  Athira, Alector) produced one-day drops of −60 % to −90 % `[from memory, verify]`.
- FDA approvals for small caps are usually smaller moves than pivotal data, unless the approval
  itself was doubted (a prior CRL, an AdCom, a novel surrogate) – those are the mispricings.

### 1.3 How often small caps 10x, and how often they lose >80 %

`[NOT FOUND]` – the search for this did not run and I know of no clean published series.
Working estimates, **not sourced** and to be replaced by output of `tools/tenx_screener.py`
once `data/universe_prices_1wk.csv.gz` is fetched locally:
- In a sector bull phase like 2025-26, perhaps 3-6 % of XBI constituents achieve ≥10x over some
  24-month window; in 2022-23 the figure was close to zero.
- Over any 24-month window, 15-30 % of sub-$500M clinical-stage names lose >80 % (failed
  readout, dilutive financing, delisting).
The asymmetry is the whole game: the loss branch is more likely than the 10x branch by a
factor of roughly 3-10.

### 1.4 The 2026 backdrop: money is back

- **XBI**: total return **+35.89 % in 2025**; **+33.41 % YTD as of 17 Sep 2026**, with the
  trailing six months described as one of the strongest stretches on record [13][14][15][16].
  Compounded, that is ≈ +81 % from end-2024 to mid-Sep 2026.
- **M&A**: $106B of biotech deals across 201 transactions by 4 Jun 2026, "on track for best
  year since pre-Covid" (CNBC [17]). H1 2026 tallies differ by scope and cut-off: 50+ M&A deals
  led by Lilly's $25B of spending (BioSpace [18]); $96B across 80 deals with average deal size
  $3.1B vs $2.7B in 2025 (IQVIA [21]); $130-134B (PharmaDossier [25], [24]); $196B for all life
  sciences, +140 % y/y (bioxconomy [22]). Q1 2026 alone >$65B, strongest quarter since 2020, with
  16 deals ≥$1B (PwC [19]). Named deals: Sun Pharma/Organon $12.6B, AbbVie/Apogee $10.7B,
  Merck/Terns $6.9B [17][18][24].
- **IPOs**: window reopened. Kailera Therapeutics priced a $625M IPO (record for a biotech
  IPO), Parabilis Medicines ~$670M in June, 14 biotech IPOs for ~$5B by late June; 11 of the
  first 13 raised ≥$250M [26][27][29]. Public offerings in H1 2026 exceeded all of 2025; Q1
  ~$1.8B. VC: Q1 2026 $6.9B but fewer rounds – capital concentrating in later-stage assets
  [28][31].

Why this matters for 10x hunting: the 10x-ers of 2025 (section 3.4) were mostly bought out.
With pharma paying $7-13B for de-risked Phase 2/3 assets, the exit multiple on a positive
pivotal readout is high – **but only if the entry cap is small**. The larger the cap at entry,
the lower the achievable multiple.

---

## 2. What the market already prices

- **Sector beta is spent.** XBI is up ~81 % since end-2024 [13][14]. In 2023-24 a large share
  of clinical-stage small caps traded below cash; after two +30 % years that discount has
  largely closed `[inference; count of below-cash biotechs NOT FOUND]`. The 2027-28 10x has to
  be idiosyncratic (data + buyout), not a sector re-rating.
- **Acquirers are paying up early.** Apogee was bought at $10.7B on Phase 2 data; Terns at $6.9B
  [17][24]. This pulls forward value into the pre-pivotal window and compresses the post-data
  multiple. It also means a name with clean Phase 2 data and a Phase 3 readout in 2027 may
  already trade at $2-5B – too large for 10x.
- **IPO supply is rising** [26][27]. Historically, heavy issuance precedes weaker small-cap
  biotech returns `[inference, not sourced]`.
- **Regulatory regime** `[from memory, verify]`: 2025 brought FDA leadership turnover, public
  release of complete-response letters, a stated openness to psychedelics and to
  "plausible-mechanism" rare-disease approvals, and a harder line on gene therapy safety after
  the Elevidys deaths. Net effect: approval risk is more idiosyncratic and less predictable
  from precedent than in 2015-2022. The sector's 2026 rally implies the market is looking past
  drug-pricing (MFN) and tariff headlines.
- **Psychedelics** `[from memory, verify]`: Compass's positive COMP005 (June 2025) and atai/
  Beckley's BPL-003 Phase 2b (July 2025) have re-rated the whole group; the market now prices a
  reasonable chance of a first psilocybin approval in 2027. Upside from here is on the launch,
  not on the regulatory event.
- **Obesity** `[from memory, verify]`: after Pfizer/Metsera (~$10B, Nov 2025) and Novo's
  interest, Roche/Zealand, and record IPOs (Kailera), every credible next-gen obesity asset
  already carries a multi-billion valuation. 10x from here requires an entry cap < $500M,
  which excludes the well-known names.

---

## 3. Candidates

**All prices, market caps, cash and EV are `[NOT FOUND]`** (no quote search ran). "Cap band"
is my recollection of the market cap in late 2025 `[from memory, verify]` and is only there to
size the 10x arithmetic; it must be replaced before use. PoS = my subjective probability of the
named catalyst being positive; P(10x by Sep 2028) is the chained probability from section 0.

| Asset (exchange) | Price (date) | Mkt cap | Cap band, late 2025 [mem] | 10x implies | Key catalyst(s), window | PoS / P(10x) | Bear case | Evidence / data confidence |
|---|---|---|---|---|---|---|---|---|
| Acumen Pharmaceuticals (ABOS, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$0.1-0.2B, near or below cash | ~$1-2B: a Phase 2-positive, differentiated-safety AD antibody | ALTITUDE-AD Phase 2 topline (n≈542, 18 mo, iADRS), guided ~late 2026 / early 2027 [mem] | 0.20 / 0.08 | AD base rate; oligomer selectivity unproven clinically; ARIA; cash burn | medium-low / medium |
| Cartesian Therapeutics (RNAC, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$0.3-0.6B | ~$3-6B: first mRNA CAR-T, durable MG responses, buyout | Phase 3 AURORA (Descartes-08, gMG) topline, guided 2026 [mem; result NOT FOUND] | 0.50 / 0.12 | Small Phase 2b; repeat-dosing logistics; argenx/FcRn competition | medium / medium |
| Kyverna Therapeutics (KYTX, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$0.3-0.6B | ~$3-6B: first approved autoimmune CAR-T + MG/MS follow-ons | KYSA-8 (SPS) registrational topline H1 2026 [NOT FOUND – critical]; BLA H2 2026; PDUFA ~2027 | 0.45 / 0.10 | Single-arm; FDA acceptance; autologous CAR-T economics; BMS/Novartis/Cabaletta competition | medium / medium-low |
| Larimar Therapeutics (LRMR, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$0.2-0.4B | ~$2-4B: accelerated approval in FA + buyout (Reata/Biogen comp $7.3B, 2023 [mem]) | BLA (accelerated, FXN biomarker) targeted mid-2026 [mem]; PDUFA ~H1 2027 | 0.40 / 0.12 | FDA rejects frataxin surrogate; historic anaphylaxis signal; single competitor already on market | medium-low / medium |
| Compass Pathways (CMPS, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$1-2B post-COMP005 [mem] | ~$10-20B: approved psilocybin + Spravato-scale launch | COMP006 26-week topline (n≈568) 2026 [NOT FOUND – critical]; NDA; possible PDUFA 2027 | 0.60 / 0.05 | Functional unblinding; −3.6 MADRS is modest; REMS/DEA; cap too large for 10x | medium / medium |
| Intellia Therapeutics (NTLA, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$0.5-1B post-hold [mem] | ~$5-10B: lonvo-z approved + MAGNITUDE resumed clean | HAELO Phase 3 (lonvo-z, HAE) H1 2026 [NOT FOUND – critical]; BLA; PDUFA ~2027; nex-z hold resolution | 0.65 (HAELO) / 0.05 | In vivo CRISPR liver death Oct 2025 [mem]; HAE is crowded; hold may not lift | medium / medium |
| Cabaletta Bio (CABA, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$0.1-0.3B | ~$1-3B: registrational myositis/lupus data + buyout | Registrational cohort data 2026; BLA target 2027 [mem] | 0.40 / 0.08 | Cash runway; crowded CD19 CAR-T; endpoints not agreed | low-medium / low |
| atai Life Sciences (ATAI, Nasdaq; merged with Beckley) | [NOT FOUND] | [NOT FOUND] | ~$0.5-1B | ~$5-10B | BPL-003 Phase 3 start 2026, readout ~2027-28 [mem]; VLS-01, EMP-01 Phase 2 | 0.50 / 0.04 | Readout likely too late for window; unblinding; Compass sets the ceiling | medium / medium |
| MindMed (MNMD, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$0.8-1.5B | ~$10B | Voyage Phase 3 (MM120, GAD) H1 2026 [NOT FOUND – critical]; Panorama, Emerge H2 2026 | n/a until Voyage known | Either already re-rated (cap too big) or dead | medium / low |
| Perspective Therapeutics (CATX, NYSE American) | [NOT FOUND] | [NOT FOUND] | ~$0.5-1B | ~$5-10B (RayzeBio $4.1B, Fusion $2.4B comps [mem]) | 212Pb VMT-α-NET registrational start; VMT01 data 2026-27 | – / 0.02 | No pivotal data by 2028; isotope supply | medium / medium |
| Kailera Therapeutics (ticker [NOT FOUND]; 2026 IPO) | [NOT FOUND] | [NOT FOUND] | multi-$B at IPO | implausible | US Phase 3 of KAI-9531 (HRS9531) starts 2026 [mem] | – / <0.01 | Entry cap too high | search-verified IPO [26][27] |
| Capricor Therapeutics (CAPR, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$0.5-1B | ~$5-10B: implausible for DMD cardiomyopathy | **PDUFA 22 Nov 2026 (delayed)** – search-verified [32][33] | 0.55 / 0.01 | Prior CRL; DMD commercial fragility post-Sarepta | medium / high (date) |
| Kodiak Sciences (KOD, Nasdaq) | [NOT FOUND] | [NOT FOUND] | ~$1B | ~$10B: implausible in anti-VEGF | **DAYBREAK Phase 3 (wet AMD) topline Sep-Dec 2026** – search-verified [32][33] | 0.55 / 0.01 | Eylea HD/Vabysmo; Kodiak's 2022 failures | medium / high (date) |

### 3.1 Neuroscience-relevant names in detail

**Acumen (ABOS)** – sabirnetug (ACU193), IgG2 antibody selective for soluble Aβ oligomers.
Phase 1 INTERCEPT-AD showed CSF target engagement and ARIA-E in the ~10 % range at the top
dose `[from memory, verify]`. ALTITUDE-AD: Phase 2, early AD, n≈542, 18 months, primary iADRS
`[from memory, verify]`. For the 10x arithmetic the key fact to verify is whether it still
trades near or below cash (late-2025 recollection: ~$100-200M cap against ~$200M cash). If
so, the failure branch is partly cushioned and the success branch is a $1-2B+ re-rate
(comps: Lilly paid nothing for donanemab's Phase 2, but partnerships for AD antibodies with a
safety edge have been $0.5-1B upfront `[from memory]`). My PoS 0.20 reflects: donanemab's
Phase 2 (TRAILBLAZER-ALZ, n=257) hit iADRS with p≈0.04 and a 3.2-point difference, lecanemab's
Phase 2b missed its Bayesian primary, and oligomer-selective agents have no positive clinical
precedent. **Kill criteria**: iADRS miss with no plasma p-tau217/amyloid-PET pharmacodynamic
signal; ARIA-E ≥ lecanemab's ~12 %; cash < 12 months without a partner.
Evidence quality: medium-low. Confidence my facts are current: medium.

**Cartesian (RNAC)** – Descartes-08, autologous BCMA CAR-T made with mRNA (no integration, no
lymphodepletion, outpatient, repeat-dosed). Phase 2b in gMG (n=36): ~71 % of Descartes-08 vs
~25 % placebo achieved a ≥5-point MG-ADL improvement at month 3, with durable responders at 12
months `[from memory, verify]`. Phase 3 AURORA (n≈100, MG-ADL primary) topline guided 2026
`[from memory; result NOT FOUND]`. Why 10x is arithmetically possible: MG is a >$3B/yr market
(argenx's efgartigimod `[from memory]`), and a one-course durable therapy from a ~$0.4B company
is a natural buyout. **Kill criteria**: AURORA miss on MG-ADL; CRS/neurotox at scale;
manufacturing failures; cap already >$1.5B when checked (then 10x is off).
Evidence quality: medium. Confidence: medium.

**Kyverna (KYTX)** – KYV-101, fully human anti-CD19 CAR-T (Stanford construct), autologous.
Stiff-person syndrome registrational Phase 2 KYSA-8 (n≈25-30, functional primary) topline
guided H1 2026 → BLA H2 2026 → PDUFA ~mid-2027 `[from memory; result NOT FOUND – critical]`.
Also KYSA-6 in MG. The mispricing thesis: the market treats autologous autoimmune CAR-T as
commercially doomed (cost, apheresis, lymphodepletion), but a first approval in an orphan
indication with no alternatives (SPS) plus MG would set a franchise value of $3-6B.
**Kill criteria**: KYSA-8 miss or FDA refusing single-arm data; ICANS/CRS deaths; dilution at
< $5/share; competitor (BMS CD19 NEX-T, Cabaletta) beating them to approval.
Evidence quality: medium. Confidence: medium-low.

**Compass Pathways (CMPS)** – COMP360 synthetic psilocybin, 25 mg single dose, TRD.
COMP005 (n=258, 25 mg vs placebo, MADRS at week 6): −3.6 points, p<0.001 (June 2025)
`[from memory, verify]`. COMP006 (n≈568, 25/10/1 mg, two doses, primary at week 26):
26-week readout 2026 `[NOT FOUND – critical]`; rolling NDA. For the neuroscientist reader:
the effect size is modest (roughly d ≈ 0.4), functional unblinding is near-total, and the
26-week endpoint after two doses is a harder test than week 6 after one. Approval is now the
base case; the 10x needs a Spravato-scale launch (>$1B/yr `[from memory]`) from a cap that is
probably already $1-2B. **Kill criteria**: COMP006 miss at week 26; FDA asks for a third trial;
REMS that limits sites to <200. Evidence: medium. Confidence: medium.

**MindMed (MNMD)** – MM120 ODT (LSD D-tartrate) 100 µg, GAD. Phase 2b (n=198): ~−7.7 HAM-A
vs placebo at week 12 `[from memory, verify]`. Voyage (Phase 3, GAD) topline H1 2026
`[NOT FOUND – critical]`; Panorama and Emerge (MDD) H2 2026. Decision rule for the second
pass: if Voyage was positive the cap is likely >$2B and 10x is off; if negative, dead. Only a
partial/ambiguous result creates a mispricing.

**atai / Beckley (ATAI)** – BPL-003 intranasal mebufotenin (5-MeO-DMT) benzoate, TRD Phase 2b
(n=193, 12 mg/8 mg/0.3 mg, MADRS day 29): ~5-6 point separation for active doses
`[from memory, verify]`; Phase 3 start 2026, readout probably 2027-28 – at the edge of the
window. Same unblinding caveats as Compass. Not a 10x candidate on timing; watch.

**uniQure (QURE)** – AMT-130 (AAV5-miHTT) Huntington's. Sept 2025: 36-month data, high dose,
~75 % slowing of cUHDRS decline vs propensity-matched external control (p≈0.003), CSF NfL
reduction `[from memory, verify]`; stock roughly tripled. Nov 2025: FDA reportedly withdrew
agreement that the external control could support a BLA; stock roughly halved
`[from memory, verify]`. 2026 status `[NOT FOUND]`. For this reader: n≈12 per dose, external
control, surgical delivery. Rejected for 10x (cap ~$1.5-3B; 10x = $15-30B); a 2-3x on a
resolved accelerated-approval path is plausible and it is the most consequential neuro
regulatory decision in the window.

**Stoke Therapeutics (STOK)** – zorevunersen (STK-001), ASO upregulating SCN1A, Dravet.
Open-label Phase 1/2a plus OLE: ~85 % median reduction in convulsive seizures at 70 mg
regimens, with Vineland cognition/behaviour gains `[from memory, verify]`. Phase 3 EMPEROR
(n≈150) topline 2027 `[from memory, verify]`. Biogen ex-North America partner (Feb 2025,
$165M upfront `[from memory]`). Cap ~$1-2B → 10x implausible; 3-5x on a positive EMPEROR is
plausible (Lundbeck/Longboard $2.6B on Phase 2 `[from memory]`). Watch, not shortlist.

**Rapport Therapeutics (RAPP)** – RAP-219 (TARP-γ8 AMPA modulator), Phase 2a focal epilepsy
positive Sep 2025 `[from memory, verify]`; Phase 2b/3 2026-27; readout inside the window is
uncertain. Cap ~$1B+ → not a 10x. Watch.

**Rejected neuro names with one-line reasons** are in section 4.

### 3.2 Other binary names in detail

**Larimar (LRMR)** – nomlabofusp (CTI-1601), TAT-frataxin fusion, Friedreich's ataxia.
Evidence is biomarker: dose-dependent frataxin increases in skin/buccal cells at 50 mg daily
`[from memory, verify]`; a 2022 clinical hold for anaphylaxis at higher doses was lifted
`[from memory]`. BLA for accelerated approval targeted mid-2026 `[from memory; status NOT
FOUND]` → PDUFA ~H1 2027. Comps: Reata (omaveloxolone) acquired by Biogen for $7.3B (2023)
`[from memory]`. The market's doubt is whether FDA will accept tissue frataxin as "reasonably
likely to predict clinical benefit"; my PoS 0.40. **Kill**: refusal-to-file or CRL on
surrogate grounds; hypersensitivity SAE; cap already >$1B.

**Intellia (NTLA)** – lonvo-z (NTLA-2002, in vivo CRISPR/KLKB1) HAE: Phase 2 ~77-80 % attack
reduction, most 50 mg patients attack-free `[from memory, verify]`; Phase 3 HAELO topline H1
2026 `[NOT FOUND – critical]`. nex-z (NTLA-2001, TTR): Phase 3 MAGNITUDE paused Oct 2025 after
a Grade 4 transaminase elevation and a patient death; clinical hold `[from memory, verify]`.
Mispricing thesis: one death in ~1,200 patients may have caused the market to write off the
whole in vivo platform; if HAELO is positive and the hold is resolved with a monitoring plan,
the re-rate is 3-4x. 10x needs both plus a buyout – P ≈ 0.05. **Kill**: HAELO miss; second
liver SAE; MAGNITUDE terminated.

**Capricor (CAPR)** – deramiocel (allogeneic cardiosphere-derived cells), DMD cardiomyopathy.
CRL July 2025 `[from memory]`; HOPE-3 Phase 3 result `[NOT FOUND – critical; I recall a
positive primary in late 2025 but am not confident]`; **FDA decision 22 Nov 2026 (delayed)**
search-verified [32][33]. Binary inside the window, but 10x = $5-10B for a slow-progression
cardiomyopathy indication in DMD – implausible. 2-3x on approval.

**Kodiak (KOD)** – DAYBREAK Phase 3 wet AMD topline Sep-Dec 2026, search-verified [32][33].
Anti-VEGF is a duopoly market; 10x implausible. Rejected.

**Invivyd (IVVD)** – VYD2311 Phase 3 DECLARATION (COVID-19 antibody), search-verified [32][33].
Tiny cap, small market, policy-exposed. Rejected.

**Anaptys (ANAB)** – an 8-K on a Q4 2026 FDA action appeared in results [37]; contents not
read. `[NOT FOUND]`.

**"Phase 3 SONATA-HCM top-line Q1 2027"** appeared in a search summary [32] without the
sponsor's name; I could not identify the company. `[NOT FOUND]`.

### 3.3 Picks-and-shovels, platforms, AI drug discovery, China, longevity, 2026 IPOs

The honest conclusion: **none of these offers a credible 10x by Sep 2028**; they offer 2-3x
with lower loss probability. Listed for completeness.

- **AI drug discovery** `[from memory, verify]`: Recursion (RXRX) cut its pipeline in 2025;
  REC-4881 (FAP) and REC-617 (CDK7) are the readouts; cap ~$2-3B, heavy burn – a positive
  Phase 2 is a 2x, not 10x. Schrödinger (SDGR): software revenue plus royalties, ~$1.5-2B, not
  binary. Absci (ABSI): ~$0.3-0.5B; ABS-101 (TL1A) Phase 1 and ABS-201 (PRLR, androgenetic
  alopecia) Phase 1/2a 2026 – a striking hair-growth result could be 3-5x; not 10x. Isomorphic,
  Xaira, Chai: private. Insilico listed in Hong Kong (Dec 2025 `[from memory]`).
- **China licensing wave** `[from memory, verify]`: a large and rising share of big-pharma
  in-licensing since 2024 has come from Chinese originators (Pfizer/3SBio, BMS/BioNTech-
  Biotheus, Merck/Hengrui, AZ/CSPC, Summit/Akeso). Tradable exposures are (a) HK-listed
  originators (Akeso, Hengrui, Innovent, Duality) – now large caps; (b) US NewCos built on
  in-licensed Chinese assets that IPO'd in 2026 – Kailera (record $625M IPO [26][27]). Entry
  valuations are high; 10x implausible. Summit (SMMT) is >$10B. No candidate.
- **Radiopharma** `[from memory, verify]`: after RayzeBio ($4.1B, BMS), Fusion ($2.4B, AZ),
  Mariana (~$1B, Novartis), the remaining small caps are Perspective (CATX), Actinium (ATNM,
  FDA required an additional Iomab-B trial – rejected), Cellectar, Telix (ASX, larger),
  Clarity (ASX). Perspective is a 3-5x buyout candidate, not a 10x.
- **Anti-aging / longevity**: BioAge (BIOA) stopped azelaprag in Dec 2024 (transaminases) and
  is a Phase 1 NLRP3 story trading near cash `[from memory]`; Unity wound down; Loyal, Altos,
  Retro, NewLimit are private. **No public longevity asset has a catalyst that could 10x it by
  2028.** Rejected as a category.
- **2026 IPOs** (search-verified list at Xtalks [27]): Kailera ($625M), Parabilis (~$670M,
  June). Both priced at multi-billion valuations into an open window – the wrong end of the
  supply cycle for a 10x. Recommend screening the full Xtalks list for any IPO < $500M cap with
  a 2027 pivotal readout; not done.
- **Obesity next-gen**: Structure (GPCR, oral small-molecule aleniglipron, Phase 2b ACCESS Dec
  2025 `[result from memory, uncertain]`, Phase 3 2026, cap ~$2-3B), Viking (VKTX, ~$3-4B,
  VANQUISH Phase 3 readouts 2026-27), Scholar Rock (SRK, apitegromab SMA CRL Sep 2025 for a
  third-party fill-finish site, resubmission; EMBRAZE muscle-preservation with tirzepatide,
  cap >$3B), Skye (SKYE, nimacimab CB1 Phase 2 missed Sep 2025 – rejected), Metsera (acquired).
  All either too large or failed. **No obesity 10x candidate in the $100M-$3B band** that I can
  name with confidence; second pass should screen for amylin/oral small caps < $500M.
- **RNA / gene editing beyond Intellia** `[from memory]`: Dyne (DYN; DYNE-251 DMD accelerated
  BLA 2026, DYNE-101 DM1 2026; cap ~$2-4B; comp Avidity/Novartis $12B, Oct 2025) – 3x, not 10x.
  Wave (WVE; WVE-N531 DMD NDA 2026, INHBE siRNA obesity, AATD RNA editing; ~$1-1.5B) – platform
  watch. Beam (BEAM; BEAM-302 AATD, BEAM-101 SCD; ~$2-3B) – not 10x. Prime (PRME; ~$0.3-0.5B,
  pivoted to liver; no pivotal data in window) – not 10x. Verve: acquired by Lilly (2025).
- **Oncology bispecifics/ADCs** `[from memory]`: Janux (JANX; JANX007 PSMA-TRACTr, ~$1-2B),
  Nuvalent (>$5B), Summit (>$10B), Merus (acquired by Genmab, 2025). Janux could 3-5x on a
  registrational mCRPC result; not 10x. No candidate.
- **Rare disease others** `[from memory]`: Vera (VERA; atacicept IgAN BLA/PDUFA 2026, ~$2-3B),
  Disc (IRON; bitopertin EPP, ~$2-3B), Savara (SVRA; molgramostim aPAP resubmission, ~$0.5B –
  2-3x on approval), Lexeo (LXEO; LX2006 FA cardiomyopathy pivotal, ~$0.3B – speculative
  watch), Solid (SLDB; SGT-003 DMD, ~$0.3B – DMD gene therapy risk), Neurogene (NGNE; NGN-401
  Rett, HLH death at high dose 2024, low-dose registrational – speculative), Taysha (TSHA;
  TSHA-102 Rett pivotal – speculative). Lexeo, Neurogene, Taysha are sub-$1B names with
  registrational neuro-genetic data possible in the window; none has a cash/cap or comp
  profile I can verify. Second pass.

### 3.4 What actually 10x'd in biotech, Sep 2024 – Sep 2026, and the common thread

All `[from memory, verify]` unless a source is cited. 2026 movers: `[NOT FOUND]` – the query
for 2026 best performers did not run.

| Name | Approx. move | Driver | Buyout? |
|---|---|---|---|
| Cidara (CDTX) | >10x: ~$15-20 (Sep 2024) → $221 Merck offer (Nov 2025) | CD388 long-acting flu prophylaxis, Phase 2b NAVIGATE ~76 % efficacy at top dose (Sep 2025) | Yes, ~$9.2B |
| Abivax (ABVX) | ~8-10x: ~$8-10 (Sep 2024) → $60+ (Jul 2025) → $80-90 (late 2025) | Phase 3 ABTECT induction in UC, two trials, ~16-19 pt remission delta | No (as of my knowledge) |
| Monopar (MNPR) | >10x across 2024-25 | In-licensed ALXN1840 (Wilson's disease) from Alexion into a micro-cap; "more than doubled in 2025" is search-verified [34] | No |
| Praxis (PRAX) | ~5-8x [uncertain] | Ulixacaltamide essential tremor Phase 3 positive (Oct 2025) | No |
| Kodiak (KOD) | ~5-6x | GLOW2 DR Phase 3 positive (2025) | No |
| Metsera | ~4.8x from Jan 2025 IPO to Pfizer's final price (Nov 2025) | Monthly GLP-1/amylin Phase 2 data; Novo/Pfizer bidding war | Yes, ~$10B |
| Verona (VRNA) | ~2.5-3x | Ohtuvayre launch → Merck $10B (Jul 2025) | Yes |
| EyePoint (EYPT) | +140.5 % in 2025 (search-verified [34]) | Duravyu Phase 3 | No |
| Structure (GPCR) | +127 % over the year to the article date (search-verified [39]) | Oral GLP-1 Phase 2b | No |

Common thread: (i) entry cap < $1B (Cidara, Abivax, Monopar, Kodiak); (ii) a single large
randomised readout that removed the dominant uncertainty; (iii) an acquirer within 6-12
months in the two cleanest cases (Cidara, Metsera); (iv) one case of an in-licensed late-stage
asset dropped into a micro-cap shell (Monopar). **None was a platform, AI, or tools story.**
The 2025 crop also had an unusually strong sector tailwind (XBI +36 %), which the second
pass should not assume for 2027-28.

---

## 4. Rejected candidates and why

Neuro / psychiatry
- **Anavex (AVXL)** – blarcamesine; negative CHMP opinion in late 2025 `[from memory, verify]`;
  data-integrity concerns for years. Low evidence quality.
- **Annovis (ANVS)** – buntanetap; Phase 2/3 in AD missed primary (2024); Phase 3 with serial
  redesigns; management credibility. Low evidence quality.
- **Cassava (SAVA)** – simufilam failed two Phase 3s (Nov 2024); dead as an AD story.
- **Athira (ATHA)** – fosgonimeton failed Phase 2/3 (2024).
- **Alector (ALEC)** – latozinemab INFRONT-3 (FTD-GRN) missed (Oct 2025 `[from memory]`).
- **INmune Bio (INMB)** – XPro AD Phase 2 missed primary (2025).
- **Prothena (PRTA)** – birtamimab AFFIRM-AL failed (2025); PRX012 too early.
- **Cognition (CGTX)** – zervimesine Phase 2 signals only; no pivotal in window; micro-cap
  financing risk. Speculative, not rejected on science – rejected on timing/cash.
- **uniQure (QURE)** – see 3.1; cap too large for 10x.
- **Xenon (XENE)** – azetukalner X-TOLE2 result `[NOT FOUND]`; cap ~$3B+ – too large.
- **Praxis (PRAX)** – already re-rated in 2025; cap likely several $B.
- **Denali (DNLI)** – tividenofusp Hunter PDUFA early 2026 `[result NOT FOUND]`; cap ~$3B.
- **Sage, Cerevel, Intra-Cellular, Karuna, Longboard, Vigil** – acquired 2024-25.
- **Neumora (NMRA)** – navacaprant Phase 3 failed (Jan 2025).
- **Marinus (MRNS)** – failed and sold.

Obesity / metabolic
- **Viking (VKTX)** – cap ~$3-4B; oral formulation tolerability issues (Aug 2025); 10x = $30-40B.
- **Structure (GPCR)** – cap ~$2-3B; 10x implausible.
- **Scholar Rock (SRK)** – cap >$3B.
- **Skye (SKYE)** – nimacimab missed (Sep 2025).
- **Metsera, Verve, Terns, Apogee** – acquired.
- **Kailera** – 2026 IPO at multi-$B valuation.

Gene editing / RNA
- **CRISPR Tx (CRSP), Beam (BEAM), Dyne (DYN), Wave (WVE)** – caps too large for 10x; 2-3x
  stories at best.
- **Prime (PRME)** – no pivotal data inside window.
- **Sarepta (SRPT)** – Elevidys deaths; not a small cap either.

Oncology / radiopharma
- **Summit (SMMT), Nuvalent (NUVL), Revolution (RVMD)** – too large.
- **Actinium (ATNM)** – FDA required another Iomab-B trial; micro-cap.
- **Iovance (IOVA)** – commercial disappointment, no binary.
- **Janux (JANX)** – interesting, but 10x = $10-20B.

Platforms / tools / AI
- **Recursion, Schrödinger, Absci, Twist, Ginkgo** – no binary that can 10x; see 3.3.
- **Any CDMO/CRO** – cyclical, 2x at most.

Longevity
- **BioAge, Unity, and all private longevity companies** – no investable catalyst.

Other in-window binaries rejected on cap or market size
- **Kodiak (KOD), Capricor (CAPR), Invivyd (IVVD), Vera (VERA), Disc (IRON), Savara (SVRA)** –
  binary events in the window but the success-case cap is < 3x the current one.

---

## 5. What I could not verify (and the exact queries for the second pass)

Critical unknowns (outcomes of 2026 events that decide whether a name is alive):
1. MindMed Voyage Phase 3 topline (H1 2026) – `MindMed MM120 Voyage Phase 3 topline results 2026`
2. Intellia HAELO Phase 3 topline and nex-z hold status – `Intellia lonvo-z HAELO results 2026`;
   `Intellia MAGNITUDE clinical hold update 2026`
3. Kyverna KYSA-8 SPS topline and BLA status – `Kyverna KYV-101 stiff person syndrome KYSA-8 topline 2026`
4. Compass COMP006 26-week data and NDA timing – `Compass Pathways COMP006 26-week results NDA 2026`
5. Capricor HOPE-3 result and the 22 Nov 2026 PDUFA – `Capricor HOPE-3 topline deramiocel PDUFA November 2026`
6. Cartesian AURORA timing/result – `Cartesian Therapeutics Descartes-08 AURORA Phase 3 topline`
7. Acumen ALTITUDE-AD timing, cash, market cap – `Acumen Pharmaceuticals ALTITUDE-AD topline timing 2026 cash`
8. Larimar BLA status – `Larimar nomlabofusp BLA submission accelerated approval 2026`
9. uniQure AMT-130 FDA path 2026 – `uniQure AMT-130 FDA accelerated approval 2026 update`
10. Xenon X-TOLE2, Denali PDUFA, Structure ACCESS results, Stoke EMPEROR timing.

Prices, caps, cash (all `[NOT FOUND]`): for every ticker in section 3, `"<ticker> market cap"`,
`"<company> cash and cash equivalents June 30 2026 runway"` (10-Q summaries appear in search
results; EDGAR itself is blocked).

Base-rate numbers to confirm against primary tables:
11. Wong et al. 2019 Table 2 phase-transition values (66.4 / 58.3 / 59.0 / 13.8 / 3.4) [1].
12. BIO 2011-2020 phase-transition values (52.0 / 28.9 / 57.8 / 90.6 / 7.9; neurology ~5.9,
    oncology ~5.3, haematology ~23.9) [4].
13. Cummings 2014 99.6 % AD failure rate – no URL retrieved.
14. Frequency of ≥10x in 24 months and of >80 % loss among XBI constituents – no source; compute
    with `tools/tenx_screener.py` on locally fetched data.

Market reaction claims to confirm:
15. Abivax one-day move on 23 Jul 2025 (I recall ~5-6x) [11].
16. Cidara: Sep-2024 price and the $221/share Merck terms (Nov 2025).
17. Monopar, Praxis, Kodiak, Metsera, Verona magnitudes in 3.4.
18. 2026 top performers – `biotech stocks best performers 2026 year to date 500%`.

Deal comps to confirm: Reata/Biogen $7.3B (2023); Avidity/Novartis $12B (Oct 2025); RayzeBio
$4.1B; Fusion $2.4B; Mariana ~$1B; Lundbeck/Longboard $2.6B; Pfizer/Metsera ~$10B; Merck/Cidara
$9.2B; Merck/Verona $10B; Lilly/Verve $1.3B.

Regulatory-regime claims in section 2 (FDA leadership, CRL publication, psychedelic posture,
gene therapy stance, MFN/tariffs) – all `[from memory, verify]`.

Not researched at all: the Xtalks 2026 IPO list [27] for sub-$500M names; amylin/oral obesity
small caps < $500M; Lexeo/Neurogene/Taysha/Solid registrational timing; Anaptys 8-K [37];
identity of the SONATA-HCM sponsor [32].

---

## Sources

All accessed 2026-09-24 via WebSearch result summaries; no page was fetched directly.

1. Wong CH, Siah KW, Lo AW. Estimation of clinical trial success rates and related parameters. *Biostatistics* 2019;20(2):273-286 – https://academic.oup.com/biostatistics/article/20/2/273/4817524
2. Corrigendum to [1] (PMC) – https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6409416/
3. BIO, Clinical Development Success Rates and Contributing Factors 2011-2020 (landing page) – https://www.bio.org/clinical-development-success-rates-and-contributing-factors-2011-2020
4. BIO / Informa / QLS report PDF – https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf
5. CPHI Online summary of [4] (NME 5.7 %, biologics 9.1 %, vaccines 9.7 %) – https://www.cphi-online.com/news/clinical-development-success-rates-and-contributing-factors-2011-2020-new-report/
6. Dynamic clinical trial success rates for drugs in the 21st century (PMC, 2025) – https://pmc.ncbi.nlm.nih.gov/articles/PMC12572394/
7. Benchmarking R&D success rates of leading pharmaceutical companies, FDA approvals 2006-2022 (ScienceDirect) – https://www.sciencedirect.com/science/article/pii/S1359644625000042
8. Event study: positive Phase III oncology results and short-term abnormal returns of biotechnology companies (2024, ResearchGate) – https://www.researchgate.net/publication/400071622_How_do_positive_Phase_III_clinical_trial_results_for_oncology_drugs_affect_the_short-term_abnormal_stock_returns_of_biotechnology_companies_within_a_three-day_event_window_around_the_announcement
9. Hwang TJ. Stock market returns and clinical trial results of investigational compounds: an event study of large biopharmaceutical companies. *PLOS One* 2013 – https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0071966
10. The reaction of sponsor stock prices to clinical trial outcomes: an event study analysis (PMC) – https://pmc.ncbi.nlm.nih.gov/articles/PMC9439234/
11. Flot.bio, "Abivax's record NASDAQ stock surge after Phase 3 data" – https://flot.bio/abivax-biotech-stock-phase-3/
12. Lund University student paper, event study on biotech stock prices – https://lup.lub.lu.se/student-papers/record/8993662/file/8993663.pdf
13. XBI overview and returns (StockAnalysis) – https://stockanalysis.com/etf/xbi/
14. XBI performance history (FinanceCharts) – https://www.financecharts.com/etfs/XBI/performance
15. XBI performance (Yahoo Finance) – https://finance.yahoo.com/quote/XBI/performance/
16. XBI performance (Morningstar) – https://www.morningstar.com/etfs/arcx/xbi/performance
17. CNBC, 4 Jun 2026, "Biotech M&A hits $106 billion, on track for best year since pre-Covid" – https://www.cnbc.com/2026/06/04/biotech-ma-dealmaking-pharma-106-billion.html
18. BioSpace, "Biopharma strikes 50+ M&A deals in H1, led by Lilly's $25B spend" – https://www.biospace.com/business/biopharma-strikes-50-m-as-deals-in-h1-led-by-lillys-25b-spend
19. PwC, Pharmaceutical and life sciences: US Deals 2026 midyear outlook – https://www.pwc.com/us/en/industries/health-industries/library/pharma-life-sciences-deals-outlook.html
20. J.P. Morgan, Biopharma and Medtech Deal Reports Q2 2026 – https://www.jpmorgan.com/insights/markets-and-economy/outlook/biopharma-medtech-deal-reports
21. IQVIA, Biopharma M&A mid-year 2026 update – https://www.iqvia.com/locations/emea/blogs/2026/07/biopharma-ma-mid-year-2026-update
22. bioxconomy, "Life sciences deals surge to $196bn" – https://www.bioxconomy.com/partnering/ife-sciences-deals-surge-to-196bn-with-early-stage-asset-demand
23. BioBucks, Biotech M&A tracker 2026 – https://www.biobucks.co/biotech-ma-tracker-2026
24. Life Science Daily, "Biopharma M&A 2026: every $1B+ deal" – https://lifesciencedaily.news/biotech-ma-2026-every-1b-deal-so-far-and-what-is-driving-them/
25. PharmaDossier, "2026 biopharma M&A by the numbers" – https://pharmadossier.com/blog/biopharma-ma-deals-by-the-numbers-2026
26. Labiotech, "After the drought, biotech IPO activity begins to pick up in 2026" – https://www.labiotech.eu/trends-news/biotech-ipo-2026/
27. Xtalks, "Pharma and biotech IPOs of 2026: a running list" – https://xtalks.com/pharma-and-biotech-ipos-of-2026-a-running-list-4695/
28. BioPharma Dive, "Biotech startup funding gap widens despite rebound in VC investment" (H1 2026) – https://www.biopharmadive.com/news/biotech-venture-capital-funding-2026-first-half/824881/
29. BioPharma Dive, "'The window's open': at BIO, investors take stock of a growing class of biotech IPOs" – https://www.biopharmadive.com/news/bio-2026-ipo-biotech-performance-predictions/823474/
30. Ropes & Gray, "From volatility to vitality: how 2025 reset the life sciences market" (Mar 2026) – https://www.ropesgray.com/en/insights/alerts/2026/03/from-volatility-to-vitality-how-2025-reset-the-life-sciences-market-and-whats-next-for-2026
31. D. Crean, "What makes a biotech company financeable in 2026?" – https://davidhcrean.substack.com/p/what-makes-a-biotech-company-financeable
32. MarketBeat via Yahoo Finance, "3 small-cap biotechs with binary catalysts on the calendar" (Kodiak DAYBREAK Sep-Dec 2026; Capricor 22 Nov 2026; Invivyd DECLARATION; SONATA-HCM Q1 2027) – https://finance.yahoo.com/healthcare/articles/3-small-cap-biotechs-binary-145000650.html
33. Same article, Globe and Mail syndication – https://www.theglobeandmail.com/investing/markets/stocks/IVVD/pressreleases/4591552/3-small-cap-biotechs-with-binary-catalysts-on-the-calendar/
34. Nasdaq/Zacks, "What awaits these 4 biotech stocks that more than doubled in 2025" (IONS, GPCR, MNPR, KOD; EYPT +140.5 %) – https://www.nasdaq.com/articles/what-awaits-these-4-biotech-stocks-more-doubled-2025
35. Insider Monkey, "11 best performing biotech stocks so far in 2025" – https://www.insidermonkey.com/blog/11-best-performing-biotech-stocks-so-far-in-2025-1605866/
36. Curved Trading, "Best small cap biotech stocks 2026: Phase 3 catalyst guide" – https://curvedtrading.com/articles/en/investing/best-small-cap-biotech-stocks-2026-readouts/
37. AnaptysBio 8-K (FY2026) exhibit – https://www.sec.gov/Archives/edgar/data/0001370053/000119312526396690/anab-ex99_1.htm
38. Catalyst calendars surfaced by search (none read): BioPharmCatalyst – https://www.biopharmcatalyst.com/calendars/fda-calendar ; BPIQ – https://app.bpiq.com/pdufa-calendar ; BiopharmaWatch – https://www.biopharmawatch.com/fda-calendar ; RTTNews – https://www.rttnews.com/corpinfo/fdacalendar.aspx ; MarketBeat – https://www.marketbeat.com/fda-calendar/upcoming/ ; Assyro – https://www.assyro.com/tools/pdufa-calendar/2026 ; Endpoint Arena – https://endpointarena.com/catalysts ; BioStockInfo – https://www.biostockinfo.com/calendar/ ; Dan Sfera – https://dansfera.com/ ; FDA Tracker – https://www.fdatracker.com/fda-calendar/ ; Biotech Edge – https://biotech-edge.com/pdufa-calendar
39. Yahoo Finance, "3 biotech stocks Wall Street analysts are bullish on for 2026" (Structure +127.2 % over the year) – https://finance.yahoo.com/news/3-biotech-stocks-wall-street-131000681.html
40. NBER w27176, Estimating probabilities of success of vaccine and other anti-infective programs – https://www.nber.org/system/files/working_papers/w27176/w27176.pdf
41. DIA Global Forum, "What are the chances of getting a cancer drug approved?" (May 2019) – https://globalforum.diaglobal.org/issue/may-2019/what-are-the-chances-of-getting-a-cancer-drug-approved/
42. Wong, Siah, Lo, oncology success rates (SSRN) – https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3355022

References recalled without a retrieved URL (verify before citing): Cummings JL et al., *Alzheimer's Res Ther* 2014;6:37; company press releases for COMP005 (Compass, Jun 2025), BPL-003 Phase 2b (atai/Beckley, Jul 2025), MM120 Phase 2b (MindMed, 2024), NAVIGATE (Cidara, Sep 2025), ABTECT (Abivax, Jul 2025), AMT-130 36-month (uniQure, Sep 2025), MAGNITUDE pause (Intellia, Oct 2025), Descartes-08 Phase 2b (Cartesian, Jul 2024), Essential3 (Praxis, Oct 2025).
