# Poster source traceability

**Content authority.** `ResearchPaper-06058747-Muhammad Faseeh Memon-Templeton.pdf` —
293 pages, SHA-256 `f371a8fe86ab6380bc5ee0426f9de708593277cb36d9bc6746b5cb14529df7aa`.
Exact submitted title: *Predicting Drinking-Water Contamination Risk and Ranking Monitoring
Technologies Under Uncertainty: An Evidence-Aware, Leakage-Safe Decision-Support Framework*.

Every number and every figure on `poster_final.pdf` traces to a page of that document. No value
was refitted, recomputed, aggregated or interpolated for the poster. The only transformations
applied are **selection, ordering, re-typesetting at poster scale, and colour mapping**.

Page references are **physical PDF pages** of the submitted file, not printed page numbers.

---

## How this was verified

`scripts/verify_poster_numbers.py` runs two automated checks and exits non-zero on any failure:

1. **Ledger check** — each of the 53 poster values is looked up in the submitted PDF *on the
   page it is attributed to below*. A value that is not on its stated page fails.
2. **Coverage check** — every numeric token extracted from the rendered `poster_final.pdf` must
   be either in the ledger or in a declared structural whitelist (figure references, axis tick
   values, reference years, the author's CID). An untraceable number on the poster fails.

Last run: **PASS**, 53 of 53 ledger values confirmed, 0 untraced tokens.

```
python scripts/verify_poster_numbers.py "<path to>/ResearchPaper-06058747-Muhammad Faseeh Memon-Templeton.pdf"
```

---

## Poster figures

### P1 — The five-stage evidence-to-action chain

| Field | Value |
|---|---|
| Where | Full-width band beneath the title block |
| Submitted source | Figure 3.1 (p43) and Figure 3.6 (p58) |
| Active thesis source | `THESIS_LATEX_BUILD/chapters/Chapter3.tex`, asset `figures/figure_3-1.png` |
| Built by | TikZ, inline in `poster_final.tex` (no raster asset) |
| Transformations | Layout only: the five stages are laid out horizontally rather than vertically. Stage names and the five permitted terminal outputs are **verbatim** from Figure 3.1. The two abstention exits are compressed into one sentence carrying both conditions. The four-item "framework rules" panel of Figure 3.1 is **omitted** for space; the rule that no output certifies water as safe to drink is retained. |
| Numerical content | None — this figure carries no data values. |
| Status | Verified against Figure 3.1 by direct reading of `figures/figure_3-1.png`. |

### P2 — Leakage-safe validation

| Field | Value |
|---|---|
| Where | Column 2 |
| Submitted source | Figure 4.4 panel a (p70); Table 4.3 (p71); Table 4.4 (p72); Section 4.3 (p68) |
| Active thesis source | `chapters/Chapter4.tex`, asset `figures/figure_4-4.pdf` |
| Final build script (thesis) | `CLAUDE/FINAL_DELIVERABLE_PACKAGE/02_FIGURE_BUILD_SCRIPTS/build_figure_4_4_model_evaluation_labelled.py` |
| Canonical record | `Thesis_Codex/04_MODEL_REPRODUCTION_AND_BENCHMARKS/TABLE_4_2_SPATIAL_VALIDATION_VERIFICATION.csv` (all seven spatial ROC-AUCs cross-checked against this file and against Table 4.3) |
| Built by | `scripts/build_poster_figures.py` → `Images/poster/P2_leakage_safe_validation.pdf` |
| Values shown | Panel a: 0.9396 / 0.8688 / 0.7696, optimism 0.1701. Panel b: 0.9062, 0.8596, 0.8160, 0.7463, 0.7440, 0.6800, 0.6348. |
| Transformations | Selection and ordering only. Panel b is sorted descending — the submitted figure uses the same order. The 0.70 reference line is the lower bound of the "acceptable" band defined in Table 4.4 (Hosmer, Lemeshow and Sturdivant, 2013) and is labelled on the poster as a general heuristic, not an environmental threshold. Panel c of the submitted Figure 4.4 (the Model A/B channel comparison) is **not redrawn**; that result appears in the poster text with its random-row boundary attached. |
| Status | Verified. |

### P3 — External transfer to India

| Field | Value |
|---|---|
| Where | Column 3 |
| Submitted source | Figure 4.5 (p77); Table 4.6 (p75) |
| Active thesis source | `chapters/Chapter4.tex`, asset `figures/figure_4-5.pdf` |
| Final build script (thesis) | `CLAUDE/FINAL_DELIVERABLE_PACKAGE/02_FIGURE_BUILD_SCRIPTS/build_figures_4_5_and_4_12_corrected.py` |
| Canonical record | `Thesis_Codex/04_MODEL_REPRODUCTION_AND_BENCHMARKS/TABLE_4_4_TRANSFER_CROSSCHECK.csv` — **CGWB rows only**. That file also holds WQP rows for the same parameters; those are a different archive and are not shown, because the poster's claim is about the India external evaluation. |
| Built by | `scripts/build_poster_figures.py` → `Images/poster/P3_india_external_transfer.pdf` |
| Values shown | All six evaluated India parameters, three metrics each: ROC-AUC, severity rank correlation, calibration slope, exactly as Table 4.6. |
| Transformations | Selection and ordering only. The three-colour verdict encoding reproduces the submitted figure's own categories: *rank transfer supported* / *transfer not supported* / *evidence insufficient*. |
| Boundary preserved | The figure note states that a supported rank is not a calibrated probability and that every India row carries negative Brier skill. No parameter is shown as having transferable probabilities. |
| Status | Verified. |

### P4 — What the next action actually is

| Field | Value |
|---|---|
| Where | Column 4 |
| Submitted source | Figure 4.14 panel a (p106); counts restated at p118 and in the Conclusions, p127 |
| Active thesis source | `chapters/Chapter4.tex`, asset `figures/figure_4-14.png` |
| Built by | `scripts/build_poster_figures.py` → `Images/poster/P4_next_action_26_contexts.pdf` |
| Values shown | 12, 6, 4, 1, 1, 1, 1 across seven action categories, summing to 26. The build script asserts this sum. |
| Transformations | Re-typeset from raster to vector at poster scale. Categories and counts are unchanged. Panel b of Figure 4.14 (what blocks a named product, 23 products) is **not** reproduced as a chart; its headline — that no product clears the gate — is carried by the "0 of 23" call-out and its note. |
| Status | Verified. The counts were read from `figures/figure_4-14.png` and cross-checked against the prose counts at p118 and p127. |

### Source explicitly rejected

`Thesis_Codex/10_HISTORICAL_FIGURE_REBUILDS/APPLIED_SYNTHESIS/FIGURE_APPLIED_ACTION_FAMILIES.csv`
gives a **different** breakdown of the same 26 contexts (rank-then-confirm 4, measure directly 12,
build valid baseline 7, repair units/metadata 3). That is a superseded categorisation from an
earlier figure rebuild. **P4 uses the submitted Figure 4.14 counts, not that file.**

### P5 — Binding constraint by parameter (built, not placed)

`Images/poster/P5_binding_constraint.pdf` reproduces the 8-parameter × 9-dimension verdict grid of
Figure 4.13 (p104). The 72 cell verdicts were extracted **from the vector content of the submitted
asset** `THESIS_LATEX_BUILD/figures/figure_4-13.pdf` — the three fill colours were read directly
from the PDF drawing operators and mapped to the three legend categories, so no cell was inferred
from a rendered image. No cell is scored, summed or reordered.

It is **not placed on the poster**: at A1 the four columns could not carry a fifth major visual
without pushing body text below the template's 26 pt level, which the QA checklist forbids. The
asset is retained so the figure can be swapped in if the layout is later rebalanced. Its finding
is carried in text by the low-resource-needs paragraph in column 4.

---

## Headline number ledger

All values verified present on the stated page of the submitted PDF by
`scripts/verify_poster_numbers.py`.

| Value | Submitted page | What it is |
|---|---:|---|
| 0.9396 / 0.8688 / 0.7696 | 68 | Mean ROC-AUC across seven tasks: random row, grouped station, spatial block |
| 0.1701 = 0.0708 + 0.0993 | 68 | Total optimism, decomposed into repeat-visit and geographic components |
| 145 | 68 | State-by-parameter cells with recorded cadence, none revisited more often than annually at its median |
| 0.9062 … 0.6348 | 71 | The seven spatial-block ROC-AUCs (Table 4.3) |
| 0.501, 0.482, 0.520 | 76 | Label-shuffle control and its 95% interval |
| 0.7426 / 0.7081 / 0.6248 / 0.6107 / 0.4870 / 0.3170 | 75 | India external ROC-AUC, six parameters (Table 4.6) |
| 0.4565 / 0.4369 / 0.2430 / 0.2025 / −0.0362 / −0.3258 | 75 | Severity rank correlation, six parameters |
| 0.3714 / 0.2892 / 0.4017 / 0.2383 / −0.0710 / −0.9128 | 75 | Calibration slope, six parameters |
| 119 observations, 116 sites | 75 | Arsenic external evaluation population |
| 5,966 → 2,838 vs 1,410; 2.01× | 79 | Conductivity confirmatory yield at the recorded operating point (Table 4.8) |
| 265 → 154 vs 64.2; 2.40× | 79 | TDS confirmatory yield at the recorded operating point |
| 1,242 and 223 | 97 | Product–criterion evidence cells, and cells with an exact-product document |
| 9 independent cells; no product reaches 11 of 11 | 97 | Independent exact-product evidence; the eleven-criterion gate |
| 12,349 records, 1,641 sites, 54.06%, 1,500 µS/cm | 103 | Rajasthan worked case (Table 4.17) |
| 12 of 26 | 118 | Baseline acquisition, the most frequent next action |
| 26 contexts | 118 | Evaluated monitoring contexts, India / Kenya / Malawi |

Values stated on the poster in words rather than digits, and their sources:

| Statement | Submitted page |
|---|---:|
| Five of seven tasks acceptable-or-better; three of seven excellent-to-outstanding | 72 (Table 4.4) |
| Every spatial PR-AUC exceeds its prevalence baseline, 7 of 7 | 72 |
| Model B higher on all six shared tasks | 73 (Table 4.5) |
| Six India parameters with an accepted population; turbidity and *E. coli* with none | 61 (Table 4.1) |
| 33-entry landscape = 23 products + 8 reference methods + 2 emerging classes | 97 (Table 4.14) |
| Cost and energy per valid result unavailable for all 23 products | 2 (abstract), 118 |
| Sixteen research priorities, only two concerning sensor design | 102, 128 |
| Kenya and Malawi as bounded comparators; no model transferred to Bangladesh or Ghana | Conclusions, 127–128 |

---

## Claim boundaries carried onto the poster

Each of these is present in the poster text, not merely implied:

- random-row performance is labelled a **channel comparison, not geographic generalisation**;
- rank transfer is stated **not** to be a calibrated probability, with negative Brier skill named;
- pH's route to direct measurement is scoped to **this evaluation**;
- arsenic is **evidence-insufficient**, with its population stated, not refuted;
- the 2.01× and 2.40× yields are tied to the **recorded operating point** and explicitly not
  claimed for the other four parameters;
- missing product documentation is **unknown evidence, not poor performance**;
- the 26 contexts are **parameter-context decisions**, not countries or sites;
- the Rajasthan exceedance share is a **record-level signal, not population exposure**;
- Kenya and Malawi **support no national estimate**; no model was transferred to Bangladesh or
  Ghana;
- the 33-entry landscape is never called 33 products.

## Not used

Not present on the poster in any form: eProfiler; conformal prediction; proposed CNN-LSTM or PINN
work; any Chapter 5 or A–J appendix structure; any named-product ranking or recommendation; the
full 23 × 54 documentary grid (Figure 4.10); any historical Antigravity, SHAP or archetype-map
asset; the superseded 195-cell documentary state.
