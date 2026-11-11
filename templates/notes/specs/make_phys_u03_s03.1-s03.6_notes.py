"""Generate the Physics U3 guided-notes student and key specs (paged schema).

    python3 templates/notes/specs/make_phys_u03_s03.1-s03.6_notes.py
    python3 templates/notes/specs/make_phys_u03_s03.1-s03.6_notes.py --all-examples DIR

One source, so the key is the student structure with answers filled and the two cannot
drift: `build(key)` runs the same code twice and only the blanks change. Edit this file,
not the JSON it writes.

Wording, order, numbers and equation forms follow the Unit 3 deck (Forces and Motion,
47 slides). Section numbering follows the deck's six sections, Matt's decision of
2026-11-10 (SHULL-CHG-0068 pending for DECISIONS.md). Each block's first cue line names
the slide(s) it captures, so a student looking at a slide knows which blank it fills.

Page budget: two sheets at most per section. A few worked examples do not fit that budget
and are left to the board (BOARD below; the default build). `--all-examples DIR` writes
the same specs with every example included, to DIR, so the cost can be measured.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "phys_u03_s03.1-s03.6_notes"
sys.path.insert(0, os.path.dirname(HERE))
import recall  # noqa: E402

# Worked examples left to the board in the budget build, by slide number. Each is listed
# with its reason in the build report; the slide still carries the full solution.
BOARD = {14, 17, 27, 32}
ALL = "--all-examples" in sys.argv

THETA = "θ"        # not in Archivo - see the build report


def blank(ans):
    """Underscores sized to the answer: handwriting runs wider than type."""
    return "_" * max(5, round(len(ans) * 1.1) + 2)


def F(text, key):
    """`{answer}` marks a blank. Student: underscores sized to it. Key: the answer, bold."""
    return re.sub(r"\{([^}]*)\}",
                  (lambda m: f"**{m.group(1)}**") if key else (lambda m: blank(m.group(1))),
                  text)


NBSP = "\u00a0"


def nb(eq):
    """An equation that must not break across lines: its spaces become no-break spaces."""
    return eq.replace(" ", NBSP)


RECALL_CUES = ["Close your notes before you write.",
               "Use the checklist to find what still needs practice."]


def build(key, board):
    f = lambda t: F(t, key)
    T = THETA

    def P(prompt, answer, lines=None):
        """A prompt naming what to write, with ruled lines sized to the key's answer. The key
        prints the deck's sentence or equation in the writing area. No inline blanks
        (Matt, 2026-11-11: "I just really dont like fill in the blanks")."""
        n = lines or (1 if len(answer) <= 60 else 2 if len(answer) <= 150 else 3)
        d = {"prompt": prompt, "lines": n}
        if key:
            d["answer"] = answer
        return d

    def ex(slides, title, given, find, answer, solution, cues=(), notes=(), height=1.4):
        # Given and Find share a line when both fit on it (about 100 characters at 10 pt
        # across the 6.02 in capture side); otherwise Find gets its own line.
        if len(given) == 1 and len(given[0]) + len(find) <= 95:
            prob = {"given": [given[0] + "     **Find:** " + find]}
        else:
            prob = {"given": given, "find": find}
        # Student: an "Answer:" label with open space beside it. Key: the full answer.
        prob["answer"] = "**Answer:**  " + F(answer, True).replace("**", "") if key \
            else "**Answer:**"
        if height > 1.4:
            prob["workHeightIn"] = height
        if key:
            prob["solution"] = solution
        return {"kind": "example", "title": title, "_slides": slides,
                "cues": [f"Slide {slides}"] + list(cues), "problem": prob,
                "notes": [P(*n) for n in notes],
                "extraNotes": False}

    def notes(slides, title, lines, cues=(), extra=True):
        label = f"Slides {slides}" if "–" in str(slides) else f"Slide {slides}"
        row = {"title": title, "_slides": slides, "cues": [label] + list(cues),
               "notes": lines}
        if not extra:
            row["extraNotes"] = False
        return row

    def qr(q, a):                               # quick recall: the key adds the answer
        return {"q": q, "a": a} if key else {"q": q}

    def board_cue(n):
        return [f"Slide {n}: worked on the board."] if n in board else []

    def rc(prompt, answer, checks, lines=3):
        r = {"kind": "recall", "title": "Section summary", "cues": RECALL_CUES,
             "lines": lines, "prompt": prompt, "selfCheck": checks}
        if key:
            r["answer"] = answer
        return r

    # ------------------------------------------------------------------ 3.1
    s31 = [
        notes("3–4", "Force · Mass and Weight", [
            P("Force: definition and unit",
              "A force is a push or a pull. It is a vector, with a size and a direction, "
              "measured in newtons (N)."),
            P("Mass vs. weight: meaning and units",
              "Mass: how much matter, in kg; stays the same when you travel. Weight: the force "
              "of gravity, in N; changes when gravity changes."),
            P("Weight: equation, g on Earth, and the 10 kg example",
              "Fg = mg, with g = 9.8 m/s² on Earth. 10 kg: 98 N down on Earth, 16 N down on "
              "the Moon."),
        ], cues=["Common mix-up: mass (kg) and weight (N) are different quantities."],
            extra=False),
        ex(5, "Weight on Earth and the Moon",
           ["m = 60 kg;   Earth: g = 9.8 m/s²;   Moon: g = 1.6 m/s²."],
           "weight in each location.",
           "Earth: Fg = {588 N down}      Moon: Fg = {96 N down}",
           ["Fg = mg", "Earth: Fg = 60(9.8) = 588 N down",
            "Moon: Fg = 60(1.6) = 96 N down",
            "Same mass. Different gravity. Different weight."],
           cues=["Same mass, different gravity"]),
        notes("6–8", "Newton’s Three Laws", [
            P("Newton’s 1st law",
              "An object at rest stays at rest, and an object in motion keeps a constant "
              "velocity, unless a net external force acts on it."),
            P("Equilibrium: condition and the two possibilities",
              "Forces balance, ∑F = 0. The object stays at rest, or moves at constant speed "
              "in a straight line."),
            P("Newton’s 2nd law: equation and meaning",
              "∑F = ma, so a = ∑F / m. Net force, ∑F, is the sum of all forces acting on the object. Same mass: more net "
              "force, more acceleration. Same force, twice the mass: half the acceleration."),
            P("Newton’s 3rd law, and why the pair does not cancel",
              "For every action, there is an equal and opposite reaction. The pair acts on two "
              "objects, so it does not cancel on one object’s FBD."),
        ], cues=["Common mix-up: a moving object does not need a net force to keep moving. "
                 "A moving puck keeps going with ∑F = 0."], extra=False),
        rc("State Newton’s three laws in your own words, and write the equation for weight.",
           f"1st: ∑F = 0, no change in velocity. 2nd: {nb('∑F = ma')}. 3rd: equal, "
           f"opposite pairs. {nb('Fg = mg')}.",
           ["I can tell mass (kg) from weight (N) and find weight with Fg = mg.",
            "I can state all three laws and explain equilibrium."], lines=2),
    ]

    # ------------------------------------------------------------------ 3.2
    s32 = [
        notes("10–11", "Free-Body Diagrams · Normal Force", [
            P("Drawing an FBD: the rules",
              "Box or dot; one labeled arrow per force; longer arrow = larger force; no "
              "motion arrows; only forces on the chosen object."),
            P("Common forces: Fg, FN, T",
              "Fg: gravity pulls down. FN: surface pushes perpendicular. T: rope pulls along "
              "the rope."),
            P("Normal force: direction, and when FN = Fg",
              "Perpendicular push from the surface: up on a floor, tilted on a ramp. FN = Fg "
              "only on a level surface, no other vertical forces, no acceleration."),
        ], cues=["Common mix-up: FN does not always equal weight. That needs the level-surface "
                 "conditions below."], extra=False),
        ex(12, "Balanced Forces: Book and Lamp",
           ["2 kg book at rest on a table;   1.5 kg lamp at rest on a rope;   "
            "g = 9.8 m/s²."],
           "the free-body diagram of each, and the upward force on each.",
           "Book: FN = {19.6 N up}      Lamp: T = {14.7 N up}",
           ["Book FBD: FN up, Fg down, equal arrows.   Lamp FBD: T up, Fg down, equal arrows.",
            "Book: FN = Fg = 2(9.8) = 19.6 N up",
            "Lamp: T = Fg = 1.5(9.8) = 14.7 N up"],
           cues=["Two FBDs: book and lamp"], height=1.6),
        ex(13, "Net Force in One Dimension",
           ["crate;   30 N right;   10 N left.   Positive: right."],
           "∑F, with its direction.",
           "∑F = {20 N to the right}",
           ["Right: +30 N     Left: −10 N", "∑F = 30 − 10 = 20 N",
            "20 N to the right"],
           cues=board_cue(14),
           notes=[("Net force: the method",
                   "Pick + direction; add with signs; x and y apart.")]),
        ex(14, "Equilibrium: The Missing Force",
           ["crate;   50 N right;   20 N left;   40 N up;   40 N down.   "
            "Positive: right and up."],
           "the force to add.",
           "Add {30 N to the left}",
           ["Vertical: ∑Fy = 40 − 40 = 0 N",
            "Horizontal: ∑Fx = 50 − 20 = 30 N right",
            "For equilibrium: add 30 N to the left."]),
        ex(15, "Resultant Force and Direction",
           ["40 N right (+x) and 30 N up, perpendicular."],
           "the size and direction of the resultant.",
           f"∑F = {{50 N}}  at  {T} = {{36.9° above +x}}",
           ["∑F = √(40² + 30²) = 50 N",
            f"{T} = tan⁻¹(30/40) = 36.9°", "50 N, 36.9° above +x"]),
        ex(16, "Breaking a Force into Components",
           ["F = 100 N pulling 30° above the horizontal."],
           "the horizontal and vertical components.",
           "Fx = {86.6 N horizontal, toward the pull}      Fy = {50.0 N up}",
           [f"Fx = F cos {T} = 100 cos 30° = 86.6 N horizontal, toward the pull",
            f"Fy = F sin {T} = 100 sin 30° = 50.0 N up",
            "Check: √(86.6² + 50.0²) ≈ 100 N"],
           notes=[("Components of an angled force", f"Fx = F cos {T};   Fy = F sin {T}")]),
        ex(17, "One Angled Force and One Straight Force",
           ["top view;   80 N at 40° above +x;   30 N left.   Positive: +x right, "
            "+y up the page."],
           "the net force and its direction.",
           f"∑F ≈ {{60 N}}  at  {T} ≈ {{59° above +x}}",
           ["Fx = 80 cos 40° − 30 = 31.3 N", "Fy = 80 sin 40° = 51.4 N",
            "∑F = √(31.3² + 51.4²) ≈ 60 N", f"{T} = tan⁻¹(51.4/31.3) ≈ 59°"]),
        ex(18, "Two Angled Forces: Tugboats",
           ["top view;  500 N at 30° above +x;  400 N at 45° above −x.  "
            "Positive: +x right, +y up the page."],
           "the net force on the barge and its direction.",
           f"∑F ≈ {{554 N}}  at  {T} ≈ {{74° above +x}}",
           ["Fx = 500 cos 30° − 400 cos 45° = 150 N",
            "Fy = 500 sin 30° + 400 sin 45° = 533 N",
            "∑F = √(150² + 533²) ≈ 554 N", f"{T} = tan⁻¹(533/150) ≈ 74°"],
           cues=["Check the quadrant before reporting an angle"] + board_cue(17)),
        rc("Summarize how to find the net force from a free-body diagram, including a force "
           "at an angle.",
           f"One arrow per force; choose a positive direction. Split angled forces with "
           f"{nb('Fx = F cos θ')} and {nb('Fy = F sin θ')}, add each direction with signs, "
           f"then combine with {nb('√(Fx² + Fy²)')}.",
           ["I can draw an FBD with one labeled arrow per force.",
            "I can add forces with signs and split an angled force into components."],
           lines=2),
    ]

    # ------------------------------------------------------------------ 3.3
    s33 = [
        notes("20–21", "Gravity on a Ramp · Normal Force on an Incline", [
            P("Ramp axes and the weight components",
              f"One axis along the ramp, one perpendicular. Fg,parallel = mg sin {T} down the "
              f"slope; Fg,perp = mg cos {T} into the surface."),
            P("FN on a ramp: equation, condition, steepness",
              f"FN = mg cos {T} (no extra perpendicular force or acceleration). Steeper ramp, "
              "less support: 15°: 0.97mg; 60°: 0.50mg."),
        ], cues=[f"Common mix-up: on a ramp FN is mg cos {T}, less than the weight."],
            extra=False),
        ex(22, "Incline Example: A 5 kg Block",
           ["m = 5 kg;   frictionless 30° ramp;   g = 9.8 m/s²."],
           "FBD, Fg,parallel, Fg,perp, and FN.",
           "Fg,parallel = {24.5 N} down the ramp    Fg,perp = {42.4 N} into the ramp    "
           "FN = {42.4 N} out",
           ["FBD: Fg down, FN perpendicular out of the ramp; Fg split into Fg,parallel and "
            "Fg,perp.",
            "Fg = mg = 5(9.8) = 49 N", "Fg,parallel = 49 sin 30° = 24.5 N down the ramp",
            "Fg,perp = 49 cos 30° = 42.4 N into the ramp",
            "FN = 42.4 N, perpendicular out of the ramp"]),
        ex(23, "Incline Example: A Push Up the Ramp",
           ["m = 12 kg;  frictionless 25° ramp;  30 N push uphill.  Positive: downhill."],
           "Fg,parallel and ∑F.",
           "Fg,parallel = {49.7 N downhill}      ∑F = {19.7 N down the ramp}",
           ["Fg,parallel = 12(9.8) sin 25° = 49.7 N downhill",
            "∑F = 49.7 − 30 = 19.7 N", "19.7 N down the ramp"]),
        rc("Describe how to split the weight on a ramp, and how FN changes as the ramp gets "
           "steeper.",
           f"{nb('Fg,parallel = mg sin θ')}, {nb('Fg,perp = mg cos θ')}, "
           f"{nb('FN = mg cos θ')}. Steeper ramp: smaller FN.",
           [f"I can write Fg,parallel = mg sin {T} and Fg,perp = mg cos {T}.",
            "I can find FN and the net force along a ramp."], lines=2),
    ]

    # ------------------------------------------------------------------ 3.4
    s34 = [
        ex(25, "Calculating Acceleration",
           ["m = 4 kg;   ∑F = 12 N to the right."],
           "the acceleration.",
           "a = {3.0 m/s² right}",
           ["∑F = ma, so a = ∑F / m", "a = 12 N / 4 kg", "a = 3.0 m/s² right"],
           notes=[("1 N in base units; direction of a",
                   "1 N = 1 kg·m/s². a points in the direction of ∑F.")]),
        ex(26, "A Car Accelerates",
           ["m = 1500 kg;   4500 N forward;   1200 N drag (backward).   Positive: forward."],
           "∑F and a.",
           "∑F = {3300 N forward}      a = {2.2 m/s² forward}",
           ["∑F = 4500 − 1200 = 3300 N forward", "a = ∑F / m = 3300 / 1500",
            "a = 2.2 m/s² forward"], cues=board_cue(27)),
        ex(27, "From a Diagram to Acceleration",
           ["10 kg cart;   50 N push right;   20 N opposing force left.   Positive: right."],
           "∑F and a.",
           "∑F = {30 N right}      a = {3.0 m/s² right}",
           ["∑F = 50 − 20 = 30 N right", "a = ∑F / m = 30 / 10",
            "a = 3.0 m/s² right"]),
        ex(28, "A Sled Pulled at an Angle",
           ["m = 20 kg;   60 N pull at 35° above horizontal;   ignore friction.   "
            "Positive: +x (right) and up."],
           "the acceleration and the normal force.",
           "a = {2.46 m/s² right}      FN ≈ {162 N up}",
           ["Fx = 60 cos 35° = 49.1 N", "a = Fx / m = 49.1 / 20 = 2.46 m/s² right",
            "Vertical: FN + 60 sin 35° − mg = 0", "FN = 196 − 34.4 ≈ 162 N up"],
           cues=["FN here is less than mg"]),
        ex(29, "Acceleration Down a Frictionless Ramp",
           ["m = 8 kg;   frictionless 20° ramp.   Positive: downhill."],
           "the acceleration.",
           "a = {3.35 m/s² downhill}",
           [f"∑F = mg sin {T}", f"ma = mg sin {T}",
            f"Mass cancels: a = g sin {T} = 9.8 sin 20°", "a = 3.35 m/s² downhill"],
           notes=[("Frictionless ramp: acceleration",
                   f"a = g sin {T}; it does not depend on mass.")]),
        notes(30, "Elevators and Apparent Weight", [
            P("Apparent weight: what a scale reads", "The upward normal force, FN."),
            P("Elevator equation (up positive) and the a = 0 case",
              "FN − mg = ma. At rest or constant velocity, a = 0, so FN = mg."),
            P("Scale reading: what changes it",
              "Acceleration, not simply moving up or down."),
        ], cues=["In an elevator, FN equals mg only when a = 0."], extra=False),
        ex(31, "Elevator Accelerating Up",
           ["m = 70 kg;   a = 2.0 m/s² upward.   Positive: up."],
           "the scale reading.",
           "FN = {826 N up}",
           ["Weight: mg = 70(9.8) = 686 N", "FN − mg = ma", "FN = 686 + 70(2.0)",
            "FN = 826 N up"], cues=board_cue(32)),
        ex(32, "Elevator Accelerating Down",
           ["m = 70 kg;   a = 2.0 m/s² downward.   Positive: up, so a = −2.0 m/s²."],
           "the scale reading.",
           "FN = {546 N up}",
           ["Up is positive: a = −2.0 m/s²", "FN − mg = ma", "FN = 686 + 70(−2.0)",
            "FN = 546 N up"]),
        rc("List the steps from a free-body diagram to an acceleration. Add how a scale "
           "reading changes in an accelerating elevator.",
           f"Choose a positive direction, add the forces to get ∑F, then {nb('a = ∑F / m')} "
           f"in the direction of ∑F. The scale reads FN; {nb('FN − mg = ma')}, so FN changes "
           "when a ≠ 0.",
           ["I can find a from ∑F = ma, with units and direction.",
            "I can find a scale reading with FN − mg = ma."], lines=2),
    ]

    # ------------------------------------------------------------------ 3.5
    s35 = [
        notes("34–35", "Static and Kinetic Friction · Comparing Coefficients", [
            P("Friction: definition",
              "Opposes sliding, or the tendency to slide, between surfaces."),
            P("Static vs. kinetic friction: equations",
              "Static (not sliding): fs matches the needed force, up to fs,max = μsFN; at rest "
              "with a 20 N push, fs = 20 N opposite the push. Kinetic (sliding): fk ≈ μkFN, "
              "usually smaller."),
            P("μ: units, and what a higher value means",
              "No units. At the same FN, higher μk means more sliding friction (shoes on ice "
              "0.05; knee joint 0.015)."),
        ], cues=["Table values are approximate (OpenStax)"]),
        ex(36, "Friction at Constant Velocity",
           ["m = 40 kg;   level floor;   constant velocity;   120 N horizontal push."],
           "FN, fk, and μk.",
           "FN = {392 N up}     fk = {120 N opposite the push}     μk ≈ {0.31}",
           ["Vertical balance: FN = mg = 40(9.8) = 392 N up",
            "Constant velocity: a = 0, so fk = 120 N, opposite the push",
            "μk = fk / FN = 120 / 392 ≈ 0.31 (no units)"]),
        ex(37, "Static or Sliding: The 25 kg Box",
           ["m = 25 kg, starts at rest;   μs = 0.40;   μk = 0.30;   pushes of 90 N and "
            "110 N.   Positive: the push direction."],
           "whether the box moves for each push, and the acceleration for 110 N.",
           "90 N: {stays at rest}      110 N: {slides}, a = {1.46 m/s²} in the push direction",
           ["FN = 25(9.8) = 245 N;   fs,max = 0.40(245) = 98 N",
            "90 N < 98 N: static friction is 90 N. The box stays at rest.",
            "110 N > 98 N: the box slides. fk = 0.30(245) = 73.5 N",
            "∑F = 110 − 73.5 = 36.5 N;   a = 36.5 / 25 = 1.46 m/s²"], height=1.6),
        ex(38, "Angled Pull with Friction",
           ["m = 30 kg, sliding;   150 N rope at 30° above horizontal;   μk = 0.25.   "
            "Positive: +x (horizontal, toward the pull) and up."],
           "FN, fk, and a.",
           "FN = {219 N} up    fk = {54.75 N} opposite the motion    a = {2.51 m/s² in +x}",
           ["FN = mg − F sin 30° = 294 − 75 = 219 N up",
            "fk = 0.25(219) = 54.75 N, opposite the motion", "∑F = 150 cos 30° − 54.75 = 75.15 N",
            "a = 75.15 / 30 = 2.51 m/s² in +x"]),
        notes(39, "Friction on an Incline", [
            P("Friction on a ramp: direction and equations",
              f"Up the ramp for a block sliding down. FN = mg cos {T}; fs,max = μsFN; "
              "fk ≈ μkFN. Reverses if sliding reverses."),
            P("Condition to start sliding down", f"mg sin {T} > μsFN"),
        ], extra=False),
        ex(40, "Sliding Down the Ramp: The 10 kg Block",
           ["m = 10 kg, at rest;  35° ramp;  μs = 0.50;  μk = 0.40.  Positive: downhill."],
           "if it slides, and a.",
           "Slides: {yes}      a = {2.41 m/s² downhill}",
           ["Fg,parallel = 10(9.8) sin 35° = 56.2 N;   FN = 10(9.8) cos 35° = 80.3 N",
            "fs,max = 0.50(80.3) = 40.1 N.   56.2 > 40.1, so it slides.",
            "fk = 0.40(80.3) = 32.1 N",
            "a = (56.2 − 32.1)/10 = 2.41 m/s² downhill"], height=1.6),
        rc("Explain how to decide whether an object at rest starts to slide, and how to find "
           "its acceleration once it does.",
           f"Compare the push (or {nb('mg sin θ')} on a ramp) with {nb('fs,max = μsFN')}. If it "
           f"is larger, it slides: use {nb('fk = μkFN')}, find ∑F, then {nb('a = ∑F / m')}.",
           ["I can tell static from kinetic friction and use fs,max = μsFN.",
            "I can find friction and acceleration on level ground and on a ramp."]),
    ]

    # ------------------------------------------------------------------ 3.6
    s36 = [
        ex(42, "Streetlight Cable Tension",
           ["20 kg streetlight at rest;   left cable 30° above horizontal;   right cable 60°;",
            "ignore cable mass.   Positive: right and up."],
           "the tension in each support cable.",
           "FTL = {98.0 N}    FTR ≈ {170 N}    each {along its cable, toward its support}",
           ["At rest: ∑Fx = 0, ∑Fy = 0;   Fdown = mg = 20(9.8) = 196 N",
            "Horizontal: FTR cos 60° = FTL cos 30°, so FTL = 0.577FTR",
            "Vertical: FTL sin 30° + FTR sin 60° = 196",
            "(0.577FTR)(0.5) + 0.866FTR = 196",
            "FTR ≈ 170 N     FTL = 98.0 N, each along its cable, toward its support"],
           notes=[("Cable with more tension", "The steeper cable.")], height=1.8),
        notes(43, "Ideal Strings and Pulleys", [
            P("Ideal string and pulley",
              "Massless, taut rope that does not stretch; massless, frictionless pulley."),
            P("Fixed-pulley rules and the method",
              "Same tension T and same size of a for both objects. Find a from the whole "
              "system, then T from one object. Separate FBD for each object."),
        ]),
        ex(44, "Atwood Machine",
           ["m₁ = 5 kg, m₂ = 3 kg, both hanging.   Positive: the motion (5 kg down, "
            "3 kg up)."],
           "a and T.",
           "a = {2.45 m/s²} (5 kg down, 3 kg up)      T = {36.8 N}",
           ["∑F = (5 − 3)(9.8) = 19.6 N", "Whole system: a = 19.6 / (5 + 3) = 2.45 m/s² (5 kg down, 3 kg up)",
            "Use the 3 kg mass: T − 3g = 3a", "T = 3(9.8 + 2.45) = 36.8 N"]),
        ex(45, "A Block on a Frictionless Table",
           ["m₁ = 4 kg on the table;   m₂ = 2 kg hanging.   Positive: the motion."],
           "a and T.",
           "a = {3.27 m/s²} (2 kg down, 4 kg toward the pulley)      T ≈ {13.1 N}",
           ["Driving force: ∑F = m₂g = 2(9.8) = 19.6 N",
            "Whole system: a = 19.6 / (4 + 2) = 3.27 m/s² (2 kg down, 4 kg toward the pulley)",
            "Table block: T = m₁a = 4(3.27) ≈ 13.1 N"],
           cues=["Hanging mass accelerates down; table block, toward the pulley"]),
        ex(46, "The Same System with Friction",
           ["m₁ = 4 kg on the table, μk = 0.20;   m₂ = 2 kg hanging.   Positive: the motion."],
           "fk, a, and T.",
           "fk = {7.84 N} away from the pulley    a = {1.96 m/s²} (2 kg down, 4 kg toward the pulley)    "
           + nb("T = {15.7 N}"),
           ["fk = μkm₁g = 0.20(4)(9.8) = 7.84 N, away from the pulley",
            "Whole system: a = (19.6 − 7.84) / 6 = 1.96 m/s² (2 kg down, 4 kg toward the pulley)",
            "Table block: T − fk = m₁a", "T = 4(1.96) + 7.84 = 15.7 N"]),
        ex(47, "Challenge: Incline and Pulley",
           ["m₁ = 6 kg on a frictionless 30° ramp;   m₂ = 5 kg hanging.   Positive: the "
            "motion (5 kg down, 6 kg up the ramp)."],
           "a and T.",
           "a = {1.78 m/s²} (5 kg down, 6 kg up the ramp)      T ≈ {40.1 N}",
           ["Hanging: 5(9.8) = 49.0 N;   along ramp: 6(9.8) sin 30° = 29.4 N",
            "Whole system: a = (49.0 − 29.4) / (5 + 6) = 1.78 m/s² (5 kg down, 6 kg up the ramp)",
            "Hanging mass: 5g − T = 5a", "T = 5(9.8 − 1.78) ≈ 40.1 N"]),
        rc("Write the two-step method for objects joined by a rope over a pulley.",
           f"Whole system: a = driving force / total mass. Then {nb('∑F = ma')} on one "
           "object gives T.",
           ["I can solve a cable-tension problem with ∑Fx = 0 and ∑Fy = 0.",
            "I can find a and T for an Atwood machine and a table-and-pulley system."], lines=2),
    ]

    secs = [
        ("3.1", "Newton’s Laws",
         "I can state Newton’s three laws and use Fg = mg to find an object’s weight.",
         s31),
        ("3.2", "Free-Body Diagrams",
         "I can draw a free-body diagram and find the net force on an object, including "
         "forces at an angle.", s32),
        ("3.3", "Forces on an Incline",
         "I can split an object’s weight into parts along and into a ramp and find the "
         "normal force.", s33),
        ("3.4", "Net Force and Acceleration",
         "I can use ∑F = ma to find acceleration, including on a ramp and in an elevator.",
         s34),
        ("3.5", "Friction",
         "I can tell static from kinetic friction and find friction, net force and "
         "acceleration on level ground and on a ramp.", s35),
        ("3.6", "Connected Objects",
         "I can find tension and acceleration for objects joined by cables, ropes and "
         "pulleys.", s36),
    ]

    sections = []
    for code, title, lt, rows in secs:
        rows = [r for r in rows if not (r.get("kind") == "example" and r["_slides"] in board)]
        split = [1] * len(rows) if os.environ.get("MEASURE") else BREAKS[ALL][code]
        pages, i = [], 0
        for n in split:
            pages.append({"rows": rows[i:i + n]})
            i += n
        assert i == len(rows), (code, i, len(rows))
        sections.append({"code": code, "title": title, "learningTarget": lt, "pages": pages})

    spec = {
        "course": "physics",
        "unit": 3,
        "key": key,
        "cover": {
            "sections": [{"code": c, "difficulty": d} for c, d in DIFFICULTY],
            "difficultyNote": "Estimated difficulty: 1 = introductory; 10 = highly challenging.",
            "equationToolbox": {
                "label": "Equation toolbox",
                "columns": [
                    {"heading": "Newton’s laws",
                     "lines": ["Fg = mg", "∑F = ma",
                               {"lhs": "a", "num": "∑F", "den": "m"},
                               "FN − mg = ma  (up is positive)"]},
                    {"heading": "Components",
                     "lines": [f"Fx = F cos {T}", f"Fy = F sin {T}",
                               "∑F = √(Fx² + Fy²)", f"{T} = tan⁻¹(Fy/Fx)"]},
                    {"heading": "Ramps and friction",
                     "lines": [f"Fg,parallel = mg sin {T}", f"Fg,perp = mg cos {T}",
                               f"FN = mg cos {T}  (ramp, no other perpendicular force)",
                               "fs,max = μsFN", "fk ≈ μkFN"]},
                ],
                "notes": ["∑F means net force (the slides write Fnet).",
                          "g = 9.8 m/s² on Earth.   1 N = 1 kg·m/s².   μ has no units.   "
                          f"Frictionless ramp: a = g sin {T}."],
            },
            "keyTerms": [
                {"code": "3.1", "terms": ["Force", "newton (N)", "mass", "weight",
                                          "equilibrium", "net force"]},
                {"code": "3.2", "terms": ["Free-body diagram", "normal force", "tension",
                                          "resultant", "components"]},
                {"code": "3.3", "terms": ["Incline", "Fg,parallel", "Fg,perp"]},
                {"code": "3.4", "terms": ["Acceleration", "apparent weight"]},
                {"code": "3.5", "terms": ["Static friction", "kinetic friction",
                                          "coefficient of friction (μ)"]},
                {"code": "3.6", "terms": ["Ideal string", "pulley", "Atwood machine"]},
            ],
            "howToUse": "The left column names the slide each block comes from. While that "
                        "slide is up, write each idea in your own words on the lines under "
                        "its prompt. In each work box, state your positive direction and "
                        "carry units to the answer.",
        },
        "sectionsContent": sections,
        "conceptReview": {
            "title": "Unit 3 / Concept Review",
            "subtitle": "Connect the ideas, check common mix-ups, and explain the physics in "
                        "your own words.",
            "sections": [
                {"code": "3.1", "heading": "Newton’s laws",
                 "paragraphs": [["Mass (kg) stays the same from place to place; weight, Fg = mg (N), "
                                 "depends on g. ∑F = 0: constant velocity."]],
                 "watchOut": "A moving object does not need a net force to keep moving."},
                {"code": "3.2", "heading": "Free-body diagrams",
                 "paragraphs": [["One object, one labeled arrow per force. Add with signs; "
                                 "split an angled force into Fx = F cos θ and Fy = F sin θ."]],
                 "watchOut": "Third-law pairs act on two objects, so they never cancel on "
                             "one FBD."},
                {"code": "3.3", "heading": "Forces on an incline",
                 "paragraphs": [["Tilt the axes: Fg,parallel = mg sin θ, Fg,perp = mg cos θ. "
                                 "FN = mg cos θ (ramp, no other perpendicular force)."]],
                 "watchOut": "Normal force does not always equal weight. A steeper ramp gives "
                             "a smaller FN."},
                {"code": "3.4", "heading": "Net force and acceleration",
                 "paragraphs": [["a = ∑F / m, in the direction of ∑F. Frictionless ramp: "
                                 "a = g sin θ. Elevator, up positive: FN − mg = ma."]],
                 "watchOut": "The scale reads FN, which changes with acceleration, not with "
                             "moving up or down."},
                {"code": "3.5", "heading": "Friction",
                 "paragraphs": [["Static friction matches the need, up to fs,max = μsFN. "
                                 "Sliding friction, fk ≈ μkFN, is usually smaller."]],
                 "watchOut": "Find FN first. An angled pull or a ramp changes it."},
                {"code": "3.6", "heading": "Connected objects",
                 "paragraphs": [["Ideal rope: one tension T, one size of a. Find a from the "
                                 "whole system, then T from one object’s ∑F = ma."]],
                 "watchOut": "Draw a separate FBD for each object."},
            ],
            "quickRecall": [
                qr("State the condition for equilibrium.", "∑F = 0: forces balance."),
                qr("Write the weight components for a block on a ramp.",
                   "Fg,parallel = mg sin θ; Fg,perp = mg cos θ."),
                qr("Explain why a scale reads more in an elevator accelerating up.",
                   "Up positive: FN − mg = ma with a > 0, so FN > mg."),
            ],
        },
    }
    return spec


DIFFICULTY = [("3.1", 3), ("3.2", 6), ("3.3", 5), ("3.4", 6), ("3.5", 7), ("3.6", 8)]

# Blocks per page, after board examples are removed (False) or with all examples (True).
BREAKS = {
    False: {"3.1": [2, 2], "3.2": [3, 4], "3.3": [4], "3.4": [3, 4], "3.5": [3, 4],
            "3.6": [3, 4]},
    True: {"3.1": [2, 2], "3.2": [3, 4, 2], "3.3": [4], "3.4": [3, 4, 2], "3.5": [3, 4],
           "3.6": [3, 4]},
}


def strip_private(node):
    if isinstance(node, dict):
        return {k: strip_private(v) for k, v in node.items() if not k.startswith("_")}
    if isinstance(node, list):
        return [strip_private(x) for x in node]
    return node


def shape(n):
    if isinstance(n, dict):
        return {k: shape(v) for k, v in n.items() if k not in ("answer", "solution", "key", "a")}
    if isinstance(n, list):
        return [shape(x) if not isinstance(x, str) else "s" for x in n]
    return type(n).__name__


def recall_offences(spec):
    """recall.py reads `rows` under a section; a paged spec keeps them under `pages`, so the
    builder's own check does not reach them. Flatten and run the same rule here, plus the
    block titles (the cue labels)."""
    flat = {"sectionsContent": [
        {"code": s["code"], "rows": [r for p in s["pages"] for r in p["rows"]]}
        for s in spec["sectionsContent"]]}
    found = recall.offences(flat)
    for s in flat["sectionsContent"]:
        for r in s["rows"]:
            for n in r.get("notes", []):
                text = n.get("prompt", "") if isinstance(n, dict) else ""
                if recall.QUESTION_MARK.search(text) or recall.OPENER.match(text):
                    found.append((s["code"], "prompt", text))
    for s in flat["sectionsContent"]:
        for r in s["rows"]:
            title = r.get("title", "")
            if recall.QUESTION_MARK.search(title) or recall.OPENER.match(title):
                found.append((s["code"], "title", title))
    return found


if __name__ == "__main__":
    board = set() if ALL else BOARD
    outdir = HERE
    if ALL:
        outdir = sys.argv[sys.argv.index("--all-examples") + 1]
    student = build(False, board)
    key = build(True, board)
    bad = recall_offences(student) + recall_offences(key)
    if bad:
        for b in bad:
            print("recall rule:", b, file=sys.stderr)
        sys.exit(1)
    coverage = []
    for s in student["sectionsContent"]:
        for pi, p in enumerate(s["pages"], 1):
            for r in p["rows"]:
                coverage.append((s["code"], pi, r.get("_slides", "-"), r.get("kind", "notes"),
                                 r["title"]))
    for name, data in (("student", student), ("key", key)):
        with open(os.path.join(outdir, f"{STEM}_{name}.json"), "w") as fh:
            json.dump(strip_private(data), fh, ensure_ascii=False, indent=2)
            fh.write("\n")
    print("structure identical (ignoring answers):",
          json.dumps(shape(strip_private(student)), sort_keys=True)
          == json.dumps(shape(strip_private(key)), sort_keys=True))
    if not ALL:
        print("left to the board:", ", ".join(f"slide {n}" for n in sorted(BOARD)))
    for c in coverage:
        print("   S0%s p%d  slide %-6s %-8s %s" % c)
