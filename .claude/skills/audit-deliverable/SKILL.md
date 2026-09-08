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
python3 -c "
import pymupdf; p=pymupdf.open('FILE.pdf')[0].get_pixmap(dpi=150,colorspace=pymupdf.csGRAY).samples
print(f'{100*sum(1 for b in p if b<240)/len(p):.1f}% marked, {100*sum(1 for b in p if b<100)/len(p):.1f}% heavy')"
```

Benchmark is around 5% marked. Any solid fill larger than a small tag, chip, or icon fails
regardless of the number.

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
