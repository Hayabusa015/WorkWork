# templates

Build sources for generated documents. Each family has its own folder and its own README; the
detail lives there, not here.

| Folder | Builds | Read |
|---|---|---|
| `slide/` | Section decks (`.pptx`) on the twelve-layout masters | `slide/README.md` |
| `worksheet/` | Worksheets and practice sets (`.docx`) with a separate key | `worksheet/README.md` |
| `notes/` | Guided / Cornell notes, student copy and key from one spec | `notes/README.md` |
| `lab/` | Lab handout and teacher prep-and-key (HTML to PDF) | `lab/README.md` |
| `practice/` | Course activity prototypes | `practice/build_practice.py` |
| `snow_day/` | Snow-day packets | `snow_day/build_snow_day_docx.py` |

`_shull_docx.py`, `_shull_name.py` and `shull_name.cjs` are shared helpers: document furniture and
the filename rule from `standards/NAMING.md`.

Colours reach a template only through a file generated from `brand/tokens.json`
(`slide/tokens.generated.js`, `lab/shull-lab-tokens.css`, and the builders' own token reads).
**Never hand-edit a generated file or type a hex here.** Change the token and re-run the generator
listed in `scripts/README.md`.

One builder serves all three courses. A course that needs a different colour is a token change,
never a fork of the builder.
