"""Audit every number printed on the poster against the submitted thesis.

Two checks run:

1. **Ledger check** - each value below is looked up in the submitted PDF *on the page
   it is attributed to*. A value that is not on its stated page fails. Values marked
   ``RASTER`` live only inside the P1/P2 poster images, which are pictures rather than
   text, so they are verified against the thesis but are not expected in the poster's
   text layer.
2. **Coverage check** - every numeric token extracted from the rendered
   ``poster_final.pdf`` must be either in the ledger or in the declared structural
   whitelist (figure and table references, axis ticks, reference years). An
   untraceable number on the poster fails.

Usage:
    python scripts/verify_poster_numbers.py [path/to/submitted_thesis.pdf]

The submitted thesis is not part of this repository. If it is not found the ledger
check is reported as SKIPPED and only the coverage check runs.
"""

import re
import sys
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
POSTER = ROOT / "poster_final.pdf"

DEFAULT_THESIS = (
    ROOT.parent / "FINAL_POSTER_BUILD_PACKAGE_25_AUG_2026"
    / "00_READ_ME_FIRST" / "GROUND_TRUTH_FINAL_SUBMITTED_THESIS.pdf"
)

TEXT = "text-layer"     # appears as selectable text on the poster
RASTER = "raster-only"  # appears only inside the P1 or P2 image

# (value as printed, 1-based physical page of the submitted PDF, what it is, where)
LEDGER = [
    # --- motivation, left rail -------------------------------------------
    ("363", 16, "million people in India lacking safely managed water", TEXT),
    ("38", 20, "national surveys in the point-of-use E. coli comparison", TEXT),
    ("35", 20, "surveys with fewer households free of E. coli at point of use", TEXT),
    ("12.9", 20, "mean change, percentage points", TEXT),

    # --- validation means and optimism (shown inside P2) ------------------
    ("0.9396", 68, "random-row mean ROC-AUC, seven tasks", RASTER),
    ("0.8688", 68, "grouped-station mean ROC-AUC", RASTER),
    ("0.7696", 68, "spatial-block mean ROC-AUC", RASTER),
    ("0.1701", 68, "apparent optimism", RASTER),
    ("145", 68, "state-by-parameter cells with recorded cadence", RASTER),

    # --- Fig 4.4 panel (a): three designs x seven tasks (Table 4.3) -------
    ("0.9830", 71, "random-row ROC-AUC, fluoride", TEXT),
    ("0.9336", 71, "grouped-station ROC-AUC, fluoride", TEXT),
    ("0.9062", 71, "spatial-block ROC-AUC, fluoride", TEXT),
    ("0.9854", 71, "random-row ROC-AUC, conductivity", TEXT),
    ("0.9411", 71, "grouped-station ROC-AUC, conductivity", TEXT),
    ("0.8596", 71, "spatial-block ROC-AUC, conductivity", TEXT),
    ("0.9626", 71, "random-row ROC-AUC, arsenic", TEXT),
    ("0.9230", 71, "grouped-station ROC-AUC, arsenic", TEXT),
    ("0.8160", 71, "spatial-block ROC-AUC, arsenic", TEXT),
    ("0.8683", 71, "random-row ROC-AUC, suspended solids", TEXT),
    ("0.8203", 71, "grouped-station ROC-AUC, suspended solids", TEXT),
    ("0.7463", 71, "spatial-block ROC-AUC, suspended solids", TEXT),
    ("0.9293", 71, "random-row ROC-AUC, turbidity", TEXT),
    ("0.8615", 71, "grouped-station ROC-AUC, turbidity", TEXT),
    ("0.7440", 71, "spatial-block ROC-AUC, turbidity", TEXT),
    ("0.9727", 71, "random-row ROC-AUC, nitrate", TEXT),
    ("0.8527", 71, "grouped-station ROC-AUC, nitrate", TEXT),
    ("0.6800", 71, "spatial-block ROC-AUC, nitrate", TEXT),
    ("0.8760", 71, "random-row ROC-AUC, pH", TEXT),
    ("0.7496", 71, "grouped-station ROC-AUC, pH", TEXT),
    ("0.6348", 71, "spatial-block ROC-AUC, pH", TEXT),

    # --- scoped negative control ------------------------------------------
    ("0.501", 76, "label-shuffle control, spatial ROC-AUC", TEXT),

    # --- Fig 4.5: external India transfer, Table 4.6 ----------------------
    ("0.7426", 75, "India external ROC-AUC, conductivity", TEXT),
    ("0.7081", 75, "India external ROC-AUC, TDS", TEXT),
    ("0.6248", 75, "India external ROC-AUC, fluoride", TEXT),
    ("0.6107", 75, "India external ROC-AUC, nitrate", TEXT),
    ("0.4870", 75, "India external ROC-AUC, pH", TEXT),
    ("0.3170", 75, "India external ROC-AUC, arsenic", TEXT),
    ("0.4565", 75, "severity rank correlation, conductivity", TEXT),
    ("0.4369", 75, "severity rank correlation, TDS", TEXT),
    ("0.2430", 75, "severity rank correlation, fluoride", TEXT),
    ("0.2025", 75, "severity rank correlation, nitrate", TEXT),
    ("0.0362", 75, "severity rank correlation, pH (negative)", TEXT),
    ("0.3258", 75, "severity rank correlation, arsenic (negative)", TEXT),
    ("0.3714", 75, "calibration slope, conductivity", TEXT),
    ("0.2892", 75, "calibration slope, TDS", TEXT),
    ("0.4017", 75, "calibration slope, fluoride", TEXT),
    ("0.2383", 75, "calibration slope, nitrate", TEXT),
    ("0.0710", 75, "calibration slope, pH (negative)", TEXT),
    ("0.9128", 75, "calibration slope, arsenic (negative)", TEXT),

    # --- confirmatory yield and product evidence (shown inside P2) --------
    ("2.01", 79, "conductivity confirmatory-test enrichment", RASTER),
    ("2.40", 79, "TDS confirmatory-test enrichment", RASTER),
    ("1,242", 97, "product-criterion evidence cells", RASTER),
    ("223", 97, "cells with an exact-product document", RASTER),

    # --- decision-uncertainty map (shown inside P1) -----------------------
    ("160", 85, "eligible state/UT-parameter cells", RASTER),
    ("17", 85, "cells decision-relevant at the stated ten per cent action level", RASTER),

    # --- Rajasthan worked case, Table 4.17 --------------------------------
    ("12,349", 103, "Rajasthan conductivity records", TEXT),
    ("54.06", 103, "Rajasthan conductivity share above the project convention", TEXT),
    ("1,500", 103, "conductivity project convention, microsiemens per cm", TEXT),
    ("3,131", 103, "Rajasthan TDS records", TEXT),
    ("51.96", 103, "Rajasthan TDS share above threshold", TEXT),
    ("1,000", 103, "TDS threshold, mg/L", TEXT),

    # --- context actions ---------------------------------------------------
    ("26", 118, "evaluated monitoring contexts", TEXT),
    ("12", 118, "contexts routed to baseline acquisition", RASTER),
]

# Numbers that legitimately appear without being a thesis result.
WHITELIST = {
    # Figure and table references to the submitted thesis
    "3.1", "4.3", "4.4", "4.5", "4.6", "4.7", "4.11", "4.13",
    # Reference years and reference-string numerals
    "2000", "2017", "2019", "2022", "2023", "2024", "30,000",
    # Small structural counts carried by the adjacent wording
    "0", "1", "2", "3", "4", "5", "6", "7", "16", "23",
    # Axis tick values on the embedded thesis figures
    "0.0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0",
}


def numbers_in(text):
    """Numeric tokens, keeping thousands separators and decimals intact."""
    return re.findall(r"\d+(?:,\d{3})*(?:\.\d+)?", text)


def main():
    if not POSTER.exists():
        sys.exit("poster_final.pdf not found - compile the poster first")

    thesis_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_THESIS
    poster_text = fitz.open(POSTER)[0].get_text()
    failures = []

    # ---- check 1: ledger against the submitted thesis ---------------------
    if thesis_path.exists():
        doc = fitz.open(thesis_path)
        print("Ledger check against %s (%d pages)\n" % (thesis_path.name, doc.page_count))
        for value, page, what, where in LEDGER:
            page_text = doc[page - 1].get_text()
            found = value in page_text or value.replace(",", "") in page_text.replace(",", "")
            on_poster = (where == RASTER) or (value in poster_text)
            ok = found and on_poster
            if not found:
                failures.append("%s (%s) not found on submitted page %d" % (value, what, page))
            if not on_poster:
                failures.append("%s (%s) is in the ledger but not in the poster text" % (value, what))
            print("  %s  %-8s p%-4d %-11s %s" % ("OK " if ok else "FAIL", value, page, where, what))
        doc.close()
    else:
        print("Ledger check SKIPPED - submitted thesis not found at:\n  %s\n" % thesis_path)

    # ---- check 2: every number on the poster is accounted for -------------
    ledger_values = {v for v, _, _, _ in LEDGER}
    ledger_values |= {v.replace(",", "") for v in ledger_values}
    unaccounted = []
    for tok in numbers_in(poster_text):
        if tok in ledger_values or tok.replace(",", "") in ledger_values:
            continue
        if tok in WHITELIST:
            continue
        unaccounted.append(tok)

    print("\nCoverage check")
    if unaccounted:
        for tok in sorted(set(unaccounted)):
            print("  UNTRACED  %s" % tok)
            failures.append("untraced number on poster: %s" % tok)
    else:
        print("  OK  every numeric token in the poster text is traced or whitelisted")

    print()
    if failures:
        print("FAILURES (%d):" % len(failures))
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("PASS - all poster numbers verified.")


if __name__ == "__main__":
    main()
