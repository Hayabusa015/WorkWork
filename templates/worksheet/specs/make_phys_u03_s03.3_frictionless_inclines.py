"""Writes templates/worksheet/specs/phys_u03_s03.3_frictionless_inclines.json. Every answer is
recomputed and asserted here first. g = 9.8 m/s^2 is treated as exact."""
import json, re
from math import sin, cos, radians
OUT = "/home/user/WorkWork/templates/worksheet/specs/phys_u03_s03.3_frictionless_inclines.json"
g = 9.8
def inc(m, d): W = m*g; return W, W*sin(radians(d)), W*cos(radians(d))
def near(a, b, tol=0.0051): assert abs(a-b) <= tol*max(1, abs(b)), (a, b)
W, p, n = inc(3.20, 20.0); near(W, 31.36); near(p, 10.7, 0.003); near(n, 29.5, 0.003)
W, p, n = inc(18.0, 35.0); near(W, 176.4); near(p, 101, 0.003); near(n, 144, 0.004); assert round(n) == 144
W, p, n = inc(0.250, 15.0); near(W, 2.45); near(p, 0.634, 0.001); near(n, 2.37, 0.002)
W, p, n = inc(0.250, 50.0); near(p, 1.88, 0.002); near(n, 1.57, 0.0035); assert round(n, 2) == 1.57
W, p, n = inc(22.0, 20.0); near(W, 215.6); near(p, 73.7, 0.001); near(p - 60.0, 13.7, 0.004); near(n, 202.6, 0.001)
W, p, n = inc(32.0, 15.0); near(W, 313.6); near(p, 81.2, 0.001)
W, p, n = inc(65.0, 18.0); near(W, 637); near(p, 197, 0.002); near(n, 606, 0.001); assert round(255 - p) == 58

def F(label, d, mag, off=0.0):
    f = {"label": label, "dir": d, "mag": mag}
    if off: f["offset"] = off
    return f
def ramp(th, *forces, caption=None):
    p = {"forces": list(forces), "tiltDeg": th, "surface": True}
    if caption: p["caption"] = caption
    return p
def fbd(*panels, arrowPx=120):
    return {"scene": "fbd", "panels": list(panels), "arrowPx": arrowPx, "labelPad": 24}
R = lambda *items: {"row": list(items)}
A = lambda lhs, val: {"answer": [lhs], "value": val}
NOTE = lambda s: {"say": s, "ink": "arrow"}
SAY = lambda s: {"say": s, "ink": "pen"}
frac = lambda n, d: {"frac": [n, d]}
UP = lambda th: th              # up the ramp (ramp rises to the right)
DOWN = lambda th: 180 + th      # down the ramp
PERP = lambda th: 90 + th       # perpendicular to the ramp, out of the surface

qs = [
 {"tier": "warm-up", "points": 2, "calculation": True, "selfCheck": "[  31.4 N  ·  10.7 N  ·  29.5 N  ]",
  "prompt": "Ty sets his 3.20 kg skateboard on a smooth ramp tilted 20.0° above the horizontal and lets go. Find the skateboard's weight, the part of that weight pulling it down the ramp, and the part pressing it into the ramp.",
  "solution": "Fg = mg = 3.20 × 9.8 = 31.4 N down. Fg,parallel = 31.36 sin 20.0° = 10.7 N down the ramp. Fg,perp = 31.36 cos 20.0° = 29.5 N into the ramp.",
  "finalAnswer": "Fg = 31.4 N down; Fg,parallel = 10.7 N down the ramp; Fg,perp = 29.5 N into the ramp",
  "keyImage": fbd(ramp(20, F("F_{N}", PERP(20), 29.47), F("F_{g}", "down", 31.36))),
  "steps": [R("F_{g} = mg = (3.20 kg)(9.8 m/s^{2})"), A("F_{g} =", "31.4 N down"),
            R("F_{g,parallel} = mg sin θ = (31.36 N) sin 20.0°"), A("F_{g,parallel} =", "10.7 N down the ramp"),
            R("F_{g,perp} = mg cos θ = (31.36 N) cos 20.0°"), A("F_{g,perp} =", "29.5 N into the ramp"),
            NOTE("Only two forces act: F_{g} and F_{N}. The parallel and perpendicular parts are pieces of F_{g}, not extra arrows.")]},
 {"tier": "warm-up", "points": 2, "calculation": True, "selfCheck": "[  101 N  ·  144 N  ]",
  "prompt": "An 18.0 kg box of books sits on the rollers of a loading ramp tilted 35.0° above the horizontal. The rollers make the ramp frictionless. Find the force pulling the box down the ramp and the normal force on the box.",
  "solution": "Fg = 18.0 × 9.8 = 176.4 N. Fg,parallel = 176.4 sin 35.0° = 101 N down the ramp. FN = mg cos θ = 176.4 cos 35.0° = 144 N, perpendicular to the ramp, away from its surface.",
  "finalAnswer": "Fg,parallel = 101 N down the ramp; FN = 144 N perpendicular to the ramp",
  "keyImage": fbd(ramp(35, F("F_{N}", PERP(35), 144.5), F("F_{g}", "down", 176.4))),
  "steps": [R("F_{g} = (18.0 kg)(9.8 m/s^{2}) = 176.4 N"),
            R("F_{g,parallel} = (176.4 N) sin 35.0°"), A("F_{g,parallel} =", "101 N down the ramp"),
            R("F_{N} = mg cos θ = (176.4 N) cos 35.0°"), A("F_{N} =", "144 N perpendicular to the ramp"),
            NOTE("F_{N} = mg cos θ only because nothing else pushes into or pulls away from the ramp.")]},
 {"tier": "practice", "points": 3, "calculation": True,
  "selfCheck": "[  15.0°: 0.634 N  ·  2.37 N     50.0°: 1.88 N  ·  1.57 N  ]",
  "prompt": "Mia props up a board with books to make a ramp for her brother's 0.250 kg toy car. First the board is tilted 15.0° above the horizontal. Then she adds books until it is tilted 50.0°.",
  "parts": ["a.  At each angle, find the force pulling the car down the ramp and the normal force on it.",
            "b.  Which force grows as the ramp gets steeper, and which one shrinks?"],
  "solution": "Fg = 0.250 × 9.8 = 2.45 N.\na. 15.0°: Fg,parallel = 2.45 sin 15.0° = 0.634 N down the ramp; FN = 2.45 cos 15.0° = 2.37 N perpendicular to the ramp. 50.0°: Fg,parallel = 2.45 sin 50.0° = 1.88 N down the ramp; FN = 2.45 cos 50.0° = 1.57 N perpendicular to the ramp.\nb. The pull down the ramp grows (sin θ grows); the normal force shrinks (cos θ shrinks).",
  "finalAnswer": "15.0°: 0.634 N down the ramp, FN 2.37 N. 50.0°: 1.88 N down the ramp, FN 1.57 N. The down-ramp pull grows; FN shrinks.",
  "keyImage": fbd(ramp(15, F("F_{N}", PERP(15), 2.367), F("F_{g}", "down", 2.45), caption="15.0°"),
                  ramp(50, F("F_{N}", PERP(50), 1.575), F("F_{g}", "down", 2.45), caption="50.0°"), arrowPx=110),
  "steps": [R("F_{g} = (0.250 kg)(9.8 m/s^{2}) = 2.45 N"),
            R("15.0°:  F_{g,parallel} = (2.45 N) sin 15.0° = 0.634 N down the ramp"),
            R("F_{N} = (2.45 N) cos 15.0° = 2.37 N"),
            R("50.0°:  F_{g,parallel} = (2.45 N) sin 50.0° = 1.88 N down the ramp"),
            R("F_{N} = (2.45 N) cos 50.0° = 1.57 N"),
            SAY("b. The pull down the ramp grows and the normal force shrinks. A steeper ramp holds up less of the weight."),
            NOTE("F_{g} is the same 2.45 N at both angles. Only how it splits changes.")]},
 {"tier": "practice", "points": 3, "calculation": True, "selfCheck": "[  13.7 N  ]",
  "prompt": "Lena is pushing her little brother up the driveway in a wagon. The driveway is steep, tilted 20.0° above the horizontal, and the wagon plus her brother come to 22.0 kg. She pushes with 60.0 N parallel to the driveway. Ignore friction.",
  "parts": ["a.  Find the net force on the wagon along the driveway, with its direction.",
            "b.  Is her push enough to keep the wagon from rolling back down?"],
  "solution": "Down the driveway is positive. Fg,parallel = 22.0 × 9.8 × sin 20.0° = 73.7 N down the driveway. ∑F = 73.7 − 60.0 = 13.7 N down the driveway.\nb. No. The forces are not balanced: the net force points down the driveway. It would take 73.7 N up the driveway to balance.",
  "finalAnswer": "a. 13.7 N down the driveway. b. No; it would take 73.7 N.",
  "keyImage": fbd(ramp(20, F("F_{app} = 60.0 N", UP(20), 60.0), F("F_{N}", PERP(20), 202.6), F("F_{g}", "down", 215.6)),
                  arrowPx=150),
  "steps": [R("down the driveway = +"),
            R("F_{g,parallel} = (22.0 kg)(9.8 m/s^{2}) sin 20.0° = 73.7 N"),
            R("∑F = 73.7 N − 60.0 N"), A("∑F =", "13.7 N down the driveway"),
            SAY("b. No. It would take 73.7 N up the driveway to balance.")]},
 {"tier": "challenge", "points": 4, "calculation": True, "selfCheck": "[  81.2 N  ]",
  "prompt": "On an icy sledding hill tilted 15.0° above the horizontal, Dad holds the rope so the sled won't slide while his daughter climbs on. Sled and daughter have a mass of 32.0 kg, and the rope runs parallel to the hill. Treat the ice as frictionless. How hard does Dad have to pull to hold the sled still?",
  "solution": "At rest, so ∑F along the hill = 0. T = Fg,parallel = 32.0 × 9.8 × sin 15.0° = 81.2 N up the hill.",
  "finalAnswer": "81.2 N up the hill, parallel to it",
  "keyImage": fbd(ramp(15, F("T", UP(15), 81.17), F("F_{N}", PERP(15), 302.9), F("F_{g}", "down", 313.6)), arrowPx=170),
  "steps": [R("at rest:  ∑F along the hill = 0"), R("T = F_{g,parallel} = mg sin θ"),
            R("T = (32.0 kg)(9.8 m/s^{2}) sin 15.0°"), A("T =", "81.2 N up the hill"),
            NOTE("The same pull would let the sled slide down at a constant speed. ∑F = 0 either way.")]},
 {"tier": "multi-topic", "points": 5, "calculation": True,
  "prompt": "Two movers roll a 65.0 kg refrigerator on a hand truck up the ramp into their truck. The ramp is tilted 18.0° above the horizontal, and they push parallel to it. Ignore friction.",
  "parts": ["a.  What push moves the fridge up the ramp at a constant speed?",
            "b.  What is the normal force from the ramp?",
            "c.  If they push with 255 N instead, what is the net force on the fridge?"],
  "solution": "Fg = 65.0 × 9.8 = 637 N.\na. Constant speed: ∑F = 0, so Fapp = 637 sin 18.0° = 197 N up the ramp.\nb. FN = 637 cos 18.0° = 606 N perpendicular to the ramp.\nc. Up the ramp positive: ∑F = 255 − 196.8 = 58 N up the ramp.",
  "finalAnswer": "a. 197 N up the ramp. b. 606 N perpendicular to the ramp. c. 58 N up the ramp.",
  "keyImage": fbd(ramp(18, F("F_{app}", UP(18), 196.8), F("F_{N}", PERP(18), 605.8), F("F_{g}", "down", 637.0)), arrowPx=160),
  "steps": [R("F_{g} = (65.0 kg)(9.8 m/s^{2}) = 637 N"),
            R("a.  constant speed:  ∑F = 0, so F_{app} = mg sin θ"),
            R("F_{app} = (637 N) sin 18.0°"), A("F_{app} =", "197 N up the ramp"),
            R("b.  F_{N} = (637 N) cos 18.0°"), A("F_{N} =", "606 N perpendicular to the ramp"),
            R("c.  up the ramp = +:  ∑F = 255 N − 196.8 N"), A("∑F =", "58 N up the ramp"),
            NOTE("Constant speed is ∑F = 0, the same as holding it still. A moving object does not need a net force.")]},
]
for q in qs:
    q["prompt"] = re.sub(r"(\d) (N|kg)\b", "\\1\u00a0\\2", q["prompt"])
    if "parts" in q:
        q["parts"] = [re.sub(r"(\d) (N|kg)\b", "\\1\u00a0\\2", x) for x in q["parts"]]
assert all("selfCheck" in q for q in qs[:-1]) and "selfCheck" not in qs[-1]
spec = {
 "$comment": "Physics 3.3 practice set, Frictionless Inclines: 6 problems, Matt's net-force-set style, standard 2/2/1/1 ramp. Tier tags hidden (tierTags: false). No graph item and everyday scenarios: rule conflicts reported, not resolved. No ∑F = ma: Matt removed the acceleration problem (not before 3.4).",
 "course": "physics", "unit": 3, "sections": ["3.3"], "docType": "Practice_Set",
 "timeTargetMin": "30–40", "equationLabel": "EQUATIONS YOU MAY USE", "pagesPerSection": 1,
 "equationStyle": "inline", "equationColumns": 2, "tierTags": False,
 "sectionsContent": [{
  "code": "3.3", "title": "Frictionless Inclines", "compactTop": True,
  "priorKnowledge": {"items": [
    "Weight is Fg = mg, with g = 9.8 m/s² (S3.1). A free-body diagram has one labelled arrow per force (S3.2).",
    "Split a force with sin and cos (S2.1). On a ramp, tilt your axes along and perpendicular to the ramp (S3.3)."]},
  "equations": [
    {"note": "weight", "plain": "F_{g} = mg     g = 9.8 m/s²"},
    {"note": "down the ramp", "plain": "F_{g,parallel} = mg sin θ"},
    {"note": "into the ramp", "plain": "F_{g,perp} = mg cos θ"},
    {"note": "normal force", "plain": "F_{N} = mg cos θ"},
    {"note": "net force", "plain": "∑F = F_{1} + F_{2} + …  (along the ramp)"}],
  "directions": "Draw a free-body diagram for each problem, then answer in your notebook. Every ramp is frictionless. Give each force a unit and a direction, like down the ramp.",
  "questions": qs}]}
json.dump(spec, open(OUT, "w"), ensure_ascii=False, indent=1)
print("wrote", OUT, len(qs), "questions,", sum(q["points"] for q in qs), "points")
