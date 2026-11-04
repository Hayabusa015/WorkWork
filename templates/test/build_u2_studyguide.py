#!/usr/bin/env python3
"""Build the Physics Unit 2 study guide and its worked teacher key.

    python3 templates/test/build_u2_studyguide.py OUTDIR

Two parts. Part 1: eleven conceptual questions, answered in the student's own words on ruled lines.
Part 2: five problems of the kinds on the Day 2 written test (a 90 degree sum, a sum at other angles,
a horizontal launch, an angled launch on level ground, an angled launch from a height), with new
numbers. Printed on regular paper (approved by Matt for this guide), so each problem has an open
box. Numbers come from u2_data.py (GUIDE), re-solved in verify_u2.py.
"""
import math, os, sys, tempfile
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
for p in (HERE, os.path.join(REPO, "templates"), os.path.join(REPO, "templates", "quiz"), os.path.join(REPO, "scripts")):
    sys.path.insert(0, p)
import u2_data as D                                                    # noqa: E402
import vectors_22 as V                                                 # noqa: E402
import build_quiz_docx as Q                                            # noqa: E402
import build_quiz_worked_keys as WK                                    # noqa: E402
import build_u2_written as W                                           # noqa: E402
from key_solution import solution_image                                # noqa: E402
from _shull_name import document_name                                  # noqa: E402
from _shull_docx import (Palette, borders, para, fix_widths, gap, one_cell, equation_bar,  # noqa: E402
                         work_box, rule_lines)

KEY_INK = Q.KEY_INK
G = D.GUIDE
S = D.solve_guide()

CONCEPT = [
    ("What is the difference between a vector and a scalar? Give one example of each.",
     "A vector has a magnitude and a direction (velocity, displacement, force). A scalar has a magnitude only (speed, distance, mass, time)."),
    ("Explain how to write “30° north of west” on the 0–360° scale.",
     "The scale starts at east and runs counterclockwise. West is 180°, and north of west is less than 180°, so subtract: 180° − 30° = 150°."),
    ("What does a negative angle mean? Which way does it turn?",
     "It is measured clockwise from east, so −60° points the same way as 300°. Add 360° to convert it."),
    ("How do the signs of Rx and Ry tell you the direction of a resultant?",
     "They give the quadrant. Rx + is east and − is west; Ry + is north and − is south. Positive x with negative y is south of east."),
    ("Two perpendicular vectors are added. How do you find the size of the resultant, and how do you find its direction?",
     "Size: Pythagorean theorem, R² = Rx² + Ry². Direction: tan(angle) = Ry / Rx, then use the signs to name the quadrant."),
    ("Why do you split vectors into x and y components before adding vectors that are not perpendicular?",
     "Components along the same axis can be added directly, so adding the x parts and the y parts gives Rx and Ry. The magnitudes alone cannot be added because the directions differ."),
    ("Why do the horizontal and vertical motions of a projectile not affect each other?",
     "Gravity acts only vertically, so it changes only the vertical velocity. They are independent and share the same time."),
    ("What stays constant during a projectile’s flight? What changes?",
     "The horizontal velocity stays constant (no horizontal acceleration). The vertical velocity changes by 9.8 m/s every second."),
    ("At the highest point of a projectile’s path, what are its vertical velocity and its acceleration?",
     "vy = 0 at the top, but the acceleration is still 9.8 m/s² downward. Gravity never stops acting."),
    ("A ball is dropped and a second ball is thrown horizontally from the same height at the same instant. Which lands first? Explain.",
     "They land at the same time. The fall depends only on the height, and the horizontal speed does not change it."),
    ("A ball is thrown at an angle from a cliff and lands below the launch height. What changes compared with a throw that lands at the launch height?",
     "It stays in the air longer and travels farther. t = 2viy/g no longer works, so you solve Δy = viy t − ½ g t² (a quadratic) and keep the positive root."),
]

PROBLEMS = [
    ("VECTORS  ·  PERPENDICULAR", f"A cyclist rides south at {abs(G['p1']['y']):.1f} m/s while a wind blows her east at {G['p1']['x']:.1f} m/s. "
     "Find her resultant velocity: magnitude and direction."),
    ("VECTORS  ·  NOT PERPENDICULAR", "A plane flies at 210 km/h toward 15° north of east. A wind blows toward 55° north of west at 70 km/h. "
     "Find the plane’s resultant velocity relative to the ground: magnitude and direction."),
    ("PROJECTILE  ·  HORIZONTAL LAUNCH", f"A ball rolls off a platform {G['p3']['h']} m high at {G['p3']['vx']} m/s. "
     "Find (a) the time in the air and (b) the horizontal distance from the platform to where it lands."),
    ("PROJECTILE  ·  LEVEL GROUND", f"A softball is hit at {G['p4']['v']:.0f} m/s at {G['p4']['ang']:.0f}° above the horizontal and is caught at the same height. "
     "Find (a) the time in the air and (b) the horizontal distance it travels."),
    ("PROJECTILE  ·  FROM A HEIGHT", f"A guard on a wall {G['p5']['y0']:.0f} m above the ground fires an arrow at {G['p5']['v']:.0f} m/s at {G['p5']['ang']:.0f}° above the "
     "horizontal at a target on the ground. Find (a) the arrow’s horizontal and vertical launch velocities, (b) the time until it lands, and (c) how far "
     "from the wall it lands."),
]
BOX = [1.5, 2.6, 1.7, 2.3, 3.4]


def part_label(doc, pal, text, sub):
    gap(doc, 8)
    c = one_cell(doc, 7.5, protect=True)
    borders(c, pal.display, sz=12, edges=("bottom",))
    para(c, text, 9, bold=True, color=pal.accent, caps_track=True, first=True)
    para(c, sub, 8.5, color=pal.label)
    c.paragraphs[0].paragraph_format.keep_with_next = True


def tight_rules(cell, n, hexval):
    """Ruled answer lines at 4 pt spacing, so eleven questions fit on one page."""
    rule_lines(cell, n, hexval)
    for p in cell.paragraphs[-n:]:
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = Pt(13)


def student(out):
    pal = Palette("physics")
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / STUDY GUIDE")
    W.header(doc, pal, "UNIT 2 STUDY GUIDE  ·  VECTORS & PROJECTILE MOTION")
    gap(doc, 4)
    t = doc.add_table(rows=1, cols=3)
    fix_widths(t, [3.6, 2.2, 1.7])
    for c, lab in zip(t.rows[0].cells, ("NAME", "DATE", "PERIOD")):
        borders(c, pal.hair, sz=6)
        para(c, lab, 8.5, bold=True, color=pal.label, caps_track=True, first=True)
        c.paragraphs[0].paragraph_format.space_after = Pt(9)
    part_label(doc, pal, "PART 1  ·  CONCEPTUAL REVIEW", "Answer each question in your own words. One or two sentences is enough.")
    for i, (q, _) in enumerate(CONCEPT, 1):
        gap(doc, 1)
        c = one_cell(doc, 7.5, protect=True)
        p = para(c, f"{i}.  {q}", 9.5, first=True)
        tight_rules(c, 2, pal.hair)
    W.page_break(doc)
    part_label(doc, pal, "PART 2  ·  PROBLEMS", "The same kinds of problems you will see on the written test. Show the givens, the equation, and units. "
               "Up is +y, g = 9.8 m/s², and air resistance is ignored.")
    gap(doc, 3)
    W.EQ.vector_block(doc, pal)
    gap(doc, 2)
    W.EQ.projectile_block(doc, pal)
    for i, ((label, text), box) in enumerate(zip(PROBLEMS, BOX), 1):
        if i == 3:
            W.page_break(doc)
        gap(doc, 6)
        c = one_cell(doc, 7.5, protect=True)
        para(c, f"{i}.   {label}", 8, bold=True, color=pal.accent, caps_track=True, first=True)
        para(c, text, 10)
        work_box(c, "", pal, box, 7.2)
    Q.finish(doc, out)


# ---- key --------------------------------------------------------------------------------

def key_doc(out, tmp):
    pal = Palette("physics")
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / STUDY GUIDE / TEACHER KEY")
    W.header(doc, pal, "UNIT 2 STUDY GUIDE  ·  VECTORS & PROJECTILE MOTION", key=True)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "East is +x and north is +y. Up is +y. Keep the extra digits until the last step, then round to two significant figures. "
            "Part 1 answers are model responses; accept any answer that makes the same point.", 8.5, color=pal.ink, first=True)
    gap(doc, 5)
    c = one_cell(doc, protect=True); borders(c, pal.hair)
    para(c, "PART 1  ·  MODEL ANSWERS", 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    for i, (q, a) in enumerate(CONCEPT, 1):
        para(c, f"{i}.  {q}", 8.5, color=pal.ink)
        para(c, a, 8.5, color=KEY_INK)
    g, s = G, S
    p1 = {**g["p1"], "kind": "velocity"}
    steps = [WK.q4_steps(p1, V.solve_q4(p1)), WK.q5_steps(g["p2"], V.solve_q5(g["p2"])),
             W.p3_steps(g["p3"], s["p3"]), W.p4_steps(g["p4"], s["p4"]), W.p5_steps(g["p5"], s["p5"])]
    for i, ((label, text), st) in enumerate(zip(PROBLEMS, steps), 1):
        gap(doc, 6)
        c = one_cell(doc, protect=True); borders(c, pal.hair)
        para(c, f"PART 2  ·  {i}.   {label}", 8, bold=True, color=pal.accent, caps_track=True, first=True)
        para(c, text, 9.5, color=pal.ink)
        png, _ = solution_image({"prompt": f"sg{i}", "steps": st}, os.path.join(tmp, f"sg{i}.png"), width_in=7.0, size=21)
        WK.picture(c, png, 7.0)
    Q.finish(doc, out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    V.VERSIONS_Q2 = {}
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        for key in (False, True):
            p = os.path.join(outdir, document_name("Study_Guide", ["2.1", "2.2", "2.3"], 2, key=key))
            key_doc(p, tmp) if key else student(p)
            nn = Q.pages(p)
            ok = nn <= (4 if key else 3)
            print("ok " if ok else "BAD", nn, "page", os.path.basename(p))
            bad += not ok
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
