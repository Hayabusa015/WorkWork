#!/usr/bin/env python3
"""Measure how much ink a print document lays down.

standards/QA_GATE.md section 5 says this is measurable rather than a matter of
taste - "rasterise and compute the percentage of marked pixels" - and names a
rebuilt practice set at 5.2% marked, 2.9% heavy as the reference. Until now
nothing computed it, so the rule was a paragraph rather than a gate.

    python3 scripts/audit_print_ink.py doc.pdf [--max-marked 8] [--max-heavy 4]

marked  any pixel darker than white by more than a hairline's worth - includes
        rules, borders and type. An ink-volume budget.
fill    the widest solid dark band on the page, in inches. THIS is what the
        standard fails immediately - "any solid fill larger than a small tag,
        chip, or icon".

The two are different measurements and an earlier version of this file conflated
them. Counting dark pixels cannot tell a solid header bar from a page of dense
10pt text, and on that basis it wrongly failed the lab template - which has no
fills at all, only a lot of words. A fill is found by geometry instead: text
makes short dark runs the width of a glyph stroke, a bar makes one run hundreds
of pixels wide, repeated down its height.
"""
import argparse, os, sys

# Calibrated against Matthew's own GEO U1 guided-notes packet, which he wrote before
# any of this system existed and which is already ink-disciplined: no cell fills
# anywhere, 5.41% marked on average, worst page 8.35%. The QA gate's quoted reference
# lands on the same numbers. The lab template is denser at 7.14% and legitimately so -
# it is five pages of procedure - hence the headroom.
MARKED_MAX_DEFAULT = 12.0
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
        marked_px = 0
        run_rows, widest_band, streak = 0, 0, 0
        for y in range(h):
            base = y * pix.stride
            row = data[base:base + w]
            marked_px += sum(1 for v in row if v < 245)
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
        out.append((i, marked_px / (w * h) * 100.0, widest_band / dpi))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--max-marked", type=float, default=MARKED_MAX_DEFAULT)
    ap.add_argument("--max-fill", type=float, default=FILL_MAX_IN_DEFAULT)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    rows = measure(a.pdf)
    name = os.path.basename(a.pdf)
    worst_m = max(r[1] for r in rows)
    worst_f = max(r[2] for r in rows)
    avg_m = sum(r[1] for r in rows) / len(rows)

    if not a.quiet:
        print(f"audit_print_ink: {name}")
        for i, m, f in rows:
            band = f"{f:.2f}in band" if f else "no fill"
            flag = "  <-- FILL" if f > a.max_fill else ""
            print(f"   p{i}: {m:5.2f}% marked   {band:>12}{flag}")
        print(f"   avg: {avg_m:5.2f}% marked")

    fail = []
    if worst_m > a.max_marked:
        fail.append(f"worst page is {worst_m:.2f}% marked, over the {a.max_marked}% budget")
    if worst_f > a.max_fill:
        fail.append(f"a solid band {worst_f:.2f}in wide — QA_GATE section 5 fails any fill "
                    f"larger than a small tag, chip or icon")
    if fail:
        print(f"\nFAIL — {name}")
        for f in fail:
            print("  - " + f)
        return 1
    print(f"\nOK — {worst_m:.2f}% marked at worst, widest solid band {worst_f:.2f}in")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Piped into head. Not a failure.
        os._exit(0)
