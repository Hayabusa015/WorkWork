#!/usr/bin/env python3
"""Write the PHYS U03 slide-solutions key spec: full worked steps for the 20 problem slides
in the 3.1-3.7 decks (templates/slide/decks/phys_u03_specs.py).

The slides carry each final answer; this key carries the steps, for Matt's class prep.
Handwritten per standards/ANSWER_KEYS.md: math in pencil, stacked fractions, one algebra
move per line. "angle" stands in for theta and "Fnet" for sigma-F, as on the slides.

    python3 templates/worksheet/specs/phys_u03_slide_solutions.py
    python3 templates/worksheet/build_worksheet_key_docx.py \
        templates/worksheet/specs/phys_u03_slide_solutions.json "Unit 3 Slide Solutions Key.docx"
"""
import json, os

F = lambda n, d: {"frac": [n, d]}
R = lambda *items, note=None: ({"row": list(items), "note": note} if note else {"row": list(items)})
ANS = lambda lhs, v: {"answer": [lhs], "value": v}
SAY = lambda s: {"say": s}


def q(prompt, final, steps):
    return {"prompt": prompt, "solution": final, "finalAnswer": final, "calculation": True, "steps": steps}


SECTIONS = [
("3.1", "Newton's Laws", [
    q("A 60 kg student stands on Earth, then on the Moon (g = 1.6 m/s²). Find the weight in each place.",
      "Earth 588 N down; Moon 96 N down", [
        R("W = mg"),
        R("W_{Earth} = (60 kg)(9.8 m/s^{2})"), ANS("W_{Earth} =", "588 N down"),
        R("W_{Moon} = (60 kg)(1.6 m/s^{2})"), ANS("W_{Moon} =", "96 N down"),
        SAY("The mass is 60 kg in both places. Only g changed."),
    ]),
]),
("3.2", "Free Body Diagrams", [
    q("Draw and label FBDs: a 2.0 kg book on a table, and a 1.5 kg lamp hanging from a cord.",
      "Book: N = W = 19.6 N; Lamp: T = W = 14.7 N", [
        R("W_{book} = (2.0 kg)(9.8 m/s^{2}) = 19.6 N"),
        R("at rest, so N = W", note="up balances down"), ANS("N =", "19.6 N up"),
        R("W_{lamp} = (1.5 kg)(9.8 m/s^{2}) = 14.7 N"),
        R("at rest, so T = W"), ANS("T =", "14.7 N up"),
        SAY("Book FBD: N up, W down. Lamp FBD: T up, W down. Two arrows each, equal length."),
    ]),
    q("Forces on a crate: 50 N right, 20 N left, 40 N up, 40 N down. Find the net force, then the one force that would put it in equilibrium.",
      "Fnet = 30 N right; balancing force 30 N left", [
        R("Fnet_{x} = +50 N − 20 N = +30 N"),
        R("Fnet_{y} = +40 N − 40 N = 0"),
        ANS("Fnet =", "30 N right"),
        SAY("Equilibrium needs Fnet = 0, so add a force equal and opposite to the net force."),
        ANS("balancing force =", "30 N left"),
    ]),
    q("Two ropes pull a crate on frictionless ice (top view): 80 N at 40° above +x, and 30 N toward −x. Find the net force.",
      "60 N at 59° above +x", [
        R("F_{1x} = 80 cos 40° = 61.3 N"), R("F_{1y} = 80 sin 40° = 51.4 N"),
        R("Fnet_{x} = 61.3 N − 30 N = 31.3 N"), R("Fnet_{y} = 51.4 N"),
        R("Fnet =", {"sqrt": "31.3^{2} + 51.4^{2}"}, " = 60.2 N"),
        R("angle = tan^{−1}", F("51.4", "31.3"), " = 58.7°"),
        ANS("Fnet =", "60 N at 59° above +x"),
    ]),
    q("Two tugboats pull a barge (top view): 500 N at 30° above +x, 400 N at 45° above −x. Find Fnet.",
      "554 N at 74° above +x", [
        R("F_{1x} = 500 cos 30° = +433.0 N", note="right"), R("F_{1y} = 500 sin 30° = +250.0 N"),
        R("F_{2x} = −400 cos 45° = −282.8 N", note="points left, so negative"), R("F_{2y} = 400 sin 45° = +282.8 N"),
        R("Fnet_{x} = 433.0 − 282.8 = 150.2 N"), R("Fnet_{y} = 250.0 + 282.8 = 532.8 N"),
        R("Fnet =", {"sqrt": "150.2^{2} + 532.8^{2}"}, " = 554 N"),
        R("angle = tan^{−1}", F("532.8", "150.2"), " = 74.3°"),
        ANS("Fnet =", "554 N at 74° above +x"),
    ]),
]),
("3.3", "Inclined Plane FBDs", [
    q("A 5.0 kg block sits on a frictionless 30° ramp. Draw its FBD. Find both weight components and N.",
      "Along 24.5 N; into 42.4 N; N = 42.4 N", [
        R("W = (5.0 kg)(9.8 m/s^{2}) = 49 N"),
        R("W_{along} = mg sin(angle) = 49 sin 30°"), ANS("W_{along} =", "24.5 N down the slope"),
        R("W_{into} = mg cos(angle) = 49 cos 30°"), ANS("W_{into} =", "42.4 N"),
        R("nothing moves into the ramp, so N = W_{into}"), ANS("N =", "42.4 N"),
        SAY("FBD: W straight down, N perpendicular out of the ramp. The components replace W; do not draw all three as separate forces."),
    ]),
    q("A worker pushes a 12 kg crate up a frictionless 25° ramp with 30 N, parallel to the ramp. Find the net force along the ramp.",
      "19.7 N down the ramp", [
        R("down the slope is positive"),
        R("W_{along} = (12)(9.8) sin 25° = 49.7 N"),
        R("Fnet = 49.7 N − 30 N"), ANS("Fnet =", "19.7 N down the ramp"),
    ]),
]),
("3.4", "F = ma Calculations", [
    q("A 1500 kg car has 4500 N of engine force forward and 1200 N of drag. Find a.",
      "2.2 m/s² forward", [
        R("Fnet = 4500 N − 1200 N = 3300 N"),
        R("Fnet = ma"), R("a =", F("Fnet", "m"), note="divide both sides by m"),
        R("a =", F("3300 N", "1500 kg")), ANS("a =", "2.2 m/s^{2} forward"),
    ]),
    q("The graph shows net force against acceleration for one cart, through (0, 0) and (3.2 m/s², 8.0 N). Find the cart's mass.",
      "2.5 kg", [
        R("slope =", F("ΔF", "Δa"), " = m"),
        R("m =", F("8.0 N − 0", "3.2 m/s^{2} − 0")),
        ANS("m =", "2.5 kg"),
        SAY("N divided by m/s² is kg, so the slope's unit checks out."),
    ]),
]),
("3.5", "Net Force & Acceleration", [
    q("A 20 kg sled on frictionless ice is pulled with 60 N at 35° above horizontal. Find a and the normal force.",
      "a = 2.5 m/s² right; N = 162 N", [
        R("F_{x} = 60 cos 35° = 49.1 N"), R("F_{y} = 60 sin 35° = 34.4 N"),
        R("a =", F("F_{x}", "m"), " =", F("49.1 N", "20 kg")), ANS("a =", "2.5 m/s^{2} right"),
        R("vertical: N + F_{y} − mg = 0"), R("N = mg − F_{y}", note="subtract F_{y} from both sides"),
        R("N = 196 N − 34.4 N"), ANS("N =", "162 N"),
    ]),
    q("An 8.0 kg box slides down a frictionless 20° ramp. Find its acceleration.",
      "3.4 m/s² down the ramp", [
        R("Fnet = mg sin(angle)"), R("ma = mg sin(angle)"), R("a = g sin(angle)", note="divide both sides by m"),
        R("a = (9.8 m/s^{2}) sin 20°"), ANS("a =", "3.4 m/s^{2} down the ramp"),
        SAY("The 8.0 kg is not needed. Mass cancels on a frictionless ramp."),
    ]),
    q("A 70 kg person stands on a scale in an elevator accelerating up at 2.0 m/s². Find the reading.",
      "826 N", [
        R("up is positive: N − mg = ma"), R("N = mg + ma = m(g + a)", note="add mg to both sides"),
        R("N = (70 kg)(9.8 + 2.0 m/s^{2})"), ANS("N =", "826 N"),
        SAY("True weight is 686 N. The scale reads more because it must also speed the person up."),
    ]),
    q("The same 70 kg person rides an elevator accelerating down at 2.0 m/s². Find the reading.",
      "546 N", [
        R("up is positive, so a = −2.0 m/s^{2}"), R("N = m(g + a)"),
        R("N = (70 kg)(9.8 − 2.0 m/s^{2})"), ANS("N =", "546 N"),
        {"mistake": ["N = (70)(9.8 + 2.0) = 826 N"], "note": "ignoring the sign of a"},
    ]),
]),
("3.6", "Frictional Forces", [
    q("A 40 kg box is pushed across the floor at constant velocity with 120 N. Find μk.",
      "0.31", [
        R("constant velocity, so Fnet = 0 and f_{k} = 120 N"),
        R("N = mg = (40)(9.8) = 392 N"),
        R("f_{k} = μ_{k} N"), R("μ_{k} =", F("f_{k}", "N"), " =", F("120 N", "392 N"), note="divide both sides by N"),
        ANS("μ_{k} =", "0.31"),
    ]),
    q("A 25 kg box (μs = 0.40, μk = 0.30) is pushed with 90 N. Does it move? If the push rises to 110 N, find a.",
      "90 N: no motion; 110 N: a = 1.5 m/s²", [
        R("N = (25)(9.8) = 245 N"),
        R("f_{s,max} = (0.40)(245 N) = 98 N"),
        SAY("90 N < 98 N, so static friction holds it. No motion."),
        R("110 N > 98 N, so it slides: f_{k} = (0.30)(245 N) = 73.5 N"),
        R("Fnet = 110 N − 73.5 N = 36.5 N"),
        R("a =", F("36.5 N", "25 kg")), ANS("a =", "1.5 m/s^{2}"),
    ]),
    q("A 30 kg crate is pulled with 150 N at 30° above horizontal. μk = 0.25. Find N and a.",
      "N = 219 N; a = 2.5 m/s²", [
        R("F_{y} = 150 sin 30° = 75 N"), R("F_{x} = 150 cos 30° = 129.9 N"),
        R("N = mg − F_{y} = 294 N − 75 N"), ANS("N =", "219 N"),
        {"mistake": ["N = mg = 294 N"], "note": "the pull lifts part of the weight"},
        R("f_{k} = (0.25)(219 N) = 54.8 N"),
        R("Fnet = 129.9 N − 54.8 N = 75.1 N"),
        R("a =", F("75.1 N", "30 kg")), ANS("a =", "2.5 m/s^{2}"),
    ]),
    q("A 10 kg block rests on a 35° incline. μs = 0.50, μk = 0.40. Does it slide? If so, find a.",
      "Slides; a = 2.4 m/s²", [
        R("W_{along} = (10)(9.8) sin 35° = 56.2 N"),
        R("N = (10)(9.8) cos 35° = 80.3 N"),
        R("f_{s,max} = (0.50)(80.3 N) = 40.1 N"),
        SAY("56.2 N > 40.1 N, so it slides. Kinetic friction takes over."),
        R("f_{k} = (0.40)(80.3 N) = 32.1 N"),
        R("Fnet = 56.2 N − 32.1 N = 24.1 N"),
        R("a =", F("24.1 N", "10 kg")), ANS("a =", "2.4 m/s^{2} down the slope"),
    ]),
]),
("3.7", "Multi-Body Systems", [
    q("A 5.0 kg mass and a 3.0 kg mass hang over a pulley (Atwood machine). Find a and the string tension.",
      "a = 2.45 m/s²; T = 36.8 N", [
        R("system: Fnet = (5.0 − 3.0)(9.8) = 19.6 N"),
        R("a =", F("19.6 N", "8.0 kg")), ANS("a =", "2.45 m/s^{2}"),
        R("3.0 kg alone (moves up): T − m_{2}g = m_{2}a"),
        R("T = m_{2}(g + a) = (3.0)(9.8 + 2.45)", note="add m_{2}g to both sides"),
        ANS("T =", "36.8 N"),
    ]),
    q("A 4.0 kg block on a frictionless table is tied over a pulley to a 2.0 kg hanging mass. Find a and T.",
      "a = 3.27 m/s²; T = 13.1 N", [
        R("only the hanging weight drives it: Fnet = (2.0)(9.8) = 19.6 N"),
        R("a =", F("19.6 N", "6.0 kg")), ANS("a =", "3.27 m/s^{2}"),
        R("block alone: T = m_{1}a = (4.0)(3.27)"), ANS("T =", "13.1 N"),
    ]),
    q("Repeat the table problem with μk = 0.20 between the 4.0 kg block and the table. Find a and T.",
      "a = 1.96 m/s²; T = 15.7 N", [
        R("f_{k} = (0.20)(4.0)(9.8) = 7.84 N"),
        R("Fnet = 19.6 N − 7.84 N = 11.76 N"),
        R("a =", F("11.76 N", "6.0 kg")), ANS("a =", "1.96 m/s^{2}"),
        R("block alone: T − f_{k} = m_{1}a"), R("T = (4.0)(1.96) + 7.84", note="add f_{k} to both sides"),
        ANS("T =", "15.7 N"),
    ]),
    q("A 6.0 kg block on a frictionless 30° incline is tied over a pulley to a 5.0 kg hanging mass. Find a and T.",
      "a = 1.78 m/s²; T = 40.1 N", [
        R("hanging pull: (5.0)(9.8) = 49.0 N"),
        R("block's pull down the slope: (6.0)(9.8) sin 30° = 29.4 N"),
        SAY("49.0 N > 29.4 N, so the hanging mass goes down and the block goes up the slope."),
        R("a =", F("49.0 N − 29.4 N", "11.0 kg")), ANS("a =", "1.78 m/s^{2}"),
        R("hanging mass alone: m_{2}g − T = m_{2}a"),
        R("T = m_{2}(g − a) = (5.0)(9.8 − 1.78)"), ANS("T =", "40.1 N"),
    ]),
]),
]


def main():
    spec = {"course": "physics", "unit": 3, "sections": [s[0] for s in SECTIONS], "docType": "Slide_Solutions",
            "sectionsContent": [{"code": c, "title": f"{c} {t}", "questions": qs} for c, t, qs in SECTIONS]}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phys_u03_slide_solutions.json")
    json.dump(spec, open(out, "w"), indent=1, ensure_ascii=False)
    print(out, sum(len(s[2]) for s in SECTIONS), "problems")


if __name__ == "__main__":
    main()
