# scripts — enforcement

| Script | Fails the build when |
|---|---|
| `validate_layers.py` | A course fact (unit title, section code, calendar date, grading percentage) appears in a skill |
| `validate_codes.py` | A `U#/S#.#` code appears anywhere without existing in the matching `courses/*/DECISIONS.md` |
| `validate_tokens.py` | A raw hex value is typed outside `tokens.json` |
| `validate_agents.py` | An agent's `tools:` grant does not match the authority matrix in `governance/GOVERNANCE.md` |
| `validate_schemas.py` | `task-report.schema.json` or `change-proposal.schema.json` accepts something it should reject (or rejects something valid) |
| `validate_references.py` | Any file points at a repository path that does not exist |
| `validate_notes.py` | A guided-notes spec asks a question instead of stating recall content (SHULL-CHG-0023) |
| `validate_profiles.py` | A worksheet course profile doesn't actually refuse what it claims to refuse |
| `audit_fonts.py` | A rendered PDF uses any face but the brand face |
| `audit_print_ink.py` | — read-only; measures marked/heavy ink coverage on a print document |
| `audit_slide_geometry.py` | A built deck has colliding or clipped text, type below the 16pt floor, or a contrast failure |
| `audit_worksheet.py` | — read-only; measures pages-per-section and print ink on a built worksheet |
| `find_session_files.py` | — read-only; lists documents created this session, for `reconcile-session-files` |
| `publish_standards.py` | — publishes `standards/` and `brand/` to Drive `_Brand/Standards/`, one direction only |
| `desk_export.py` | — read-only; exports `governance/proposals/*.md` as a JSON batch for the Secretary's Desk dashboard's `proposals` collection. The records are authoritative; this only reads them. |

| Generator | Writes | From |
|---|---|---|
| `measure_tokens.py` | Contrast and grayscale measurements, written back into `brand/tokens.json` | `brand/tokens.json` itself |
| `build_app_css.py` | `app/public/tokens.generated.css`, `app/public/icon.svg` | `brand/tokens.json` |
| `build_template_previews.py` | `app/public/previews/` — a page image per document template, plus `catalog.json` | each template's own builder |
| `build_diagram_molecule.py` | A branded structure figure (`--out` path) with formula and molar mass | a SMILES string, via RDKit; colours from `brand/tokens.json` |
| `build_diagram_nuclear_notation.py` | The carbon-14 nuclear-symbol / hyphen-notation figure for CHEM U01 S1.4 | `brand/tokens.json` |
| `build_lab_css.py` | `templates/lab/shull-lab-tokens.css` | `brand/tokens.json` |
| `build_slide_tokens.py` | `templates/slide/tokens.generated.js` | `brand/tokens.json` |
| `repack_pptx.py` | Recompresses a `.pptx` — pptxgenjs writes its zip almost uncompressed | the `.pptx` itself |
| `image_prompts.py` | Lists every unfilled image slot in a deck spec, with a prompt for each | a deck spec |
| `key_solution.py` | One question's worked solution in the key-handwriting face (SHULL-CHG-0043 Stage 2) | a solution spec; used by key builders, never run on its own |

All of these write build artifacts. Never hand-edit one; re-run the script. `build_app_css.py --check`
fails when the generated theme has drifted from the tokens, and is the reason
`validate_tokens.py` can keep the app under the same one-hex rule as the print templates.
`build_template_previews.py` needs the full build toolchain (python-docx, WeasyPrint, pptxgenjs,
LibreOffice, poppler); a family whose tools are missing is reported and skipped rather than
failing the run.

`legacy/` is excluded from every validator.

These three checks would have caught, respectively: the Chemistry skill that was ordered trimmed
and never was; the Geology numbering offset, before a packet printed with the wrong footer; and
every palette conflict in the system, all of which came from the same hex being typed into two
files by hand.

`_shullos.py` is the shared helper every validator above imports (repo-root resolution, the
never-scan list for `legacy/`, `docs/`, `governance/`). Not run on its own.

`hook-drive-guard.sh` is the PreToolUse hook gating Drive trash operations behind logged, explicit
approval — Drive has no permanent delete, only trash, so trash is the destructive operation this
guards. `hook-validate.sh` is the Stop hook that runs every validator above before a session ends;
that is where drift actually gets caught. `setup-environment.sh` is the SessionStart hook that
builds the environment (fonts, Python toolchain) — idempotent, safe to re-run. All three are wired
in `.claude/settings.json`.

`build_handwriting_font.py` rebuilds ShullHand (`brand/fonts/ShullHand.ttf` and its alternates map) from the
committed scan in `brand/fonts/source/` (SHULL-CHG-0044). Routine regeneration; the command is in
`brand/fonts/README.md`.

`build_handwriting_sheet.py` writes the printable handwriting-capture sheet (PDF) and its layout manifest
(JSON), used to turn Matt's own handwriting into a key font. A tool, not a validator.

`key_ink.py` is a drawing helper for handwritten-look teacher keys (SHULL-CHG-0043): pencil and pen
text, stacked fractions, boxes, arrows, strike-throughs, and a pencil-grain sketch layer. Colours come
from the `keyInk` tokens; it is used by key builders, never run on its own.

`science_tools.py` is a shared helper (not a validator or generator): optional access to RDKit,
mendeleev and pint, plus brand tokens and fonts. mendeleev is a cross-check only; its values
are never a source for a student page.
