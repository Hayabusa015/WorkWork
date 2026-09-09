#!/usr/bin/env python3
"""Measure a built worksheet: pages per section, and print ink.

    python3 scripts/audit_worksheet.py out.docx [spec.json]
    python3 scripts/audit_worksheet.py out.pdf  [spec.json]

Two rules, both measured rather than judged:

  THE PAGE BUDGET.       A section is handed out as a unit, so how many sheets of paper
  it costs per student is a design decision, not an accident. The spec declares it
  (`pagesPerSection`) and this measures against that. It is not one page for everybody:
  a Physics section is one page because there is nothing to write on it, a Chemistry
  section with eight work boxes cannot be, and a cut-and-glue activity is two by
  construction - the cards, then the slots they are glued into. Declaring the number
  is the point: a section that quietly grows a page is the failure, not a section that
  was always three.

  THE INK BUDGET.        Delegated to audit_print_ink.py, which reports % marked and
  the widest solid band. Section 8 of the design system fails the band, not the
  percentage; do not read one as the other.
"""
import json, os, re, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE = re.compile(r"PRACTICE SET|WORKSHEET|ACTIVITY|STUDY GUIDE", re.I)


def to_pdf(path):
    if path.lower().endswith(".pdf"):
        return path, None
    tmp = tempfile.mkdtemp()
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, path],
                   check=True, capture_output=True)
    return os.path.join(tmp, os.path.basename(path)[:-5] + ".pdf"), tmp


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    import pymupdf
    budget, per_code = 1, {}
    if len(sys.argv) > 2:
        spec = json.load(open(sys.argv[2]))
        budget = int(spec.get("pagesPerSection", 1))
        for sec in spec.get("sectionsContent", []):
            if "pagesPerSection" in sec:
                per_code[f"U{int(spec['unit']):02d}/S{sec['code']}"] = \
                    int(sec["pagesPerSection"])
    pdf, _tmp = to_pdf(sys.argv[1])
    doc = pymupdf.open(pdf)
    print(f"audit_worksheet: {os.path.basename(sys.argv[1])}")

    # A section starts on the page whose text carries the brand eyebrow. Anything
    # between one eyebrow and the next belongs to that section.
    starts = []
    for i, page in enumerate(doc):
        txt = page.get_text()
        flat = txt.replace(" ", "")
        if "SHULLSCIENCE·" in flat and "MR.SHULL" in flat:
            # The kicker is letter-tracked, so the code arrives as "U 0 1  /  S 1 . 1".
            # Match on the despaced text or nothing will ever be found.
            m = re.search(r"U\d{1,2}/S\d{1,2}\.\d", flat)
            starts.append((i, m.group(0) if m else f"page {i + 1}"))
    if not starts:
        print("   no section headers found — not a worksheet built by this template.")
        starts = [(0, "whole document")]

    bad = []
    for j, (i, code) in enumerate(starts):
        end = starts[j + 1][0] if j + 1 < len(starts) else doc.page_count
        n = end - i
        want = per_code.get(code, budget)
        flag = "" if n == want else f"   <-- budget {want}"
        print(f"   {code:<12} {n} page(s){flag}")
        if n != want:
            # Name what spilled, so the fix is obvious rather than a guess.
            over = doc[end - 1].get_text().strip().split("\n")
            tail = next((x for x in over if x.strip()), "")[:58]
            bad.append((code, n, tail))
    print()
    ink = subprocess.run([sys.executable, os.path.join(REPO, "scripts", "audit_print_ink.py"), pdf],
                         capture_output=True, text=True)
    print(ink.stdout.strip().split("\n")[-1])

    if bad:
        print()
        print("FAIL — sections off their declared page budget:")
        for code, n, tail in bad:
            want = per_code.get(code, budget)
            print(f"   {code}  {n} pages, budget {want}. "
                  f"Last page opens with: {tail!r}")
        print("\nEither trim the section - block margins, then a key idea or a "
              "prior-knowledge item, then a checklist line, never a question - or "
              "raise\n`pagesPerSection` in the spec if the extra page is genuinely "
              "the design.")
        return 1
    if ink.returncode:
        print(ink.stderr.strip())
        return 1
    print("\nOK — every section is on its declared page budget, and the ink is within "
          "budget.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
