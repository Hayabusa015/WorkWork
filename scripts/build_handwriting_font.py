#!/usr/bin/env python3
"""Build ShullHand, the key-handwriting font, from Matt's scanned handwriting sheet (SHULL-CHG-0044).

    python3 scripts/build_handwriting_font.py \\
        --scan brand/fonts/source/ShullHand-handwriting-sample-2026-10-16.pdf \\
        --page-order 4,1,2,3 --out brand/fonts/ShullHand

--page-order gives, for each page of the scan in order, which sheet page it is (the scanner
reordered them). Writes <out>.ttf and <out>_alts.json, and prints a build report.

Pipeline: rasterise at 300 dpi -> straighten each page on its four corner squares -> cut every box
by the layout in build_handwriting_sheet.py -> trace the ink -> place each glyph on its line ->
space it to his running writing -> write the TrueType file.

The spacing and width numbers below were fitted to his own sentences on sheet page 4, not
guessed: his running letters are ~17% narrower than his box letters, nearly touch, and his word
gap is measured from the same lines. Legibility still wins where they conflict (see PUNCT_LSB).

Needs: opencv-python-headless, potracer, numpy, fontTools, poppler (pdftoppm).
"""
import argparse, json, os, statistics, subprocess, sys, tempfile
import cv2, numpy as np, potrace
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.reverseContourPen import ReverseContourPen

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_handwriting_sheet import layout

DPI = 300
UPM, CAP = 1000, 700
VERSION = "Version 0.2"
INK_THRESH = 110           # scan grey below this is ink; the blue guide lines and labels sit above it
UP = 4                     # upsample before tracing, for smooth curves
LSB_DEFAULT = 4            # his letters nearly touch (fitted gap about -3 px); kept just positive so pairs never merge
PUNCT_LSB = 30             # . , : ; get room so 2.0 never reads as 20 (legibility beats the look)
H_SCALE = 0.83             # running letters are ~17% narrower than box letters (fitted on 39 of his words)
LOWER_SCALE = 0.92         # running lowercase is ~8% smaller than box lowercase (measured x-height band)
TRACE_T = 127
THICKEN = 2                # dilate the upsampled ink to match his pen weight (5.5 px at 300 dpi)
BOTTOM = set("abcdehiklmnorstuvwxz" + "ABCDEFGHIKLMNOPRSTUVWXYZ" + "0123456789" + ".!?")
HANG = {",": 0.30}         # comma: top sits this fraction of x-height above the baseline, the rest hangs
TOP_XH = set("gpqy")       # tails: align the top of the letter to x-height
TOP_ASC = set("f")         # his f has an ascender and a tail: align its top to ascender height
TOP_CAP = set("JQ")
UNI = {"−": 0x2212, "×": 0xD7, "°": 0xB0, "·": 0xB7, "±": 0xB1, "→": 0x2192, "←": 0x2190,
       "↑": 0x2191, "↓": 0x2193, "⇌": 0x21CC}

# What he actually wrote on sheet page 4 (from the scan), used to fit the word gap. Line 4 (vector
# arrows) and line 6 (commas with no spaces) cannot be split into words by gaps and are left out.
WRITTEN = {0: "The quick brown fox jumps over the lazy dog.",
           1: "Sphinx of black quartz, judge my vow",
           2: "Step 1: convert grams to moles. Step 2: multiply by",
           3: "Subtract 4 from both sides, then divide both sides by 2, so x=1.",
           5: "The mole cancels, molecules remain. 1s 2s 2p 3s 3p, six valence electrons."}


# ------------------------------------------------------------------ registration
def rasterise(pdf, tmp):
    subprocess.run(["pdftoppm", "-r", str(DPI), "-png", pdf, os.path.join(tmp, "p")], check=True)
    return sorted(os.path.join(tmp, f) for f in os.listdir(tmp) if f.startswith("p-"))


def register(path, m):
    g = cv2.imread(path, 0)
    _, bw = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY_INV)
    n, _, st, cen = cv2.connectedComponentsWithStats(bw)
    found = [tuple(cen[i]) for i in range(1, n)
             if 3000 < st[i][4] < 6500 and 0.8 < st[i][2] / st[i][3] < 1.25 and st[i][4] > 0.8 * st[i][2] * st[i][3]]
    if len(found) < 4:
        sys.exit(f"{os.path.basename(path)}: found {len(found)} corner squares, need 4. Rescan with the corners clear.")
    dst = np.float32([((x + w / 2) * DPI, (y + h / 2) * DPI) for x, y, w, h in m["reg_squares_in"]])
    src = np.float32([min(found, key=lambda p: (p[0] - dx) ** 2 + (p[1] - dy) ** 2) for dx, dy in dst])
    H = cv2.getPerspectiveTransform(src, dst)
    return cv2.warpPerspective(g, H, (int(8.5 * DPI), int(11 * DPI)), flags=cv2.INTER_CUBIC, borderValue=255)


def crops(items):
    for b in items:
        wx, wy, ww, wh = b["write"]
        yield b, [int(round(v * DPI)) for v in (wx, wy, wx + ww, wy + wh)]


# ------------------------------------------------------------------ ink
def ink_mask(gray):
    ink = (gray < INK_THRESH).astype(np.uint8)
    h, w = ink.shape
    ink[:, :8] = 0; ink[:, -8:] = 0; ink[:6, :] = 0; ink[-6:, :] = 0
    n, lab, st, _ = cv2.connectedComponentsWithStats(ink)
    for i in range(1, n):                       # drop guide-line remnants and specks
        _, _, cw, ch, a = st[i]
        if (cw > 0.8 * w and ch < 8) or a < 14:
            ink[lab == i] = 0
    return ink


def bbox(ink):
    ys, xs = np.nonzero(ink)
    return None if len(xs) == 0 else (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)


def trace(ink_crop):
    big = cv2.resize(ink_crop * 255, None, fx=UP * H_SCALE, fy=UP, interpolation=cv2.INTER_CUBIC)
    big = cv2.GaussianBlur(big, (0, 0), 1.6 * UP / 2)
    ink = (big > TRACE_T).astype(np.uint8)
    if THICKEN:
        ink = cv2.dilate(ink, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * THICKEN + 1,) * 2))
    return potrace.Bitmap(ink == 0).trace(turdsize=6 * UP, alphamax=1.05, opticurve=True, opttolerance=0.25)


def draw(plist, x_of, y_of, pen):
    for curve in plist:
        sp = curve.start_point
        pen.moveTo((x_of(sp.x), y_of(sp.y)))
        for seg in curve.segments:
            if seg.is_corner:
                pen.lineTo((x_of(seg.c.x), y_of(seg.c.y)))
                pen.lineTo((x_of(seg.end_point.x), y_of(seg.end_point.y)))
            else:
                pen.curveTo((x_of(seg.c1.x), y_of(seg.c1.y)), (x_of(seg.c2.x), y_of(seg.c2.y)),
                            (x_of(seg.end_point.x), y_of(seg.end_point.y)))
        pen.closePath()


# ------------------------------------------------------------------ spacing
def word_gap_px(page4, sent_page):
    """Median word gap in his running writing: the n-1 widest gaps on each line are the word breaks."""
    lines = list(crops(sent_page["lines"]))
    gaps = []
    for li, text in WRITTEN.items():
        _, (x0, y0, x1, y1) = lines[li]
        cols = np.nonzero(ink_mask(page4[y0:y1, x0:x1]).sum(0) > 0)[0]
        g = sorted((b - a - 1 for a, b in zip(cols, cols[1:]) if b - a > 1), reverse=True)
        gaps += g[:len(text.split()) - 1]
    return statistics.median(gaps)


# ------------------------------------------------------------------ build
def build(pages, m, out):
    items = []
    for pg in m["pages"]:
        if pg.get("kind") == "sentences":
            continue
        img = pages[pg["n"]]
        for b, (x0, y0, x1, y1) in crops(pg["boxes"]):
            ink = ink_mask(img[y0:y1, x0:x1])
            bb = bbox(ink)
            if bb is None:
                items.append(dict(char=b["char"], missing=True))
                continue
            by = int(round(b["baseline_y"] * DPI)) - y0
            items.append(dict(char=b["char"], alt="again" in b["name"], ink=ink, bb=bb,
                              bottom_off=bb[3] - by, page=pg["n"]))
    ok = [i for i in items if not i.get("missing")]
    missing = [i["char"] for i in items if i.get("missing")]

    # each page's baseline correction comes from letters that sit on the line (not tails, not J/Q)
    shift = {p: statistics.median([i["bottom_off"] for i in ok if i["page"] == p and i["char"].isalnum()
                                   and i["char"].isascii() and i["char"] not in "gjpqyfQJ"] or [0])
             for p in {i["page"] for i in ok}}
    cap_px = statistics.median([i["bb"][3] - i["bb"][1] for i in ok
                                if i["char"] in "ABDEFHIKLMNPRTUVWXYZ" and not i["alt"]])
    scale = CAP / cap_px
    h = lambda i: (i["bb"][3] - i["bb"][1]) * scale * LOWER_SCALE
    xh_ref = statistics.median([h(i) for i in ok if i["char"] in "acemnorsuvwxz"])
    asc_ref = statistics.median([h(i) for i in ok if i["char"] in "bdhkl"])

    glyphs, order, metrics, cmap, alts = {}, [".notdef", "space"], {}, {}, {}
    pen = TTGlyphPen(None)
    for a, b, c, d in ((60, 0, 460, 700), (100, 40, 420, 660)):
        pen.moveTo((a, b)); pen.lineTo((a, d)); pen.lineTo((c, d)); pen.lineTo((c, b)); pen.closePath()
    glyphs[".notdef"] = pen.glyph(); metrics[".notdef"] = (520, 60)
    glyphs["space"] = TTGlyphPen(None).glyph()

    used = {}
    for i in ok:
        ch = i["char"]
        name = (ch + ("_cap" if ch.isupper() else "")) if (ch.isascii() and ch.isalpha()) else \
               (ch if ch.isascii() and ch.isalnum() else f"uni{ord(ch):04X}")
        used[name] = used.get(name, 0) + 1
        gname = name + ".alt" if i["alt"] else (name if used[name] == 1 else f"{name}.dup{used[name] - 1}")
        x0, y0, x1, y1 = i["bb"]
        cx0, cy0 = max(0, x0 - 6), max(0, y0 - 6)
        crop = i["ink"][cy0:y1 + 6, cx0:x1 + 6]
        gs = LOWER_SCALE if (ch.islower() and ch.isascii()) else 1.0
        hu = (y1 - y0) * scale * gs
        if ch in BOTTOM:
            bottom = 0
        elif ch in HANG:
            bottom = HANG[ch] * xh_ref - hu
        elif ch in TOP_XH:
            bottom = xh_ref - hu
        elif ch in TOP_ASC:
            bottom = asc_ref - hu
        elif ch in TOP_CAP:
            bottom = CAP - hu
        else:
            bottom = -(i["bottom_off"] - shift[i["page"]]) * scale * gs
        lsb = PUNCT_LSB if ch in ".,:;" else LSB_DEFAULT
        pen = TTGlyphPen(None)
        draw(trace(crop),
             lambda u: round(((u / UP) + (cx0 - x0) * H_SCALE) * scale * gs + lsb),
             lambda v: round((y1 - (v / UP + cy0)) * scale * gs + bottom),
             ReverseContourPen(Cu2QuPen(pen, max_err=1.0, reverse_direction=False)))
        glyphs[gname] = pen.glyph()
        metrics[gname] = (round((x1 - x0) * H_SCALE * scale * gs + 2 * lsb), lsb)
        order.append(gname)
        if i["alt"]:
            cmap[0xE000 + len(alts)] = gname          # second hand-written copy, reachable by key_ink
            alts[ch] = chr(0xE000 + len(alts))
        else:
            cmap[UNI.get(ch, ord(ch))] = gname
            if ch == "−":
                cmap[0x2013] = gname
            if ch == "-":
                cmap[0x2010] = gname
    if 0x27 in cmap:
        cmap.setdefault(0x2019, cmap[0x27])

    wg = word_gap_px(pages[4], [p for p in m["pages"] if p.get("kind") == "sentences"][0])
    space = max(150, round(wg * scale - 2 * LSB_DEFAULT))
    metrics["space"] = (space, 0)
    cmap[0x20] = "space"

    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics({g: metrics[g] for g in order})
    fb.setupHorizontalHeader(ascent=900, descent=-300)
    fb.setupNameTable({"familyName": "ShullHand", "styleName": "Regular",
                       "copyright": "Handwriting of Matthew Shull, made from his own writing sample (SHULL-CHG-0044).",
                       "uniqueFontIdentifier": "ShullHand-Regular", "fullName": "ShullHand Regular",
                       "psName": "ShullHand-Regular", "version": VERSION})
    fb.setupOS2(sTypoAscender=900, sTypoDescender=-300, usWinAscent=1000, usWinDescent=350,
                sxHeight=round(xh_ref), sCapHeight=CAP, fsType=0)
    fb.setupPost()
    fb.save(out + ".ttf")
    with open(out + "_alts.json", "w") as fh:
        json.dump(alts, fh, ensure_ascii=False, indent=1)
    report = {"version": VERSION, "glyphs": len(order), "alternates": len(alts), "missing": missing,
              "cap_px": float(cap_px), "units_per_px": round(scale, 3), "x_height": round(xh_ref),
              "ascender": round(asc_ref), "word_gap_px": float(wg), "space_advance": space}
    print(json.dumps(report, indent=1, ensure_ascii=False))
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--scan", required=True)
    ap.add_argument("--page-order", default="1,2,3,4", help="sheet page number for each scan page, in scan order")
    ap.add_argument("--out", required=True, help="output path without extension")
    a = ap.parse_args()
    m = layout()
    order = [int(x) for x in a.page_order.split(",")]
    with tempfile.TemporaryDirectory() as tmp:
        files = rasterise(a.scan, tmp)
        if len(files) != len(order) or sorted(order) != list(range(1, len(m["pages"]) + 1)):
            sys.exit(f"scan has {len(files)} pages; --page-order must list each of 1..{len(m['pages'])} once")
        pages = {n: register(f, m) for f, n in zip(files, order)}
    build(pages, m, a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
