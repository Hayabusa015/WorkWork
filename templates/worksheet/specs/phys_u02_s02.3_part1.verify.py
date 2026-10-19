"""Independent numeric check for phys_u02_s02.3_part1.json (run by phys_u02_s02.3_part1.build.sh).
Exit 1 on any mismatch.

Every answer is recomputed from the givens in the problem text with plain math, rounded to two
significant figures (g = 9.8 m/s² has two), and must appear in:
  - the student self-check bracket (every question but the last, SHULL-CHG-0021),
  - the typed finalAnswer, and
  - a boxed answer in the handwritten key steps.
Also checks the ramp, self-check placement, and that no glyph Archivo cannot set (theta, Delta,
subscript digits) or stray bold markup reaches the student page.
Sign convention: up is +y, launch direction is +x, g = -9.8 m/s². Horizontal launch: vy0 = 0."""
import json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(HERE, "phys_u02_s02.3_part1.json")
G = 9.8
RAMP = {"warm-up": 3, "practice": 3, "challenge": 1, "multi-topic": 1}   # must match build.sh
TIERS = ("warm-up", "practice", "challenge", "multi-topic")
BAD_GLYPHS = "θΔ₀₁₂₃₄₅₆₇₈₉"


def sf(x, n=2):
    """x rounded to n significant figures, as printed (trailing zeros kept: 0.60, 3.0)."""
    d = n - 1 - math.floor(math.log10(abs(x)))
    r = round(x, d)
    d2 = n - 1 - math.floor(math.log10(abs(r)))
    if d2 < d:                      # rounding carried into a new digit, e.g. 9.96 -> 10
        d, r = d2, round(x, d2)
    return f"{r:.{max(d, 0)}f}"


def has(text, token):
    return re.search(r"(?<![\d.])" + re.escape(token) + r"(?![\w/])", text or "") is not None


def fall_time(h):
    """Time to fall h metres from vy0 = 0: h = ½ g t²."""
    return math.sqrt(2 * h / G)


# ---------------------------------------------------------------- recompute from the givens
cases = {}

t = fall_time(45); x = 12 * t                                   # Q1 Mario: 45 m cliff, 12 m/s
cases[1] = ("Mario shell", [f"{sf(t)} s", f"{sf(x)} m"], f"t={t:.4f} x={x:.4f}")

h = 0.5 * G * 0.80 ** 2; x = 3.5 * 0.80                         # Q2 Patrick: 3.5 m/s, 0.80 s
cases[2] = ("Patrick pier", [f"{sf(h)} m", f"{sf(x)} m"], f"h={h:.4f} x={x:.4f}")

t = fall_time(78); x = 22 * t                                   # Q3 Minion: 22 m/s, 78 m
cases[3] = ("Minion banana", [f"{sf(t)} s", f"{sf(x)} m"], f"t={t:.4f} x={x:.4f}")

t = 1.2 / 2.0; h = 0.5 * G * t ** 2                             # Q4 Buzz: 2.0 m/s, lands 1.2 m out
cases[4] = ("Buzz bookshelf", [f"{sf(t)} s", f"{sf(h)} m"], f"t={t:.4f} h={h:.4f}")

t = fall_time(22); v = 61 / t                                   # Q5 Sonic: 22 m ledge, 61 m out
cases[5] = ("Sonic ledge", [f"{sf(t)} s", f"{sf(v)} m/s"], f"t={t:.4f} v={v:.4f}")

v = 7.7 / 0.55; h = 0.5 * G * 0.55 ** 2                         # Q6 Bumblebee: 7.7 m in 0.55 s
cases[6] = ("Bumblebee dock", [f"{sf(v)} m/s", f"{sf(h)} m"], f"v={v:.4f} h={h:.4f}")

t = fall_time(2.0); x = 7.5 * t; vmin = 5.0 / t                 # Q7 Coyote: 7.5 m/s, gap 5.0 m, drop 2.0 m
cases[7] = ("Coyote canyon", [f"{sf(t)} s", f"{sf(x)} m", f"{sf(vmin)} m/s"],
            f"t={t:.4f} x={x:.4f} vmin={vmin:.4f}")
coyote_short = x < 5.0

v = math.sqrt(2 * 3.5 * 18); t = fall_time(7.2); x = v * t      # Q8 McQueen: a 3.5, 18 m, 7.2 m drop
cases[8] = ("McQueen stunt", [f"{sf(v)} m/s", f"{sf(t)} s", f"{sf(x)} m"],
            f"v={v:.4f} t={t:.4f} x={x:.4f}")

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

report(coyote_short, "Q7 Coyote falls short of the 5.0 m ledge (key says he does)")

# structure: ramp, order, self-check placement, key fields
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

# glyphs on the student page
visible = [sec["title"], sec["concept"]["summary"], sec["directions"]]
visible += sec["concept"].get("keyIdeas", []) + sec["priorKnowledge"]["items"]
for e in sec["equations"]:
    visible += [e.get("note", ""), e.get("plain", "")]
for q in qs:
    visible += [q["prompt"], q.get("selfCheck", "")] + q.get("parts", [])
bad = sorted({c for s in visible for c in s if c in BAD_GLYPHS})
report(not bad, f"student page free of {BAD_GLYPHS!r}" + (f"  found {bad}" if bad else ""))
report(not any("**" in s for s in visible), "no ** markup on the student page")

sys.exit(1 if fail else 0)
