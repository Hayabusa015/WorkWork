# SHULL-CHG-0070 — Physics notation: write net force as ∑F, not Fnet

> **Change ID is provisional.** Taken as the next integer after `SHULL-CHG-0069`, the highest ID in
> the local `governance/proposals/` on 2026-11-11. `SHULL-CHG-0069` (no inline blanks) was being
> written by another Secretary run at the same time. The session that wrote this record has no git
> tool. It could not `git fetch origin main` and cannot push. Under `governance/CHANGE_CONTROL.md` §2
> this ID is **not allocated** until someone checks it against a freshly fetched `origin/main` and
> pushes the record there. If `SHULL-CHG-0070` already exists on `origin/main`, renumber this file
> before pushing it.
>
> **No conflict with a LOCKED rule.** No existing rule in `courses/physics/DECISIONS.md`, a standard
> or a Physics spec fixes net-force notation (see section 3). This adds a rule. It does not replace one.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0070 (provisional, see banner) |
| **Date** | 2026-11-11 |
| **Source** | User. Matt, in conversation, 2026-11-11, about the Physics U3 guided notes, verbatim: "Also in front of forces. Can we use the sum of symbol, I want to emphasize its the sum of". He attached an image of "∑F = ma". |
| **Current Rule** | None. `courses/physics/DECISIONS.md` has no notation rule for net force. The nearest rules are "Physics-specific build rules — CONFIRMED as discipline standards", **Vectors** (lines 105-106): "Any vector quantity gets a direction, always. Magnitude alone is an incomplete answer for displacement, velocity, acceleration, force, momentum, and field strength." and **Free-body diagrams** (lines 108-110). Neither names a symbol. In practice, built material uses `Fnet` (section 3). |
| **Proposed Rule** | See section 2. |
| **Supersedes** | No written rule. It replaces the unwritten `Fnet` convention used in the U3 deck, the U3 guided-notes specs and the U4.1 practice spec (section 3). |
| **Reason** | Matt wants the symbol itself to show that net force is the sum of all forces on the object. `Fnet` names the result. `∑F` shows the operation. This holds across every Physics unit that uses Newton's 2nd law, so it is a course convention, not a one-off. It affects Physics only, so under CLAUDE.md §2 it belongs in `courses/physics/DECISIONS.md`, not in a standard. |
| **Affected Agents** | Designer (builds notes, slides, practice). Auditor (could check for stray `Fnet` on Physics pages). |
| **Affected Skills** | Physics notes, practice and slide build skills, wherever they type the equation. No skill is known to state `Fnet` as a rule (not exhaustively checked). |
| **Affected Courses** | Physics only (Path A content, recorded as a proposal because the decisions file is only changed against an approval). |
| **Risk** | Low for the rule itself. Medium knock-on: the U3 deck and the U3 notes specs print `Fnet` throughout (section 4). |
| **Recommendation** | Approve. Matt asked for it directly, and it fits the Vectors rule already in force. Answer the questions in section 5 when approving. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

---

## 1. Matt's request (verbatim)

> "Also in front of forces. Can we use the sum of symbol, I want to emphasize its the sum of"

Attached image: "∑F = ma". 2026-11-11, about the Physics U3 guided notes.

## 2. Proposed Rule (verbatim, not adopted)

A new paragraph in `courses/physics/DECISIONS.md`, "Physics-specific build rules — CONFIRMED as
discipline standards", placed directly after **Vectors** (after line 106):

> **Net force notation.** Net force is written **∑F**, never `Fnet`. Newton's 2nd law is
> **∑F = ma**. Components are **∑Fx** and **∑Fy**, with x and y as subscripts. Equilibrium is
> ∑F = 0, or ∑Fx = 0 and ∑Fy = 0. Typeset the symbol as **U+2211 N-ARY SUMMATION (∑)**, which
> Archivo carries. Do not use U+03A3 GREEK CAPITAL LETTER SIGMA (Σ), which Archivo lacks and which
> would fall back to another face. (SHULL-CHG-0070)

Plus a dated decision-log entry at the top of the Physics decision log (CHANGE_CONTROL §5), citing
this ID.

## 3. Existing notation: what was checked

| Source | What it says | Rule or usage |
|---|---|---|
| `courses/physics/DECISIONS.md` | No "Fnet", "∑F" or "ΣF". "net force" appears only at line 36 (U3 section title), line 121 (misconception list) and line 266 (a 1.3 lab log entry). | No rule |
| Physics U1 specs: `templates/notes/specs/phys_u01_s01.1-s01.4.json`, `templates/worksheet/specs/phys_u01_s01.1-s01.4.json`, `phys_u01_s01.1_extended.json`, `phys_u01_s01.2_10q.json` | No occurrence of Fnet or net force. | No rule |
| Physics U2 specs | **None exist** in `templates/`. | Nothing to check |
| `templates/practice/specs/physics.json` (4.1 Work and Power) | Line 21 `"plain": "Fnet = m a"`. Line 90 answer: "Fnet = +8.0 N; a = Fnet/m". | Usage only |
| `templates/notes/specs/make_phys_u03_s03.1-s03.6_notes.py`, `phys_u03_s03.1-s03.6_notes_student.json`, `phys_u03_s03.1-s03.6_notes_key.json` | `Fnet` throughout, including `Fnet = ma`, `a = Fnet / m`, `Fnet,x`, `Fnet,y`, `Fnet = √(Fx² + Fy²)`. | Usage only |
| `standards/`, `brand/` | No net-force notation. | No rule |
| `docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md` line 480 | "a moving object must have net force" (misconception list, LOCKED). Wording, not notation. Unaffected. | Not notation |

## 4. Knock-on effects (listed here, not part of this change)

| Item | Note |
|---|---|
| **U3 deck** ("SHULL Physics Unit 03 - Forces and Motion.pptx") prints `Fnet` throughout | **Open question for Matt** (question 2). Not edited by this change. |
| U3 guided-notes specs (the three files in section 3) | Being built now. They would need `Fnet` changed to `∑F` and `Fnet,x`/`Fnet,y` to `∑Fx`/`∑Fy`. The magnitude line `Fnet = √(Fx² + Fy²)` would become `∑F = √((∑Fx)² + (∑Fy)²)` or similar. The exact form is Matt's call (question 3). Not edited by this change. |
| `templates/practice/specs/physics.json` (4.1) | Uses `Fnet = m a`. Not edited by this change. |
| Answer keys in ShullHand | `brand/fonts/README.md` line 43: ShullHand v0.2 has "No sigma". Keys fall back per glyph to Patrick Hand (SHULL-CHG-0044). **Not verified** whether Patrick Hand carries U+2211. If it does not, ∑ on a key would fall back again or show a missing-glyph box. Check before building a key with ∑. |
| Archivo coverage of U+2211, and its absence of U+03A3 | Stated in the request. **Not verified** by this session, which has no shell to inspect `brand/fonts/Archivo*.ttf`. Verify during implementation (`Verified:` field). |
| Already-built Physics material in Drive | Stays as built under the no-retrofit policy unless Matt says otherwise. |

## 5. Questions for Matt

1. Approve the rule in section 2, ∑F in place of Fnet for all Physics material?
2. Should the current U3 deck be updated from `Fnet` to `∑F`, or left as built?
3. For the magnitude of a 2-D net force, which form: `∑F = √((∑Fx)² + (∑Fy)²)`, or a simpler
   `|∑F| = √(Fx² + Fy²)` with Fx, Fy understood as the summed components?

## 6. What this does not do

- It does not edit `courses/physics/DECISIONS.md`.
- It does not edit the U3 deck, the U3 notes specs or the 4.1 practice spec.
- It does not change any font file.
