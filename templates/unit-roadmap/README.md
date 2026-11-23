# Unit Roadmap

The one-page opener filed at the front of each unit's binder section. Document type `Roadmap`
(`standards/NAMING.md` §2, SHULL-CHG-0100). One builder for all three courses.

| File | What it is |
|---|---|
| `build_unit_roadmap.py` | Spec → HTML → PDF (WeasyPrint, like `templates/lab/`), with the checks below |
| `unit_roadmap.css` | Layout. Colours only through `../lab/shull-lab-tokens.css`; fonts from `brand/fonts/` |
| `specs/<course>_u<NN>.json` | One per unit. Chemistry has all sixteen, `chem_u00`–`chem_u15` |
| `build_course_outline.py` | The one-page Course Outline (SHULL-CHG-0106): every unit by phase with its taught sections |
| `course_outline.css` | Outline layout, loaded after `unit_roadmap.css` (same fonts, page box and type sizes) |

## Build

```
python3 templates/unit-roadmap/build_unit_roadmap.py templates/unit-roadmap/specs/chem_u06.json
```

Writes `output/<course>/u<NN>/Unit N Roadmap[ - Short Title].pdf` (and the HTML beside it). The topic
is the unit's row in the course "Short titles" table; with no row the name has no topic.

## What comes from where

A fact lives in one place, so the spec does **not** carry:

- **Unit title, phase, section codes and titles**: read from the curriculum map in
  `courses/<course>/DECISIONS.md`. Retired, dropped and folded codes are skipped.
- **Colours and type**: `brand/tokens.json`, through the generated lab token stylesheet.

The spec carries only what is particular to the page: big idea, builds-on list, each section's
focus line, I-can statements and standards (main and supporting), the standards key, and the
"How Learning Is Measured" lines. Those lines must agree with "Assessment shape" in the course
decisions file; if that changes, update the specs.

**Standards are optional.** A spec whose sections carry no `standards` (omitted or `null`) prints no
standards column, standards key or bold/dashed legend; the I-can column widens and "How Learning Is
Measured" spans the bottom (Chemistry U15: no Chemistry content statement covers nuclear chemistry).
A spec with standards must give them on every section (`{"main": [...], "support": [...]}`; either
list may be empty, which leaves that cell blank) plus `standards_label`, `standards_source` and
`standards_key`. The legend shows only the box kinds the page uses. Chemistry codes and key wording
follow `reports/chem-ohio-standards-verification.md`.

A backticked marker in a curriculum-map title (`9.5 Spontaneity \`EXT\``) prints as a small outline
tag, never as backticks.

Spec text accepts `**bold**`, `_{sub}`, `^{sup}`, and `[[no line break]]` (keeps `-ate / -ite`
together).

## Checks the builder runs

1. The spec's sections and the decisions file's taught sections are the same set. A mismatch stops
   the build: a code is never built from a spec alone (CLAUDE.md §3).
2. Exactly one page. If it overflows, shorten the spec text; never shrink the type.

## Course Outline

```
python3 templates/unit-roadmap/build_course_outline.py chemistry
```

Writes `output/<course>/reference/Reference - Course Outline.pdf` (and the HTML). Everything comes from
the curriculum map through the same parser as the roadmaps: phases, units, taught sections, `EXT`
tags. Retired, dropped and folded codes are left out. The unit and section counts in the header are
counted, not typed. No dates, quarters or pacing. The build stops if `Course Outline` is not a `REF`
row in the course Short titles, and fails unless the page count is exactly 1.

Then run the QA tools as for any print document: `scripts/audit_print_ink.py`,
`scripts/audit_fonts.py`, `scripts/validate_tokens.py`.

## Layout

Header (unit chip, course · phase, unit title with one accent word, teacher block) → Big Idea and
Builds On → section table (number box, title, focus | I-can checklist | standards, bold box = main,
dashed box = supporting) → standards key and "How Learning Is Measured" → running footer with the
`U# / S#.#` range. Outline treatments only; no solid fills (`brand/SHULL_DESIGN_SYSTEM.md`, ink rule).
