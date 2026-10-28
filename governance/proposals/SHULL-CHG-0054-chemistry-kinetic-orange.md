# SHULL-CHG-0054 — Chemistry palette: Lab Lime + Aqua replaced by Kinetic Orange

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0054 |
| **Date** | 2026-10-28 |
| **Source** | User, 2026-10-28. The user supplied a reference image of the "Kinetic Orange" palette and asked for Chemistry's colours to be swapped to it. |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | See section 2. |
| **Supersedes** | `brand/tokens.json` `courses.chemistry.primary` (Lab Lime, source "SHULL-CHG-0002 context; spec Part 8"), `courses.chemistry.secondary` (Aqua, source "spec Part 8") and `courses.chemistry.primaryDeep` (Lab Lime Deep, source "SHULL-CHG-0008"). Also `courses/chemistry/DECISIONS.md` decision-log entry "2026-09-07 — Palette" (Status: CONFIRMED · SHULL-CHG-0002 context, SHULL-CHG-0008). That entry is superseded by a new entry. It is not edited (CHANGE_CONTROL section 5: "Never edit history; append"). |
| **Reason** | The user, verbatim: *"It just works better for me."* |
| **Affected Agents** | Secretary (implements). Designer and any agent that builds Chemistry artifacts use the new tokens through the generated CSS and JS. No agent file restates the Chemistry palette (checked by Grep of `.claude/`). |
| **Affected Skills** | None restate it (Grep of `.claude/` for lime, aqua, kinetic, energy orange, ice blue: no hits). `apply-shull-design` points at `rules.grayscaleSeparationMin` and is unchanged. |
| **Affected Courses** | Chemistry (identity colours). Geology and all-course surfaces are affected indirectly through risk 1. |
| **Risk** | Medium. See section 3. Risk 5 was found while drafting and is not in the original brief. |
| **Recommendation** | Implement as requested, with the risks in section 3 put to the user first. Before approving, the user needs to answer the one question in section 5: the status of the derived `primaryDeep`. Optional follow-up, the user's choice only: if two oranges bother them in practice, shift Chemistry's secondary or Geology's Rust Orange. That would need its own record. |
| **Decision** | **Approved by the user, 2026-10-28**, in the main session. Verbatim: *"I want to swap the color pallette of chemsitry to kinetic orange. It just works better for me. Approve file change color"*. The user did not answer the section 5 question, so `primaryDeep` is PROVISIONAL per that section. Recorded under SHULL-CHG-0034. |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

---

## 1. Current Rule (verbatim)

### 1a. `brand/tokens.json`, `courses.chemistry`, lines 123-167 (the authoritative statement)

```json
      "primary": {
        "hex": "#A3E635",
        "name": "Lab Lime",
        "status": "LOCKED",
        "use": "display",
        "source": "SHULL-CHG-0002 context; spec Part 8",
        "measured": {
          "grayscale": 190,
          "onWhite": 1.51,
          "onWhiteVerdict": "NOT TYPE - fill, rule, border or block only",
          "onParchment": 1.31,
          "onAsphalt": 12.0,
          "onAsphaltVerdict": "body text, AAA"
        }
      },
      "secondary": {
        "hex": "#22D3EE",
        "name": "Aqua",
        "status": "LOCKED",
        "use": "display",
        "source": "spec Part 8",
        "measured": {
          "grayscale": 161,
          "onWhite": 1.81,
          "onWhiteVerdict": "NOT TYPE - fill, rule, border or block only",
          "onParchment": 1.57,
          "onAsphalt": 10.01,
          "onAsphaltVerdict": "body text, AAA"
        }
      },
      "primaryDeep": {
        "hex": "#4D730E",
        "name": "Lab Lime Deep",
        "status": "LOCKED",
        "use": "text-on-light",
        "source": "SHULL-CHG-0008",
        "measured": {
          "grayscale": 92,
          "onWhite": 5.56,
          "onWhiteVerdict": "body text, meets SHULL target",
          "onParchment": 4.82,
          "onAsphalt": 3.25,
          "onAsphaltVerdict": "large text only (24px+, or 19px bold)"
        }
      },
```

### 1b. Restatements of that brand fact elsewhere

These say the same fact a second time. Under CLAUDE.md section 1 ("A fact lives in exactly one
place") each one is replaced with a pointer, or with wording that names no colour. The new colours
are not restated in any of them.

`README.md` line 63:

> | Chemistry | Lab Lime + Aqua |

`courses/chemistry/DECISIONS.md` line 314, section "Course brand exceptions" (live text):

> **None.** Chemistry uses Lab Lime + Aqua inside the shared system, per SHULL-CHG-0002 context.

`courses/chemistry/DECISIONS.md` lines 448-452, decision log (history, not edited):

> ### 2026-09-07 — Palette
> Chemistry is Lab Lime + Aqua , inside the shared system. Coloured type on a
> light ground uses Lab Lime Deep.
> Supersedes: the base SHULL palette for Chemistry.
> Status: CONFIRMED · SHULL-CHG-0002 context, SHULL-CHG-0008

`brand/SHULL_DESIGN_SYSTEM.md` lines 90-92, "Course identity overrides nothing":

> **Semantic colours are permitted even when they are not in the course palette.** A safety warning is
> red because it is a warning. Do **not** substitute a course colour to avoid using a semantically
> correct one — a Chemistry hazard note in Lab Lime is a defect, not brand consistency.

`templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` lines 28-30 (comment):

> · Print palette is the same for all three courses. The per-course
>   accent palettes (Lab Lime / Kinetic / Terra Teal) are PROJECTION
>   ONLY and never touch a printed page.

Student-facing text naming the colour, in three files:
`templates/notes/specs/chem_u01_s01.1-s01.5_notes_student.json` line 94,
`templates/notes/specs/chem_u01_s01.1-s01.5_notes_key.json` line 94 and
`templates/notes/specs/make_chem_u01_s01.1-s01.5_notes.py` line 62:

> "Quiz yourself with the left-column questions. Gray side rules mark must-write notes (lime blocks in the slides). Show your reasoning and units in each work box."

`templates/notes/build_notes_docx.py` line 548 (docstring):

> """A line the student must have in their notes - lime on the slide. A grey rule

Hard-coded in generated files. Each is regenerated, never hand-edited:
`templates/lab/shull-lab-tokens.css` lines 22-23 and 30, `templates/notes/shull-notes-tokens.css`
lines 22-23 and 30, `templates/slide/tokens.generated.js` lines 21-23,
`app/public/tokens.generated.css` lines 20-21, `app/public/icon.svg` line 7. `icon.svg` carries the
header `GENERATED FROM brand/tokens.json BY scripts/build_app_css.py - DO NOT EDIT`, so it is
regenerated by that script. It is not a hand edit.

## 2. Proposed Rule

### 2a. Edit 1 (brand layer, Path B): `brand/tokens.json` `courses.chemistry`

| Slot | Now | Proposed | Origin of the proposed value |
|---|---|---|---|
| `primary` | Lab Lime `#A3E635` | **Energy Orange `#FF6B1A`**, `use: display` | Supplied by the user's reference image |
| `secondary` | Aqua `#22D3EE` | **Ice Blue `#3DD6F4`**, `use: display` | Supplied by the user's reference image |
| `primaryDeep` | Lab Lime Deep `#4D730E` | **Energy Orange Deep `#B84100`**, `use: text-on-light` | **Derived, not supplied.** The image has no deep variant. The value was derived from Energy Orange's hue at reduced lightness, aiming for the 5.5 text target on white. |

- `source` fields: primary and secondary read `SHULL-CHG-0054; user reference image 2026-10-28`.
  primaryDeep reads `SHULL-CHG-0054; derived from Energy Orange, not user-supplied`.
- `status`: primary and secondary become LOCKED on approval, because the user supplied them.
  primaryDeep's status is the open question in section 5. The Secretary does not make it LOCKED on
  its own judgment.
- `measured` blocks are written by `scripts/measure_tokens.py` and never by hand. The top-level
  `updated` date is bumped.
- `icons` is unchanged.

The neutrals in the reference image are Asphalt Black and Graphite. They are the existing
`ground.asphalt` and `ground.graphite` tokens and are **unchanged**.

**Measurements computed while drafting.** These are not authoritative.
`measure_tokens.py` produces the authoritative values when the change is implemented.

| Token | Grayscale | On white | On asphalt | Verdict on white |
|---|---|---|---|---|
| Energy Orange | 142 | 2.85:1 | 6.35:1 | Not type. Fill, rule, border or block only |
| Ice Blue | 172 | 1.73:1 | 10.45:1 | Not type. Fill, rule, border or block only |
| Energy Orange Deep | 93 (target 5.5) | 5.53:1 | not computed while drafting | Body text, meets SHULL target |

The display pair is 30 grey levels apart, which clears `rules.grayscaleSeparationMin` (20). The
design-system sentence "four of the six stopped clearing WCAG as text on white and the other two
reached large-text-only" (`brand/SHULL_DESIGN_SYSTEM.md` lines 104-106) still holds: Chemistry's
pair moves from not-type/not-type to not-type/not-type.

Then regenerate: `scripts/build_app_css.py` (writes `app/public/tokens.generated.css` and
`app/public/icon.svg`), `scripts/build_lab_css.py` (writes lab and notes token CSS), and
`scripts/build_slide_tokens.py`.

### 2b. Edit 1, continued: restatements become pointers

| File | Proposed |
|---|---|
| `README.md` line 63 | `\| Chemistry \| Energy Orange + Ice Blue \|`. This uses names only, like the Physics and Geology rows. Hex values stay in `brand/tokens.json` (line 59 already says so). |
| `brand/SHULL_DESIGN_SYSTEM.md` line 92 | "...a Chemistry hazard note in the course primary is a defect, not brand consistency." The example no longer names a colour, so it cannot go stale again. The rule itself is unchanged and still governs: a warning keeps its semantic colour plus border and label. |
| `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` line 29 | Replace "(Lab Lime / Kinetic / Terra Teal)" with a pointer to `courses.*` in `brand/tokens.json`. See finding F-2 in section 4: the rest of this comment is stale for a separate reason, and that is **not** bundled into this change. |
| Three notes spec and generator files, "(lime blocks in the slides)" | Change to wording that names no colour, for example "(highlighted blocks in the slides)". The Secretary does not pick the exact student-facing phrase. The user confirms it at approval or the Designer proposes it. |
| `templates/notes/build_notes_docx.py` line 548 | "lime on the slide" becomes "course colour on the slide". Comment only. |

### 2c. Edit 1, continued: the old palette stays recoverable

- New file `brand/palette-archive/chem-lab-lime.md`. It preserves Lab Lime, Aqua and Lab Lime Deep
  with the three hex values and sources quoted in 1a, the dates the palette was authoritative
  (2026-09-07 to the implementation date), what superseded it (SHULL-CHG-0054), and the materials
  built on it (every finished Chemistry document on Drive as of the implementation date). Recording
  the materials stops the Janitor flagging those documents as defects later
  (`brand/palette-archive/README.md` lines 20-21).
- Add a row for it to the table in `brand/palette-archive/README.md`.
- Add a dated note to `brand/palette-archive/per-course-2026-09-06.md`, without editing its existing
  text, saying that the DEPRECATED Physics "Kinetic" hexes were revived for Chemistry by
  SHULL-CHG-0054. See finding F-1.

### 2d. Edit 2 (course layer): `courses/chemistry/DECISIONS.md`

CHANGE_CONTROL section 1 says a change touching both layers is split into two edits, each labelled.
This is the course-layer edit.

Line 314 (live text) becomes:

> **None.** Chemistry's identity colours are `courses.chemistry` in `brand/tokens.json`, inside the
> shared system (SHULL-CHG-0054). This file does not restate them.

A new entry goes at the **top** of the decision log (CHANGE_CONTROL section 5), with the date of
implementation:

> ### YYYY-MM-DD — Palette changed
> Chemistry's identity colours changed. Values live in `brand/tokens.json` `courses.chemistry`; the
> retired palette is preserved in `brand/palette-archive/chem-lab-lime.md`. Finished documents on
> Drive stay as built until rebuilt.
> Supersedes: 2026-09-07 — Palette (this log).
> Status: CONFIRMED · SHULL-CHG-0054

The 2026-09-07 entry stays exactly as written. The brief asked for lines 449-450 to become a
pointer. They are not edited, because they are history and section 5 forbids editing history. The
new entry supersedes them by name, and that is how the change shows up as visible drift rather
than silent drift.

### 2e. Commit

There is one commit carrying `SHULL-CHG-0054` (CHANGE_CONTROL section 6). Its message labels Edit 1
(brand) and Edit 2 (course) separately, as section 1 requires.

## 3. Risks

1. **Near-collision with Geology.** Geology's secondary, Rust Orange, measures grayscale 128
   (`brand/tokens.json` line 243). That is 14 grey levels from Energy Orange's 142, below the
   floor of 20, and the hue is nearly the same. The floor applies to two colours that carry a
   distinction. Course colours do not normally share one artifact, so this may not breach the rule
   as written. Cross-course surfaces will still show two oranges side by side: the app's course
   cards (`--course-chemistry` and `--course-geology-2` in `app/public/tokens.generated.css`) and
   any all-course overview. `measure_tokens.py`'s `pair_warnings` checks only within a course
   (lines 100-111), so it will not report this.
2. **Semantic proximity, display colour.** `semantic.caution` is amber (grayscale 167, 25 levels
   from Energy Orange). Chemistry carries the most safety notes because it has labs. An orange
   course accent next to amber caution notes weakens the "colour means warning" signal. The design
   system's "Course identity overrides nothing" (lines 88-92) still governs: warnings keep semantic
   colour plus border and label.
3. **Worksheet tiers.** Tier colours run "quiet grey → amber → red → full ink"
   (`templates/worksheet/README.md` line 58). On a Chemistry sheet the amber tier sits next to an
   orange accent.
4. **Nothing propagates on its own.** Finished Chemistry documents on Google Drive stay lime until
   rebuilt. The archived rule "New work only; no retrofit" (`per-course-2026-09-06.md` line 32)
   suggests they stay as built unless the user asks otherwise. The app's preview images
   (`app/public/previews/`, e.g. `worksheet-chem_u07_s07.4-*.png`) may show the old colours until
   `scripts/build_template_previews.py` is re-run. Already-printed U1 notes say "lime blocks in the
   slides".
   *Checked, no action:* `templates/notes/assets/chem_u01_cover_atom.png` is a greyscale atom
   rendering with no lime in it. It needs no follow-up.
5. **Semantic proximity, deep text colour (found while drafting, not in the brief).** The proposed
   `primaryDeep` is a dark red-orange at grayscale 93. `semantic.caution.deep` measures 83
   (`tokens.json` line 308), 10 levels away, and is also a dark orange-brown.
   `semantic.danger.deep` measures 75 (line 286), 18 levels away, and is a dark red. Both gaps are
   below the floor of 20. On white, Chemistry coloured type (headings, cue labels and notes headings
   use the course colour, per `templates/notes/build_notes_docx.py` lines 16-17) would sit near
   caution and danger labels in nearly the same hue and value. This is the same problem as risk 2,
   but for text, where border and label do less to separate them. Lab Lime Deep (green) did not
   have this problem.

## 4. Findings outside this change (not bundled)

- **F-1. This palette has been considered before.** Energy Orange and Ice Blue are exactly the hexes
  of the **Physics "Kinetic" palette** in `brand/palette-archive/per-course-2026-09-06.md` line 16,
  where it is marked **DEPRECATED**. Physics moved to Quantum Gold + Deep Purple under
  SHULL-CHG-0002. It was never a rejected *Chemistry* option, so reviving it for Chemistry is
  legitimate. The archive exists so that a revival is a choice made in the open, never one made by
  accident (`brand/palette-archive/README.md` lines 6-8), so it is stated here. The note in 2c
  records the revival.
- **F-2. The lab template comment is already stale.** Lines 28-30 of
  `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` call course accents "PROJECTION ONLY". That
  contradicts `templates/lab/README.md` lines 93-95 ("Course identity colours apply across all
  media, not projection only"). Its "Kinetic" also meant Physics, not Chemistry. This change
  replaces only the palette-name list with a pointer. The "projection only" contradiction should be
  its own proposal.

## 5. The question for the user

**Should the derived Energy Orange Deep `#B84100` be LOCKED on approval, or PROVISIONAL until it has
been seen on a printed Chemistry sheet?** The value was derived, not supplied, and risk 5 is about
this exact token. If the user wants it LOCKED, the approval should say so. Otherwise the Secretary
sets it PROVISIONAL.

## 6. Verification plan (for `Verified:`)

1. `python3 scripts/measure_tokens.py`, then `python3 scripts/measure_tokens.py --check`. Record the
   authoritative measurements, which replace the drafting values in 2a.
2. `python3 scripts/build_app_css.py --check`, plus `build_lab_css.py` and `build_slide_tokens.py`.
   The generated files must match `tokens.json`. Confirm `app/public/icon.svg` no longer carries the
   old primary.
3. `validate_tokens.py`, `validate_layers.py`, `validate_references.py`, `validate_schemas.py`,
   `validate_agents.py`, `validate_codes.py`, `validate_notes.py`, `validate_profiles.py`: all OK.
4. Grep outside `legacy/`, `docs/`, `reports/`, `governance/proposals/`, `brand/palette-archive/`
   and `change-log/` for "Lab Lime", "Aqua" (as a colour), "lime" (as a colour) and the three old
   hex values. Expect no hits except the superseded decision-log entry.
5. Rebuild one Chemistry worksheet **and** one Chemistry notes packet, render both to PDF, and
   check them by eye: accent and coloured type are visible, the amber tier and any caution note
   still read as warnings, and the page survives a greyscale view.
