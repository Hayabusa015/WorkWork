# SHULL-CHG-0068 — Physics U3 section list: adopt the deck's six sections

> **No conflict with a LOCKED rule.** The Physics curriculum map is labelled CONFIRMED, not LOCKED.
> It does replace a confirmed map that was taken from a cited source (`SHULL_Physics_Unit_Map_1.pdf`).
> See section 4.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0068 |
| **Date** | 2026-11-10 |
| **Source** | User. Found by the main session on 2026-11-10 while building the Physics Unit 3 guided notes. |
| **Current Rule** | `courses/physics/DECISIONS.md`, "Curriculum map — CONFIRMED", lines 34-37: "**U3 · Forces and Motion** — 7 sections / `3.1` Newton's Laws · `3.2` Free Body Diagrams · `3.3` Inclined Plane FBDs · `3.4` F = ma Calculations · `3.5` Net Force & Acceleration from FBDs · `3.6` Frictional Forces · `3.7` Multi-Body Systems (Atwood Machines)". This is also counted in line 11 ("Units 0–10, 48 sections") and line 70 ("7+4+3 = 14 · ... **total 48.**"). Cross-referenced at line 109-110: "This matters most across `3.2`, `3.3`, and `3.5` — three consecutive FBD sections." |
| **Proposed Rule** | See section 2. |
| **Supersedes** | `courses/physics/DECISIONS.md`, Curriculum map, U3 entry (lines 34-37). Also the section totals at line 11 and line 70, and the FBD cross-reference at lines 109-110. |
| **Reason** | Matt's current Unit 3 deck, "SHULL Physics Unit 03 - Forces and Motion.pptx" (47 slides), uses six sections, not seven. On 2026-11-10 Matt decided in conversation that the U3 guided notes follow the deck's six-section numbering. Until the decisions file matches, the notes carry codes that mean different things in the two sources. Codes 3.4, 3.5 and 3.6 differ in content, and 3.7 exists in only one of them. CLAUDE.md §3 forbids building against a code the decisions file does not confirm. Matt has **not** yet approved changing `DECISIONS.md`. This record asks him to. |
| **Affected Agents** | Designer, Librarian (footers, filenames, Drive section folders), Auditor (code checks). |
| **Affected Skills** | Physics build skills that read section codes. No skill is known to restate the U3 list (not exhaustively checked). |
| **Affected Courses** | Physics only (Path A content, recorded here because Matt asked for a proposal before the decisions file changes). |
| **Risk** | Medium. Changing the code list renumbers 3.4 to 3.7, and Drive already holds seven U3 section folders (see section 3). Leaving it unchanged is also medium risk, because the guided notes being built now already use the six-section codes. |
| **Recommendation** | Approve. Matt has already chosen the deck's numbering for the built material, and the decisions file should match what gets printed. Answer the two questions in section 5 when approving. |
| **Decision** | Approved by the user in chat, 2026-11-11, answering the open questions on this record: "Friction doesnt but id like to add it before we do the math for it." Read by the main session as: approve the six-section U3 list; 3.5 Friction is not an FBD section (FBD cross-reference reads 3.2, 3.3, 3.4); friction may appear in FBD practice before the 3.5 friction calculations. Earlier, 2026-11-10, he chose "Follow the deck" for the U3 numbering. Recorded by the main session (§4.1). |
| **Status** | **APPROVED** |
| **Implemented By** | `courses/physics/DECISIONS.md` and `change-log/CHANGELOG.md` edited by the Secretary on 2026-11-11, to be committed by the main session with this Change ID in the message. **SHA of that commit: pending, add it here.** Then set Status to IMPLEMENTED. |
| **Verified** | **Partially, pending commit.** The Secretary re-read each edited passage against section 2 and the Decision: the U3 list (6 sections, titles as in section 1), the map heading (47), the section-count line (6+4+3 = 13, total 47, with the provenance sentence from section 2 item 3), the FBD cross-reference (`3.2`, `3.3`, `3.4`, with 3.5 named as not an FBD section and the friction-in-FBD-practice note), and a dated decision-log entry at the top of the log. Arithmetic checked: 11 + 13 + 11 + 12 = 47. A grep found no remaining use of `3.7` or the old U3 titles outside the historical folders (section 7, F5). Not done: confirming the diff in git (the Secretary has no git tool). See section 7. |

---

## 1. The two lists side by side

| Code | `DECISIONS.md` now (7) | Deck (6), proposed |
|---|---|---|
| 3.1 | Newton's Laws | Newton's Laws |
| 3.2 | Free Body Diagrams | Free-Body Diagrams |
| 3.3 | Inclined Plane FBDs | Forces on an Incline |
| 3.4 | F = ma Calculations | Net Force and Acceleration |
| 3.5 | Net Force & Acceleration from FBDs | Friction |
| 3.6 | Frictional Forces | Connected Objects |
| 3.7 | Multi-Body Systems (Atwood Machines) | (none) |

The deck has no separate "F = ma Calculations" section. Its content appears to fold into
3.4 Net Force and Acceleration. That reading comes from the section titles only, not from the
slide contents.

## 2. Proposed Rule (verbatim, not adopted)

Four edits to `courses/physics/DECISIONS.md`, applied together:

1. **Lines 34-37** become:
   > **U3 · Forces and Motion** — 6 sections
   > `3.1` Newton's Laws · `3.2` Free-Body Diagrams · `3.3` Forces on an Incline ·
   > `3.4` Net Force and Acceleration · `3.5` Friction · `3.6` Connected Objects

2. **Line 11** heading becomes: `## Curriculum map — CONFIRMED (Units 0–10, 47 sections)`

3. **Line 70** becomes: `**Section count:** 4+4+3 = 11 · 6+4+3 = 13 · 3+5+3 = 11 · 6+6 = 12 · **total 47.**`
   The trailing "Matches the map header." would no longer be true of `SHULL_Physics_Unit_Map_1.pdf`.
   Proposed replacement: "U3 follows Matt's deck, not the map PDF (SHULL-CHG-0068)."

4. **Lines 109-110** become: "This matters most across `3.2`, `3.3`, and `3.4` — three consecutive
   FBD sections." Under the deck's titles, 3.4 Net Force and Acceleration takes the place of the old
   3.5. Whether 3.5 Friction also counts as an FBD section is Matt's call (question 2).

Plus a dated decision-log entry at the top of the Physics decision log (CHANGE_CONTROL §5), citing this ID.

## 3. Knock-on effects (listed here, not part of this change)

| Item | Where | Note |
|---|---|---|
| Drive holds 7 Physics U3 section folders (03.1–03.7) | `reports/drive-operations/2026-09-16c_physics-build-shull-chg-0023.md` line 38. Folder IDs at `reports/drive-operations/2026-09-16d_geo-phys-retrofit-shull-chg-0024.md` lines 212-218 (Physics table, inferred from the 7-row run) | Folder 03.7 would map to no section, and folder names for 03.3–03.6 would be stale. Any rename, move or trash needs its own record and a pre-logged Drive operation (CHANGE_CONTROL §7). |
| Open question 1 (line 183-184) | `courses/physics/DECISIONS.md` | Cites "Atwood machines, inclined-plane FBDs" as rigor evidence. Still true if Connected Objects covers Atwood machines. Not edited by this change. |
| Open question 2 (line 186-188) | `courses/physics/DECISIONS.md` | Cites "inclined-plane FBDs at `3.3`". Code still valid, title changes. Not edited by this change. |
| Short titles table | `courses/physics/DECISIONS.md` lines 227-234 | No U3 rows exist yet. Nothing to change. |

## 4. Not a LOCKED conflict, but a provenance change

The map is CONFIRMED and was taken from `SHULL_Physics_Unit_Map_1.pdf`, which has still not been found
in Drive (open question 5). Adopting this change means U3 no longer follows that source. CLAUDE.md
precedence (Matt's direct instruction first) supports the change. It still needs Matt's own approval
of this record, because the decision he made today covered the guided notes, not the decisions file.

## 5. Questions for Matt

1. Approve replacing the U3 list with the deck's six sections, as written in section 2?
2. Is 3.5 Friction an FBD section for the line 109 convention? That is, should the line read
   "`3.2`, `3.3`, and `3.4`", or "`3.2`–`3.5`"?

## 6. What this does not do

- It does not edit `courses/physics/DECISIONS.md`.
- It does not rename, move or trash any Drive folder.
- It does not touch the guided notes being built.

(Section 6 describes the record as proposed. Implementation is in the `Implemented By` field.)

## 7. Implementation notes and follow-ups (recorded, not acted on)

Applied 2026-11-11 against the APPROVED Decision recorded at commit `ecd988c` (branch
`claude/focused-mendel-cefeca`). Question 2 was answered by the Decision: 3.5 Friction is not an FBD
section, so the cross-reference reads `3.2`, `3.3`, `3.4`, and friction may appear in FBD practice
before the 3.5 calculations. The Change ID was checked free against a fetched `origin/main` and
pushed in the branch's first commit (reported by the main session; the Secretary has no git tool).

| # | Follow-up | Where | What it needs |
|---|---|---|---|
| F1 | Drive holds seven U3 section folders. `03.7` maps to no section. Folder names `03.3`–`03.6` carry the old titles. | Drive, `Physics/Unit 03 - Forces and Motion/`. IDs per section 3. | Its own record, and a Drive operation pre-logged in `reports/drive-operations/` (CHANGE_CONTROL §7). Not acted on. |
| F2 | Open question 1 cites "Atwood machines, inclined-plane FBDs". | `courses/physics/DECISIONS.md`, Open questions 1 | Left unedited, as section 3 says. Still true: the built U3 notes specs teach the Atwood machine under `3.6` (`templates/notes/specs/make_phys_u03_s03.1-s03.6_notes.py` lines 428 and 535). |
| F3 | Open question 2 cites "inclined-plane FBDs at `3.3`". | `courses/physics/DECISIONS.md`, Open questions 2 | Left unedited, as section 3 says. The code is still valid. The title is now "Forces on an Incline". |
| F4 | The map's `Source:` line still names `SHULL_Physics_Unit_Map_1.pdf` as the source of the whole map. | `courses/physics/DECISIONS.md`, Curriculum map, `Source:` line | Not in section 2, so not edited. The section-count line now says U3 follows Matt's deck. A one-line qualifier on the `Source:` line would need its own approval. |
| F5 | Code that may still use the old U3 codes or titles (`3.7`, "Inclined Plane FBDs", "Multi-Body Systems"). | `templates/`, `.claude/skills/`, builders | A grep on 2026-11-11 (excluding `legacy/`, `docs/`, `reports/`, `governance/`; `.claude/` searched separately) found no `"3.7"`, `S03.7`, "Inclined Plane FBDs" or "Multi-Body Systems". The builders read section codes from this file, so any spec declaring `3.7` would now be refused. |
| F6 | The U3 notes generator docstring says "SHULL-CHG-0068 pending for DECISIONS.md". | `templates/notes/specs/make_phys_u03_s03.1-s03.6_notes.py` line 12 | Stale once this commit lands. A one-word fix by whoever next edits that file. Templates were out of scope here. |
| F7 | `courses/README.md` line 18 restates the Physics count: "11 units, 48 sections". Now stale (47). It is a duplicate of a fact owned by `courses/physics/DECISIONS.md`. | `courses/README.md` | Not in section 2, so not edited. The fix under CLAUDE.md §1 is to point at the decisions file, not to restate 47. Needs its own approval. (Historical reports under `reports/` and older records that say 48 are history and stay.) |
