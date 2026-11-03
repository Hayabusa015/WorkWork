#!/usr/bin/env python3
"""Build the Physics Unit 2 study guide and its worked teacher key.

    python3 templates/test/build_u2_studyguide.py OUTDIR

Four sections (vector basics, adding at 90 degrees, adding at other angles, projectile motion). Each opens with
what the unit covered, then two problems: one simple, one average. Printed on regular paper
(approved by Matt for this guide), so every problem has an open box for the work. The problems
do not repeat the test's. Numbers come from u2_data.py (GUIDE), re-solved in verify_u2.py.
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
from _shull_docx import (Palette, borders, para, run, fix_widths, gap, one_cell, equation_bar,  # noqa: E402
                         work_box, rule_lines)

KEY_INK = Q.KEY_INK
G = D.GUIDE
S = D.solve_guide()
sf, n = D.sf, WK.n

# Each section: the concept statements as fill-ins. "{}" marks a blank; the answers are listed in order.
# One source: the student page prints blanks, the key and the Key Concepts sheet print the same
# sentences completed.
SECTIONS = [
    ("1", "VECTOR BASICS", "S2.1", [
        ("A {} has both a magnitude and a direction. A {} has a magnitude only.", ["vector", "scalar"]),
        ("On the 0–360° scale, angles start at {} and run {}.", ["east", "counterclockwise"]),
        ("A negative angle runs {} from east, so −60° and 300° point the same way.", ["clockwise"]),
        ("In a vector drawing, the {} shows the direction and the {} shows the magnitude.", ["arrowhead", "length"]),
        ("A vector in quadrant III has an x component that is {} and a y component that is {}.", ["negative", "negative"]),
    ]),
    ("2", "ADDING AT 90°", "S2.2", [
        ("Perpendicular vectors are the {} of a right triangle, and the resultant is the {}.", ["legs", "hypotenuse"]),
        ("The size of a resultant at 90° comes from the {} theorem, R² = Rx² + Ry².", ["Pythagorean"]),
        ("The angle comes from tan(angle) = {} ÷ {}.", ["Ry", "Rx"]),
        ("The signs of Rx and Ry decide the {} of the direction, such as south of east.", ["quadrant"]),
        ("Every vector answer needs a magnitude with {} and a direction with a named {}.", ["units", "reference"]),
    ]),
    ("3", "ADDING AT OTHER ANGLES", "S2.2", [
        ("A vector that is not along an axis is first split into {} and {} components.", ["x", "y"]),
        ("Ax = A {}(angle) and Ay = A {}(angle).", ["cos", "sin"]),
        ("To add vectors, add all of the {} parts together and all of the {} parts together.", ["x", "y"]),
        ("Writing each angle on the 0–360° scale makes the {} of the components come out right.", ["signs"]),
        ("Adding three vectors works the same way, with one more {} in each sum.", ["term"]),
    ]),
    ("4", "PROJECTILE MOTION", "S2.3", [
        ("A projectile’s horizontal and vertical motions are {} of each other and share the same {}.", ["independent", "time"]),
        ("Horizontal velocity stays {} because the horizontal acceleration is {}.", ["constant", "zero"]),
        ("At the highest point, vy is {}, but the acceleration is still {} downward.", ["zero", "9.8 m/s²"]),
        ("For a horizontal launch, viy = {}, and the fall time comes from t = {}.", ["0", "√(2h/g)"]),
        ("When the landing height differs from the launch height, solve Δy = viy t − ½ g t² and keep the {} root.", ["positive"]),
    ]),
]


def blank(answer):
    return "_" * max(9, int(len(answer) * 1.5))


def fill_text(template, answers, solved=False):
    """The sentence with its blanks, or with the answers written in."""
    out = template
    for a in answers:
        out = out.replace("{}", a if solved else blank(a), 1)
    return out


def fill_para(cell, number, template, answers, pal, solved=False, size=10, color=None):
    """One numbered statement; when solved, the answers are bold in the accent colour."""
    p = para(cell, "", size)
    run(p, f"{number}.  ", size, bold=True, color=pal.ink)
    parts = template.split("{}")
    for i, part in enumerate(parts):
        run(p, part, size, color=pal.ink)
        if i < len(answers):
            run(p, answers[i] if solved else blank(answers[i]), size, bold=solved, color=color if solved else pal.ink)
    return p


def problems():
    g, s = G, S
    ub = lambda x: f"{x:.1f}"
    p = []
    p.append(("1", "Simple", f"Write {g['s1_p1']['given']}° in two other ways: as a compass direction and as a negative angle.", 0.9))
    p.append(("1", "Average", f"A skater moves at {g['s1_p2']['mag']} m/s at 35° south of west. (a) Write the direction on the 0–360° scale. "
              f"(b) Sketch the vector on axes, labeled. (c) Find the x and y components, with signs.", 1.8))
    p.append(("2", "Simple", f"A hiker walks {ub(g['s2_p1']['x'])} m east and then {ub(g['s2_p1']['y'])} m north. Find the resultant displacement: magnitude and direction.", 1.35))
    p.append(("2", "Average", f"A boat heads north across a river at {ub(g['s2_p2']['y'])} m/s while the current carries it west at {abs(g['s2_p2']['x']):.1f} m/s. "
              "Find the boat’s resultant velocity: magnitude and direction.", 1.5))
    p.append(("3", "Simple", "A plane flies at 150 km/h toward 40° north of east. A wind blows toward 20° south of east at 40 km/h. "
              "Find the plane’s resultant velocity relative to the ground: magnitude and direction.", 2.1))
    p.append(("3", "Average", "A hiker walks 30 m east, then 20 m north, then 25 m toward 45° south of west. "
              "Find the hiker’s resultant displacement: magnitude and direction.", 2.4))
    p.append(("4", "Simple", f"A marble rolls horizontally off a table {g['s4_p1']['h']} m high at {g['s4_p1']['vx']} m/s. "
              "Find (a) the time in the air and (b) the horizontal distance from the table to where it lands.", 1.45))
    p.append(("4", "Average", f"A ball is thrown from the roof of a {g['s4_p2']['y0']:.0f} m building at {g['s4_p2']['v']:.0f} m/s at "
              f"{g['s4_p2']['ang']:.0f}° above the horizontal. Find (a) the time until it hits the ground and (b) how far from the building it lands.", 2.3))
    return p


BOX = {"1.1": 1.2, "1.2": 3.0, "2.1": 2.3, "2.2": 2.9, "3.1": 2.9, "3.2": 3.4, "4.1": 2.2, "4.2": 3.4}


def student(out):
    pal = Palette("physics")
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / STUDY GUIDE")
    W.header(doc, pal, "UNIT 2 STUDY GUIDE  ·  VECTORS & PROJECTILE MOTION")
    W.TOTAL = ""
    gap(doc, 4)
    t = doc.add_table(rows=1, cols=3)
    fix_widths(t, [3.6, 2.2, 1.7])
    for c, lab in zip(t.rows[0].cells, ("NAME", "DATE", "PERIOD")):
        borders(c, pal.hair, sz=6)
        para(c, lab, 8.5, bold=True, color=pal.label, caps_track=True, first=True)
        c.paragraphs[0].paragraph_format.space_after = Pt(9)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "In each section, complete the statements, then work the two problems on this paper. The simple one checks the skill; the "
            "average one is closer to test level. Every answer needs a unit, and every vector answer needs a direction. "
            "Up is +y, g = 9.8 m/s², and air resistance is ignored.", 8.5, color=pal.ink, first=True)
    probs = problems()
    for num, title, std, bullets in SECTIONS:
        if num != "1":
            W.page_break(doc)
        gap(doc, 8)
        c = one_cell(doc, 7.5, protect=True)
        borders(c, pal.display, sz=12, edges=("bottom",))
        para(c, f"SECTION {num}  ·  {title}  ·  {std}", 9, bold=True, color=pal.accent, caps_track=True, first=True)
        c.paragraphs[0].paragraph_format.keep_with_next = True
        c = one_cell(doc, 7.5, protect=True)
        para(c, "COMPLETE EACH STATEMENT", 7.5, bold=True, color=pal.label, caps_track=True, first=True)
        for i, (tpl, ans) in enumerate(bullets, 1):
            fill_para(c, i, tpl, ans, pal)
        k = 0
        for pn, kind, text, box in probs:
            if pn != num:
                continue
            k += 1
            gap(doc, 5)
            c = one_cell(doc, 7.5, protect=True)
            para(c, f"{num}.{k}   {kind.upper()}", 8, bold=True, color=pal.accent, caps_track=True, first=True)
            para(c, text, 10)
            work_box(c, "", pal, BOX[f"{num}.{k}"], 7.2)
    Q.finish(doc, out)


# ---- key --------------------------------------------------------------------------------

def three_vec_steps(spec, s):
    u = spec["unit"]
    names = "ABC"
    steps = [WK.say("Write each direction on the 0–360° scale, then split into x and y parts.")]
    for (m, sp), nm in zip(spec["v"], names):
        steps.append(WK.row(f"{nm}: {V.standard_formula(*sp)[0]}" if sp[0] not in (0, 90) else f"{nm}: {V.theta_from(*sp):.0f}°"))
    for (m, th), (cx, cy), nm in zip(s["vs"], s["parts"], names):
        steps.append(WK.row(f"{nm}x = {m:g} cos {th:.0f}° = {n(cx)} {u}", "     ", f"{nm}y = {m:g} sin {th:.0f}° = {n(cy)} {u}"))
    px = " + ".join(f"({n(c[0])})" for c in s["parts"])
    py = " + ".join(f"({n(c[1])})" for c in s["parts"])
    steps += [
        WK.row(f"Rx = {px} = {n(s['rx'])} {u}"),
        WK.row(f"Ry = {py} = {n(s['ry'])} {u}"),
        WK.row(f"R^{{2}} = ({n(s['rx'])})^{{2}} + ({n(s['ry'])})^{{2}} = {s['rx'] ** 2 + s['ry'] ** 2:.2f}"),
        WK.row("R =", {"sqrt": f"{s['rx'] ** 2 + s['ry'] ** 2:.2f}"}, f"= {s['R']:.2f} {u}"),
        WK.ans("R =", f"{sf(s['R'])} {u}", note="round last"),
        WK.row("tan(angle) =", {"frac": [f"{abs(s['ry']):.2f}", f"{abs(s['rx']):.2f}"]}, f"= {abs(s['ry']) / abs(s['rx']):.2f}"),
        WK.row(f"angle = tan^{{−1}}({abs(s['ry']) / abs(s['rx']):.2f}) = {s['ref']:.1f}°", note="a size only; the signs give the quadrant"),
    ]
    ns = "north" if s["ry"] > 0 else "south"; ew = "east" if s["rx"] > 0 else "west"
    steps += [WK.say(f"Rx is {'positive' if s['rx'] > 0 else 'negative'} and Ry is {'positive' if s['ry'] > 0 else 'negative'}, so the result points {ns} of {ew}."),
              WK.ans("direction:", f"{s['ref']:.0f}° {ns} of {ew}")]
    return steps


def key_steps():
    g, s = G, S
    st = {}
    e = s["s1_p1"]
    st["1.1"] = [WK.say("The 0–360° scale starts at east and runs counterclockwise: 300° is in quadrant IV."),
                 WK.row("360° − 300° = 60°", note="from east, below the axis"), WK.ans("compass:", e["c1"]),
                 WK.row("90° − 60° = 30°", note="from the other axis"), WK.ans("or:", e["c2"]),
                 WK.row("300° − 360° = −60°", note="clockwise: subtract 360"), WK.ans("negative:", e["neg"])]
    p = s["s1_p2"]; mag = g["s1_p2"]["mag"]
    st["1.2"] = [WK.row(f"{V.standard_formula(*g['s1_p2']['spec'])[0]}", note="start at west (180°) and turn south"), WK.ans("(a)", f"{p['theta']:.0f}°"),
                 WK.say("(b) Tail at the origin, arrow into quadrant III (down and left), labeled 40 m/s at 215°.", "arrow"),
                 WK.row(f"vx = {mag} cos {p['theta']:.0f}° = {n(p['comps'][0])} m/s", "     ", f"vy = {mag} sin {p['theta']:.0f}° = {n(p['comps'][1])} m/s"),
                 WK.ans("(c)", f"vx = {n(p['comps'][0], 1)} m/s,  vy = {n(p['comps'][1], 1)} m/s", note="both negative in quadrant III")]
    for k, key in (("2.1", "s2_p1"), ("2.2", "s2_p2")):
        spec = {**g[key], "kind": "displacement"}
        st[k] = WK.q4_steps(spec, V.solve_q4(spec))
    sp = {**g["s3_p1"]}
    st["3.1"] = WK.q5_steps(sp, V.solve_q5(sp))
    st["3.2"] = three_vec_steps(g["s3_p2"], s["s3_p2"])
    st["4.1"] = W.p3_steps(g["s4_p1"], s["s4_p1"])
    st["4.2"] = W.p5_steps({**g["s4_p2"]}, s["s4_p2"])
    return st


def key_doc(out, tmp):
    pal = Palette("physics")
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / STUDY GUIDE / TEACHER KEY")
    W.header(doc, pal, "UNIT 2 STUDY GUIDE  ·  VECTORS & PROJECTILE MOTION", key=True)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "East is +x and north is +y. Up is +y. Keep the extra digits until the last step, then round to two significant figures.",
         8.5, color=pal.ink, first=True)
    para(c, "The answers to the fill-in statements are the completed sentences on the Key Concepts sheet.", 8.5, color=KEY_INK)
    steps = key_steps()
    probs = problems()
    counter = {}
    for pn, kind, text, _ in probs:
        counter[pn] = counter.get(pn, 0) + 1
        code = f"{pn}.{counter[pn]}"
        gap(doc, 6)
        c = one_cell(doc, protect=True); borders(c, pal.hair)
        para(c, f"{code}   {kind.upper()}", 8, bold=True, color=pal.accent, caps_track=True, first=True)
        para(c, text, 9.5, color=pal.ink)
        w = 7.0 if code not in ("1.1",) else 7.0
        png, _ = solution_image({"prompt": code, "steps": steps[code]}, os.path.join(tmp, f"sg{code}.png"), width_in=w, size=21)
        WK.picture(c, png, w)
        if code == "4.2":
            pass
    Q.finish(doc, out)


def review(out):
    """One page to hand out: every concept statement, completed. Built from the same SECTIONS."""
    pal = Palette("physics")
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / KEY CONCEPTS")
    W.header(doc, pal, "UNIT 2 KEY CONCEPTS  ·  VECTORS & PROJECTILE MOTION")
    gap(doc, 4)
    t = doc.add_table(rows=1, cols=3)
    fix_widths(t, [3.6, 2.2, 1.7])
    for c, lab in zip(t.rows[0].cells, ("NAME", "DATE", "PERIOD")):
        borders(c, pal.hair, sz=6)
        para(c, lab, 8.5, bold=True, color=pal.label, caps_track=True, first=True)
        c.paragraphs[0].paragraph_format.space_after = Pt(9)
    for num, title, std, items in SECTIONS:
        gap(doc, 8)
        c = one_cell(doc, 7.5, protect=True)
        borders(c, pal.display, sz=12, edges=("bottom",))
        para(c, f"SECTION {num}  ·  {title}  ·  {std}", 9, bold=True, color=pal.accent, caps_track=True, first=True)
        c.paragraphs[0].paragraph_format.keep_with_next = True
        c = one_cell(doc, 7.5, protect=True)
        for i, (tpl, ans) in enumerate(items, 1):
            fill_para(c, i, tpl, ans, pal, solved=True, size=11.5, color=pal.accent)
    Q.finish(doc, out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    V.VERSIONS_Q2 = {}
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(outdir, document_name("Study_Guide", ["2.1", "2.2", "2.3"], 2, descriptor="Key Concepts"))
        review(p)
        nn = Q.pages(p)
        print("ok " if nn == 1 else "BAD", nn, "page", os.path.basename(p))
        bad += nn != 1
        for key in (False, True):
            p = os.path.join(outdir, document_name("Study_Guide", ["2.1", "2.2", "2.3"], 2, key=key))
            key_doc(p, tmp) if key else student(p)
            nn = Q.pages(p)
            ok = nn <= 4
            print("ok " if ok else "BAD", nn, "page", os.path.basename(p))
            bad += not ok
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
