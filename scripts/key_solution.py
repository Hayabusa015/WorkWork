"""Draw one question's worked solution in the key-handwriting face (SHULL-CHG-0043 Stage 2).

    from key_solution import solution_image
    solution_image(question_dict, "q3.png", width_in=7.2)

A question opts in by carrying "steps" (and, for a physics story problem, "sketch"). The
builder embeds the PNG; a question without "steps" keeps its typed solution.

    "steps": [
      {"row": ["v = v_{0} + at"], "note": "subtract v_{0} from both sides"},
      {"row": ["a =", {"frac": ["v − v_{0}", "t"]}]},
      {"mistake": ["a =", {"frac": ["30 − 10", "4"]}, "= 5 m/s^{2}"], "note": "final minus initial, not the reverse"},
      {"answer": ["a ="], "value": "−5 m/s^{2}"},
      {"say": "The average-velocity equation needs no acceleration.", "ink": "pen"},
      {"label": "Phase 1"}
    ]

Math rows are pencil, written answers ("say") pen, notes and vectors arrow, final answers and the
unknown box. Division is only ever a {"frac": [...]} item. A unit's own slash (m/s) stays inline.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from key_ink import Page

LOGICAL_PER_IN = 150          # Page draws at 150 logical px per inch and saves at 2x: 300 dpi


def _items(row):
    out = []
    for it in row:
        if isinstance(it, str):
            out.append(it)
        elif "frac" in it:
            out.append(("frac", it["frac"][0], it["frac"][1]))
        elif "sqrt" in it:
            out.append(("sqrt", it["sqrt"]))
        elif "ink" in it:
            out.append((it["ink"], it["text"]))
        else:
            raise ValueError(f"unknown step item {it!r}")
    return out


def _has_frac(items):
    return any(isinstance(i, tuple) and i[0] == "frac" for i in items)


def _wrap(P, text, size, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if cur and P.width(t, size) > width:
            lines.append(cur); cur = w
        else:
            cur = t
    return lines + ([cur] if cur else [])


def draw_steps(P, x0, y, steps, width, size):
    for st in steps:
        if "label" in st:
            P.text(x0, y, st["label"], size * 0.8, "pen")
            y += size * 1.35
            continue
        if "say" in st:
            for line in _wrap(P, st["say"], size * 0.92, width - 20):
                P.text(x0, y, line, size * 0.92, st.get("ink", "pen"))
                y += size * 1.45
            y += size * 0.25
            continue
        kind = "answer" if "answer" in st else "mistake" if "mistake" in st else "row"
        items = _items(st[kind])
        tall = _has_frac(items)
        ry = y + (size * 0.75 if tall else 0)          # fractions need room above the text line
        end = P.row(x0, ry, items, size, st.get("ink", "pencil"))
        if kind == "answer":
            end = P.answer(end, ry, st["value"], size, st.get("ink", "pencil"))
        if kind == "mistake":
            P.strike(x0, end - 6, ry + size * 0.55, "pencil")
        h = size * (2.9 if tall else 1.75)
        if st.get("note"):
            ns = size * 0.8
            if end + 34 + P.width(st["note"], ns) < x0 + width:
                P.text(end + 34, ry + size * 0.12, st["note"], ns, "arrow")
            else:
                P.text(x0 + 40, y + h - size * 0.25, st["note"], ns, "arrow")
                h += size * 1.25
        y += h
    return y


def _label(P, x, y, s, size, unknown=False):
    return P.text(x, y, s, size, "box" if unknown else "pencil")


def linear_scene(P, x0, y0, width, sc):
    """Objects moving along a line: start and end positions, velocity vectors, acceleration,
    and time / distance brackets, labelled from the problem's own givens."""
    sk = P.sketch()
    fs = 22
    unk = lambda v: str(v).strip() == "?"
    find = sc.get("find")
    y = y0
    if find:
        fw = P.width("find: " + find, 26) + 34
        P.box(x0 + width - fw - 10, y, x0 + width - 10, y + 50)
        P.text(x0 + width - fw + 6, y + 8, "find: " + find, 26, "box")
    y += 58
    lanes = sc.get("lanes", [])
    bw, bh = 170, 46
    xs0 = x0 + 30
    xe = x0 + width - 60 - bw
    starts = []
    for li, ln in enumerate(lanes):
        gy = y + 150
        sx = xs0 + (int(ln.get("offset_px", 0)) if ln.get("offset") else 0)
        starts.append((sx, gy))
        if sc.get("ground", True):
            sk.seg((x0, gy + 8), (x0 + width, gy + 8), w=2.0, alpha=140)
            for i in range(int(width / 24)):
                hx = x0 + 10 + i * 24
                sk.seg((hx, gy + 12), (hx - 9, gy + 25), w=1.1, alpha=85, passes=1, amp=.4)
        for bx in (sx, xe):
            sk.rect(bx, gy - bh - 6, bx + bw, gy - 6)
            P.text(bx + 10, gy - bh + 4, ln.get("name", ""), fs, "pencil")
        sk.dashed((sx + bw + 6, gy - 29), (xe - 6, gy - 29))
        v0 = ln.get("v0")
        if v0 is not None:
            if str(v0).startswith("0"):
                _label(P, sx, gy - bh - 46, "v_{0} = 0 (rest)", fs)
            else:
                sk.vector((sx, gy - bh - 18), (sx + 120, gy - bh - 18))
                _label(P, sx, gy - bh - 56, f"v_{{0}} = {v0}", fs, unk(v0))
        v = ln.get("v")
        if v is not None:
            sk.vector((xe, gy - bh - 18), (xe + (150 if not unk(v) else 120), gy - bh - 18))
            _label(P, xe, gy - bh - 56, f"v = {v}", fs, unk(v))
        a = ln.get("a")
        if a is not None:
            mx = (sx + bw + xe) / 2 - 60
            if str(a).strip() == "0":                 # no vector for zero acceleration
                _label(P, mx, gy - bh - 40, "a = 0 (constant v)", fs)
            else:
                d = -1 if ln.get("a_dir", 1) < 0 else 1
                ax0, ax1 = (mx, mx + 70) if d > 0 else (mx + 70, mx)
                sk.vector((ax0, gy - bh - 24), (ax1, gy - bh - 24))
                _label(P, mx - 10, gy - bh - 62, f"a = {a}", fs, unk(a))
        if ln.get("offset") and li > 0:               # head start: bracket under the ground, clear of labels
            px, py = starts[0][0], gy + 42
            sk.seg((px, py), (sx, py), "arrow", w=1.6, alpha=170, passes=1)
            sk.seg((px, py - 10), (px, py + 10), "arrow", w=1.6, alpha=170, passes=1)
            sk.seg((sx, py - 10), (sx, py + 10), "arrow", w=1.6, alpha=170, passes=1)
            _label(P, px + 6, py + 8, f"head start {ln['offset']}", fs - 2)
            gy += 46
        y = gy + 34
    for key, lab in (("t", "t"), ("dx", "Δx")):
        if sc.get(key) is None:
            continue
        val = sc[key]
        sk.seg((xs0, y + 14), (xe + bw, y + 14), "arrow", w=1.7, alpha=170)
        for bx in (xs0, xe + bw):
            sk.seg((bx, y + 2), (bx, y + 26), "arrow", w=1.7, alpha=170, passes=1)
        _label(P, (xs0 + xe + bw) / 2 - 50, y + 22, f"{lab} = {val}", fs + 2, unk(val))
        y += 64
    sk.commit()
    return y


SCENES = {"linear": linear_scene}


def solution_image(q, out_png, width_in=7.2, size=27):
    W = int(width_in * LOGICAL_PER_IN)
    P = Page(W, 3200, seed=hash(q.get("prompt", "")) % 1000)
    y = 8
    if q.get("sketch"):
        sc = q["sketch"]
        y = SCENES[sc.get("scene", "linear")](P, 10, y, W - 20, sc) + 16
    y = draw_steps(P, 14, y, q["steps"], W - 28, size)
    P.crop(y + 10)
    P.save(png=out_png)
    return out_png, (y + 10) / LOGICAL_PER_IN      # height in inches
