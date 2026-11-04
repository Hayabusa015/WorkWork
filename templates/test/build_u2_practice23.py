#!/usr/bin/env python3
"""Build the Physics S2.3 projectile practice set (three all-in-one problems) and its worked key.

    python3 templates/test/build_u2_practice23.py OUTDIR

Problem 1: an angled launch from a height, landing below (the archer on the castle wall).
Problem 2: a horizontal launch off a cliff, with the landing velocity.
Problem 3: an angled launch that lands ABOVE the launch height (two times fit; keep the later one).
Physics practice sets carry no work boxes: the work goes in the Hayden-McNeil notebook
(templates/worksheet/README.md). Every number is solved here and re-solved by stepping the motion
forward in time (verify()).
"""
import math, os, sys, tempfile
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
for p in (HERE, os.path.join(REPO, "templates"), os.path.join(REPO, "templates", "quiz"), os.path.join(REPO, "scripts")):
    sys.path.insert(0, p)
import u2_data as D                                                    # noqa: E402
import u2_equations as EQ                                              # noqa: E402
import build_quiz_docx as Q                                            # noqa: E402
import build_quiz_worked_keys as WK                                    # noqa: E402
import build_u2_written as W                                           # noqa: E402
from key_solution import solution_image                                # noqa: E402
from _shull_name import document_name                                  # noqa: E402
from _shull_docx import Palette, borders, para, fix_widths, gap, one_cell   # noqa: E402

G = 9.8
P1 = {"y0": 18.0, "v": 32.0, "ang": 25.0}
P2 = {"h": 45.0, "vx": 9.0}
P3 = {"v": 21.0, "ang": 55.0, "ledge": 6.0}

TEXT = [
    ("ANGLED LAUNCH  ·  LANDING BELOW",
     "An archer stands on a castle wall 18 m above the ground and shoots an arrow at 32 m/s at 25° above the horizontal at an enemy "
     "on the ground below. Find (a) the arrow’s horizontal and vertical launch velocities, (b) the time until it lands, (c) how far from "
     "the wall it lands, and (d) its speed and direction just before it lands."),
    ("HORIZONTAL LAUNCH  ·  FROM A CLIFF",
     "A rock is thrown horizontally at 9.0 m/s from the top of a 45 m cliff. Find (a) the time until it hits the ground, (b) how far from "
     "the base of the cliff it lands, and (c) its speed and direction just before it hits."),
    ("ANGLED LAUNCH  ·  LANDING ABOVE",
     "A football is kicked from the ground at 21 m/s at 55° above the horizontal toward a platform 6.0 m above the field. It lands on the "
     "platform on its way down. Find (a) the greatest height the ball reaches above the field, (b) the time until it lands on the platform, "
     "and (c) the horizontal distance from the kicker to where it lands."),
]


def solve():
    s1 = D.from_height(P1["y0"], P1["v"], P1["ang"])
    s1["speed"] = math.hypot(s1["vx"], s1["vyf"]); s1["below"] = math.degrees(math.atan(abs(s1["vyf"]) / s1["vx"]))
    s2 = D.horizontal_launch(P2["h"], P2["vx"])
    s2["speed"] = math.hypot(P2["vx"], s2["vy"]); s2["below"] = math.degrees(math.atan(abs(s2["vy"]) / P2["vx"]))
    vx, vy = P3["v"] * math.cos(math.radians(P3["ang"])), P3["v"] * math.sin(math.radians(P3["ang"]))
    a, b, c = 0.5 * G, -vy, P3["ledge"]
    disc = b * b - 4 * a * c
    t_up, t_dn = (-b - math.sqrt(disc)) / (2 * a), (-b + math.sqrt(disc)) / (2 * a)
    s3 = {"vx": vx, "vy": vy, "H": vy * vy / (2 * G), "a": a, "b": b, "c": c, "disc": disc, "t_up": t_up, "t_dn": t_dn,
          "x": vx * t_dn, "vy_dn": vy - G * t_dn}
    return s1, s2, s3


def verify(s1, s2, s3):
    """Step the motion forward in time instead of using the formulas."""
    def run(y0, vx, vy, stop):
        x, y, t, dt = 0.0, y0, 0.0, 1e-5
        while True:
            vy2 = vy - G * dt
            y2 = y + 0.5 * (vy + vy2) * dt
            if stop(y2, vy2):
                return t, x, vy2
            x += vx * dt; y, vy, t = y2, vy2, t + dt
    t, x, vyf = run(P1["y0"], s1["vx"], s1["vy"], lambda y, v: y <= 0)
    assert abs(t - s1["t"]) < 2e-4 and abs(x - s1["x"]) < 2e-3 and abs(vyf - s1["vyf"]) < 2e-3, "P1"
    t, x, vyf = run(P2["h"], P2["vx"], 0, lambda y, v: y <= 0)
    assert abs(t - s2["t"]) < 2e-4 and abs(x - s2["x"]) < 2e-3 and abs(vyf - s2["vy"]) < 2e-3, "P2"
    t, x, vyf = run(0.0, s3["vx"], s3["vy"], lambda y, v: y <= P3["ledge"] and v < 0)
    assert abs(t - s3["t_dn"]) < 2e-4 and abs(x - s3["x"]) < 2e-3, "P3"
    top = max(s3["vy"] * t_ - 0.5 * G * t_ * t_ for t_ in [i * 1e-4 for i in range(0, 40000)])
    assert abs(top - s3["H"]) < 1e-3, "P3 height"


def student(out):
    pal = Palette("physics")
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / S02.3 / PRACTICE SET")
    W.TITLE = "UNIT 2 · MOTION IN TWO DIMENSIONS"
    W.CODE = "U02 / S02.3"
    W.header(doc, pal, "S2.3 PROJECTILE MOTION  ·  PRACTICE SET")
    gap(doc, 4)
    t = doc.add_table(rows=1, cols=3)
    fix_widths(t, [3.6, 2.2, 1.7])
    for c, lab in zip(t.rows[0].cells, ("NAME", "DATE", "PERIOD")):
        borders(c, pal.hair, sz=6)
        para(c, lab, 8.5, bold=True, color=pal.label, caps_track=True, first=True)
        c.paragraphs[0].paragraph_format.space_after = Pt(9)
    gap(doc, 4)
    c = one_cell(doc, 7.5); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "Work every problem in your Hayden-McNeil notebook. Write the givens with signs, name the equation you use, and carry units. "
            "Up is +y, g = 9.8 m/s², air resistance is ignored, and answers are rounded to two significant figures.", 9, color=pal.ink, first=True)
    gap(doc, 4)
    EQ.projectile_block(doc, pal)
    for i, (label, text) in enumerate(TEXT, 1):
        gap(doc, 9)
        c = one_cell(doc, 7.5, protect=True)
        para(c, f"{i}.   {label}", 8, bold=True, color=pal.accent, caps_track=True, first=True)
        para(c, text, 10.5)
    Q.finish(doc, out)


def steps(s1, s2, s3):
    sf, n = D.sf, WK.n
    st1 = W.p5_steps(P1, s1)
    st1 += [WK.say("Landing velocity: the horizontal part is unchanged, the vertical part keeps changing.", "arrow"),
            WK.row(f"vy = viy − g t = {s1['vy']:.2f} − (9.8)({s1['t']:.2f}) = {n(s1['vyf'])} m/s"),
            WK.row("speed =", {"sqrt": f"({s1['vx']:.2f})^{2} + ({abs(s1['vyf']):.2f})^{2}"}, f"= {s1['speed']:.2f} m/s"),
            WK.row("tan(angle) =", {"frac": [f"{abs(s1['vyf']):.2f}", f"{s1['vx']:.2f}"]}, f"= {abs(s1['vyf']) / s1['vx']:.2f}"),
            WK.ans("(d)", f"{sf(s1['speed'])} m/s at {sf(s1['below'])}° below the horizontal")]
    st2 = W.p3_steps(P2, s2)
    st2 += [WK.say("Landing velocity: vx stays 9.0 m/s; vy comes from the fall.", "arrow"),
            WK.row(f"vy = −g t = −(9.8)({s2['t']:.2f}) = {n(s2['vy'])} m/s"),
            WK.row("speed =", {"sqrt": f"({P2['vx']:.1f})^{2} + ({abs(s2['vy']):.2f})^{2}"}, f"= {s2['speed']:.2f} m/s"),
            WK.row("tan(angle) =", {"frac": [f"{abs(s2['vy']):.2f}", f"{P2['vx']:.1f}"]}, f"= {abs(s2['vy']) / P2['vx']:.2f}"),
            WK.ans("(c)", f"{sf(s2['speed'])} m/s at {sf(s2['below'])}° below the horizontal")]
    L = P3["ledge"]
    st3 = [WK.row(f"vix = {P3['v']:g} cos {P3['ang']:g}° = {s3['vx']:.2f} m/s", "     ", f"viy = {P3['v']:g} sin {P3['ang']:g}° = {s3['vy']:.2f} m/s"),
           WK.say("(a) At the top vy = 0, so the height above the field comes from viy and g."),
           WK.row("Δy =", {"frac": [f"viy^{{2}}", "2g"]}, "=", {"frac": [f"({s3['vy']:.2f})^{{2}}", "2(9.8)"]}, f"= {s3['H']:.2f} m"),
           WK.ans("(a) Δy =", f"{sf(s3['H'])} m"),
           WK.say(f"(b) The platform is {L:g} m above the launch, so Δy = +{L:g} m."),
           WK.row(f"{L:g} = {s3['vy']:.2f} t − 4.9 t^{{2}}   →   4.9 t^{{2}} − {s3['vy']:.2f} t + {L:g} = 0", note=f"a = 4.9,  b = −{s3['vy']:.2f},  c = {L:g}"),
           WK.row("b^{2} − 4ac =", f"({n(s3['b'])})^{{2}} − 4(4.9)({L:g}) = {s3['disc']:.1f}"),
           WK.row("square root =", {"sqrt": f"{s3['disc']:.1f}"}, f"= {math.sqrt(s3['disc']):.2f}"),
           WK.row("t =", {"frac": [f"{s3['vy']:.2f} ± {math.sqrt(s3['disc']):.2f}", "2(4.9)"]}, f"=  {s3['t_up']:.2f} s   or   {s3['t_dn']:.2f} s"),
           WK.say(f"Two times: the ball passes the platform height going up ({s3['t_up']:.2f} s), then lands on the way down.", "arrow"),
           WK.say(f"Check: at {s3['t_dn']:.2f} s, vy = {n(s3['vy_dn'])} m/s (negative, falling). Keep the later time.", "arrow"),
           WK.ans("(b) t =", f"{sf(s3['t_dn'])} s"),
           WK.row(f"Δx = vix t = ({s3['vx']:.2f})({s3['t_dn']:.2f}) = {s3['x']:.1f} m"),
           WK.ans("(c) Δx =", f"{sf(s3['x'])} m")]
    return [st1, st2, st3]


def key_doc(out, tmp, s1, s2, s3):
    pal = Palette("physics")
    doc = Q.new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / S02.3 / PRACTICE SET / TEACHER KEY")
    W.header(doc, pal, "S2.3 PROJECTILE MOTION  ·  PRACTICE SET", key=True)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "Up is +y. Keep the extra digits until the last step, then round to two significant figures. A speed and direction at "
            "impact is the vector sum of vx and the final vy; name the direction as an angle below the horizontal.", 8.5, color=pal.ink, first=True)
    for i, ((label, text), st) in enumerate(zip(TEXT, steps(s1, s2, s3)), 1):
        gap(doc, 6)
        c = one_cell(doc, protect=True); borders(c, pal.hair)
        para(c, f"{i}.   {label}", 8, bold=True, color=pal.accent, caps_track=True, first=True)
        para(c, text, 9.5, color=pal.ink)
        png, _ = solution_image({"prompt": f"pp{i}", "steps": st}, os.path.join(tmp, f"pp{i}.png"), width_in=7.0, size=21)
        WK.picture(c, png, 7.0)
    gap(doc, 6)
    c = one_cell(doc, protect=True); borders(c, pal.hair)
    para(c, "COMMON ERRORS", 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    para(c, "Using t = 2viy/g when the landing height differs (1, 3) · forgetting Δy = −18 m for a landing below the launch (1) · "
            "keeping the negative root, or the earlier root in 3 · giving the landing speed as just vy · forgetting that vx is unchanged · "
            "naming the landing angle without “below the horizontal.”", 8.5, color=pal.ink)
    Q.finish(doc, out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    s1, s2, s3 = solve()
    verify(s1, s2, s3)
    V = WK.V
    V.VERSIONS_Q2 = {}
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        for key in (False, True):
            p = os.path.join(outdir, document_name("Practice_Set", ["2.3"], 2, key=key))
            key_doc(p, tmp, s1, s2, s3) if key else student(p)
            n = Q.pages(p)
            ok = n <= (3 if key else 1)
            print("ok " if ok else "BAD", n, "page", os.path.basename(p))
            bad += not ok
    print("answers: P1 t=%.2f x=%.1f speed=%.1f below=%.0f | P2 t=%.2f x=%.1f speed=%.1f below=%.0f | P3 H=%.1f t=%.2f x=%.1f" % (
        s1["t"], s1["x"], s1["speed"], s1["below"], s2["t"], s2["x"], s2["speed"], s2["below"], s3["H"], s3["t_dn"], s3["x"]))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
