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
sys.exit(1 if fail else 0)
