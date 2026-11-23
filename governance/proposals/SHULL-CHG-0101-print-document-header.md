# SHULL-CHG-0101 — One print document header for every builder

> **No conflict with a LOCKED rule.** The rail-and-hairline header every docx builder draws
> today is not written in `brand/SHULL_DESIGN_SYSTEM.md`; it is a copy-pasted convention
> (`borders(h, pal.display, sz=30, edges=("left",))` in six builders, a `.masthead` in three HTML
> templates). This writes the header down once and gives it one implementation per format.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0101 |
| **Date** | 2026-11-23 |
| **Source** | User. Matt, in conversation, 2026-11-23, about the header on the Unit 6 overview built outside WorkWork, verbatim: "I really like the header you made for this without the influence of work work. Could we update the work work headers with this heads but make the font a tad.smaller. maybe 30% smaller." |
| **Current Rule** | None written. In code: a 1-row table, heavy course-display rail on the left, hairlines top and bottom, eyebrow `UNIT N — TITLE` 7.5 pt, title 15 pt Archivo bold, code 11 pt and document type 6.5 pt on the right (`templates/worksheet/build_worksheet_docx.py` `header()`, and copies in the worksheet key, `templates/activity/_print_parts.py`, quiz, grader, question bank). HTML: `.masthead` in the lab master, lab key, missing-work template. |
| **Proposed Rule** | `brand/SHULL_DESIGN_SYSTEM.md` §11, "The document header": left, an outlined code chip and a `COURSE · DOCUMENT TYPE` kicker in the course's text-safe colour, then the title in condensed capitals (Archivo Narrow) with one accent word; right, teacher, school and unit; under both, a double rule in the course display colour. Ruled, never filled. Values in `brand/tokens.json` `print.header`: title 17 pt, kicker 7.5 pt, meta 7 pt, teacher, school. One implementation per format: `templates/_shull_docx.py` `print_header()` and `templates/_shull_header.css`. |
| **Supersedes** | The unwritten rail header above, in every builder that draws one. |
| **Reason** | Matt prefers the header from the 2026-11-19 overview. He chose its layout plus the condensed title, keeping WorkWork's course colours ("Layout + condensed title font"), for all print documents ("All print documents"), sized so the header is no taller than the old one ("Reduce the font slightly to made the height of the old header"). Measured: old header 0.593 in, new 0.600 in at 17 pt (LibreOffice render, 150 dpi). Also removes six copies of one drawing, the defect CLAUDE.md §1 names. |
| **Affected Agents** | Designer (every print build), Auditor. |
| **Affected Skills** | apply-shull-design, build-document, build-lab, build-assessment: none restates the old header in a way checked by grep for `sz=30` or `masthead` (not exhaustive). |
| **Affected Courses** | All three. |
| **Risk** | Medium. Page budgets: same height, so page counts should hold; verified per builder in the implementing commit. Filed documents are not retrofitted. Guided notes are out of scope: their page opener is the SHULL-CHG-0038 section bar, measured by the notes pager; changing it is a follow-up. One-off builders for already-filed documents (Physics U2 test/quiz/study-guide set, the two Gizmo sheets, the U2 electron set, `build_u02_assessments.py`, `build_phys_u02_s2.1_front_back.py`, `build_quiz_s22_docx.py`) keep their own header until they are next used. |
| **Recommendation** | Approve. |
| **Decision** | Approved by the user in chat, 2026-11-23: "All print documents" and "Layout + condensed title font", answering "Which WorkWork documents should get the new header?" and "What did you like about the original header: the look (layout), or also its fonts and colors?"; then "Reduce the font slightly to made the height of the old header than move ahead with the filing", answering the plan and preview. Recorded by the main session (§4.1). |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `ae93fe3`. Applied by the main session in the 2026-11-23 cloud session; the Secretary agent was not available there as a sub-agent. Review before merging to main. Out of scope as stated under Risk: guided notes (SHULL-CHG-0038 section bar) and the one-off builders for filed documents. |
| **Verified** | Yes. Header height 0.600 in vs 0.593 in (LibreOffice, 150 dpi). Fifteen documents rebuilt from the old and new trees (worksheets ×7, keys ×2, quiz, grader, question bank, Operation Periodic Table activity + key): page counts identical; three builds fail identically in both trees (pre-existing spec issues, not this change). Lab master 5 pages, lab key 2, missing-work 1 ×4 variants: unchanged. `templates/worksheet` tests 29/29. `validate_tokens` 51 problems before and after (none in changed files); `validate_references` OK; `validate_layers` no new findings. Rendered page 1 of each family and looked at it. |
