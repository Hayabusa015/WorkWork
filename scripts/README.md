# scripts — enforcement

| Script | Fails the build when |
|---|---|
| `validate_layers.py` | A course fact (unit title, section code, calendar date, grading percentage) appears in a skill |
| `validate_codes.py` | A `U#/S#.#` code appears anywhere without existing in the matching `courses/*/DECISIONS.md` |
| `validate_tokens.py` | A raw hex value is typed outside `tokens.json` |
| `publish_standards.py` | — publishes `standards/` and `brand/` to Drive `_Brand/Standards/`, one direction only |

| Generator | Writes | From |
|---|---|---|
| `build_app_css.py` | `app/public/tokens.generated.css`, `app/public/icon.svg` | `brand/tokens.json` |
| `build_template_previews.py` | `app/public/previews/` — a page image per document template, plus `catalog.json` | each template's own builder |
| `build_app_icon.py` | `build/icon.ico` — the Windows app and installer icon | `build/icon-source.png` |

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
