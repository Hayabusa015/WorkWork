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

Key images (SHULL-CHG-0071). An item may instead (or also) carry "keyImage": a scene object,
{"scene": "<name>", ...}, drawn by SCENES[name]. "sketch" takes the same object. With "steps" the
steps are drawn below the image; without them the image stands alone. The typed "solution" stays
mandatory: it is what verify-content checks the drawing against, and it is what the key prints if
a scene raises SceneUnsupported. The "linear" scene's fields are read in linear_scene() below.

The "fbd" scene: a free-body diagram. Object as a box or a dot, one arrow per force, each arrow
starting at the object, labelled from the spec, its length scaled to "mag" (relative; the largest
force in the item gets the full arrow). Lines, the object and labels are pencil; force arrows
are vectors and keep the arrow ink (standards/ANSWER_KEYS.md §2, §6).

    "keyImage": {"scene": "fbd",
      "panels": [                                  # one per object, drawn side by side, one scale
        {"caption": "Block",                       # optional, written under the panel
         "object": "box",                          # "box" (default) or "dot"
         "name": "block",                          # optional, written inside the box
         "tiltDeg": 0,                             # box rotation, e.g. 25 on a 25 degree ramp
         "surface": false,                         # dashed line along the box's base (ramp, floor)
         "forces": [
           {"label": "F_{N}", "dir": "up", "mag": 1.0},
           {"label": "F_{g}", "dir": 270, "mag": 1.0, "offset": 0.0}
         ]}
      ]}

"dir" is "up" / "down" / "left" / "right" or degrees counter-clockwise from the +x axis (right).
"offset" (-0.45 to 0.45, a fraction of the box side) slides an arrow's tail sideways so two
parallel arrows do not sit on top of each other. A single-object diagram may give "forces" (and
the other panel keys) at the top level instead of "panels". A force labelled or named as motion,
velocity, speed or acceleration is refused (MotionArrowError): an FBD has no arrow for motion
(courses/physics/DECISIONS.md, free-body diagrams).
"""
import math, os, re, sys
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


class SceneUnsupported(Exception):
    """The scene cannot model this item. The key prints the typed solution instead
    (standards/ANSWER_KEYS.md §6.3 as amended by SHULL-CHG-0071): no sketch beats a wrong one."""


class MotionArrowError(ValueError):
    """An FBD force labelled as motion. Refused outright, never quietly dropped."""


_DIRS = {"right": 0.0, "up": 90.0, "left": 180.0, "down": 270.0}
# Whole-word names for motion. "v" and "a" alone are velocity and acceleration; F_{app} is not.
_MOTION = re.compile(r"^\s*(v|a|ma|v_\{?\w*\}?|a_\{?\w*\}?)\s*$|\b(motion|velocity|speed|accel\w*|moving)\b",
                     re.I)


def fbd_forces(sc):
    """Panels of an fbd scene, each with its forces checked. Raises MotionArrowError or
    SceneUnsupported; returns the panel list."""
    panels = sc.get("panels") or [sc]
    if not panels or any(not p.get("forces") for p in panels):
        raise SceneUnsupported("fbd scene with a panel that has no forces")
    for p in panels:
        if p.get("object", "box") not in ("box", "dot"):
            raise SceneUnsupported(f"fbd object {p.get('object')!r}: only box or dot")
        for f in p["forces"]:
            for field in (f.get("label", ""), f.get("name", "")):
                if field and _MOTION.search(str(field)):
                    raise MotionArrowError(
                        f"fbd force {field!r} names motion. A free-body diagram has no arrow for "
                        "motion: one arrow per force (courses/physics/DECISIONS.md).")
            if not f.get("label"):
                raise SceneUnsupported("fbd force with no label")
            d = f.get("dir")
            if isinstance(d, str):
                if d not in _DIRS:
                    raise SceneUnsupported(f"fbd direction {d!r}")
            elif not isinstance(d, (int, float)):
                raise SceneUnsupported(f"fbd direction {d!r}")
            if not isinstance(f.get("mag"), (int, float)) or f["mag"] <= 0:
                raise SceneUnsupported(f"fbd force {f['label']!r} needs a positive mag")
    return panels


def _deg(d):
    return _DIRS[d] if isinstance(d, str) else float(d)


def fbd_scene(P, x0, y0, width, sc):
    """A free-body diagram, one panel per object, every panel on one magnitude scale.

    Geometry is laid out first around a centre at y = 0, then the whole row is moved down so
    its tallest arrow or label clears the top - the image is only as tall as the diagram."""
    panels = fbd_forces(sc)
    fs = 30                                       # label size
    half = 34                                     # half the box side, logical px
    big = max(f["mag"] for p in panels for f in p["forces"])
    full = float(sc.get("arrowPx", 118))          # the largest force's arrow beyond the object
    unit = full / big
    pw = width / len(panels)
    lay, ys = [], [-half - 10, half + 10]
    for i, p in enumerate(panels):
        cx = x0 + pw * i + pw / 2
        tilt = math.radians(float(p.get("tiltDeg", 0)))
        ct, st_ = math.cos(tilt), math.sin(tilt)
        dot = p.get("object", "box") == "dot"
        arrows = []
        for f in p["forces"]:
            ang = math.radians(_deg(f["dir"]))
            dx, dy = math.cos(ang), -math.sin(ang)          # screen y runs down
            off = float(f.get("offset", 0)) * 2 * half
            px, py = -dy * off, dx * off                    # sideways shift, perpendicular to the arrow
            if dot:
                t = 7
            else:
                # Where the ray from the centre leaves the (rotated) box: the arrow starts there.
                lx, ly = dx * ct - dy * st_, dx * st_ + dy * ct
                lpx, lpy = px * ct - py * st_, px * st_ + py * ct
                ts = [(half - lpx) / lx if lx > 1e-9 else (-half - lpx) / lx if lx < -1e-9 else 1e9,
                      (half - lpy) / ly if ly > 1e-9 else (-half - lpy) / ly if ly < -1e-9 else 1e9]
                t = min(ts)
            sx, sy = px + dx * t, py + dy * t
            L = f["mag"] * unit
            ex, ey = sx + dx * L, sy + dy * L
            lab = str(f["label"])
            w, h = P.width(lab, fs), fs * 1.15
            if abs(dx) < 0.2:                        # vertical arrow: label beside the head,
                side = 1 if px >= 0 else -1          # on the side the arrow was shifted to
                gx, gy = ex + side * (w / 2 + 14), ey + dy * 6
            else:
                gx = ex + dx * (12 + abs(dx) * w / 2 + abs(dy) * h / 2)
                gy = ey + dy * (12 + abs(dy) * h / 2 + abs(dx) * w / 2)
            arrows.append((sx, sy, ex, ey, lab, gx - w / 2, gy - h / 2))
            ys += [ey, gy - h / 2 - 4, gy + h / 2 + 4]
        lay.append((p, cx, ct, st_, dot, arrows))
    cy = y0 + 8 - min(ys)
    bottom = cy + max(ys)
    cap_y = bottom + 10
    sk = P.sketch()
    P.arrows_drawn = getattr(P, "arrows_drawn", 0)
    P.labels_drawn = getattr(P, "labels_drawn", [])
    for p, cx, ct, st_, dot, arrows in lay:
        # Local box coordinates (y down) to the page, rotated counter-clockwise by the tilt.
        rot = lambda lx, ly: (cx + lx * ct + ly * st_, cy - lx * st_ + ly * ct)
        if dot:
            sk.circle(cx, cy, 7, w=2.4, alpha=200)
            sk.circle(cx, cy, 3, w=3.0, alpha=220)
        else:
            corners = [rot(-half, -half), rot(half, -half), rot(half, half), rot(-half, half)]
            for a, b in zip(corners, corners[1:] + corners[:1]):
                sk.seg(a, b, w=2.0, alpha=170)
            if p.get("surface"):
                sk.dashed(rot(-half - 70, half + 3), rot(half + 70, half + 3), n=22)
        for sx, sy, ex, ey, lab, lx, ly in arrows:
            sk.vector((cx + sx, cy + sy), (cx + ex, cy + ey))
            P.arrows_drawn += 1
        if p.get("name") and not dot:
            nw = P.width(p["name"], 18)
            P.text(cx - nw / 2, cy - 13, p["name"], 18, "pencil", jitter=0.3)
    sk.commit()
    for p, cx, ct, st_, dot, arrows in lay:     # labels over the strokes, never under them
        for sx, sy, ex, ey, lab, lx, ly in arrows:
            P.text(cx + lx, cy + ly, lab, fs, "pencil")
            P.labels_drawn.append(lab)
        if p.get("caption"):
            cw = P.width(p["caption"], 22)
            P.text(cx - cw / 2, cap_y, p["caption"], 22, "pencil")
    return cap_y + (34 if any(p.get("caption") for p in panels) else 0)


SCENES = {"linear": linear_scene, "fbd": fbd_scene}


def scene_of(q):
    """The scene object an item asks for: keyImage, or the older sketch field."""
    return q.get("keyImage") or q.get("sketch")


def solution_image(q, out_png, width_in=7.2, size=27):
    """Draw an item's scene (keyImage or sketch) and/or its steps. Raises SceneUnsupported if the
    scene cannot model the item, and MotionArrowError for an FBD with a motion arrow."""
    sc = scene_of(q)
    if sc is not None and sc.get("scene", "linear") not in SCENES:
        raise SceneUnsupported(f"no scene named {sc.get('scene')!r}")
    if sc is None and not q.get("steps"):
        raise SceneUnsupported("nothing to draw: no keyImage, sketch or steps")
    W = int(width_in * LOGICAL_PER_IN)
    P = Page(W, 3200, seed=hash(q.get("prompt", "")) % 1000)
    y = 8
    if sc is not None:
        y = SCENES[sc.get("scene", "linear")](P, 10, y, W - 20, sc) + 16
    if q.get("steps"):
        y = draw_steps(P, 14, y, q["steps"], W - 28, size)
    P.crop(y + 10)
    P.save(png=out_png)
    return out_png, (y + 10) / LOGICAL_PER_IN      # height in inches
