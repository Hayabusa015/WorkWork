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
| **Decision** | **Approved 2026-09-09 — Option A, the `.docx`.** He also required the headers to follow the print ink rule; see finding 4. |
| **Status** | **IMPLEMENTED** |

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

**Chosen: A, the `.docx`.** Guided notes are the one document a teacher edits after the fact —
dropping a line for one class, adding a diagram, adjusting for a modified copy. Option B is more
precise on the page, but a PDF cannot be changed at 7:40 a.m. The lab template stays HTML→PDF
because a lab handout is shipped as printed, not edited.

Option B stays in the repo. The spec is the source and a second view of it costs nothing.

---

## Finding 4 — I added ink his packet never had, and it was measurable

**He caught this: "make sure headers follow the low low printer ink rule."** He was right, and the
standard already said so — `SHULL_DESIGN_SYSTEM.md` §8: *"no full-page colour banners, no shaded
section backgrounds, no solid-fill headers."*

The first build had solid asphalt bars across the brand header, all three section heads, and the
close banner, plus parchment shading on every cue column and the callout box. **His original packet
has no cell fill anywhere** — the extraction found zero `w:fill` values. He had been following the
ink rule by hand, before this system existed.

`standards/QA_GATE.md` §5 says the check is computable — *"rasterise and compute the percentage of
marked pixels"* — and nothing computed it. `scripts/audit_print_ink.py` now does.

| | marked | heavy | worst page |
|---|---|---|---|
| **His original packet** | 5.41% | 2.80% | 8.35% / 3.97% |
| **My first build** | **17.10%** | **4.32%** | **26.74% / 9.21%** |
| **After the fix** | **6.18%** | **2.22%** | 8.31% / 3.34% |

**3.2× his ink**, on a document that gets photocopied for every student in the course.

Fixed by replacing every fill with a rule: the brand bar, section heads and close banner are now a
hairline above and a heavy accent rule below; the cue column is separated by its border alone, which
is the Cornell convention anyway. Hierarchy is unchanged. Both renderers were fixed, not just the
chosen one.

The checker's limits are calibrated to **his packet**, not to a number I picked — my first threshold
was arbitrary and failed his original too, which is how I knew it was wrong.

## Finding 5 — I reported the lab template as failing. It was not. The check was wrong.

**WITHDRAWN, and worth keeping on the record.**

The first version of `audit_print_ink.py` scored a "heavy" percentage — pixels below mid-grey — and
treated that as the fill test. On that basis the lab template failed at 4.96% heavy, and I told the
user so.

Then I looked at the page. **It has no fills at all.** It is five pages of dense procedure, and a
page of small dark type puts down as many dark pixels as a solid bar does. The metric could not tell
the two apart, and the standard fails *fills*, not ink volume.

Rewritten to measure the thing the standard actually names — *"any solid fill larger than a small
tag, chip, or icon"* — as geometry rather than volume. Text makes dark runs a glyph-stroke wide; a
bar makes one run hundreds of pixels wide, held down its height. The checker reports **the widest
solid band on each page, in inches.**

| | marked, worst page | widest solid band |
|---|---|---|
| His original packet | 8.35% | **none** |
| Lab template | 10.66% | **none** |
| Notes, after finding 4 | 8.31% | **none** |
| *Positive control* — notes with the old solid header put back | 14.01% | **7.50 in** |
| *Positive control* — a slide deck, dark grounds by design | 100% | 13.15 in |

The controls matter: a check that never fires is not a check. Both were run and both flagged.

**The lab template needs no change.** Finding 4 stands — the notes template really did add fills his
packet never had, and the ink measurement of that was correct. What was wrong was the conclusion
drawn about a second template from a metric that could not support it.

## Verification

Both renderers build from the same spec, check the section code against
`courses/geology/DECISIONS.md` before building, and were rendered and inspected page by page.
`pdffonts` run on both.
