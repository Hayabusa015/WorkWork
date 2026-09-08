---
name: build-lab
description: Build a SHULL lab handout and its separate teacher prep-and-key file from the locked template. Use for any lab, pre-lab, post-lab, missed-lab, or rock and mineral identification activity. Produces two HTML files rendered to PDF, page-budget checked and visually inspected.
---

# build-lab

Template: `templates/lab/`. Spec and locked rules: `templates/lab/README.md`.

**Do not redesign the lab template.** It is built from the confirmed Intro Skills Lab and its
structure is the standard.

## Procedure

1. **Confirm the code exists** in `courses/<course>/DECISIONS.md`. Stop and ask if not.
2. **Copy both files** — master and teacher key — and rename per `standards/NAMING.md`:
   `SHULL_CHEM_Lab_U01_S01.4_Isotope_Beans.html` and `..._Key.html`.
3. **Set the course class** on `<body>`: `chem` · `phys` · `geo`. This now drives the accent colour.
4. **Fill every `[[ TOKEN ]]`.** Search for `[[`.
5. **Delete blocks you do not need** — each is marked `BLOCK:` in a comment.
6. **Render:** `python3 templates/lab/build_lab.py FILE.html [expected_pages]`
7. **Rasterize and look at it.** Then run `audit-deliverable`.

## The rules that are not yours to change

- **No write space on the handout.** No ruled lines, no answer blanks, no fillable data tables. The
  lab notebook is the write-on surface and the carbonless copy is what gets graded. Table skeletons
  exist to be **copied**, not filled.
- **Two files, always.** The key is never appended to the handout.
- **The Alconox block** — disposal items 4–6 — is standing boilerplate. **Keep it verbatim.** Only
  items 1–3 change per lab.
- **Margins are locked.** Never adjust them to fix a page count; reduce body size or line-height.
- **Every formula appears with its name.**
- **Percent error wherever an accepted value exists** — and the accepted value is always supplied.
- **"Human error" is never an acceptable error analysis.**
- **Never invent a safety claim.** Flag uncertain handling or disposal for verification.
- Fit one 50-minute period with five minutes reserved for cleanup.

## Safety is the part to slow down on

Every hazard bullet names **the specific hazard and the behaviour that controls it.** Never generic.
Every chemical statement gets verified against the SDS and district policy **before the handout is
copied**, and the teacher key records that verification with a date.

Uncertain about a disposal limit? **Say so and stop.** A wrong disposal instruction is the worst
defect this system can ship.

## Course differences

**Chemistry** — the template matches the confirmed structure exactly.

**Physics** — same structure. Background leans harder on the governing equation and sign
conventions. Worksheets and labs both carry no work areas, so nothing changes.

**Geology** — most Geology work is activity-shaped, not lab-shaped. This template is mainly for the
U3 rocks-and-minerals identification work, and may run lighter: goal, brief background, procedure
and ID steps, data table, a few analysis questions — without the full pre-lab and disposal apparatus
unless a real hazard is present. **Specimen photographs for identification are shot, never
generated.**

## Still open

Lab placements past Chemistry Unit 0 are PROVISIONAL. Building a U9 calorimetry or U14 titration lab
means confirming the lab exists in the pacing **before it ships as final rather than draft.**
