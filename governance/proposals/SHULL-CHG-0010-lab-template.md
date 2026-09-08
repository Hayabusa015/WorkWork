# SHULL-CHG-0010 — Adopt the existing lab template

| Field | Value |
|---|---|
| **Date** | 2026-09-08 |
| **Source** | User decision |
| **Resolves** | The `build-lab` skill's source material question |
| **Current Rule** | No lab skill exists. Spec Part 17: preserve the structural strengths of the existing lab template, apply the approved visual system, and flag conflicts before changing major structure. |
| **Proposed Rule** | **`build-lab` is built on the existing lab template in `_Brand/Templates/Lab/`**, not redesigned. |
| **Supersedes** | Nothing — this fills a gap |
| **Affected Skills** | `build-lab` |
| **Affected Courses** | All three |
| **Risk** | Medium — see the two findings below |
| **Decision** | Approved by the user |
| **Status** | **PARTIALLY IMPLEMENTED** |
| **Implemented By** | `templates/lab/build_lab.py`, `templates/lab/README.md` |
| **Verified** | `build_lab.py` migrated and executed successfully — token detection and the page-count check both fire correctly. |

## Finding 1 — the HTML template files do not exist

`README_Lab_Template.md` describes five files in `_Brand/Templates/Lab/`:

| File | Present in Drive |
|---|---|
| `build_lab.py` | **yes** |
| `README_Lab_Template.md` | **yes** |
| `SHULL_Lab_TEMPLATE_MASTER.html` | **no** |
| `SHULL_Lab_TEMPLATE_TEACHER_KEY.html` | **no** |
| `SHULL_Lab_TEMPLATE_MASTER_PREVIEW.pdf` | **no** |
| `SHULL_Lab_TEMPLATE_TEACHER_KEY_PREVIEW.pdf` | **no** |

Two of six exist. **The template itself — the thing that would be copied and filled — is not there.**

This is the same defect class as CONFLICT-14: a README describing files that were specified and
never created, or created and never saved. It is the eleventh such broken reference found.

**Consequence:** "use the existing lab template" cannot mean copy it. What exists is a **complete
specification** of it, plus a working renderer. The template HTML must be authored to that spec.
That is a build task, not a migration, and it is flagged as such rather than presented as recovery
of an existing asset.

## Finding 2 — the template's palette section is superseded

`README_Lab_Template.md` states, under "What's locked and why":

> *"Print palette is identical for all three courses. Deep Forest, Moss Green, Warm Earth, Bio Lime,
> Parchment. The per-course accents (Chemistry Lab Lime, Physics Kinetic, Geology Terra Teal) are
> projection-only and never reach paper."*

Three parts of that are now false:

| Template says | Now |
|---|---|
| Base palette on print | White is the default ground; the base palette is archived (CHG-0002/0003) |
| Per-course accents are projection-only | Course colours apply to **all media** |
| Physics is "Kinetic" | Physics is Quantum Gold + Deep Purple (CHG-0002) |

Per spec Part 17 this is **flagged, not silently changed.** The structure is preserved; the palette
is re-derived from `brand/tokens.json`.

## What is adopted verbatim — the structural strengths

- **Two files, always.** Student handout and teacher key are separate. The key is never appended.
- **Token-based fill.** `[[ TOKEN ]]` placeholders; the build script reports any left unfilled.
- **`BLOCK:` comments** mark optional sections so they can be deleted cleanly.
- **A `<body>` course class** — `chem`, `phys`, `geo` — as a hook for course-specific rules without
  re-editing existing labs.
- **Locked margins**, matching the SHULL print standard. Never adjusted to fix a page-count problem;
  reduce body font size or line-height first.
- **Ink discipline** — outline and rule treatments only.
- **No write space on the handout.** No ruled lines, no answer blanks, no fillable data tables. The
  lab notebook is the write-on surface and the carbonless copy is what gets graded. The pre-lab makes
  students draw their own tables; the table skeletons exist to be copied, not filled.
- **The Alconox cleanup block** — disposal items 4–6 are standing boilerplate, kept verbatim. Only
  items 1–3 change per lab.
- **The pre-copier checklist**, which folds into `standards/QA_GATE.md`.

## Course notes carried forward

**Chemistry** — the template matches the confirmed structure exactly. Percent error whenever an
accepted value exists, and the accepted value is always supplied.

**Physics** — same structure. Physics worksheets carry no work areas and labs never did either, so
nothing changes. Expect Background to lean harder on the governing equation and sign conventions.

**Geology** — most Geology work is activity-shaped rather than lab-shaped, so this template is mainly
for the U3 rocks-and-minerals identification work. **Specimen photographs for identification are
shot, never generated.**

## Open items the template records and does not resolve

- Lab placements past Chemistry Unit 0 are PROVISIONAL.
- The Bunsen burner lighting station addition to the U0 Intro Skills Lab is still open.
- *(The template's third open item — "Physics has no unit/section map" — is resolved. Physics has 11
  units and 48 sections.)*

---

## RESOLUTION — 2026-09-08

**Finding 1 is closed.** The four missing files were uploaded to `_Brand/Templates/Lab/` at
00:45 on 2026-09-08. All four now exist. Both HTML templates were migrated into
`templates/lab/` **byte-exact** — 27,231 and 8,936 bytes, matching Drive.

The template is well-built and the voice is unmistakably Matt's: *"'It changed' is not an
observation." · "Never scribble it out and never erase — I need to see what you originally
recorded." · "Goggles come off last, once the whole room is finished — not once you are."*
Nothing in it was rewritten.

**Finding 2 is resolved as predicted.** Rendering v1.0 unmodified confirmed the conflict
empirically: `pdffonts` reported **DejaVu Sans and Liberation Sans**. The template asks for
Poppins, which is not installed, so it silently fell back to a font nobody chose — the exact defect
CHG-0006 describes, reproduced on a real document.

### The migration

`scripts/build_lab_css.py` generates `templates/lab/shull-lab-tokens.css` from `brand/tokens.json`,
so no hex is hand-typed. The two templates now reference custom properties.

After: `pdffonts` reports **Archivo, Archivo-Medium, Archivo-SemiBold, Archivo-Bold**, and page 1
measures **5.2% marked / 2.4% heavy** — matching the SHULL ink benchmark.

Rasterized and inspected, both pages. Safety headings render in the semantic amber rather than a
course colour, which is Part 9 behaving correctly: *course identity does not override semantic
meaning.*

### Two things recorded, not fixed

1. **The master renders 5 pages; its own comments describe a 4-page document.** With tokens in place
   of real content that may resolve on its own, but a filled lab should be page-budget checked —
   `build_lab.py` takes an expected count as its second argument for exactly this.
2. **`5.2` / `5.4` in the Geology map** remains open and unrelated to this template.

| Field | Value |
|---|---|
| **Status** | **IMPLEMENTED** |
| **Verified** | Rendered, font-checked, ink-measured, and visually inspected at 110 dpi. |
