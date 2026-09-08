#!/usr/bin/env python3
"""
SHULL Science — Lab template renderer.

    python3 build_lab.py SHULL_CHEM_Lab_U00_S0.3_Intro_Skills.html

Writes a PDF beside the HTML with the same name, then runs the two checks
that catch the defects the QA gate cares about most:
  · unfilled [[ TOKENS ]] left in the document
  · page count, so a four-page lab doesn't quietly become five
"""
import re
import sys
from pathlib import Path

from weasyprint import HTML

def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 build_lab.py <file.html> [expected_pages]")
        return 2

    src = Path(sys.argv[1]).resolve()
    if not src.exists():
        print(f"not found: {src}")
        return 2

    html = src.read_text(encoding="utf-8")

    # Strip HTML comments so instructional notes never render into the PDF.
    render_html = re.sub(r"<!--.*?-->", "", html, flags=re.S)

    # Check 1 — unfilled tokens (ignore the ones inside comments).
    tokens = re.findall(r"\[\[.*?\]\]", render_html, flags=re.S)
    if tokens:
        print(f"⚠  {len(tokens)} unfilled token(s) still in the document:")
        for t in tokens[:12]:
            print("   ", " ".join(t.split())[:88])
        if len(tokens) > 12:
            print(f"    ... and {len(tokens) - 12} more")

    out = src.with_suffix(".pdf")
    doc = HTML(string=render_html, base_url=str(src.parent)).render()
    doc.write_pdf(out)

    # Check 2 — page budget.
    pages = len(doc.pages)
    print(f"✓  {out.name} — {pages} pages")
    if len(sys.argv) > 2:
        want = int(sys.argv[2])
        if pages != want:
            print(f"⚠  expected {want} pages, got {pages}. Tighten in this order: "
                  "@page margins → base font-size → line-height → block margins. "
                  "Never shrink one question to fit.")
            return 1

    print("   Now rasterize and LOOK at it before it goes to the copier.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
