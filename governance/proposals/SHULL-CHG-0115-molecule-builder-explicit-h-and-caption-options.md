# SHULL-CHG-0115 — Molecule builder: keep hydrogens, label every carbon, optional caption

> **No conflict with a LOCKED rule.** This extends the tool that SHULL-CHG-0042 requires. It does not
> change that rule. When no new flag is passed, output is unchanged. Nothing CONFLICT, PROVISIONAL
> or UNKNOWN is converted.
>
> **Why a record, when `scripts/` is not protected.** `scripts/build_diagram_molecule.py` is the tool
> that a LOCKED build rule names (SHULL-CHG-0042, carried in four build skills and the audit
> checklist). Changing what it can draw changes what that rule permits. That makes it a rule-bearing
> change, and CHANGE_CONTROL §§2–4 apply even though the file sits outside `brand/`, `standards/`,
> `governance/` and `courses/`.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0115 |
| **Date** | 2026-11-24 |
| **Source** | User, with an Auditor finding. Matt, main session, 2026-11-24, answered "Yes." to the Chemistry U7 unit-reading plan. Its decision D2 read: "Fix the shared molecule script so it keeps the hydrogens (your new rules say to use it). If the fix isn't ready in time, show formulas and molar masses without the drawings." The same gap is open as finding #2 in `reports/chem_u07_reading_audit.md`: "UNRESOLVED: pending Matt's decision. The options are: (a) extend `scripts/build_diagram_molecule.py` with an explicit-H / fixed-coordinate option and rebuild Figs 7.5 and 7.7 through it, or (b) record Matt's approval of the local routine as an exception." D2 chooses (a). That "Yes." approved the plan and the drafting of this proposal. It is not recorded here as approval of this record (see Decision). |
| **Current Rule** | **The rule (unchanged by this record):** SHULL-CHG-0042 §2.1: "any molecular structure appearing on a student-facing page is produced with `scripts/build_diagram_molecule.py` from a SMILES string. Never hand-drawn, never AI-generated, never a pasted web image. If RDKit cannot draw it well (large polymers, crystal lattices, etc.), stop and ask Matt — do not improvise." **The tool's current behaviour,** `scripts/build_diagram_molecule.py`: (1) line 59 parses with `Chem.MolFromSmiles(a.smiles)`, RDKit's default, which **removes explicit hydrogens**. Hydrogens on carbon are never drawn, and `[H]C#C[H]` comes out as a bare triple bond. Hydrogens on heteroatoms appear only as condensed labels (`OH`, `OH2`). (2) Carbons are **unlabelled**: skeletal convention, nothing sets `atomLabels`. (3) A fixed **caption block** is always drawn: `--name` (required) above the structure (line 96), a rule (line 99), the formula with subscripts (line 100) and the molar mass (lines 101–103). Only the mass can be turned off (`--no-mass`). (4) The canvas is fixed at 900 × 640 logical px × `SCALE` 4 = 3600 × 2560, with the structure panel at 3600 × 1600 pasted at y = 400. (5) Benzene from aromatic SMILES (`c1ccccc1`) is drawn Kekulé, alternating single and double bonds, because `MolDraw2D` kekulizes when it prepares the molecule. That is RDKit's default and the script does not override it. |
| **Proposed Rule** | Add three flags to `scripts/build_diagram_molecule.py`. **When none is passed, behaviour and output are unchanged.** (a) **`--explicit-h`** (off by default). After parsing, call `Chem.AddHs(mol)` so every hydrogen is drawn as its own atom with its own bond. Formula and molar mass stay computed from the same molecule, and `CalcMolFormula` gives the same result with or without explicit H. (b) **`--label-carbons`** (off by default). Set `drawOptions().atomLabels[idx] = "C"` for every carbon, so no vertex is left for the student to read as an implied C. This is for students who have not met skeletal drawings. (c) **`--no-caption`** (off by default). Skip the name, rule, formula and mass, and write the structure panel alone, cropped to the drawing. `--name` becomes optional **only** with `--no-caption`; without it, `--name` stays required. The script's stdout line (`wrote … <formula> <mass> g/mol`) is still printed with `--no-caption`, so the builder that places the figure can typeset the computed formula and mass beside it from the same molecule. One sentence goes in the script docstring and one in its `scripts/README.md` row, naming the three flags. **No skill text changes:** the skills say "built with `scripts/build_diagram_molecule.py` from a SMILES string", which stays true, and `--help` is the one place the flags are listed. |
| **Supersedes** | Nothing. Extends `scripts/build_diagram_molecule.py` (introduced with SHULL-CHG-0042). SHULL-CHG-0042 §2 is unchanged. Once implemented, the local `molecule()` routine in `templates/reading/specs/make_chem_u07_figures.py` (lines 179–214) is no longer needed. That routine exists today only because the shared builder strips H (its docstring, lines 13–18). Retiring it is the U7 rebuild's job, not this record's (see Follow-ups). |
| **Reason** | `workflows/unit-textbook.md` (Chemistry row of the page-decisions table) says "Use the repository molecular-structure builder where applicable", and SHULL-CHG-0042 says every structure on a student page comes from it. Textbook figures for students meeting structures for the first time need every atom shown: H₂O with both H, C₂H₂ as H–C≡C–H, C₆H₆ drawn Kekulé with all six C and all six H. The shared builder cannot draw these, so the U7 build made a local copy of its drawing code with `removeHs = False` and per-carbon labels. That is the drift SHULL-CHG-0042 exists to stop: a second molecule drawer, outside the rule. The caption option is needed because a textbook figure is captioned by the page (figure number, caption text, formula and mass in the adjoining prose, per `workflows/unit-textbook.md` "Words and figures"). The builder's own name/formula block would print the label twice. |
| **Affected Agents** | Textbook Page Designer and the other builder agents (consumers of the new flags), Auditor (the SHULL-CHG-0042 audit line can now be met for textbook figures, with no exception), Overseer (routes the U7 rebuild). |
| **Affected Skills** | None edited. `build-presentation`, `build-document`, `build-lab`, `build-assessment` and `audit-deliverable` cite the script by path. The citation stays correct. |
| **Affected Courses** | All three. The tool is shared. In practice Chemistry, starting with the U7 unit reading. |
| **Risk** | Low. Default output is unchanged, and the regression check below compares it against a pre-change render. Known limits, stated so they are not mistaken for defects: (1) **Bond angles are RDKit's 2D layout.** Water with explicit H draws near 120°, not 104.5°. The U7 local routine fixes this with hand-set coordinates. A `--coords` option is **not** part of this record (see Open question). (2) **Size.** Output stays 3600 px wide. Placed in a 3.5 in column at 300 dpi (1050 px), the 34 × 4 px atom labels come out at about 9.5 pt, matching the 9.5 pt the U7 routine uses, so no size flag is proposed. Bond lines thin to about 2.3 px at that scale. If they print too light, line width is a later tuning change, not part of this record. (3) **Crowding.** `--explicit-h` on a large molecule can clutter the drawing. That is a builder's judgement, and SHULL-CHG-0042's "if RDKit cannot draw it well, stop and ask" still applies. |
| **Recommendation** | Approve. If approved, the change is better implemented by the **main session** than by the Secretary or the Textbook Page Designer, with the Secretary filling in `Implemented By` and `Verified`. Reasons: `scripts/` is not a protected directory, so the Secretary-only write rule does not bind. The Textbook Page Designer's charter limits it to "assigned textbook artifacts" and bars it from changing "system rules", and this shared tool is cited by four skills. A builder should also not verify its own tool change: the H-count check should be run or re-run by someone other than whoever wrote the code (an Auditor pass, or the main session if the designer wrote it). |
| **Decision** | 2026-11-24, user, in the main session, answering "Approve SHULL-CHG-0115, the molecule script's three optional switches (keep hydrogens, label carbons, no caption)? It's already built in one commit and changes no existing drawing.": "Approve it". (Supersedes the earlier recording of a plan-level "Yes.", which did not approve this record.) |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

---

## Affected files

| File | Change |
|---|---|
| `scripts/build_diagram_molecule.py` | Three flags as above. Docstring gains one sentence naming them. `--name` required unless `--no-caption`. |
| `scripts/README.md` (line 28 row) | The "what it makes" cell adds: "optional explicit H (`--explicit-h`), every C labelled (`--label-carbons`), structure only (`--no-caption`)". |

Nothing in `brand/`, `standards/`, `governance/` (apart from this record and its changelog row),
`courses/` or `.claude/` changes.

## Verification plan

Run on the implementation commit by someone other than its author. Record the results in `Verified`.

1. **Default unchanged.** Before the change, render
   `--smiles "CC(=O)O" --name "acetic acid" --course chemistry` and keep the PNG. After the change,
   run the same command with no new flag. The stdout line must be identical
   (`3600x2560  C2H4O2  60.052 g/mol`, as SHULL-CHG-0042's verification recorded), and the two
   PNGs must be pixel-identical (`PIL.ImageChops.difference(...).getbbox() is None`).
2. **H counts, with `--explicit-h --label-carbons --no-caption`:**

   | SMILES | Expected drawing | Check |
   |---|---|---|
   | `O` | H–O–H | 3 atoms drawn: 1 O, 2 H. Formula H2O, 18.02 g/mol |
   | `C#C` | H–C≡C–H | 4 atoms: 2 C labelled, 2 H. Formula C2H2, 26.04 g/mol |
   | `c1ccccc1` | Kekulé ring, alternating double bonds, each C labelled, one H on each C | 12 atoms: 6 C labelled, 6 H. Three double bonds visible. Formula C6H6, 78.11 g/mol |

   **How to check:** (i) A short check script counts `a.GetSymbol() == "H"` on the molecule that is
   actually passed to `DrawMolecule`, and compares the count with the H subscript in the printed
   formula. They must match, for each of the three. (ii) A person opens each PNG and counts the H
   labels and the C labels by eye. The visible count must match the table. A count that matches only
   in code is not a pass. (iii) For benzene, confirm the ring is drawn Kekulé, not as a circle.
3. **Flags apart.** `--explicit-h` alone on `C#C` draws the two H with **unlabelled** carbons.
   `--label-carbons` alone on `CC(=O)O` labels both C, with no H on carbon. `--no-caption` alone
   writes a structure-only PNG with no name text, rule, formula or mass, and the stdout line still
   carries the formula and mass.
4. **Required-argument rule.** Without `--no-caption`, omitting `--name` still exits with an argparse
   error. With `--no-caption`, `--name` may be omitted.
5. **Repository checks.** `python3 scripts/validate_references.py` passes. So does any test that
   imports or runs the script, if one exists at implementation time.
6. Fill in `Implemented By` with the commit SHA, and `Verified` with steps 1–5 and who ran them.

## Open question for Matt (does not block approval)

Should the builder also accept fixed atom positions (`--coords`), so water can be drawn at its real
104.5° angle as the U7 local routine does? This record leaves it out because D2 asked only for
hydrogens. If the answer is yes, it is a separate record.

## Follow-ups this record does not authorise

- **The U7 rebuild.** Rebuilding Figures 7.3, 7.5 and 7.7 through the extended builder, and deleting
  the local `molecule()` routine in `templates/reading/specs/make_chem_u07_figures.py`, is classroom
  work. It routes through the Overseer (CLAUDE.md §6) and closes audit finding #2 there.
- **D2's fallback.** Matt's fallback ("show formulas and molar masses without the drawings") is a
  build decision inside the U7 plan. It needs no record and is not changed by this one.

## Not done by this record

No script, skill, standard or course file was edited. Implementation waits for a committed record
whose `Status:` reads APPROVED and whose `Decision:` quotes Matt verbatim
(`governance/CHANGE_CONTROL.md` §4). The main session records that decision.
