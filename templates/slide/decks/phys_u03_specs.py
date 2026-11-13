#!/usr/bin/env python3
"""Write the seven PHYS U03 section-deck specs (3.1-3.7) for build_deck.js.

Outline approved by Matt 2026-11-04: 46 slides, one problem slide per problem type, and each
problem slide carries its problem, its diagram and its final answer together (layout 11). The
full worked steps live in the separate teacher key, not on the slides.

Archivo has no Greek capital sigma or small theta, so the decks write "Fnet" and "angle" (the
brand forbids a substitute face). The micro sign, the Greek capital delta and superscript two
are in Archivo and are used.

    python3 templates/slide/decks/phys_u03_specs.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
A = "../assets/phys_u03/"


def title(n, code, name, sub, subject):
    return {"master": "02_SECTION_TITLE",
            "fields": {"number": f"{n:02d}", "headline": f"{code}\n{name}", "subhead": sub},
            "imageSubjects": {"section": subject}}


def problem(head, sub, prob, given, eq, ans, img):
    return {"master": "11_GIVENS_EQUATION_ANSWER",
            "fields": {"headline": head, "subhead": sub, "problem": prob,
                       "q1_l": "GIVEN", "q1_b": given, "q2_l": "EQUATION", "q2_b": eq, "answer": ans},
            "images": {"setup": A + img}}


def grouped(head, sub, l1, b1, l2, b2, must, img):
    return {"master": "03_GROUPED_CONCEPT",
            "fields": {"headline": head, "subhead": sub, "c1_l": l1, "c1_b": b1, "c2_l": l2, "c2_b": b2,
                       "mustwrite": must},
            "images": {"concept": A + img}}


def diagram(head, sub, rows, img):
    f = {"headline": head, "subhead": sub}
    for i, (l, b) in enumerate(rows, 1):
        f[f"a{i}_l"], f[f"a{i}_b"] = l, b
    return {"master": "08_DIAGRAM_ANNOTATION", "fields": f, "images": {"diagram": A + img}}


def worked(head, sub, flabel, fbody, work, must, img):
    return {"master": "10_WORKED_SOLUTION",
            "fields": {"headline": head, "subhead": sub, "f1_l": flabel, "f1_b": fbody, "work": work,
                       "mustwrite": must},
            "images": {"data": A + img}}


DECKS = {
"3.1": ("Newton's Laws", [
    title(1, "3.1", "Newton's Laws", "Measure forces in newtons, separate mass from weight, and use Newton's three laws.",
          "a cast-iron weight hanging from a spring scale against a dark wall"),
    diagram("What Is a Force?", "Every force you draw this unit has two parts: a size and a direction.", [
        ("PUSH OR PULL", "A force is a push or a pull on an object."),
        ("NEWTONS (N)", "1 N is about the weight of a small apple."),
        ("ALWAYS A DIRECTION", "Force is a vector: a size plus a direction."),
    ], "s31_force.png"),
    grouped("Mass vs. Weight", "They are not the same quantity, and they do not use the same unit.",
            "MASS", "Amount of matter, in kg.\nThe same everywhere.",
            "WEIGHT", "Pull of gravity, in N.\nW = mg, g = 9.8 m/s²\nChanges with location.",
            "Weight is a force: W = mg, in newtons. Mass is in kilograms.", "s31_mass_weight.png"),
    problem("Weight on Earth and on the Moon", "On the Moon, g = 1.6 m/s².",
            "A 60 kg student stands on Earth, then on the Moon. Find the weight in each place.",
            "m = 60 kg\ng Earth = 9.8 m/s²\ng Moon = 1.6 m/s²", "W = mg",
            "Earth: 588 N down  ·  Moon: 96 N down", "s31_weight_problem.png"),
    {"master": "06_CONCEPT_IMAGE",
     "fields": {"headline": "Newton's First Law",
                "subhead": "An object keeps its velocity unless a net force acts on it. Fnet = 0 is equilibrium: at rest or at constant velocity.",
                "keyq": "A puck slides at constant speed. Net force? Zero."},
     "images": {"concept": A + "s31_puck.png"}},
    grouped("Newton's Second Law", "A net force makes an object accelerate. We put numbers on it in 3.4.",
            "MORE FORCE", "Same mass, bigger push.\nMore acceleration.",
            "MORE MASS", "Same push, bigger mass.\nLess acceleration.",
            "A net force causes acceleration. No net force, no acceleration.", "s31_second_law.png"),
    grouped("Newton's Third Law", "For every force, the other object pushes back equally, in the opposite direction.",
            "A THIRD-LAW PAIR", "Book pushes on table.\nTable pushes on book.\nTwo different objects.",
            "BALANCED, NOT A PAIR", "W and N both act\non the book.\nSame object: not a pair.",
            "Action-reaction pairs act on different objects, so they never cancel.", "s31_third_law.png"),
]),
"3.2": ("Free Body Diagrams", [
    title(2, "3.2", "Free Body Diagrams", "Draw free body diagrams, find the net force, and break angled forces into components.",
          "a tug-of-war rope pulled taut across a gym floor"),
    diagram("Drawing a Free Body Diagram", "One arrow per force, never one for motion. Friction waits until 3.6.", [
        ("THE RULES", "A box or dot, one labeled arrow per force, to scale."),
        ("FORCE TYPES", "Weight W, normal N, applied F_app, tension T."),
        ("TENSION", "A rope only pulls, along the rope, away from the object."),
    ], "s32_rules.png"),
    problem("Draw the FBDs", "Both objects are at rest, so the forces on each one balance.",
            "Draw and label FBDs: a 2.0 kg book on a table, and a 1.5 kg lamp hanging from a cord.",
            "Book: m = 2.0 kg\nLamp: m = 1.5 kg\nBoth at rest", "W = mg\nAt rest: Fnet = 0",
            "Book: N = W = 19.6 N  ·  Lamp: T = W = 14.7 N", "s32_draw_problem.png"),
    grouped("Net Force in One Dimension", "Add the forces along each axis, with signs.",
            "SIGN CONVENTION", "Right and up are +.\nLeft and down are −.\nState it every time.",
            "ADD BY AXIS", "Fnet,x: the horizontals.\nFnet,y: the verticals.\nNever mix the two.",
            "Net force is the sum of every force, with signs: Fnet = F1 + F2 + ...", "s32_net1d.png"),
    problem("Net Force and Equilibrium", "Use +x right and +y up.",
            "Find the net force on the crate, then the one force that would put it in equilibrium.",
            "50 N right, 20 N left\n40 N up, 40 N down", "Fnet,x = 50 − 20\nFnet,y = 40 − 40",
            "Fnet = 30 N right  ·  Balancing force: 30 N left", "s32_crate_problem.png"),
    worked("Resultant and Angle", "When Fnet,x and Fnet,y are both nonzero, combine them into one force.",
           "FORMULA", "F = √(Fx² + Fy²)\nangle = tan inverse (Fy/Fx)\nmeasured from +x",
           "F = √(40² + 30²)\n= 50 N\nangle = 37° above +x",
           "A resultant needs a size and a direction. State both, every time.", "s32_resultant.png"),
    diagram("Forces at Angles", "Break an angled force into the part along x and the part along y.", [
        ("X-COMPONENT", "Fx = F cos(angle) = 100 cos 30° = 87 N"),
        ("Y-COMPONENT", "Fy = F sin(angle) = 100 sin 30° = 50 N"),
        ("CHECK", "√(87² + 50²) = 100 N. The parts rebuild the force."),
    ], "s32_components.png"),
    problem("One Angled Force, One Straight", "Seen from above, on frictionless ice. Use +x right.",
            "Two ropes pull a crate: 80 N at 40° above +x, and 30 N toward −x. Find the net force.",
            "80 N at 40°\n30 N toward −x", "Fx = F cos(angle)\nFy = F sin(angle)",
            "Fnet = 60 N at 59° above +x", "s32_two_force_problem.png"),
    problem("Two Angled Forces", "Seen from above. Angles are measured from the x-axis.",
            "Two tugboats pull a barge: 500 N at 30° above +x, 400 N at 45° above −x. Find Fnet.",
            "500 N at 30° (+x)\n400 N at 45° (−x)", "Sum Fx, sum Fy, then\nF = √(Fx² + Fy²)",
            "Fnet = 554 N at 74° above +x", "s32_two_angled_problem.png"),
]),
"3.3": ("Inclined Plane FBDs", [
    title(3, "3.3", "Inclined Plane FBDs", "Tilt the axes and split the weight into parts along and into the slope.",
          "a wooden ramp leaning against a loading dock in low light"),
    diagram("Tilt the Axes on a Slope", "The angle between W and the tilted y-axis equals the ramp angle.", [
        ("TILT THE AXES", "x along the slope, y perpendicular to the slope."),
        ("ALONG THE SLOPE", "mg sin(angle), pointing down the slope."),
        ("INTO THE SLOPE", "mg cos(angle), pressing into the surface."),
    ], "s33_components.png"),
    grouped("Normal Force Is Not the Weight", "The steeper the ramp, the less the surface pushes back.",
            "NEARLY FLAT", "N gets close to mg.\nAlmost nothing pulls\nthe block along.",
            "NEARLY VERTICAL", "N gets close to 0.\nThe pull along the\nslope nears mg.",
            "On an incline, N = mg cos(angle), not mg.", "s33_angle_extremes.png"),
    problem("Block on a 30° Ramp", "Frictionless. Tilt your axes before you calculate anything.",
            "A 5.0 kg block sits on a 30° ramp. Draw its FBD. Find both weight components and N.",
            "m = 5.0 kg\nangle = 30°\nW = 49 N", "along: mg sin(angle)\ninto: mg cos(angle)",
            "Along: 24.5 N  ·  Into: 42.4 N  ·  N = 42.4 N", "s33_block_problem.png"),
    problem("Net Force Along the Slope", "Frictionless. The push is parallel to the ramp.",
            "A worker pushes a 12 kg crate up a 25° ramp with 30 N. Find the net force along the ramp.",
            "m = 12 kg, angle = 25°\npush = 30 N up the ramp", "Fnet = mg sin(angle) − 30",
            "Fnet = 19.7 N down the ramp", "s33_push_problem.png"),
]),
"3.4": ("F = ma Calculations", [
    title(4, "3.4", "F = ma Calculations", "Use Newton's second law to connect net force, mass, and acceleration.",
          "a lab cart on a track with a hanging mass at the far end"),
    worked("Newton's Second Law: Fnet = ma", "The acceleration is in the direction of the net force.",
           "FORMULA", "Fnet = ma\n1 N = 1 kg·m/s²\na = Fnet/m",
           "a = 12 N / 4.0 kg\n= 3.0 m/s²\nto the right",
           "Fnet = ma. Use the net force, never a single force.", "s34_cart_example.png"),
    problem("Two Opposing Forces", "Use forward as positive.",
            "A 1500 kg car has 4500 N of engine force forward and 1200 N of drag. Find a.",
            "m = 1500 kg\n4500 N forward\n1200 N backward", "Fnet = 4500 − 1200\na = Fnet/m",
            "a = 2.2 m/s² forward", "s34_car_problem.png"),
    diagram("Reading an F vs. a Graph", "Plot net force against acceleration for one object.", [
        ("AXES", "Net force on y, acceleration on x."),
        ("SLOPE", "rise/run = ΔF/Δa = m, in kilograms."),
        ("THROUGH THE ORIGIN", "Zero net force gives zero acceleration."),
    ], "s34_graph_concept.png"),
    problem("Mass from a Graph", "Use two points far apart on the line.",
            "The graph shows net force against acceleration for one cart. Find the cart's mass.",
            "Read two points\noff the line", "m = slope = ΔF/Δa",
            "m = 8.0 N / 3.2 m/s² = 2.5 kg", "s34_graph_problem.png"),
]),
"3.5": ("Net Force & Acceleration", [
    title(5, "3.5", "Net Force & Acceleration", "Go from a free body diagram to a net force to an acceleration.",
          "an elevator shaft seen from below, cables catching the light"),
    {"master": "05_PROCESS_TIMELINE",
     "fields": {"headline": "From FBD to Acceleration",
                "subhead": "Example: a 10 kg cart is pulled 50 N right and 20 N left.",
                "s1_l": "Draw", "s1_b": "FBD, every force labeled.",
                "s2_l": "Axes", "s2_b": "Pick + and write it down.",
                "s3_l": "Sum", "s3_b": "Fnet = 50 − 20 = 30 N",
                "s4_l": "Solve", "s4_b": "a = 30/10 = 3.0 m/s²"},
     "images": {"band": A + "s35_chain.png"}},
    problem("Pulling at an Angle", "Frictionless ice. Only the horizontal part of the pull speeds it up.",
            "A 20 kg sled is pulled with 60 N at 35° above horizontal. Find a and the normal force.",
            "m = 20 kg\n60 N at 35°", "a = F cos(angle)/m\nN = mg − F sin(angle)",
            "a = 2.5 m/s² right  ·  N = 162 N", "s35_sled_problem.png"),
    problem("Sliding Down a Frictionless Ramp", "Use down the slope as positive.",
            "An 8.0 kg box slides down a frictionless 20° ramp. Find its acceleration.",
            "m = 8.0 kg\nangle = 20°", "Fnet = mg sin(angle)\na = g sin(angle)",
            "a = 3.4 m/s² down the ramp", "s35_incline_problem.png"),
    grouped("Elevators and Apparent Weight", "A bathroom scale measures how hard it pushes up on you.",
            "WHAT THE SCALE READS", "The normal force N,\nnot your weight.",
            "AT REST OR CONSTANT v", "Fnet = 0, so N = mg.\nThe scale reads your\ntrue weight.",
            "Accelerating elevator: N − mg = ma, with up as positive.", "s35_elevator_concept.png"),
    problem("Elevator Speeding Up, Going Up", "Use up as positive. True weight: 686 N.",
            "A 70 kg person stands on a scale in an elevator accelerating up at 2.0 m/s². Find the reading.",
            "m = 70 kg\na = +2.0 m/s²", "N − mg = ma\nN = m(g + a)",
            "Scale reads 826 N, more than 686 N", "s35_elevator_up.png"),
    problem("Elevator Accelerating Down", "Use up as positive, so the acceleration is negative.",
            "The same 70 kg person rides an elevator accelerating down at 2.0 m/s². Find the reading.",
            "m = 70 kg\na = −2.0 m/s²", "N − mg = ma\nN = m(g − 2.0)",
            "Scale reads 546 N, less than 686 N", "s35_elevator_down.png"),
]),
"3.6": ("Frictional Forces", [
    title(6, "3.6", "Frictional Forces", "Find friction from the normal force, and decide whether an object slides.",
          "a heavy wooden crate on a rough concrete floor, scuff marks behind it"),
    {"master": "07_COMPARISON_CARDS",
     "fields": {"headline": "Friction", "subhead": "Friction acts along the surface and opposes sliding.",
                "k1_l": "DIRECTION", "k1_b": "Along the surface,\nagainst the sliding\n(or the would-be sliding).",
                "k2_l": "STATIC", "k2_b": "Holds a resting object.\nMatches the push, up to\nfs,max = μs N.",
                "k3_l": "KINETIC", "k3_b": "Acts while sliding.\nfk = μk N, constant.\nUsually less than fs,max.",
                "mustwrite": "Friction = μN. It depends on the normal force, not directly on the weight."},
     "images": {"aside": A + "s36_friction_aside.png"}},
    problem("Constant Velocity", "Constant velocity means Fnet = 0, so friction equals the push.",
            "A 40 kg box is pushed across the floor at constant velocity with 120 N. Find μk.",
            "m = 40 kg\npush = 120 N\nconstant velocity", "fk = push\nμk = fk/N",
            "μk = 120 N / 392 N = 0.31", "s36_constant_v.png"),
    problem("Will It Move?", "Compare the push with the maximum static friction first.",
            "A 25 kg box is pushed with 90 N. Does it move? If the push rises to 110 N, find a.",
            "m = 25 kg\nμs = 0.40, μk = 0.30", "fs,max = μs N\nfk = μk N",
            "90 N: no motion  ·  110 N: a = 1.5 m/s²", "s36_static.png"),
    problem("Pulling at an Angle with Friction", "The upward part of the pull lowers N, and lowers friction.",
            "A 30 kg crate is pulled with 150 N at 30° above horizontal. μk = 0.25. Find N and a.",
            "m = 30 kg, μk = 0.25\n150 N at 30°", "N = mg − F sin(angle)\nFnet = F cos(angle) − μk N",
            "N = 219 N  ·  a = 2.5 m/s²", "s36_angle_pull.png"),
    diagram("Friction on an Incline", "Same tilted axes as 3.3, plus one more force along the slope.", [
        ("FRICTION'S DIRECTION", "Up the slope, against the sliding."),
        ("NORMAL FORCE", "N = mg cos(angle), the same as in 3.3."),
        ("THE TEST", "Slides only if mg sin(angle) > μs N."),
    ], "s36_incline_fbd.png"),
    problem("Does the Block Slide?", "Run the test first. Use down the slope as positive.",
            "A 10 kg block rests on a 35° incline. μs = 0.50, μk = 0.40. Does it slide? If so, find a.",
            "m = 10 kg, angle = 35°\nμs = 0.50, μk = 0.40", "test: mg sin vs μs N\nFnet = mg sin − μk N",
            "Slides (56.2 N > 40.1 N)  ·  a = 2.4 m/s²", "s36_incline_problem.png"),
]),
"3.7": ("Multi-Body Systems", [
    title(7, "3.7", "Multi-Body Systems", "Solve pulley systems as one object for a, then one mass alone for tension.",
          "a steel pulley wheel and rope hanging in a workshop"),
    grouped("Ideal Strings and Pulleys", "Massless string, frictionless pulley: the string just changes direction.",
            "WHAT IS THE SAME", "One tension T all\nalong the string.\nOne size of a for all.",
            "TWO WAYS TO SOLVE", "System: a = Fnet/total m.\nThen one mass alone\nfor T.",
            "Solve the whole system for a first, then one mass alone for T.", "s37_ideal.png"),
    problem("Atwood Machine", "The heavier mass goes down. Use its direction as positive.",
            "A 5.0 kg mass and a 3.0 kg mass hang over a pulley. Find a and the string tension.",
            "m1 = 5.0 kg\nm2 = 3.0 kg", "a = (m1 − m2)g/(m1 + m2)\nT = m2(g + a)",
            "a = 2.45 m/s²  ·  T = 36.8 N", "s37_atwood_problem.png"),
    problem("Block on a Table", "Frictionless table. Only the hanging weight drives the system.",
            "A 4.0 kg block on a table is tied over a pulley to a 2.0 kg hanging mass. Find a and T.",
            "block 4.0 kg\nhanging 2.0 kg", "a = m2 g/(m1 + m2)\nT = m1 a",
            "a = 3.27 m/s²  ·  T = 13.1 N", "s37_table_problem.png"),
    problem("Block on a Table, with Friction", "Same setup, now μk = 0.20 between block and table.",
            "Repeat the table problem with μk = 0.20. Find a and T.",
            "block 4.0 kg, μk = 0.20\nhanging 2.0 kg", "Fnet = m2 g − μk m1 g\nT = m1 a + fk",
            "a = 1.96 m/s²  ·  T = 15.7 N", "s37_table_friction.png"),
    problem("Challenge: Incline and Pulley", "Frictionless incline. Decide which way it moves first.",
            "A 6.0 kg block on a 30° incline is tied over a pulley to a 5.0 kg hanging mass. Find a and T.",
            "block 6.0 kg, 30°\nhanging 5.0 kg", "Fnet = m2 g − m1 g sin(angle)\nT = m2(g − a)",
            "a = 1.78 m/s²  ·  T = 40.1 N", "s37_incline_pulley.png"),
]),
}


def main():
    for code, (name, slides) in DECKS.items():
        spec = {"course": "physics", "unit": 3, "section": code, "sectionTitle": name,
                "note": "Outline approved by Matt 2026-11-04. Problem slides show problem, diagram and final answer "
                        "together; full worked steps are in the Unit 3 slide solutions key.",
                "slides": slides}
        out = os.path.join(HERE, f"phys_u03_s0{code}.json")
        json.dump(spec, open(out, "w"), indent=2, ensure_ascii=False)
        print(out, len(slides))
    print("total", sum(len(s) for _, s in DECKS.values()))


if __name__ == "__main__":
    main()
