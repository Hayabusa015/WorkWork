#!/usr/bin/env python3
"""Measure how much ink a print document lays down.

standards/QA_GATE.md section 5 says this is measurable rather than a matter of
taste - "rasterise and compute the percentage of marked pixels" - and names a
rebuilt practice set at 5.2% marked, 2.9% heavy as the reference. Until now
nothing computed it, so the rule was a paragraph rather than a gate.

    python3 scripts/audit_print_ink.py doc.pdf [--max-marked 8] [--max-heavy 4]

toner   ink volume: the mean darkness of the page, which is what a cartridge
        actually spends. THIS is the ink budget.
marked  the share of the page carrying any mark at all. A density and whitespace
        reading, NOT an ink reading - reported, not failed on except at an
        extreme.
fill    the widest solid dark band on the page, in inches. THIS is what the
        standard fails immediately - "any solid fill larger than a small tag,
        chip, or icon".

These are three different measurements and this file has now conflated two pairs
of them, so both mistakes are written down.

Counting dark pixels cannot tell a solid header bar from a page of dense 10pt
text, and on that basis an early version wrongly failed the lab template - which
has no fills at all, only a lot of words. A fill is found by geometry instead:
text makes short dark runs the width of a glyph stroke, a bar makes one run
hundreds of pixels wide, repeated down its height.

Then `marked` was used as the ink budget, which it is not. It counts a 7% grey
tint exactly as hard as solid black, so it ranked a sheet with two pale panels
(18.70% marked, 4.68% toner) as worse than one with solid navy banners across
every page (12.47% marked, 8.15% toner) - when the second lays down 74% more
ink. Toner coverage is the ink model: a pixel at 93% white costs 7% of a black
one, because that is what the cartridge spends. SHULL-CHG-0020.
"""
import argparse, os, sys

# Calibrated against Matthew's own GEO U1 guided-notes packet, which he wrote before
# any of this system existed and which is already ink-disciplined: no cell fills
# anywhere, 5.41% marked on average, worst page 8.35%. The QA gate's quoted reference
# lands on the same numbers. The lab template is denser at 7.14% and legitimately so -
# it is five pages of procedure - hence the headroom.
# Calibrated on his own files, measured rather than picked:
#   his nebular cut-and-glue sheet   3.09% toner    (the sheet he says he loves)
#   his old PHYS U01 practice set    8.15% toner
#   his Master_Physics mockup        8.70% toner    (fails on the band, not the ink)
# 9% passes everything he has written and shown, and fails a page meaningfully
# darker than any of it.
TONER_MAX_DEFAULT = 9.0
# `marked` is no longer the ink gate, so its ceiling is set where it catches a page
# that is genuinely covered rather than one that carries a pale panel.
MARKED_MAX_DEFAULT = 40.0
FILL_MAX_IN_DEFAULT = 0.60   # anything wider is a band, not a tag, chip or icon


# A band this wide, holding for this many rows, is a fill and not a glyph.
FILL_MIN_IN = 0.60      # wider than any letterform or a small chip
FILL_MIN_ROWS_IN = 0.06 # and it has to persist down the page, not be one hairline


def measure(path, dpi=110):
    import pymupdf
    doc = pymupdf.open(path)
    min_run = int(FILL_MIN_IN * dpi)
    min_rows = max(2, int(FILL_MIN_ROWS_IN * dpi))
    out = []
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
        w, h, data = pix.width, pix.height, pix.samples
        marked_px, ink = 0, 0
        run_rows, widest_band, streak = 0, 0, 0
        for y in range(h):
            base = y * pix.stride
            row = data[base:base + w]
            marked_px += sum(1 for v in row if v < 245)
            ink += sum(255 - v for v in row)
            best = run = 0
            for v in row:
                run = run + 1 if v < 128 else 0
                if run > best:
                    best = run
            if best >= min_run:
                streak += 1
                if streak >= min_rows and best > widest_band:
                    widest_band = best
            else:
                streak = 0
        out.append((i, marked_px / (w * h) * 100.0, widest_band / dpi,
                    ink / (255.0 * w * h) * 100.0))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--max-toner", type=float, default=TONER_MAX_DEFAULT)
    ap.add_argument("--max-marked", type=float, default=MARKED_MAX_DEFAULT)
    ap.add_argument("--max-fill", type=float, default=FILL_MAX_IN_DEFAULT)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    rows = measure(a.pdf)
    name = os.path.basename(a.pdf)
    worst_m = max(r[1] for r in rows)
    worst_f = max(r[2] for r in rows)
    worst_t = max(r[3] for r in rows)
    avg_t = sum(r[3] for r in rows) / len(rows)

    if not a.quiet:
        print(f"audit_print_ink: {name}")
        for i, m, f, t in rows:
            band = f"{f:.2f}in band" if f else "no fill"
            flag = "  <-- FILL" if f > a.max_fill else ""
            print(f"   p{i}: {t:5.2f}% toner   {m:5.2f}% marked   {band:>12}{flag}")
        print(f"   avg: {avg_t:5.2f}% toner")

    fail = []
    if worst_t > a.max_toner:
        fail.append(f"worst page lays down {worst_t:.2f}% toner, over the "
                    f"{a.max_toner}% budget")
    if worst_m > a.max_marked:
        fail.append(f"worst page is {worst_m:.2f}% marked — that is most of the page "
                    f"carrying something, over the {a.max_marked}% ceiling")
    if worst_f > a.max_fill:
        fail.append(f"a solid band {worst_f:.2f}in wide — QA_GATE section 5 fails any fill "
                    f"larger than a small tag, chip or icon")
    if fail:
        print(f"\nFAIL — {name}")
        for f in fail:
            print("  - " + f)
        return 1
    print(f"\nOK — {worst_t:.2f}% toner at worst ({worst_m:.2f}% marked), "
          f"widest solid band {worst_f:.2f}in")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Piped into head. Not a failure.
        os._exit(0)
