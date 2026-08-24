# Final A1 poster QA

Gate: `10_FINAL_POSTER_QA_CHECKLIST.md` from the poster handover package, worked item by item
with the evidence for each pass. Artefact under test: `poster_final.pdf`, built from
`poster_final.tex` with XeLaTeX.

**Verdict: GO.**

---

## Content and science

| Check | Result | Evidence |
|---|---|---|
| Exact submitted title | PASS | Title matches the submitted PDF metadata and title page character for character; not shortened. |
| Author: Muhammad Faseeh Memon | PASS | Title block, with CID 06058747 as on p1 of the submitted PDF. |
| Supervisor: Professor Michael Templeton | PASS | Title block. |
| India identified as principal empirical application | PASS | Column 1, "Scope": "India is the principal empirical application." |
| Kenya/Malawi only as bounded local comparators | PASS | Column 1: "bounded local comparators and support no national estimate." |
| Bangladesh/Ghana literature-grounded, no model transfer | PASS | Column 1: "appear only as literature-grounded applications of the decision logic, with no model transferred to either." |
| Random-row never described as geographic generalisation | PASS | Column 2: "a random-row channel comparison, not geographic generalisation." |
| 0.9396 / 0.8688 / 0.7696 / 0.1701 used correctly | PASS | P2 panel a and the column-2 note; optimism decomposition 0.0708 + 0.0993 stated. |
| 4/6 rank transfer not converted into calibrated probabilities | PASS | P3 note: "A supported rank is not a calibrated probability: every India row carries negative Brier skill." Column 3: "Any probability use — recalibrate on local labels first." |
| pH direct-measurement scoped to this evaluation | PASS | Column 3: "pH — not supported **in this evaluation**: measure directly." |
| Arsenic described as evidence-insufficient, not failed | PASS | Column 3 and P3 legend category "Evidence insufficient"; population 119 observations at 116 sites stated. |
| 2.01× / 2.40× labelled "recorded operating point" | PASS | Column 3 note, with the explicit statement that the operating point "is not usable for the other four parameters". |
| 33 entries / 23 products / 10 archetypes never conflated | PASS | Column 4: "The 33-entry landscape is separate: 23 products, 8 reference methods, 2 emerging classes." The phrase "33 products" appears nowhere (grep). The 10-archetype MCDA layer is not shown, so it cannot be conflated. |
| 1,242 / 223 / 9 / 0-of-23 match the final report | PASS | Verified against p97 by `scripts/verify_poster_numbers.py`. |
| Missing product evidence not described as poor performance | PASS | Column 4: "This is abstention, not poor performance — missing documentation remains unknown evidence." |
| 26 contexts not described as countries or sites | PASS | P4 note: "Direct counts across 26 parameter-context decisions … Not a score, and not 26 countries or sites." |
| Baseline acquisition 12/26 used as an action count | PASS | P4 is a count chart with the axis "Monitoring contexts, of 26"; no risk language attached. |
| Low-resource implications include operating evidence | PASS | Column 4 names cost and energy per valid result, threshold-near accuracy, operator effect, invalid tests, reliability, reagent stability and persistent identifiers. No "cheap sensor" shorthand. |
| No eProfiler / conformal / PINN / CNN-LSTM result | PASS | Automated scan of the rendered poster text: zero hits. |

A scripted scan of the rendered PDF text for prohibited constructions returned four hits, all
verified as correct usages: *"not population exposure"*, *"support no national estimate"*, *"no
model transferred to either"*, *"Ranking transferred where calibration did not"*. No occurrence of
"33 products", "accurate", "robust", "proven", "breakthrough", or any named-product
recommendation.

## Traceability

| Check | Result | Evidence |
|---|---|---|
| Every headline claim has a page/table/figure source | PASS | `poster_source_traceability.md`; 53-entry ledger. |
| Every plot has a final source record | PASS | P1 ← Fig 3.1/3.6; P2 ← Fig 4.4 / Table 4.3; P3 ← Fig 4.5 / Table 4.6; P4 ← Fig 4.14. |
| No historical-only asset appears | PASS | All four visuals are built from submitted-PDF values by `scripts/build_poster_figures.py`. The superseded `FIGURE_APPLIED_ACTION_FAMILIES.csv` action breakdown was found and **rejected**; see traceability. |
| Poster redraws reproduce final values exactly | PASS | `scripts/verify_poster_numbers.py`: 53 of 53 ledger values found on their stated submitted pages. |
| Axis units and thresholds agree with the report | PASS | ROC-AUC axes 0.5–1.0 and 0.0–1.0; the 0.70 line is Table 4.4's acceptable-band boundary and is labelled a general heuristic. |
| Any selected subset identified as a subset | PASS | P2 omits Figure 4.4 panel c (stated in traceability, and the channel result appears in text with its boundary). P3 shows CGWB rows only, stated in traceability. P4 omits Figure 4.14 panel b, stated. |
| No untraceable number on the poster | PASS | Coverage check: 0 untraced numeric tokens. |

## Official template compliance

| Check | Result | Evidence |
|---|---|---|
| A1 exact page size | PASS | `pdfinfo`: 2383.94 × 1683.78 pt = **841.0 × 594.0 mm**. Official landscape POTX `<p:sldSz cx="30275213" cy="21383625"/>` = 84.0978 × 59.3990 cm. Difference 0.02 mm × 0.01 mm. |
| `landscape, a1papersize` enabled | PASS | `poster_final.tex` line 18–20. Class default A0 is overridden. |
| Official Imperial logo retained | PASS | Class header, `ICL_Logo_Blue_CMYK.pdf` (selected by the `print` option). |
| White background, official Imperial blue / dark blue | PASS | `ICLBlue` RGB(0,0,205) and `ICLDarkBlue` RGB(0,0,128) from the unmodified class; poster figures use the same values. |
| Official title / author / footer geometry retained | PASS | `\titlesection` used as supplied; footer rule with "Imperial College London" and "imperial.ac.uk" unchanged. |
| No placeholder grey boxes or sample text | PASS | No `Grey_*.pdf` is referenced; all sample copy removed. |
| No unnecessary coauthor or funder logos | PASS | `\coauthorlogos` not called; no UKRI or placeholder logo. |
| Body text at the official 26 pt level | PASS | Class A1 body 26/32.5 pt, unchanged. Nothing was shrunk to fit. |
| Small text and captions ≥ 16 pt | PASS with one documented exception | All figure credits and notes use `\smalltext` (16/20 pt). The class's 10 pt caption format is overridden to 16 pt. **Exception:** secondary annotation inside the P1 schematic (14.5–15.5 pt) and axis tick labels inside P3 (14 pt) sit slightly below 16 pt. The visual-asset plan permits this for "a compact secondary annotation"; all data values and category labels are ≥ 15 pt. |
| Print colour mode | PASS | `print` class option enabled: CMYK colour conversion and the CMYK logo. The screen/RGB build was also compiled as a check — comment the single `print` option to produce it; it yields the same one-page A1 geometry. |
| Class and sample templates unmodified | PASS | `ImperialPoster.cls`, `template_poster_landscape.tex` and `template_poster_portrait.tex` are byte-identical to the supplied originals (verified by SHA-256 against `POSTER_LATEX.zip`, modulo line endings). `git status` shows no modification to any of them. |

### Deviations, declared

All three are local to `poster_final.tex`; the class is untouched.

1. **`\parskip` reduced from 32.5 pt to 24 pt inside the column block.** Inter-paragraph space
   only. No font size changed. Made to fit content on one page without dropping below the 26 pt
   body level, which the checklist forbids.
2. **Italic shape declared.** The supplied Imperial Sans Text family has no italic file, so the
   class leaves `TU/ImperialSansText/m/it` undefined and LaTeX substituted a non-brand face. A
   `\setmainfont` redeclaration with `FakeSlant=0.18` keeps italics (species names, publication
   titles) in the brand typeface. The build now emits no font warning and embeds only Imperial
   Sans faces.
3. **`\raggedright` inside the poster title.** Without it the class's title parbox justifies the
   long submitted title and hyphenates it ("Monitor-ing"). Ragged setting only; no size change.

## Visual hierarchy

| Check | Result | Note |
|---|---|---|
| Title readable first | PASS | 42 pt bold Imperial blue, three lines, no hyphenation. |
| One-line takeaway visible within seconds | PASS | Two 42 pt `\boldsection` lines: "A recommendation is only as defensible as the evidence layer beneath it" (column 1) and "Ranking can stay useful after calibration stops" (column 4). |
| Results occupy more space than methodology | PASS | Methodology is one full-width band ≈ 12% of the content area. Columns 2–4 are results. |
| No more than 4–5 major figures | PASS | Four: P1 band, P2, P3, P4. |
| Each major figure has one clear message | PASS | Each carries a takeaway title rather than a dissertation caption. |
| Columns have similar visual weight | PASS | Four columns, each filled to within roughly one line of the same depth. |
| White space deliberate | PASS | Consistent column gutters; one deliberate gap at the foot of column 1. |
| No dissertation-length paragraphs | PASS | Longest 26 pt block is four lines; detail is set as 16 pt blocks. |
| Important numbers large but in context | PASS | "0 of 23" (64 pt) and "2.01× 2.40×" (50 pt) each sit directly above the sentence that bounds them. |
| Conclusion visible without searching | PASS | Column 4, 42 pt. |

## Figure quality

| Check | Result | Note |
|---|---|---|
| Vector output | PASS | P1 is TikZ; P2–P4 are vector PDF from matplotlib. No raster chart anywhere. |
| Raster resolution adequate | N/A | The poster contains no raster image. |
| Labels legible at viewing distance | PASS | Inspected at whole-page, reading and figure-zoom scales. Data labels 15–19 pt at final size. |
| No tiny legend | PASS | P3 legend 14.5 pt, set horizontally above the panels. |
| No overlapping annotations | PASS | Three collisions found during QA and fixed: P3's legend over the axis labels (moved above the panels), P2's value labels across the 0.70 reference line (moved inside the bars), P4's axis label against its note (note moved into the poster source). Re-inspected at zoom after each fix. |
| No truncated titles or axes | PASS | Verified at figure zoom. |
| Colours distinguishable, adequate contrast | PASS | Imperial dark blue, mid blue, rust and ochre; white value labels only on the dark fills. |
| Warm/error colours used consistently | PASS | Rust means "not supported / below the heuristic band" in both P2 and P3; ochre means "evidence insufficient" only. |
| Figures do not encode missing evidence as poor performance | PASS | The one figure that could — the Fig 4.13 verdict grid — is not on the poster, and P4 charts actions, not scores. |

## Technical

| Check | Result | Evidence |
|---|---|---|
| XeLaTeX clean build | PASS | `latexmk -xelatex`; no errors. |
| Exactly one page | PASS | `pdfinfo` Pages: 1. |
| No missing file or font errors | PASS | Log scanned; the only remaining line is the benign `pdftexcmds Info: \pdfdraftmode not found`. |
| No overfull boxes affecting output | PASS | `grep -c Overfull` = **0**. |
| No clipped text or figures | PASS | Confirmed by zoom inspection of all four columns and the band. |
| PDF opens normally | PASS | Opened and rendered page-by-page with PyMuPDF. |
| Page dimensions verified programmatically | PASS | See template compliance above. |
| Fonts embedded | PASS | Only `ImperialSansText-Regular/-Bold/-Medium/-Extrabold`, all embedded subsets. The Computer Modern and Latin Modern faces present in an earlier build were removed by replacing `$\times$`, `$\bullet$` and `\texttt` with brand glyphs. |
| No hidden second page | PASS | Page count is 1. |
| External URLs / QR codes tested | N/A | None used. |

## Final comparative review

- **Against the official landscape POTX:** geometry, colour values, title/author split, body and
  small-text sizes and footer all match; measured differences are ≤ 0.02 mm. The POTX was read
  directly from `ppt/presentation.xml`.
- **Against the four department example posters:** the examples run to roughly eight figures with
  dense justified body copy and captions well below the official small-text level. This poster is
  materially less dense — four visuals, 26 pt body, ≥ 16 pt notes — and sits comfortably inside
  the density ceiling those examples set. Their older dark-navy header style was deliberately not
  copied; the current official white and blue template is used.
- **Cold read against the submitted PDF:** performed. No claim on the poster is stronger than the
  corresponding claim in the thesis, and no boundary present in the thesis was dropped.
- **Numerical diff against the claims ledger:** `scripts/verify_poster_numbers.py` → PASS.

## Recorded decisions

1. **Exact submitted title**, unshortened, per the checklist and the user's instruction.
2. **P1 laid out horizontally as a full-width band** rather than as a column figure. A vertical
   five-stage chain in one column consumed roughly 24 cm of a 32 cm column and forced the poster
   onto three pages. Content is unchanged; stage names and terminal outputs remain verbatim.
3. **P5 (Figure 4.13 binding-constraint grid) built but not placed.** At A1 the four columns could
   not carry a fifth major visual without pushing body copy below 26 pt. The asset and its build
   code are retained; its finding is carried in text. This is the release valve the poster
   visual-asset plan anticipates.
4. **Figure 4.4 panel c and Figure 4.14 panel b are not redrawn**; both findings appear in the
   poster text with their boundaries attached, and the omissions are recorded in traceability.
5. **Print (CMYK) build is the deliverable.** The screen/RGB build was compiled as a check and is
   produced by commenting one class option.

## Reproducing this build

```
python scripts/build_poster_figures.py
latexmk -xelatex poster_final.tex
python scripts/verify_poster_numbers.py "<path>/ResearchPaper-06058747-Muhammad Faseeh Memon-Templeton.pdf"
```
