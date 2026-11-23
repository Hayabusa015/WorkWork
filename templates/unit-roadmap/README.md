# Unit Roadmap

The one-page opener filed at the front of each unit's binder section. Document type `Roadmap`
(`standards/NAMING.md` §2, SHULL-CHG-0100). One builder for all three courses.

| File | What it is |
|---|---|
| `build_unit_roadmap.py` | Spec → HTML → PDF (WeasyPrint, like `templates/lab/`), with the checks below |
| `unit_roadmap.css` | Layout. Colours only through `../lab/shull-lab-tokens.css`; fonts from `brand/fonts/` |
| `specs/<course>_u<NN>.json` | One per unit. `chem_u06.json` is the first |

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

Spec text accepts `**bold**`, `_{sub}`, `^{sup}`, and `[[no line break]]` (keeps `-ate / -ite`
together).

## Checks the builder runs

1. The spec's sections and the decisions file's taught sections are the same set. A mismatch stops
   the build: a code is never built from a spec alone (CLAUDE.md §3).
2. Exactly one page. If it overflows, shorten the spec text; never shrink the type.

Then run the QA tools as for any print document: `scripts/audit_print_ink.py`,
`scripts/audit_fonts.py`, `scripts/validate_tokens.py`.

## Layout

Header (unit chip, course · phase, unit title with one accent word, teacher block) → Big Idea and
Builds On → section table (number box, title, focus | I-can checklist | standards, bold box = main,
dashed box = supporting) → standards key and "How Learning Is Measured" → running footer with the
`U# / S#.#` range. Outline treatments only; no solid fills (`brand/SHULL_DESIGN_SYSTEM.md`, ink rule).
