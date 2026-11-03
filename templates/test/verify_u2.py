#!/usr/bin/env python3
"""Independent re-solve of every Unit 2 test number, by a different method than u2_data.py.

Vectors by complex numbers; projectiles by stepping the motion forward in time (no formula for t).
Exits non-zero on any disagreement.
    python3 templates/test/verify_u2.py
"""
import cmath, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u2_data as D
import vectors_22 as V

bad = 0


def check(label, a, b, tol):
    global bad
    ok = abs(a - b) <= tol
    bad += not ok
    if not ok:
        print("MISMATCH", label, a, b)


def simulate(y0, vx, vy, dt=1e-5):
    x, y, t = 0.0, y0, 0.0
    while True:
        vy_new = vy - 9.8 * dt
        y_new = y + 0.5 * (vy + vy_new) * dt
        if y_new <= 0 and t > 0:
            f = y / (y - y_new)
            return t + f * dt, x + vx * f * dt, vy_new
        x += vx * dt; y, vy, t = y_new, vy_new, t + dt


def z(mag, deg):
    return cmath.rect(mag, math.radians(deg))


for L in D.VERS:
    w, s = D.WRITTEN[L], D.solve_written(L)
    q1 = w["q1"]; zz = complex(q1["x"], q1["y"])
    check(L + "q1 R", abs(zz), s["q1"]["R"], 1e-9); check(L + "q1 th", math.degrees(cmath.phase(zz)) % 360, s["q1"]["th"], 1e-9)
    tot = sum(z(m, V.theta_from(*sp)) for m, sp in w["q2"]["v"])
    check(L + "q2 R", abs(tot), s["q2"]["R"], 1e-9); check(L + "q2 th", math.degrees(cmath.phase(tot)) % 360, s["q2"]["th"], 1e-9)
    t, x, _ = simulate(w["q3"]["h"], w["q3"]["vx"], 0)
    check(L + "q3 t", t, s["q3"]["t"], 2e-4); check(L + "q3 x", x, s["q3"]["x"], 2e-3)
    q4 = w["q4"]; vx, vy = q4["v"] * math.cos(math.radians(q4["ang"])), q4["v"] * math.sin(math.radians(q4["ang"]))
    t, x, _ = simulate(1e-12, vx, vy)
    check(L + "q4 t", t, s["q4"]["t"], 2e-4); check(L + "q4 R", x, s["q4"]["R"], 2e-3)
    q5 = w["q5"]; vx, vy = q5["v"] * math.cos(math.radians(q5["ang"])), q5["v"] * math.sin(math.radians(q5["ang"]))
    t, x, _ = simulate(q5["y0"], vx, vy)
    check(L + "q5 t", t, s["q5"]["t"], 2e-4); check(L + "q5 x", x, s["q5"]["x"], 2e-3)
    check(L + "q5 vx", vx, s["q5"]["vx"], 1e-9); check(L + "q5 vy", vy, s["q5"]["vy"], 1e-9)

g, s = D.GUIDE, D.solve_guide()
zz = complex(g["p1"]["x"], g["p1"]["y"])
check("p1 R", abs(zz), s["p1"]["R"], 1e-9); check("p1 th", math.degrees(cmath.phase(zz)) % 360, s["p1"]["th"], 1e-9)
tot = sum(z(m, V.theta_from(*sp)) for m, sp in g["p2"]["v"])
check("p2 R", abs(tot), s["p2"]["R"], 1e-9); check("p2 th", math.degrees(cmath.phase(tot)) % 360, s["p2"]["th"], 1e-9)
t, x, _ = simulate(g["p3"]["h"], g["p3"]["vx"], 0)
check("p3 t", t, s["p3"]["t"], 2e-4); check("p3 x", x, s["p3"]["x"], 2e-3)
for k in ("p4", "p5"):
    a = g[k]; vx, vy = a["v"] * math.cos(math.radians(a["ang"])), a["v"] * math.sin(math.radians(a["ang"]))
    t, x, _ = simulate(a.get("y0", 1e-12), vx, vy)
    check(k + " t", t, s[k]["t"], 2e-4); check(k + " x", x, s[k].get("x", s[k].get("R")), 2e-3)

# multiple-choice calculation items: correct text vs an independent number, per version
EXPECT = {   # base index -> [A, B, C] expected correct answer text
    1: ["150°", "320°", "205°"], 2: ["320°", "235°", "160°"],
    3: ["35° south of west", "55° north of west", "50° south of east"],
    7: ["10 km", "13 m", "17 m/s"], 8: ["53° north of east", "23° south of west", "62° south of east"],
    9: ["4 m/s east", "150 km/h north", "1.5 m/s west"],
    11: ["43 m/s", "73 km/h", "6.0 m/s"], 13: ["7 m", "−11 m", "−3 m"],
    21: ["2.0 s", "3.0 s", "4.0 s"], 22: ["2.4 m", "4.8 m", "3.0 m"],
    23: ["10 m/s", "19 m/s", "13 m/s"], 24: ["3.0 s", "5.0 s", "2.0 s"], 25: ["60°", "70°", "65°"],
    27: ["10 m/s", "26 m/s", "14 m/s"], 29: ["4.9 m/s upward", "9.8 m/s downward", "14.7 m/s downward"],
}
for L in D.VERS:
    for q in D.build_mc(L):
        if q["base"] in EXPECT:
            got = q["choices"][q["answer"]][0]
            want = EXPECT[q["base"]][D.VERS.index(L)]
            if got != want:
                bad += 1; print("MC MISMATCH", L, q["base"], got, want)
print("verify_u2:", "FAIL" if bad else "all numbers agree")
sys.exit(1 if bad else 0)
