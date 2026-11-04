#!/usr/bin/env python3
"""Draw every science figure for the PHYS U03 (Forces and Motion) section decks.

Hand-built, never generated: each figure carries a force value, an angle, or a label that
students read as science (build-presentation, Images). Every number drawn here is the
same number the deck spec and the teacher key use, so they are defined once, in VALUES,
and the figure reads them from there.

Colours come from brand/tokens.json; type from the shipped Archivo files.

    python3 scripts/build_diagram_phys_u03.py
"""
import json, math, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch, Arc

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "templates", "slide", "assets", "phys_u03")
os.makedirs(OUT, exist_ok=True)

for f in ("Archivo-Regular.ttf", "Archivo-SemiBold.ttf", "Archivo-Bold.ttf"):
    font_manager.fontManager.addfont(os.path.join(REPO, "brand", "fonts", f))
plt.rcParams["font.family"] = "Archivo"
plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Archivo"
plt.rcParams["mathtext.it"] = "Archivo:italic"

T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
WHITE = T["ground"]["white"]["hex"]
INK = T["ground"]["asphalt"]["hex"]
GRAPHITE = T["ground"]["graphite"]["hex"]
PARCH = T["ground"]["parchment"]["hex"]
MUTED = T["ground"]["label"]["hex"]
LIGHTMUTED = T["ground"]["mutedOnDark"]["hex"]
FORCE = T["courses"]["physics"]["primaryDeep"]["hex"]     # force arrows on light ground
GOLD = T["courses"]["physics"]["primary"]["hex"]          # force arrows on dark ground
COMP = T["courses"]["physics"]["secondary"]["hex"]        # components, second object
G = 9.8

# Slot sizes (inches) from the masters, so a figure is drawn at the shape it is placed in.
SLOT = {"setup": (4.78, 2.55), "diagram": (5.05, 3.0), "concept": (5.1, 2.87),
        "concept06": (5.45, 3.06), "data": (4.23, 2.48), "band": (6.2, 2.0), "aside": (2.88, 1.62)}


def canvas(slot, dark=False, xlim=None):
    w, h = SLOT[slot]
    fig = plt.figure(figsize=(w, h), dpi=300)
    fig.patch.set_facecolor(GRAPHITE if dark else WHITE)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(GRAPHITE if dark else WHITE)
    xl = xlim or (0, w)
    ax.set_xlim(*xl)
    ax.set_ylim(0, h * (xl[1] - xl[0]) / w)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=300, facecolor=fig.get_facecolor())
    plt.close(fig)


def arrow(ax, x, y, dx, dy, color=FORCE, lw=2.4, dashed=False):
    ax.add_patch(FancyArrowPatch((x, y), (x + dx, y + dy), arrowstyle="-|>", mutation_scale=14,
                                 color=color, lw=lw, linestyle="--" if dashed else "-",
                                 shrinkA=0, shrinkB=0, zorder=5))


def text(ax, x, y, s, size=11, color=INK, ha="center", va="center", bold=False, rot=0):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, rotation=rot,
            fontweight="bold" if bold else "normal", zorder=6)


def box(ax, cx, cy, w, h, label="", color=INK, fill=PARCH, size=10):
    ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, facecolor=fill, edgecolor=color,
                           lw=1.8, zorder=4))
    if label:
        text(ax, cx, cy, label, size=size, color=color, bold=True)


def ground(ax, x0, x1, y, color=MUTED):
    ax.plot([x0, x1], [y, y], color=color, lw=1.6, zorder=3)
    for i in range(int((x1 - x0) / 0.12)):
        xx = x0 + i * 0.12
        ax.plot([xx, xx - 0.07], [y, y - 0.07], color=color, lw=0.8, zorder=3)


# ---------------------------------------------------------------- 3.1 Newton's Laws

def s31_force():
    fig, ax = canvas("diagram")
    ground(ax, 0.5, 4.55, 1.05)
    box(ax, 2.52, 1.5, 1.0, 0.9, "crate", size=11)
    arrow(ax, 0.55, 1.5, 1.4, 0)
    text(ax, 1.25, 1.75, "push  20 N", size=11, color=FORCE, bold=True)
    arrow(ax, 3.05, 1.5, 1.35, 0, color=COMP)
    text(ax, 3.72, 1.75, "pull  15 N", size=11, color=COMP, bold=True)
    text(ax, 2.52, 2.55, "Each arrow: size in newtons, plus a direction", size=10, color=MUTED)
    save(fig, "s31_force.png")


def s31_mass_weight():
    fig, ax = canvas("concept")
    for cx, place, g in ((1.35, "EARTH", 9.8), (3.75, "MOON", 1.6)):
        ground(ax, cx - 0.9, cx + 0.9, 1.7)
        box(ax, cx, 2.05, 0.75, 0.7, "10 kg", size=11)
        L = 1.25 * g / 9.8
        arrow(ax, cx, 1.7, 0, -max(L, 0.2))
        text(ax, cx + 0.55, 1.7 - max(L, 0.2) / 2 - 0.05, f"W = {10 * g:.0f} N", size=11, color=FORCE,
             ha="left", bold=True)
        text(ax, cx, 2.62, place, size=11, color=MUTED, bold=True)
    text(ax, 2.55, 0.18, "Same mass. Different weight.", size=11, color=INK, bold=True)
    save(fig, "s31_mass_weight.png")


def s31_weight_problem():
    fig, ax = canvas("setup")
    for cx, place in ((1.2, "EARTH  g = 9.8 m/s²"), (3.6, "MOON  g = 1.6 m/s²")):
        ground(ax, cx - 0.85, cx + 0.85, 1.25)
        box(ax, cx, 1.6, 0.7, 0.7, "60 kg", size=11)
        arrow(ax, cx, 1.25, 0, -0.8)
        text(ax, cx + 0.42, 0.78, "W = ?", size=12, color=FORCE, ha="left", bold=True)
        text(ax, cx, 2.25, place, size=10, color=MUTED, bold=True)
    save(fig, "s31_weight_problem.png")


def s31_puck():
    fig, ax = canvas("concept06", dark=True)
    ax.plot([0.4, 5.05], [1.15, 1.15], color=LIGHTMUTED, lw=1.4)
    ax.add_patch(Rectangle((2.2, 1.15), 1.05, 0.32, facecolor=INK, edgecolor=LIGHTMUTED, lw=1.5, zorder=4))
    arrow(ax, 2.72, 1.47, 0, 0.95, color=GOLD)
    text(ax, 2.95, 2.0, "N = 1.6 N", size=12, color=GOLD, ha="left", bold=True)
    arrow(ax, 2.72, 1.15, 0, -0.95, color=GOLD)
    text(ax, 2.95, 0.45, "W = 1.6 N", size=12, color=GOLD, ha="left", bold=True)
    text(ax, 0.55, 2.7, "v = constant", size=12, color=WHITE, ha="left", bold=True)
    text(ax, 0.55, 2.4, "Fnet = 0", size=12, color=WHITE, ha="left", bold=True)
    save(fig, "s31_puck.png")


def s31_second_law():
    fig, ax = canvas("concept")
    for y, w, m, a in ((2.1, 0.7, "m", "a"), (0.8, 1.2, "2m", "a ÷ 2")):
        ground(ax, 0.4, 4.7, y - 0.33)
        box(ax, 1.6, y, w, 0.62, m, size=12)
        arrow(ax, 1.6 - w / 2 - 1.05, y, 1.0, 0)
        text(ax, 1.6 - w / 2 - 0.55, y + 0.27, "F", size=12, color=FORCE, bold=True)
        L = 1.4 if a == "a" else 0.7
        arrow(ax, 2.9, y, L, 0, color=COMP, dashed=True)
        text(ax, 2.9 + L / 2, y + 0.25, a, size=12, color=COMP, bold=True)
    text(ax, 2.55, 2.72, "Same push on both. Dashed arrow = acceleration, not a force.", size=9, color=MUTED)
    save(fig, "s31_second_law.png")


def s31_third_law():
    fig, ax = canvas("concept")
    ax.add_patch(Rectangle((0.5, 1.2), 2.9, 0.18, facecolor=PARCH, edgecolor=INK, lw=1.8))
    for lx in (0.65, 3.15):
        ax.add_patch(Rectangle((lx, 0.15), 0.12, 1.05, facecolor=PARCH, edgecolor=INK, lw=1.5))
    box(ax, 1.95, 1.55, 1.1, 0.34, "book", size=10)
    arrow(ax, 1.65, 1.72, 0, 0.85)
    text(ax, 1.55, 2.3, "N on book", size=10, color=FORCE, ha="right", bold=True)
    arrow(ax, 2.25, 1.55, 0, -0.85)
    text(ax, 2.35, 0.95, "W on book", size=10, color=FORCE, ha="left", bold=True)
    arrow(ax, 1.7, 1.38, 0, -0.75, color=COMP)
    text(ax, 1.62, 0.5, "book on table", size=10, color=COMP, ha="center", bold=True)
    text(ax, 4.35, 2.15, "Gold: forces\non the book", size=10, color=FORCE, bold=True)
    text(ax, 4.35, 1.2, "Purple: force\non the table", size=10, color=COMP, bold=True)
    save(fig, "s31_third_law.png")


# ---------------------------------------------------------------- 3.2 Free Body Diagrams

def s32_rules():
    fig, ax = canvas("diagram")
    cx, cy = 2.5, 1.5
    box(ax, cx, cy, 0.9, 0.8, "box", size=11)
    arrow(ax, cx, cy + 0.4, 0, 1.0); text(ax, cx + 0.12, cy + 1.25, "N", size=13, color=FORCE, ha="left", bold=True)
    arrow(ax, cx, cy - 0.4, 0, -1.0); text(ax, cx + 0.12, cy - 1.25, "W", size=13, color=FORCE, ha="left", bold=True)
    arrow(ax, cx + 0.45, cy, 1.4, 0); text(ax, cx + 1.3, cy + 0.2, "F_app", size=13, color=FORCE, bold=True)
    arrow(ax, cx - 0.45, cy, -0.9, 0, color=COMP); text(ax, cx - 1.05, cy + 0.2, "T", size=13, color=COMP, bold=True)
    save(fig, "s32_rules.png")


def s32_draw_problem():
    fig, ax = canvas("setup")
    # book: scene and FBD
    ax.add_patch(Rectangle((0.15, 0.9), 1.15, 0.12, facecolor=PARCH, edgecolor=INK, lw=1.4))
    box(ax, 0.72, 1.12, 0.6, 0.2, "", size=8)
    text(ax, 0.72, 1.45, "book 2.0 kg", size=9, color=MUTED, bold=True)
    bx, by = 1.75, 1.2
    box(ax, bx, by, 0.36, 0.3)
    arrow(ax, bx, by + 0.15, 0, 0.75); text(ax, bx + 0.1, by + 0.75, "N = 19.6 N", size=10, color=FORCE, ha="left", bold=True)
    arrow(ax, bx, by - 0.15, 0, -0.75); text(ax, bx + 0.1, by - 0.75, "W = 19.6 N", size=10, color=FORCE, ha="left", bold=True)
    # lamp: scene and FBD
    ax.plot([2.95, 3.45], [2.4, 2.4], color=INK, lw=2.0)
    ax.plot([3.2, 3.2], [2.4, 1.55], color=INK, lw=1.2)
    ax.add_patch(Polygon([[3.0, 1.3], [3.4, 1.3], [3.3, 1.55], [3.1, 1.55]], facecolor=PARCH, edgecolor=INK, lw=1.4))
    text(ax, 3.2, 1.08, "lamp 1.5 kg", size=9, color=MUTED, bold=True)
    lx, ly = 4.05, 1.2
    ax.add_patch(Circle((lx, ly), 0.07, color=INK, zorder=6))
    arrow(ax, lx, ly, 0, 0.75); text(ax, lx - 0.1, ly + 0.75, "T = 14.7 N", size=10, color=FORCE, ha="right", bold=True)
    arrow(ax, lx, ly, 0, -0.75); text(ax, lx - 0.1, ly - 0.75, "W = 14.7 N", size=10, color=FORCE, ha="right", bold=True)
    save(fig, "s32_draw_problem.png")


def s32_net1d():
    fig, ax = canvas("concept")
    cx, cy = 2.55, 1.75
    ground(ax, 0.3, 4.8, cy - 0.4)
    box(ax, cx, cy, 0.9, 0.8, "crate", size=11)
    arrow(ax, cx + 0.45, cy, 1.5, 0); text(ax, cx + 1.2, cy + 0.2, "30 N", size=12, color=FORCE, bold=True)
    arrow(ax, cx - 0.45, cy, -0.6, 0); text(ax, cx - 0.75, cy + 0.2, "10 N", size=12, color=FORCE, bold=True)
    arrow(ax, 4.55, 2.55, 0.4, 0, color=MUTED, lw=1.5); text(ax, 4.45, 2.55, "+", size=13, color=MUTED, ha="right", bold=True)
    text(ax, 2.55, 0.65, "Fnet = +30 N − 10 N = +20 N  (20 N right)", size=11, color=INK, bold=True)
    save(fig, "s32_net1d.png")


def s32_crate_problem():
    fig, ax = canvas("setup")
    cx, cy = 2.39, 1.27
    box(ax, cx, cy, 0.7, 0.62, "crate", size=10)
    arrow(ax, cx + 0.35, cy, 1.15, 0); text(ax, cx + 0.95, cy + 0.17, "50 N", size=11, color=FORCE, bold=True)
    arrow(ax, cx - 0.35, cy, -0.5, 0); text(ax, cx - 0.62, cy + 0.17, "20 N", size=11, color=FORCE, bold=True)
    arrow(ax, cx, cy + 0.31, 0, 0.85); text(ax, cx + 0.1, cy + 0.85, "40 N", size=11, color=FORCE, ha="left", bold=True)
    arrow(ax, cx, cy - 0.31, 0, -0.85); text(ax, cx + 0.1, cy - 0.85, "40 N", size=11, color=FORCE, ha="left", bold=True)
    text(ax, 0.2, 2.35, "+x right, +y up", size=10, color=MUTED, ha="left", bold=True)
    save(fig, "s32_crate_problem.png")


def angle_arc(ax, x, y, r, a0, a1, label, color=MUTED, lr=None, size=11):
    ax.add_patch(Arc((x, y), 2 * r, 2 * r, theta1=a0, theta2=a1, color=color, lw=1.4, zorder=5))
    am = math.radians((a0 + a1) / 2)
    lr = lr or r + 0.2
    text(ax, x + lr * math.cos(am), y + lr * math.sin(am), label, size=size, color=color, bold=True)


def s32_resultant():
    fig, ax = canvas("data")
    ox, oy, s = 0.55, 0.35, 0.065   # 40 N -> 2.6 in
    fx, fy = 40 * s, 30 * s
    arrow(ax, ox, oy, fx, 0, color=COMP); text(ax, ox + fx / 2, oy - 0.15, "Fx = 40 N", size=11, color=COMP, bold=True)
    arrow(ax, ox + fx, oy, 0, fy, color=COMP); text(ax, ox + fx + 0.12, oy + fy / 2, "Fy = 30 N", size=11, color=COMP, ha="left", bold=True)
    arrow(ax, ox, oy, fx, fy)
    text(ax, ox + fx / 2 - 0.35, oy + fy / 2 + 0.25, "F = 50 N", size=12, color=FORCE, bold=True)
    angle_arc(ax, ox, oy, 0.5, 0, 36.87, "37°", lr=0.75)
    save(fig, "s32_resultant.png")


def s32_components():
    fig, ax = canvas("diagram")
    ox, oy, s = 1.35, 0.45, 0.031   # 100 N -> 3.4 in
    F, th = 100, math.radians(30)
    fx, fy = F * math.cos(th) * s, F * math.sin(th) * s
    arrow(ax, ox, oy, fx, 0, color=COMP); text(ax, ox + fx / 2, oy - 0.17, "Fx = 87 N", size=12, color=COMP, bold=True)
    ax.plot([ox + fx, ox + fx], [oy, oy + fy], color=COMP, lw=1.6, ls="--")
    arrow(ax, ox, oy, 0, fy, color=COMP); text(ax, ox - 0.12, oy + fy / 2, "Fy = 50 N", size=12, color=COMP, ha="right", bold=True)
    ax.plot([ox, ox + fx], [oy + fy, oy + fy], color=COMP, lw=1.6, ls="--")
    arrow(ax, ox, oy, fx, fy)
    text(ax, ox + fx / 2 - 0.1, oy + fy / 2 + 0.3, "F = 100 N", size=13, color=FORCE, bold=True)
    angle_arc(ax, ox, oy, 0.6, 0, 30, "30°", lr=0.85)
    save(fig, "s32_components.png")


def top_view_problem(name, forces, label):
    """forces: list of (magnitude, angle_deg from +x, colour). Top view, so no weight in the plane."""
    fig, ax = canvas("setup")
    cx, cy = 2.39, 1.2
    s = 0.95 / max(f[0] for f in forces)
    box(ax, cx, cy, 0.5, 0.5, label, size=9)
    ax.plot([cx - 1.9, cx + 1.9], [cy, cy], color=MUTED, lw=0.8, ls=":")
    for mag, ang, col in forces:
        a = math.radians(ang)
        dx, dy = mag * s * math.cos(a), mag * s * math.sin(a)
        sx, sy = cx + 0.25 * math.cos(a) / max(abs(math.cos(a)), abs(math.sin(a)), 1e-9) * min(1, 1), cy
        ex0, ey0 = cx + 0.36 * math.cos(a), cy + 0.36 * math.sin(a)
        arrow(ax, ex0, ey0, dx, dy, color=col)
        lx, ly = ex0 + dx * 1.0 + 0.05 * math.cos(a), ey0 + dy + 0.12
        text(ax, lx, ly, f"{mag} N", size=11, color=col, bold=True)
        if ang % 180:
            ref = 0 if math.cos(a) > 0 else 180
            a0, a1 = sorted((ref, ang))
            angle_arc(ax, ex0, ey0, 0.38, a0, a1, f"{abs(ang - ref):.0f}°", size=10, lr=0.6)
    text(ax, 0.15, 0.2, "TOP VIEW  ·  +x right, +y up the page", size=9, color=MUTED, ha="left", bold=True)
    save(fig, name)


# ---------------------------------------------------------------- inclines

def incline(ax, x0, y0, base, deg, color=INK, fill=PARCH):
    th = math.radians(deg)
    h = base * math.tan(th)
    ax.add_patch(Polygon([[x0, y0], [x0 + base, y0], [x0, y0 + h]], facecolor=fill, edgecolor=color, lw=1.8, zorder=2))
    angle_arc(ax, x0 + base, y0, 0.45, 180 - deg, 180, f"{deg}°", lr=0.7)
    return th, h


def block_on_incline(ax, x0, y0, base, deg, frac=0.5, bw=0.6, bh=0.42, label=""):
    """Returns the block centre and the slope unit vectors (down-slope u, outward normal n)."""
    th = math.radians(deg)
    h = base * math.tan(th)
    px, py = x0 + base * frac, y0 + h * (1 - frac)
    u = (math.cos(th), -math.sin(th))          # down the slope
    n = (math.sin(th), math.cos(th))           # out of the surface
    cx, cy = px + n[0] * bh / 2, py + n[1] * bh / 2
    corners = [(-bw / 2, -bh / 2), (bw / 2, -bh / 2), (bw / 2, bh / 2), (-bw / 2, bh / 2)]
    pts = [[cx + a * u[0] + b * n[0], cy + a * u[1] + b * n[1]] for a, b in corners]
    ax.add_patch(Polygon(pts, facecolor=WHITE, edgecolor=INK, lw=1.8, zorder=4))
    if label:
        text(ax, cx, cy, label, size=9, color=INK, bold=True, rot=-deg)
    return (cx, cy), u, n


def s33_components():
    fig, ax = canvas("diagram")
    incline(ax, 0.35, 0.3, 4.3, 30)
    (cx, cy), u, n = block_on_incline(ax, 0.35, 0.3, 4.3, 30, frac=0.45)
    L = 1.3
    arrow(ax, cx, cy, 0, -L); text(ax, cx - 0.12, cy - L + 0.05, "W = mg", size=11, color=FORCE, ha="right", bold=True)
    s, c = math.sin(math.radians(30)), math.cos(math.radians(30))
    arrow(ax, cx, cy, u[0] * L * s, u[1] * L * s, color=COMP)
    text(ax, cx + u[0] * L * s + 0.1, cy + u[1] * L * s + 0.2, "mg sin 30°", size=11, color=COMP, ha="left", bold=True)
    arrow(ax, cx, cy, -n[0] * L * c, -n[1] * L * c, color=COMP)
    text(ax, cx - n[0] * L * c - 0.55, cy - n[1] * L * c + 0.05, "mg cos 30°", size=11, color=COMP, ha="right", bold=True)
    arrow(ax, cx, cy, n[0] * L * c, n[1] * L * c)
    text(ax, cx + n[0] * L * c + 0.1, cy + n[1] * L * c + 0.1, "N", size=12, color=FORCE, ha="left", bold=True)
    save(fig, "s33_components.png")


def s33_angle_extremes():
    fig, ax = canvas("concept")
    for x0, deg in ((0.2, 15), (2.75, 60)):
        base = 2.1 if deg == 15 else 1.15
        incline(ax, x0, 0.4, base, deg)
        (cx, cy), u, n = block_on_incline(ax, x0, 0.4, base, deg, frac=0.55 if deg == 15 else 0.5, bw=0.45, bh=0.32)
        c = math.cos(math.radians(deg))
        arrow(ax, cx, cy, n[0] * 1.1 * c, n[1] * 1.1 * c)
        text(ax, cx + n[0] * 1.1 * c + 0.05, cy + n[1] * 1.1 * c + 0.15, f"N = {c:.2f} mg", size=10, color=FORCE, bold=True)
    save(fig, "s33_angle_extremes.png")


def s33_block_problem(name, deg, label, push=None):
    fig, ax = canvas("setup")
    incline(ax, 0.4, 0.3, 3.9, deg)
    (cx, cy), u, n = block_on_incline(ax, 0.4, 0.3, 3.9, deg, frac=0.5, bw=0.62, bh=0.4, label=label)
    if push:
        arrow(ax, cx - u[0] * 1.15, cy - u[1] * 1.15 - 0.0, -u[0] * 0.0001, 0, color=WHITE, lw=0.1)
        sx, sy = cx - u[0] * 0.31, cy - u[1] * 0.31
        arrow(ax, sx + u[0] * 0.0 + u[0] * -0.0, sy, -u[0] * 0.9, -u[1] * 0.9)
        text(ax, sx - u[0] * 0.9 - 0.1, sy - u[1] * 0.9 + 0.15, push, size=11, color=FORCE, ha="right", bold=True)
    text(ax, 3.2, 2.2, "frictionless", size=10, color=MUTED, bold=True)
    save(fig, name)


# ---------------------------------------------------------------- 3.4 / 3.5

def s34_cart_example(name, m, forces, slot="data"):
    fig, ax = canvas(slot)
    w, h = SLOT[slot]
    cx, cy = w / 2, 1.15
    ground(ax, 0.25, w - 0.25, cy - 0.45)
    ax.add_patch(Rectangle((cx - 0.55, cy - 0.3), 1.1, 0.6, facecolor=PARCH, edgecolor=INK, lw=1.8, zorder=4))
    for wx in (cx - 0.33, cx + 0.33):
        ax.add_patch(Circle((wx, cy - 0.36), 0.09, color=INK, zorder=5))
    text(ax, cx, cy, m, size=11, color=INK, bold=True)
    for mag, sign, col in forces:
        L = 0.04 * mag if mag < 40 else 0.022 * mag
        x0 = cx + sign * 0.55
        arrow(ax, x0, cy, sign * L, 0, color=col)
        text(ax, x0 + sign * L / 2, cy + 0.22, f"{mag} N", size=11, color=col, bold=True)
    save(fig, name)


def car_problem():
    fig, ax = canvas("setup")
    cx, cy = 2.39, 1.15
    ground(ax, 0.2, 4.6, cy - 0.42)
    ax.add_patch(Polygon([[cx - 0.75, cy - 0.3], [cx + 0.75, cy - 0.3], [cx + 0.75, cy + 0.02], [cx + 0.35, cy + 0.05],
                          [cx + 0.2, cy + 0.32], [cx - 0.45, cy + 0.32], [cx - 0.6, cy + 0.05], [cx - 0.75, cy + 0.02]],
                         facecolor=PARCH, edgecolor=INK, lw=1.8, zorder=4))
    for wx in (cx - 0.45, cx + 0.45):
        ax.add_patch(Circle((wx, cy - 0.3), 0.12, color=INK, zorder=5))
    text(ax, cx, cy - 0.1, "1500 kg", size=10, color=INK, bold=True)
    arrow(ax, cx + 0.78, cy - 0.1, 1.2, 0); text(ax, cx + 1.4, cy + 0.12, "4500 N", size=11, color=FORCE, bold=True)
    arrow(ax, cx - 0.78, cy - 0.1, -0.5, 0); text(ax, cx - 1.05, cy + 0.12, "1200 N", size=11, color=FORCE, bold=True)
    text(ax, 0.2, 2.3, "engine force forward, drag backward", size=9, color=MUTED, ha="left", bold=True)
    save(fig, "s34_car_problem.png")


def graph(name, slot, points=None, generic=False):
    w, h = SLOT[slot]
    fig = plt.figure(figsize=(w, h), dpi=300)
    fig.patch.set_facecolor(WHITE)
    ax = fig.add_axes([0.17, 0.2, 0.78, 0.74])
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(INK); ax.spines[sp].set_linewidth(1.4)
    ax.tick_params(colors=INK, labelsize=10)
    ax.set_xlabel("acceleration a (m/s²)", fontsize=11, color=INK, fontweight="bold")
    ax.set_ylabel("net force Fnet (N)", fontsize=11, color=INK, fontweight="bold")
    if generic:
        ax.plot([0, 4], [0, 8], color=FORCE, lw=2.4)
        ax.plot([1, 3], [2, 2], color=COMP, lw=1.6, ls="--"); ax.plot([3, 3], [2, 6], color=COMP, lw=1.6, ls="--")
        ax.text(2, 1.4, "run = Δa", color=COMP, ha="center", fontsize=11, fontweight="bold")
        ax.text(3.1, 4, "rise = ΔF", color=COMP, ha="left", fontsize=11, fontweight="bold")
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlim(0, 4.2); ax.set_ylim(0, 8.6)
    else:
        xs = [p[0] for p in points]; ys = [p[1] for p in points]
        ax.plot([0, 4], [0, 4 * ys[-1] / xs[-1]], color=FORCE, lw=2.2)
        ax.scatter(xs, ys, color=INK, s=22, zorder=5)
        ax.set_xlim(0, 4); ax.set_ylim(0, 10)
        ax.set_xticks([0, 0.8, 1.6, 2.4, 3.2, 4.0]); ax.set_yticks([0, 2, 4, 6, 8, 10])
        ax.grid(True, color=T["ground"]["ruleHairline"]["hex"], lw=0.7)
    save(fig, name)


def sled_angle_problem():
    fig, ax = canvas("setup")
    cx, cy = 1.7, 1.0
    ax.plot([0.2, 4.6], [cy - 0.25, cy - 0.25], color=MUTED, lw=1.6)
    text(ax, 0.3, cy - 0.45, "frictionless ice", size=9, color=MUTED, ha="left", bold=True)
    box(ax, cx, cy, 0.9, 0.5, "20 kg", size=10)
    a = math.radians(35)
    sx, sy = cx + 0.45, cy + 0.05
    arrow(ax, sx, sy, 1.6 * math.cos(a), 1.6 * math.sin(a))
    text(ax, sx + 1.6 * math.cos(a) + 0.1, sy + 1.6 * math.sin(a), "60 N", size=12, color=FORCE, ha="left", bold=True)
    ax.plot([sx, sx + 1.3], [sy, sy], color=MUTED, lw=1, ls=":")
    angle_arc(ax, sx, sy, 0.5, 0, 35, "35°", lr=0.72)
    save(fig, "s35_sled_problem.png")


def elevator(name, slot, a_label=None, mass="70 kg", fbd=True):
    fig, ax = canvas(slot)
    w, h = SLOT[slot]
    ex, ey, ew, eh = 0.5, 0.25, 1.6, h - 0.5
    ax.add_patch(Rectangle((ex, ey), ew, eh, facecolor=WHITE, edgecolor=INK, lw=2.0))
    ax.plot([ex + ew / 2, ex + ew / 2], [ey + eh, h], color=INK, lw=1.4)
    ax.add_patch(Rectangle((ex + 0.45, ey + 0.05), 0.7, 0.12, facecolor=PARCH, edgecolor=INK, lw=1.2))
    pcx = ex + 0.8
    ax.add_patch(Circle((pcx, ey + 1.45), 0.13, facecolor=PARCH, edgecolor=INK, lw=1.4))
    ax.plot([pcx, pcx], [ey + 1.32, ey + 0.85], color=INK, lw=1.8)
    ax.plot([pcx, pcx - 0.15], [ey + 0.85, ey + 0.2], color=INK, lw=1.8)
    ax.plot([pcx, pcx + 0.15], [ey + 0.85, ey + 0.2], color=INK, lw=1.8)
    ax.plot([pcx - 0.25, pcx + 0.25], [ey + 1.15, ey + 1.15], color=INK, lw=1.8)
    text(ax, pcx, ey + eh - 0.2, mass, size=10, color=INK, bold=True)
    if a_label:
        up = "up" in a_label
        arrow(ax, ex + ew + 0.25, h / 2 - (0.4 if up else -0.4), 0, 0.8 if up else -0.8, color=COMP, dashed=True)
        text(ax, ex + ew + 0.38, h / 2, a_label.replace(" up", "\nup").replace(" down", "\ndown"),
             size=11, color=COMP, ha="left", bold=True)
    if fbd:
        fx, fy = w - 0.75, h / 2
        box(ax, fx, fy, 0.4, 0.4)
        arrow(ax, fx, fy + 0.2, 0, 0.8); text(ax, fx + 0.12, fy + 0.85, "N", size=12, color=FORCE, ha="left", bold=True)
        arrow(ax, fx, fy - 0.2, 0, -0.8); text(ax, fx + 0.12, fy - 0.85, "W = mg", size=11, color=FORCE, ha="left", bold=True)
    save(fig, name)


# ---------------------------------------------------------------- 3.6 friction

def friction_box(name, slot, m, push_label, f_label, angle=None, surface="", show_nw=False):
    fig, ax = canvas(slot)
    w, h = SLOT[slot]
    cx, cy = w / 2 - (0.25 if angle else 0), 0.95 if h > 2 else 0.75
    bw = 0.9 if h > 2 else 0.7
    bh = 0.6 if h > 2 else 0.46
    ground(ax, 0.15, w - 0.15, cy - bh / 2)
    box(ax, cx, cy, bw, bh, m, size=10 if h > 2 else 9)
    sz = 11 if h > 2 else 9
    if angle:
        a = math.radians(angle)
        sx, sy = cx + bw / 2, cy + bh / 4
        arrow(ax, sx, sy, 1.3 * math.cos(a), 1.3 * math.sin(a))
        text(ax, sx + 1.3 * math.cos(a) + 0.08, sy + 1.3 * math.sin(a), push_label, size=sz, color=FORCE, ha="left", bold=True)
        ax.plot([sx, sx + 0.9], [sy, sy], color=MUTED, lw=1, ls=":")
        angle_arc(ax, sx, sy, 0.45, 0, angle, f"{angle}°", lr=0.65, size=10)
    else:
        L = 0.9 if h > 2 else 0.6
        arrow(ax, cx - bw / 2 - L, cy + bh / 6, L, 0)
        text(ax, cx - bw / 2 - L / 2, cy + bh / 6 + 0.2, push_label, size=sz, color=FORCE, bold=True)
    if f_label:
        L = 0.7 if h > 2 else 0.55
        arrow(ax, cx - bw / 2, cy - bh / 2 + 0.03, -L, 0, color=COMP)
        fx = cx - bw / 2 - L / 2
        text(ax, fx, cy - bh / 2 - 0.18, f_label, size=sz, color=COMP, bold=True)
    if surface:
        text(ax, 0.2, h - 0.2, surface, size=9 if h > 2 else 8, color=MUTED, ha="left", va="top", bold=True)
    save(fig, name)


def s36_incline_friction(name, slot, deg, label="", detail=True):
    fig, ax = canvas(slot)
    w, h = SLOT[slot]
    base = 3.4 if slot == "setup" else 3.6
    x0 = 0.45 if slot == "setup" else 0.5
    incline(ax, x0, 0.3, base, deg)
    (cx, cy), u, n = block_on_incline(ax, x0, 0.3, base, deg, frac=0.45, bw=0.6, bh=0.4, label=label)
    if detail:
        L = 1.1
        s, c = math.sin(math.radians(deg)), math.cos(math.radians(deg))
        arrow(ax, cx, cy, 0, -L); text(ax, cx - 0.12, cy - L + 0.05, "W", size=12, color=FORCE, ha="right", bold=True)
        arrow(ax, cx, cy, n[0] * L * c, n[1] * L * c); text(ax, cx + n[0] * L * c + 0.08, cy + n[1] * L * c + 0.1, "N", size=12, color=FORCE, ha="left", bold=True)
        arrow(ax, cx, cy, -u[0] * 0.85, -u[1] * 0.85, color=COMP)
        text(ax, cx - u[0] * 0.85 - 0.05, cy - u[1] * 0.85 + 0.2, "f", size=12, color=COMP, ha="right", bold=True)
    save(fig, name)


# ---------------------------------------------------------------- 3.7 pulleys

def pulley_wheel(ax, x, y, r=0.2):
    ax.add_patch(Circle((x, y), r, facecolor=PARCH, edgecolor=INK, lw=1.8, zorder=4))
    ax.add_patch(Circle((x, y), 0.04, color=INK, zorder=5))


def atwood(name, slot, m1, m2, show_T=False):
    fig, ax = canvas(slot)
    w, h = SLOT[slot]
    px, py, r = w / 2, h - 0.35, 0.28
    ax.plot([px - 0.5, px + 0.5], [h - 0.05, h - 0.05], color=INK, lw=2)
    ax.plot([px, px], [h - 0.05, py], color=INK, lw=1.4)
    pulley_wheel(ax, px, py, r)
    ly, ry = 0.9, 1.35
    ax.plot([px - r, px - r], [py, ly + 0.25], color=INK, lw=1.4)
    ax.plot([px + r, px + r], [py, ry + 0.25], color=INK, lw=1.4)
    box(ax, px - r, ly, 0.55, 0.5, m1, size=10)
    box(ax, px + r, ry, 0.5, 0.5, m2, size=10)
    if show_T:
        text(ax, px - r - 0.12, py - 0.55, "T", size=12, color=FORCE, ha="right", bold=True)
        text(ax, px + r + 0.12, py - 0.55, "T", size=12, color=FORCE, ha="left", bold=True)
    save(fig, name)


def table_pulley(name, m_block, m_hang, mu=None):
    fig, ax = canvas("setup")
    ty = 1.6
    ax.add_patch(Rectangle((0.2, ty - 0.12), 3.2, 0.12, facecolor=PARCH, edgecolor=INK, lw=1.6))
    ax.add_patch(Rectangle((0.35, 0.15), 0.12, ty - 0.27, facecolor=PARCH, edgecolor=INK, lw=1.2))
    pulley_wheel(ax, 3.55, ty + 0.15, 0.17)
    box(ax, 1.6, ty + 0.25, 0.85, 0.5, m_block, size=10)
    ax.plot([2.02, 3.55], [ty + 0.32, ty + 0.32], color=INK, lw=1.4)
    ax.plot([3.72, 3.72], [ty + 0.15, 0.85], color=INK, lw=1.4)
    box(ax, 3.72, 0.6, 0.55, 0.5, m_hang, size=10)
    text(ax, 1.6, ty - 0.35, f"μk = {mu}" if mu else "frictionless table", size=10, color=MUTED, bold=True)
    save(fig, name)


def incline_pulley(name):
    fig, ax = canvas("setup")
    deg, x0, y0, base = 30, 0.3, 0.25, 3.3
    th, hgt = math.radians(deg), 3.3 * math.tan(math.radians(30))
    ax.add_patch(Polygon([[x0, y0], [x0 + base, y0], [x0 + base, y0 + hgt]], facecolor=PARCH, edgecolor=INK, lw=1.8, zorder=2))
    angle_arc(ax, x0, y0, 0.5, 0, deg, "30°", lr=0.75)
    # block on the slope (rising to the right)
    fr = 0.5
    px, py = x0 + base * fr, y0 + hgt * fr
    u = (math.cos(th), math.sin(th)); n = (-math.sin(th), math.cos(th))
    bw, bh = 0.65, 0.42
    cx, cy = px + n[0] * bh / 2, py + n[1] * bh / 2
    pts = [[cx + a * u[0] + b * n[0], cy + a * u[1] + b * n[1]] for a, b in
           ((-bw / 2, -bh / 2), (bw / 2, -bh / 2), (bw / 2, bh / 2), (-bw / 2, bh / 2))]
    ax.add_patch(Polygon(pts, facecolor=WHITE, edgecolor=INK, lw=1.8, zorder=4))
    text(ax, cx, cy, "6.0 kg", size=9, color=INK, bold=True, rot=deg)
    tx, ty = x0 + base + 0.12, y0 + hgt + 0.12
    pulley_wheel(ax, tx, ty, 0.15)
    ax.plot([cx + u[0] * bw / 2, tx - 0.1], [cy + u[1] * bw / 2, ty + 0.1], color=INK, lw=1.4)
    ax.plot([tx + 0.15, tx + 0.15], [ty, 0.95], color=INK, lw=1.4)
    ax.plot([tx + 0.15, tx + 0.38], [0.95, 0.95], color=WHITE, lw=0)
    box(ax, tx + 0.38, 0.5, 0.6, 0.45, "5.0 kg", size=9)
    ax.plot([tx + 0.15, tx + 0.38], [0.75, 0.725], color=WHITE, lw=0)
    text(ax, 1.0, 2.25, "frictionless incline", size=10, color=MUTED, bold=True)
    save(fig, name)


def main():
    s31_force(); s31_mass_weight(); s31_weight_problem(); s31_puck(); s31_second_law(); s31_third_law()
    s32_rules(); s32_draw_problem(); s32_net1d(); s32_crate_problem(); s32_resultant(); s32_components()
    top_view_problem("s32_two_force_problem.png", [(80, 40, FORCE), (30, 180, FORCE)], "crate")
    top_view_problem("s32_two_angled_problem.png", [(500, 30, FORCE), (400, 135, FORCE)], "barge")
    s33_components(); s33_angle_extremes()
    s33_block_problem("s33_block_problem.png", 30, "5.0 kg")
    s33_block_problem("s33_push_problem.png", 25, "12 kg", push="30 N")
    s34_cart_example("s34_cart_example.png", "4.0 kg", [(12, 1, FORCE)])
    car_problem()
    graph("s34_graph_concept.png", "diagram", generic=True)
    graph("s34_graph_problem.png", "setup", points=[(0.8, 2.0), (1.6, 4.0), (2.4, 6.0), (3.2, 8.0)])
    s34_cart_example("s35_chain.png", "10 kg", [(50, 1, FORCE), (20, -1, FORCE)], slot="band")
    sled_angle_problem()
    s33_block_problem("s35_incline_problem.png", 20, "8.0 kg")
    elevator("s35_elevator_concept.png", "concept", a_label=None)
    elevator("s35_elevator_up.png", "setup", a_label="a = 2.0 m/s² up")
    elevator("s35_elevator_down.png", "setup", a_label="a = 2.0 m/s² down")
    friction_box("s36_friction_aside.png", "aside", "", "push", "f")
    friction_box("s36_constant_v.png", "setup", "40 kg", "120 N", "f", surface="constant velocity")
    friction_box("s36_static.png", "setup", "25 kg", "90 N", "", surface="μs = 0.40   μk = 0.30")
    friction_box("s36_angle_pull.png", "setup", "30 kg", "150 N", "f", angle=30, surface="μk = 0.25")
    s36_incline_friction("s36_incline_fbd.png", "diagram", 30)
    s36_incline_friction("s36_incline_problem.png", "setup", 35, label="10 kg", detail=False)
    atwood("s37_ideal.png", "concept", "m1", "m2", show_T=True)
    atwood("s37_atwood_problem.png", "setup", "5.0 kg", "3.0 kg")
    table_pulley("s37_table_problem.png", "4.0 kg", "2.0 kg")
    table_pulley("s37_table_friction.png", "4.0 kg", "2.0 kg", mu="0.20")
    incline_pulley("s37_incline_pulley.png")
    print("wrote", len([f for f in os.listdir(OUT) if f.endswith(".png")]), "figures to", OUT)


if __name__ == "__main__":
    main()
