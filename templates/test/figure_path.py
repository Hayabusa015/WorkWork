#!/usr/bin/env python3
"""A cleaner version of the 'ball tossed from a platform, which point is ...' figure questions.

    python3 templates/test/figure_path.py OUTDIR

Writes `path_figure.png` (the figure alone, for a quiz platform) and a one-page student sheet and teacher key.

What is different from the usual version of this figure:
  * the points are numbered 1-4, so a point never shares a letter with an answer choice (A-D);
  * a dashed line marks the launch height, so "same height as the toss" is something you can see;
  * point 3 sits exactly at the launch height and point 2 exactly at the top, both computed from the physics;
  * every question has one defensible answer, and the key says why.
Colour from brand/tokens.json; Archivo only; the figure survives grayscale (outlines and labels, not hue).
"""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
for p in (HERE, os.path.join(REPO, "templates"), os.path.join(REPO, "templates", "quiz"), os.path.join(REPO, "scripts")):
    sys.path.insert(0, p)
import build_quiz_s22_docx as Q                                            # noqa: E402
import build_u2_written as W                                           # noqa: E402
from _shull_docx import T, Palette, borders, para, gap, one_cell, fix_widths, hexof   # noqa: E402

G, H0, V0, ANG = 9.8, 6.0, 14.0, 45.0
VX, VY = V0 * math.cos(math.radians(ANG)), V0 * math.sin(math.radians(ANG))


def pos(t):
    return VX * t, H0 + VY * t - 0.5 * G * t * t


def vel(t):
    return VX, VY - G * t


t_top = VY / G
t_same = 2 * VY / G
t_land = (VY + math.sqrt(VY * VY + 2 * G * H0)) / G
POINTS = {1: t_top * 0.4, 2: t_top, 3: t_same, 4: t_land - 0.12}


def checks():
    """The facts the answers rely on, computed rather than assumed."""
    assert abs(vel(POINTS[2])[1]) < 1e-9
    assert abs(pos(POINTS[3])[1] - H0) < 1e-9
    assert abs(math.hypot(*vel(POINTS[3])) - V0) < 1e-9
    speeds = {k: math.hypot(*vel(t)) for k, t in POINTS.items()}
    assert max(speeds, key=speeds.get) == 4
    assert min(speeds, key=speeds.get) == 2
    assert all(abs(vel(t)[0] - VX) < 1e-9 for t in POINTS.values())


def font(px, bold=True):
    f = ImageFont.truetype(os.path.expanduser("~/.fonts/Archivo[wdth,wght].ttf"), px)
    try:
        f.set_variation_by_axes([700 if bold else 400, 100])
    except Exception:
        pass
    return f


def figure(path):
    S = 3
    W_, H_ = 1500 * S, 740 * S
    im = Image.new("RGB", (W_, H_), "white")
    d = ImageDraw.Draw(im)
    pal = Palette("physics")
    ink, label, accent = "#" + hexof(pal.ink), "#" + hexof(pal.label), "#" + hexof(pal.accent)
    ox, oy = 150 * S, 700 * S                       # ground-left origin
    sx, sy = 46 * S, 44 * S                         # px per metre
    X = lambda x: ox + x * sx
    Y = lambda y: oy - y * sy
    # ground and platform
    d.line([(X(-2.6), Y(0)), (X(29), Y(0))], fill=ink, width=3 * S)
    d.rectangle([X(-2.4), Y(H0), X(0), Y(0)], outline=ink, width=3 * S)
    for k in range(0, int(29 * 1.0), 2):                # ground hatch
        d.line([(X(k), Y(0)), (X(k - 0.8), Y(-0.7))], fill=label, width=2 * S)
    # dashed launch-height line
    x = X(0)
    while x < X(26.5):
        d.line([(x, Y(H0)), (x + 14 * S, Y(H0))], fill=label, width=2 * S)
        x += 26 * S
    d.text((X(13.5), Y(H0) + 18 * S), "launch height", font=font(26 * S, False), fill=label, anchor="mm")
    # path
    pts = [(X(pos(t)[0]), Y(pos(t)[1])) for t in [i * t_land / 300 for i in range(301)]]
    d.line(pts, fill=ink, width=4 * S, joint="curve")
    # launch arrow and the ball at the toss
    ax, ay = X(0), Y(H0)
    d.ellipse([ax - 11 * S, ay - 11 * S, ax + 11 * S, ay + 11 * S], fill=ink)
    # numbered points
    for k, t in POINTS.items():
        px, py = X(pos(t)[0]), Y(pos(t)[1])
        d.ellipse([px - 9 * S, py - 9 * S, px + 9 * S, py + 9 * S], fill="white", outline=ink, width=3 * S)
        off = {1: (-34, -22), 2: (0, -40), 3: (34, -22), 4: (34, 6)}[k]
        tx, ty = px + off[0] * S, py + off[1] * S
        d.ellipse([tx - 20 * S, ty - 20 * S, tx + 20 * S, ty + 20 * S], fill="white", outline=accent, width=3 * S)
        d.text((tx, ty), str(k), font=font(28 * S), fill=ink, anchor="mm")
    d.text((X(-1.2), Y(H0 / 2)), "platform", font=font(22 * S, False), fill=label, anchor="mm")
    im = im.resize((W_ // S, H_ // S), Image.LANCZOS)
    im.save(path, dpi=(300, 300))
    return path


QUESTIONS = [
    ("At which point is the vertical component of the ball’s velocity zero?",
     ["Point 1", "Point 2", "Point 3", "Point 4"], 1,
     "Point 2, the top of the path. The ball has stopped rising and has not started falling, so vy = 0 there."),
    ("At which point is the ball’s speed about equal to the speed at which it was tossed?",
     ["Point 1", "Point 2", "Point 3", "Point 4"], 2,
     "Point 3. It is back at the launch height (the dashed line), so it has the same speed as the toss, just pointing downward at the same angle."),
    ("At which point is the ball moving the fastest?",
     ["Point 1", "Point 2", "Point 3", "Point 4"], 3,
     "Point 4, the lowest point. The ball has been speeding up since the top, and it is below the launch height."),
    ("At which point is the horizontal component of the ball’s velocity greatest?",
     ["Point 1", "Point 2", "Point 3", "It is the same at all four points"], 3,
     "The same everywhere. Nothing pushes sideways, so vx never changes (air resistance ignored)."),
]
LET = "ABCD"


def sheet(out, key=False):
    pal = Palette("physics")
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / S02.3 / PATH FIGURE" + (" / TEACHER KEY" if key else ""))
    W.header(doc, pal, "PROJECTILE PATH  ·  FIGURE QUESTIONS", key=key)
    if not key:
        W.TOTAL = len(QUESTIONS)
        W.fields_row(doc, pal)
    gap(doc, 4)
    c = one_cell(doc, 7.4); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "A ball is tossed up and outward from a platform and follows the path shown. The dashed line is the height "
            "of the toss. Ignore air resistance. Circle the best answer.", 9, color=pal.ink, first=True)
    gap(doc, 4)
    c = one_cell(doc, 7.4)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(FIG, width=Inches(6.6))
    for i, (stem, ch, ans, why) in enumerate(QUESTIONS, 1):
        gap(doc, 6)
        c = one_cell(doc, 7.4, protect=True)
        para(c, f"{i}.   {stem}", 10.5, bold=True, first=True)
        t = c.add_table(rows=1, cols=4)
        fix_widths(t, [1.7, 1.7, 1.7, 2.1])
        for k, (cell, text) in enumerate(zip(t.rows[0].cells, ch)):
            mark = key and k == ans
            para(cell, f"{LET[k]}.  {text}" + ("   ✔" if False else ""), 10.5, bold=mark,
                 color=Q.KEY_INK if mark else pal.ink, first=True)
        if key:
            para(c, why, 9, color=Q.KEY_INK)
    Q.finish(doc, out)


FIG = None


def main():
    global FIG
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    checks()
    FIG = figure(os.path.join(outdir, "path_figure.png"))
    bad = 0
    for key in (False, True):
        p = os.path.join(outdir, "Path Figure Questions" + (" Key" if key else "") + ".docx")
        sheet(p, key)
        n = Q.pages(p)
        print("ok " if n == 1 else "BAD", n, "page", os.path.basename(p))
        bad += n != 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
