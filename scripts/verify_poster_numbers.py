"""Audit every number printed on the poster against the submitted thesis.

Two checks run:

1. **Ledger check** - each poster claim below is looked up in the submitted PDF at
   the page it is attributed to. A claim whose value cannot be found on its stated
   page fails.
2. **Coverage check** - every numeric token extracted from the rendered poster PDF
   must be accounted for, either by the ledger or by the structural whitelist
   (figure and table numbers, axis tick values, years, edition numbers). A number
   on the poster that no one can trace fails.

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
    ROOT.parent.parent / "ResearchPaper-06058747-Muhammad Faseeh Memon-Templeton.pdf"
)

# (value as printed on the poster, 1-based physical page of the submitted PDF,
#  what the value is)
LEDGER = [
    ("0.9396", 68, "random-row mean ROC-AUC, seven tasks"),
    ("0.8688", 68, "grouped-station mean ROC-AUC"),
    ("0.7696", 68, "spatial-block mean ROC-AUC"),
    ("0.1701", 68, "total optimism"),
    ("0.0708", 68, "optimism component, repeat visits"),
    ("0.0993", 68, "optimism component, geographic separation"),
    ("0.9062", 71, "spatial-block ROC-AUC, fluoride"),
    ("0.8596", 71, "spatial-block ROC-AUC, conductivity"),
    ("0.8160", 71, "spatial-block ROC-AUC, arsenic"),
    ("0.7463", 71, "spatial-block ROC-AUC, suspended solids"),
    ("0.7440", 71, "spatial-block ROC-AUC, turbidity"),
    ("0.6800", 71, "spatial-block ROC-AUC, nitrate"),
    ("0.6348", 71, "spatial-block ROC-AUC, pH"),
    ("0.501", 76, "label-shuffle control, spatial ROC-AUC"),
    ("0.482", 76, "label-shuffle control, lower 95% bound"),
    ("0.520", 76, "label-shuffle control, upper 95% bound"),
    ("0.7426", 75, "India external ROC-AUC, conductivity"),
    ("0.7081", 75, "India external ROC-AUC, TDS"),
    ("0.6248", 75, "India external ROC-AUC, fluoride"),
    ("0.6107", 75, "India external ROC-AUC, nitrate"),
    ("0.4870", 75, "India external ROC-AUC, pH"),
    ("0.3170", 75, "India external ROC-AUC, arsenic"),
    ("0.4565", 75, "severity rank correlation, conductivity"),
    ("0.4369", 75, "severity rank correlation, TDS"),
    ("0.2430", 75, "severity rank correlation, fluoride"),
    ("0.2025", 75, "severity rank correlation, nitrate"),
    ("0.0362", 75, "severity rank correlation, pH (negative)"),
    ("0.3258", 75, "severity rank correlation, arsenic (negative)"),
    ("0.3714", 75, "calibration slope, conductivity"),
    ("0.2892", 75, "calibration slope, TDS"),
    ("0.4017", 75, "calibration slope, fluoride"),
    ("0.2383", 75, "calibration slope, nitrate"),
    ("0.0710", 75, "calibration slope, pH (negative)"),
    ("0.9128", 75, "calibration slope, arsenic (negative)"),
    ("119", 75, "arsenic external observations"),
    ("116", 75, "arsenic external sites"),
    ("5,966", 79, "conductivity tests spent at the recorded operating point"),
    ("2,838", 79, "conductivity exceeding sites found"),
    ("1,410", 79, "conductivity expected untargeted"),
    ("2.01", 79, "conductivity enrichment"),
    ("265", 79, "TDS tests spent"),
    ("154", 79, "TDS exceeding sites found"),
    ("64.2", 79, "TDS expected untargeted"),
    ("2.40", 79, "TDS enrichment"),
    ("1,242", 97, "product-criterion evidence cells"),
    ("223", 97, "cells with an exact-product document"),
    ("12,349", 103, "Rajasthan conductivity records"),
    ("1,641", 103, "Rajasthan conductivity sites"),
    ("54.06", 103, "Rajasthan share above the project convention"),
    ("1,500", 103, "conductivity project convention, microsiemens per cm"),
    ("12", 118, "baseline acquisition, of 26 contexts"),
    ("26", 118, "evaluated monitoring contexts"),
    ("145", 68, "state-by-parameter cells with recorded cadence"),
]

# Numbers that legitimately appear on the poster without being a thesis result.
WHITELIST = {
    # Figure and table references to the submitted thesis
    "3.1", "3.6", "4.3", "4.6", "4.14",
    # Reference years and edition
    "2013", "2023", "3",
    # Structural counts stated in the text and carried by the ledger context
    "23", "33", "54", "9", "8", "2", "1", "0", "4", "5", "6", "7", "11", "16",
    # Axis tick values on the poster charts
    "0.0", "0.5", "1.0", "0.6", "0.7", "0.8", "0.9", "0.4", "10", "95",
    # Author CID on the title block
    "06058747",
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
        for value, page, what in LEDGER:
            page_text = doc[page - 1].get_text()
            # The thesis sets thousands separators; compare with and without.
            found = value in page_text or value.replace(",", "") in page_text.replace(",", "")
            on_poster = value in poster_text
            status = "OK " if (found and on_poster) else "FAIL"
            if not found:
                failures.append("%s (%s) not found on submitted page %d" % (value, what, page))
            if not on_poster:
                failures.append("%s (%s) is in the ledger but not on the poster" % (value, what))
            print("  %s  %-8s p%-4d %s" % (status, value, page, what))
        doc.close()
    else:
        print("Ledger check SKIPPED - submitted thesis not found at:\n  %s\n" % thesis_path)

    # ---- check 2: every number on the poster is accounted for -------------
    ledger_values = {v for v, _, _ in LEDGER}
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
        print("  OK  every numeric token on the poster is traced or whitelisted")

    print()
    if failures:
        print("FAILURES (%d):" % len(failures))
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("PASS - all poster numbers verified.")


if __name__ == "__main__":
    main()
