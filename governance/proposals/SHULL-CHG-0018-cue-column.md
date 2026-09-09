---
id: SHULL-CHG-0018
title: The cue column narrows and condenses; the equation bar loses its box
status: IMPLEMENTED
opened: 2026-09-09
decided: 2026-09-09
decided_by: Matthew Shull
---

# SHULL-CHG-0018 — Cue column, equation bar

## What he asked for

> "in the notes. why are the prompt columns so damn big. those should be on the left side and
> rather small and condensed."

and, on the equation bar built under SHULL-CHG-0017:

> "i don't need a take around the equations / table"

## What was there

The Cornell split was 1.88 in / 5.62 in, copied from his own Geology packet (his Physics packet ran
2.00 in). The cue label was tracked-out caps at 7.5 pt and the prompts were 9 pt, so a two-word
label wrapped and a one-sentence prompt ran to four lines. The equation bar sat inside an accent
border.

## Decision

1. **The split is 1.28 in / 6.22 in.** The cue is a prompt, not a second body column. The half inch
   it gives back goes to the side students write on.
2. **The cue text condenses.** The label keeps caps, weight and accent colour but gives back its
   letter tracking — tracking is what made it wrap. Prompts drop 9 pt → 8.5 pt.
3. **No box around the equation bar.** The only rules on that block are the fraction bars, which
   are the point of it.

This is a change to his own packets' geometry, made on his instruction. It is recorded rather than
silently applied because the 1.88 in figure was documented as "preserved from the original" and that
sentence is no longer true.

## Mechanism, not documentation

- `CUE_W_IN` in `templates/notes/build_notes_docx.py` is the only place the split is decided.
  `NOTES_W_IN` and `NOTES_INNER_IN` derive from it, and every width on the notes side — work box,
  GIVEN/NEED row, diagram figure and label columns, the figure image itself — is measured off
  `NOTES_INNER_IN`. Moving the cue column again moves all of them.
- `SHULL_Notes_TEMPLATE.html` carries the same two numbers with a comment naming the Python
  constants, because the two renderers print the same page.

## Two defects found while verifying

- **The equals sign did not sit on the fraction bar.** `w:vAlign` was written and honoured; the
  cause was the blank paragraphs python-docx leaves around a nested table. They are full-size, they
  count toward the row height, and the vertically centred `v  =` centred against that padding. Fixed
  by `unpad_cell()`: the leading blank is removed and the trailing one — which Word requires — is
  collapsed to 1 pt. Confirmed in the render, not assumed from the XML.
- **The fraction bar was sized by a character-count guess** (`0.085 × len + 0.20`), padded wide so a
  term could never wrap inside it. It now measures the term against the shipped Archivo metrics, the
  same source `audit_slide_geometry.py` uses, and adds an optical 0.16 in.

## Also fixed here

Option B silently dropped `problem`, `equations` and `diagram` — a worked-example row rendered as an
empty cell and the build reported success. Option B now refuses such a spec and names Option A.
A renderer that cannot print what the spec asks for says so.

## Verification

- Both packets rebuilt and read at 100 dpi: cue column narrow, no wrapped labels, equals signs on
  their bars, diagram block widened with the notes column.
- `scripts/audit_print_ink.py` — Physics 8.76% marked at worst, Geology 8.30%, widest solid band
  0.00 in in both. Under the 12% budget and the 0.60 in fill limit.
- `scripts/hook-validate.sh` clean.
