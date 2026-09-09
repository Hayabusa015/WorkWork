# SHULL-CHG-0014 — Guided / Cornell notes template

| Field | Value |
|---|---|
| **Date** | 2026-09-09 |
| **Source** | Matthew supplied the GEO U1 S1.2–S1.4 packet: *"here is the guided notes for geology I loved."* |
| **Resolves** | `build-document` had rules but no template and no builder — it could not produce a file |
| **Current Rule** | None. Guided notes were produced ad hoc by the legacy `shull-guided-notes-builder` skill. |
| **Proposed Rule** | **The structure of Matthew's GEO U1 packet becomes the guided-notes template**, restyled onto SHULL OS tokens. Two renderers are offered from one content spec; he picks. |
| **Supersedes** | Nothing — this fills a gap |
| **Affected Skills** | `build-document` |
| **Affected Courses** | All three |
| **Decision** | **PROPOSED — awaiting his choice of Option A or B** |

Legacy packet snapshotted at `legacy/guided-notes/`, md5 recorded.

---

## What is preserved

The structure is the asset and none of it was redesigned:

- **The Cornell split, 1.88 in cue / 5.62 in notes.** Pinned in both renderers.
- The section rhythm: header bar → learning target → Cornell rows → summary box.
- **The closed-notes summary** — "close your notes before you write this" — and the self-check.
- The unit wrapper: brand bar, name/date/period, targets ∥ key terms, "how these notes work",
  section checklist.
- The close: "pulling it together", checklist, big picture, **"still fuzzy on"**.
- Letter, 0.5 in margins, 7.5 in content width.
- **Trade Gothic Next** — already the locked SHULL face (SHULL-CHG-0006), so no conflict. The
  original used it for all 228 runs.

## Finding 1 — the palette is superseded

The packet uses a warm set that predates the current system: `3D2B1F` brown structure, `B5502F`
rust, `C77B2E` amber, `8A9A5B` sage. None survive SHULL-CHG-0003 and -0008.

| Original role | Was | Now |
|---|---|---|
| Structure, bars | warm brown | `ground.asphalt` |
| Section labels | rust | Geology `primaryDeep` (Terra Teal Deep) — text-safe on white |
| Eyebrow labels | amber | `primaryDeep` |
| **Must-write rule** | **sage green** | Geology `primary` (Terra Teal) — a fill/rule, never type |
| Cue column, callout | white | `ground.parchment` — the sanctioned callout surface |

**One line of his content had to change with it.** The packet told students *"Sage green lines are
must-write."* There is no sage green any more, so the instruction now reads *"A teal rule down the
left of a line means must-write."* Flagging it because it is his words, changed by me, on a page
students read.

## Finding 2 — two glyphs are not in Archivo

`✎` U+270E (the must-write marker) and `☐` U+2610 (checkboxes) both fall through the font stack.

- **`✎` is gone.** Must-write is now a prefix in the spec and the rule is drawn, not typed. The PDF
  embeds Archivo and nothing else.
- **`☐` survives in Option A only**, because a `.docx` cannot draw a box inline the way CSS can. It
  is the one glyph in the Word output that substitutes. Option B draws the box in CSS and embeds
  Archivo alone.

## Finding 3 — one packet, one must-write

I assumed the sage marker was used throughout and that reading text alone would lose most of them.
Checked the XML for the sage border rather than guessing: **the packet carries exactly one.** The
extraction lost nothing.

## The two options

Both build from **the same spec file**. Identical structure, identical content, identical tokens —
only the output differs. Whichever he picks, the other renderer stays in the repo, because the
spec is the source and a second view of it costs nothing.

| | **Option A — `.docx`** | **Option B — HTML → PDF** |
|---|---|---|
| Builder | `templates/notes/build_notes_docx.py` | `templates/notes/build_notes.py` |
| Editable in Word | **Yes** | No |
| Students can type into it | **Yes** | No |
| Layout holds exactly | Mostly — Word reflows, and the Cornell widths had to be pinned against autofit | **Yes** |
| Fonts | Archivo + one substituted glyph (`☐`) | **Archivo only** |
| Writing lines | Paragraph borders | CSS rules |
| Matches the lab template | Same tokens, different pipeline | **Same tokens AND same pipeline** |

**My recommendation: A, the `.docx`.** Guided notes are the one document a teacher edits after the
fact — dropping a line for one class, adding a diagram, adjusting for a modified copy. Option B is
more precise on the page, but a PDF cannot be changed at 7:40 a.m. The lab template stays HTML→PDF
because a lab handout is shipped as printed, not edited.

## Verification

Both renderers build from the same spec, check the section code against
`courses/geology/DECISIONS.md` before building, and were rendered and inspected page by page.
`pdffonts` run on both.
