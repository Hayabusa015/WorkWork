"""Independent numeric check for phys_u02_s02.3_part3.json (run by phys_u02_s02.3_part3.build.sh).
Exit 1 on any mismatch.

Every answer is recomputed from the givens in the problem text with plain math, rounded to two
significant figures (g = 9.8 m/s² has two), and must appear in:
  - the student self-check bracket (every question but the last, SHULL-CHG-0021),
  - the typed finalAnswer, and
  - a boxed answer in the handwritten key steps.
Also checks the ramp, self-check placement, and that no glyph Archivo cannot set (theta, Delta,
subscript digits) or stray bold markup reaches the student page.
Sign convention: up is +y, launch direction is +x, g = -9.8 m/s². y is the landing height measured
from the launch point."""
import json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(HERE, "phys_u02_s02.3_part3.json")
G = 9.8
RAMP = {"warm-up": 1, "practice": 2, "challenge": 1, "multi-topic": 1}   # must match build.sh
TIERS = ("warm-up", "practice", "challenge", "multi-topic")
BAD_GLYPHS = "θΔ₀₁₂₃₄₅₆₇₈₉"


def sf(x, n=2):
    """x rounded to n significant figures, as printed (trailing zeros kept: 0.60, 3.0)."""
    d = n - 1 - math.floor(math.log10(abs(x)))
    r = round(x, d)
    d2 = n - 1 - math.floor(math.log10(abs(r)))
    if d2 < d:
        d, r = d2, round(x, d2)
    return f"{r:.{max(d, 0)}f}"


def has(text, token):
    return re.search(r"(?<![\d.])" + re.escape(token) + r"(?![\w/])", text or "") is not None


def comps(v, deg):
    a = math.radians(deg)
    return v * math.cos(a), v * math.sin(a)


def times_at(vy0, y):
    """Both roots of y = vy0 t - ½ g t², smaller first."""
    disc = vy0 ** 2 - 2 * G * y
    assert disc >= 0, "never reaches that height"
    r = math.sqrt(disc)
    return (vy0 - r) / G, (vy0 + r) / G


# ---------------------------------------------------------------- recompute from the givens
cases, checks = {}, []

vx, vy = comps(22, 25); t0, t = times_at(vy, -18); x = vx * t    # Q1 Sparrow: 22 m/s, 25°, 18 m cliff
cases[1] = ("Sparrow cannon", [f"{sf(t)} s", f"{sf(x)} m"], f"roots={t0:.4f},{t:.4f} x={x:.4f}")
checks.append((t0 < 0, "Q1 the discarded root is negative"))

vx, vy = comps(45, 10); t = 62 / vx; y = vy * t - 0.5 * G * t ** 2   # Q2 Link: 45 m/s, 10°, 62 m
cases[2] = ("Link arrow", [f"{sf(t)} s", f"{sf(y)} m"], f"t={t:.4f} y={y:.4f}")
checks.append((y > 0, "Q2 the arrow hits above the launch height (key says above)"))

vx, vy = comps(14, 60); t_up, t = times_at(vy, 6.0); x = vx * t    # Q3 Michelangelo: 14 m/s, 60°, roof +6.0 m
cases[3] = ("Michelangelo pizza", [f"{sf(t)} s", f"{sf(x)} m"], f"roots={t_up:.4f},{t:.4f} x={x:.4f}")
checks.append((t_up > 0 and vy - G * t < 0, "Q3 both roots positive; the kept root is on the way down"))

vx, vy = comps(28, 40)                                            # Q4 Shrek: 28 m/s, 40°, 15 m wall
H = 15 + vy ** 2 / (2 * G); t0, t = times_at(vy, -15); x = vx * t
cases[4] = ("Shrek trebuchet", [f"{sf(H)} m", f"{sf(t)} s", f"{sf(x)} m"],
            f"ymax={H:.4f} roots={t0:.4f},{t:.4f} x={x:.4f}")
checks.append((t0 < 0, "Q4 the discarded root is negative"))

vx, vy = comps(18, -20); t0, t = times_at(vy, -35); x = vx * t    # Q5 Ash: 18 m/s, 20° below, 35 m
vy_end = vy - G * t; v = math.hypot(vx, vy_end); ang = math.degrees(math.atan(abs(vy_end) / vx))
cases[5] = ("Ash Poke Ball", [f"{sf(t)} s", f"{sf(x)} m", f"{sf(v)} m/s", f"{round(ang)}°"],
            f"vy0={vy:.4f} t={t:.4f} x={x:.4f} vy={vy_end:.4f} v={v:.4f} angle={ang:.3f}")
checks.append((t0 < 0, "Q5 the discarded root is negative"))
checks.append((abs(v ** 2 - (18 ** 2 + 2 * G * 35)) < 1e-6, "Q5 impact speed agrees with vy² = vy0² + 2gy"))

# ---------------------------------------------------------------- compare with the spec
spec = json.load(open(SPEC, encoding="utf-8"))
sec = spec["sectionsContent"][0]
qs = sec["questions"]
fail = 0


def report(ok, msg):
    global fail
    fail += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {msg}")


report(len(qs) == len(cases), f"question count {len(qs)} (expected {len(cases)})")
for n, (label, tokens, raw) in cases.items():
    q = qs[n - 1]
    last = n == len(qs)
    boxed = " | ".join(str(s.get("value", "")) for s in q.get("steps", []) if "answer" in s)
    miss = []
    for tok in tokens:
        if not last and not has(q.get("selfCheck"), tok):
            miss.append(f"selfCheck lacks {tok!r}")
        if not has(q.get("finalAnswer"), tok):
            miss.append(f"finalAnswer lacks {tok!r}")
        if not has(boxed, tok):
            miss.append(f"key box lacks {tok!r}")
    report(not miss, f"Q{n} {label}: {raw}  -> {', '.join(tokens)}" + ("  " + "; ".join(miss) if miss else ""))
for ok, msg in checks:
    report(ok, msg)
report("above" in qs[1]["selfCheck"] and "above" in qs[1]["finalAnswer"], "Q2 sheet and key say 'above'")
report("below" in qs[4]["finalAnswer"], "Q5 key gives the impact direction as below the horizontal")

shape = {}
for q in qs:
    shape[q.get("tier")] = shape.get(q.get("tier"), 0) + 1
report(shape == RAMP, f"ramp {shape} == {RAMP}")
order = [TIERS.index(q["tier"]) for q in qs]
report(order == sorted(order) and qs[-1]["tier"] == "multi-topic", "tiers never go backwards; last is multi-topic")
for n, q in enumerate(qs, 1):
    last = n == len(qs)
    if last:
        report(not q.get("selfCheck"), f"Q{n} (last) carries no self-check")
    else:
        report(bool(q.get("selfCheck")), f"Q{n} carries a self-check")
    report(bool(q.get("solution")) and bool(q.get("steps")), f"Q{n} has solution and steps")

visible = [sec["title"], sec["concept"]["summary"], sec["directions"]]
visible += sec["concept"].get("keyIdeas", []) + sec["priorKnowledge"]["items"]
for e in sec["equations"]:
    visible += [e.get("note", ""), e.get("plain", "")]
for q in qs:
    visible += [q["prompt"], q.get("selfCheck", "")] + q.get("parts", [])
bad = sorted({c for s in visible for c in s if c in BAD_GLYPHS})
report(not bad, f"student page free of {BAD_GLYPHS!r}" + (f"  found {bad}" if bad else ""))
report(not any("**" in s for s in visible), "no ** markup on the student page")

import os
SPEC_PATH = SPEC

# Matt 2026-10-20: every boxed direction carries a "same direction:" line listing its other forms.
# Independent check: turn each listed form into a unit vector and confirm all point the same way
# as the boxed answer, to within half a degree (the answers are rounded to whole degrees).
def _dir_check():
    import json as _j, math as _m, re as _re
    _spec = _j.load(open(SPEC_PATH, encoding="utf-8"))
    AX = {"east": 0, "north": 90, "west": 180, "south": 270}
    def ang(form, ref):
        form = form.strip().replace("−", "-")
        m = _re.fullmatch(r"(-?[\d.]+)°", form)
        if m: return float(m.group(1))
        m = _re.fullmatch(r"([\d.]+)° (\w+) of (\w+)", form)
        if m:
            d, to, frm = float(m.group(1)), AX[m.group(2)], AX[m.group(3)]
            turn = ((to - frm + 180) % 360) - 180          # +90 or -90: which way "toward" is
            return frm + d * (1 if turn > 0 else -1)
        m = _re.fullmatch(r"due (\w+)", form)
        if m: return AX[m.group(1)]
        m = _re.fullmatch(r"([\d.]+)° from straight (up|down)", form)
        if m: return (90 - float(m.group(1))) if m.group(2) == "up" else (-90 + float(m.group(1)))
        raise ValueError(form)
    def boxed(v):
        v = v.split(" at ")[-1]
        m = _re.match(r"([\d.]+)° (above|below) horizontal", v)
        if m: return float(m.group(1)) * (1 if m.group(2) == "above" else -1)
        return float(v.rstrip("°"))
    n = bad = 0
    for qi, q in enumerate(_spec["sectionsContent"][0]["questions"], 1):
        last = None
        for st in q["steps"]:
            if "answer" in st: last = st
            r = st.get("row", [""])[0]
            if isinstance(r, str) and r.startswith("same direction:"):
                ref = boxed(last["value"])
                for form in r.split(":", 1)[1].split("="):
                    a = ang(form, ref); n += 1
                    dev = abs(((a - ref + 180) % 360) - 180)
                    if dev > 0.5:
                        bad += 1; print(f"FAIL  Q{qi} '{form.strip()}' is {a}°, boxed answer is {ref}°")
    print(f"{'PASS' if not bad else 'FAIL'}  {n} equivalent-direction forms all match their boxed answers")
    return bad

fail += _dir_check()
sys.exit(1 if fail else 0)
