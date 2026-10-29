"""Independent check for the three Physics U02 S2.3 projectile practice sets (run by phys_u02_s02.3_practice.build.sh).

Recomputes every answer from the givens in plain Python and exits 1 on any mismatch. Times are found by
bisection on the height equation, not by the quadratic formula the keys use, so a slip in the key's
algebra cannot hide behind the same slip here. Checks, per set:
  - five questions; points total as the sheet states
  - every value appears in the finalAnswer and in a boxed key answer, and (Q1-Q4) in the self-check
    bracket; the last question carries no bracket (SHULL-CHG-0021)
  - notation: equations use v_i and v_f (never v or v_0), the kinematic equations are written for y only
    and labelled so, x has exactly one equation (v_x = Δx / t) and is labelled so, nothing is solved for
    time, and division is a stacked fraction, never a slash
  - the keys use the same symbols the equations give
  - every "same direction:" line points the same way as its boxed angle
"""
import json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
g = 9.8
fail = 0

def report(ok, msg):
    global fail
    fail += not ok
    print(("PASS  " if ok else "FAIL  ") + msg)

def s2(x):
    d = 1 - math.floor(math.log10(abs(x)))
    return f"{round(x, d):.{max(d, 0)}f}"

def later_root(vy, dy):
    """Later time at which height change = dy for vertical launch speed vy: bisection on vy t - g t^2/2 - dy."""
    f = lambda t: vy * t - 0.5 * g * t * t - dy
    lo = max(vy, 0.0) / g            # the apex (or t = 0 when thrown downward)
    hi = lo + 100.0
    if f(lo) < 0:
        raise ValueError("never reaches that height")
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) >= 0 else (lo, mid)
    return (lo + hi) / 2

def has(text, e):
    """e appears in text as a whole number (not inside 36.3 or 136)."""
    return re.search(rf"(?<![\d.]){re.escape(e)}(?![\d])", text) is not None

def comp(v, a):
    return v * math.cos(math.radians(a)), v * math.sin(math.radians(a))

def expected():
    E = {1: [], 2: [], 3: []}
    t = later_root(0, -45);            E[1].append([s2(t), s2(12 * t)])
    E[1].append([s2(0.5 * g * 0.8 ** 2), s2(3.5 * 0.8)])
    t = 1.2 / 2.0;                     E[1].append([s2(t), s2(0.5 * g * t * t)])
    t = later_root(0, -22);            E[1].append([s2(t), s2(61 / t)])
    t = later_root(0, -2.0);           E[1].append([s2(t), s2(7.5 * t), s2(5.0 / t)])
    # part 2
    vx, vy = comp(24, 30); t = later_root(vy, 0)
    E[2].append([s2(vx), s2(vy), s2(t), s2(vx * t)])
    vx, vy = comp(19, 40); t = later_root(vy, 0); ym = vy * (t / 2) - 0.5 * g * (t / 2) ** 2
    E[2].append([s2(t), s2(vx * t), s2(ym)])
    vy = g * 4.3 / 2; v = vy / math.sin(math.radians(55)); vx = v * math.cos(math.radians(55)); ym = vy * 2.15 - 0.5 * g * 2.15 ** 2
    E[2].append([s2(v), s2(vx * 4.3), s2(ym)])
    row = []
    for ang in (25, 65):
        vx, vy = comp(28, ang); t = later_root(vy, 0); ym = vy * (t / 2) - 0.5 * g * (t / 2) ** 2
        row += [s2(t), s2(vx * t), s2(ym)]
    E[2].append(row)
    vi = math.hypot(15, 11); t = later_root(11, 0); ym = 11 * (t / 2) - 0.5 * g * (t / 2) ** 2
    E[2].append([s2(vi), str(round(math.degrees(math.atan2(11, 15)))), s2(t), s2(15 * t), s2(ym)])
    # part 3
    vx, vy = comp(22, 25); t = later_root(vy, -18);  E[3].append([s2(t), s2(vx * t)])
    vx, vy = comp(14, 60); t = later_root(vy, 6.0);  E[3].append([s2(t), s2(vx * t)])
    vx, vy = comp(28, 40); t = later_root(vy, -15)
    E[3].append([s2(vy * vy / (2 * g) + 15), s2(t), s2(vx * t)])
    return E

AX = {"east": 0, "north": 90, "west": 180, "south": 270}
def ang_of(form):
    form = form.strip().replace("−", "-")
    m = re.fullmatch(r"(-?[\d.]+)°", form)
    if m: return float(m.group(1))
    m = re.fullmatch(r"([\d.]+)° from straight (up|down)", form)
    if m: return (90 - float(m.group(1))) if m.group(2) == "up" else (-90 + float(m.group(1)))
    raise ValueError(form)

def flat(steps):
    out = []
    for st in steps:
        for k in ("row", "mistake"):
            for it in st.get(k, []):
                out.append(it if isinstance(it, str) else " ".join(it["frac"]))
        if "note" in st: out.append(st["note"])
        if "answer" in st: out.append(st["answer"][0] + " " + st["value"])
    return " ".join(out)

E = expected()
POINTS = {1: 14, 2: 16, 3: 9}
NQ = {1: 5, 2: 5, 3: 3}
for part in (1, 2, 3):
    spec = json.load(open(os.path.join(HERE, f"phys_u02_s02.3_part{part}.json"), encoding="utf-8"))
    sec = spec["sectionsContent"][0]
    qs = sec["questions"]
    tag = f"P{part}"
    report(len(qs) == NQ[part], f"{tag}: {NQ[part]} questions")
    report(sum(q["points"] for q in qs) == POINTS[part], f"{tag}: points total {POINTS[part]}")
    for i, (q, exp) in enumerate(zip(qs, E[part]), start=1):
        boxed = [s["value"] for s in q["steps"] if "answer" in s]
        fa = re.sub(r"\([^)]*\)", "", q["finalAnswer"])          # the parentheses hold unrounded values
        okf = all(has(fa, e) for e in exp)
        okb = all(any(has(b, e) for b in boxed) for e in exp)
        report(okf and okb, f"{tag} Q{i}: {', '.join(exp)}  (finalAnswer {'ok' if okf else 'MISMATCH ' + q['finalAnswer']}; boxed {'ok' if okb else 'MISMATCH ' + str(boxed)})")
        if i < len(qs):
            report(all(has(q.get("selfCheck", ""), e) for e in exp), f"{tag} Q{i}: self-check bracket shows {', '.join(exp)}")
        else:
            report(not q.get("selfCheck"), f"{tag} Q{i}: last question has no self-check")
        text = flat(q["steps"])
        bad = [p for p in (r"v_\{0\}", r"v_\{y0\}", r"vy0", r"v_\{ix\}", r"v_\{y\}", r"v_\{o", r"t\s*=\s*√\(2") if re.search(p, text)]
        report(not bad, f"{tag} Q{i}: key uses v_i / v_f notation" + (f"  found {bad}" if bad else ""))
    groups = sec["equationGroups"]
    eqs = [e for grp in groups for e in grp["eqs"]]
    alltext = " ".join(eqs)
    labels = {grp["label"]: grp for grp in groups}
    report("v_{fy}" in alltext and "v_{iy}" in alltext, f"{tag}: equations use v_i and v_f (v_iy, v_fy)")
    report(not re.search(r"v_0|v_o|\bv_\{0|\bvo\b", alltext), f"{tag}: no v_0 or v_o in the equations")
    report(not any(re.match(r"\s*t\s*=\s*√", e) for e in eqs), f"{tag}: no equation solved for time by square root")
    report(" / " not in alltext and "/" not in re.sub(r"m/s", "", alltext), f"{tag}: no slash division in the equations (stacked fractions)")
    ygrp, xgrp = labels.get("Vertical (y)"), labels.get("Horizontal (x)")
    report(ygrp is not None and xgrp is not None and "y only" in ygrp["note"], f"{tag}: the y group and the x group are labelled, with the y-only note")
    yset = ygrp["eqs"] if ygrp else []
    report(any(e.startswith("v_{fy} = v_{iy}") for e in yset) and any("[1|2] a_{y} t^2" in e for e in yset)
           and any(e.startswith("v_{fy}^2") for e in yset) and any("(v_{iy} + v_{fy})" in e for e in yset),
           f"{tag}: all four kinematic equations are given, written for y")
    report(all(("Δx" not in e and "v_{ix}" not in e and "a_{x}" not in e) for e in yset), f"{tag}: nothing in the y group uses x")
    report((xgrp["eqs"] if xgrp else []) == ["v_{x} = [Δx|t]"], f"{tag}: the x group is exactly v_x = Δx / t")
    others = [e for grp in groups if grp["label"] != "Horizontal (x)" for e in grp["eqs"] if "Δx" in e]
    report(not others, f"{tag}: no other equation uses Δx")
    vis = sec["directions"] + " ".join(q["prompt"] + " ".join(q.get("parts", [])) for q in qs)
    badg = sorted({c for c in vis if c in "θΔ₀₁₂₃₄₅₆₇₈₉"})
    report(not badg, f"{tag}: directions and prompts free of unsupported glyphs" + (f" found {badg}" if badg else ""))
    report(len(sec["directions"]) <= 260, f"{tag}: directions are short ({len(sec['directions'])} characters)")
    for i, q in enumerate(qs, start=1):
        lines = [s["row"][0] for s in q["steps"] if "row" in s and str(s["row"][0]).startswith("same direction:")]
        if lines:
            boxed_ang = [s["value"] for s in q["steps"] if "answer" in s and s["answer"][0].startswith("θ")][-1]
            m = re.match(r"(\d+)° (above|below) horizontal", boxed_ang)
            ref = float(m.group(1)) * (1 if m.group(2) == "above" else -1)
            forms = lines[0].split(":", 1)[1].split("=")
            ok = all(abs(((ang_of(f) - ref + 180) % 360) - 180) < 1e-9 for f in forms)
            report(ok, f"{tag} Q{i}: {len(forms)} equivalent forms match {boxed_ang}")
sys.exit(1 if fail else 0)
