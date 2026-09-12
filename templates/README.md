# templates

Build sources for generated artifacts. Every builder here draws its drawing primitives — a work
box, a stacked fraction, a page that does not gain a trailing blank sheet — from
`templates/_shull_docx.py`, so "how a work box is drawn" is one fact and not a copy per builder.
Colour and type come from `brand/tokens.json`. No hex is hand-typed anywhere under `templates/`.

*Status, corrected 2026-09-12 — this file previously said the slide template had not migrated and
did not mention notes, worksheet, or assessment at all. Both were stale; see
`change-log/CHANGELOG.md`.*

| System | Format | Course coverage | Status |
|---|---|---|---|
| `lab/` | `.html` → PDF | template is generic across all three (a `<body>` course class hooks course rules) | **Implemented** — SHULL-CHG-0010, rendered/font-checked/ink-measured/inspected |
| `notes/` | `.docx` | Geology (U1 S1.2–1.4), Physics (U1 S1.1–1.4) — no Chemistry demo yet | Implemented, one course short of a demo on each course |
| `worksheet/` (practice sets) | `.docx` | all three have profile specs; several demo sheets | **Implemented** — SHULL-CHG-0019, three enforced course profiles |
| `slide/` | `.pptx` (twelve layouts) | Chemistry only (U1 S1.4 isotopes) | **Implemented** — SHULL-CHG-0013, token-driven (`tokens.generated.js` from `brand/tokens.json`); untested on Physics/Geology |
| `assessment/` | Day 1 `.txt` item bank + Day 2 `.docx` | Chemistry only (U7 S7.1–S7.4 demo) | **New** — build scripts exist, one course demoed; Physics has no assessment-shape section yet, Geology's shape is unbuilt |

`node build.js` in `slide/` regenerates all twelve layouts from a token change; `build.js` selects
its token module from `process.env.SHULL_TOKENS` so a course palette variant supplies its own file
rather than forking the build. That indirection is the best engineering carried over from the
legacy system — preserve it.

See each subdirectory's own `README.md` for its course profile rules, page grammar, and the
specific things its build-time validator refuses.
