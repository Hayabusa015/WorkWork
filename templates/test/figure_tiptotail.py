#!/usr/bin/env python3
"""One picture-choice question on the tip-to-tail method, in the format of the 'which image shows R = C + d − A' item.

    python3 templates/test/figure_tiptotail.py OUTDIR

One image: a reference strip with vectors A, B and C drawn separately, then four numbered drawings (a 2 x 2 grid).
The question: which drawing correctly uses the tip-to-tail method for R = A + B − C? Each drawing carries the
resultant R as a dashed arrow. The wrong drawings are the mistakes students make: C added instead of subtracted,
R drawn backward, and A reversed. Also writes the four drawings as separate images, a one-page student sheet and a
teacher key. Colour from brand/tokens.json; Archivo only.
"""
import math, os, sys
from PIL import Image, ImageDraw
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
for p in (HERE, os.path.join(REPO, "templates"), os.path.join(REPO, "templates", "quiz"), os.path.join(REPO, "scripts")):
    sys.path.insert(0, p)
import figure_vectors as FV                                            # noqa: E402
import build_quiz_s22_docx as Q                                            # noqa: E402
import build_u2_written as W                                           # noqa: E402
from _shull_docx import para, gap, one_cell                            # noqa: E402

S = FV.S
A, B, C = (4, 0), (2, 3), (-3, 1)
NEG = lambda v: (-v[0], -v[1])
STEM = "Which of the following images illustrates the correct use of the “tip-to-tail” method for the vector operation R = A + B − C ?"


class Board(FV.Panel):
    def __init__(self, w, h):
        self.im = Image.new("RGB", (w * S, h * S), "white")
        self.d = ImageDraw.Draw(self.im)
        self.o, self.letter, self.size = (0, 0), "", (w, h)

    def head(self, base, tip, color=FV.ACCENT, size=26):
        ang = math.atan2(tip[1] - base[1], tip[0] - base[0])
        p1 = (tip[0] - size * math.cos(ang - 0.38), tip[1] - size * math.sin(ang - 0.38))
        p2 = (tip[0] - size * math.cos(ang + 0.38), tip[1] - size * math.sin(ang + 0.38))
        self.d.polygon([(tip[0] * S, tip[1] * S), (p1[0] * S, p1[1] * S), (p2[0] * S, p2[1] * S)], fill=color)

    def dashed_arrow(self, a, b, color=FV.ACCENT, w=5):
        self.line(a, b, color, w, dash=True)
        self.head(a, b, color)


def label_side(a, b, off=24):
    """A point beside the middle of a-b, on the side away from the page's top-left."""
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    nx, ny = (b[1] - a[1]), -(b[0] - a[0])
    n = math.hypot(nx, ny) or 1
    return mx + off * nx / n, my + off * ny / n


def draw_chain(board, cell, steps, rdir="forward", u=34):
    """Draw vectors tip to tail inside the cell (x0, y0, w, h), centred, with a dashed resultant R."""
    x0, y0, w, h = cell
    pts = [(0.0, 0.0)]
    for _, v in steps:
        pts.append((pts[-1][0] + v[0], pts[-1][1] + v[1]))
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    px = [(x0 + w / 2 + (p[0] - cx) * u, y0 + h / 2 - (p[1] - cy) * u) for p in pts]
    for i, (name, _) in enumerate(steps):
        board.arrow(px[i], px[i + 1], w=5, head=22)
        lx, ly = label_side(px[i], px[i + 1], 24)
        board.text((lx, ly), name, 30)
    a, b = (px[0], px[-1]) if rdir == "forward" else (px[-1], px[0])
    board.dashed_arrow(a, b)
    q = (px[0][0] + 0.72 * (px[-1][0] - px[0][0]), px[0][1] + 0.72 * (px[-1][1] - px[0][1]))
    lx, ly = label_side(px[0], px[-1], 0)
    nx, ny = (px[-1][1] - px[0][1]), -(px[-1][0] - px[0][0])
    n = math.hypot(nx, ny) or 1
    board.text((q[0] + 30 * nx / n, q[1] + 30 * ny / n), "R", 30, True, FV.ACCENT)
    board.dot(px[0], 6)


OPTIONS = [
    # (steps, rdir, why)
    ([("A", A), ("B", B), ("C", C)], "forward",
     "C was added instead of subtracted. The −C step needs an arrow pointing opposite to C."),
    ([("A", A), ("B", B), ("−C", NEG(C))], "backward",
     "The vectors are laid out correctly, but R points backward. The resultant runs from the start (tail of the first vector) to the tip of the last."),
    ([("A", A), ("B", B), ("−C", NEG(C))], "forward", None),
    ([("−A", NEG(A)), ("B", B), ("−C", NEG(C))], "forward",
     "A was reversed. R = A + B − C adds A, so A keeps its direction; only C is reversed."),
]
ANS = 2


def reference_strip(board, y0=0, h=230):
    board.text((560, y0 + 26), "vectors", 28, False, FV.LABEL)
    for v, name, o in ((A, "A", (110, y0 + 150)), (B, "B", (520, y0 + 190)), (C, "C", (860, y0 + 160))):
        tip = (o[0] + v[0] * 40, o[1] - v[1] * 40)
        board.dot(o, 6)
        board.arrow(o, tip, w=5, head=24)
        lx, ly = label_side(o, tip, 26)
        board.text((lx, ly), name, 34)


def build(outdir):
    W_, H_ = 1120, 1010
    img = Board(W_, H_)
    reference_strip(img)
    top = 250
    cw, ch = 560, 380
    cells = [(0, top, cw, ch), (cw, top, cw, ch), (0, top + ch, cw, ch), (cw, top + ch, cw, ch)]
    # frame
    img.line((0, top), (W_, top), FV.INK, 3); img.line((0, top + ch), (W_, top + ch), FV.INK, 3)
    img.line((0, top + 2 * ch), (W_, top + 2 * ch), FV.INK, 3); img.line((cw, top), (cw, top + 2 * ch), FV.INK, 3)
    img.line((0, top), (0, top + 2 * ch), FV.INK, 3); img.line((W_, top), (W_, top + 2 * ch), FV.INK, 3)
    for k, (steps, rdir, _) in enumerate(OPTIONS):
        x0, y0, w, h = cells[k]
        draw_chain(img, cells[k], steps, rdir)
        bx, by = x0 + 34, y0 + 34
        img.d.ellipse([(bx - 24) * S, (by - 24) * S, (bx + 24) * S, (by + 24) * S], fill="white", outline=FV.INK, width=3 * S)
        img.text((bx, by), str(k + 1), 30)
    full = img.im.resize((W_, 250 + 2 * ch), Image.LANCZOS).crop((0, 0, W_, 250 + 2 * ch))
    path = os.path.join(outdir, "tiptotail_question.png")
    full.save(path, dpi=(300, 300))
    # the four drawings on their own
    singles = []
    for k, (steps, rdir, _) in enumerate(OPTIONS):
        b = Board(cw, ch)
        draw_chain(b, (0, 0, cw, ch), steps, rdir)
        bx, by = 34, 34
        b.d.ellipse([(bx - 24) * S, (by - 24) * S, (bx + 24) * S, (by + 24) * S], fill="white", outline=FV.INK, width=3 * S)
        b.text((bx, by), str(k + 1), 30)
        p = os.path.join(outdir, f"tiptotail_option_{k + 1}.png")
        b.im.resize((cw, ch), Image.LANCZOS).save(p, dpi=(300, 300))
        singles.append(p)
    return path, singles


def sheet(path, image, key=False):
    pal = FV.PAL
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / S02.1 / TIP TO TAIL" + (" / TEACHER KEY" if key else ""))
    W.header(doc, pal, "TIP-TO-TAIL  ·  PICTURE QUESTION", key=key)
    if not key:
        W.TOTAL = 1
        W.fields_row(doc, pal)
    gap(doc, 8)
    c = one_cell(doc, 7.5, protect=True)
    para(c, "1.   " + STEM, 10.5, bold=True, first=True)
    p = c.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(image, width=Inches(5.6 if key else 6.4))
    if key:
        para(c, f"Answer: {ANS + 1}", 10, bold=True, color=Q.KEY_INK)
        para(c, "Tip to tail: start the first vector at the start point, start each next vector at the tip of the one before it, and for a "
                "minus sign draw that vector reversed (same length, opposite direction). R runs from the start to the tip of the last vector. "
                "The order of the steps can change; the arrows cannot.", 9, color=Q.KEY_INK)
        for k, (_, _, why) in enumerate(OPTIONS):
            if why:
                para(c, f"{k + 1}.  {why}", 9, color=Q.KEY_INK)
    Q.finish(doc, path)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(out, exist_ok=True)
    image, singles = build(out)
    bad = 0
    for key in (False, True):
        p = os.path.join(out, "Tip to Tail Question" + (" Key" if key else "") + ".docx")
        sheet(p, image, key)
        n = Q.pages(p)
        print("ok " if n == 1 else "BAD", n, "page", os.path.basename(p))
        bad += n != 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
