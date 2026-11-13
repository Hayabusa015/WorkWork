"""Independent check for the Physics U2 S2.2 quiz, versions A and B (run by phys_u02_s02.2_quiz.build.sh).

Recomputes everything from the givens in plain Python and exits 1 on any mismatch:
  - every "same direction:" form on Q1-Q3 points the same way as the given direction (exact)
  - Q4 and Q5 magnitude and direction match the boxed answers and the finalAnswer strings
  - the points add to 16, and no unwanted glyphs reach the student page
"""
import json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
AX = {"east": 0, "north": 90, "west": 180, "south": 270}
fail = 0
def report(ok, msg):
    global fail
    fail += not ok
    print(("PASS  " if ok else "FAIL  ") + msg)

def ang(form):
    form = form.strip().replace("−", "-")
    m = re.fullmatch(r"(-?[\d.]+)°", form)
    if m: return float(m.group(1))
    m = re.fullmatch(r"([\d.]+)° (\w+) of (\w+)", form)
    if m:
        d, to, frm = float(m.group(1)), AX[m.group(2)], AX[m.group(3)]
        turn = ((to - frm + 180) % 360) - 180
        return frm + d * (1 if turn > 0 else -1)
    raise ValueError(form)

def res(vecs):
    x = sum(m * math.cos(math.radians(a)) for m, a in vecs)
    y = sum(m * math.sin(math.radians(a)) for m, a in vecs)
    return x, y, math.hypot(x, y), math.degrees(math.atan2(y, x)) % 360

# (given direction on the 0-360 scale as the sheet words it, then vectors for Q4 and Q5)
CASES = {
    "a": dict(given=[215, 140, -70],
              q4=[(45, 90), (28, 180)], q4_exp=(53, 122),
              q5=[(240, 40), (65, -30)], q5_exp=(270, 27)),
    "b": dict(given=[310, 205, -200],
              q4=[(52, 0), (36, 270)], q4_exp=(63, 325),
              q5=[(24, 155), (9.0, 50)], q5_exp=(23, 133)),
}
def sig2(x): return float(f"{x:.2g}")
for v, c in CASES.items():
    spec = json.load(open(os.path.join(HERE, f"phys_u02_s02.2_quiz_{v}.json"), encoding="utf-8"))
    qs = spec["sectionsContent"][0]["questions"]
    report(sum(q["points"] for q in qs) == 16, f"{v.upper()}: points total 16")
    # Q1-Q3: each listed form is the given direction, and the prompt states that direction
    for i, g in enumerate(c["given"]):
        line = next(s["row"][0] for s in qs[i]["steps"] if "row" in s and s["row"][0].startswith("same direction:"))
        forms = line.split(":", 1)[1].split("=")
        devs = [abs(((ang(f) - g + 180) % 360) - 180) for f in forms]
        report(all(d < 1e-9 for d in devs) and len(forms) >= 3, f"{v.upper()} Q{i+1}: {len(forms)} listed forms all equal the given direction")
        boxed = [s["value"] for s in qs[i]["steps"] if "answer" in s]
        report(all(abs(((ang(b) - g + 180) % 360) - 180) < 1e-9 for b in boxed), f"{v.upper()} Q{i+1}: boxed restatements are correct")
        given_in_prompt = re.search(r"Restate (.+?) in two other ways", qs[i]["prompt"]).group(1)
        report(abs(((ang(given_in_prompt) - g + 180) % 360) - 180) < 1e-9, f"{v.upper()} Q{i+1}: prompt direction '{given_in_prompt}' matches the key's direction")
    # Q4, Q5
    for qi, key in ((3, "q4"), (4, "q5")):
        x, y, R, th = res(c[key])
        eR, eth = c[key + "_exp"]
        fa = qs[qi]["finalAnswer"]
        ok = sig2(R) == eR and round(th) % 360 == eth and fa.startswith(f"{eR:g} ") and fa.endswith(f"at {eth}°")
        report(ok, f"{v.upper()} Q{qi+1}: Rx={x:.3f} Ry={y:.3f} R={R:.3f} theta={th:.3f} -> {fa}")
        boxed_deg = [s["value"] for s in qs[qi]["steps"] if "answer" in s and s["answer"][0].startswith("θ")]
        report(boxed_deg == [f"{eth}°"], f"{v.upper()} Q{qi+1}: boxed angle {boxed_deg}")
        fl = next(s["row"][0] for s in qs[qi]["steps"] if "row" in s and s["row"][0].startswith("same direction:"))
        forms = fl.split(":", 1)[1].split("=")
        report(all(abs(((ang(f) - eth + 180) % 360) - 180) < 1e-9 for f in forms), f"{v.upper()} Q{qi+1}: same-direction forms match {eth}°")
    # Q5 is not a right angle
    a1, a2 = c["q5"][0][1], c["q5"][1][1]
    report(abs(((a1 - a2) % 360) - 90) > 5 and abs(((a1 - a2) % 360) - 270) > 5, f"{v.upper()} Q5: vectors are {abs(a1-a2)}° apart, not 90°")
    # Q4 vectors are along the axes
    report(all(a % 90 == 0 for _, a in c["q4"]), f"{v.upper()} Q4: both vectors lie along north/south/east/west")
    visible = [qq["prompt"] for qq in qs] + [spec["sectionsContent"][0]["directions"]]  # θ is allowed only in "equations": the builder draws it
    bad = sorted({ch for s in visible for ch in s if ch in "θΔ₀₁₂₃₄₅₆₇₈₉"})
    report(not bad, f"{v.upper()}: student page free of unsupported glyphs" + (f" found {bad}" if bad else ""))
sys.exit(1 if fail else 0)
