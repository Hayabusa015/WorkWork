#!/usr/bin/env python3
"""
SHULL Science - Missing Work renderer.

    python3 templates/missing-work/build_missing_work.py

Renders the neutral master plus one course-accent version each for Chemistry,
Physics and Geology from SHULL_Missing_Work_TEMPLATE.html. Fails if any output
is not exactly one page. Afterwards run, per PDF:
    python3 scripts/audit_fonts.py FILE.pdf
    python3 scripts/audit_print_ink.py FILE.pdf
and rasterise and LOOK at it.
"""
import re
import sys
from pathlib import Path

from weasyprint import HTML

HERE = Path(__file__).resolve().parent
SRC = HERE / "SHULL_Missing_Work_TEMPLATE.html"

VARIANTS = [
    ("", "neutral", None),
    ("_CHEM", "chem", "Chemistry"),
    ("_PHYS", "phys", "Physics"),
    ("_GEO", "geo", "Geology"),
]


def render(suffix, cls, course, html):
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html = html.replace('<body class="neutral">', f'<body class="{cls}">')
    if course:
        chip = f'<div class="chip">{course.upper()}</div>'
        html = html.replace("</h1>\n  </div>", f"</h1>\n    {chip}\n  </div>", 1)
        html = re.sub(r'<div class="course-select">.*?</div>\n', "", html, count=1, flags=re.S)
        html = html.replace('<div class="m-course"></div>',
                            f'<div class="m-course"> \\00b7  {course.upper()}</div>'.replace("\\00b7", "·"))
    out = HERE / f"SHULL_Missing_Work_TEMPLATE{suffix}.pdf"
    doc = HTML(string=html, base_url=str(HERE)).render()
    doc.write_pdf(out)
    return out, len(doc.pages)


def main() -> int:
    html = SRC.read_text(encoding="utf-8")
    bad = 0
    for suffix, cls, course in VARIANTS:
        out, pages = render(suffix, cls, course, html)
        flag = "ok" if pages == 1 else "OVER BUDGET"
        print(f"{out.name}: {pages} page(s) {flag}")
        bad += pages != 1
    if bad:
        print("Tighten in order: @page margins, base font-size, line-height, row height.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
