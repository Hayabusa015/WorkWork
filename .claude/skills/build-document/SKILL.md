---
name: build-document
description: Build SHULL print documents - practice sets, guided and Cornell notes, study guides, reference sheets, graphic organizers, and cut/colour/glue activities. Produces a student file plus a separate key where the document has answers.
---

# build-document

## The production path

```bash
python3 templates/notes/build_notes_docx.py templates/notes/specs/<spec>.json out.docx
```

**`.docx`, chosen by the user 2026-09-09** (SHULL-CHG-0014) — guided notes are the one document he
edits after the fact, and a PDF cannot be changed at 7:40 a.m. For a fixed-layout copy, convert the
built `.docx` with `soffice --headless --convert-to pdf`. `build_notes.py` (Option B, HTML to PDF)
still exists, but it reads only the old flat spec and draws the old layout. It cannot render a
paged spec.

Structure, and why: `templates/notes/README.md`. The content lives in a JSON spec; the builder
checks the section code against that course's `DECISIONS.md` before building anything.

**Every packet is measured before it ships:**

```bash
python3 scripts/audit_print_ink.py out.pdf     # convert the .docx first
python3 scripts/audit_fonts.py out.pdf         # Archivo only, or it names the character
```

`audit_fonts.py` is the enforcement of the rule this repo states in four places and, until
SHULL-CHG-0019, checked in none: DejaVu or Liberation in `pdffonts` means the substitution did not
take and the classroom copy has different metrics from the one that was checked. It names the
character, because one U+2610 checkbox pulls in a whole second font.

No solid-fill headers, no shaded section backgrounds. This is measured, not judged — the first
build of the template ran 3.2× the ink of the packet the user had written by hand.

The check reports **toner** (ink volume, the budget), **marked** (page density, reported) and
**the widest solid band in inches** (the thing the standard actually fails). Do not read any one as
another. A page of dense small type puts down as many dark pixels as a bar does — an early version
confused those two and wrongly failed the lab template. And a pale tint marks every pixel it covers
while spending almost no toner — reading `marked` as the ink budget was the second confusion, and
it ranked a tinted sheet worse than one using 74% more ink. SHULL-CHG-0020.

Design: `brand/SHULL_DESIGN_SYSTEM.md`. Voice: `standards/VOICE.md`. Naming: `standards/NAMING.md`.

## Every document

1. **Confirm the code exists** in `courses/<course>/DECISIONS.md`. Stop and ask if not.
2. Read that course's decisions file for its conventions — they differ more than you expect.
3. Build. 4. Run `anti-ai-slop`. 5. Run `audit-deliverable`.

**Ruled lines are for prose. Open boxes are for math.** This holds everywhere.

## Worksheets and practice sets

```bash
python3 templates/worksheet/build_worksheet_docx.py specs/<spec>.json out.docx
python3 scripts/audit_worksheet.py out.docx specs/<spec>.json
python3 scripts/audit_fonts.py out.pdf
```

Structure and the three course profiles: `templates/worksheet/README.md`. The profiles are
enforced at build time, not described — a Physics spec carrying a work box is refused.

**The ramp.** Difficulty never goes backwards, and the multi-topic problem is last. Physics holds
his shipped shape exactly: **2 warm-up / 2 practice / 1 challenge / 1 multi-topic**, six per
section. Chemistry has the order enforced and picks its own counts.

> The earlier figure here — exactly 8 questions, 2/3/2/1, strictly two pages — was **INHERITED**
> from the legacy studio skill and never confirmed. His own `SHULL_PHYS_Practice_Sets_U01.docx`
> runs 2/2/1/1 across all four sections. The artifact won. SHULL-CHG-0019.

**Tier tags carry no box and sit in their own right-aligned column**, so every prompt starts on
one edge. His existing Physics sheet fills them — light blue warm-up, solid navy multi-topic — and
sets each question number in a solid navy square. Both are section 8 violations and the square is
the withdrawn number-box (SHULL-CHG-0015). An outlined boxed tag was tried first and he rejected it
on sight: a run border cannot be padded, so at 7pt it clamps to the cap height, and four tiers in
four border weights read as a rendering fault rather than a scale.

Work boxes carry a faint **SHOW WORK HERE** watermark, at `print.watermarkOpacityPct`.

**Every calculation carries its answer except the last question** (SHULL-CHG-0021) — the last one
they finish without a net, and the builder refuses a self-check on it. Bracketed answers are for
**numeric results only**, never for explanation, vocabulary, or graph-reading, which is why the
spec marks a question `"calculation": true` rather than the builder guessing from its wording.
Multi-part items keep full body size on every part.

**The page budget is declared in the spec** (`pagesPerSection`) and measured against. It is not one
number for everybody: a Physics section is one page, a Chemistry section with eight work boxes is
four, a cut-and-glue activity is two by construction. The failure is a section that *grows* a page,
not a section that was always three.

> **Physics carries no work areas at all** — no ruled lines, no work boxes. A prior-knowledge and
> equations reminder block goes at the top instead. Students work in their Hayden-McNeil carbonless
> lab notebooks. **Flag this whenever a request tries to reuse the Chemistry template unmodified
> for Physics.** Removing the work boxes took his own U01 packet from eight pages to four.

## Guided and Cornell notes

**The notes and the deck are one object.** A student should look at a slide and know exactly which
blank it fills. **Locate the section deck first.** If it does not exist, build it first or say the
notes are provisional.

Set the scaffolding level and **state the choice in one line** so it can be overridden. The ladder
comes down across the year; the per-course index is in each decisions file.

The packet is a set of designed pages, **one sheet each** (layout: SHULL-CHG-0025; headers:
SHULL-CHG-0030). It opens with a cover carrying the SHULL-CHG-0014 packet opening: the
course-colour school line, unit title and `GUIDED NOTES · PHASE nn · N SECTIONS` kicker over a
course-accent rule, Name/Date/Period, unit learning targets ∥ key terms, how these notes work, and
the sections-in-this-unit checklist, plus the cover image and the equation toolbox. Each section
in the checklist carries a **1–10 difficulty rating**. It is a standard cover feature, and the
values are course content supplied in the spec. Cover text the spec does not give is derived only
from the spec itself, and the build lists what it derived. Nothing is invented. Each section
starts on a new page, **opened by the section title bar** (title, `U01 / S01.2` code, course-accent
rule) and its **`LEARNING TARGET` line**. Continuation pages carry no head. A section usually spans
two pages of about three open two-column blocks. Each block has a course-colour cue label and, where it
differs, a notes heading, and **no block number**. Colour is a thin accent only: rules in the course `primary`,
label type in `primaryDeep`, never a fill. Every section ends with a **RECALL block** (summary prompt plus
self-check). The packet closes on a **Concept Review** page. Cue questions carry no writing line.
Worked problems use `Given:` / `Find:` and an open bordered work box, at least 1.4 in tall — **never
ruled lines.** Build with `--verify` so a spilled page fails the build. Layout, schema, and why:
`templates/notes/README.md`. Blanks are sized to the expected answer; a one-word blank and a
full-sentence blank must not look identical. Leave a margin note where a common misconception
lives, named plainly.

**Always two files** — student copy and filled key — generated from the same source so they cannot
drift.

## Geology activities

**Not every Geology assignment is a cut-and-glue.** SHULL-CHG-0022 — he said so directly. The
default is a one-page sheet: a diagram to label, a `match` grid, a `sort` (order it in place, write
the number in the box, no scissors), and one written question. Cut-and-glue is worth two pages and
a pair of scissors *sometimes*, and it is not the shape a Geology sheet should fall into by
default.


Foldables, cut-and-sequence, diagram labelling and colouring, graphic organizers as a *primary*
note-taking format. **Clear fold lines, generous cut margins, print-safe non-bleeding colour
regions** — these have to survive scissors and glue in a 50-minute period.

## Page budget

If over: `@page` margins → base font size → line-height → block margins. **In that order. Never
shrink a single question to fit.**
