"""Physics Unit 2 test data: every answer solved in code, nothing typed by hand.

Three things live here, all for S2.1-S2.3 (Vectors, Vector Addition, Projectile Motion):
  WRITTEN   the Day 2 written test, versions A / B / C (five problems, 30 points)
  MC        the 30-question multiple-choice test, versions A / B / C
  GUIDE     the study-guide problems (one version)

Conventions match the guided notes: g = 9.8 m/s^2, +y is up, no air resistance, angles on the
0-360 scale start at east and run counterclockwise.
"""
import math, os, random, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "quiz"))
import vectors_22 as V                                            # noqa: E402

G = 9.8
VERS = "ABC"


def sf(x, n=2):
    """Round to n significant figures and print without scientific notation."""
    if x == 0:
        return "0"
    d = n - int(math.floor(math.log10(abs(x)))) - 1
    r = round(x, d)
    return f"{r:.{max(d, 0)}f}"


# ---------------------------------------------------------------------------------------
# Projectile solvers (the independent check re-derives these a different way in verify_u2.py)
# ---------------------------------------------------------------------------------------

def horizontal_launch(h, vx):
    t = math.sqrt(2 * h / G)
    return {"t": t, "x": vx * t, "vy": -G * t}


def level_angled(v, ang):
    vx, vy = v * math.cos(math.radians(ang)), v * math.sin(math.radians(ang))
    t = 2 * vy / G
    return {"vx": vx, "vy": vy, "t": t, "R": vx * t, "H": vy * vy / (2 * G)}


def from_height(y0, v, ang):
    vx, vy = v * math.cos(math.radians(ang)), v * math.sin(math.radians(ang))
    # 0 = y0 + vy t - 4.9 t^2  ->  4.9 t^2 - vy t - y0 = 0, keep the positive root
    a, b, c = 0.5 * G, -vy, -y0
    disc = b * b - 4 * a * c
    t = (-b + math.sqrt(disc)) / (2 * a)
    return {"vx": vx, "vy": vy, "a": a, "b": b, "c": c, "disc": disc, "t": t, "x": vx * t,
            "vyf": vy - G * t}


# ---------------------------------------------------------------------------------------
# Written test: five problems per version
# ---------------------------------------------------------------------------------------

WRITTEN = {
    "A": {
        "q1": {"x": 1.8, "y": 3.5, "unit": "m/s",
               "text": "Maya paddles her kayak north across a river at 3.5 m/s while the current carries it east at "
                       "1.8 m/s. Find the kayak’s resultant velocity: magnitude and direction."},
        "q2": {"unit": "km/h", "v": [(240, (35, "north", "east")), (50, (20, "north", "west"))],
               "text": "A plane flies at 240 km/h toward 35° north of east. A wind blows toward 20° north of west at "
                       "50 km/h. Find the plane’s resultant velocity relative to the ground: magnitude and direction."},
        "q3": {"h": 5.0, "vx": 12.0,
               "text": "A stunt cyclist leaves the end of a horizontal ramp 5.0 m above the ground at 12 m/s. "
                       "Find (a) the time in the air and (b) the horizontal distance traveled before landing."},
        "q4": {"v": 22.0, "ang": 35.0,
               "text": "A soccer player kicks a ball at 22 m/s at 35° above the horizontal on level ground. "
                       "Find (a) the time in the air and (b) the horizontal range."},
        "q5": {"y0": 15.0, "v": 25.0, "ang": 20.0,
               "text": "Hawkeye stands on a castle wall 15 m above the ground and shoots an arrow at 25 m/s at 20° above "
                       "the horizontal. The enemy is on the ground below. Find (a) the arrow’s horizontal and vertical "
                       "launch velocities, (b) the time until it lands, and (c) how far from the wall it lands."},
    },
    "B": {
        "q1": {"x": -90.0, "y": -120.0, "unit": "m",
               "text": "A hiker walks 90 m west and then 120 m south. Find the hiker’s resultant displacement: "
                       "magnitude and direction."},
        "q2": {"unit": "km/h", "v": [(180, (40, "south", "west")), (45, (70, "north", "east"))],
               "text": "A plane flies at 180 km/h toward 40° south of west. A wind blows toward 70° north of east at "
                       "45 km/h. Find the plane’s resultant velocity relative to the ground: magnitude and direction."},
        "q3": {"h": 20.0, "vx": 7.0,
               "text": "A pebble is kicked horizontally off a 20 m cliff at 7.0 m/s. "
                       "Find (a) the time in the air and (b) the horizontal distance from the base of the cliff to where it lands."},
        "q4": {"v": 18.0, "ang": 50.0,
               "text": "A football is thrown at 18 m/s at 50° above the horizontal and caught at the same height. "
                       "Find (a) the time in the air and (b) the horizontal distance it travels."},
        "q5": {"y0": 12.0, "v": 22.0, "ang": 30.0,
               "text": "Katniss stands on a platform 12 m above the ground and fires an arrow at 22 m/s at 30° above "
                       "the horizontal at a target on the ground. Find (a) the arrow’s horizontal and vertical "
                       "launch velocities, (b) the time until it lands, and (c) how far from the platform it lands."},
    },
    "C": {
        "q1": {"x": 12.0, "y": -5.0, "unit": "m/s",
               "text": "A drone flies east at 12 m/s while a wind blows it south at 5.0 m/s. Find the drone’s "
                       "resultant velocity: magnitude and direction."},
        "q2": {"unit": "km/h", "v": [(200, (25, "east", "north")), (40, (30, "south", "east"))],
               "text": "A plane flies at 200 km/h toward 25° east of north. A wind blows toward 30° south of east at "
                       "40 km/h. Find the plane’s resultant velocity relative to the ground: magnitude and direction."},
        "q3": {"h": 1.1, "vx": 1.5,
               "text": "A cat knocks a mug off a kitchen counter 1.1 m high. The mug leaves the counter horizontally at "
                       "1.5 m/s. Find (a) the time in the air and (b) the horizontal distance from the counter to where it lands."},
        "q4": {"v": 26.0, "ang": 28.0,
               "text": "A golf ball is hit at 26 m/s at 28° above the horizontal on a level fairway. "
                       "Find (a) the time in the air and (b) the horizontal range."},
        "q5": {"y0": 18.0, "v": 28.0, "ang": 15.0,
               "text": "Legolas stands on a tower 18 m above the ground and shoots an arrow at 28 m/s at 15° above the "
                       "horizontal at an enemy on the ground. Find (a) the arrow’s horizontal and vertical launch "
                       "velocities, (b) the time until it lands, and (c) how far from the tower it lands."},
    },
}
POINTS = (5, 5, 5, 5, 5)           # 25, each scored on the 0-5 rubric


def solve_written(L):
    w = WRITTEN[L]
    out = {}
    q1 = w["q1"]
    out["q1"] = {"R": math.hypot(q1["x"], q1["y"]),
                 "th": math.degrees(math.atan2(q1["y"], q1["x"])) % 360}
    vs = [(m, V.theta_from(*s)) for m, s in w["q2"]["v"]]
    rx, ry, R, th = V.addition(vs)
    out["q2"] = {"vs": vs, "parts": [V.comps(m, t) for m, t in vs], "rx": rx, "ry": ry, "R": R, "th": th}
    out["q3"] = horizontal_launch(w["q3"]["h"], w["q3"]["vx"])
    out["q4"] = level_angled(w["q4"]["v"], w["q4"]["ang"])
    out["q5"] = from_height(w["q5"]["y0"], w["q5"]["v"], w["q5"]["ang"])
    return out


# ---------------------------------------------------------------------------------------
# Multiple choice
# ---------------------------------------------------------------------------------------
# An item is (std, stem, correct, [(wrong, why), ...]). Conceptual items carry one variant
# per version; calculation items are generated from the version's numbers.

def _pick(cands, correct, k=3):
    """First k distinct candidates that differ from the correct text."""
    seen, out = {correct}, []
    for text, why in cands:
        if text not in seen:
            seen.add(text); out.append((text, why))
        if len(out) == k:
            break
    assert len(out) == k, (correct, cands)
    return out


def _ang(a):
    return f"{a:.0f}°".replace("-", "−")


def rnd(x):
    return f"{x:.0f}" if x >= 100 else f"{x:.2g}"


def _compass(a, first, second):
    return V.fmt(a, first, second)


def mc_items(i):
    """The thirty items for version index i (0, 1, 2) in blueprint order."""
    it = []

    # ---- S2.1 -----------------------------------------------------------------------
    c1 = [
        ("Which of these quantities is a vector?", "A car’s velocity of 25 m/s east",
         [("A car’s speed of 25 m/s", "A speed has no direction."), ("The time of the trip, 3.0 h", "Time is a scalar."),
          ("The mass of the car, 1200 kg", "Mass is a scalar.")]),
        ("Which of these quantities is a vector?", "A displacement of 40 m south",
         [("A distance of 40 m", "A distance has no direction."), ("A temperature of 40 °C", "Temperature is a scalar."),
          ("A volume of 40 L", "Volume is a scalar.")]),
        ("Which of these quantities is a vector?", "A force of 15 N downward",
         [("A speed of 15 m/s", "A speed has no direction."), ("An energy of 15 J", "Energy is a scalar."),
          ("A length of 15 cm", "A length has no direction.")]),
    ][i]
    it.append(("S2.1", c1[0], c1[1], c1[2]))

    a, f, s = [(30, "north", "west"), (40, "south", "east"), (25, "south", "west")][i]
    th = V.theta_from(a, f, s)
    cands = [(_ang(a), "Read the angle from east and ignored the other axis."),
             (_ang(180 + a), "Added the angle to 180° when it should be subtracted."),
             (_ang(360 - a), "Turned the wrong way from east."),
             (_ang(90 + a), "Measured from north instead of the stated axis."),
             (_ang(270 + a), "Measured from south instead of the stated axis.")]
    it.append(("S2.1", f"Which angle on the 0–360° scale (counterclockwise from east) matches {_compass(a, f, s)}?",
               _ang(th), _pick(cands, _ang(th))))

    n = [-40, -125, -200][i]
    c = n % 360
    cands = [(_ang(abs(n)), "Dropped the negative sign instead of turning clockwise."),
             (_ang(180 - abs(n)), "Subtracted from 180° instead of from 360°."),
             (_ang(180 + abs(n)), "Added to 180° instead of subtracting from 360°."),
             (_ang(90 + abs(n)), "Added to 90°.")]
    it.append(("S2.1", f"A vector’s direction is {str(n).replace('-', '−')}°. Written on the 0–360° scale, it is", _ang(c), _pick(cands, _ang(c))))

    t = [215, 125, 310][i]
    ca, cf, cs = V.compass(t)
    right = V.fmt(ca, cf, cs)
    flip = {"north": "south", "south": "north", "east": "west", "west": "east"}
    cands = [(V.fmt(ca, flip[cf], cs), "Right angle, wrong north/south side."),
             (V.fmt(ca, cf, flip[cs]), "Right angle, wrong east/west side."),
             (V.fmt(90 - ca, cf, cs), "Used the angle from the other axis but kept the same words.")]
    it.append(("S2.1", f"A vector points at {t}° on the 0–360° scale. As a compass direction, that is", right, _pick(cands, right)))

    t = [140, 250, 320][i]
    sx = "+" if math.cos(math.radians(t)) > 0 else "−"
    sy = "+" if math.sin(math.radians(t)) > 0 else "−"
    right = f"Rx is {sx}, Ry is {sy}"
    allc = [f"Rx is {a}, Ry is {b}" for a in "+−" for b in "+−"]
    why = "Component signs do not match the quadrant."
    it.append(("S2.1", f"A vector points at {t}° on the 0–360° scale. The signs of its components are",
               right, [(x, why) for x in allc if x != right]))

    c6 = [
        ("When you draw a vector, the length of the arrow shows its", "magnitude, drawn to a chosen scale",
         [("direction", "Direction is shown by the way the arrow points."), ("starting position", "The tail shows where it starts."),
          ("time of travel", "A vector drawing carries no time.")]),
        ("When you draw a vector, the arrowhead shows its", "direction",
         [("magnitude", "Magnitude is shown by the length."), ("units", "Units are written beside it."),
          ("mass", "Mass is not part of a vector drawing.")]),
        ("A vector has a magnitude and a direction. A vector drawing shows the magnitude with the", "length of the arrow",
         [("color of the arrow", "Color carries no value."), ("width of the arrow", "Width carries no value."),
          ("position of the arrowhead on the page", "Where it sits on the page does not change the vector.")]),
    ][i]
    it.append(("S2.1", c6[0], c6[1], c6[2]))

    c7 = [
        ("To add two vectors by drawing them, you place them tip to tail. The resultant is drawn",
         "from the tail of the first to the tip of the last",
         [("from the tip of the first to the tail of the last", "That arrow points backward."),
          ("from the tail of the first to the tail of the last", "Two tails do not make a closed path."),
          ("along the longer vector only", "The resultant depends on both vectors.")]),
        ("Three vectors are added tip to tail. The resultant is drawn",
         "from the tail of the first vector to the tip of the last vector",
         [("from the tip of the first to the tip of the last", "It must start at the first tail."),
          ("from the tail of the last to the tip of the first", "That arrow points backward."),
          ("parallel to the middle vector", "The middle vector does not set the resultant.")]),
        ("A student draws vectors A and B tip to tail. The resultant R is the arrow that",
         "starts at the tail of A and ends at the tip of B",
         [("starts at the tip of A and ends at the tail of B", "That arrow points backward."),
          ("is the same length as A", "R depends on both A and B."),
          ("is drawn from the tip of B back to the tip of A", "That is the difference, not the sum.")]),
    ][i]
    it.append(("S2.1", c7[0], c7[1], c7[2]))

    # ---- S2.2 -----------------------------------------------------------------------
    legs = [(6.0, 8.0, "km", "east", "north", "hiker"), (5.0, 12.0, "m", "south", "west", "bug"),
            (8.0, 15.0, "m/s", "east", "south", "boat")][i]
    p, q, u, d1, d2, who = legs
    R = math.hypot(p, q)
    verbs = {"km": "walks {p} km {d1} and then {q} km {d2}", "m": "crawls {p} m {d1} and then {q} m {d2}",
             "m/s": "heads {d1} at {p} m/s while the current carries it {d2} at {q} m/s"}
    mv = verbs[u].format(p=f"{p:.1f}", q=f"{q:.1f}", d1=d1, d2=d2)
    cands = [(f"{p + q:.0f} {u}", "Added the magnitudes; perpendicular vectors need Pythagoras."),
             (f"{R * R:.0f} {u}", "Forgot the square root."),
             (f"{max(p, q):.0f} {u}", "Took the larger leg."), (f"{abs(q - p):.0f} {u}", "Subtracted the magnitudes.")]
    right = f"{R:.0f} {u}"
    sub = {"hiker": "A hiker", "bug": "A beetle", "boat": "A boat"}[who]
    if u == "m/s":
        stem = f"A boat {mv}. What is the magnitude of the boat’s resultant velocity?"
    else:
        stem = f"{sub} {mv}. What is the magnitude of the resultant displacement?"
    it.append(("S2.2", stem, right, _pick(cands, right)))

    # direction of the same sum, from the horizontal axis (the compass form the unit uses)
    sx, sy, lx, ly = [(1, 1, 6.0, 8.0), (-1, -1, 12.0, 5.0), (1, -1, 8.0, 15.0)][i]   # signs; |x| and |y| legs
    ang = round(math.degrees(math.atan(ly / lx)))
    ns, ew = ("north" if sy > 0 else "south"), ("east" if sx > 0 else "west")
    right = V.fmt(ang, ns, ew)
    flip = {"north": "south", "south": "north", "east": "west", "west": "east"}
    cands = [(V.fmt(90 - ang, ns, ew), "Flipped the ratio: used adjacent over opposite."),
             (V.fmt(ang, flip[ns], ew), "Wrong north/south side."),
             (V.fmt(ang, ns, flip[ew]), "Wrong east/west side.")]
    stem2 = stem.replace("What is the magnitude of the resultant displacement?", "What is the direction of the resultant displacement?") \
                .replace("What is the magnitude of the boat’s resultant velocity?", "What is the direction of the boat’s resultant velocity?")
    it.append(("S2.2", stem2, right, _pick(cands, right)))

    a3 = [(7, 3, "m/s", "boat heads east at 7 m/s against a 3 m/s current flowing west", "east", "west"),
          (200, 50, "km/h", "plane flies north at 200 km/h into a 50 km/h headwind from the north", "north", "south"),
          (6.0, 4.5, "m/s", "swimmer swims west at 6.0 m/s against a 4.5 m/s current flowing east", "west", "east")][i]
    big, small, un, desc, d_big, d_small = a3
    net = big - small
    fl = lambda x: f"{x:g}" if big == int(big) else f"{x:.1f}"
    right = f"{fl(net)} {un} {d_big}"
    cands = [(f"{fl(big + small)} {un} {d_big}", "Added vectors that point opposite ways."),
             (f"{fl(net)} {un} {d_small}", "Right size, wrong direction."),
             (f"{rnd(math.hypot(big, small))} {un} {d_big}", "Used Pythagoras on vectors that are not perpendicular.")]
    it.append(("S2.2", f"A {desc}. The resultant velocity is", right, _pick(cands, right)))

    a4 = [(7, 5, [1, 8, 13, 15]), (9, 4, [3, 10, 14, 20]), (6, 10, [2, 12, 17, 18])][i]
    m1, m2, opts = a4
    ok = [x for x in opts if abs(m1 - m2) <= x <= m1 + m2][0]
    it.append(("S2.2", f"Two forces of {m1} N and {m2} N act on one object. Which resultant could the two forces produce?",
               f"{ok} N", [(f"{x} N", f"A resultant must lie between {abs(m1 - m2)} N and {m1 + m2} N.") for x in opts if x != ok]))

    a5 = [(50, 30), (80, 25), (12, 60)][i]
    mag, ang = a5
    r = math.radians(ang)
    right = f"{mag * math.cos(r):.0f}"
    unit = "m/s" if i != 1 else "km/h"
    cands = [(f"{mag * math.sin(r):.0f}", "Used sine for the horizontal component."),
             (f"{mag / math.cos(r):.0f}", "Divided by cosine."), (f"{mag * math.tan(r):.0f}", "Used tangent.")]
    if i == 2:
        right = f"{mag * math.cos(r):.1f}"
        cands = [(f"{mag * math.sin(r):.1f}", "Used sine for the horizontal component."),
                 (f"{mag / math.cos(r):.1f}", "Divided by cosine."), (f"{mag * math.tan(r):.1f}", "Used tangent.")]
    cands = [(f"{c} {unit}", w) for c, w in cands]
    it.append(("S2.2", f"A vector of {mag} {unit} points {ang}° above the +x axis. Its x component is", f"{right} {unit}", _pick(cands, f"{right} {unit}")))

    a6 = [
        ("A student has Rx and Ry. Which equation gives the angle between the resultant and the x axis?",
         "tan(angle) = Ry / Rx",
         [("tan(angle) = Rx / Ry", "Flipped the ratio."), ("sin(angle) = Ry × Rx", "Not an equation for the angle."),
          ("cos(angle) = Ry / Rx", "Mixed cosine with the ratio of components.")]),
        ("After adding the x parts and the y parts, you can find the reference angle with",
         "tan(angle) = Ry / Rx",
         [("tan(angle) = Rx / Ry", "Flipped the ratio."), ("angle = Ry + Rx", "An angle is not a sum of lengths."),
          ("sin(angle) = Rx / Ry", "Wrong ratio for sine.")]),
        ("To get the size of a resultant from its components, use", "R² = Rx² + Ry²",
         [("R = Rx + Ry", "Components are perpendicular; add them with Pythagoras."), ("R = Rx × Ry", "A product is not a length."),
          ("R = Rx / Ry", "A ratio is not a length.")]),
    ][i]
    it.append(("S2.2", a6[0], a6[1], a6[2]))

    ax, bx = [(12, -5), (-8, -3), (6.5, -9.5)][i]
    s = ax + bx
    fn = lambda x: f"{x:g}".replace("-", "−")
    cands = [(f"{fn(-s)} m", "Flipped the sign."), (f"{fn(ax - bx)} m", "Subtracted instead of added."),
             (f"{sf(math.hypot(ax, bx))} m", "Used Pythagoras on components that lie along the same axis."),
             (f"{fn(abs(ax) + abs(bx))} m", "Dropped the signs.")]
    it.append(("S2.2", f"Vector A has Ax = {fn(ax)} m and vector B has Bx = {fn(bx)} m. The x component of the resultant, Rx, is",
               f"{fn(s)} m", _pick(cands, f"{fn(s)} m")))

    a8 = [
        ("A plane’s velocity points 30° north of east and the wind points 20° north of west. Before adding them you should",
         "resolve each into x and y components",
         [("add the two magnitudes", "Directions matter; magnitudes alone do not add."), ("average the two angles", "Angles are not averaged."),
          ("multiply the magnitudes", "Vector addition does not multiply.")]),
        ("A boat’s velocity points 40° south of east and the current points 15° north of east. To add them you should",
         "resolve each into x and y components",
         [("add the two magnitudes", "Directions matter; magnitudes alone do not add."), ("subtract the two angles", "Angles are not subtracted to give a resultant."),
          ("use Pythagoras on the two magnitudes", "They are not perpendicular.")]),
        ("A hiker walks 20 m at 30° north of west and then 35 m at 50° south of west. Before adding the walks you should",
         "resolve each into x and y components",
         [("add 20 m and 35 m", "Directions matter."), ("add 30° and 50°", "Angles are not added to give a resultant."),
          ("use Pythagoras on 20 m and 35 m", "They are not perpendicular.")]),
    ][i]
    it.append(("S2.2", a8[0], a8[1], a8[2]))

    a9 = [
        ("Vectors A and B are added. If you add B + A instead of A + B, the resultant",
         "is the same",
         [("points the opposite way", "Addition order does not reverse the result."), ("is longer", "Order does not change the size."),
          ("is the same only if A and B are perpendicular", "Order never matters.")]),
        ("A student adds A + B and gets a resultant R. Her partner adds B + A. Their resultants",
         "match exactly",
         [("point in opposite directions", "Order does not reverse the result."), ("match only if the vectors are equal", "Order never matters."),
          ("match in size but not in direction", "Both size and direction match.")]),
        ("Does the order matter when you add vectors tip to tail?", "No, A + B gives the same resultant as B + A",
         [("Yes, the longer vector must go first", "Order never matters."), ("Yes, the first vector sets the direction", "Order never matters."),
          ("Only when the vectors are at 90°", "Order never matters.")]),
    ][i]
    it.append(("S2.2", a9[0], a9[1], a9[2]))

    rx, ry = [(-12, 5), (9, -4), (-3, -8)][i]
    ns = "north" if ry > 0 else "south"
    ew = "east" if rx > 0 else "west"
    right = f"{ns} of {ew}"
    allv = [f"{a} of {b}" for a in ("north", "south") for b in ("east", "west")]
    sg = lambda x: f"{x:+d}".replace("-", "−")
    it.append(("S2.2", f"A resultant has Rx = {sg(rx)} m and Ry = {sg(ry)} m (east and north are positive). Its direction is",
               right, [(x, "The signs of Rx and Ry give the quadrant.") for x in allv if x != right]))

    # ---- S2.3 -----------------------------------------------------------------------
    p1 = [
        ("At the highest point of a kicked ball’s path, the ball’s vertical velocity is",
         "zero, and its acceleration is still 9.8 m/s² downward",
         [("zero, and its acceleration is zero", "Gravity never stops acting."), ("9.8 m/s upward, and its acceleration is zero", "Nothing holds the ball up at the top."),
          ("at its maximum, and its acceleration is zero", "Vertical velocity is zero at the top.")]),
        ("At the top of an arrow’s flight, the arrow’s vertical velocity is",
         "zero, and its acceleration is still 9.8 m/s² downward",
         [("zero, and its acceleration is zero", "Gravity never stops acting."), ("equal to its launch speed", "That is not true at the top."),
          ("9.8 m/s downward, and its acceleration is zero", "The acceleration is 9.8 m/s² downward all flight.")]),
        ("A stone is thrown at an angle. At the top of its path, its vertical velocity is",
         "zero, and its acceleration is 9.8 m/s² downward",
         [("zero, and its acceleration is zero", "Gravity never stops acting."), ("9.8 m/s², and its acceleration is zero", "Velocity and acceleration are different quantities."),
          ("the same as at launch", "The vertical velocity changes the whole flight.")]),
    ][i]
    it.append(("S2.3", p1[0], p1[1], p1[2]))

    p2 = [
        ("Ignoring air resistance, a projectile’s horizontal velocity during the flight", "stays constant",
         [("steadily decreases", "Nothing pushes horizontally, so it does not decrease."), ("increases by 9.8 m/s each second", "9.8 m/s² is the vertical acceleration."),
          ("is zero at the highest point", "That is the vertical velocity.")]),
        ("A ball is thrown at an angle. Ignoring air resistance, its horizontal velocity", "does not change",
         [("drops to zero at the top", "Horizontal velocity is unchanged at the top."), ("decreases as it rises and increases as it falls", "That is the vertical motion."),
          ("increases as it falls", "Gravity acts vertically only.")]),
        ("Which statement about the horizontal motion of a projectile is correct (no air resistance)?", "It has zero acceleration",
         [("It accelerates at 9.8 m/s²", "That is the vertical acceleration."), ("It slows down as the projectile rises", "Horizontal motion is unaffected by rising."),
          ("It stops at the highest point", "Only the vertical velocity is zero at the top.")]),
    ][i]
    it.append(("S2.3", p2[0], p2[1], p2[2]))

    p3 = [
        ("One ball is dropped and a second is thrown horizontally from the same height at the same instant. Which lands first?",
         "They land at the same time",
         [("The dropped ball", "Horizontal speed does not change the fall."), ("The thrown ball", "Horizontal speed does not change the fall."),
          ("It depends on how fast the second ball is thrown", "Both fall the same way vertically.")]),
        ("A bullet is fired horizontally at the instant a second bullet is dropped from the same height. Ignoring air, which hits the ground first?",
         "They hit at the same time",
         [("The dropped bullet", "Horizontal speed does not change the fall."), ("The fired bullet, because it is faster", "Speed sideways does not change the fall."),
          ("The fired bullet, because it travels farther", "Distance does not change the fall time.")]),
        ("A marble rolls off a table at the instant a second marble is dropped from the table’s edge. Compared with the dropped marble, the rolling marble",
         "lands at the same time but farther from the table",
         [("lands sooner", "Falling time depends only on height."), ("lands later", "Falling time depends only on height."),
          ("lands at the same time and at the same spot", "It keeps moving sideways while it falls.")]),
    ][i]
    it.append(("S2.3", p3[0], p3[1], p3[2]))

    p4 = [
        ("For an object launched horizontally, the time in the air depends only on", "the height it falls through",
         [("its horizontal speed", "Horizontal speed changes the distance, not the time."), ("its mass", "Mass does not change the fall time."),
          ("its horizontal speed and its mass", "Neither changes the time.")]),
        ("Two balls leave the same cliff horizontally at different speeds. The one with the greater speed", "lands farther out in the same time",
         [("lands sooner", "Falling time depends only on height."), ("lands later", "Falling time depends only on height."),
          ("lands at the same spot", "It keeps moving sideways while it falls.")]),
        ("A pebble is thrown horizontally from a 20 m cliff. If the pebble is thrown twice as fast, the time to reach the ground", "stays the same",
         [("doubles", "Falling time does not depend on horizontal speed."), ("is cut in half", "Falling time does not depend on horizontal speed."),
          ("is cut to one fourth", "Falling time does not depend on horizontal speed.")]),
    ][i]
    it.append(("S2.3", p4[0], p4[1], p4[2]))

    h = [20, 45, 80][i]
    t = math.sqrt(2 * h / G)
    right = f"{t:.1f} s"
    cands = [(f"{math.sqrt(h / G):.1f} s", "Left out the 2 in t = √(2h/g)."), (f"{2 * h / G:.1f} s", "Forgot the square root."),
             (f"{math.sqrt(h / (2 * G)):.1f} s", "Put the 2 in the wrong place.")]
    it.append(("S2.3", f"A ball rolls off a ledge {h} m above the ground. How long does it take to reach the ground?", right, _pick(cands, right)))

    vx, tt = [(4.0, 0.60), (6.0, 0.80), (2.5, 1.2)][i]
    right = f"{vx * tt:.1f} m"
    cands = [(f"{vx / tt:.1f} m", "Divided instead of multiplying."), (f"{vx + tt:.1f} m", "Added speed and time."),
             (f"{vx * tt * tt:.1f} m", "Squared the time.")]
    it.append(("S2.3", f"A ball rolls horizontally off a table at {vx} m/s and takes {sf(tt)} s to reach the floor. How far from the table does it land?",
               right, _pick(cands, right)))

    v, ang = [(20, 30), (30, 40), (15, 60)][i]
    r = math.radians(ang)
    right = f"{v * math.sin(r):.0f} m/s"
    cands = [(f"{v * math.cos(r):.0f} m/s", "Used cosine, which gives the horizontal part."), (f"{v * math.tan(r):.0f} m/s", "Used tangent."),
             (f"{v / math.sin(r):.0f} m/s", "Divided by sine.")]
    it.append(("S2.3", f"A ball is launched at {v} m/s at {ang}° above the horizontal. Its initial vertical velocity is", right, _pick(cands, right)))

    vy0 = [14.7, 24.5, 9.8][i]
    t = 2 * vy0 / G
    right = f"{t:.1f} s"
    cands = [(f"{vy0 / G:.1f} s", "Found only the time to the top."), (f"{math.sqrt(2 * vy0 / G):.1f} s", "Used the fall formula."),
             (f"{vy0 * vy0 / (2 * G):.1f} s", "That is the height, not the time.")]
    it.append(("S2.3", f"A ball leaves level ground with an initial vertical velocity of {vy0} m/s and lands at the same height. How long is it in the air?",
               right, _pick(cands, right)))

    a0 = [30, 20, 25][i]
    right = f"{90 - a0}°"
    cands = [("45°", "That angle gives the greatest range, not the same one."), (f"{a0 // 2 if a0 // 2 != 90 - a0 else 7}°", "Half the angle does not match."),
             (f"{105 - a0}°", "Steeper than the matching angle.")]
    cands[1] = (f"{2 * a0}°" if 2 * a0 != 90 - a0 else "15°", "Doubling the angle does not match.")
    it.append(("S2.3", f"A ball is launched at {a0}° from level ground. At the same speed, which other launch angle gives the same range?",
               right, _pick(cands, right)))

    p10 = [
        ("On level ground, with no air resistance and the same launch speed, which angle gives the greatest range?", "45°",
         [("30°", "Not the best angle."), ("60°", "Not the best angle."), ("90°", "That sends it straight up.")]),
        ("A cannon fires at a fixed speed over level ground. Which launch angle sends the ball farthest?", "45°",
         [("15°", "Too flat."), ("75°", "Too steep."), ("90°", "That sends it straight up.")]),
        ("To throw a ball the farthest horizontal distance on level ground at a given speed, aim at about", "45° above the horizontal",
         [("0° (horizontal)", "That gives almost no flight time."), ("30° above the horizontal", "Not the best angle."),
          ("60° above the horizontal", "Not the best angle.")]),
    ][i]
    it.append(("S2.3", p10[0], p10[1], p10[2]))

    v, ang = [(20, 60), (30, 30), (16, 30)][i]
    r = math.radians(ang)
    right = f"{v * math.cos(r):.0f} m/s"
    cands = [("0 m/s", "The ball is still moving sideways at the top."), (f"{v} m/s", "That is the launch speed, not the speed at the top."),
             (f"{v * math.sin(r):.0f} m/s", "That is the vertical component at launch.")]
    it.append(("S2.3", f"A ball is launched at {v} m/s at {ang}° above the horizontal. At the top of its path, its speed is", right, _pick(cands, right)))

    p12 = [
        ("A ball is thrown at an angle from a cliff and lands on the ground far below. Compared with the same throw from level ground, it",
         "stays in the air longer and lands farther away",
         [("stays in the air the same time and lands farther away", "The extra fall adds time."), ("stays in the air longer but lands the same distance away", "More time means more horizontal distance."),
          ("stays in the air a shorter time", "It has farther to fall, so it takes longer.")]),
        ("An arrow is shot from a castle wall and lands at the foot of the hill below. Compared with a shot from level ground at the same speed and angle, the arrow",
         "has a longer time of flight and a greater range",
         [("has the same time of flight and a greater range", "The extra fall adds time."), ("has a longer time of flight and the same range", "More time means more horizontal distance."),
          ("has a shorter time of flight", "It falls farther, so it takes longer.")]),
        ("A football is kicked from the top of a stadium roof at an angle and lands on the field. Compared with the same kick from the field, it",
         "stays in the air longer and travels farther horizontally",
         [("stays in the air the same time", "The extra fall adds time."), ("travels the same horizontal distance", "More time means more horizontal distance."),
          ("stays in the air a shorter time", "It falls farther, so it takes longer.")]),
    ][i]
    it.append(("S2.3", p12[0], p12[1], p12[2]))

    vy0, t = [(24.5, 2.0), (29.4, 4.0), (14.7, 3.0)][i]
    vy = vy0 - G * t
    word = lambda x: f"{abs(x):.1f} m/s " + ("upward" if x > 0 else "downward")
    right = word(vy)
    cands = [(word(-vy), "Sign error: down is negative in the equation."), (word(vy0 + G * t), "Added gt instead of subtracting it."),
             (word(vy0 - G), "Used one second instead of the actual time.")]
    it.append(("S2.3", f"A ball is launched with an initial vertical velocity of {vy0} m/s upward. What is its vertical velocity {t:.1f} s later? (Ignore air resistance.)",
               right, _pick(cands, right)))
    return it


MC_SECTIONS = [(0, 7, "S2.1  VECTORS & VECTOR BASICS"), (7, 17, "S2.2  VECTOR ADDITION"), (17, 30, "S2.3  PROJECTILE MOTION")]


def build_mc(L):
    """Shuffle each section's questions and place the correct answer in a balanced position.
    Returns [{"n", "std", "stem", "choices":[(text, why)], "answer": 0-3, "base": blueprint index}]."""
    i = VERS.index(L)
    items = mc_items(i)
    assert len(items) == 30
    rng = random.Random(1000 + i)
    order = []
    for lo, hi, _ in MC_SECTIONS:
        idx = list(range(lo, hi))
        rng.shuffle(idx)
        order += idx
    pos = [k % 4 for k in range(30)]
    rng.shuffle(pos)
    out = []
    for n, (b, p) in enumerate(zip(order, pos), 1):
        std, stem, right, wrong = items[b]
        wrong = list(wrong)
        rng.shuffle(wrong)
        ch = wrong[:p] + [(right, None)] + wrong[p:]
        out.append({"n": n, "std": std, "stem": stem, "choices": ch, "answer": p, "base": b})
    return out


# ---------------------------------------------------------------------------------------
# Study guide problems
# ---------------------------------------------------------------------------------------

GUIDE = {          # five problems, same types as the Day 2 written test, new numbers
    "p1": {"x": 2.5, "y": -6.0, "unit": "m/s"},
    "p2": {"unit": "km/h", "v": [(210, (15, "north", "east")), (70, (55, "north", "west"))]},
    "p3": {"h": 3.0, "vx": 4.5},
    "p4": {"v": 30.0, "ang": 40.0},
    "p5": {"y0": 20.0, "v": 30.0, "ang": 25.0},
}


def solve_guide():
    g = GUIDE
    out = {}
    x, y = g["p1"]["x"], g["p1"]["y"]
    out["p1"] = {"R": math.hypot(x, y), "th": math.degrees(math.atan2(y, x)) % 360}
    vs = [(m, V.theta_from(*sp)) for m, sp in g["p2"]["v"]]
    rx, ry, R, th = V.addition(vs)
    out["p2"] = {"vs": vs, "parts": [V.comps(m, t) for m, t in vs], "rx": rx, "ry": ry, "R": R, "th": th}
    out["p3"] = horizontal_launch(g["p3"]["h"], g["p3"]["vx"])
    out["p4"] = level_angled(g["p4"]["v"], g["p4"]["ang"])
    out["p5"] = from_height(g["p5"]["y0"], g["p5"]["v"], g["p5"]["ang"])
    return out


if __name__ == "__main__":
    for L in VERS:
        s = solve_written(L)
        print(L, {k: {a: (round(b, 3) if isinstance(b, float) else b) for a, b in v.items() if a not in ("vs", "parts")} for k, v in s.items()})
    for L in VERS:
        mc = build_mc(L)
        print(L, "answers", "".join("ABCD"[q["answer"]] for q in mc))
    print(solve_guide())
