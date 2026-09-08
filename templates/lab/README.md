# SHULL Lab Document Template

**Adapted from** `_Brand/Templates/Lab/README_Lab_Template.md` (v1.0, 2026-09-07).
Structure preserved per spec Part 17. **Palette section corrected** — see SHULL-CHG-0010.
Verbatim original: `legacy/drive-standards/` is for superseded standards; this template is a live
build input, so the original text is quoted in the change record rather than snapshotted here.

Built from `SHULL_CHEM_U0_S0.3_Intro_Skills_Lab`. **That lab's structure is the standard**; this is
that structure with the content lifted out.

---

## Status

| File | State |
|---|---|
| `build_lab.py` | Migrated from Drive, verified working |
| `SHULL_Lab_TEMPLATE_MASTER.html` | **v1.1** — migrated byte-exact from Drive, then moved onto the token system |
| `SHULL_Lab_TEMPLATE_TEACHER_KEY.html` | **v1.1** — same |
| `shull-lab-tokens.css` | **Generated** by `scripts/build_lab_css.py` from `brand/tokens.json`. Do not hand-edit. |

Verified end to end: both files render, `pdffonts` shows Archivo, and page 1 of the master
measures **5.2% of pixels marked, 2.4% heavy** — at the SHULL ink benchmark.

### What changed from Drive v1.0

Structure, wording, blocks, and the locked rules are **untouched**. Only brand values moved:

| v1.0 | v1.1 |
|---|---|
| Poppins / Liberation Sans | `var(--display)` / `var(--body)` → Trade Gothic Next → Archivo → Liberation Sans |
| Deep Forest | `var(--ink)` |
| Moss Green | `var(--accent)` — the course text-safe deep variant |
| Warm Earth | `var(--warn)` / `var(--warn-rule)` — semantic, not brand |
| Parchment as light ground | White. Parchment survives only as the SVG liquid fill. |
| "the print palette is identical for all three courses" | **False now.** The `<body>` course class drives a real accent. |

The `<body class="chem\|phys\|geo">` hook was described in v1.0 as changing "nothing visual today."
**It now does.** Setting it switches `--accent` to that course's `primaryDeep`.

### Known exception

Seven literal hexes remain inside the hand-built SVG diagram, because
`var()` does not resolve in SVG presentation attributes under this renderer. They are the only
hand-typed hexes permitted in this directory and `validate_tokens.py` must allow them.

---

## The five-minute version

1. Copy the two HTML files and rename them to the `standards/NAMING.md` grammar:

   ```
   SHULL_CHEM_Lab_U01_S01.4_Isotope_Beans.html
   SHULL_CHEM_Lab_U01_S01.4_Isotope_Beans_Key.html
   ```

   *Note the zero-padded section code — `S01.4`, not `S1.4`. The original README predates
   SHULL-CHG-0007.*

2. Set the course class on `<body>`: `chem`, `phys`, or `geo`.

3. Fill every `[[ TOKEN ]]`. Search for `[[` to find them all. Delete any block you don't need —
   each is labelled `BLOCK:` in a comment.

4. Render:

   ```
   python3 templates/lab/build_lab.py SHULL_CHEM_Lab_U01_S01.4_Isotope_Beans.html
   ```

   It writes the PDF, lists any token you missed, and reports the page count. Pass an expected page
   count as a second argument to make the budget a hard check.

5. File the PDF in
   `[Course]/Unit ## - [Name]/Section ##.# - [Name]/Labs-Case Studies-Projects/`.

---

## What's locked and why

**Margins.** Per `brand/tokens.json` → `print.margins`. **Don't touch them to fix a page-count
problem** — reduce body font size or line-height first.

**Ink.** Outline and rule treatments only. No solid banners, no filled table headers, no shaded
section backgrounds. Number squares and chips are outlined, not filled. This is the standing rule
for every printed SHULL document, not a choice made for this template.

**No write space on the handout.** No ruled lines, no answer blanks, no fillable data tables. **The
lab notebook is the write-on surface and the carbonless copy is what gets graded.** The pre-lab
makes students draw their own tables — the table skeletons on page 2 exist to be copied, not filled.

**Colour** — *corrected from the original, which is superseded.* Values come from
`brand/tokens.json`. White is the ground. Course identity colours apply across all media, not
projection only. **Coloured type on a light ground uses the course `primaryDeep`** — the display
colours fail as text on white. The original README's base-palette paragraph and its "Physics
Kinetic" reference are archived in `brand/palette-archive/`.

**The `<body>` course class** stays a structural hook. It may now carry a real colour difference,
where it previously changed nothing visual.

**Alconox cleanup block.** Disposal items 4–6 are standing boilerplate. **Keep them verbatim.** Only
items 1–3 change per lab.

**The teacher key is its own file.** Never appended to the student handout.

---

## Student section order

Header (course, unit, section, lab code, Name/Date/Period, group line) → Topic/Goals → Purpose →
Background (only the theory needed) → **Safety** (specific PPE and named hazards, spill and exposure
response) → **Pre-Lab** (2–3 conceptual, 3–4 procedural-reading, at least one safety or disposal
check) → Materials → **Procedure** (numbered major steps, bulleted substeps, exact quantities,
times, temperatures, endpoints; formula name *and* formula) → Data/Observations → **Disposal and
Cleanup** (exact location and method) → **Post-Lab Analysis** (2–3 "what happened and why",
calculations with work and units, percent error with the accepted value supplied, error analysis
naming a real procedural cause).

## Teacher section

Materials per group and per class · solution recipes and concentrations · advance-prep timeline ·
room and equipment setup · expected duration by phase · safety and disposal notes · common failure
points · expected data range and observations · worked calculations and answers · cleanup and reset
checklist · Missed Lab Analysis guidance.

## Standing rules

- Fit one 50-minute period with five minutes reserved for cleanup.
- Every formula appears with its name.
- Percent error whenever an accepted value exists — **and the accepted value is always supplied.**
- **"Human error" is never an acceptable error analysis.**
- **Never invent a safety claim.** Flag uncertain handling or disposal for verification.
- Missed lab → a Missed Lab Analysis, not a re-run.

---

## Course notes

**Chemistry** — matches the confirmed lab template exactly.

**Physics** — same structure. Physics worksheets carry no work areas; labs never did either, so
nothing changes. Expect Background to lean harder on the governing equation and sign conventions.

**Geology** — most Geology work is activity-shaped rather than lab-shaped, so this template is mainly
for U3 rocks-and-minerals identification. A rock/mineral lab may use a lighter form — goal, brief
background, procedure and ID steps, data table, a few analysis questions — without the full pre-lab,
safety, and disposal apparatus unless a real hazard is present. **Specimen photographs for
identification are shot, never generated.**

---

## Before it goes to the copier

- [ ] Rendered and **looked at** every page. Clipped text is the defect that hides.
- [ ] Zero unfilled `[[ tokens ]]` — the build script reports these.
- [ ] `U#/S#.#` matches the document chip, the running footer, the filename, and the folder path.
      One system.
- [ ] The code exists in that course's `DECISIONS.md`.
- [ ] Every chemical hazard and disposal route verified against the SDS and district policy. **Never
      state a disposal limit you haven't checked.**
- [ ] Every calculation in the key solved independently, not pattern-matched.
- [ ] Safety bullets name a specific hazard *and* the behaviour that controls it.
- [ ] Photocopy test: would the categories still read in grayscale?

Full gate: `standards/QA_GATE.md`.

---

## Open items this template does not resolve

- **Lab placements past Chemistry Unit 0 are PROVISIONAL.** Building a U9 calorimetry or U14
  titration lab means confirming the lab exists in the pacing before it ships as final rather than
  draft.
- The Bunsen burner lighting station addition to the U0 Intro Skills Lab is still open.
- *Resolved since the original was written: Physics now has a confirmed unit and section map, so
  Physics labs can carry a valid code.*
