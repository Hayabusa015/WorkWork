#!/usr/bin/env python3
"""Draw the hand-built figures for CHEM U02 S2.1 The Bohr Model.

Hand-built, not generated. A Bohr diagram and an energy-level diagram carry counts and
spacing a student reads as science, and a generated one gets the electron count or the
spacing wrong in a way nobody catches at a glance.

NO energy value is printed anywhere (Matt's instruction, 2026-10-04: no scientific notation
and no numeric energy calculations in S2.1). The spacing of the to-scale figures is still
computed from the 1/n^2 shape (relative energy -1/n^2), so levels crowd together as n grows,
but the numbers never reach the page. Assertions check level order, monotonic spacing, the
drop ranking, and that no printed string carries an exponent, a times sign, a unit or a
digit run that is not a level label.

Colours come from brand/tokens.json. Type comes from the shipped Archivo files, the same
ones the deck embeds. Text is asphalt (measured against its ground); the course accent is
used for lines, arrows and the electron, never for small type on parchment.

Each figure is drawn at the pixel density of the slot it will sit in, so a 16 pt label on
the slide is 16 pt in the figure. The slot sizes are the ones declared in
templates/slide/build.js (layout 08 "diagram" 5.05 x 3.0 in; layout 10 "data" 4.23 x 2.48).

    python3 scripts/build_diagram_u02_s02.1_bohr_figures.py
"""
import json, math, os, sys
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(REPO, "templates", "slide", "assets")
SCALE = 3                       # supersample; stays crisp on a projector

def rel_energy(n):
    """Relative energy of level n: -1/n^2 (n = 1 is -1, n = infinity is 0). Used only for
    POSITIONS. It is never printed."""
    return -1.0 / (n * n)


PRINTED = []                    # every string drawn; checked by assert_text() in main()


T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
PARCH = T["ground"]["parchment"]["hex"]
WHITE = T["ground"]["white"]["hex"]
INK = T["ground"]["asphalt"]["hex"]
GRAPH = T["ground"]["graphite"]["hex"]
ACC = T["courses"]["chemistry"]["primaryDeep"]["hex"]


def font(name, px):
    return ImageFont.truetype(os.path.join(REPO, "brand", "fonts", name), int(round(px * SCALE)))


class Fig:
    def __init__(self, w_px, slot_w_in, slot_h_in, bg):
        self.ppi = w_px / slot_w_in
        self.W = w_px
        self.H = int(round(slot_h_in * self.ppi))
        self.im = Image.new("RGB", (self.W * SCALE, self.H * SCALE), bg)
        self.d = ImageDraw.Draw(self.im)

    def pt(self, p):
        return p / 72.0 * self.ppi

    # ---- primitives (design px in, supersampled out) ----
    def line(self, pts, fill=INK, w=3, dash=None):
        pts = [(x * SCALE, y * SCALE) for x, y in pts]
        if dash is None:
            self.d.line(pts, fill=fill, width=int(w * SCALE), joint="curve")
            return
        (x0, y0), (x1, y1) = pts[0], pts[-1]
        L = math.hypot(x1 - x0, y1 - y0)
        on, off = dash[0] * SCALE, dash[1] * SCALE
        t = 0
        while t < L:
            t2 = min(t + on, L)
            self.d.line([(x0 + (x1 - x0) * t / L, y0 + (y1 - y0) * t / L),
                         (x0 + (x1 - x0) * t2 / L, y0 + (y1 - y0) * t2 / L)],
                        fill=fill, width=int(w * SCALE))
            t += on + off

    def circle(self, cx, cy, r, fill=None, outline=None, w=3):
        self.d.ellipse([(cx - r) * SCALE, (cy - r) * SCALE, (cx + r) * SCALE, (cy + r) * SCALE],
                       fill=fill, outline=outline, width=int(w * SCALE))

    def arrow(self, x0, y0, x1, y1, fill=ACC, w=6, head=26):
        ang = math.atan2(y1 - y0, x1 - x0)
        bx, by = x1 - head * math.cos(ang), y1 - head * math.sin(ang)
        self.line([(x0, y0), (bx, by)], fill=fill, w=w)
        hw = head * 0.55
        px, py = -math.sin(ang), math.cos(ang)
        self.d.polygon([(x1 * SCALE, y1 * SCALE),
                        ((bx + px * hw) * SCALE, (by + py * hw) * SCALE),
                        ((bx - px * hw) * SCALE, (by - py * hw) * SCALE)], fill=fill)

    def wave(self, x0, x1, y, amp=13, period=34, fill=ACC, w=5):
        pts, x = [], x0
        while x <= x1:
            pts.append((x, y + amp * math.sin((x - x0) / period * 2 * math.pi)))
            x += 2
        self.line(pts, fill=fill, w=w)

    # ---- text. parts = [(text, mode)], mode "n" normal, "sup", "sub" ----
    def _parts_w(self, parts, size, fname):
        tot = 0
        for txt, mode in parts:
            s = size * (0.62 if mode != "n" else 1)
            tot += font(fname, s).getlength(txt) / SCALE
        return tot

    def rich(self, x, y, parts, size, fname="Archivo-SemiBold.ttf", fill=INK, anchor="l"):
        """y is the baseline. anchor l / m / r on x."""
        if isinstance(parts, str):
            parts = [(parts, "n")]
        PRINTED.append("".join(t for t, _ in parts))
        w = self._parts_w(parts, size, fname)
        x0 = x if anchor == "l" else (x - w / 2 if anchor == "m" else x - w)
        for txt, mode in parts:
            s = size * (0.62 if mode != "n" else 1)
            yy = y - (size * 0.40 if mode == "sup" else (-size * 0.16 if mode == "sub" else 0))
            f = font(fname, s)
            self.d.text((x0 * SCALE, yy * SCALE), txt, font=f, fill=fill, anchor="ls")
            x0 += f.getlength(txt) / SCALE
        return w

    def halo_box(self, x0, y0, x1, y1, bg):
        self.d.rectangle([x0 * SCALE, y0 * SCALE, x1 * SCALE, y1 * SCALE], fill=bg)

    def save(self, name):
        out = self.im.resize((self.W, self.H), Image.LANCZOS) if False else self.im
        path = os.path.join(ASSETS, name)
        os.makedirs(ASSETS, exist_ok=True)
        out.save(path)
        print(f"wrote {os.path.relpath(path, REPO)}  {out.width}x{out.height}")





# ---------------------------------------------------------------------------------------
def level_ys(ns, y_bottom, y_top_n, n_top):
    """y position (px) of each level in ns, to scale: relative energy -1/n^2, with n = 1 at
    y_bottom and level n_top at y_top_n. Returns dict n -> y."""
    k = (y_bottom - y_top_n) / (rel_energy(n_top) - rel_energy(1))
    return {n: y_bottom - (rel_energy(n) - rel_energy(1)) * k for n in ns}, k


def assert_levels(ys):
    """Level order and spacing. Higher n sits higher on the page (smaller y), and each gap
    is smaller than the one below it."""
    ns = sorted(ys)
    for a, b in zip(ns, ns[1:]):
        assert ys[b] < ys[a], f"level {b} not above level {a}"
    gaps = [ys[a] - ys[b] for a, b in zip(ns, ns[1:])]
    for g1, g2 in zip(gaps, gaps[1:]):
        assert g2 < g1, f"spacing not shrinking: {gaps}"


def fig_bohr_hydrogen():
    f = Fig(1010, 5.05, 3.0, PARCH)
    lab = f.pt(16) * 1.0
    cx, cy, a = 300, 300, 31                     # orbit radius = n^2 * a, as in Bohr's model
    for n in (1, 2, 3):
        f.circle(cx, cy, n * n * a, outline=GRAPH, w=3)
    f.circle(cx, cy, 8, fill=INK)                # nucleus: 1 proton
    ang = math.radians(215)                      # the electron, on the n = 1 orbit
    ex, ey = cx + a * math.cos(ang), cy - a * math.sin(ang)
    f.circle(ex, ey, 12, fill=ACC, outline=INK, w=3)

    col = 670
    rows = [("n = 3", 3, 38, 80), ("n = 2", 2, 48, 175), ("n = 1", 1, 30, 270)]
    for txt, n, deg, y in rows:
        r = n * n * a
        px, py = cx + r * math.cos(math.radians(deg)), cy - r * math.sin(math.radians(deg))
        f.line([(px, py), (col - 14, y)], fill=GRAPH, w=2)
        f.rich(col, y + lab * 0.35, txt, lab)
    # nucleus and electron: labelled from the figure to the lower right
    f.line([(cx + 9, cy + 2), (col - 14, 365)], fill=GRAPH, w=2)
    f.rich(col, 365 + lab * 0.35, "1 proton", lab)
    f.line([(ex + 12, ey + 4), (col - 14, 460)], fill=GRAPH, w=2)
    f.rich(col, 460 + lab * 0.35, "1 electron", lab)
    f.save("chem_u02_s2.1_bohr_hydrogen.png")


def _more_energy_axis(f, lab, x, y_bot, y_top, label_y=52):
    f.rich(x, label_y, "more energy", lab, fill=GRAPH)
    f.arrow(x, y_bot, x, y_top, fill=GRAPH, w=3, head=16)


def fig_level_numbers():
    """Slide 8. Levels n = 1..4, to scale (relative -1/n^2), labelled by n only. Between n = 1
    and n = 2 a dashed line says there is no level there (whole numbers only)."""
    f = Fig(1010, 5.05, 3.0, PARCH)
    lab = f.pt(16)
    ys, _ = level_ys((1, 2, 3, 4), 540, 100, 4)
    assert_levels(ys)
    x0, x1, labx = 110, 480, 600
    _more_energy_axis(f, lab, 50, 548, 84, label_y=52)
    label_rows = {4: 74, 3: 130, 2: ys[2], 1: ys[1]}      # spread labels where levels crowd
    for n in (4, 3, 2, 1):
        y = ys[n]
        f.line([(x0, y), (x1, y)], fill=ACC if n == 1 else INK, w=7 if n == 1 else 4)
        ry = label_rows[n]
        f.line([(x1 + 6, y), (labx - 14, ry)], fill=GRAPH, w=2)
        f.rich(labx, ry + lab * 0.35, f"n = {n}", lab)
    ymid = (ys[1] + ys[2]) / 2
    f.line([(x0, ymid), (x1, ymid)], fill=GRAPH, w=3, dash=(8, 14))
    f.rich(labx, ymid + lab * 0.35, "no level here", lab, fill=GRAPH)
    f.save("chem_u02_s2.1_level_numbers.png")


def fig_levels():
    """Slide 9. n = 1..6 and the top (n = infinity), to scale, no values printed."""
    f = Fig(1010, 5.05, 3.0, PARCH)
    lab = f.pt(16)
    top, bot = 100, 548                           # top of the diagram (n = infinity) and n = 1
    ys = {n: bot - (rel_energy(n) - rel_energy(1)) * (bot - top) for n in range(1, 7)}
    y_inf = top
    assert_levels(ys)
    assert all(y > y_inf for y in ys.values())
    _more_energy_axis(f, lab, 40, bot + 4, 78, label_y=52)
    x0, x1 = 90, 480
    labx_n = 600
    pitch = 52
    rows = [("∞", None)] + [(str(n), n) for n in (6, 5, 4, 3, 2)]
    for i, (nn, n) in enumerate(rows):
        y = y_inf if n is None else ys[n]
        f.line([(x0, y), (x1, y)], fill=GRAPH if n is None else INK, w=3,
               dash=(14, 10) if n is None else None)
        ry = top + i * pitch
        f.line([(x1 + 6, y), (labx_n - 14, ry)], fill=GRAPH, w=2)
        f.rich(labx_n, ry + lab * 0.35, f"n = {nn}", lab)
    y = ys[1]
    f.line([(x0, y), (x1, y)], fill=ACC, w=7)
    f.line([(x1 + 6, y), (labx_n - 14, y)], fill=GRAPH, w=2)
    f.rich(labx_n, y + lab * 0.35, "n = 1", lab)
    f.save("chem_u02_s2.1_energy_levels.png")


def _three_levels(f, lab, top=70, bot=515):
    """n = 1, 2, 3 in order, NOT to scale: at true scale n = 2 and n = 3 are too close for an
    arrow and a dot. The energy-level slide is the to-scale figure; this one says so."""
    ys = {1: bot, 2: 235, 3: top}
    assert_levels(ys)
    y_of = lambda n: ys[n]
    x0, x1 = 215, 965
    for n in (1, 2, 3):
        y = y_of(n)
        f.line([(x0, y), (x1, y)], fill=INK, w=4)
        f.rich(190, y + lab * 0.35, f"n = {n}", lab, anchor="r")
    f.rich(x0, 36, "energy", lab, fill=GRAPH)
    f.arrow(x0 - 18, bot + 8, x0 - 18, 30, fill=GRAPH, w=3, head=16)
    f.rich(x1, 590, "levels not to scale", lab, fill=GRAPH, anchor="r")
    return y_of, x0, x1


def fig_absorption():
    f = Fig(1010, 5.05, 3.0, PARCH)
    lab = f.pt(16)
    y_of, x0, x1 = _three_levels(f, lab)
    ax = 470
    r = 13
    f.arrow(ax, y_of(1) - r - 4, ax, y_of(2) + r + 8, fill=ACC, w=6, head=26)
    f.circle(ax, y_of(1), r, fill=ACC, outline=INK, w=3)                  # electron before
    f.circle(ax, y_of(2), r, fill=PARCH, outline=ACC, w=4)                # electron after
    wy = (y_of(1) + y_of(2)) / 2
    f.wave(x0 + 20, ax - 30, wy, fill=ACC)
    f.rich(x0 + 20, wy - 36, "photon in", lab)
    f.rich(600, wy - 4, "atom gains energy", lab)
    f.rich(600, wy + 52, "electron goes up", lab)
    f.save("chem_u02_s2.1_absorption.png")


def fig_emission():
    f = Fig(1010, 5.05, 3.0, PARCH)
    lab = f.pt(16)
    y_of, x0, x1 = _three_levels(f, lab)
    ax = 470
    r = 13
    f.arrow(ax, y_of(3) + r + 4, ax, y_of(2) - r - 8, fill=ACC, w=6, head=22)
    f.circle(ax, y_of(3), r, fill=PARCH, outline=ACC, w=4)                # electron before
    f.circle(ax, y_of(2), r, fill=ACC, outline=INK, w=3)                  # electron after
    wy = (y_of(3) + y_of(2)) / 2 + 6
    f.wave(ax + 36, ax + 360, wy, fill=ACC)
    f.rich(ax + 40, wy - 28, "photon out", lab)
    ty = (y_of(2) + y_of(1)) / 2
    f.rich(600, ty, "atom loses energy", lab)
    f.rich(600, ty + 52, "electron goes down", lab)
    f.save("chem_u02_s2.1_emission.png")


def _data_fig():
    return Fig(850, 4.23, 2.48, WHITE)


def fig_ground_excited():
    """Slide 14 (solution 1). Levels n = 1..5, NOT to scale (at true scale n = 3, 4, 5 are
    too close together to draw an arrow), but the gaps still shrink as n rises."""
    f = _data_fig()
    lab = f.pt(16)
    ys = {1: 440, 2: 350, 3: 285, 4: 240, 5: 205}
    assert_levels(ys)
    x0, x1, lx = 30, 250, 330
    r = 13
    for n in (5, 4, 3, 2, 1):
        y = ys[n]
        f.line([(x0, y), (x1, y)], fill=ACC if n == 1 else INK, w=7 if n == 1 else 4)
    notes = {5: "n = 5, goal", 4: "n = 4", 3: "n = 3, start", 2: "n = 2", 1: "n = 1, ground state"}
    # labels: n = 5 and n = 4 are close, so spread them with leaders
    rows = {5: 170, 4: 228, 3: 285, 2: 350, 1: 440}
    for n in (5, 4, 3, 2, 1):
        f.line([(x1 + 6, ys[n]), (lx - 14, rows[n])], fill=GRAPH, w=2)
        f.rich(lx, rows[n] + lab * 0.35, notes[n], lab)
    ax = 120
    f.arrow(ax, ys[3] - r - 4, ax, ys[5] + 6, fill=ACC, w=6, head=22)
    f.circle(ax, ys[3], r, fill=ACC, outline=INK, w=3)                    # the electron, now
    f.rich(x0, 60, "levels not to scale", lab, fill=GRAPH)
    f.save("chem_u02_s2.1_ground_excited.png")


def fig_drops_ranked():
    """Slide 16 (solution 2). Levels n = 1..4 and the top, TO SCALE. Three drops: A 4 to 2,
    B 3 to 2, C 2 to 1. Arrow length is the energy released, so the arrows rank themselves."""
    f = _data_fig()
    lab = f.pt(16)
    top, bot = 60, 400
    ys = {n: bot - (rel_energy(n) - rel_energy(1)) * (bot - top) for n in (1, 2, 3, 4)}
    assert_levels(ys)
    drops = {"A": (4, 2), "B": (3, 2), "C": (2, 1)}
    size = {k: ys[b] - ys[a] for k, (a, b) in drops.items()}      # arrow length, px
    order = sorted(size, key=size.get)
    assert order == ["B", "A", "C"], order                          # least to most energy
    x0, x1, lx = 30, 250, 330
    f.line([(x0, top), (x1, top)], fill=GRAPH, w=3, dash=(14, 10))
    f.rich(lx, 34 + lab * 0.35, "top: electron gone", lab, fill=GRAPH)
    rows = {4: 92, 3: 140, 2: 188, 1: ys[1]}
    for n in (4, 3, 2, 1):
        f.line([(x0, ys[n]), (x1, ys[n])], fill=ACC if n == 1 else INK, w=7 if n == 1 else 4)
        f.line([(x1 + 6, ys[n]), (lx - 14, rows[n])], fill=GRAPH, w=2)
        f.rich(lx, rows[n] + lab * 0.35, f"n = {n}", lab)
    xs = {"A": 62, "B": 125, "C": 190}
    for k, (a, b) in drops.items():
        f.arrow(xs[k], ys[a] + 3, xs[k], ys[b] - 2, fill=ACC, w=5, head=18)
    # letters: A and B under the n = 2 line, C beside its long arrow
    for k in ("A", "B"):
        f.rich(xs[k], ys[2] + 14 + lab * 0.8, k, lab * 1.1, "Archivo-Bold.ttf", anchor="m")
    f.rich(xs["C"] + 24, (ys[2] + ys[1]) / 2 + lab * 0.35, "C", lab * 1.1, "Archivo-Bold.ttf")
    f.rich(x0, 474, "levels to scale", lab, fill=GRAPH)
    f.save("chem_u02_s2.1_drops_ranked.png")


def fig_ionization():
    """Slide 18 (solution 3). n = 1, 2, 3 to scale, the dashed top, an arrow up and out."""
    f = _data_fig()
    lab = f.pt(16)
    top, bot = 95, 410
    ys = {n: bot - (rel_energy(n) - rel_energy(1)) * (bot - top) for n in (1, 2, 3)}
    assert_levels(ys)
    x0, x1, lx = 30, 250, 330
    r = 13
    f.line([(x0, top), (x1, top)], fill=GRAPH, w=3, dash=(14, 10))
    f.line([(x1 + 6, top), (lx - 14, 72)], fill=GRAPH, w=2)
    f.rich(lx, 72 + lab * 0.35, "n = ∞", lab)
    rows = {3: 130, 2: 188, 1: ys[1]}
    for n in (3, 2, 1):
        f.line([(x0, ys[n]), (x1, ys[n])], fill=ACC if n == 1 else INK, w=7 if n == 1 else 4)
        f.line([(x1 + 6, ys[n]), (lx - 14, rows[n])], fill=GRAPH, w=2)
        f.rich(lx, rows[n] + lab * 0.35, f"n = {n}" + (", ground" if n == 1 else ""), lab)
    ax = 120
    f.arrow(ax, ys[1] - r - 4, ax, top - 34, fill=ACC, w=6, head=24)
    f.circle(ax, ys[1], r, fill=ACC, outline=INK, w=3)                    # electron, start
    f.circle(ax, top - 56, r, fill=WHITE, outline=ACC, w=4)               # electron, gone
    f.rich(ax + 28, top - 52 + lab * 0.35, "leaves", lab)
    f.save("chem_u02_s2.1_ionization.png")


def assert_text():
    """No exponent, times sign, energy unit or number that is not a level label."""
    import re
    bad = []
    for s in PRINTED:
        if not s:
            continue
        if re.search(r"[×−\^]|10|e-\d|\bJ\b|\bjoule", s, re.I):
            bad.append(s)
        # digits are allowed only as level labels: "n = 4", "n = 4, goal" ...
        if re.search(r"\d", s) and not re.fullmatch(r"(n = \d(, [a-z ]+)?|1 proton|1 electron)", s):
            bad.append(s)
    assert not bad, f"forbidden text in figures: {bad}"


def main():
    fig_bohr_hydrogen()
    fig_level_numbers()
    fig_levels()
    fig_absorption()
    fig_emission()
    fig_ground_excited()
    fig_drops_ranked()
    fig_ionization()
    assert_text()
    print(f"text check passed on {len(PRINTED)} printed strings; no number but level labels")
    return 0


if __name__ == "__main__":
    sys.exit(main())
