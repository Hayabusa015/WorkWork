#!/usr/bin/env python3
"""Check the binding side of every printed page: hole zone clear, guides present.

    python3 scripts/audit_binding.py doc.pdf [--dpi 150]
    python3 scripts/audit_binding.py doc.docx          # rendered with LibreOffice first

SHULL-CHG-0075 (brand/SHULL_DESIGN_SYSTEM.md §8). Every printed page has an inside
margin for three-hole punching - left on odd pages, right on even pages - and three
faint guide circles where the holes land. All numbers come from brand/tokens.json
(`print.binding`, `print.holeGuides`) through templates/_shull_print.py; none is typed
here.

Per page, rasterised in greyscale:

  zone    The HOLE ZONE is the full height of the inside margin, binding edge to
          `print.binding.inside`. With the three guide circles masked out, nothing may
          mark it. Any pixel darker than the paper there is content ink that a punch
          would cut through or graze. FAIL.
  guides  Each of the three circles must be drawn where tokens put it, on the binding
          side for this page's parity, and must NOT be drawn on the other edge (a page
          that did not flip). FAIL.
  ink     The guides must stay within the print-ink rules: outline only (no solid band
          anywhere inside them) and no darker than the ruleHairline stroke they are
          drawn in. Their toner share of the page is reported. FAIL on a fill or a
          stroke darker than the token.

The darkest guide pixel is also reported, because a hairline in a pale grey can drop
out on a copier: it is the number to look at before trusting the guides to show.
"""
import argparse, math, os, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "templates"))
from _shull_print import BINDING, PAGE_W_IN, guides, hole_zone   # noqa: E402

PAPER = 245            # a pixel darker than this is a mark (audit_print_ink's "marked")
EDGE_TOL_IN = 0.02     # anti-aliasing of a rule set exactly on the inside margin
MASK_PAD_IN = 0.05     # room around a guide circle for its own anti-aliasing
RING_HIT = 252         # a ring sample this dark or darker counts as the guide being drawn
RING_MIN_SHARE = 0.6   # share of ring samples that must be drawn for a guide to exist
RING_STRAY_SHARE = 0.2 # on the wrong edge, more than this share means a guide is there
OUTER_ARC_IN = 0.30    # see ring_share(edge_only=True)
GREY_TOL = 25          # how much darker than the stroke token anti-aliased edges may read


def to_pdf(path):
    if path.lower().endswith(".pdf"):
        return path
    tmp = tempfile.mkdtemp()
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, path],
                   check=True, capture_output=True)
    return os.path.join(tmp, os.path.splitext(os.path.basename(path))[0] + ".pdf")


def _lum(hexval):
    h = hexval.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return round(0.299 * r + 0.587 * g + 0.114 * b)


def ring_share(px, w, h, cx, cy, r, dpi, edge_only=False):
    """Share of points around the circle (radius r, inches) that carry a mark.

    `edge_only` samples just the arc nearer the sheet edge than OUTER_ARC_IN, where no
    builder puts content (the narrowest outside margin is 0.35 in). It is how the other
    edge is checked for a guide that should not be there without mistaking the end of a
    line of text for one."""
    n, hit, used = 72, 0, 0
    for k in range(n):
        a = 2 * math.pi * k / n
        px_in = cx + r * math.cos(a)
        if edge_only and min(px_in, PAGE_W_IN - px_in) >= OUTER_ARC_IN:
            continue
        used += 1
        x0, y0 = px_in * dpi, (cy + r * math.sin(a)) * dpi
        best = 255
        for dx in (-2, -1, 0, 1, 2):
            for dy in (-2, -1, 0, 1, 2):
                x, y = int(round(x0)) + dx, int(round(y0)) + dy
                if 0 <= x < w and 0 <= y < h:
                    best = min(best, px[y * w + x])
        hit += best <= RING_HIT
    return hit / used if used else 0.0


def audit_page(px, w, h, page_no, dpi):
    r = BINDING.radius_in
    mask_r = (r + MASK_PAD_IN) * dpi
    centres = [(x * dpi, y * dpi) for x, y in guides(page_no)]
    x0, x1 = hole_zone(page_no)
    if x0 == 0:
        x1 -= EDGE_TOL_IN
    else:
        x0 += EDGE_TOL_IN
    xa, xb = int(math.floor(x0 * dpi)), min(w, int(math.ceil(x1 * dpi)))

    stray, stray_box = 0, None
    guide_ink, darkest, band = 0, 255, 0
    for y in range(h):
        run = 0
        for x in range(xa, xb):
            v = px[y * w + x]
            inside = any((x - cx) ** 2 + (y - cy) ** 2 <= mask_r ** 2 for cx, cy in centres)
            if inside:
                guide_ink += 255 - v
                darkest = min(darkest, v)
                run = run + 1 if v < 128 else 0
                band = max(band, run)
            elif v < PAPER:
                stray += 1
                bx = (x / dpi, y / dpi)
                stray_box = (bx, bx) if stray_box is None else (
                    (min(stray_box[0][0], bx[0]), min(stray_box[0][1], bx[1])),
                    (max(stray_box[1][0], bx[0]), max(stray_box[1][1], bx[1])))

    shares = [ring_share(px, w, h, cx, cy, r, dpi) for cx, cy in guides(page_no)]
    other = [ring_share(px, w, h, PAGE_W_IN - cx, cy, r, dpi, edge_only=True)
             for cx, cy in guides(page_no)]
    return {
        "page": page_no, "side": "left" if page_no % 2 else "right",
        "stray": stray, "stray_box": stray_box, "shares": shares, "other": other,
        "darkest": darkest, "band_in": band / dpi,
        "toner_pct": guide_ink / (255.0 * w * h) * 100.0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doc")
    ap.add_argument("--dpi", type=int, default=150)
    a = ap.parse_args()
    import pymupdf
    pdf = to_pdf(a.doc)
    doc = pymupdf.open(pdf)
    stroke_lum = _lum(BINDING.stroke_hex)
    name = os.path.basename(a.doc)
    print(f"audit_binding: {name}   (inside {BINDING.inside_in} in, guides "
          f"{BINDING.diameter_in} in at {BINDING.centre_from_edge_in} in, "
          f"{BINDING.stroke_pt} pt, {a.dpi} dpi)")
    fails = []
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=a.dpi, colorspace=pymupdf.csGRAY, alpha=False)
        if pix.width != round(PAGE_W_IN * a.dpi):
            fails.append(f"p{i}: page is not {PAGE_W_IN} in wide")
            continue
        px = bytes(pix.samples) if pix.stride == pix.width else b"".join(
            pix.samples[y * pix.stride:y * pix.stride + pix.width] for y in range(pix.height))
        res = audit_page(px, pix.width, pix.height, i, a.dpi)
        ok_g = all(s >= RING_MIN_SHARE for s in res["shares"])
        ok_o = all(s <= RING_STRAY_SHARE for s in res["other"])
        ok_z = res["stray"] == 0
        ok_i = res["band_in"] == 0 and res["darkest"] >= stroke_lum - GREY_TOL
        print(f"   p{i:<2} {res['side']:<5}  zone {'clear' if ok_z else 'INK x%d' % res['stray']:<10}"
              f" guides {'/'.join('%.0f%%' % (s * 100) for s in res['shares']):<14}"
              f" other edge {'/'.join('%.0f%%' % (s * 100) for s in res['other']):<12}"
              f" darkest {res['darkest']:>3}  guide toner {res['toner_pct']:.3f}%")
        if not ok_z:
            (ax, ay), (bx, by) = res["stray_box"]
            fails.append(f"p{i}: {res['stray']} content pixels in the hole zone, "
                         f"x {ax:.2f}-{bx:.2f} in, y {ay:.2f}-{by:.2f} in")
        if not ok_g:
            fails.append(f"p{i}: a hole guide is missing on the {res['side']} edge")
        if not ok_o:
            fails.append(f"p{i}: guides drawn on the outside edge too (page did not flip?)")
        if not ok_i:
            fails.append(f"p{i}: guide ink out of bounds (band {res['band_in']:.2f} in, "
                         f"darkest {res['darkest']} vs stroke {stroke_lum})")
    if fails:
        print(f"\nFAIL — {name}")
        for f in fails:
            print("  - " + f)
        return 1
    print(f"\nOK — {len(doc)} pages: hole zone clear, guides on the binding side, "
          f"outline only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
