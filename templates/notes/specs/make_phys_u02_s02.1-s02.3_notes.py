"""Generate the Physics U2 guided-notes student and key specs (flat schema).

    python3 templates/notes/specs/make_phys_u02_s02.1-s02.3_notes.py

One source, so the key is the student packet with the board notes and worked solutions put in
the boxes and the two cannot drift. Edit this file, not the JSON it writes. Wording follows the
45-slide "Physics Unit 2 - Quantum Gold" deck; every row's cue label names the slides it keys to.
Key text avoids theta and the superscript minus: Archivo has neither glyph.
"""
import json, sys
def row(slides, cues, label, box, statement=None, work=""):
    # No label inside the box: the open space starts at the top edge.
    cues = list(cues)
    if work.startswith("YOUR TURN"): cues.append("Work it first, then check the board")
    p = {"workLabel": "", "workHeightIn": box}
    if statement: p["statement"] = statement
    # `notesLabel` carries the slide's topic; `extraNotes: False` keeps the open space open.
    return {"cueLabel": slides, "cues": cues, "notesLabel": label, "notes": [],
            "extraNotes": False, "problem": p, "_label": label}
EX = "WORKED EXAMPLE — SETUP, STEPS, ANSWER WITH UNITS"
YT = "YOUR TURN — WORK IT FIRST, THEN CHECK THE BOARD"

s21 = [
 row("SLIDE 3", ["Definition of each term", "Magnitude — its range of values"], "VECTOR · MAGNITUDE · DIRECTION", 1.7),
 row("SLIDE 4", ["Tail, tip and scale", "Length as magnitude, angle as direction"], "DRAWING A VECTOR", 2.0, work="SKETCH AND LABEL"),
 row("SLIDE 5", ["The two component equations", "Adjacent side and opposite side"], "RESOLVING A VECTOR INTO COMPONENTS", 2.2, work="SKETCH AND RECORD"),
 row("SLIDES 6–7", ["The setup, before any number"], "EXAMPLE — RESOLVING A DISPLACEMENT", 2.0,
     "A hiker walks 50 m at 30° above the horizontal. Find the x- and y-components.", EX),
 row("SLIDES 8–9", ["Axis angle and compass bearing", "Two names for one direction"], "DEGREES AND COMPASS DIRECTIONS", 2.0, work="SKETCH AND RECORD"),
 row("SLIDES 10–11", ["The relationship between the two angles"], "EXAMPLE — CONVERTING THE ANGLE", 1.5,
     "A vector points 40° North of East. Express its direction as an angle East of North.", EX),
 row("SLIDES 12–13", ["Same method, new numbers"], "YOUR TURN — A HIKING BEARING", 1.5,
     "A hiker walks at 65° East of North. Express this as an angle North of East.", YT),
 row("SLIDE 14", ["Two skills in one problem"], "QUICK CHECK — CONVERT AND RESOLVE", 2.0,
     "A force of 20 N acts at 70° East of North. Find its angle North of East, then resolve its components.", YT),
]
s22 = [
 row("SLIDE 17", ["Tip-to-tail and the resultant", "Magnitude and direction equations", "The condition for this shortcut"], "ADDING PERPENDICULAR VECTORS", 2.4, work="SKETCH AND RECORD"),
 row("SLIDES 18–19", ["Magnitude and direction, both required", "Common error — a magnitude with no direction"], "EXAMPLE — PLANE IN A CROSSWIND", 2.4,
     "A plane flies 80 km/h east relative to the air. A wind blows 20 km/h north. Find the plane’s velocity relative to the ground.", EX),
 row("SLIDE 20", ["The three steps, in order", "Reason components come first"], "ADDING VECTORS AT ANY ANGLE", 2.4, work="SKETCH AND RECORD"),
 row("SLIDES 21–22", ["Add x to x and y to y", "Extra digits kept until the final answer"], "EXAMPLE — TWO FORCES ON A BOX", 3.0,
     "A 40 N force acts east, and a 30 N force acts 60° above east. Find the resultant force.", EX),
 row("SLIDE 23", ["Same three steps"], "YOUR TURN — TWO DISPLACEMENTS", 2.6,
     "Walk 30 m east, then 40 m at 45° above east. Find the resultant displacement.", YT),
 row("ADDED", ["Three vectors, same three steps", "Resolve every vector, then add"], "PRACTICE — THREE FORCES ON A CRATE", 3.2,
     "Three ropes pull on a crate: 30 N east, 40 N north, and 20 N at 30° south of west. Find the resultant force.", YT),
]
s23 = [
 row("SLIDE 26", ["Definition of each term", "Assumptions of the model"], "PROJECTILE · TRAJECTORY · RANGE", 1.8),
 row("SLIDE 27", ["Horizontal velocity with no air resistance", "Inertia as the reason", "Common error — a force is needed to keep it moving sideways"], "NO HORIZONTAL FORCE NEEDED", 1.8, work="SKETCH AND RECORD"),
 row("SLIDE 29", ["Stage 1 — flat launch", "Horizontal and vertical motion, separately", "The time-to-land equation"], "THE FLAT LAUNCH", 2.0, work="SKETCH AND RECORD"),
 row("SLIDES 30–31", ["Vertical motion first, for the shared time", "Horizontal distance from that time"], "EXAMPLE — ROLLING OFF A TABLE", 2.6,
     "A ball rolls off a 0.80 m table at 2.5 m/s. How long until it lands, and how far does it travel horizontally?", EX),
 row("SLIDE 32", ["Same two steps"], "YOUR TURN — OFF A HIGHER SHELF", 2.4,
     "A marble rolls off a 1.25 m shelf at 3.0 m/s. How far from the shelf does it land?", YT),
 row("SLIDE 34", ["Stage 2 — launch angle", "Velocity components", "Time of flight, and when it applies", "The range equation"], "LAUNCHING AT AN ANGLE", 2.2, work="SKETCH AND RECORD"),
 row("SLIDES 35–36", ["Resolve the velocity first", "Time depends on viy, range on both components"], "EXAMPLE — A KICKED SOCCER BALL", 2.8,
     "A ball is kicked at 18 m/s at 30° above level ground. Find its time of flight and range.", EX),
 row("SLIDE 37", ["Resolve first, then the level-ground formulas"], "YOUR TURN — A LAUNCHED ARROW", 2.6,
     "An arrow is shot at 45 m/s at 40° above level ground. Find its range, neglecting air resistance.", YT),
 row("SLIDE 39", ["Stage 3 — different heights", "Conditions at the peak", "Height gained", "Reason the level-ground shortcut fails"], "WHEN LAUNCH AND LANDING DIFFER", 2.4, work="SKETCH AND RECORD"),
 row("SLIDES 40–41", ["Vertical velocity at the peak", "Height above launch, then above ground"], "EXAMPLE — MAX HEIGHT FROM A CLIFF", 2.6,
     "A rock is launched at 20 m/s at 35° from a 15 m cliff. Find its maximum height above the launch point.", EX),
 row("SLIDES 42–43", ["The full position equation", "The quadratic and the root to keep"], "EXAMPLE — LANDING BELOW THE LAUNCH", 2.8,
     "The same rock (20 m/s, 35°, from a 15 m cliff) lands on the ground below. Find its total time of flight.", EX),
 row("SLIDE 44", ["One approach for each stage", "The quantity shared by both axes"], "THREE STAGES, ONE IDEA", 1.8),
]
spec = {
 "course": "physics", "unit": 2, "sections": ["2.1", "2.2", "2.3"],
 "kicker": "GUIDED NOTES · 3 SECTIONS · S2.1 – S2.3",
 "fields": "NAME  ______________________________________   DATE  ______________   PERIOD  _______",
 "unitTargets": [
  "▸  I can describe a vector by its magnitude and direction, and resolve it into components.",
  "▸  I can add vectors, at right angles and at any angle, and report the resultant with a direction.",
  "▸  I can split a projectile’s motion into two axes that share one time.",
  "▸  I can solve flat, angled and different-height launches using one shared time."],
 "keyTerms": [
  "▸  Vector, magnitude, direction, component",
  "▸  Resultant, tip-to-tail",
  "▸  North of East, East of North",
  "▸  Projectile, trajectory, range"],
 "howItWorks": [
  "The left column names what to record. The open space beside it is for the board: write, sketch, label. Use as much of it as the slide needs.",
  "Worked examples print the problem. Copy the setup and every step from the board, and carry units the whole way.",
  "Your Turn: work it in the box first, then check against the board before the next slide.",
  "Every vector answer carries a direction. Every number carries a unit.",
  "Projectile problems: +y is up, so down is negative. Neglect air resistance."],
 "sectionList": [
  "S2.1   Vectors & Vector Basics (Review)",
  "S2.2   Vector Addition",
  "S2.3   Projectile Motion (All Types)"],
 "sectionsContent": [
  {"code": "U2 / S2.1", "title": "Vectors & Vector Basics (Review)",
   "learningTarget": "I can describe a vector by its magnitude and direction, name a direction two ways, and resolve a vector into x- and y-components.",
   "rows": s21,
   "summaryPrompt": "In your own words: why is a number alone not enough to describe a vector, and what do you need to resolve one into components?",
   "selfCheck": ["I can draw a vector and label its tail, tip and angle.", "I can convert North of East to East of North.", "I can resolve a vector into x- and y-components."]},
  {"code": "U2 / S2.2", "title": "Vector Addition",
   "learningTarget": "I can add two vectors, at 90° or at any angle, and state the resultant’s magnitude and direction.",
   "rows": s22,
   "summaryPrompt": "In your own words: when can you use the right-triangle shortcut, and what do you do when you cannot?",
   "selfCheck": ["I can add two perpendicular vectors.", "I can add vectors at any angle using components.", "I can state a resultant with magnitude and direction."]},
  {"code": "U2 / S2.3", "title": "Projectile Motion (All Types)",
   "learningTarget": "I can split a projectile’s motion into two axes, solve the vertical motion for time, and use that time horizontally.",
   "rows": s23,
   "summaryPrompt": "In your own words: explain how one projectile moves with constant velocity in one direction and accelerates in the other, and what the two motions share.",
   "selfCheck": ["I can find the time from the vertical motion and use it horizontally.", "I can solve a flat, an angled and a different-height launch.", "I can find the peak height and the total flight time from a cliff."]}],
 "close": {"banner": "UNIT 2 · PULLING IT TOGETHER",
  "checklist": ["Notes complete for S2.1–S2.3", "Worked examples recorded with units", "Your Turn problems checked against the board", "Summary boxes written"],
  "bigPicture": "Trace one projectile all the way through: resolve the launch velocity, solve the vertical motion for time, then use that same time horizontally.",
  "fuzzyLabel": "STILL FUZZY ON — bring these to review day"},
 "noEquationBar": True
}

KEYS = {
 "VECTOR · MAGNITUDE · DIRECTION": ["Vector: magnitude AND direction; drawn as an arrow.", "Magnitude: the size or length; never negative, zero is possible.", "Direction: which way it points, given relative to a reference direction.", "A number alone does not specify a nonzero vector."],
 "DRAWING A VECTOR": ["Choose a scale first. Tail = start, tip = end.", "Arrow length = magnitude. Angle measured from a reference axis at the tail.", "Tip points the way the vector acts.", "Sketch: arrow with tail, tip and angle theta from the axis labeled."],
 "RESOLVING A VECTOR INTO COMPONENTS": ["Ax = A cos theta   (adjacent to theta)        Ay = A sin theta   (opposite theta)", "theta measured from +x. Components let you add vectors.", "Sketch: right triangle with A as the hypotenuse, Ax along x, Ay along y."],
 "EXAMPLE — RESOLVING A DISPLACEMENT": ["Given: A = 50 m, theta = 30°.   Find: Ax and Ay.", "Ax = 50 cos 30° = 43.3 m        Ay = 50 sin 30° = 25.0 m", "Check: Ax² + Ay² = A², allowing for rounding."],
 "DEGREES AND COMPASS DIRECTIONS": ["From an axis: measure from the horizontal or vertical reference.", "Compass bearing: “40° North of East” starts at east, then turns toward north.", "One vector, two names: 40° N of E = 50° E of N, because 40° + 50° = 90°."],
 "EXAMPLE — CONVERTING THE ANGLE": ["East of North = 90° − North of East", "90° − 40° = 50°", "Answer: 50° East of North (same direction as 40° North of East)."],
 "YOUR TURN — A HIKING BEARING": ["North of East = 90° − East of North", "90° − 65° = 25°", "Answer: 25° North of East."],
 "QUICK CHECK — CONVERT AND RESOLVE": ["theta = 90° − 70° = 20° North of East", "Fx = 20 cos 20° = 18.8 N        Fy = 20 sin 20° = 6.84 N"],
 "ADDING PERPENDICULAR VECTORS": ["Tip-to-tail; the resultant joins the original tail to the final tip.", "Magnitude: R = √(A² + B²)        Direction: theta = arctan(B/A), from the A direction.", "Only for perpendicular vectors."],
 "EXAMPLE — PLANE IN A CROSSWIND": ["R = √(80² + 20²) = 82.5 km/h", "theta = arctan(20/80) = 14°", "Answer: 82.5 km/h at 14° N of E.  Always report magnitude AND direction."],
 "ADDING VECTORS AT ANY ANGLE": ["1 • Resolve: Ax = A cos theta, Ay = A sin theta", "2 • Add: Rx = sum of the x-components, Ry = sum of the y-components", "3 • Recombine: R = √(Rx² + Ry²), theta = arctan(Ry/Rx)", "Use the signs of the components to choose the correct quadrant."],
 "EXAMPLE — TWO FORCES ON A BOX": ["F₁ = (40, 0) N        F₂ = (30 cos 60°, 30 sin 60°) = (15, 25.98) N", "Rx = 40 + 15 = 55 N        Ry = 0 + 25.98 = 25.98 N", "R = 60.8 N at 25.3° N of E"],
 "YOUR TURN — TWO DISPLACEMENTS": ["Rx = 30 + 40 cos 45° = 58.28 m        Ry = 40 sin 45° = 28.28 m", "R = √(58.28² + 28.28²) = 64.8 m        theta = arctan(28.28/58.28) = 25.9°", "Answer: R ≈ 64.8 m at 25.9° N of E."],
 "PRACTICE — THREE FORCES ON A CRATE": ["F₁ = (30, 0) N        F₂ = (0, 40) N", "F₃ = (−20 cos 30°, −20 sin 30°) = (−17.32, −10.0) N", "Rx = 30 − 17.32 = 12.68 N        Ry = 40 − 10.0 = 30.0 N", "R = √(12.68² + 30.0²) = 32.6 N        theta = arctan(30.0/12.68) = 67.1°", "Answer: R ≈ 32.6 N at 67.1° N of E.   (Added problem: not on the slides.)"],
 "PROJECTILE · TRAJECTORY · RANGE": ["Projectile: an object moving under gravity alone after release.", "Trajectory: the path it follows; a parabola when horizontal velocity is nonzero.", "Range: horizontal distance from launch to landing.", "Model: no air resistance, constant g = 9.8 m/s². Horizontal and vertical motion are independent and share the same time."],
 "NO HORIZONTAL FORCE NEEDED": ["Gravity acts downward. With no air resistance, vx stays constant.", "Inertia: no horizontal net force means no horizontal acceleration.", "Common error: a force is needed to keep it moving sideways. It is not."],
 "THE FLAT LAUNCH": ["Horizontal: vx = vix = constant;  x = vix t", "Vertical drop: viy = 0;  h = ½gt²   (h = positive drop distance)", "Time to land: t = √(2h/g).   Equal time steps → equal horizontal spacing."],
 "EXAMPLE — ROLLING OFF A TABLE": ["Given: h = 0.80 m;  vix = 2.5 m/s, viy = 0.", "Vertical first: 0.80 = ½(9.8)t²  →  t = √(1.60/9.8) = 0.404 s", "Horizontal: x = vix t = 2.5(0.404) = 1.01 m", "Answer: t ≈ 0.40 s,  x ≈ 1.0 m"],
 "YOUR TURN — OFF A HIGHER SHELF": ["t = √(2h/g) = √(2(1.25)/9.8) = 0.505 s", "x = vix t = 3.0(0.505) = 1.52 m", "Answer: x ≈ 1.5 m from the shelf."],
 "LAUNCHING AT AN ANGLE": ["Components: vix = vi cos theta;  viy = vi sin theta", "Time of flight: t = 2viy/g   (same launch and landing height only)", "Range: R = vix t", "At the peak: vy = 0, vx unchanged."],
 "EXAMPLE — A KICKED SOCCER BALL": ["vix = 18 cos 30° = 15.59 m/s        viy = 18 sin 30° = 9.00 m/s", "t = 2(9.00)/9.8 = 1.84 s", "R = vix t = 15.59(1.84) ≈ 28.6 m"],
 "YOUR TURN — A LAUNCHED ARROW": ["vix = 45 cos 40° = 34.47 m/s        viy = 45 sin 40° = 28.93 m/s", "t = 2viy/g = 2(28.93)/9.8 ≈ 5.90 s", "R = vix t = 34.47(5.90) ≈ 203 m"],
 "WHEN LAUNCH AND LANDING DIFFER": ["Not symmetric about the peak; the level-ground shortcut fails.", "Choose +y upward. Landing lower means more time descending than ascending.", "At the peak: vy = 0;  t_apex = viy/g.        Height gained: Δy = viy²/(2g).", "Total flight time: solve 0 = y₀ + viy t − ½gt² when the landing surface is y = 0."],
 "EXAMPLE — MAX HEIGHT FROM A CLIFF": ["viy = 20 sin 35° = 11.47 m/s;  vy = 0 at the top.", "Δy = viy²/(2g) = 11.47²/(2·9.8) = 6.71 m above the launch point", "(Above the ground: 15 + 6.71 = 21.7 m.)"],
 "EXAMPLE — LANDING BELOW THE LAUNCH": ["y(t) = y₀ + viy t − ½gt²   →   0 = 15 + 11.47t − 4.9t²", "t = [11.47 ± √(11.47² + 4(4.9)(15))] / 9.8", "Keep the positive root: t ≈ 3.28 s ≈ 3.3 s. The negative root is before release."],
 "THREE STAGES, ONE IDEA": ["1 • Horizontal launch: viy = 0; find time from the drop.", "2 • Angled, level ground: resolve vi first; t = 2viy/g.", "3 • Different heights: find the peak or solve the full vertical-position equation.", "Every projectile problem: resolve, solve vertically, then use the same time horizontally."],
}
SUMKEYS = {
 "U2 / S2.1": "Sample: a number alone gives only a size, so a vector also needs a direction. To resolve one you need its magnitude and its angle from a reference axis, then Ax = A cos theta and Ay = A sin theta.",
 "U2 / S2.2": "Sample: use R = √(A² + B²) when the vectors are perpendicular. Otherwise resolve each vector, add the x-components and the y-components, then recombine.",
 "U2 / S2.3": "Sample: horizontally the velocity is constant (no horizontal force); vertically it accelerates at g. The two motions share the same time, found from the vertical motion.",
}
for sec in spec["sectionsContent"]:
    sec["summaryAnswer"] = SUMKEYS[sec["code"]]
    for r in sec["rows"]:
        r["problem"]["solution"] = KEYS[r.pop("_label")]

import copy, os
HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "phys_u02_s02.1-s02.3_notes"
student = copy.deepcopy(spec)
for sec in student["sectionsContent"]:
    sec.pop("summaryAnswer", None)
    for r in sec["rows"]:
        r["problem"].pop("solution", None)
key = copy.deepcopy(spec)
key["key"] = True
for name, data in (("student", student), ("key", key)):
    with open(os.path.join(HERE, f"{STEM}_{name}.json"), "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
print("wrote", STEM + "_student.json and _key.json")
