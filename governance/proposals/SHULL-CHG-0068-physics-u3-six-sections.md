# SHULL-CHG-0068 — Physics U3 section list: adopt the deck's six sections

> **Change ID is provisional.** Taken as the next integer after `SHULL-CHG-0067`, the highest ID in
> the local `governance/proposals/` and `change-log/CHANGELOG.md` on 2026-11-10. The Secretary
> session that wrote this record has no git tool. It could not `git fetch origin main` and cannot
> push. Under `governance/CHANGE_CONTROL.md` §2 this ID is **not allocated** until someone checks it
> against a freshly fetched `origin/main` and pushes the record there. If `SHULL-CHG-0068` already
> exists on `origin/main`, renumber this file before pushing it.
>
> **No conflict with a LOCKED rule.** The Physics curriculum map is labelled CONFIRMED, not LOCKED.
> It does replace a confirmed map that was taken from a cited source (`SHULL_Physics_Unit_Map_1.pdf`).
> See section 4.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0068 (provisional, see banner) |
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
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

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
