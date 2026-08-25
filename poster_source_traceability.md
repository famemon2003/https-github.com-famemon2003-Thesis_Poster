# Poster source traceability — v2 asymmetric build

**Scientific authority.** `GROUND_TRUTH_FINAL_SUBMITTED_THESIS.pdf` — 293 pages, SHA-256
`f371a8fe86ab6380bc5ee0426f9de708593277cb36d9bc6746b5cb14529df7aa`. Byte-identical to
`ResearchPaper-06058747-Muhammad Faseeh Memon-Templeton.pdf`.

Built to `FINAL_POSTER_BUILD_PACKAGE_25_AUG_2026`. Page references are **physical PDF pages**.

## Automated verification

`scripts/verify_poster_numbers.py` checks two things and exits non-zero on any failure:

1. **Ledger** — each of 61 values is looked up in the submitted PDF *on the page it is
   attributed to*. Values marked `raster-only` sit inside the P1/P2 images (pictures, not text),
   so they are verified against the thesis but not expected in the poster's text layer.
2. **Coverage** — every numeric token in the rendered poster text must be in the ledger or the
   declared structural whitelist.

Last run: **PASS**, 61/61 verified, 0 untraced.

```
python scripts/verify_poster_numbers.py
```

## Assets and crops

| Poster element | Source | Size used | Crop |
|---|---|---|---|
| P2 graphical abstract | `P2_RESULT_LED_GRAPHICAL_ABSTRACT_FINAL.png` | 34.5 cm wide (151 dpi) | none |
| P1 decision-uncertainty map | `P1_DECISION_UNCERTAINTY_MAP_FINAL.png` | 19.8 cm wide (186 dpi) | none |
| Methodology | `METHODOLOGY_FIGURE_3_1...pdf` (Fig 3.1, p43) | 12.8 cm wide | `trim=5pt 100pt 5pt 5pt` |
| Leakage-safe validation | `RESULT_FIGURE_4_4...pdf` (Fig 4.4a, p70) | 23.0 cm wide | `trim=0pt 405pt 18pt 6pt` |
| India transfer | `RESULT_FIGURE_4_5...pdf` (Fig 4.5, p77) | 18.0 cm wide | `trim=0pt 42pt 12pt 5pt` |
| Binding constraints | `RESULT_FIGURE_4_13...pdf` (Fig 4.13, p104) | 15.0 cm wide | `trim=20pt 45pt 15pt 8pt` |

Fig 4.12 was supplied as an optional backup and is **not used**: P2 and the application block
already carry the 26-context result, and the spec forbids adding it if it duplicates content.

### Three crop values in the spec were wrong and were corrected

Each was found by rendering the crop and reading it, as `04_ASSET_PLACEMENT_AND_CROPPING.md`
instructs ("do not trust the numeric trim blindly").

| Figure | Spec value | Problem | Corrected |
|---|---|---|---|
| Fig 4.4 | `trim=24pt 405pt 18pt 6pt` | 24 pt left trim clipped the y-axis task labels — "Conductivity" rendered as "onductivity", "Suspended solids" as "nded solids". The spec's own QA requires all seven task names to remain. | left trim `0pt` |
| Fig 4.5 | `trim=18pt 42pt 12pt 5pt` | 18 pt left trim clipped "Conductivity" the same way. | left trim `0pt` |
| Fig 3.1 | `trim=5pt 72pt 5pt 5pt` | 72 pt bottom trim left a visible sliver of the "Framework rules" box below the figure. | bottom trim `100pt` |

Fig 4.13's specified crop was verified correct as given: title, subtitle, all 8 parameter rows,
all 9 evidence dimensions and the legend survive; only the explanatory paragraph is removed.

## Claim → source

| Poster claim | Submitted source |
|---|---|
| 363 million people in India lacking safely managed drinking water | p16, Section 1.1 |
| 35 of 38 surveys; mean change −12.9 percentage points | p20, Section 1.2 (Santos et al., 2023) |
| Five-stage evidence-to-decision sequence; abstention a designed output | Fig 3.1, p43 |
| 0.9396 / 0.8688 / 0.7696; optimism 0.1701 (inside P2) | Section 4.3, p68 |
| 145 cadence cells, **median revisit ≥ 1 year** (inside P2) | p68 — thesis wording: "not one has a median revisit interval shorter than a year" |
| All 21 ROC-AUC values in Fig 4.4 panel (a) | Table 4.3, p71 |
| 5/7 acceptable-or-better under the stated heuristic | Table 4.4, p72 |
| Label shuffle → ROC-AUC 0.501 | Table 4.7 / Section 4.3, p76 |
| All 18 transfer values in Fig 4.5 | Table 4.6, p75 |
| 4 of 6 rank transfer supported | Table 4.6, p75 |
| 17/160 cells decision-relevant at the stated 10% action level (inside P1) | p85, Fig 4.7 / Table 4.11 |
| 2.01× / 2.40× enrichment (inside P2) | Table 4.8, p79 |
| 1,242 / 223 / 9 / 0 of 23 (inside P2) | Section 4.7, p97 |
| 26/26, 12/26, 6/26 (inside P2; 26 also in poster text) | p118, Conclusions p127 |
| Rajasthan: 12,349 records, 54.06%; TDS 3,131 records, 51.96% | Table 4.17, p103 |
| Only 2 of 16 research priorities concern sensor design | p102 ("at two of its sixteen"), p128 |

## References

All seven entries exist in the submitted bibliography (pp289–292), verified by string match.
Author lists are abbreviated with *et al.*, and DOIs omitted, as
`07_REFERENCES_SELECTED.md` permits. **One correction to the spec:** reference 4's first author is
`Camargo, E.` in the thesis, not `De Camargo, E.`

## Claim boundaries carried onto the poster

Record fraction is stated as **not** population prevalence; the methodology figure carries "no
output certifies that water is safe to drink"; rank transfer is separated from calibrated
probability ("local recalibration precedes probability-based use"); arsenic is
evidence-insufficient rather than refuted; pH routes to direct measurement; missing product
evidence is not described as poor performance; 26 are contexts, not countries or sites; no
named-product recommendation appears. eProfiler, conformal prediction, CNN-LSTM/PINN, a Chapter 5
structure and the full 23×54 matrix appear nowhere.
