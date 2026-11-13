#!/usr/bin/env python3
"""Build the Physics S2.3 "Trebuchet" Gizmo activity (student sheet and key), one page each.

    python3 templates/activity/build_gizmo_trebuchet.py OUTDIR

A short completion activity for a day the teacher is out: students design a trebuchet in the
Explore Learning Gizmo, copy the launch readouts, try to hit the target, and answer a few short
questions. Nothing is calculated. Layout helpers come from build_gizmo_monkey.py.
"""
import os, sys
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_gizmo_monkey as M                                           # noqa: E402
from _shull_name import document_name                                    # noqa: E402
from _shull_docx import (Palette, borders, para, fix_widths, gap, one_cell, rule_lines,  # noqa: E402
                         trim_tail, schema_order)

KEY_INK = M.KEY_INK
SETUP = [
    "Open the Gizmo: Explore Learning › Trebuchet. Stay on the DESIGN tab.",
    "Leave every setting as you found it and click Launch test.",
    "Copy the Launch angle and Initial speed that appear under the buttons.",
]


def header(doc, pal, key=False):
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [5.6, 1.8])
    a, b = t.rows[0].cells
    for c in (a, b):
        borders(c, pal.display, sz=18, edges=("bottom",))
    para(a, "SHULL SCIENCE  ·  JAMES A. GARFIELD LOCAL SCHOOLS", 7.5, bold=True, color=pal.accent,
         caps_track=True, first=True)
    para(a, "TREBUCHET TARGET", 16, bold=True, color=pal.ink)
    para(a, "PROJECTILE MOTION GIZMO  ·  ABOUT 20 MINUTES" + ("  ·  TEACHER KEY" if key else ""), 8.5,
         bold=True, color=KEY_INK if key else pal.label, caps_track=True)
    p = para(b, "U02 / S02.3", 9, bold=True, color=pal.accent, caps_track=True, first=True)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT


def body(doc, pal, key=False):
    gap(doc, 6)
    c = one_cell(doc, 7.4); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "SET UP", 8.5, bold=True, color=pal.accent, caps_track=True, first=True)
    for i, s in enumerate(SETUP, 1):
        para(c, f"{i}.  {s}", 10)
    para(c, "This is a completion activity. Fill in what you see and answer each part. "
            "Close counts.", 9, color=pal.label)

    M.part(doc, pal, 1, "TRY THREE DESIGNS", [
        "Row 1 is the starting design. For rows 2 and 3, change ONE setting each time (counterweight, "
        "arm length, prong angle, anything), click Launch test, and copy the readouts."])
    kr = [["any", "any"]] * 3 if key else None
    M.grid(doc, pal, ["TRY", "WHAT I CHANGED", "LAUNCH ANGLE", "INITIAL SPEED"],
           [["1", "", "", ""], ["2", "", "", ""], ["3", "", "", ""]], [0.6, 3.2, 1.8, 1.8],
           [["starting design", "", ""]] * 0 or None)
    q = one_cell(doc, 7.4)
    para(q, "Which setting changed the launch angle the most?   ______________", 10, first=True)
    if key:
        para(q, "Likely the prong angle, or the sling length. Accept any setting the student’s own "
                "table supports.", 9, color=KEY_INK)
    para(q, "Which setting changed the initial speed the most?   ______________", 10)
    if key:
        para(q, "Likely the counterweight or the long arm length. Accept any setting the table "
                "supports.", 9, color=KEY_INK)

    M.part(doc, pal, 2, "HIT THE TARGET", [
        "Click the LAUNCH tab. The target is listed on the screen (range, height). Use the design "
        "that you think will work and launch. Try up to three times; stop if you hit it."])
    M.grid(doc, pal, ["SHOT", "DID IT HIT?  (circle)", "WHERE IT LANDED  (short, long, on target)"],
           [["1", "yes   no", ""], ["2", "yes   no", ""], ["3", "yes   no", ""]], [0.9, 2.8, 3.7])
    q = one_cell(doc, 7.4)
    para(q, "What did you change between shots, and did it help?", 10, first=True)
    if key:
        para(q, "Open-ended. Full credit for any honest description. Air slows the shot a little, so the "
                "Gizmo will not match the no-air equations exactly.", 9, color=KEY_INK)
    else:
        rule_lines(q, 2, pal.hair)

    M.part(doc, pal, 3, "CONNECT IT TO CLASS", [
        "The Gizmo gives a launch angle and an initial speed. Those are the two numbers you use to split "
        "a launch into a horizontal speed and a vertical speed."])
    q = one_cell(doc, 7.4)
    para(q, "A steeper launch angle sends more of the speed:   upward    sideways     (circle)", 10, first=True)
    if key:
        para(q, "Upward. That is what keeps the shot in the air longer.", 9, color=KEY_INK)
    para(q, "During the flight, the speed that stays constant is the ________________ velocity.", 10)
    if key:
        para(q, "horizontal (vx). Nothing pushes sideways once it is released (ignoring air).", 9,
             color=KEY_INK)


def build(out, key=False):
    pal = Palette("physics")
    doc = M.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / S02.3 / TREBUCHET TARGET"
                    + (" / TEACHER KEY" if key else ""))
    header(doc, pal, key)
    if not key:
        M.fields_row(doc, pal)
    else:
        gap(doc, 4)
        c = one_cell(doc, 7.4); borders(c, pal.hair)
        para(c, "Grade for completion only: every blank filled, every question circled or answered. "
                "Readouts differ by design, so there are no expected numbers. The target and its "
                "limits are whatever the chosen scenario shows.", 8.5, color=pal.label, first=True)
    body(doc, pal, key)
    trim_tail(doc)
    schema_order(doc)
    doc.save(out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    bad = 0
    for key in (False, True):
        p = os.path.join(outdir, document_name("Activity", ["2.3"], 2, key=key))
        build(p, key)
        n = M.pages(p)
        print("ok" if n == 1 else "FAIL", n, "page", p)
        bad += n != 1
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
