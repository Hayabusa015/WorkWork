#!/usr/bin/env python3
"""Draw the hand-built figures for CHEM U02 S2.1 The Bohr Model.

Hand-built, not generated. A Bohr diagram, an energy-level diagram and an equation all
carry numbers and counts a student reads as science, and a generated one gets the
electron count or the spacing wrong in a way nobody catches at a glance. Every energy
printed here is computed from E_n = -2.18e-18 J / n^2, not typed.

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

RYD = 2.18e-18                  # J, the course constant (courses/chemistry via the brief)


def energy_1e19(n):
    """E_n in units of 1e-19 J (so 2.18e-18 J is 21.8)."""
    return -RYD / (n * n) / 1e-19


def fmt(x):
    return f"{x:.3g}".replace("-", "−")


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


E = lambda n: [("E", "n"), (str(n), "sub")]          # E with subscript level
EXP = lambda m: [("× 10", "n"), (m, "sup")]       # x 10^m


# ---------------------------------------------------------------------------------------
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


def fig_equation():
    f = Fig(1010, 5.05, 3.0, PARCH)
    big = 78
    lab = f.pt(16)
    num = [("2.18 × 10", "n"), ("−18", "sup"), (" J", "n")]
    den = [("n", "n"), ("2", "sup")]
    fb = "Archivo-Bold.ttf"
    wE = f._parts_w(E("n"), big * 1.15, fb)
    wEq = f._parts_w([(" = −", "n")], big, fb)
    wNum = f._parts_w(num, big * 0.82, fb)
    barw = wNum + 36
    gap = 22
    total = wE + wEq + gap + barw
    x0 = (f.W - total) / 2
    base = 305                                    # baseline of the "E_n = -" part and the bar
    bar_y = base - big * 0.33
    f.rich(x0, base, E("n"), big * 1.15, fb)
    f.rich(x0 + wE, base, [(" = −", "n")], big, fb)
    fx = x0 + wE + wEq + gap
    f.line([(fx, bar_y), (fx + barw, bar_y)], fill=INK, w=5)
    f.rich(fx + barw / 2, bar_y - 20, num, big * 0.82, fb, anchor="m")
    f.rich(fx + barw / 2, bar_y + 20 + big * 0.82 * 0.72, den, big * 0.82, fb, anchor="m")
    # three plain labels, each tied to its part by a short rule
    # constant, above
    f.line([(fx + barw / 2, 120), (fx + barw / 2, bar_y - 20 - big * 0.82 * 0.8)], fill=ACC, w=3)
    f.rich(fx + barw / 2, 88, "constant for hydrogen", lab, anchor="m")
    # energy, below E_n
    ex_mid = x0 + wE / 2
    f.line([(ex_mid, base + 14), (ex_mid, 400)], fill=ACC, w=3)
    f.rich(ex_mid, 400 + lab * 0.95, "energy", lab, anchor="m")
    # level number, below n^2
    dn_mid = fx + barw / 2
    f.line([(dn_mid, bar_y + 20 + big * 0.82 * 0.72 + 22), (dn_mid, 400)], fill=ACC, w=3)
    f.rich(dn_mid, 400 + lab * 0.95, "n = 1, 2, 3 ...", lab, anchor="m")
    f.save("chem_u02_s2.1_energy_equation.png")


def fig_levels():
    f = Fig(1010, 5.05, 3.0, PARCH)
    lab = f.pt(16)
    top, bot = 100, 548                           # E = 0 at top, n = 1 at the bottom
    k = (bot - top) / abs(energy_1e19(1))         # px per 1e-19 J: drawn to scale
    y_of = lambda e: top - e * k
    f.rich(40, 52, [("Energy (", "n")] + EXP("−19") + [(" J)", "n")], lab)
    x0, x1 = 60, 480
    f.arrow(40, bot + 4, 40, 78, fill=GRAPH, w=3, head=16)
    labx_n, labx_v = 600, 960
    pitch = 52
    rows = [("∞", None)] + [(str(n), n) for n in (6, 5, 4, 3, 2)]
    for i, (nn, n) in enumerate(rows):
        e = 0.0 if n is None else energy_1e19(n)
        y = y_of(e)
        f.line([(x0, y), (x1, y)], fill=GRAPH if n is None else INK, w=3,
               dash=(14, 10) if n is None else None)
        ry = top + i * pitch
        f.line([(x1 + 6, y), (labx_n - 14, ry)], fill=GRAPH, w=2)
        f.rich(labx_n, ry + lab * 0.35, f"n = {nn}", lab)
        f.rich(labx_v, ry + lab * 0.35, "0" if n is None else fmt(e), lab, anchor="r")
    y = y_of(energy_1e19(1))
    f.line([(x0, y), (x1, y)], fill=ACC, w=7)
    f.line([(x1 + 6, y), (labx_n - 14, y)], fill=GRAPH, w=2)
    f.rich(labx_n, y + lab * 0.35, "n = 1", lab)
    f.rich(labx_v, y + lab * 0.35, fmt(energy_1e19(1)), lab, anchor="r")
    f.save("chem_u02_s2.1_energy_levels.png")


def _three_levels(f, lab, top=70, bot=515):
    """n = 1, 2, 3 in order, NOT to scale: at true scale n = 2 and n = 3 are too close for an
    arrow and a dot. The energy-level slide is the to-scale figure; this one says so."""
    ys = {1: bot, 2: 235, 3: top}
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
    f.rich(600, wy - 4, [("\u0394E = E", "n"), ("2", "sub"), (" \u2212 E", "n"), ("1", "sub")], lab)
    f.rich(600, wy + 52, "\u0394E is positive", lab)
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
    f.rich(600, ty, [("\u0394E = E", "n"), ("2", "sub"), (" \u2212 E", "n"), ("3", "sub")], lab)
    f.rich(600, ty + 52, "\u0394E is negative", lab)
    f.save("chem_u02_s2.1_emission.png")


def _data_fig():
    return Fig(850, 4.23, 2.48, WHITE)


def fig_level_n3():
    f = _data_fig()
    lab = f.pt(16)
    top, bot = 70, 420
    k = (bot - top) / abs(energy_1e19(2))
    y_of = lambda e: top - e * k
    x0, x1, lx = 30, 300, 322
    f.line([(x0, y_of(0)), (x1, y_of(0))], fill=GRAPH, w=3, dash=(14, 10))
    f.rich(lx, y_of(0) + lab * 0.35, "n = \u221e:  E = 0", lab)
    for n, hi in ((3, True), (2, False)):
        e = energy_1e19(n)
        y = y_of(e)
        f.line([(x0, y), (x1, y)], fill=ACC if hi else INK, w=7 if hi else 4)
        f.rich(lx, y + lab * 0.35, E(n) + [(" = " + fmt(e) + " ", "n")] + EXP("\u221219") + [(" J", "n")], lab)
    f.circle(150, y_of(energy_1e19(3)), 13, fill=ACC, outline=INK, w=3)
    f.save("chem_u02_s2.1_level_n3.png")


def fig_transition_3_to_2():
    f = _data_fig()
    lab = f.pt(16)
    top, bot = 80, 400
    y3, y2 = top, bot
    x0, x1, lx = 30, 300, 322
    r = 13
    for n, y in ((3, y3), (2, y2)):
        f.line([(x0, y), (x1, y)], fill=INK, w=4)
        f.rich(lx, y + lab * 0.35, E(n) + [(" = " + fmt(energy_1e19(n)) + " ", "n")] + EXP("\u221219") + [(" J", "n")], lab)
    ax = 100
    f.arrow(ax, y3 + r + 4, ax, y2 - r - 8, fill=ACC, w=6, head=22)
    f.circle(ax, y3, r, fill=WHITE, outline=ACC, w=4)
    f.circle(ax, y2, r, fill=ACC, outline=INK, w=3)
    wy = (y3 + y2) / 2
    f.wave(ax + 30, x1 - 10, wy, fill=ACC)
    f.rich(lx, wy + lab * 0.35, [("\u0394E = " + fmt(energy_1e19(2) - energy_1e19(3)) + " ", "n")] + EXP("\u221219") + [(" J", "n")], lab)
    f.save("chem_u02_s2.1_transition_3_to_2.png")


def fig_ionization():
    f = _data_fig()
    lab = f.pt(16)
    top, bot = 80, 400
    x0, x1, lx = 30, 300, 322
    r = 13
    f.line([(x0, top), (x1, top)], fill=GRAPH, w=3, dash=(14, 10))
    f.rich(lx, top + lab * 0.35, "n = \u221e:  E = 0", lab)
    f.line([(x0, bot), (x1, bot)], fill=INK, w=4)
    f.rich(lx, bot + lab * 0.35, E(1) + [(" = \u22122.18 ", "n")] + EXP("\u221218") + [(" J", "n")], lab)
    ax = 100
    f.arrow(ax, bot - r - 4, ax, top + 2, fill=ACC, w=6, head=24)
    f.circle(ax, bot, r, fill=ACC, outline=INK, w=3)
    f.rich(lx, (top + bot) / 2 + lab * 0.35, [("\u0394E = +2.18 ", "n")] + EXP("\u221218") + [(" J", "n")], lab)
    f.save("chem_u02_s2.1_ionization.png")


def main():
    fig_bohr_hydrogen()
    fig_equation()
    fig_levels()
    fig_absorption()
    fig_emission()
    fig_level_n3()
    fig_transition_3_to_2()
    fig_ionization()
    return 0


if __name__ == "__main__":
    sys.exit(main())
