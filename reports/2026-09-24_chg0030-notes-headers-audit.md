# Audit — SHULL-CHG-0030 (old notes headers on the paged layout)

**Date:** 2026-09-24 · **Auditor:** independent pass, report only · **Against:** working tree over
HEAD `330fccf`; reference build from `0f3b078` (the SHULL-CHG-0014 template).

**Verdict: template change PASS.** No blocking defect introduced. Mechanical, regression and brand
checks all pass. Rows 2–5 are items the record reserves for the user; they do not block the commit.

| # | File | Problem | Your action | Time |
|---|---|---|---|---|
| 1 | `templates/notes/specs/phys_u01_s01.1-s01.4.json:321` | **Blocking for any Physics student copy — pre-existing, not 0030.** The worked-example answer line prints "meaning 29.7 m/s downward" beside the blanks. Present at 0f3b078, HEAD and in this build. | Designer: move it into the key's `solution` | 5 min |
| 2 | `build_notes_docx.py` `cover_content()` | Unit targets default to the section learning targets when a spec has no `unitTargets` (record §5 flag 2 reserves this for the user). Verbatim spec text, nothing invented. | User: keep the default, or show Key Terms full width | 2 min |
| 3 | `build_notes_docx.py` `label_of()` / `render_notes()` | Chemistry label mapping (title in caps as the cue label; notes heading only when it differs) has to be shown to the user (record §5 flag 3). | Show Chemistry p2 beside Geology p2 | 2 min |
| 4 | `build_notes_docx.py` cover | Chemistry `cover.sections[].blurb` descriptions no longer print; the unit targets take their place. | User: confirm in one line | 1 min |
| 5 | `templates/notes/specs/geo_u01_s01.2-s01.4.json:9` | Geology kicker prints "PHASE 01" from the spec; `courses/geology/DECISIONS.md` has no phases. | User: does Geology use phases? | 2 min |
| 6 | `SHULL-CHG-0030` §7 | This table stored here; commit, Implemented By and Verified to follow. Chemistry has no 0f3b078 spec, so its header check is against the 0014 design only. | Secretary: note the Chemistry exception in Verified | 10 min |
| 7 | Chemistry and Physics rules | Accent rules print pale on mono (lime and gold both ≈ grey 190). Disclosed in §5a; tokens are LOCKED; the ink rule keeps the hierarchy. | None | 0 |
| 8 | Per-page subtitles | Dropped, as choice c requires. | None | 0 |
| 9 | Geology cover | 4.92 in of 9.67 in, a consequence of choice b for a course with no image, toolbox or ratings. | Tell the user | 0 |
| 10 | `pad_codes` scope | Legacy REVIEW checklists still print unpadded codes ("S1.2, S1.3, S1.4"). Pre-existing text. | Designer: pad `close.checklist` | 10 min |
| 11 | `.claude/skills/build-document/SKILL.md` | Said every block has a notes heading. | **Fixed before commit** | — |
| 12 | `build_notes_docx.py` vs `README.md` | "Two corrections" vs "Three corrections". | **Fixed before commit** | — |
| 13 | Legacy worked examples | 0014's accent problem label is not restored (not one of 0030's five elements). | None unless the user asks | 0 |
| 14 | Scratch test builds | Test builds shared the delivered files' names. | **Renamed `TEST_ONLY_…` before commit** | — |

## What was verified

- **Headers against 0f3b078** (Geology and Physics, element by element): cover masthead, school line,
  unit title, kicker and accent rule; Name/Date/Period; targets ∥ key terms; "How these notes work";
  sections checklist; section title bar with the ink rule above, the accent rule below and the code
  at the right; `LEARNING TARGET` line; course-colour labels. Disclosed deviations: labels raised to
  the 8 pt floor, learning target closed by a hairline, codes zero-padded (SHULL-CHG-0007).
- **User choices a–d:** no fills and no new hex (`primary` used only as a border colour, type in
  `primaryDeep`, only fill is parchment `EDF0E5`); cover separate with the image, ratings and
  toolbox; a head only at the start of each section; no block numbers.
- **No 0025 regression:** a new page per section; RECALL, RECAP and REVIEW present; work boxes 1.4 in
  with `cantSplit`; the 0016 refusal exits 1 when `problem` is stripped (Chemistry and Physics); cue
  grid 1843/8957 twips; stacked fractions; bare numbers; Concept Review page; `--verify` 8/8/9/9.
- **Content honesty:** derived cover text is verbatim from the spec; the key matches the student
  copy; no answer leaks introduced (row 1 predates this change).
- **Standard checks:** Archivo only on all four PDFs; ink audit OK (worst page 3.99% toner, widest
  band 0.00 in); validators pass except the known `app/public/style.css` token failure; the
  worksheet regression is byte-identical to HEAD.
- **Delivered Chemistry notes untouched:** mtimes predate the change; SHA-256 values match.
