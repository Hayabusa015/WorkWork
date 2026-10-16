# scripts — enforcement

| Script | Fails the build when |
|---|---|
| `validate_layers.py` | A course fact (unit title, section code, calendar date, grading percentage) appears in a skill |
| `validate_codes.py` | A `U#/S#.#` code appears anywhere without existing in the matching `courses/*/DECISIONS.md` |
| `validate_tokens.py` | A raw hex value is typed outside `tokens.json` |
| `find_session_files.py` | — read-only; lists documents created this session, for `reconcile-session-files` |
| `publish_standards.py` | — publishes `standards/` and `brand/` to Drive `_Brand/Standards/`, one direction only |

| Generator | Writes | From |
|---|---|---|
| `build_app_css.py` | `app/public/tokens.generated.css`, `app/public/icon.svg` | `brand/tokens.json` |
| `build_template_previews.py` | `app/public/previews/` — a page image per document template, plus `catalog.json` | each template's own builder |
| `build_diagram_molecule.py` | A branded structure figure (`--out` path) with formula and molar mass | a SMILES string, via RDKit; colours from `brand/tokens.json` |

Both write build artifacts. Never hand-edit one; re-run the script. `build_app_css.py --check`
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

*Status: not yet written. Phase 9.*

`key_ink.py` is a drawing helper for handwritten-look teacher keys (SHULL-CHG-0043): pencil and pen
text, stacked fractions, boxes, arrows, strike-throughs, and a pencil-grain sketch layer. Colours come
from the `keyInk` tokens; it is used by key builders, never run on its own.

`science_tools.py` is a shared helper (not a validator or generator): optional access to RDKit,
mendeleev and pint, plus brand tokens and fonts. mendeleev is a cross-check only; its values
are never a source for a student page.
