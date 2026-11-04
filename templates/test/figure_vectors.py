#!/usr/bin/env python3
"""Picture-choice questions on the correct way to draw a vector (Physics S2.1).

    python3 templates/test/figure_vectors.py OUTDIR

Five questions, four drawings each (lettered A-D inside the image). Every wrong drawing is a mistake
students actually make: the arrowhead at the wrong end, the angle measured from the wrong axis, a
negative angle turned the wrong way, vectors added tail to tail, a length that is not to scale. The key
says what each wrong drawing got wrong. Writes `vectors_q<N>_<letter>.png` for each drawing (for a quiz
platform), a two-page student sheet and a teacher key. Colour from brand/tokens.json; Archivo only.
"""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
for p in (HERE, os.path.join(REPO, "templates"), os.path.join(REPO, "templates", "quiz"), os.path.join(REPO, "scripts")):
    sys.path.insert(0, p)
import build_quiz_docx as Q                                            # noqa: E402
import build_u2_written as W                                           # noqa: E402
from _shull_docx import Palette, borders, para, gap, one_cell, fix_widths, tight_cells, hexof   # noqa: E402

S = 3
CW, CH = 520, 460
PAL = Palette("physics")
INK, LABEL, ACCENT, HAIR = ("#" + hexof(PAL.ink), "#" + hexof(PAL.label), "#" + hexof(PAL.accent), "#" + hexof(PAL.hair))
LET = "ABCD"


def font(px, bold=True):
    f = ImageFont.truetype(os.path.expanduser("~/.fonts/Archivo[wdth,wght].ttf"), px * S)
    try:
        f.set_variation_by_axes([700 if bold else 400, 100])
    except Exception:
        pass
    return f


class Panel:
    def __init__(self, letter, origin=(260, 235)):
        self.im = Image.new("RGB", (CW * S, CH * S), "white")
        self.d = ImageDraw.Draw(self.im)
        self.o = origin
        self.letter = letter

    def P(self, deg, r, o=None):
        ox, oy = o or self.o
        return (ox + r * math.cos(math.radians(deg)), oy - r * math.sin(math.radians(deg)))

    def line(self, a, b, color=INK, w=5, dash=False):
        if not dash:
            self.d.line([(a[0] * S, a[1] * S), (b[0] * S, b[1] * S)], fill=color, width=w * S)
            return
        L = math.dist(a, b)
        n = int(L // 16)
        for i in range(n):
            t0, t1 = i / n, (i + 0.55) / n
            self.d.line([((a[0] + (b[0] - a[0]) * t0) * S, (a[1] + (b[1] - a[1]) * t0) * S),
                         ((a[0] + (b[0] - a[0]) * t1) * S, (a[1] + (b[1] - a[1]) * t1) * S)], fill=color, width=w * S)

    def axes(self):
        ox, oy = self.o
        self.line((ox - 215, oy), (ox + 215, oy), HAIR, 2)
        self.line((ox, oy - 200), (ox, oy + 190), HAIR, 2)
        f = font(26)
        for txt, (x, y) in {"E": (ox + 232, oy), "W": (ox - 232, oy), "N": (ox, oy - 214), "S": (ox, oy + 206)}.items():
            self.d.text((x * S, y * S), txt, font=f, fill=LABEL, anchor="mm")

    def arrow(self, a, b, head_at="end", color=INK, w=6, head=26):
        self.line(a, b, color, w)
        tip, base = (b, a) if head_at == "end" else (a, b)
        ang = math.atan2(tip[1] - base[1], tip[0] - base[0])
        p1 = (tip[0] - head * math.cos(ang - 0.38), tip[1] - head * math.sin(ang - 0.38))
        p2 = (tip[0] - head * math.cos(ang + 0.38), tip[1] - head * math.sin(ang + 0.38))
        self.d.polygon([(tip[0] * S, tip[1] * S), (p1[0] * S, p1[1] * S), (p2[0] * S, p2[1] * S)], fill=color)

    def text(self, xy, s, size=30, bold=True, color=INK):
        self.d.text((xy[0] * S, xy[1] * S), s, font=font(size, bold), fill=color, anchor="mm")

    def arc(self, a0, a1, r=70, label=None):
        """Arc from math angle a0 to a1 (degrees), going the short way unless a1 < a0 is given explicitly."""
        n = 60
        pts = [self.P(a0 + (a1 - a0) * i / n, r) for i in range(n + 1)]
        self.d.line([(x * S, y * S) for x, y in pts], fill=ACCENT, width=4 * S)
        if label:
            x, y = self.P((a0 + a1) / 2, r + 34)
            self.text((x, y), label, 30, True, ACCENT)

    def dot(self, xy, r=7):
        self.d.ellipse([(xy[0] - r) * S, (xy[1] - r) * S, (xy[0] + r) * S, (xy[1] + r) * S], fill=INK)

    def badge(self):
        x, y = 36, 36
        self.d.ellipse([(x - 24) * S, (y - 24) * S, (x + 24) * S, (y + 24) * S], fill="white", outline=INK, width=3 * S)
        self.text((x, y), self.letter, 30, True, INK)

    def save(self, path):
        self.badge()
        im = self.im.resize((CW, CH), Image.LANCZOS)
        im.save(path, dpi=(300, 300))
        return path


def vec_panel(letter, theta, label, head="end", arc=None, tail=None, length=165, ang_label=None):
    p = Panel(letter)
    p.axes()
    o = tail or p.o
    tip = p.P(theta, length, o)
    p.arrow(o, tip, head_at=head)
    if arc:
        p.arc(arc[0], arc[1], 70, arc[2])
    lx, ly = p.P(theta, length + 42, o)               # the magnitude sits just past the arrowhead
    p.text((lx, ly), label, 30)
    p.dot(p.o)
    return p


def sum_panel(letter, kind):
    p = Panel(letter, origin=(110, 340))
    ox, oy = p.o
    A = (ox + 165, oy)
    if kind == "good":                       # A, then B from the tip of A, R from the tail of A to the tip of B
        B = (A[0], A[1] - 110); p.arrow((ox, oy), A); p.arrow(A, B); p.arrow((ox, oy), B, color=ACCENT)
    elif kind == "tailtail":                 # both from the origin; R from tip to tip
        B = (ox, oy - 110); p.arrow((ox, oy), A); p.arrow((ox, oy), B); p.arrow(A, B, color=ACCENT)
    elif kind == "backward":                 # tip to tail, but R points back to the start
        B = (A[0], A[1] - 110); p.arrow((ox, oy), A); p.arrow(A, B); p.arrow(B, (ox, oy), color=ACCENT)
    else:                                    # B drawn pointing the wrong way
        B = (A[0], A[1] + 110); p.arrow((ox, oy), A); p.arrow(A, B); p.arrow((ox, oy), B, color=ACCENT)
    p.text((ox + 82, oy + 30), "A", 32)
    if kind == "tailtail":
        p.text((ox - 28, oy - 55), "B", 32)
    else:
        p.text((A[0] + 30, (A[1] + B[1]) / 2), "B", 32)
    rx, ry = {"good": (ox + 62, oy - 70), "tailtail": ((A[0] + ox) / 2 + 40, oy - 62), "backward": (ox + 62, oy - 70), "wrong": (ox + 62, oy + 72)}[kind]
    p.text((rx, ry), "R", 32, True, ACCENT)
    p.dot((ox, oy))
    return p


def scale_panel(letter, length):
    p = Panel(letter, origin=(60, 200))
    p.text((260, 40), "reference:  4 m/s", 28, False, LABEL)
    p.arrow((60, 90), (60 + 70, 90), color=LABEL, w=5)
    p.arrow((60, 300), (60 + length, 300))
    p.text((60 + length / 2, 350), "8 m/s", 30)
    return p


# ---- the five questions -----------------------------------------------------------------
Q_DEFS = []


def build_panels():
    qs = []
    # 1. 40 m/s at 35 degrees south of west (math angle 215); correct = B
    qs.append(("Which drawing correctly shows a vector of 40 m/s at 35° south of west?", [
        (lambda L: vec_panel(L, 145, "40 m/s", arc=(180, 145, "35°")),
         "Wrong side. It points north of west, not south of west."),
        (lambda L: vec_panel(L, 215, "40 m/s", arc=(180, 215, "35°")), None),
        (lambda L: vec_panel(L, 235, "40 m/s", arc=(270, 235, "35°")),
         "Angle measured from the wrong axis. 35° from south is “35° west of south,” a different direction."),
        (lambda L: vec_panel(L, 215, "40 m/s", head="start", arc=(180, 215, "35°")),
         "The arrowhead is at the tail end, so it points toward the origin (up and to the right). The arrowhead shows the direction."),
    ], 1))
    # 2. 250 degrees on the 0-360 scale; correct = D
    qs.append(("Which drawing correctly shows a vector at 250° on the 0–360° scale (measured counterclockwise from east)?", [
        (lambda L: vec_panel(L, 290, "250°"), "290° is the mirror image: 250° measured clockwise instead of counterclockwise."),
        (lambda L: vec_panel(L, 160, "250°"), "160° is 250° − 90°, measured from the wrong starting axis."),
        (lambda L: vec_panel(L, 70, "250°"), "70° is 250° − 180°, the opposite direction."),
        (lambda L: vec_panel(L, 250, "250°"), None),
    ], 3))
    # 3. -60 degrees; correct = A
    qs.append(("Which drawing correctly shows a vector with a direction of −60°?", [
        (lambda L: vec_panel(L, 300, "−60°"), None),
        (lambda L: vec_panel(L, 60, "−60°"), "The negative sign was ignored. +60° turns counterclockwise, above the axis."),
        (lambda L: vec_panel(L, 240, "−60°"), "240° is 60° past west. −60° is measured clockwise from east, not from west."),
        (lambda L: vec_panel(L, 120, "−60°"), "120° is 60° counterclockwise from north, not 60° clockwise from east."),
    ], 0))
    # 4. adding A + B; correct = C
    qs.append(("Vector A points east and vector B points north. Which drawing correctly adds them tip to tail and shows the resultant R?", [
        (lambda L: sum_panel(L, "tailtail"), "Tail to tail. The resultant must start at the tail of the first vector and end at the tip of the last, "
                                            "not run from one tip to the other."),
        (lambda L: sum_panel(L, "backward"), "R points backward. It starts at the tip of B and ends at the start; the arrowhead belongs at the tip of B."),
        (lambda L: sum_panel(L, "good"), None),
        (lambda L: sum_panel(L, "wrong"), "B was drawn pointing south. B points north, so it must go up from the tip of A."),
    ], 2))
    # 5. scale; correct = B (140 px)
    qs.append(("Vector A is 4 m/s and is drawn to scale as shown. Which drawing shows a vector B of 8 m/s drawn to the same scale?", [
        (lambda L: scale_panel(L, 35), "Too short. Half of A’s length would be 2 m/s."),
        (lambda L: scale_panel(L, 140), None),
        (lambda L: scale_panel(L, 70), "The same length as A, so it shows 4 m/s, not 8 m/s."),
        (lambda L: scale_panel(L, 280), "Too long. Four times A’s length would be 16 m/s."),
    ], 1))
    return qs


def write_pngs(outdir):
    qs = build_panels()
    out = []
    for n, (stem, opts, ans) in enumerate(qs, 1):
        files = []
        for k, (fn, why) in enumerate(opts):
            files.append(fn(LET[k]).save(os.path.join(outdir, f"vectors_q{n}_{LET[k]}.png")))
        out.append((stem, files, [w for _, w in opts], ans))
    return out


def sheet(path, data, key=False):
    doc = Q.new_doc(PAL, "SHULL SCIENCE / PHYSICS / UNIT 02 / S02.1 / DRAWING VECTORS" + (" / TEACHER KEY" if key else ""))
    W.header(doc, PAL, "DRAWING VECTORS  ·  PICTURE QUESTIONS", key=key)
    if not key:
        W.TOTAL = len(data)
        W.fields_row(doc, PAL)
    gap(doc, 4)
    c = one_cell(doc, 7.5); borders(c, PAL.display, sz=18, edges=("left",))
    para(c, "Look at all four drawings before you choose. East is to the right and north is up. Circle the letter of the "
            "drawing that is drawn correctly.", 9, color=PAL.ink, first=True)
    for n, (stem, files, whys, ans) in enumerate(data, 1):
        if n == 4 and not key:
            W.page_break(doc)
        gap(doc, 7)
        c = one_cell(doc, 7.5, protect=True)
        para(c, f"{n}.   {stem}", 10.5, bold=True, first=True)
        t = c.add_table(rows=1, cols=4)
        fix_widths(t, [1.84] * 4)
        tight_cells(t, top=20, bottom=20, left=20, right=20)
        for k, (cell, f) in enumerate(zip(t.rows[0].cells, files)):
            borders(cell, "#000000"[1:] if False else PAL.hair, sz=6)
            cell.paragraphs[0].add_run().add_picture(f, width=Inches(1.5 if key else 1.76))
            if key and k == ans:
                borders(cell, PAL.accent, sz=18)
        if key:
            para(c, f"Answer: {LET[ans]}", 9.5, bold=True, color=Q.KEY_INK)
            for k, w_ in enumerate(whys):
                if w_:
                    para(c, f"{LET[k]}.  {w_}", 8.5, color=Q.KEY_INK)
    Q.finish(doc, path)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    data = write_pngs(outdir)
    bad = 0
    for key in (False, True):
        p = os.path.join(outdir, "Drawing Vectors Questions" + (" Key" if key else "") + ".docx")
        sheet(p, data, key)
        n = Q.pages(p)
        ok = n == (2 if not key else 2)
        print("ok " if ok else "BAD", n, "page", os.path.basename(p))
        bad += not ok
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
