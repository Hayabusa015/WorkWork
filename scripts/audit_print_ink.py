#!/usr/bin/env python3
"""Measure how much ink a print document lays down.

standards/QA_GATE.md section 5 says this is measurable rather than a matter of
taste - "rasterise and compute the percentage of marked pixels" - and names a
rebuilt practice set at 5.2% marked, 2.9% heavy as the reference. Until now
nothing computed it, so the rule was a paragraph rather than a gate.

    python3 scripts/audit_print_ink.py doc.pdf [--max-marked 8] [--max-heavy 4]

marked  any pixel darker than white by more than a hairline's worth - includes
        rules, borders and type
heavy   pixels dark enough to be a fill rather than a mark. This is the number
        that catches a solid header bar, which the standard fails immediately.
"""
import argparse, os, sys

# Calibrated against Matthew's own GEO U1 guided-notes packet, which he wrote before
# any of this system existed and which is already ink-disciplined: no cell fills
# anywhere, 5.41% marked and 2.80% heavy on average, worst page 8.35% / 3.97%. The QA
# gate's quoted reference - 5.2% marked, 2.9% heavy - lands on the same numbers.
# So the limits sit just above his packet. Anything materially inkier than what he was
# already doing by hand is the thing this check is for.
MARKED_MAX_DEFAULT = 9.0
HEAVY_MAX_DEFAULT = 4.0    # above this there is a fill on the page


def measure(path, dpi=110):
    import pymupdf
    doc = pymupdf.open(path)
    rows = []
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
        hist = [0] * 256
        for b in pix.samples:
            hist[b] += 1
        total = pix.width * pix.height
        marked = sum(hist[:245]) / total * 100.0
        heavy = sum(hist[:128]) / total * 100.0
        rows.append((i, marked, heavy))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--max-marked", type=float, default=MARKED_MAX_DEFAULT)
    ap.add_argument("--max-heavy", type=float, default=HEAVY_MAX_DEFAULT)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    rows = measure(a.pdf)
    name = os.path.basename(a.pdf)
    worst_m = max(r[1] for r in rows)
    worst_h = max(r[2] for r in rows)
    avg_m = sum(r[1] for r in rows) / len(rows)
    avg_h = sum(r[2] for r in rows) / len(rows)

    if not a.quiet:
        print(f"audit_print_ink: {name}")
        for i, m, h in rows:
            flag = "  <-- heavy" if h > a.max_heavy else ""
            print(f"   p{i}: {m:5.2f}% marked   {h:5.2f}% heavy{flag}")
        print(f"   avg: {avg_m:5.2f}% marked   {avg_h:5.2f}% heavy")

    fail = []
    if worst_m > a.max_marked:
        fail.append(f"worst page is {worst_m:.2f}% marked, over the {a.max_marked}% limit")
    if worst_h > a.max_heavy:
        fail.append(f"worst page is {worst_h:.2f}% heavy, over the {a.max_heavy}% limit — "
                    f"that is a fill, and QA_GATE section 5 fails a solid fill immediately")
    if fail:
        print(f"\nFAIL — {name}")
        for f in fail:
            print("  - " + f)
        return 1
    print(f"\nOK — within the print ink budget "
          f"({worst_m:.2f}% marked, {worst_h:.2f}% heavy at worst)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
