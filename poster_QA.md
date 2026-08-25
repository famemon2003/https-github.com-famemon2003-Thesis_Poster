# Final A1 poster QA — v2 asymmetric build

Gate: `05_REFERENCE_AND_QA/FINAL_POSTER_QA_CHECKLIST.md`. Artefact: `poster_final.pdf`,
built from `poster_final.tex` with XeLaTeX.

**Verdict: GO, with two disclosed compromises** — both forced by the specification's content
exceeding its own geometry, both recorded below, neither affecting a number or a claim.

---

## Scientific

| Check | Result |
|---|---|
| Ground truth is the submitted thesis PDF | PASS — SHA-256 confirmed identical to the 293-page submission |
| No stale result introduced | PASS — automated ledger, 61/61 values on their stated pages |
| 145/145 cadence wording uses **≥ 1 year** | PASS — inside P2, matching thesis wording on p68 |
| 0.9396 / 0.8688 / 0.7696 correct | PASS |
| 0.1701 apparent optimism correct | PASS |
| 5/7 framed under the stated heuristic | PASS — "under the thesis heuristic" |
| 4/6 India rank transfer correct | PASS |
| 2.01× / 2.40× labelled enrichment at the recorded operating point | PASS — inside P2, which carries that wording |
| pH and arsenic outcomes kept distinct | PASS — pH → direct measurement; arsenic → evidence acquisition |
| 17/160 correct at the stated 10% action level | PASS — inside P1 |
| Map record fractions not described as prevalence | PASS — "not contamination severity or population prevalence" |
| 1,242 / 223 / 9 / 0-of-23 exact | PASS |
| Missing evidence ≠ poor performance | PASS — P2 states "missing evidence ≠ poor performance" |
| 26/26, 12/26, 6/26 exact | PASS |
| 2/16 sensor-design result correctly framed | PASS |
| Rajasthan 54.06% / 51.96% are record-level findings | PASS |
| No claim that prediction certifies safe water | PASS — methodology figure states the opposite explicitly |
| No unsupported named-product recommendation | PASS |

A scripted scan for prohibited constructions returned only correct usages: the *negation* of
population prevalence, the "certifies nothing" boundary, and "recalibration precedes
probability-based use". No occurrence of "33 products", "accurate", "robust", "proven",
"breakthrough", eProfiler, conformal, CNN-LSTM, PINN or Chapter 5.

## Template

| Check | Result |
|---|---|
| A1 landscape exactly | PASS — 2383.94 × 1683.78 pt = 841.0 × 594.0 mm; official POTX `<p:sldSz>` = 84.0978 × 59.3990 cm |
| `a1papersize` enabled | PASS — `[landscape, a1papersize, print]` |
| XeLaTeX | PASS |
| Official Imperial logo | PASS — CMYK logo via the `print` option |
| Imperial Sans | PASS for all poster text (see font note below) |
| Body 22–26 pt | PASS — body 22/25 pt, never reduced below 22 |
| Major captions ≥ 16 pt | PASS — captions 16 pt, source tags 13.5 pt |
| No sample/coauthor/funder placeholders | PASS — `\coauthorlogos` not called, no `Grey_*.pdf` |
| Footer correct | PASS |
| White background | PASS |
| Class and templates unmodified | PASS — `ImperialPoster.cls` and both `template_poster_*.tex` byte-identical |

**Font note.** The embedded PDF fonts are the four Imperial Sans faces plus Arial and DejaVu Sans.
The latter two come from *inside* the supplied thesis figure PDFs (Figs 3.1, 4.4, 4.5, 4.13),
which the spec requires be used as vector originals. No poster text uses them.

**Declared local overrides** (poster file only; the class is untouched): a `\setmainfont` italic
redeclaration with `FakeSlant`, because the Imperial family ships no italic file and LaTeX was
otherwise substituting a non-brand face; a 16 pt caption format override; and `\parskip` set to
0 with all spacing controlled explicitly, since the class's 32.5 pt default would break the
fixed-height panel geometry.

## Layout

| Check | Result |
|---|---|
| Left rail and results field clearly separated | PASS — 18.5 cm rail, 1.0 cm gutter, 59.4 cm field |
| Reading order obvious | PASS — intro → gap → method → P2 → results → application → conclusion |
| P2 visually dominant near top | **PARTIAL** — P2 spans the top of the results field but at 34.5 cm, not the specified 55–59 cm. See compromise 1 |
| P1 large enough to read all state labels | PASS at close reading — 19.8 cm, ~186 dpi, labels ≈ 8 pt |
| Validation chart labels readable | PASS — Fig 4.4 at 23.0 cm, all seven task names present |
| India transfer labels readable | PASS — all three panels, six parameters, all values |
| Binding-constraint matrix readable | PASS — 15.0 cm, 8 rows × 9 dimensions plus legend |
| Application block not overcrowded | PASS |
| References unobtrusive but readable | PASS — 14 pt, two columns |
| No accidental empty holes | PASS |
| No panel touching another | PASS — 8–10 mm gutters |
| No text within ~5 mm of a card edge | PASS |

## Figures

| Check | Result |
|---|---|
| P1/P2 aspect ratio preserved | PASS — width-only scaling |
| P1/P2 not recreated | PASS — used as single images, unaltered |
| Vector PDFs remain vector | PASS |
| Fig 4.4 crop shows panel (a) only | PASS — verified by render; no part of panel (b) |
| Fig 4.5 preserves all three dimensions | PASS |
| Fig 4.13 paragraph cropped, matrix and legend preserved | PASS |
| No low-resolution resampling | PASS — P2 151 dpi, P1 186 dpi at final size |
| No stretched figures | PASS |

## Technical

| Check | Result |
|---|---|
| Exactly one page | PASS |
| A1 dimensions | PASS |
| No font substitution affecting output | PASS — no font warnings in the log |
| No missing images | PASS |
| No overfull boxes | PASS — `grep -c Overfull` = **0** |
| No clipping | PASS — confirmed by render at whole-page and panel zoom |
| Body text readable at 100% | PASS |
| Title and top result read immediately at whole-page view | PASS |
| Final PDF opens normally | PASS |

## Ten-second test

Whole-page render confirms a reader can identify: the monitoring problem (rail heading and two
callouts), the evidence-aware framework (P2 spine), that honest validation reduces apparent
performance (Fig 4.4 plus the 5/7 line), that rank transfer remains useful in India (Fig 4.5
heading), the measurement-priority map (P1), and that the framework returns practical next
actions (the application block heading and "Only 2 / 16").

---

## Disclosed compromises

The specification's content exceeds its own geometry. Measured against the 43.2 cm of body height
available below the title block, the left rail's specified content required **~50 cm** and the
results field **~48 cm**. On the user's instruction the shortfall was absorbed by **trimming
prose and reducing figure sizes, never by dropping body type below 22 pt** and never by removing
a number, a boundary or a conclusion.

**1. P2 is 34.5 cm wide, not the specified 55–59 cm.** At 34.5 cm its headline numbers
(145/145, 0.9396, 4/6, 26/26, 0/23) remain large and legible and it still spans and orients the
top of the results field, but its smallest internal annotations render at roughly 5 pt and are
decorative at print size rather than readable. Every claim inside P2 is also carried in the
poster's own text or in Figs 4.4/4.5/4.13, so nothing is lost, and the automated ledger verifies
those values against the thesis regardless. **This is the item worth fixing:** a re-export of P2
with fewer, larger internal labels — or the same content at a wider aspect ratio — would let it
sit at full width. Swapping it is a one-line change plus a recompile.

**2. Figure sizes below the specified widths.** P1 19.8 cm (spec 26.5–27.5), Fig 4.4 23.0 cm
(spec ~31.6), Fig 4.13 15.0 cm (spec 16.5), Fig 3.1 12.8 cm. All remain legible at close reading;
the ordering follows the spec's own visual-priority ranking, which places the binding-constraint
matrix and methodology last.

**Prose trimmed** in the Introduction, the literature gap cards, the resource-constrained
requirements list and the three conclusions — the spec's own cut order (items 1–4). The three
gap cards are set as one flowing paragraph with inline bold labels rather than three separate
cards, and the author metadata is compacted to three lines. Fig 4.13 carries no separate LaTeX
heading because its crop already includes its own title, applying the spec's "no duplicate title"
rule for P1.

## Reproducing

```
latexmk -xelatex poster_final.tex
python scripts/verify_poster_numbers.py
```
