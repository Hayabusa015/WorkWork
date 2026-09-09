---
name: audit-deliverable
description: Run the full QA gate against a finished deliverable and report findings. Use before anything ships, and whenever an independent quality check is warranted. Reports; never fixes.
---

# audit-deliverable

Gate: `standards/QA_GATE.md`. This is the procedure.

> **Never fix what you find.** Report it. The Overseer routes the fix to the Designer.

## 1. Render it and look at it

```bash
# .docx / .pptx
soffice --headless --norestore --convert-to pdf --outdir . FILE
# then rasterize and actually view the pages
python3 -c "import pymupdf; d=pymupdf.open('FILE.pdf'); [d[i].get_pixmap(dpi=110).save(f'/tmp/p{i}.png') for i in range(len(d))]"
```

**Then open the images.** Never ship a document you have not seen rendered.

## 2. Check the font actually used

```bash
pdffonts FILE.pdf
```

**Archivo or Archivo Narrow.** DejaVu or Liberation means the substitution did not take and every
layout check below is being run against the wrong metrics.

## 3. Measure the ink — print documents only

```bash
python3 scripts/audit_print_ink.py FILE.pdf
python3 scripts/audit_fonts.py FILE.pdf
```

**Do not measure ink by counting marked pixels.** That was the rule here and it is wrong: it counts
a 7% grey tint exactly as hard as solid black. The budget is **toner coverage** — the mean darkness
of the page, which is what a cartridge spends. `audit_print_ink.py` reports toner (the budget,
ceiling 9%), marked (density, reported), and the widest solid band. Any solid fill wider than
0.60 in fails regardless of either number. SHULL-CHG-0020.

`audit_fonts.py` fails a PDF that renders in anything but Archivo and names the character that
pulled the substitute in.

## 4. Then the rest of the gate

Clipped text — highest priority, scan every page edge · page budget · grayscale · codes match and
exist in the decisions file · voice · separate answer key · every number re-solved.

Plus the deliverable-specific additions in the gate.

## Report

| # | Check | Problem | Fix | Severity |
|---|---|---|---|---|

**blocking** (student-facing error, wrong science, unreadable print) · **should-fix** (brand drift) ·
**nice-to-have** (polish). Blocking first, then shortest fix first.

**If any check fails, the deliverable is INCOMPLETE.** Say so plainly. Do not let a nearly-passing
deliverable through because the remaining issue looks small — clipped text and a wrong accepted
value both look small in a summary.
