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
edits after the fact, and a PDF cannot be changed at 7:40 a.m. `build_notes.py` renders the same
spec to PDF if a fixed-layout copy is ever wanted.

Structure, and why: `templates/notes/README.md`. The content lives in a JSON spec; the builder
checks the section code against that course's `DECISIONS.md` before building anything.

**Every packet is measured before it ships:**

```bash
python3 scripts/audit_print_ink.py out.pdf     # convert the .docx first
```

No solid-fill headers, no shaded section backgrounds. This is measured, not judged — the first
build of the template ran 3.2× the ink of the packet the user had written by hand.

Design: `brand/SHULL_DESIGN_SYSTEM.md`. Voice: `standards/VOICE.md`. Naming: `standards/NAMING.md`.

## Every document

1. **Confirm the code exists** in `courses/<course>/DECISIONS.md`. Stop and ask if not.
2. Read that course's decisions file for its conventions — they differ more than you expect.
3. Build. 4. Run `anti-ai-slop`. 5. Run `audit-deliverable`.

**Ruled lines are for prose. Open boxes are for math.** This holds everywhere.

## Practice sets — locked v2 shape

Exactly **8 questions**: 2 warm-up / 3 practice / 2 challenge / 1 multi-topic.
**Strictly two pages**, enforced by a page-count check.

Tag pills in four tiers, separated by **border colour as well as fill** so they survive a
photocopier. Work boxes carry a border-tab label sitting *on* the border, not floating grey text
inside. Bracketed self-check answers for **numeric results only** — never for explanation,
vocabulary, or graph-reading. Multi-part items keep full body size on every part.

> **Physics carries no work areas at all** — no ruled lines, no work boxes. A prior-knowledge and
> equations reminder block goes at the top instead. Students work in their lab notebooks.
> **Flag this whenever a request tries to reuse the Chemistry template unmodified for Physics.**

## Guided and Cornell notes

**The notes and the deck are one object.** A student should look at a slide and know exactly which
blank it fills. **Locate the section deck first.** If it does not exist, build it first or say the
notes are provisional.

Set the scaffolding level and **state the choice in one line** so it can be overridden. The ladder
comes down across the year; the per-course index is in each decisions file.

Every section starts a new page and ends with a summary box plus self-check. Worked problems use an
open bordered box with a faint prompt — **never ruled lines.** Blanks are sized to the expected
answer; a one-word blank and a full-sentence blank must not look identical. Leave a margin note
where a common misconception lives, named plainly.

**Always two files** — student copy and filled key — generated from the same source so they cannot
drift.

## Geology activities

Foldables, cut-and-sequence, diagram labelling and colouring, graphic organizers as a *primary*
note-taking format. **Clear fold lines, generous cut margins, print-safe non-bleeding colour
regions** — these have to survive scissors and glue in a 50-minute period.

## Page budget

If over: `@page` margins → base font size → line-height → block margins. **In that order. Never
shrink a single question to fit.**
