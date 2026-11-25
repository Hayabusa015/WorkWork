"""Writes templates/worksheet/specs/phys_u03_s03.4_newtons_second_law.json. Every answer is
recomputed and asserted here first. g = 9.8 m/s^2 is treated as exact. No friction coefficient
appears (3.5 Friction comes later): friction and drag are given forces in newtons."""
import json, re
from math import sin, cos, radians
OUT = "/home/user/WorkWork/templates/worksheet/specs/phys_u03_s03.4_newtons_second_law.json"
g = 9.8
def near(a, b, tol=0.0051): assert abs(a-b) <= tol*max(1, abs(b)), (a, b)

# 1. shopping cart: a = ∑F/m
s1 = 45.0 - 15.0; a1 = s1/15.0; near(s1, 30.0); near(a1, 2.00)
# 2. e-scooter: solve for m
s2 = 180 - 60.0; m2 = s2/1.50; near(s2, 120); near(m2, 80.0)
# 3. bike braking while moving east (east +): ∑F and a point west
s3 = -105 - 45.0; a3 = s3/60.0; near(s3, -150); near(a3, -2.50); W3 = 60.0*g; near(W3, 588)
# 4. suitcase pulled at 40.0° above the horizontal, no friction
Fx4, Fy4 = 45.0*cos(radians(40)), 45.0*sin(radians(40)); W4 = 15.0*g
a4 = Fx4/15.0; N4 = W4 - Fy4
near(Fx4, 34.5, 0.002); near(Fy4, 28.9, 0.002); near(W4, 147); near(a4, 2.30, 0.002); near(N4, 118, 0.002)
# 5. frictionless water slide, 32.0°: a = g sin θ for both riders
for m in (52.0, 24.0):
    s5 = m*g*sin(radians(32)); a5 = s5/m; near(a5, 5.19, 0.001)
a5 = g*sin(radians(32)); near(a5, 5.19, 0.001)
N5L, N5E = 52.0*g*cos(radians(32)), 24.0*g*cos(radians(32))
# 6. elevator, up +: FN − mg = ma
W6 = 60.0*g; N6a = W6 + 60.0*1.20; N6b = W6 + 60.0*(-1.20)
near(W6, 588); near(N6a, 660); near(N6b, 516)
# 7. wagon, handle 30.0° above the horizontal, rolling friction 30.0 N given
Fx7 = 80.0*cos(radians(30)); a7 = (Fx7 - 30.0)/30.0
near(Fx7, 69.3, 0.001); near(a7, 1.31, 0.002)
s7b = 30.0*0.500; Fx7b = s7b + 30.0; F7b = Fx7b/cos(radians(30))
near(s7b, 15.0); near(Fx7b, 45.0); near(F7b, 52.0, 0.002)
N7 = 30.0*g - 80.0*sin(radians(30)); near(N7, 254)

def F(label, d, mag, off=0.0):
    f = {"label": label, "dir": d, "mag": mag}
    if off: f["offset"] = off
    return f
def panel(*forces, caption=None, tilt=0, surface=True, obj=None):
    p = {"forces": list(forces)}
    if tilt: p["tiltDeg"] = tilt
    if surface: p["surface"] = True
    if caption: p["caption"] = caption
    if obj: p["object"] = obj
    return p
def fbd(*panels, arrowPx=150):
    big = max(f["mag"] for p in panels for f in p["forces"])
    short = min(f["mag"] for p in panels for f in p["forces"]) / big * arrowPx
    assert short >= 50, ("arrow not clearly longer than its 20 px head", short)
    return {"scene": "fbd", "panels": list(panels), "arrowPx": arrowPx, "labelPad": 24}
R = lambda *items: {"row": list(items)}
A = lambda lhs, val: {"answer": [lhs], "value": val}
NOTE = lambda s: {"say": s, "ink": "arrow"}
SAY = lambda s: {"say": s, "ink": "pen"}
frac = lambda n, d: {"frac": [n, d]}

qs = [
 {"tier": "warm-up", "points": 2, "calculation": True, "selfCheck": "[  2.00 m/s² forward  ]",
  "prompt": "Priya pushes a 15.0 kg grocery cart with 45.0 N forward. Wheel friction pushes back with 15.0 N. Find its acceleration.",
  "solution": "Forward is positive. ∑F = 45.0 − 15.0 = 30.0 N forward. a = ∑F/m = 30.0/15.0 = 2.00 m/s² forward.",
  "finalAnswer": "2.00 m/s² forward",
  "keyImage": fbd(panel(F("45.0 N", "right", 45.0), F("f = 15.0 N", "left", 15.0),
                        F("F_{N}", "up", 22.0), F("F_{g}", "down", 22.0))),
  "steps": [R("forward = +"), R("∑F = 45.0 N − 15.0 N = 30.0 N"),
            R("a =", frac("∑F", "m"), "=", frac("30.0 N", "15.0 kg")), A("a =", "2.00 m/s^{2} forward"),
            NOTE("F_{N} and F_{g} balance and are not to scale; the cart's weight is 147 N.")]},
 {"tier": "warm-up", "points": 2, "calculation": True, "selfCheck": "[  80.0 kg  ]",
  "prompt": "Your electric scooter's motor drives you forward with 180 N, and air drag plus rolling friction push back with 60.0 N. You speed up at 1.50 m/s². What is the mass of you and the scooter together?",
  "solution": "Forward is positive. ∑F = 180 − 60.0 = 120 N forward. m = ∑F/a = 120/1.50 = 80.0 kg.",
  "finalAnswer": "80.0 kg",
  "keyImage": fbd(panel(F("180 N", "right", 180), F("60.0 N", "left", 60.0),
                        F("F_{N}", "up", 90.0), F("F_{g}", "down", 90.0))),
  "steps": [R("forward = +"), R("∑F = 180 N − 60.0 N = 120 N"),
            R("∑F = ma, so m =", frac("∑F", "a")),
            R("m =", frac("120 N", "1.50 m/s^{2}")), A("m =", "80.0 kg"),
            NOTE("1 N = 1 kg·m/s^{2}, so N ÷ m/s^{2} leaves kg. Mass has no direction.")]},
 {"tier": "practice", "points": 3, "calculation": True, "selfCheck": "[  150 N west  ·  2.50 m/s² west  ]",
  "prompt": "Jada is coasting east on her bike when a dog darts out, so she brakes. She and the bike are 60.0 kg. Her brakes give 105 N west and air drag 45.0 N west. Find ∑F and her acceleration. Which way does she accelerate while rolling east?",
  "solution": "East is positive. ∑F = −105 − 45.0 = −150 N, so 150 N west. a = −150/60.0 = −2.50 m/s², so 2.50 m/s² west. She accelerates west, the direction of ∑F, even though she is still moving east: she is slowing down.",
  "finalAnswer": "∑F = 150 N west; a = 2.50 m/s² west, while she still moves east (slowing down)",
  "keyImage": fbd(panel(F("brakes 105 N", "left", 105, -0.3), F("drag 45.0 N", "left", 45.0, 0.3),
                        F("F_{N}", "up", 55.0), F("F_{g}", "down", 55.0)), arrowPx=130),
  "steps": [R("east = +"), R("∑F = −105 N − 45.0 N"), A("∑F =", "150 N west"),
            R("a =", frac("∑F", "m"), "=", frac("−150 N", "60.0 kg")), A("a =", "2.50 m/s^{2} west"),
            SAY("West, the way ∑F points. She is still moving east, so she is slowing down."),
            NOTE("No arrow for her motion east. F_{N} and F_{g} (588 N) balance; not to scale.")]},
 {"tier": "practice", "points": 3, "calculation": True, "selfCheck": "[  2.30 m/s² forward  ·  118 N  ]",
  "prompt": "Running late for her flight, Nora pulls her 15.0 kg rolling suitcase by its handle with 45.0 N at 40.0° above the horizontal. Ignore friction.",
  "parts": ["a.  Find the suitcase's acceleration.",
            "b.  Find the normal force from the floor."],
  "solution": "Forward and up are positive. Horizontal part 45.0 cos 40.0° = 34.5 N; vertical part 45.0 sin 40.0° = 28.9 N.\na. a = 34.5/15.0 = 2.30 m/s² forward.\nb. No vertical acceleration: FN + 28.9 − 147 = 0, so FN = 118 N up.",
  "finalAnswer": "a. 2.30 m/s² forward. b. 118 N up.",
  "keyImage": fbd(panel(F("45.0 N", 40, 45.0), F("F_{N}", "up", N4), F("F_{g}", "down", W4)), arrowPx=170),
  "steps": [R("forward = +, up = +"),
            R("F_{x} = (45.0 N) cos 40.0° = 34.5 N"), R("F_{y} = (45.0 N) sin 40.0° = 28.9 N"),
            R("a. a =", frac("F_{x}", "m"), "=", frac("34.5 N", "15.0 kg")), A("a =", "2.30 m/s^{2} forward"),
            R("b. F_{N} + F_{y} − mg = 0"), R("F_{N} = 147 N − 28.9 N"), A("F_{N} =", "118 N up"),
            NOTE("The handle lifts part of the weight, so F_{N} is less than mg.")]},
 {"tier": "practice", "points": 3, "calculation": True, "selfCheck": "[  5.19 m/s²  ·  same  ]",
  "prompt": "At the water park, Liam (52.0 kg) and his little sister Emma (24.0 kg) take turns on a straight slide tilted 32.0° above the horizontal. Treat the slide as frictionless.",
  "parts": ["a.  Find Liam's acceleration.",
            "b.  Does Emma speed up faster, slower or at the same rate? Show why."],
  "solution": "Down the slide is positive. ∑F = mg sin θ, so ma = mg sin θ and a = g sin θ.\na. a = 9.8 sin 32.0° = 5.19 m/s² down the slide.\nb. The same, 5.19 m/s² down the slide. Mass cancels: a = g sin θ has no m in it. Emma has less force down the slide, but also less mass to speed up.",
  "finalAnswer": "a. 5.19 m/s² down the slide. b. The same, 5.19 m/s² down the slide; mass cancels in a = g sin θ.",
  "keyImage": fbd(panel(F("F_{N}", 122, N5L), F("F_{g}", "down", 52.0*g), tilt=32, caption="Liam"), arrowPx=130),
  "steps": [R("down the slide = +"), R("∑F = mg sin θ"), R("ma = mg sin θ, so a = g sin θ"),
            R("a. a = (9.8 m/s^{2}) sin 32.0°"), A("a =", "5.19 m/s^{2} down the slide"),
            SAY("b. The same rate. m cancels, so a = g sin θ for any rider."),
            NOTE("Emma's diagram has the same shape, scaled down. She has less pull down the slide, but less mass to speed up.")]},
 {"tier": "challenge", "points": 4, "calculation": True, "selfCheck": "[  660 N  ·  516 N  ]",
  "prompt": "Zoe, whose mass is 60.0 kg, stands on a bathroom scale in a hotel elevator. The scale reads in newtons.",
  "parts": ["a.  Leaving the lobby, the elevator speeds up going up at 1.20 m/s². What does the scale read?",
            "b.  Later, leaving the top floor, it speeds up going down at 1.20 m/s². What does the scale read now?"],
  "solution": "Up is positive. The scale reads FN. mg = 60.0 × 9.8 = 588 N. FN − mg = ma, so FN = mg + ma.\na. a = +1.20 m/s²: FN = 588 + 60.0(1.20) = 660 N.\nb. a = −1.20 m/s²: FN = 588 + 60.0(−1.20) = 516 N.",
  "finalAnswer": "a. 660 N. b. 516 N. (Both are the upward normal force; her weight is 588 N.)",
  "keyImage": fbd(panel(F("F_{N} = 660 N", "up", N6a), F("F_{g} = 588 N", "down", W6), caption="a. speeding up, going up"), arrowPx=120),
  "steps": [R("up = +"), R("mg = (60.0 kg)(9.8 m/s^{2}) = 588 N"), R("F_{N} − mg = ma, so F_{N} = mg + ma"),
            R("a. F_{N} = 588 N + (60.0 kg)(1.20 m/s^{2})"), A("a.  scale:", "660 N"),
            R("b. a = −1.20 m/s^{2}"), R("F_{N} = 588 N + (60.0 kg)(−1.20 m/s^{2})"), A("b.  scale:", "516 N"),
            NOTE("In b, F_{N} (516 N) is shorter than F_{g}. The scale reads F_{N}; it changes with the acceleration, not with which way she rides.")]},
 {"tier": "multi-topic", "points": 5, "calculation": True,
  "prompt": "Grandpa pulls his grandson in a wagon by a handle tilted 30.0° above the horizontal. Wagon and grandson have a mass of 30.0 kg, and rolling friction on the wheels is 30.0 N.",
  "parts": ["a.  He pulls with 80.0 N. Find the wagon's acceleration.",
            "b.  How hard would he have to pull, at the same angle, to speed up at 0.500 m/s² instead?"],
  "solution": "Forward is positive.\na. Fx = 80.0 cos 30.0° = 69.3 N. ∑F = 69.3 − 30.0 = 39.3 N forward. a = 39.3/30.0 = 1.31 m/s² forward.\nb. ∑F = ma = 30.0 × 0.500 = 15.0 N. Fx − 30.0 = 15.0, so Fx = 45.0 N. F = 45.0/cos 30.0° = 52.0 N at 30.0° above the horizontal.",
  "finalAnswer": "a. 1.31 m/s² forward. b. 52.0 N at 30.0° above the horizontal.",
  "keyImage": fbd(panel(F("80.0 N", 30, 80.0), F("f = 30.0 N", "left", 30.0),
                        F("F_{N}", "up", 60*N7/(30.0*g)), F("F_{g}", "down", 60.0)), arrowPx=150),
  "steps": [R("forward = +"),
            R("a. F_{x} = (80.0 N) cos 30.0° = 69.3 N"), R("∑F = 69.3 N − 30.0 N = 39.3 N"),
            R("a =", frac("39.3 N", "30.0 kg")), A("a =", "1.31 m/s^{2} forward"),
            R("b. ∑F = ma = (30.0 kg)(0.500 m/s^{2}) = 15.0 N"),
            R("F_{x} − 30.0 N = 15.0 N, so F_{x} = 45.0 N"),
            R("F =", frac("F_{x}", "cos θ"), "=", frac("45.0 N", "cos 30.0°")), A("F =", "52.0 N at 30.0° above horizontal"),
            NOTE("F_{N} (254 N) and F_{g} (294 N) are drawn shorter than scale.")]},
]
assert [q["points"] for q in qs] == [2, 2, 3, 3, 3, 4, 5]
for q in qs:
    q["prompt"] = re.sub(r"(\d) (N|kg)\b", "\\1\u00a0\\2", q["prompt"])
    if "parts" in q:
        q["parts"] = [re.sub(r"(\d) (N|kg)\b", "\\1\u00a0\\2", x) for x in q["parts"]]
    text = q["prompt"] + " ".join(q.get("parts", []))
    assert "Fnet" not in text and "μ" not in text and "+x" not in text and "Σ" not in text
assert all("selfCheck" in q for q in qs[:-1]) and "selfCheck" not in qs[-1]
spec = {
 "$comment": "Physics 3.4 practice set, Newton's Second Law: 7 problems, Matt's net-force-set style. One-time build override: RAMP['physics'] = 2/3/1/1 in memory for 7 items (see build script). Tier tags hidden (tierTags: false). No graph item and everyday scenarios: rule conflicts reported, not resolved. No μ (3.5 Friction not yet taught); friction and drag are given forces. Descriptor 'Newton's Second Law' pending Matt's OK.",
 "course": "physics", "unit": 3, "sections": ["3.4"], "docType": "Practice_Set",
 "timeTargetMin": "30–40", "equationLabel": "EQUATIONS YOU MAY USE", "pagesPerSection": 1,
 "equationStyle": "inline", "equationColumns": 2, "tierTags": False,
 "keyLayout": "side", "keyFbdIn": 2.6, "keyStepScale": 0.85,
 "sectionsContent": [{
  "code": "3.4", "title": "Newton's Second Law", "compactTop": True,
  "priorKnowledge": {"items": [
    "∑F adds every force, with signs for direction (S3.2). Split an angled force with sin and cos (S2.1)."]},
  "equations": [
    {"note": "second law", "plain": "∑F = ma     a = ∑F / m"},
    {"note": "weight", "plain": "F_{g} = mg     g = 9.8 m/s²"},
    {"note": "frictionless ramp", "plain": "a = g sin θ"},
    {"note": "elevator (up +)", "plain": "F_{N} − mg = ma"}],
  "directions": "Draw a free-body diagram, then solve. Forward, east, up and down a slide are positive. Answers need units and directions.",
  "questions": qs}]}
json.dump(spec, open(OUT, "w"), ensure_ascii=False, indent=1)
print("wrote", OUT, len(qs), "questions,", sum(q["points"] for q in qs), "points")
