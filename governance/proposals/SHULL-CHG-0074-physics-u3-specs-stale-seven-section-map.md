# SHULL-CHG-0074 — Physics U3 slide and solution specs still use the retired seven-section map

> **Blocking. Course-fact conflict.** `courses/physics/DECISIONS.md` wins (CLAUDE.md §2 precedence
> 2), so the specs are stale. This record does not resolve the conflict. Matt decides between
> retiring and remapping. Any rebuild is a classroom deliverable and routes through the Overseer
> (CLAUDE.md §6).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0074 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 1) |
| **Current Rule** | `courses/physics/DECISIONS.md` U3 (lines 35-36, SHULL-CHG-0068, 2026-11-11): "`3.1` Newton's Laws · `3.2` Free-Body Diagrams · `3.3` Forces on an Incline · `3.4` Net Force and Acceleration · `3.5` Friction · `3.6` Connected Objects". Same file, decision log: "the old `3.7` no longer exists. The course total is 47 sections." |
| **Proposed Rule** | No rule change. The specs are brought into line with the decisions file: the `3.7` deck and the `3.7` slide-solution entries are either retired or remapped onto the six-section map, as Matt chooses. |
| **Supersedes** | Nothing in the rule layer. Replaces stale course facts in the spec files listed below. |
| **Reason** | Specs from a 2026-11-04 branch, merged in the 2026-11-13 consolidation, still carry "3.7 Multi-Body Systems" and "Inclined Plane FBDs". The SHULL-CHG-0068 F5 grep ("no 3.7 found", 2026-11-11) ran before that merge and is no longer true. `validate_codes` fails on two of the files. A rebuild from these specs would print a section that does not exist. |
| **Affected Agents** | Overseer (entry point for any rebuild), Builder (rebuild), Auditor (post-build audit), Secretary (correct the F5 note on SHULL-CHG-0068 only if Matt approves). |
| **Affected Skills** | build-presentation, build-document (solutions). |
| **Affected Courses** | Physics. |
| **Risk** | High. A student-facing deck could print a non-existent section code and title. |
| **Recommendation** | Matt chooses retire or remap (open question 1). Until then, do not build from any `phys_u03` deck or the slide-solutions spec. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

Drive was not checked this run (no connector). The seven old U3 Drive folders (03.1–03.7) are a
separate item already noted on SHULL-CHG-0068.

## Files

Confirmed by grep for `3.7|Multi-Body|Inclined Plane FBD` on 2026-11-22:

| File | Hits |
|---|---|
| `templates/slide/decks/phys_u03_s03.7.json` | 3 |
| `templates/slide/decks/phys_u03_all.json` | 9 |
| `templates/slide/decks/phys_u03_s03.3.json` | 2 |
| `templates/slide/decks/phys_u03_specs.py` | 5 |
| `templates/worksheet/specs/phys_u03_slide_solutions.json` | 4 |
| `templates/worksheet/specs/phys_u03_slide_solutions.py` | 3 |

Not listed by the Janitor but also matched: `templates/slide/decks/phys_u03_combined.py` (1 hit).
It is not yet confirmed whether that hit is a U3 section reference.

## Open question

1. Retire the `3.7` deck and its slide-solution entries, or remap their content into the six-section
   U3 (for example into `3.6` Connected Objects and `3.3` Forces on an Incline)? The mapping is a
   course decision and is not guessed here.
2. Should the SHULL-CHG-0068 F5 verification note be annotated as invalidated by the 11-13 merge?
   That record is APPROVED; this sweep does not edit it.

## Researcher corroboration (2026-W47)

The Researcher reported the same finding independently (`reports/2026-W47/researcher.md` row 1). It adds:

- **The combined deck dodges the code check.** `templates/slide/decks/phys_u03_combined.py` declares
  `"section": "3.1"` "only to satisfy the build's code check" (its own note, line 22). Meanwhile every
  slide prints its own footer through `setdefault("code", f"U03 • S03.{n}")` (line 19), including
  `U03 • S03.7`. This settles the open item above: the hit in `phys_u03_combined.py` is a U3 section
  reference.
- **The approved ∑F switch would rebuild from these specs.** SHULL-CHG-0070 F1 (switch the U3 deck to
  ∑F, approved, not done) would print the dead codes if it ran before this record is resolved. Do the
  remap in the same pass as F1.
- **Correct SHULL-CHG-0068 F5.** Its "no 3.7 found" grep result is wrong.
- **Optional, separate proposal:** have `validate_codes.py` / `build_deck.js` also check per-slide
  `code` footers, not only the top-level `section`.
