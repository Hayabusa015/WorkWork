#!/usr/bin/env python3
"""Build the one-page grading sheet for the Unit 2 Day 2 written test (versions A, B and C together).

    python3 templates/test/build_u2_gradesheet.py OUTDIR

For each version and problem: the checkpoint values to look for in a student's work, the final answer, and the
range to accept. Pairs with the worked keys (`Unit 2 Test A/B/C Key - Day 2 Written`). Every number is read from
u2_data.py (solved in code, re-solved in verify_u2.py); nothing is typed here.
"""
import math, os, sys
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
for p in (HERE, os.path.join(REPO, "templates"), os.path.join(REPO, "templates", "quiz"), os.path.join(REPO, "scripts")):
    sys.path.insert(0, p)
import u2_data as D                                                    # noqa: E402
import vectors_22 as V                                                 # noqa: E402
import build_quiz_docx as Q                                            # noqa: E402
import build_u2_written as W                                           # noqa: E402
from _shull_name import document_name                                  # noqa: E402
from _shull_docx import Palette, borders, para, fix_widths, gap, one_cell, tight_cells, no_split   # noqa: E402

KEY_INK = Q.KEY_INK
MINUS = "−"


def f(x, nd=2):
    return f"{x:.{nd}f}".replace("-", MINUS)


def rng(x):
    """The 2-s.f. answer plus or minus one in its last place: 3.9 -> 3.8 to 4.0; 150 -> 140 to 160."""
    step = 10 ** (math.floor(math.log10(abs(x))) - 1)
    dec = max(0, 1 - math.floor(math.log10(abs(x))))
    base = round(x / step) * step
    return f"{base - step:.{dec}f}–{base + step:.{dec}f}"


def direction(th):
    e = V.equivalents(round(th))
    return f"{e['c1']} ({e['deg']})"


def rows(L):
    w, s = D.WRITTEN[L], D.solve_written(L)
    out = []
    q1 = w["q1"]; a = s["q1"]; u = q1["unit"]
    out.append(("1", f"Rx = {f(q1['x'], 1)} {u}, Ry = {f(q1['y'], 1)} {u} (signs)  ·  R² = {a['R'] ** 2:.2f}",
                f"{D.sf(a['R'])} {u}, {direction(a['th'])}", f"R {rng(a['R'])}  ·  angle ±1°"))
    q2 = w["q2"]; b = s["q2"]; u = q2["unit"]
    (ax, ay), (bx, by) = b["parts"]
    out.append(("2", f"A: ({f(ax, 1)}, {f(ay, 1)})  ·  B: ({f(bx, 1)}, {f(by, 1)})  ·  Rx = {f(b['rx'], 1)}, Ry = {f(b['ry'], 1)}",
                f"{D.sf(b['R'])} {u}, {direction(b['th'])}", f"R {rng(b['R'])}  ·  angle ±1°"))
    c = s["q3"]
    out.append(("3", f"t = √(2h/g) = {f(c['t'])} s  ·  Δx = vix t = {f(c['x'], 1)} m",
                f"t = {D.sf(c['t'])} s;  Δx = {D.sf(c['x'])} m", f"t {rng(c['t'])}  ·  Δx {rng(c['x'])}"))
    c = s["q4"]
    out.append(("4", f"vix = {f(c['vx'], 1)}, viy = {f(c['vy'], 1)} m/s  ·  t = 2viy/g = {f(c['t'])} s  ·  R = {f(c['R'], 1)} m",
                f"t = {D.sf(c['t'])} s;  R = {D.sf(c['R'])} m", f"t {rng(c['t'])}  ·  R {rng(c['R'])}"))
    c = s["q5"]
    other = (-c["b"] - math.sqrt(c["disc"])) / (2 * c["a"])
    out.append(("5", f"vix = {f(c['vx'], 1)}, viy = {f(c['vy'], 1)} m/s  ·  Δy = {MINUS}{w['q5']['y0']:g} m  ·  quadratic roots {f(c['t'])} s and {f(other)} s (reject the negative)",
                f"(a) {D.sf(c['vx'])} and {D.sf(c['vy'])} m/s;  (b) {D.sf(c['t'])} s;  (c) {D.sf(c['x'])} m", f"t {rng(c['t'])}  ·  Δx {rng(c['x'])}"))
    return out


def table(doc, pal, L):
    gap(doc, 4)
    c = one_cell(doc, 7.5, protect=True)
    para(c, f"VERSION {L}", 8.5, bold=True, color=pal.accent, caps_track=True, first=True)
    data = rows(L)
    t = c.add_table(rows=1 + len(data) + 1, cols=5)
    fix_widths(t, [0.35, 3.0, 1.95, 1.4, 0.8])
    tight_cells(t, top=25, bottom=25, left=40, right=40)
    for cell, h in zip(t.rows[0].cells, ("Q", "CHECKPOINTS IN THE WORK", "FINAL ANSWER", "ACCEPT", "SCORE / 5")):
        borders(cell, pal.display, sz=8, edges=("bottom",))
        para(cell, h, 7, bold=True, color=pal.label, caps_track=True, first=True)
    for row, (q, chk, fin, acc) in zip(t.rows[1:], data):
        no_split(row)
        for cell in row.cells:
            borders(cell, pal.hair, sz=4, edges=("bottom",))
        para(row.cells[0], q, 9.5, bold=True, first=True)
        para(row.cells[1], chk, 8, first=True)
        para(row.cells[2], fin, 8.5, bold=True, color=KEY_INK, first=True)
        para(row.cells[3], acc, 7.5, first=True)
        para(row.cells[4], "", 9, first=True)
        row.cells[4].paragraphs[0].paragraph_format.space_after = Pt(7)
    last = t.rows[-1]
    para(last.cells[0], "", 8, first=True)
    para(last.cells[1], "", 8, first=True)
    para(last.cells[2], "", 8, first=True)
    para(last.cells[3], "TOTAL", 8, bold=True, color=pal.label, caps_track=True, first=True)
    para(last.cells[4], "/ 25", 9, bold=True, first=True)


def build(path):
    pal = Palette("physics")
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / DAY 2 WRITTEN / GRADE SHEET")
    W.header(doc, pal, "UNIT 2  ·  DAY 2 WRITTEN  ·  GRADE SHEET", key=True)
    gap(doc, 4)
    c = one_cell(doc, 7.5); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "SCORE EACH PROBLEM 0–5", 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    for pt, txt in (("5", "All answers correct; all words and thought process shown."),
                    ("4", "A minor error (a missed negative, one rounding slip); all other work correct, even if the final answer ends up wrong."),
                    ("3", "Correct thought process, but wrong variables or wrong calculations."),
                    ("2", "Started correctly, but the variables and math are incorrect."),
                    ("1", "Variables listed; everything else wrong."),
                    ("0", "No attempt.")):
        p = para(c, "", 8.5)
        from _shull_docx import run
        run(p, f"{pt}   ", 8.5, bold=True, color=KEY_INK)
        run(p, txt, 8.5, color=pal.ink)
    para(c, "Accept: the answer plus or minus one in its last place (3.9 accepts 3.8 to 4.0), and ±1° on angles. A student who rounds early can land "
            "inside that range: still a 5 if the work is complete. Worked solutions: the three keys.", 8, color=pal.label)
    for L in D.VERS:
        table(doc, pal, L)
    Q.finish(doc, path)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    p = os.path.join(outdir, document_name("Test", ["2.1", "2.2", "2.3"], 2, key=True, descriptor="Day 2 Written Grade Sheet"))
    build(p)
    n = Q.pages(p)
    print("ok " if n == 1 else "BAD", n, "page", os.path.basename(p))
    return 0 if n == 1 else 1


if __name__ == "__main__":
    sys.exit(main())
