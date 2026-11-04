#!/usr/bin/env python3
"""Build the Physics Unit 2 Day 2 written test (versions A, B, C) and its worked teacher keys.

    python3 templates/test/build_u2_written.py OUTDIR

Student copy: two pages, equations at the top of each page, an open box under every problem for the
paper work. Key: every problem worked step by step in the key-handwriting face
(standards/ANSWER_KEYS.md). Every number comes from u2_data.py, solved in code and re-solved by a
different method in verify_u2.py.
"""
import math, os, sys, tempfile
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
for p in (HERE, os.path.join(REPO, "templates"), os.path.join(REPO, "templates", "quiz"), os.path.join(REPO, "scripts")):
    sys.path.insert(0, p)
import u2_data as D                                                    # noqa: E402
import u2_equations as EQ                                              # noqa: E402
import vectors_22 as V                                                 # noqa: E402
import build_quiz_docx as Q                                            # noqa: E402
import build_quiz_worked_keys as WK                                    # noqa: E402
from key_solution import solution_image                                # noqa: E402
from _shull_name import document_name                                  # noqa: E402
from _shull_docx import (T, Palette, borders, para, fix_widths, gap, one_cell, equation_bar,  # noqa: E402
                         work_box)

KEY_INK = Q.KEY_INK
TITLE = "UNIT 2 · MOTION IN TWO DIMENSIONS"
CODE = "U02 / S02.1–S02.3"
TOTAL = sum(D.POINTS)
DIRECTIONS = ("Show all of your work on this paper. Write the givens, the equation you use, and units on every answer. "
              "Round final answers to two significant figures. Up is +y, g = 9.8 m/s², and air resistance is ignored. "
              "Angles may be given as a compass direction or on the 0–360° scale starting at east and running counterclockwise.")
VEC_EQ = [{"plain": "Rx = R cos(angle)"}, {"plain": "Ry = R sin(angle)"}, {"plain": "tan(angle) = Ry / Rx"},
          {"plain": "R² = Rx² + Ry²"}, {"plain": "Rx = Ax + Bx"}, {"plain": "Ry = Ay + By"}]
PROJ_EQ = [{"plain": "vix = vi cos(angle)"}, {"plain": "viy = vi sin(angle)"}, {"plain": "Δx = vix t"},
           {"plain": "Δy = viy t − ½ g t²"}, {"plain": "vy = viy − g t"}, {"plain": "t = [−b ± √(b² − 4ac)] / 2a"}]


def header(doc, pal, sub, key=False):
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [5.6, 1.9])
    a, b = t.rows[0].cells
    for c in (a, b):
        borders(c, pal.display, sz=18, edges=("bottom",))
    para(a, "SHULL SCIENCE  ·  JAMES A. GARFIELD LOCAL SCHOOLS", 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    para(a, TITLE, 15, bold=True, color=pal.ink)
    para(a, sub + ("  ·  TEACHER KEY" if key else ""), 8.5, bold=True, color=KEY_INK if key else pal.label, caps_track=True)
    p = para(b, CODE, 9, bold=True, color=pal.accent, caps_track=True, first=True)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT


def fields_row(doc, pal):
    gap(doc, 4)
    t = doc.add_table(rows=1, cols=4)
    fix_widths(t, [3.0, 1.7, 1.3, 1.5])
    for c, lab in zip(t.rows[0].cells, ("NAME", "DATE", "PERIOD", f"SCORE        / {TOTAL}")):
        borders(c, pal.hair, sz=6)
        para(c, lab, 8.5, bold=True, color=pal.label, caps_track=True, first=True)
        c.paragraphs[0].paragraph_format.space_after = Pt(9)


def q_block(doc, pal, n, pts, text, box_in):
    gap(doc, 6)
    c = one_cell(doc)
    para(c, f"{n}.   {pts} pts", 8, bold=True, color=pal.accent, caps_track=True, first=True)
    para(c, text, 10.5)
    work_box(c, "", pal, box_in, 7.2)


def page_break(doc):
    """A one-point paragraph that carries the break, so a full page cannot spill a blank one."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = Pt(1)
    r = p.add_run(); r.font.size = Pt(1); r.add_break(WD_BREAK.PAGE)


def student(L, out):
    pal = Palette("physics")
    w = D.WRITTEN[L]
    doc = Q.new_doc(pal, f"SHULL SCIENCE / PHYSICS / UNIT 02 / TEST {L} / DAY 2 WRITTEN")
    header(doc, pal, f"UNIT 2 TEST  ·  DAY 2 WRITTEN  ·  VERSION {L}")
    fields_row(doc, pal)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, DIRECTIONS, 8.5, color=pal.ink, first=True)
    gap(doc, 3)
    EQ.vector_block(doc, pal)
    q_block(doc, pal, 1, D.POINTS[0], w["q1"]["text"], 2.0)
    q_block(doc, pal, 2, D.POINTS[1], w["q2"]["text"], 3.4)
    page_break(doc)
    EQ.projectile_block(doc, pal)
    q_block(doc, pal, 3, D.POINTS[2], w["q3"]["text"], 1.1)
    q_block(doc, pal, 4, D.POINTS[3], w["q4"]["text"], 1.9)
    q_block(doc, pal, 5, D.POINTS[4], w["q5"]["text"], 2.85)
    Q.finish(doc, out)


# ---- key steps --------------------------------------------------------------------------

def p3_steps(spec, s):
    h, vx = spec["h"], spec["vx"]
    return [
        WK.say("Vertical first. It leaves level, so viy = 0, and it falls the height h."),
        WK.row(f"h = ½ g t^{{2}}   so   t =", {"sqrt": f"2({h:g}) / 9.8"}, f"= {s['t']:.2f} s"),
        WK.ans("t =", f"{D.sf(s['t'])} s"),
        WK.say("Now use that same time horizontally.", "arrow"),
        WK.row(f"Δx = vix t = ({vx:.1f} m/s)({s['t']:.2f} s) = {s['x']:.2f} m"),
        WK.ans("Δx =", f"{D.sf(s['x'])} m"),
    ]


def p4_steps(spec, s):
    v, a = spec["v"], spec["ang"]
    return [
        WK.row(f"vix = {v:g} cos {a:g}° = {s['vx']:.2f} m/s", "     ", f"viy = {v:g} sin {a:g}° = {s['vy']:.2f} m/s"),
        WK.say("Level ground, so it lands at the same height it started."),
        WK.row("t =", {"frac": ["2 viy", "g"]}, "=", {"frac": [f"2({s['vy']:.2f})", "9.8"]}, f"= {s['t']:.2f} s"),
        WK.ans("t =", f"{D.sf(s['t'])} s"),
        WK.row(f"R = vix t = ({s['vx']:.2f} m/s)({s['t']:.2f} s) = {s['R']:.1f} m"),
        WK.ans("R =", f"{D.sf(s['R'])} m"),
    ]


def p5_steps(spec, s):
    y0, v, a = spec["y0"], spec["v"], spec["ang"]
    root = math.sqrt(s["disc"])
    other = (-s["b"] - root) / (2 * s["a"])
    return [
        WK.row(f"vix = {v:g} cos {a:g}° = {s['vx']:.2f} m/s", "     ", f"viy = {v:g} sin {a:g}° = {s['vy']:.2f} m/s"),
        WK.ans("(a)", f"vix = {s['vx']:.1f} m/s,  viy = {s['vy']:.1f} m/s"),
        WK.say("It lands on the ground, 15 m below the start, so Δy = −" + f"{y0:g} m. Up is +y.".replace("15", f"{y0:g}")
               if False else f"The arrow lands on the ground, {y0:g} m below the start, so Δy = −{y0:g} m (up is +y)."),
        WK.row(f"Δy = viy t − ½ g t^{{2}}   →   −{y0:g} = {s['vy']:.2f} t − 4.9 t^{{2}}"),
        WK.row(f"4.9 t^{{2}} − {s['vy']:.2f} t − {y0:g} = 0", note="a = 4.9,  b = " + f"−{s['vy']:.2f},  c = −{y0:g}"),
        WK.row("b^{2} − 4ac =", f"({s['b']:.2f})^{{2}} − 4(4.9)(−{y0:g}) = {s['disc']:.1f}".replace("-", "−")),
        WK.row("square root =", {"sqrt": f"{s['disc']:.1f}"}, f"= {root:.2f}"),
        WK.row("t =", {"frac": [f"{s['vy']:.2f} + {root:.2f}", "2(4.9)"]}, f"= {s['t']:.2f} s"),
        WK.say(f"The other root is {other:.2f} s, before the launch, so reject it.", "arrow"),
        WK.ans("(b) t =", f"{D.sf(s['t'])} s"),
        WK.row(f"Δx = vix t = ({s['vx']:.2f} m/s)({s['t']:.2f} s) = {s['x']:.1f} m"),
        WK.ans("(c) Δx =", f"{D.sf(s['x'])} m"),
    ]


RUBRIC = {
    1: "1 Rx and Ry set up with signs · 1 Pythagoras · 1 R with units · 1 angle by tan · 1 direction named.",
    2: "1 each vector resolved (2) · 1 Rx and Ry sums · 1 R with units · 1 angle · 1 direction from the signs.",
    3: "1 vertical setup (viy = 0) · 1 time · 1 horizontal equation · 1 distance with units · 1 same time used.",
    4: "1 components · 1 time equation · 1 time · 1 range equation · 1 range with units · 1 same time used.",
    5: "2 launch components · 1 Δy = −y0 · 2 quadratic and its root · 1 positive root kept · 1 distance with units · 1 same time used.",
}


def worked_key(L, out, tmp):
    pal = Palette("physics")
    w, s = D.WRITTEN[L], D.solve_written(L)
    doc = Q.new_doc(pal, f"SHULL SCIENCE / PHYSICS / UNIT 02 / TEST {L} / DAY 2 WRITTEN / TEACHER KEY")
    header(doc, pal, f"UNIT 2 TEST  ·  DAY 2 WRITTEN  ·  VERSION {L}", key=True)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "East is +x and north is +y. Up is +y. Keep the extra digits until the last step, then round to two "
            "significant figures. Points per problem: " + ", ".join(f"Q{i + 1} {p}" for i, p in enumerate(D.POINTS)) + f" · total {TOTAL}.",
         8.5, color=pal.ink, first=True)
    q1 = V.solve_q4(w["q1"])
    q2 = V.solve_q5(w["q2"])
    items = [
        (1, w["q1"]["text"], WK.q4_steps({**w["q1"], "kind": "velocity"}, q1)),
        (2, w["q2"]["text"], WK.q5_steps(w["q2"], q2)),
        (3, w["q3"]["text"], p3_steps(w["q3"], s["q3"])),
        (4, w["q4"]["text"], p4_steps(w["q4"], s["q4"])),
        (5, w["q5"]["text"], p5_steps(w["q5"], s["q5"])),
    ]
    for n, text, steps in items:
        gap(doc, 6)
        c = one_cell(doc, protect=True); borders(c, pal.hair)
        para(c, f"{n}.   {D.POINTS[n - 1]} pts", 8, bold=True, color=pal.accent, caps_track=True, first=True)
        para(c, text, 9.5, color=pal.ink)
        png, _ = solution_image({"prompt": f"{L}{n}", "steps": steps}, os.path.join(tmp, f"{L}q{n}.png"), width_in=7.0, size=22)
        WK.picture(c, png, 7.0)
        para(c, "Points: " + RUBRIC[n], 7.5, color=pal.label)
    gap(doc, 6)
    c = one_cell(doc); borders(c, pal.hair)
    para(c, "GRADING NOTES", 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    para(c, "Common errors: adding magnitudes instead of Pythagoras (Q1) · dropping a component’s sign (Q2) · using sine "
            "for the horizontal part · forgetting that Δy is negative when the landing is below the launch (Q5) · using "
            "t = 2viy/g when the landing height differs (Q5) · rounding the time before using it for the distance.", 8.5, color=pal.ink)
    para(c, "Judgment call for you: a student who rounds t early can land a few tenths of a meter off in Q3–Q5. "
            "The key keeps the extra digits; decide whether to accept the rounded value.", 8.5, color=pal.ink)
    Q.finish(doc, out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    V.VERSIONS_Q2 = {}
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        for L in D.VERS:
            for key in (False, True):
                p = os.path.join(outdir, document_name("Test", ["2.1", "2.2", "2.3"], 2, version=L, key=key, descriptor="Day 2 Written"))
                (worked_key(L, p, tmp) if key else student(L, p))
                n = Q.pages(p)
                limit = 3 if key else 2
                ok = n <= limit and (key or n == 2)
                print("ok " if ok else "BAD", n, "page", os.path.basename(p))
                bad += not ok
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
