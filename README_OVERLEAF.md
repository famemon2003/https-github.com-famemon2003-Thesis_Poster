# Opening this poster in Overleaf

Three settings must be right or the poster will not build. Overleaf does not read the
`%!TEX program` line in the source, so the compiler has to be set by hand.

## 1. Upload

**New Project → Upload Project**, and select `Thesis_Poster_Overleaf.zip`.

The files must sit at the top level of the project, not inside a folder. The zip is already
built that way — do not re-wrap it in a directory, or `Fonts/` and `Images/` will stop resolving.

## 2. Set the compiler to XeLaTeX

**Menu → Settings → Compiler → XeLaTeX.**

The poster uses the Imperial Sans OpenType fonts through `fontspec`. pdfLaTeX cannot load them
and will fail immediately.

## 3. Set the main document to `poster_final.tex`

**Menu → Settings → Main document → `poster_final.tex`.**

This matters: the project also contains `template_poster_landscape.tex` and
`template_poster_portrait.tex`, which are the untouched Imperial sample templates. If Overleaf
picks one of those as the main document you will compile a two-page sample poster full of
placeholder text rather than this poster.

Then press **Recompile**. The result is a single A1 landscape page, 841 × 594 mm.

---

## What is in the project

| Path | What it is |
|---|---|
| `poster_final.tex` | **The poster.** The only file you need to edit. |
| `poster_final.pdf` | The compiled poster, as built and checked locally. |
| `Images/poster/` | The four poster figures, vector PDF. |
| `scripts/build_poster_figures.py` | Rebuilds those figures. Runs locally with Python and matplotlib, not on Overleaf. |
| `scripts/verify_poster_numbers.py` | Checks every number on the poster against the submitted thesis. Runs locally. |
| `poster_source_traceability.md` | Where each figure and number comes from, page by page. |
| `poster_QA.md` | The QA checklist with results and the recorded decisions. |
| `ImperialPoster.cls` | Official Imperial poster class, **unmodified**. |
| `template_poster_landscape.tex`, `template_poster_portrait.tex` | Official samples, **unmodified**. Kept for reference; not part of the poster. |
| `Fonts/`, `Images/` | Official Imperial Sans fonts and logo assets. |

## If you edit the poster

The layout fits one A1 page with very little slack. Adding a couple of lines to any column will
push the poster to two pages. If that happens, the fix is to cut content — not to reduce the font
size. The body text is at the official 26 pt level and the notes are at the official 16 pt level;
dropping below either breaks template compliance.

After any edit, check the page count is still 1 before printing.

## Changing the colour mode

The poster is set up for print, in CMYK:

```latex
\documentclass[landscape, a1papersize, print]{ImperialPoster}
```

For an on-screen or web version in RGB, comment out `print,` in that list. Everything else stays
the same.
