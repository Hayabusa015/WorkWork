"""Independent numeric check for phys_u02_s02.2.json (run by phys_u02_s02.2.build.sh). Exit 1 on any mismatch.
Angles: counterclockwise from +x (east), reported 0-360."""
import math, sys

def resultant(vecs):
    rx = sum(m * math.cos(math.radians(a)) for m, a in vecs)
    ry = sum(m * math.sin(math.radians(a)) for m, a in vecs)
    return rx, ry, math.hypot(rx, ry), math.degrees(math.atan2(ry, rx)) % 360

# (label, vectors, expected magnitude as printed, magnitude decimals, expected angle deg)
CASES = [
    ("Q1 velocity",     [(6.0, 0), (2.5, 270)],                  6.5,  1, 337),
    ("Q2 force",        [(840, 90), (350, 180)],                 910,  0, 113),
    ("Q3 acceleration", [(4.5, 270), (2.0, 180)],                4.9,  1, 246),
    ("Q4 displacement", [(20.0, 35), (9.0, 27)],                 29,   0, 33),
    ("Q5 displacement", [(45, 120), (30, 200)],                  58,   0, 150),
    ("Q6 displacement", [(65, 300), (40, 35)],                   73,   0, 333),
    ("Q7 displacement", [(2.5, 60), (4.0, 150), (1.5, 250)],     3.9,  1, 135),
    ("Q8a force",       [(150, 20), (210, 135), (180, 255)],     60.0, 1, 154),
]
fail = 0
for label, vecs, mag, dec, ang in CASES:
    rx, ry, r, th = resultant(vecs)
    ok = round(r, dec) == mag and round(th) % 360 == ang
    fail += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {label}: Rx={rx:.4f} Ry={ry:.4f} R={r:.4f} theta={th:.3f}"
          f"  (sheet: {mag} at {ang} deg)")
# Q8b: the opposite of the Q8a resultant
rx, ry, r, th = resultant(CASES[-1][1])
th_b = (th + 180) % 360
ok = round(r, 1) == 60.0 and round(th_b) == 334
fail += not ok
print(f"{'PASS' if ok else 'FAIL'}  Q8b Megatron: R={r:.4f} theta={th_b:.3f}  (sheet: 60.0 N at 334 deg)")
import os
SPEC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phys_u02_s02.2.json")

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
