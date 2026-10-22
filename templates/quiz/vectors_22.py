"""Physics S2.2 Vectors quiz: versions A, B, C, every answer solved in code.

One source for the student quiz, the key and the grader sheet, so they cannot drift. Nothing
here is typed from memory: each answer below is computed from the givens. Edit the givens, not
the answers. Blueprint (identical across versions, 16 points): three direction restatements
(2 pts each), one perpendicular-vector addition (5 pts), one two-vector addition at angles
(5 pts). Answers are reported to two significant figures.

Greek letters are not written anywhere: Archivo has no theta, so the text says "angle".
"""
import math

CODE = "U02 / S02.2"
TITLE_LINES = ("UNIT 2 · MOTION IN TWO DIMENSIONS", "VECTOR ADDITION QUIZ")
TOTAL = 16

# ---- angle forms ---------------------------------------------------------------------

def theta_from(a, first, second):
    """Degrees on the 0-360 scale for 'a degrees FIRST of SECOND', e.g. (40,'north','west')."""
    if second in ("east", "west"):                 # measured from the horizontal axis
        base = 0 if second == "east" else 180
        up = (first == "north")
        return (base + a if (second == "east") == up else base - a) % 360
    base = 90 if second == "north" else 270        # measured from the vertical axis
    return (base - a if first == "east" else base + a) % 360

def compass(theta):
    """(a, 'north', 'west') style, measured from the nearer horizontal axis."""
    t = theta % 360
    if t < 90:   return (t, "north", "east")
    if t < 180:  return (180 - t, "north", "west")
    if t < 270:  return (t - 180, "south", "west")
    return (360 - t, "south", "east")

def other_axis(theta):
    """The same direction measured from the nearer vertical axis."""
    a, ns, ew = compass(theta)
    return (90 - a, ew, ns)

def fmt(a, first, second, short=False):
    n = f"{a:.0f}" if abs(a - round(a)) < 1e-9 else f"{a:.1f}"
    if short:
        return f"{n}° {first[0].upper()} of {second[0].upper()}"
    return f"{n}° {first} of {second}"

def equivalents(theta, skip=None):
    """Every correct way to write a direction: 0-360, negative, and both compass forms."""
    t = theta % 360
    out = {"deg": f"{t:.0f}°", "neg": f"−{360 - t:.0f}°" if t else "0°",
           "c1": fmt(*compass(t)), "c2": fmt(*other_axis(t))}
    out["c1s"], out["c2s"] = fmt(*compass(t), short=True), fmt(*other_axis(t), short=True)
    return out

# ---- vector arithmetic -----------------------------------------------------------------

def comps(mag, theta):
    r = math.radians(theta)
    return mag * math.cos(r), mag * math.sin(r)

def addition(vs):
    rx = sum(comps(m, t)[0] for m, t in vs)
    ry = sum(comps(m, t)[1] for m, t in vs)
    return rx, ry, math.hypot(rx, ry), math.degrees(math.atan2(ry, rx)) % 360

def two_sf(x):
    return f"{x:.2g}"

# ---- the three versions ----------------------------------------------------------------
# restate: Q1 gives 0-360; Q2 gives a compass direction; Q3 gives a negative angle.
# q4: perpendicular legs (x, y) with units and who/what; q5: two vectors as compass specs.
VERSIONS = {
  "A": {
    "q1": 140, "q2": (65, "south", "east"), "q3": -130,
    "q4": {"x": 4.0, "y": -1.6, "unit": "m/s", "kind": "velocity",
           "text": "Moana paddles her canoe east at 4.0 m/s while a current pushes it south at 1.6 m/s. "
                   "Find the canoe’s resultant velocity: magnitude and direction."},
    "q5": {"unit": "m", "kind": "displacement", "v": [(45, (40, "south", "west")), (60, (70, "north", "east"))],
           "text": "Kirby floats 45 m at 40° south of west, then a gust blows him 60 m at 70° north of east. "
                   "Find Kirby’s resultant displacement: magnitude and direction."},
  },
  "B": {
    "q1": 255, "q2": (35, "north", "west"), "q3": -160,
    "q4": {"x": -28.0, "y": 36.0, "unit": "m", "kind": "displacement",
           "text": "Spider-Man swings 28 m west and then 36 m north across the city. "
                   "Find his resultant displacement: magnitude and direction."},
    "q5": {"unit": "km/h", "kind": "velocity", "v": [(80, (25, "north", "east")), (60, (60, "south", "west"))],
           "text": "Aang’s glider flies at 80 km/h at 25° north of east while an air current blows toward "
                   "60° south of west at 60 km/h. Find the glider’s resultant velocity: magnitude and direction."},
  },
  "C": {
    "q1": 330, "q2": (55, "south", "west"), "q3": -250,
    "q4": {"x": 3.0, "y": 7.5, "unit": "m/s", "kind": "velocity", "frame": "v",
           "text": "Buzz Lightyear flies north at 7.5 m/s while a crosswind blows him east at 3.0 m/s. "
                   "Find his resultant velocity: magnitude and direction."},
    "q5": {"unit": "m", "kind": "displacement", "v": [(35, (20, "south", "east")), (45, (10, "west", "north"))],
           "text": "Mario walks 35 m toward 20° south of east, then turns and walks 45 m toward 10° west of "
                   "north. Find Mario’s resultant displacement: magnitude and direction."},
  },
}

def restate_items(v):
    t1 = v["q1"] % 360
    t2 = theta_from(*v["q2"])
    t3 = v["q3"] % 360
    items = []
    for n, theta, given in ((1, t1, f"{t1:.0f}°"), (2, t2, fmt(*v["q2"])), (3, t3, f"−{abs(v['q3'])}°")):
        eq = equivalents(theta)
        given_key = {1: "deg", 2: "c1", 3: "neg"}[n]       # the form the prompt itself uses
        items.append({"n": n, "given": given, "theta": theta, "eq": eq, "given_key": given_key})
    return items

def solve_q4(q):
    x, y = q["x"], q["y"]
    R = math.hypot(x, y)
    th = math.degrees(math.atan2(y, x)) % 360
    eq = equivalents(round(th))
    # The direction is stated from the axis the problem's own story is told along.
    return {"R": R, "th": th, "ref": math.degrees(math.atan(abs(y) / abs(x))),
            "stated": eq["c2"] if q.get("frame") == "v" else eq["c1"], "eq": eq}

def solve_q5(q):
    vs = [(m, theta_from(*spec)) for m, spec in q["v"]]
    rx, ry, R, th = addition(vs)
    eq = equivalents(round(th))
    return {"vs": vs, "parts": [comps(m, t) for m, t in vs], "rx": rx, "ry": ry, "R": R, "th": th,
            "eq": eq, "stated": eq["c1"]}

def build():
    data = {}
    for L, v in VERSIONS.items():
        data[L] = {"v": v, "restate": restate_items(v), "q4": solve_q4(v["q4"]), "q5": solve_q5(v["q5"])}
    return data

if __name__ == "__main__":
    for L, d in build().items():
        print("VERSION", L)
        for it in d["restate"]:
            print("  Q%d given %s -> %s" % (it["n"], it["given"], it["eq"]))
        q4, q5 = d["q4"], d["q5"]
        print("  Q4 R=%.3f (%s) th=%.2f ref=%.2f stated=%s eq=%s" % (q4["R"], two_sf(q4["R"]), q4["th"], q4["ref"], q4["stated"], q4["eq"]))
        print("  Q5 parts=%s Rx=%.2f Ry=%.2f R=%.2f (%s) th=%.2f stated=%s eq=%s" % (
            [(round(a, 2), round(b, 2)) for a, b in q5["parts"]], q5["rx"], q5["ry"], q5["R"], two_sf(q5["R"]), q5["th"], q5["stated"], q5["eq"]))
