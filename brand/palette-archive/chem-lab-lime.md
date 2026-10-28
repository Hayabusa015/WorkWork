# ARCHIVED — Chemistry "Lab Lime" + Aqua

**Status:** SUPERSEDED · **Superseded:** 2026-10-28 by SHULL-CHG-0054 (the Chemistry tokens now in
`brand/tokens.json` `courses.chemistry`)
**Was authoritative in:** `brand/tokens.json` `courses.chemistry`, 2026-09-07 to 2026-10-28.
Before that, the 2026-09-06 per-course memo (`per-course-2026-09-06.md`, row "Chemistry"), whose
hexes spec Part 8 carried forward.

| Token | Slot | Hex | Grey | Status when retired | Source |
|---|---|---|---:|---|---|
| Lab Lime | `primary`, display | `#A3E635` | 190 | LOCKED | SHULL-CHG-0002 context; spec Part 8 |
| Aqua | `secondary`, display | `#22D3EE` | 161 | LOCKED | spec Part 8 |
| Lab Lime Deep | `primaryDeep`, text-on-light | `#4D730E` | 92 | LOCKED | SHULL-CHG-0008 |

The grey values are the `measured.grayscale` figures `scripts/measure_tokens.py` wrote for these hexes
before retirement. Measured on white: Lab Lime 1.51:1, Aqua 1.81:1 (both fill, rule, border or block
only), Lab Lime Deep 5.56:1 (body text, meets SHULL target).

## Why it was replaced

The user, 2026-10-28, verbatim: *"It just works better for me."* Full reasoning and risks are in
`governance/proposals/SHULL-CHG-0054-chemistry-kinetic-orange.md`.

## To restore it

Put the three rows above back into `brand/tokens.json` `courses.chemistry`, run
`scripts/measure_tokens.py` and the `build_*` token generators. This needs its own change record.

## Materials built on it: leave as they are

Every Chemistry document finished before SHULL-CHG-0054 was implemented, including all Chemistry
worksheets, guided notes, labs and slide decks on Google Drive under `SHULL Science/`, was built
on Lab Lime and Aqua. **The individual Drive files have not been listed yet.** That list needs a
Drive inventory, which has not been run for this entry. The materials known in the repository are:

- the Chemistry U1 guided notes (`templates/notes/specs/chem_u01_s01.1-s01.5_notes_*.json`), whose
  student text says "lime blocks in the slides";
- the app's preview images of Chemistry builds in `app/public/previews/`.

Under the no-retrofit policy (`per-course-2026-09-06.md`, "Rules carried forward") these stay as
built and are **not** brand defects. Ask the user before rebuilding any of them.
