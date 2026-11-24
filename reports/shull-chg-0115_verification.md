# SHULL-CHG-0115 — Independent verification

| Field | Value |
|---|---|
| Change ID | SHULL-CHG-0115 (molecule builder: `--explicit-h`, `--label-carbons`, `--no-caption`) |
| Commit verified | `f5d9d875ed0b136572825574d0a8df4706979cda` (HEAD of `claude/ecstatic-pascal-9cro1w`; working tree clean) |
| Parent compared | `f5d9d87^` (`3705a66`) |
| Verifier | Auditor (subagent). Not the author; the main session wrote the code |
| Date | 2026-11-24 |
| Environment | RDKit 2026.09.2; Archivo-SemiBold.ttf present (atom labels render in Archivo) |
| Scratch renders | `/tmp/claude-0/-home-user/3da17e47-8c6d-54ca-81fc-464404b893fa/scratchpad/aud/` |

**Overall verdict: PASS.** All five verification steps in the record pass. Nothing blocking or should-fix. Two nice-to-have observations below.

## Results

| # | Check (record's Verification plan) | Evidence | Result |
|---|---|---|---|
| 1a | Default stdout unchanged | New script, `--smiles "CC(=O)O" --name "acetic acid" --course chemistry`, prints `3600x2560  C2H4O2  60.052 g/mol`. Matches the record and SHULL-CHG-0042 | PASS |
| 1b | Default PNG identical to the main session's pre-change render | `ImageChops.difference(before_acetic.png, new_acetic.png).getbbox()` is `None`. SHA-256 identical (`c922b0ff…5fd5c`) | PASS |
| 1c | Extra check: parent script rendered here | `git show f5d9d87^:scripts/build_diagram_molecule.py`, run against the repo's `science_tools`. Same stdout. PNG pixel-identical and SHA-256 identical to both the new render and `before_acetic.png` | PASS |
| 2(i) | Code check: H atoms on the mol actually passed to `DrawMolecule` vs formula H subscript | Wrapped `MolDraw2DCairo.DrawMolecule` and captured its argument. `O`: 3 atoms, H=2, formula H2O → match. `C#C`: 4 atoms, H=2, C=2, formula C2H2 → match. `c1ccccc1`: 12 atoms, H=6, C=6, formula C6H6 → match | PASS |
| 2(ii) | By eye: H and C labels counted on each PNG | `water.png`: 2 H, 1 O, no C, two bonds. `acetylene.png`: H–C≡C–H, 2 C labelled, 2 H, triple bond. `benzene.png`: 6 C labelled, 6 H, one H on each C. All match the table | PASS |
| 2(iii) | Benzene drawn Kekulé, not as a circle | Three double bonds visible, alternating with single bonds. No inscribed circle. The kekulized mol has 3 DOUBLE, 3 ring SINGLE and 6 C–H SINGLE bonds | PASS |
| 2(iv) | Formula / mass values | Stdout `H2O 18.015`, `C2H2 26.038`, `C6H6 78.114` g/mol. These round to the record's 18.02 / 26.04 / 78.11 | PASS |
| 3a | `--explicit-h` alone on `C#C` | Both H drawn, carbons **unlabelled** (skeletal). Stdout `C2H2 26.038` | PASS |
| 3b | `--label-carbons` alone on `CC(=O)O` | Both C labelled "C" and no H on carbon. Checked both with `--no-caption` and with the full caption block | PASS |
| 3c | `--no-caption` alone on `CC(=O)O` | Cropped structure-only PNG (1668x1432). No name, rule, formula or mass. Stdout still carries `C2H4O2  60.052 g/mol`. Adding `--name` with `--no-caption` gives a pixel-identical PNG, so the name is ignored | PASS |
| 4a | No `--no-caption` and no `--name` → argparse error | `error: --name is required unless --no-caption is given`, exit 2, no file written | PASS |
| 4b | `--no-caption` and no `--name` → allowed | Exit 0, file written (steps 2 and 3c) | PASS |
| 5 | `python3 scripts/validate_references.py` | `308 file(s) checked  OK`, exit 0. No test imports or runs the script (only `test_key_solution.py` exists) | PASS |
| — | README row and docstring sentence (Affected files) | `scripts/README.md` row matches the record's wording exactly. The docstring names the three flags | PASS |
| — | Scope: only the files the record lists changed | Commit touches only `scripts/build_diagram_molecule.py` and `scripts/README.md` | PASS |
| — | Crop / clipping on `--no-caption` | The 48 px (12 x SCALE) margin holds on all renders. No label or bond is cut at an edge, including acetylene's outer triple-bond lines | PASS |
| — | Brand colour | Heteroatom accent is `primaryDeep` (#B84100, the Chemistry text-safe deep token), via `science_tools.palette`. H and C are Asphalt | PASS |

## Known limit (not a defect, per the record's Risk §1)

| Item | Observed |
|---|---|
| Water bond angle | RDKit's 2D layout puts H–O–H at **120.0°** (from `Compute2DCoords`; the render also measures about 120°), not the real 104.5°. A `--coords` option is outside this record (open question for Matt) |

## Observations (nice-to-have; none blocks)

| # | Check | Problem | Fix | Severity |
|---|---|---|---|---|
| 1 | Flag combinations for novice figures | `--label-carbons` without `--explicit-h` draws a methyl carbon as a bare "C" with no H. A student who has not met skeletal drawings could read that as an actual bare carbon. `--explicit-h` without `--label-carbons` on C#C draws H—≡—H, with the two carbons as invisible vertices on one long line. Each works as specified, but for first-exposure figures only the two flags together give an unambiguous picture | Builders and the Auditor should treat `--explicit-h --label-carbons` as the pair for first-exposure textbook figures. Optionally, a one-line note in `--help`. Route to the Overseer for the U7 rebuild brief; no record change is needed | nice-to-have |
| 2 | Default behaviour edge case | `--name ""` (empty string) used to be accepted by `required=True` and drew no title. It now fails with the argparse error. That is stricter and arguably correct, but strictly speaking it is a behaviour change on the default path | None needed. Recorded for completeness | nice-to-have |

## For the record's `Verified` field

Steps 1–5 run by the Auditor (non-author) on commit `f5d9d87`, 2026-11-24. All pass. The default render is pixel-identical to both the pre-change PNG and a fresh render from the parent script. H counts match the formula in code and by eye for water (2 H), ethyne (2 C, 2 H) and benzene (6 C, 6 H, Kekulé). Each flag behaves correctly on its own. The `--name` rule holds. `validate_references.py` is OK. Water draws at 120° (known limit).
