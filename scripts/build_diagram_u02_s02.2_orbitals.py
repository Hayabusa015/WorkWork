#!/usr/bin/env python3
"""Draw the five science figures for CHEM U02 S2.2 (Energy Levels, Sublevels & Orbitals).

Hand-built, not generated. Anything a student reads as science - an orbital shape with a
label, a level/sublevel/orbital map, a capacity table, a block map of the periodic table -
is built with PIL from numbers that are checked here, not drawn from a model's idea of what
an orbital looks like.

Colours come from brand/tokens.json. Type comes from the shipped Archivo files, the same
ones the deck embeds.

Canvas: 505 x 300 units = the 08_DIAGRAM_ANNOTATION diagram slot (5.05 x 3.00 in) at 100
units per inch, so one unit is 0.01 in on the slide and 16 pt is 22.2 units. Every label
below is 23 units or larger, which keeps it at or above the 16 pt floor once placed.

    python3 scripts/build_diagram_u02_s02.2_orbitals.py
"""
import json, math, os, sys
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(REPO, "templates", "slide", "assets")
SCALE = 4
W, H = 505, 300
MIN_LABEL = 23          # units; 16 pt at placed size

T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
WHITE = T["ground"]["white"]["hex"]
ASPHALT = T["ground"]["asphalt"]["hex"]
GRAPHITE = T["ground"]["graphite"]["hex"]
PARCH = T["ground"]["parchment"]["hex"]
HAIR = T["ground"]["ruleHairline"]["hex"]
LIME = T["courses"]["chemistry"]["primary"]["hex"]
DEEP = T["courses"]["chemistry"]["primaryDeep"]["hex"]


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    """t of a over b."""
    ra, rb = rgb(a), rgb(b)
    return "#%02X%02X%02X" % tuple(round(ra[i] * t + rb[i] * (1 - t)) for i in range(3))


LIME_TINT = mix(LIME, WHITE, 0.55)
LIME_PALE = mix(LIME, WHITE, 0.25)


def font(name, units):
    assert units >= MIN_LABEL, f"label {units} units is under the 16 pt floor"
    return ImageFont.truetype(os.path.join(REPO, "brand", "fonts", name), int(units * SCALE))


def S(v):
    return int(round(v * SCALE))


def canvas():
    im = Image.new("RGB", (W * SCALE, H * SCALE), WHITE)
    return im, ImageDraw.Draw(im)


def text(d, xy, s, f, fill=ASPHALT, anchor="mm"):
    d.text((S(xy[0]), S(xy[1])), s, font=f, fill=fill, anchor=anchor)


def rect(d, x0, y0, x1, y1, fill=None, outline=None, width=1):
    d.rectangle([S(x0), S(y0), S(x1), S(y1)], fill=fill, outline=outline, width=int(width * SCALE))


def save(im, name):
    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, name)
    im.save(path)
    print(f"wrote {os.path.relpath(path, REPO)}  {im.width}x{im.height}")


# ------------------------------------------------------------------ 1. shapes
def lobe(cx, cy, ang, a, b, n=72):
    """Polygon for an ellipse centred (cx,cy), semi-axes a (along ang) and b."""
    pts = []
    ca, sa = math.cos(ang), math.sin(ang)
    for i in range(n):
        t = 2 * math.pi * i / n
        x, y = a * math.cos(t), b * math.sin(t)
        pts.append((S(cx + x * ca - y * sa), S(cy + x * sa + y * ca)))
    return pts


def shapes():
    im, d = canvas()
    im = im.convert("RGBA")
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    fill = rgb(LIME) + (130,)
    edge = rgb(DEEP) + (255,)

    cxs = [84, 252, 420]
    cy = 126

    # s: one sphere
    ld.ellipse([S(cxs[0] - 50), S(cy - 50), S(cxs[0] + 50), S(cy + 50)], fill=fill, outline=edge, width=S(2))

    # p: three dumbbells on x, y, z axes (z drawn toward the viewer, lower left)
    for ang in (0, math.pi / 2, math.radians(135)):
        for sign in (1, -1):
            ox, oy = math.cos(ang) * 28 * sign, math.sin(ang) * 28 * sign
            ld.polygon(lobe(cxs[1] + ox, cy + oy, ang, 28, 13), fill=fill, outline=edge)
            ld.line(lobe(cxs[1] + ox, cy + oy, ang, 28, 13) + [lobe(cxs[1] + ox, cy + oy, ang, 28, 13)[0]],
                    fill=edge, width=S(2))

    # d: four lobes between the axes
    for ang in (math.radians(45), math.radians(135)):
        for sign in (1, -1):
            ox, oy = math.cos(ang) * 32 * sign, math.sin(ang) * 32 * sign
            pts = lobe(cxs[2] + ox, cy + oy, ang, 32, 14)
            ld.polygon(pts, fill=fill)
            ld.line(pts + [pts[0]], fill=edge, width=S(2))
    im = Image.alpha_composite(im, layer)
    d = ImageDraw.Draw(im)

    # nuclei
    for x in cxs:
        d.ellipse([S(x - 3.5), S(cy - 3.5), S(x + 3.5), S(cy + 3.5)], fill=ASPHALT)

    f_big = font("Archivo-Bold.ttf", 36)
    f_lab = font("Archivo-SemiBold.ttf", 23)
    f_ax = font("Archivo-SemiBold.ttf", 23)
    for x, letter, n in zip(cxs, "spd", ("1 orbital", "3 orbitals", "5 orbitals")):
        text(d, (x, 22), letter, f_big)
        text(d, (x, 206 if letter == "d" else 214), n, f_lab)
    text(d, (cxs[2], 231), "(1 of 5 shown)", f_lab, GRAPHITE)
    # p axis letters at the lobe tips
    text(d, (cxs[1] + 70, cy), "x", f_ax, GRAPHITE)
    text(d, (cxs[1] + 2, cy - 72), "y", f_ax, GRAPHITE)
    text(d, (cxs[1] - 58, cy + 56), "z", f_ax, GRAPHITE)

    for x in (168, 336):
        d.line([(S(x), S(10)), (S(x), S(230))], fill=HAIR, width=S(1))
    d.line([(S(20), S(244)), (S(W - 20), S(244))], fill=HAIR, width=S(1))
    text(d, (W / 2, 272), "PROBABILITY REGIONS, NOT PATHS", font("Archivo-Bold.ttf", 24), GRAPHITE)
    save(im, "chem_u02_s2.2_orbital_shapes.png")


# ------------------------------------------------------- 2. level/sublevel map
def level_map():
    im, d = canvas()
    f_n = font("Archivo-Bold.ttf", 25)
    f_sub = font("Archivo-Bold.ttf", 24)
    box, gap = 24, 14
    x_start = 74
    counts = {"s": 1, "p": 3, "d": 5, "f": 7}
    pitch = 72
    for i, n in enumerate((4, 3, 2, 1)):
        y_label = 14 + i * pitch
        y_box = 30 + i * pitch
        text(d, (8, y_box + box / 2 + 1), f"n={n}", f_n, ASPHALT, anchor="lm")
        x = x_start
        for letter in "spdf"[:n]:
            k = counts[letter]
            gw = k * box
            for j in range(k):
                rect(d, x + j * box, y_box, x + (j + 1) * box, y_box + box, fill=LIME_TINT,
                     outline=GRAPHITE, width=1.5)
            text(d, (x + gw / 2, y_label), f"{n}{letter}", f_sub)
            x += gw + gap
    save(im, "chem_u02_s2.2_level_sublevel_orbital_map.png")


# ------------------------------------------------------ 3. shell capacity table
def capacity_table():
    im, d = canvas()
    rows = []
    for n in (1, 2, 3, 4):
        subs = "  ".join(f"{n}{l}" for l in "spdf"[:n])
        orbs = sum(2 * i + 1 for i in range(n))      # 1 + 3 + 5 + 7 ...
        rows.append((str(n), subs, str(orbs), str(2 * orbs)))
    assert [r[2] for r in rows] == ["1", "4", "9", "16"]
    assert [r[3] for r in rows] == ["2", "8", "18", "32"]
    assert all(int(r[2]) == int(r[0]) ** 2 and int(r[3]) == 2 * int(r[0]) ** 2 for r in rows)

    x_n, x_sub, x_orb, x_el = 28, 60, 286, 422
    # tinted columns carry the two totals
    rect(d, 228, 4, 346, 296, fill=LIME_PALE)
    rect(d, 346, 4, 498, 296, fill=LIME_TINT)
    f_h = font("Archivo-SemiBold.ttf", 23)
    f_d = font("Archivo-Bold.ttf", 28)
    f_nn = font("Archivo-Bold.ttf", 28)
    top = 8
    hh = 44
    for x, label, anc in ((x_n, "n", "mm"), (x_sub, "SUBLEVELS", "lm"), (x_orb, "ORBITALS", "mm"),
                          (x_el, "ELECTRONS", "mm")):
        text(d, (x, top + hh / 2), label, f_h, GRAPHITE, anchor=anc)
    d.line([(S(8), S(top + hh)), (S(W - 8), S(top + hh))], fill=GRAPHITE, width=S(2))
    rh = (H - 8 - top - hh) / 4
    for i, (n, subs, orbs, els) in enumerate(rows):
        yc = top + hh + rh * i + rh / 2
        text(d, (x_n, yc), n, f_nn)
        text(d, (x_sub, yc), subs, f_d, anchor="lm")
        text(d, (x_orb, yc), orbs, f_d)
        text(d, (x_el, yc), els, f_d)
        if i < 3:
            y = top + hh + rh * (i + 1)
            d.line([(S(8), S(y)), (S(W - 8), S(y))], fill=HAIR, width=S(1))
    save(im, "chem_u02_s2.2_shell_capacity_table.png")


# ----------------------------------------------------------- 4. filling order
def filling_order():
    im, d = canvas()
    order = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p"]
    ncount = {"s": 1, "p": 3, "d": 5}
    col_x = {"s": 104, "p": 194, "d": 338}      # left edge of the first box
    f = font("Archivo-Bold.ttf", 24)
    box = 24
    y0, step = 266, 31
    centers = []
    for r, name in enumerate(order):
        l = name[1]
        yc = y0 - r * step
        k = ncount[l]
        for j in range(k):
            x = col_x[l] + j * (box + 3)
            rect(d, x, yc - 6, x + box, yc + 6, fill=LIME_TINT, outline=GRAPHITE, width=1.5)
        gx0 = col_x[l]
        gx1 = col_x[l] + k * box + (k - 1) * 3
        text(d, (gx0 - 8, yc), name, f, anchor="rm")
        centers.append(((gx0 + gx1) / 2, yc))
    # a thin path through the sequence, drawn under nothing: hairline between neighbours
    for (xa, ya), (xb, yb) in zip(centers, centers[1:]):
        d.line([(S(xa), S(ya - 8)), (S(xb), S(yb + 8))], fill=HAIR, width=S(1))
    # arrow, bottom to top, with a rotated label
    ax = 20
    d.line([(S(ax), S(290)), (S(ax), S(24))], fill=DEEP, width=S(3))
    d.polygon([(S(ax), S(10)), (S(ax - 8), S(26)), (S(ax + 8), S(26))], fill=DEEP)
    lab = "FILLING ORDER"
    fl = font("Archivo-Bold.ttf", 23)
    tmp = Image.new("RGBA", (S(190), S(30)), (0, 0, 0, 0))
    ImageDraw.Draw(tmp).text((S(95), S(15)), lab, font=fl, fill=GRAPHITE, anchor="mm")
    rot = tmp.rotate(90, expand=True)
    im.paste(rot, (S(30), S(150) - rot.height // 2), rot)
    save(im, "chem_u02_s2.2_filling_order.png")


# ------------------------------------------------------ 5. block map of the table
def block_map():
    im, d = canvas()
    cw, ch = 25.5, 23
    x0, y0 = 32, 34
    grid = {}   # (row, col) -> block ; row 1..7, col 1..18 ; f rows are 8, 9
    for r in range(1, 8):
        for c in range(1, 19):
            blk = None
            if r == 1:
                blk = "s" if c in (1, 18) else None
            else:
                if c in (1, 2):
                    blk = "s"
                elif 13 <= c <= 18:
                    blk = "p"
                elif 3 <= c <= 12 and r >= 4:
                    blk = "d"
            if blk:
                grid[(r, c)] = blk
    for r in (8, 9):
        for c in range(3, 17):
            grid[(r, c)] = "f"
    # checks: widths match the sublevel capacities
    assert sum(1 for (r, c), b in grid.items() if r == 5 and b == "s") == 2
    assert sum(1 for (r, c), b in grid.items() if r == 5 and b == "d") == 10
    assert sum(1 for (r, c), b in grid.items() if r == 5 and b == "p") == 6
    assert sum(1 for (r, c), b in grid.items() if r == 8 and b == "f") == 14
    row_len = [sum(1 for (r, c) in grid if r == k) for k in range(1, 8)]
    f_each = 14
    totals = [row_len[k] + (f_each if k >= 5 else 0) for k in range(7)]
    assert totals == [2, 8, 8, 18, 18, 32, 32], totals

    fillc = {"s": LIME_TINT, "p": PARCH, "d": HAIR, "f": WHITE}

    def ypos(r):
        return y0 + (r - 1) * ch + (10 if r >= 8 else 0)

    def cell(r, c):
        x = x0 + (c - 1) * cw
        y = ypos(r)
        return x, y, x + cw, y + ch

    for (r, c), b in grid.items():
        xa, ya, xb, yb = cell(r, c)
        rect(d, xa, ya, xb, yb, fill=fillc[b], outline=WHITE, width=0.8)
    # heavy boundary wherever the neighbour belongs to a different block
    for (r, c), b in grid.items():
        xa, ya, xb, yb = cell(r, c)
        for dr, dc, seg in ((-1, 0, (xa, ya, xb, ya)), (1, 0, (xa, yb, xb, yb)),
                            (0, -1, (xa, ya, xa, yb)), (0, 1, (xb, ya, xb, yb))):
            nb = grid.get((r + dr, c + dc))
            if nb != b:
                # f block: deep-green heavy border so it reads apart from p in grayscale
                d.line([(S(seg[0]), S(seg[1])), (S(seg[2]), S(seg[3]))],
                       fill=DEEP if b == "f" else GRAPHITE, width=S(3.2 if b == "f" else 1.8))

    f_p = font("Archivo-SemiBold.ttf", 23)
    f_grp = font("Archivo-SemiBold.ttf", 23)
    f_blk = font("Archivo-Bold.ttf", 34)
    # period numbers
    for r in range(1, 8):
        text(d, (26, y0 + (r - 1) * ch + ch / 2), str(r), f_p, GRAPHITE, anchor="rm")
    # group brackets
    for label, c0, c1 in (("1–2", 1, 2), ("3–12", 3, 12), ("13–18", 13, 18)):
        xa = x0 + (c0 - 1) * cw + 2
        xb = x0 + c1 * cw - 2
        text(d, ((xa + xb) / 2, 12), label, f_grp, GRAPHITE)
        d.line([(S(xa), S(y0 - 6)), (S(xb), S(y0 - 6))], fill=GRAPHITE, width=S(1.2))
    # block letters, centred in the block
    def centre(rows, cols):
        xa, _, _, _ = cell(rows[0], cols[0])
        _, _, xb, _ = cell(rows[0], cols[1])
        _, ya, _, _ = cell(rows[0], cols[0])
        _, _, _, yb = cell(rows[1], cols[0])
        return (xa + xb) / 2, (ya + yb) / 2
    text(d, centre((3, 7), (1, 2)), "s", f_blk)
    text(d, centre((2, 7), (13, 18)), "p", f_blk)
    text(d, centre((4, 7), (3, 12)), "d", f_blk)
    text(d, centre((8, 9), (3, 16)), "f", f_blk)
    # widths row, tying the blocks to the capacities
    text(d, (W / 2, 280), "WIDTH:   s 2    p 6    d 10    f 14", font("Archivo-Bold.ttf", 24), GRAPHITE)
    save(im, "chem_u02_s2.2_periodic_table_blocks.png")


def main():
    shapes()
    level_map()
    capacity_table()
    filling_order()
    block_map()
    return 0


if __name__ == "__main__":
    sys.exit(main())
