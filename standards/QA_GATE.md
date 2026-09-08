# The QA Gate

**Every deliverable passes this before it ships.** Report the result in chat as a short checklist,
not prose.

The Auditor runs this independently and **never fixes what it finds** — findings route back through
the Overseer to the Designer. An auditor that patches its own findings is not an audit.

The qualitative half of quality is `standards/ANTI_AI_SLOP_STANDARD.md` §10. This is the mechanical
half.

---

## 1. Render it and look at it

**Never ship a document you have not seen rendered.**

| Format | Path |
|---|---|
| `.pdf` | rasterise with PyMuPDF and view the pages |
| `.docx` / `.pptx` | `soffice --headless --convert-to pdf`, then rasterise, then view |

The toolchain is installed by `scripts/setup-environment.sh`. If `soffice` cannot convert, **stop** —
do not ship on the assumption it looks right.

> **Confirm the render used the right font.** `pdffonts` on the output should show Archivo or
> Archivo Narrow. If it shows DejaVu or Liberation, the font substitution did not take and you are
> inspecting different metrics than the classroom copy will have. That was the real state of this
> system until 2026-09-08.

## 2. Page budget

Practice set is exactly 2 pages. Everything else is whatever was specified.

If over, fix **in this order**: reduce `@page` margins → reduce base font size → tighten line-height
→ reduce block bottom margins.

> **Never shrink a single question to fit.**

## 3. No clipped text

Scan every rasterised page for text cut off at a box, column, or slide edge. **This is the
highest-priority visual defect** — it has shipped before.

On slides, clipping almost always means the reserved-height rule was violated: text was placed first
and the highlight block overlaid on top.

## 4. Grayscale

Would a photocopy still distinguish the categories? **If the only difference is hue, fix it.**

Check the grayscale separation of any two colours carrying a distinction against
`rules.grayscaleSeparationMin` in `brand/tokens.json`. **Geology needs particular attention** — its
display pair is six levels apart, so border and label differentiation is mandatory, not optional.

## 5. Ink — print documents only

Estimate what a printer would lay down. This is measurable, not a matter of taste: rasterise and
compute the percentage of marked pixels. A rebuilt practice set measured 5.2% marked, 2.9% heavy.

**Fails immediately:**

- any solid fill larger than a small tag, chip, or icon
- full-page banners
- shaded section backgrounds
- table shading at medium or full saturation

Convert to outline treatment before shipping. This is not a nice-to-have — it ships back to the
Designer.

## 6. Codes match

The `U#/S#.#` on the document, in the filename, and in the folder path all agree — and the code
exists in that course's `DECISIONS.md`.

## 7. Voice

Read the directions aloud in your head. **Any sentence that sounds like a brochure gets rewritten.**

Then run the audit list in `standards/ANTI_AI_SLOP_STANDARD.md` §6.

## 8. Answer key exists and is a separate file

If the document has answers, the key is its own file ending `_Key`.

## 9. Every number re-solved independently

Including in **each** parallel version. A/B/C/D versions are not shuffles — re-solve each one from
scratch. Ugly or unrealistic answers mean changing the numbers, not shipping them.

---

## Deliverable-specific additions

**Slide decks** — no text under the 16pt content floor in the student-facing area · at most one
highlight block per slide · dark grounds only on title, divider, summary, index · the code chip on
every slide, matching the filename · **every worked example followed by a solution slide** · subheads
clear of the first bullet · rail card content vertically centred · headlines read correctly as
grammar, not just spelling.

**Guided notes** — student copy and filled key generated from the same source so they cannot drift ·
every section starts on a new page and ends with a summary box plus self-check · blanks sized to the
expected answer.

**Assessments** — every item maps to a learning target · distractors are real misconceptions ·
exactly one unambiguously best answer · parallel versions carry identical blueprints, standards
coverage, and point totals.

**Labs** — every formula appears with its name · percent error wherever an accepted value exists,
and the accepted value is supplied · **no write-lines, answer spaces, or data tables on the handout**
where the course uses lab notebooks · no invented safety claim.

---

## Reporting

A short checklist. Findings as a table, sorted blocking first, then by how long the fix takes:

| # | Check | Problem | Fix | Severity |
|---|---|---|---|---|

Severity is **blocking** (student-facing error, wrong science, unreadable print) · **should-fix**
(brand drift, inconsistency) · **nice-to-have** (polish).

**If any check fails, the deliverable is INCOMPLETE.** Do not report WORK COMPLETE.
