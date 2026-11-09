"""Geology U3 guided-notes fill-in figures, hand-built (SHULL_DESIGN_SYSTEM.md §7).

    python3 templates/notes/specs/make_geo_u03_figures.py

Writes a student and a key PNG per figure into templates/notes/assets/. Same geometry
in both; the student copy leaves the answer boxes empty and the key fills them in the
course's text-safe colour. Ink only, hairline boxes, Archivo. Wording follows Matt's
U3 slide deck, slide by slide.
"""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageFont
REPO = "/home/user/WorkWork"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
DPI = 300
INK, LABEL, HAIR, WHITE, KEYC = "#14161B", "#55604F", "#C8CDC2", "#FFFFFF", "#0E766A"
F = lambda w, pt: ImageFont.truetype(f"{REPO}/brand/fonts/Archivo-{w}.ttf", int(pt / 72 * DPI))
px = lambda v: int(round(v * DPI))
rgb = lambda h: tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))

class Fig:
    def __init__(s, w, h):
        s.im = Image.new("RGB", (px(w), px(h)), rgb(WHITE)); s.d = ImageDraw.Draw(s.im)
    def box(s, cx, cy, w, h, text="", key=False, bold=True, pt=9.5, fill=WHITE, edge=LABEL, lw=0.8):
        r = (px(cx - w / 2), px(cy - h / 2), px(cx + w / 2), px(cy + h / 2))
        s.d.rectangle(r, fill=rgb(fill), outline=rgb(edge), width=max(2, px(lw / 72)))
        if text: s.text(cx, cy, text, pt, bold, KEYC if key else INK)
        return (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    def text(s, cx, cy, text, pt=9.5, bold=True, color=INK, anchor="mm"):
        f = F("Bold" if bold else "Regular", pt)
        lines = text.split("\n"); lh = pt / 72 * 1.18
        y0 = cy - lh * (len(lines) - 1) / 2
        for i, ln in enumerate(lines):
            s.d.text((px(cx), px(y0 + i * lh)), ln, font=f, fill=rgb(color), anchor=anchor)
    def arrow(s, a, b, color=LABEL, lw=1.0, head=0.09):
        (x0, y0), (x1, y1) = a, b
        s.d.line([px(x0), px(y0), px(x1), px(y1)], fill=rgb(color), width=max(2, px(lw / 72)))
        ang = math.atan2(y1 - y0, x1 - x0)
        p = [(x1, y1), (x1 - head * math.cos(ang - .4), y1 - head * math.sin(ang - .4)),
             (x1 - head * math.cos(ang + .4), y1 - head * math.sin(ang + .4))]
        s.d.polygon([(px(x), px(y)) for x, y in p], fill=rgb(color))
    def save(s, path): s.im.save(path, dpi=(DPI, DPI))

def clip(rect, a, b):
    """Point where segment a->b leaves rect (rect contains a)."""
    (x0, y0, x1, y1), (ax, ay), (bx, by) = rect, a, b
    ts = []
    for edge, d, o in ((x0, bx - ax, ax), (x1, bx - ax, ax)):
        if d: ts.append((edge - o) / d)
    for edge, d, o in ((y0, by - ay, ay), (y1, by - ay, ay)):
        if d: ts.append((edge - o) / d)
    t = min(t for t in ts if t > 0 and all(
        r0 - 1e-6 <= v <= r1 + 1e-6 for v, r0, r1 in
        ((ax + t * (bx - ax), x0, x1), (ay + t * (by - ay), y0, y1))))
    return ax + t * (bx - ax), ay + t * (by - ay)

def wordbank(fig, y, w, lines, note=None):
    fig.d.line([px(0.05), px(y - 0.18), px(w - 0.05), px(y - 0.18)], fill=rgb(HAIR), width=2)
    fig.text(0.05, y, "WORD BANK", 7.5, True, LABEL, anchor="lm")
    for i, terms in enumerate(lines):
        fig.text(0.95, y + i * 0.2, "  ·  ".join(terms), 8.5, False, INK, anchor="lm")
    if note: fig.text(0.95, y + len(lines) * 0.2, note, 7.5, False, LABEL, anchor="lm")

# ---------------------------------------------------------------- rock cycle
def rock_cycle(key):
    """Laid out as slide 13 is: Magma top left, Igneous top right, Sediment right,
    Sedimentary bottom, Metamorphic left. Arrow words are the slide's."""
    W, H = 6.2, 4.55
    g = Fig(W, H)
    BW, BH = 1.6, 0.5
    nodes = {"mag": (1.0, 0.35, "MAGMA", True), "ign": (5.2, 0.35, "IGNEOUS ROCK", False),
             "met": (0.9, 1.95, "METAMORPHIC ROCK", False), "sed": (5.3, 1.95, "SEDIMENT", True),
             "sdr": (3.1, 3.5, "SEDIMENTARY ROCK", False)}
    edges = [((1.8, 0.35), (4.4, 0.35), "Cooling", .5),
             ((5.25, 0.6), (5.3, 1.7), "Weathering & erosion", .5),
             ((5.1, 2.2), (3.9, 3.3), "Compaction & cementation", .5),
             ((2.3, 3.35), (1.0, 2.2), "Heat & pressure", .5),
             ((0.9, 1.7), (1.0, 0.6), "Melting", .5),
             ((4.5, 0.6), (1.7, 1.75), "Heat & pressure", .5),
             ((1.7, 1.95), (4.5, 1.95), "Weathering & erosion", .5)]
    LW, LH = 1.7, 0.38
    labels = []
    for p0, p1, txt, t in edges:
        g.arrow(p0, p1)
        labels.append((p0[0] + t * (p1[0] - p0[0]), p0[1] + t * (p1[1] - p0[1]), txt))
    for cx, cy, txt in labels:
        g.box(cx, cy, LW, LH, txt if key else "", key, bold=False, pt=8.5, edge=HAIR, lw=0.6)
    for k, (x, y, name, printed) in nodes.items():
        g.box(x, y, BW, BH, name if (printed or key) else "", key and not printed, lw=1.0)
    wordbank(g, 4.08, W, [["igneous rock", "sedimentary rock", "metamorphic rock", "cooling", "melting"],
                          ["weathering & erosion", "compaction & cementation", "heat & pressure"]],
             "Terms may be used more than once.")
    return g

# ---------------------------------------------------------------- Bowen's
def bowen(key):
    """Slide 23: temperature bar, the two series, the low-temperature minerals, and the
    composition column, in the slide's words."""
    W, H = 6.2, 4.55
    g = Fig(W, H)
    g.text(0.38, 0.14, "HOTTER", 7.5, True, LABEL); g.text(0.38, 0.3, "~1200 °C", 7.5, False, LABEL)
    g.arrow((0.38, 0.42), (0.38, 3.55), LABEL, 1.2)
    g.text(0.38, 3.68, "COOLER", 7.5, True, LABEL); g.text(0.38, 3.84, "~650 °C", 7.5, False, LABEL)
    g.text(1.75, 0.14, "DISCONTINUOUS", 7.5, True, LABEL)
    g.text(1.75, 0.3, "Mineral type changes", 7, False, LABEL)
    g.text(3.75, 0.14, "CONTINUOUS", 7.5, True, LABEL)
    g.text(3.75, 0.3, "Plagioclase changes", 7, False, LABEL)
    BH = 0.36
    disc = [("Olivine", 0.65), ("Pyroxene", 1.12), ("Amphibole", 1.59), ("Biotite", 2.06)]
    for i, (m, y) in enumerate(disc):
        g.box(1.75, y, 1.3, BH, m if key else "", key)
        if i: g.arrow((1.75, disc[i - 1][1] + BH / 2), (1.75, y - BH / 2))
    g.box(3.75, 0.65, 1.6, 0.46, "Calcium-rich\nplagioclase" if key else "", key, pt=8.5)
    g.box(3.75, 2.0, 1.6, 0.46, "Sodium-rich\nplagioclase" if key else "", key, pt=8.5)
    g.arrow((3.75, 0.88), (3.75, 1.77))
    low = [("Potassium feldspar", 2.92), ("Muscovite", 3.37), ("Quartz", 3.82)]
    g.arrow((1.75, 2.06 + BH / 2), (2.45, 2.92 - BH / 2)); g.arrow((3.75, 2.23), (3.05, 2.92 - BH / 2))
    for i, (m, y) in enumerate(low):
        g.box(2.75, y, 1.7, BH, m if key else "", key)
        if i: g.arrow((2.75, low[i - 1][1] + BH / 2), (2.75, y - BH / 2))
    comp = [("Ultramafic", 0.42, 1.05), ("Mafic", 1.05, 1.65), ("Intermediate", 1.65, 2.3),
            ("Felsic", 2.3, 4.0)]
    for name, y0, y1 in comp:
        g.box(5.55, (y0 + y1) / 2, 1.15, y1 - y0, name if key else "", key, pt=8.5)
    wordbank(g, 4.28, W, [["olivine", "pyroxene", "amphibole", "biotite", "muscovite", "quartz",
                           "potassium feldspar"],
                          ["calcium-rich plagioclase", "sodium-rich plagioclase", "ultramafic", "mafic",
                           "intermediate", "felsic"]])
    return g

# ---------------------------------------------------------------- Mohs
def mohs(key):
    """Slide 6's table: hardness printed, mineral to write."""
    mins = ["Talc", "Gypsum", "Calcite", "Fluorite", "Apatite",
            "Orthoclase", "Quartz", "Topaz", "Corundum", "Diamond"]
    W, H = 6.2, 2.05
    g = Fig(W, H)
    for half in range(2):
        x0 = 0.02 + half * 3.14
        g.box(x0 + 0.3, 0.17, 0.6, 0.3, "1–5" if half == 0 else "6–10", pt=8, fill="#EDF0E5", edge=HAIR, lw=0.6)
        g.box(x0 + 1.8, 0.17, 2.4, 0.3, "Mineral", pt=8, fill="#EDF0E5", edge=HAIR, lw=0.6)
        for i in range(5):
            y = 0.5 + i * 0.34
            n = half * 5 + i
            g.box(x0 + 0.3, y, 0.6, 0.34, str(n + 1), bold=False, pt=9, edge=HAIR, lw=0.6)
            g.box(x0 + 1.8, y, 2.4, 0.34, mins[n] if key else "", key, pt=9, edge=HAIR, lw=0.6)
    return g

# ---------------------------------------------------------------- ID keys
def id_key(root, yes, no, bank, key):
    rows = max(len(yes), len(no))
    W, H = 6.2, 1.15 + rows * 0.55 + 0.45
    g = Fig(W, H)
    g.box(W / 2, 0.25, 2.0, 0.4, root)
    for side, (cx, label, items) in enumerate(((1.55, "YES", yes), (4.65, "NO", no))):
        g.arrow((W / 2 + (-0.6 if side == 0 else 0.6), 0.45), (cx, 0.72))
        g.box(cx, 0.88, 0.7, 0.3, label, pt=8.5)
        for i, (clue, ans) in enumerate(items):
            y = 1.45 + i * 0.55
            g.box(cx - 0.62, y, 1.66, 0.42, clue, bold=False, pt=8, edge=HAIR, lw=0.6)
            g.arrow((cx + 0.21, y), (cx + 0.43, y))
            g.box(cx + 0.92, y, 0.98, 0.42, ans if key else "", key, pt=8.5)
    wordbank(g, H - 0.2, W, [bank])
    return g

sed = lambda k: id_key("VISIBLE GRAINS?",
    [("Gravel-sized, rounded", "Conglomerate"), ("Gravel-sized, angular", "Breccia"),
     ("Sand-sized grains", "Sandstone")],
    [("Fine mud + thin layers", "Shale"), ("Fizzes in dilute acid", "Limestone"),
     ("Black + plant material", "Coal")],
    ["conglomerate", "breccia", "sandstone", "shale", "limestone", "coal"], k)
met = lambda k: id_key("FOLIATION VISIBLE?",
    [("Fine + flat split", "Slate"), ("Silky sheen", "Phyllite"), ("Visible mica", "Schist"),
     ("Light/dark bands", "Gneiss")],
    [("Fizzes in dilute acid", "Marble"), ("Hard, quartz-rich,\nscratches glass", "Quartzite")],
    ["slate", "phyllite", "schist", "gneiss", "marble", "quartzite"], k)

# ---------------------------------------------------------------- two branches
def branch2(root, branches, leaves, key):
    """One root, two branches, two leaves under each - the builder's flowchart shape,
    drawn wide enough to hold the slide's full wording. The student copy prints only
    the root, as the builder's flowchart does."""
    W, H = 6.2, 2.15
    g = Fig(W, H)
    g.box(W / 2, 0.22, 2.1, 0.38, root)
    for b, cx in enumerate((1.55, 4.65)):
        g.arrow((W / 2 + (-0.5 if b == 0 else 0.5), 0.41), (cx, 0.66))
        g.box(cx, 0.85, 2.6, 0.38, branches[b] if key else "", key)
        for j in range(2):
            y = 1.38 + j * 0.5
            g.box(cx, y, 2.9, 0.42, leaves[2 * b + j] if key else "", key, bold=False, pt=8.5)
        g.d.line([px(cx), px(1.04), px(cx), px(1.17)], fill=rgb(LABEL), width=3)
    return g

FLOWS = {
    "geo_u03_s18_intrusive_extrusive": ("IGNEOUS ROCK", ["INTRUSIVE", "EXTRUSIVE"],
        ["Cools inside Earth.", "Usually has larger crystals.",
         "Cools at the surface.", "Usually has smaller crystals."]),
    "geo_u03_s39_contact_regional": ("METAMORPHISM", ["CONTACT METAMORPHISM", "REGIONAL METAMORPHISM"],
        ["Nearby magma heats the rock.", "The change is mostly local.",
         "Heat and pressure affect a large area,", "often during mountain building."]),
}

# ---------------------------------------------------------------- chains
def chain(steps, blank, key, caption=None, desc_pt=7.5):
    """A left-to-right sequence. steps = [(name, desc)]. `blank` is "name" or "desc":
    which half the student writes. A step whose name starts with "=" is printed in
    both copies (the starting rock, say)."""
    n = len(steps)
    W = 6.2
    gap = 0.26
    bw = (W - 0.04 - gap * (n - 1)) / n
    nh, dh = 0.36, 0.62
    H = 0.06 + nh + dh + 0.06 + (0.3 if caption else 0)
    g = Fig(W, H)
    for i, (name, desc) in enumerate(steps):
        x0 = 0.02 + i * (bw + gap)
        cx = x0 + bw / 2
        fixed = name.startswith("=")
        name = name.lstrip("=")
        show_name = key or fixed or blank != "name"
        show_desc = key or fixed or blank != "desc"
        g.box(cx, 0.06 + nh / 2, bw, nh, name if show_name else "",
              key and blank == "name" and not fixed, pt=9)
        g.box(cx, 0.06 + nh + dh / 2, bw, dh, desc if show_desc else "",
              key and blank == "desc" and not fixed, bold=False, pt=desc_pt, edge=HAIR, lw=0.6)
        if i:
            g.arrow((x0 - gap + 0.03, 0.06 + nh / 2), (x0 - 0.02, 0.06 + nh / 2))
    if caption:
        y = H - 0.15
        g.arrow((0.4, y), (W - 0.4, y), LABEL, 0.8)
        g.text(W / 2, y - 0.0, "  " + caption + "  ", 7.5, True, LABEL)
        # white knockout behind the caption so the arrow does not run through it
        f = F("Bold", 7.5); tw = g.d.textlength("  " + caption + "  ", font=f) / DPI
        g.d.rectangle((px(W / 2 - tw / 2), px(y - 0.08), px(W / 2 + tw / 2), px(y + 0.08)), fill=rgb(WHITE))
        g.text(W / 2, y, caption, 7.5, True, LABEL)
    return g

def foliation(key):
    W, H = 6.2, 1.85
    g = Fig(W, H)
    rnd = random.Random(7)
    for side, (x0, title) in enumerate(((0.25, "BEFORE"), (3.45, "AFTER DIRECTED PRESSURE"))):
        pw, ph, y0 = 2.5, 1.2, 0.38
        g.text(x0 + pw / 2, 0.14, title, 7.5, True, LABEL)
        g.d.rectangle((px(x0), px(y0), px(x0 + pw), px(y0 + ph)), outline=rgb(LABEL), width=3)
        for _ in range(70):
            cx, cy = x0 + 0.12 + rnd.random() * (pw - 0.24), y0 + 0.1 + rnd.random() * (ph - 0.2)
            ang = rnd.random() * math.pi if side == 0 else rnd.uniform(-0.08, 0.08)
            L = 0.16
            g.d.line([px(cx - L / 2 * math.cos(ang)), px(cy - L / 2 * math.sin(ang)),
                      px(cx + L / 2 * math.cos(ang)), px(cy + L / 2 * math.sin(ang))],
                     fill=rgb(INK), width=5)
        if side == 1:
            for ax in (x0 + 0.6, x0 + 1.25, x0 + 1.9):
                g.arrow((ax, 0.24), (ax, y0 - 0.03), LABEL, 1.0, 0.07)
                g.arrow((ax, y0 + ph + 0.15), (ax, y0 + ph + 0.03), LABEL, 1.0, 0.07)
    g.arrow((2.9, 0.98), (3.3, 0.98), LABEL, 1.2)
    return g

CHAINS = {
    "geo_u03_s12_sandstone_chain": dict(steps=[
        ("Weathering", "Breaks rock\ninto pieces."), ("Erosion", "Moves the\npieces."),
        ("Deposition", "Drops the pieces\nin layers."), ("Compaction", "Weight squeezes\nthe grains together."),
        ("Cementation", "Minerals grow\nbetween grains\nand glue them.")], blank="name"),
    "geo_u03_s14_journey": dict(steps=[
        ("Granite", "Rock we\nstart with"), ("Sediment", "Weathering,\nerosion, and\ntransport"),
        ("Sandstone", "Quartz-rich sand\ndeposits and\ncements"), ("Quartzite", "Heat and\npressure")],
        blank="name"),
    "geo_u03_s16_basalt_schist": dict(steps=[
        ("Basalt", "Igneous\nparent rock"), ("Metamorphism", "Minerals change\nand can line up"),
        ("Chlorite schist", "One possible\nresult")], blank="name"),
    "geo_u03_s29_sed_forms": dict(steps=[
        ("Weathering", "Breaks rock down"), ("Erosion", "Moves the pieces"),
        ("Deposition", "Drops the pieces"), ("Lithification", "Makes sediment\ninto rock")],
        blank="name"),
    "geo_u03_s30_sediment_rock": dict(steps=[
        ("=Loose sediment", "Open spaces\nbetween grains"), ("Compaction", "Grains pack\ncloser together"),
        ("Cementation", "Minerals join\nthe grains")], blank="desc"),
    "geo_u03_s42_grade": dict(steps=[
        ("=Shale", "Parent rock"), ("Slate", "Very fine /\nflat split"), ("Phyllite", "Fine /\nsilky sheen"),
        ("Schist", "Visible mica\nflakes"), ("Gneiss", "Light and\ndark bands")],
        blank="name", caption="INCREASING GRADE"),
}

for name, fn in (("geo_u03_rock_cycle", rock_cycle), ("geo_u03_bowens", bowen), ("geo_u03_s06_mohs", mohs),
                 ("geo_u03_sed_id_key", sed), ("geo_u03_met_id_key", met)):
    for k in (False, True):
        fn(k).save(os.path.join(OUT, f"{name}{'_key' if k else ''}.png"))
for k in (False, True):
    for name, args in FLOWS.items():
        branch2(*args, k).save(os.path.join(OUT, f"{name}{'_key' if k else ''}.png"))
    foliation(k).save(os.path.join(OUT, f"geo_u03_s40_foliation{'_key' if k else ''}.png"))
    for name, kw in CHAINS.items():
        chain(key=k, **kw).save(os.path.join(OUT, f"{name}{'_key' if k else ''}.png"))
print("ok")
