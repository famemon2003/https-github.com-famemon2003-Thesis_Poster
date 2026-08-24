"""Build the poster-specific figures for the A1 landscape thesis poster.

Every value in this file is transcribed from the submitted report
``ResearchPaper-06058747-Muhammad Faseeh Memon-Templeton.pdf`` (293 pages), with the
source page recorded beside it. Nothing is refitted, recomputed, aggregated or derived.
The only transformations applied are selection, ordering, re-typesetting at poster scale
and colour mapping. See ``poster_source_traceability.md``.

Output: vector PDF into ``Images/poster/``.
Run: ``python scripts/build_poster_figures.py`` from the repository root.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Patch, Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Images" / "poster"
OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Typography: register Imperial Sans Text so poster charts match poster body text.
# Figures are drawn at the exact on-poster column width (19.025 cm = 7.49 in), so a
# point size set here is the point size the reader sees. Nothing is below 13.5 pt,
# and no data label is below 15 pt.
# ---------------------------------------------------------------------------
FONTS = ROOT / "Fonts"
for ttf in sorted(FONTS.glob("ImperialSansText-*.ttf")):
    font_manager.fontManager.addfont(str(ttf))

FAMILY = "Imperial Sans Text" if any(
    f.name == "Imperial Sans Text" for f in font_manager.fontManager.ttflist
) else "DejaVu Sans"

COL_W = 7.49  # inches; one poster column

plt.rcParams.update({
    "font.family": FAMILY,
    "font.size": 17,
    "axes.titlesize": 20,
    "axes.labelsize": 17,
    "xtick.labelsize": 16,
    "ytick.labelsize": 17,
    "legend.fontsize": 16,
    "axes.edgecolor": "#4A4A4A",
    "axes.linewidth": 1.2,
    "pdf.fonttype": 42,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
})

# Imperial brand plus the thesis's own verdict encoding (Fig 4.5, Fig 4.13).
ICL_DARK = "#000080"     # ICLDarkBlue, RGB(0,0,128)
MID = "#6D8FB0"          # partial / intermediate
PALE = "#B9C6DE"         # optimistic / least leakage-safe
SAND = "#E8E0D6"         # absent, refuted or deferred
RUST = "#9C4A2F"         # transfer not supported
OCHRE = "#C9A227"        # evidence insufficient
GREY = "#5A5A5A"


def save(fig, name):
    path = OUT / name
    fig.savefig(path, format="pdf")
    plt.close(fig)
    print("wrote", path.relative_to(ROOT))


# ===========================================================================
# P2 - Leakage-safe validation.  Source: Fig 4.4 p70, Table 4.3 p71,
#      Table 4.4 p72, Section 4.3 p68 of the submitted PDF.
# ===========================================================================
def build_p2():
    # Mean ROC-AUC across the seven canonical tasks (p68, abstract p2).
    designs = ["Random row", "Grouped station", "Spatial block"]
    means = [0.9396, 0.8688, 0.7696]
    shades = [PALE, MID, ICL_DARK]

    # Per-task spatial-block ROC-AUC (Table 4.3 p71; Fig 4.4 panel a).
    tasks = ["Fluoride", "Conductivity", "Arsenic", "Suspended solids",
             "Turbidity", "Nitrate", "pH"]
    spatial = [0.9062, 0.8596, 0.8160, 0.7463, 0.7440, 0.6800, 0.6348]

    fig = plt.figure(figsize=(COL_W, 6.0))
    gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.35], hspace=0.46)

    # --- panel a: the three validation designs -----------------------------
    ax = fig.add_subplot(gs[0])
    y = [2, 1, 0]
    ax.barh(y, means, height=0.62, color=shades, zorder=3)
    for yi, v in zip(y, means):
        ax.text(v - 0.008, yi, "%.4f" % v, va="center", ha="right",
                color="white", fontweight="bold", fontsize=19, zorder=4)
    ax.set_yticks(y)
    ax.set_yticklabels(designs)
    ax.set_xlim(0.5, 1.0)
    ax.set_xticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_xlabel("Mean ROC-AUC, seven tasks")
    ax.set_title("a  Validation design changes the answer",
                 loc="left", fontweight="bold", color=ICL_DARK, pad=34)
    ax.annotate("", xy=(0.7696, 2.60), xytext=(0.9396, 2.60),
                annotation_clip=False,
                arrowprops=dict(arrowstyle="<->", color=RUST, lw=2.0))
    ax.text(0.855, 2.74, "optimism 0.1701", ha="center", va="bottom",
            color=RUST, fontweight="bold", fontsize=17, clip_on=False)
    ax.set_ylim(-0.6, 2.55)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="x", color="#DDDDDD", lw=0.9, zorder=0)
    ax.set_axisbelow(True)

    # --- panel b: the seven tasks under spatial blocking -------------------
    ax2 = fig.add_subplot(gs[1])
    yb = list(range(len(tasks)))[::-1]
    colours = [ICL_DARK if v >= 0.70 else RUST for v in spatial]
    ax2.barh(yb, spatial, height=0.66, color=colours, zorder=3)
    for yi, v in zip(yb, spatial):
        ax2.text(v - 0.008, yi, "%.4f" % v, va="center", ha="right",
                 color="white", fontweight="bold", fontsize=16, zorder=4)
    ax2.axvline(0.70, color=GREY, ls="--", lw=1.6, zorder=2)
    ax2.set_yticks(yb)
    ax2.set_yticklabels(tasks)
    ax2.set_xlim(0.5, 1.03)
    ax2.set_xticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax2.set_xlabel("Spatial-block ROC-AUC")
    ax2.set_title("b  Five of seven stay acceptable or better",
                  loc="left", fontweight="bold", color=ICL_DARK, pad=12)
    ax2.set_ylim(-0.7, len(tasks) - 0.15)
    for s in ("top", "right"):
        ax2.spines[s].set_visible(False)
    ax2.grid(axis="x", color="#DDDDDD", lw=0.9, zorder=0)
    ax2.set_axisbelow(True)

    fig.text(0.0, -0.008,
             "Bands are general ROC-AUC heuristics (Hosmer, Lemeshow and Sturdivant,\n"
             "2013), not established environmental thresholds. Every spatial PR-AUC\n"
             "exceeds its prevalence baseline, 7 of 7.",
             fontsize=16, color=GREY, va="top", ha="left")
    save(fig, "P2_leakage_safe_validation.pdf")


# ===========================================================================
# P3 - External transfer to India.  Source: Fig 4.5 p77, Table 4.6 p75.
# ===========================================================================
def build_p3():
    params = ["Conductivity", "TDS", "Fluoride", "Nitrate", "pH", "Arsenic"]
    auc = [0.7426, 0.7081, 0.6248, 0.6107, 0.4870, 0.3170]
    rho = [0.4565, 0.4369, 0.2430, 0.2025, -0.0362, -0.3258]
    slope = [0.3714, 0.2892, 0.4017, 0.2383, -0.0710, -0.9128]
    verdict = ["supported", "supported", "supported", "supported",
               "not supported", "insufficient"]
    cmap = {"supported": ICL_DARK, "not supported": RUST, "insufficient": OCHRE}
    colours = [cmap[v] for v in verdict]

    fig, axes = plt.subplots(1, 3, figsize=(COL_W, 4.4), sharey=True,
                             gridspec_kw=dict(wspace=0.16))
    y = list(range(len(params)))[::-1]

    panels = [
        (auc, "a  Threshold\n    discrimination", "ROC-AUC", (0.0, 1.06), None,
         [0.0, 0.5, 1.0]),
        (rho, "b  Severity\n    ranking", "Rank correlation", (-0.55, 0.82), 0.0,
         [-0.4, 0.0, 0.4]),
        (slope, "c  Calibration\n    slope", "Calibration slope", (-1.50, 0.85), 0.0,
         [-1.0, 0.0]),
    ]
    for ax, (vals, title, xlabel, xlim, zero, xticks) in zip(axes, panels):
        ax.barh(y, vals, height=0.66, color=colours, zorder=3)
        span = xlim[1] - xlim[0]
        for yi, v in zip(y, vals):
            offset = 0.022 * span
            if v >= 0:
                ax.text(v + offset, yi, "%.4f" % v, va="center", ha="left",
                        fontsize=15, color=GREY)
            else:
                ax.text(v - offset, yi, "%.4f" % v, va="center", ha="right",
                        fontsize=15, color=GREY)
        if zero is not None:
            ax.axvline(zero, color=GREY, lw=1.2)
        ax.set_xlim(*xlim)
        ax.set_xticks(xticks)
        ax.set_xlabel(xlabel, fontsize=15)
        ax.set_title(title, loc="left", fontweight="bold", color=ICL_DARK,
                     fontsize=16.5)
        ax.tick_params(axis="x", labelsize=14)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.grid(axis="x", color="#DDDDDD", lw=0.9, zorder=0)
        ax.set_axisbelow(True)
        ax.set_ylim(-0.7, len(params) - 0.3)

    axes[0].set_yticks(y)
    axes[0].set_yticklabels(params, fontsize=16.5)

    handles = [Patch(facecolor=ICL_DARK, label="Rank transfer supported"),
               Patch(facecolor=RUST, label="Transfer not supported"),
               Patch(facecolor=OCHRE, label="Evidence insufficient")]
    fig.legend(handles=handles, loc="upper left", ncol=3, frameon=False,
               bbox_to_anchor=(-0.005, 1.10), fontsize=14.5, handlelength=1.2,
               columnspacing=1.1, handletextpad=0.5)
    fig.text(0.0, -0.10,
             "A supported rank is not a calibrated probability: every India row carries\n"
             "negative Brier skill, so recalibration on local labels is required before\n"
             "any score is read as a local exceedance probability.",
             fontsize=16, color=GREY, va="top", ha="left")
    save(fig, "P3_india_external_transfer.pdf")


# ===========================================================================
# P4 - What the next action actually is.  Source: Fig 4.14 panel a p106;
#      counts restated at p118 and in the Conclusions p127.
# ===========================================================================
def build_p4():
    actions = [
        ("Acquire a baseline measurement population", 12),
        ("Repair identity, units or metadata", 6),
        ("Extend repeat measurement and cadence", 4),
        ("Collect local recalibration labels", 1),
        ("Governance review of a threshold", 1),
        ("Paired field against reference validation", 1),
        ("Other", 1),
    ]
    labels = [a for a, _ in actions]
    counts = [c for _, c in actions]
    assert sum(counts) == 26

    fig, ax = plt.subplots(figsize=(COL_W, 2.95))
    y = list(range(len(labels)))[::-1]
    colours = [ICL_DARK] + [MID] * (len(labels) - 1)
    ax.barh(y, counts, height=0.66, color=colours, zorder=3)
    for yi, c in zip(y, counts):
        ax.text(c + 0.25, yi, str(c), va="center", ha="left",
                fontsize=17, color=GREY, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=15)
    ax.set_xlim(0, 14.6)
    ax.set_xticks([0, 5, 10])
    ax.set_xlabel("Monitoring contexts, of 26", fontsize=16)
    fig.text(0.0, 1.0, "Every evaluated context returned a next action",
             fontweight="bold", color=ICL_DARK, fontsize=18.5, ha="left", va="bottom")
    ax.set_ylim(-0.7, len(labels) - 0.3)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="x", color="#DDDDDD", lw=0.9, zorder=0)
    ax.set_axisbelow(True)
    # The note that these are direct counts, not scores, and cover 26 contexts
    # rather than 26 countries or sites, is set in the poster source beneath the
    # figure so that it cannot collide with the axis label at this figure height.
    save(fig, "P4_next_action_26_contexts.pdf")


# ===========================================================================
# P5 - The binding constraint by parameter.  Source: Fig 4.13 p104.
# The verdict grid was read directly from the vector content of the submitted
# figure asset THESIS_LATEX_BUILD/figures/figure_4-13.pdf: 72 cells, three
# recorded verdict levels. No cell is scored, summed or reordered.
# A = adequate, P = partial or weak, . = absent, refuted or deferred
# ===========================================================================
def build_p5():
    rows = ["pH", "Conductivity", "TDS", "Nitrate", "Fluoride",
            "Arsenic", "Turbidity", "E. coli"]
    cols = ["Accepted\nbaseline", "Temporal\nsupport", "Rank\ntransfer",
            "Probability\ncalibration", "Direct\nmeasurement",
            "Independent\nevidence", "Deployment\nevidence", "Cost\nevidence",
            "Permitted\noutcome"]
    grid = [
        "AA....P..",   # pH
        "AAA...P.P",   # Conductivity
        "APA...P.P",   # TDS
        "A.P...P.P",   # Nitrate
        "A.P...P.P",   # Fluoride
        "......P..",   # Arsenic
        "......P..",   # Turbidity
        ".....AP..",   # E. coli
    ]
    assert len(grid) == len(rows)
    for r in grid:
        assert len(r) == len(cols), r

    fill = {"A": ICL_DARK, "P": MID, ".": SAND}
    fig, ax = plt.subplots(figsize=(COL_W, 4.25))
    for i, r in enumerate(grid):
        for j, v in enumerate(r):
            ax.add_patch(Rectangle((j, len(rows) - 1 - i), 0.94, 0.94,
                                   facecolor=fill[v], edgecolor="white", lw=1.4))
    ax.set_xlim(-0.06, 9.0)
    ax.set_ylim(-0.06, len(rows))
    ax.set_xticks([j + 0.47 for j in range(len(cols))])
    ax.set_xticklabels(cols, fontsize=14.5, rotation=38, ha="right",
                       rotation_mode="anchor")
    ax.set_yticks([len(rows) - 1 - i + 0.47 for i in range(len(rows))])
    ax.set_yticklabels(rows, fontsize=16)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    fig.text(0.0, 1.0, "The binding constraint changes by parameter",
             fontweight="bold", color=ICL_DARK, fontsize=18.5, ha="left", va="bottom")
    handles = [Patch(facecolor=ICL_DARK, label="Adequate"),
               Patch(facecolor=MID, label="Partial or weak"),
               Patch(facecolor=SAND, label="Absent, refuted or deferred")]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.02, -0.40),
              ncol=3, frameon=False, fontsize=14.5, handlelength=1.2,
              columnspacing=1.2, handletextpad=0.5)
    save(fig, "P5_binding_constraint.pdf")


if __name__ == "__main__":
    build_p2()
    build_p3()
    build_p4()
    build_p5()
