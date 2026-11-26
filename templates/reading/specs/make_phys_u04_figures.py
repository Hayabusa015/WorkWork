#!/usr/bin/env python3
"""Figures 4.1-4.7 for the Physics U4 unit reading (Work, Energy & Power).

    python3 templates/reading/specs/make_phys_u04_figures.py OUT_DIR

Drawn with matplotlib at the size they print: FIG_IN wide (the builder places every
figure at FIG_W_IN = 3.0 in), so an 8 pt label is 8 pt on paper. Every number traces to
reports/phys_u04_reading_dossier.md section B (DER) or section C; each plotted value is
computed here from the givens with g = 9.8 m/s^2, and a mismatch with the dossier stops the
build.

Course rules (courses/physics/DECISIONS.md): an FBD has one labelled arrow per force,
scaled to relative magnitude, and no motion arrow (Figure 4.1a). Displacement is never an
arrow on an FBD: it is a dimension bracket on a separate scene sketch (dossier A-5). The
angle in the angled pull is marked between F and the horizontal, the direction of d.

Print discipline (brand/SHULL_DESIGN_SYSTEM.md section 8): outlines only, no fills; a
chart area is hatched, not tinted. Distinctions are carried by line style, hatch and
label, never by hue alone. Quantum Gold (the course `primary`) prints pale, so nothing that
must be read is drawn in it: lines are ink and labels are ink or the text-safe
`primaryDeep`. Type is Archivo; theta, which Archivo lacks, comes from the brand math
fallback (typography.mathFallback, Inter) through matplotlib's font fallback. Colour is
read from brand/tokens.json; no hex is typed here.
"""
import json, math, os, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                   # noqa: E402
from matplotlib import font_manager                               # noqa: E402
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch, Arc  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
FONTS = os.path.join(REPO, "brand", "fonts")
for f in ("Archivo-Regular.ttf", "Archivo-Bold.ttf", "Archivo-SemiBold.ttf"):
    font_manager.fontManager.addfont(os.path.join(FONTS, f))
INTER = "/usr/share/fonts/opentype/inter"
for f in ("Inter-Regular.otf", "Inter-Bold.otf"):
    if not os.path.exists(os.path.join(INTER, f)):
        sys.exit(f"math fallback face {f} is not installed (typography.mathFallback)")
    font_manager.fontManager.addfont(os.path.join(INTER, f))
plt.rcParams.update({
    "font.family": ["Archivo", "Inter"], "mathtext.fontset": "custom", "mathtext.rm": "Archivo",
    "mathtext.it": "Archivo", "mathtext.bf": "Archivo:bold", "mathtext.cal": "Archivo",
    "mathtext.sf": "Archivo", "mathtext.tt": "Archivo", "mathtext.fallback": None,
    "axes.unicode_minus": True, "svg.fonttype": "none",
    "hatch.linewidth": 0.5,
})

DPI = 300
FIG_IN = 3.0
G = 9.8
INK = T["ground"]["asphalt"]["hex"]
LABEL = T["ground"]["label"]["hex"]
HAIR = T["ground"]["ruleHairline"]["hex"]
ACCENT = T["courses"]["physics"]["primaryDeep"]["hex"]     # type on white
plt.rcParams["hatch.color"] = INK


def m(s):
    """'PE_{g}' -> mathtext in the text face for the sub/superscript only. Plain text
    passes through (so theta, outside mathtext, falls back to Inter)."""
    if "_{" not in s and "^{" not in s:
        return s
    out, i = "", 0
    while i < len(s):
        if s.startswith("_{", i) or s.startswith("^{", i):
            j = s.index("}", i)
            out += "$" + s[i] + "{\\mathregular{" + s[i + 2:j].replace("-", "{-}").replace("+", "{+}") + "}}$"
            i = j + 1
        else:
            out += s[i]
            i += 1
    return out.replace("$$", "")


def canvas(h_in):
    fig = plt.figure(figsize=(FIG_IN, h_in), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FIG_IN); ax.set_ylim(0, h_in); ax.axis("off")
    ax.set_aspect("equal")
    return fig, ax


def text(ax, x, y, s, size=8, weight="regular", color=INK, ha="center", va="center", rot=0):
    ax.text(x, y, m(s), fontsize=size, fontweight=weight, color=color, ha=ha, va=va, rotation=rot)


def arrow(ax, a, b, color=INK, lw=1.1, head=5.0, ls="-"):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=f"-|>,head_length={head},head_width={head * 0.55}",
                                 mutation_scale=1, color=color, linewidth=lw, linestyle=ls,
                                 shrinkA=0, shrinkB=0))


def bracket(ax, x0, x1, y, label, tick=0.06, size=8):
    """A dimension bracket (not an arrow): a line with end ticks and the label under it."""
    ax.plot([x0, x1], [y, y], color=INK, linewidth=0.8)
    for x in (x0, x1):
        ax.plot([x, x], [y - tick, y + tick], color=INK, linewidth=0.8)
    text(ax, (x0 + x1) / 2, y - 0.13, label, size, "semibold")


def vbracket(ax, x, y0, y1, label, tick=0.06, size=8, side="right"):
    ax.plot([x, x], [y0, y1], color=INK, linewidth=0.8)
    for y in (y0, y1):
        ax.plot([x - tick, x + tick], [y, y], color=INK, linewidth=0.8)
    dx = 0.08 if side == "right" else -0.08
    text(ax, x + dx, (y0 + y1) / 2, label, size, "semibold", ha="left" if side == "right" else "right")


def crate(ax, x, y, w, h, ls="-", lw=1.1):
    ax.add_patch(Rectangle((x, y), w, h, fill=False, edgecolor=INK, linewidth=lw, linestyle=ls))


def floor(ax, x0, x1, y):
    ax.plot([x0, x1], [y, y], color=INK, linewidth=1.0)
    k = x0 + 0.04
    while k < x1:                       # ground hatching ticks, ink, thin
        ax.plot([k, k - 0.06], [y, y - 0.06], color=HAIR, linewidth=0.6)
        k += 0.12


def graph_axes(fig, rect):
    ax = fig.add_axes(rect)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK); ax.spines[s].set_linewidth(0.8)
    ax.tick_params(colors=INK, labelsize=7.6, width=0.6, length=2.5)
    return ax


def save(fig, out):
    fig.savefig(out, dpi=DPI, facecolor="white")
    plt.close(fig)


def check(name, got, want, tol=1e-6):
    if abs(got - want) > tol * max(1.0, abs(want)):
        sys.exit(f"{name}: computed {got}, dossier says {want}")


# ---------------------------------------------------------------------------------
def fig_crate(out):
    """4.1: Example 4.1. (a) FBD of the crate: F_push 120. N, f_k 90.0 N, F_N, F_g - four
    arrows, one per force, horizontal pair scaled 120 : 90, F_N = F_g (the vertical pair is
    not to scale with the horizontal pair; no mass is given). No motion arrow. (b) A
    separate scene sketch: start and end positions, d = 4.00 m as a dimension bracket."""
    push, fric = 120.0, 90.0
    check("4.1 net force", push - fric, 30.0)
    fig, ax = canvas(1.62)
    # (a) FBD
    text(ax, 0.06, 1.52, "(a) FREE-BODY DIAGRAM", 7.6, "bold", ACCENT, ha="left")
    cx, cy, s = 0.74, 0.80, 0.28                 # crate centre and size
    crate(ax, cx - s / 2, cy - s / 2, s, s)
    unit = 0.0048                                # in per newton, horizontal pair
    lp, lf = push * unit, fric * unit
    arrow(ax, (cx + s / 2, cy), (cx + s / 2 + lp, cy))
    text(ax, cx + s / 2 + lp, cy + 0.17, "F_{push} =\n120. N", 7.6, "semibold", ha="right")
    arrow(ax, (cx - s / 2, cy), (cx - s / 2 - lf, cy))
    text(ax, cx - s / 2 - lf, cy + 0.17, "f_{k} =\n90.0 N", 7.6, "semibold", ha="left")
    lv = 0.36
    arrow(ax, (cx, cy + s / 2), (cx, cy + s / 2 + lv))
    text(ax, cx + 0.06, cy + s / 2 + lv - 0.05, "F_{N}", 8, "semibold", ha="left")
    arrow(ax, (cx, cy - s / 2), (cx, cy - s / 2 - lv))
    text(ax, cx + 0.06, cy - s / 2 - lv + 0.05, "F_{g}", 8, "semibold", ha="left")
    # divider
    ax.plot([1.50, 1.50], [0.08, 1.50], color=HAIR, linewidth=0.6)
    # (b) scene
    text(ax, 1.60, 1.52, "(b) SCENE", 7.6, "bold", ACCENT, ha="left")
    fy = 0.62
    floor(ax, 1.58, 2.96, fy)
    w = 0.34
    x0, x1 = 1.68, 2.52
    crate(ax, x0, fy, w, w, ls=(0, (3, 2)), lw=0.9)
    crate(ax, x1, fy, w, w)
    text(ax, x0 + w / 2, fy + w + 0.10, "start", 7.6, color=LABEL)
    text(ax, x1 + w / 2, fy + w + 0.10, "end", 7.6, color=LABEL)
    bracket(ax, x0, x1, fy - 0.20, "d = 4.00 m")
    save(fig, out)


def fig_fx_rect(out):
    """4.2: F-x graph of the constant 120. N push over 4.00 m. The hatched area is the
    work: (120. N)(4.00 m) = 480. J (dossier B 4.1)."""
    F, d = 120.0, 4.00
    check("4.1 push work", F * d, 480.0)
    fig = plt.figure(figsize=(FIG_IN, 1.75), dpi=DPI)
    ax = graph_axes(fig, [0.17, 0.25, 0.78, 0.68])
    ax.plot([0, d], [F, F], color=INK, linewidth=1.3)
    ax.add_patch(Rectangle((0, 0), d, F, fill=False, edgecolor=INK, linewidth=0.0, hatch="////"))
    ax.plot([d, d], [0, F], color=INK, linewidth=0.8, linestyle=(0, (3, 2)))
    ax.set_xlim(0, 5.0); ax.set_ylim(0, 160)
    ax.set_xticks([0, 1, 2, 3, 4, 5]); ax.set_yticks([0, 40, 80, 120, 160])
    ax.set_xlabel("position x (m)", fontsize=8, color=INK, labelpad=2)
    ax.set_ylabel("force F (N)", fontsize=8, color=INK, labelpad=2)
    ax.text(2.0, 60, "area = work\n(120. N)(4.00 m) = 480. J", fontsize=7.8, color=INK,
            ha="center", va="center", fontweight="semibold",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))
    ax.text(2.0, 132, "F = 120. N", fontsize=7.8, color=ACCENT, ha="center", fontweight="semibold")
    save(fig, out)


def fig_angle(out):
    """4.3: the angled pull, a scene sketch (not an FBD). F = 50.0 N along the rope at
    30.0 deg above the horizontal; theta is marked between F and the horizontal, the
    direction of d. Dashed components: F cos(theta) = 43.3 N along d, F sin(theta) = 25.0 N
    perpendicular. d = 5.00 m as a bracket. W = 217 J (dossier B 4.1)."""
    F, th, d = 50.0, 30.0, 5.00
    fx, fy_ = F * math.cos(math.radians(th)), F * math.sin(math.radians(th))
    check("Fx", round(fx, 1), 43.3); check("Fy", round(fy_, 1), 25.0)
    check("pull work", round(F * d * math.cos(math.radians(th))), 217)
    fig, ax = canvas(1.55)
    gy = 0.50
    floor(ax, 0.04, 2.96, gy)
    w = 0.34
    x0, x1 = 0.10, 1.06
    crate(ax, x0, gy, w, w, ls=(0, (3, 2)), lw=0.9)
    crate(ax, x1, gy, w, w)
    text(ax, x0 + w / 2, gy + w + 0.10, "start", 7.6, color=LABEL)
    text(ax, x1 + w / 2, gy + w + 0.10, "end", 7.6, color=LABEL)
    bracket(ax, x0, x1, gy - 0.20, "d = 5.00 m")
    # the pull, from the end crate's upper right corner
    px, py = x1 + w, gy + w * 0.55
    L = 1.20
    ex, ey = px + L * math.cos(math.radians(th)), py + L * math.sin(math.radians(th))
    arrow(ax, (px, py), (ex, ey), lw=1.3)
    text(ax, ex - 0.02, ey + 0.11, "F = 50.0 N", 8, "bold", ha="right")
    # horizontal reference (direction of d), dashed components
    ax.plot([px, px + L + 0.15], [py, py], color=INK, linewidth=0.7, linestyle=(0, (1.5, 1.5)))
    hx = L * math.cos(math.radians(th))
    arrow(ax, (px, py - 0.0), (px + hx, py), lw=0.8, ls=(0, (3, 2)), head=4)
    arrow(ax, (px + hx, py), (px + hx, ey), lw=0.8, ls=(0, (3, 2)), head=4)
    text(ax, px + hx / 2 + 0.05, py - 0.12, "F cos θ = 43.3 N", 7.6, "semibold", ACCENT)
    text(ax, px + hx + 0.06, (py + ey) / 2, "F sin θ\n= 25.0 N", 7.6, "semibold", ACCENT, ha="left")
    ax.add_patch(Arc((px, py), 0.62, 0.62, theta1=0, theta2=th, color=INK, linewidth=0.8))
    text(ax, px + 0.40, py + 0.09, "θ = 30.0°", 7.6, "semibold", ha="left")
    save(fig, out)


def fig_ke_v(out):
    """4.4: KE = 1/2 m v^2 for the 1200. kg car of Example 4.2. 20.0 m/s -> 2.40 x 10^5 J;
    40.0 m/s -> 9.60 x 10^5 J: twice the speed, four times the KE (dossier B 4.2)."""
    mass = 1200.0
    ke = lambda v: 0.5 * mass * v * v
    check("KE at 20", ke(20.0), 2.40e5); check("KE at 40", ke(40.0), 9.60e5)
    check("ratio", ke(40.0) / ke(20.0), 4.0)
    fig = plt.figure(figsize=(FIG_IN, 1.95), dpi=DPI)
    ax = graph_axes(fig, [0.17, 0.22, 0.79, 0.72])
    vs = [i * 0.5 for i in range(0, 91)]
    ax.plot(vs, [ke(v) / 1e5 for v in vs], color=INK, linewidth=1.3)
    for v, lab in ((20.0, "2.40"), (40.0, "9.60")):
        k = ke(v) / 1e5
        ax.plot([v, v], [0, k], color=INK, linewidth=0.7, linestyle=(0, (3, 2)))
        ax.plot([0, v], [k, k], color=INK, linewidth=0.7, linestyle=(0, (3, 2)))
        ax.plot([v], [k], marker="o", markersize=3.6, markerfacecolor="white", markeredgecolor=INK,
                markeredgewidth=0.9)
    ax.set_xlim(0, 45); ax.set_ylim(0, 12)
    ax.set_xticks([0, 10, 20, 30, 40]); ax.set_yticks([0, 2.4, 4, 6, 8, 9.6, 12])
    ax.set_yticklabels(["0", "2.40", "", "", "", "9.60", ""])
    ax.set_xlabel("speed v (m/s)", fontsize=8, color=INK, labelpad=2)
    ax.set_ylabel(m("kinetic energy (10^{5} J)"), fontsize=8, color=INK, labelpad=2)
    ax.text(12, 6.6, "speed × 2\nKE × 4", fontsize=8, color=ACCENT, fontweight="bold", ha="center")
    ax.text(25.5, 1.3, "1200. kg car", fontsize=7.6, color=LABEL, ha="left")
    save(fig, out)


def fig_paths(out):
    """4.5: lift straight up versus a frictionless ramp to the same shelf height h, from
    the same reference level. The work against gravity is mgh on both paths (dossier B
    4.3, path independence via mg sin(theta) x L = mgh)."""
    fig, ax = canvas(1.62)
    gy, top = 0.34, 1.20
    # reference level
    ax.plot([0.04, 2.96], [gy, gy], color=INK, linewidth=1.0)
    text(ax, 0.06, gy - 0.13, "reference level (h = 0)", 7.6, "semibold", ACCENT, ha="left")
    # path 2: the ramp, up to the shelf edge
    rx0, rx1 = 0.22, 1.70
    ax.plot([rx0, rx1], [gy, top], color=INK, linewidth=1.1)
    th = math.degrees(math.atan2(top - gy, rx1 - rx0))
    ax.add_patch(Arc((rx0, gy), 0.56, 0.56, theta1=0, theta2=th, color=INK, linewidth=0.8))
    text(ax, rx0 + 0.32, gy + 0.08, "θ", 8, "semibold", ha="left")
    text(ax, 0.86, (gy + top) / 2 + 0.24, "path 2: up the ramp,", 7.6, ha="center", rot=th)
    text(ax, 0.98, (gy + top) / 2 + 0.10, "length L", 7.6, ha="center", rot=th)
    # shelf and h
    ax.plot([rx1, 2.96], [top, top], color=INK, linewidth=1.2)
    text(ax, 2.10, top + 0.10, "shelf", 7.6, color=LABEL)
    vbracket(ax, 1.88, gy, top, "", size=8)
    text(ax, 1.97, (gy + top) / 2, "h", 9, "bold", ha="left")
    # path 1: straight up (a path, drawn dashed; not a force)
    b = 0.16
    px = 2.74
    crate(ax, px, gy, b, b, ls=(0, (3, 2)), lw=0.8)
    crate(ax, px, top, b, b, lw=1.0)
    arrow(ax, (px + b / 2, gy + b + 0.04), (px + b / 2, top - 0.04), lw=0.8, ls=(0, (3, 2)), head=4)
    text(ax, px - 0.06, (gy + top) / 2 - 0.02, "path 1:\nstraight up", 7.6, "regular", ha="right")
    save(fig, out)


def fig_spring(out):
    """4.6: F = kx for k = 400. N/m up to x = 0.150 m (F = 60.0 N). The hatched triangle
    is the work done stretching the spring, 1/2 (0.150 m)(60.0 N) = 4.50 J (dossier B 4.3)."""
    k, x = 400.0, 0.150
    F = k * x
    check("kx", F, 60.0); check("triangle", 0.5 * x * F, 4.50); check("1/2 k x^2", 0.5 * k * x * x, 4.50)
    fig = plt.figure(figsize=(FIG_IN, 1.80), dpi=DPI)
    ax = graph_axes(fig, [0.17, 0.24, 0.78, 0.70])
    ax.plot([0, x], [0, F], color=INK, linewidth=1.3)
    ax.plot([x, 0.20], [F, k * 0.20], color=INK, linewidth=0.9, linestyle=(0, (3, 2)))
    ax.add_patch(Polygon([(0, 0), (x, 0), (x, F)], closed=True, fill=False, edgecolor=INK,
                         linewidth=0.0, hatch="////"))
    ax.plot([x, x], [0, F], color=INK, linewidth=0.8, linestyle=(0, (3, 2)))
    ax.plot([0, x], [F, F], color=INK, linewidth=0.7, linestyle=(0, (1.5, 1.5)))
    ax.set_xlim(0, 0.20); ax.set_ylim(0, 90)
    ax.set_xticks([0, 0.05, 0.10, 0.15, 0.20]); ax.set_xticklabels(["0", "0.050", "0.100", "0.150", "0.200"])
    ax.set_yticks([0, 20, 40, 60, 80])
    ax.set_xlabel("stretch or compression x (m)", fontsize=8, color=INK, labelpad=2)
    ax.set_ylabel("spring force F (N)", fontsize=8, color=INK, labelpad=2)
    ax.text(0.04, 74, "slope = k = 400. N/m", fontsize=7.8, color=ACCENT, fontweight="semibold", ha="left")
    ax.text(0.118, 14, "area\n= 4.50 J", fontsize=7.8, color=INK, fontweight="bold", ha="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.0))
    save(fig, out)


def fig_bars(out):
    """4.7: energy bar charts for a skateboarder on a ramp. Frictionless: top (all PE_g),
    halfway down in height (half and half), bottom (all KE); the total is the same in all
    three. With friction: at the bottom KE is less than the starting PE_g and a thermal bar
    makes up the difference, so the total is unchanged. Schematic: bar heights are to scale
    with each other, no values. Bars are outlined; KE is hatched, PE_g open, thermal
    dotted, so the three read apart in grayscale."""
    total = 1.0
    states = [("TOP", {"KE": 0.0, "PE_{g}": 1.0}),
              ("HALF THE HEIGHT", {"KE": 0.5, "PE_{g}": 0.5}),
              ("BOTTOM", {"KE": 1.0, "PE_{g}": 0.0})]
    fric = ("BOTTOM, WITH FRICTION", {"KE": 0.72, "PE_{g}": 0.0, "thermal": 0.28})
    for name, d in states + [fric]:
        check(f"bars {name}", sum(d.values()), total)
    style = {"KE": dict(hatch="//////"), "PE_{g}": dict(hatch=None), "thermal": dict(hatch="....")}
    fig, ax = canvas(2.30)
    H = 0.62          # bar height for the full total
    bw = 0.22

    def chart(x0, y0, title, d, width):
        keys = list(d)
        gap = (width - len(keys) * bw) / (len(keys) + 1)
        text(ax, x0 + width / 2, y0 + H + 0.17, title, 7.6, "bold", ACCENT)
        ax.plot([x0, x0 + width], [y0, y0], color=INK, linewidth=0.8)
        ax.plot([x0, x0 + width], [y0 + H, y0 + H], color=INK, linewidth=0.6, linestyle=(0, (1.5, 1.5)))
        for i, kname in enumerate(keys):
            bx = x0 + gap + i * (bw + gap)
            h = d[kname] * H
            if h > 0:
                ax.add_patch(Rectangle((bx, y0), bw, h, fill=False, edgecolor=INK, linewidth=0.9,
                                       **({"hatch": style[kname]["hatch"]} if style[kname]["hatch"] else {})))
            else:
                ax.plot([bx, bx + bw], [y0, y0], color=INK, linewidth=1.6)
            text(ax, bx + bw / 2, y0 - 0.10, kname, 7.6, "semibold")

    # y-axis label once, at the left (energy in J; schematic)
    text(ax, 0.07, 1.62, "energy (J)", 7.6, "regular", LABEL, rot=90)
    w = 0.86
    for i, (name, d) in enumerate(states):
        chart(0.18 + i * (w + 0.06), 1.33, name, d, w)
    chart(0.18, 0.24, fric[0], fric[1], 1.40)
    text(ax, 0.07, 0.55, "energy (J)", 7.6, "regular", LABEL, rot=90)
    text(ax, 1.72, 0.68, "dotted line: total energy\nat the top. The total\nnever changes.", 7.6,
         "regular", INK, ha="left", va="center")
    save(fig, out)


FIGS = {"fig4_1_crate.png": fig_crate, "fig4_2_fx_area.png": fig_fx_rect, "fig4_3_angle.png": fig_angle,
        "fig4_4_ke_v.png": fig_ke_v, "fig4_5_paths.png": fig_paths, "fig4_6_spring.png": fig_spring,
        "fig4_7_bars.png": fig_bars}


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "build", "phys_u04_reading", "fig")
    os.makedirs(out, exist_ok=True)
    for name, fn in FIGS.items():
        fn(os.path.join(out, name))
        print("wrote", os.path.join(out, name))


if __name__ == "__main__":
    main()
