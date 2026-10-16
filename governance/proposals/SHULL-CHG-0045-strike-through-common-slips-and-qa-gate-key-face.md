# SHULL-CHG-0045 — Strike-through may use well-known calculation slips; QA gate points at the key face

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0045 |
| **Date** | 2026-10-16 |
| **Source** | User — Matt, 2026-10-16. Came up while implementing SHULL-CHG-0043 Stage 2 (commit d3b5543, main session's account; the Secretary has not inspected that commit). Both items are already flagged as open in SHULL-CHG-0043 §10. |
| **Current Rule** | See §1, verbatim, with file and line. |
| **Proposed Rule** | See §2. Two items (A, B), each separately approvable. |
| **Supersedes** | Item A: SHULL-CHG-0043 Item C.4, **only** its last sentence ("The source of 'common' is the course `DECISIONS.md` misconception list or Matt; if neither supports it, no strike-through."), and the sentence that implements it in `standards/ANSWER_KEYS.md` §3 (lines 39-40). Item B: supersedes nothing. It adds one pointer line to `standards/QA_GATE.md` §1, and the existing Archivo sentence stays. |
| **Reason** | Item A: the only misconception list in `courses/` is Physics `DECISIONS.md` line 120. It lists conceptual misconceptions, not calculation slips, and Chemistry and Geology have no list. Under the current wording, then, a well-known slip can back a strike-through only on Matt's say-so, case by case. Item B: `standards/QA_GATE.md` §1 tells the reader that `pdffonts` should show Archivo or Archivo Narrow. A handwritten key will not show only those, and §1 does not point at the rule that covers keys. |
| **Affected Agents** | Builder agents that produce keys; Auditor (reads QA_GATE §1 and ANSWER_KEYS §3); Secretary (implements only after approval). |
| **Affected Skills** | None. The five 0043 pointer lines point at `standards/ANSWER_KEYS.md` and restate nothing, so they stay correct. |
| **Affected Courses** | All three, keys only. No course `DECISIONS.md` is edited. |
| **Risk** | Low |
| **Recommendation** | Approve both items. See §6. |
| **Decision** | Approved by Matthew Shull, 2026-10-16 ("option 1, and yes to the QA_GATE line"): Item A (option 1) and Item B. |
| **Status** | **IMPLEMENTED** (both items applied; see §10) |
| **Implemented By** | e00b137 |
| **Verified** | Yes, by the main session (main session's account; the Secretary has no shell and did not run these): validate_tokens, validate_layers, validate_codes, validate_references, validate_agents, validate_schemas, validate_profiles, validate_notes all OK; grep found no font name in `standards/ANSWER_KEYS.md` or `standards/QA_GATE.md`; the diff matches the approved wording for Items A and B. |

---

## 1. Current Rule — verbatim

### 1a. `governance/proposals/SHULL-CHG-0043-handwritten-answer-keys.md`, Item C.4 (line 105)

> 4. **Strike-through** shows a wrong attempt only when it is a mistake students genuinely commonly make ("but only if its a common mistake"). Never an invented mistake. A short note names the mistake. The source of "common" is the course `DECISIONS.md` misconception list or Matt; if neither supports it, no strike-through.

### 1b. `standards/ANSWER_KEYS.md` §3 (lines 36-40), the implemented text

> ## 3. Strike-through
>
> A crossed-out attempt appears **only for a mistake students genuinely commonly make**, never an
> invented one. A short note in the arrow ink names the mistake. "Common" comes from the course
> `DECISIONS.md` misconception list or from Matt; if neither supports it, there is no strike-through.

The sentence this record would replace is the last one: `"Common" comes from the course` (line 39) through `there is no strike-through.` (line 40).

### 1c. The only misconception list in `courses/`: `courses/physics/DECISIONS.md` (lines 120-123)

> **Misconceptions to write distractors against:** heavier objects fall faster · a moving object must
> have a net force on it · normal force always equals weight · centripetal force is a separate force
> acting outward · energy is "used up" rather than transferred · confusing mass with weight, speed
> with velocity, heat with temperature.

Checked by grep for "misconception" across `courses/`. Chemistry has only `courses/chemistry/DECISIONS.md` line 151 ("strong distractors from real misconceptions."), which mentions misconceptions but lists none. Geology has nothing. Every entry in the Physics list is conceptual. None is a calculation slip.

### 1d. `standards/QA_GATE.md` §1 (lines 26-29)

> > **Confirm the render used the right font.** `pdffonts` on the output should show Archivo or
> > Archivo Narrow. If it shows DejaVu or Liberation, the font substitution did not take and you are
> > inspecting different metrics than the classroom copy will have. That was the real state of this
> > system until 2026-09-08.

(The file has this as a blockquote. The outer `>` is this record's quote.)

## 2. Proposed Rule

### Item A — What counts as a "common mistake" for a strike-through (`standards/ANSWER_KEYS.md` §3)

Replace **only** the last sentence of §3 (lines 39-40, quoted in 1b) with:

> A mistake qualifies only if students at this level genuinely and routinely make it. The course DECISIONS.md misconception list is one source; a well-known calculation slip, such as a flipped sign or an unsquared t, is another. If it is in doubt, leave it out.

The first two sentences of §3 do not change. After the edit, §3 would read:

> ## 3. Strike-through
>
> A crossed-out attempt appears **only for a mistake students genuinely commonly make**, never an
> invented one. A short note in the arrow ink names the mistake. A mistake qualifies only if students
> at this level genuinely and routinely make it. The course DECISIONS.md misconception list is one
> source; a well-known calculation slip, such as a flipped sign or an unsquared t, is another. If it
> is in doubt, leave it out.

(At implementation the Secretary may put `DECISIONS.md` in code formatting to match the rest of the file. The words stay the same.)

Notes for Matt:

- **This retroactively backs the four strike-throughs on the Physics U1 S1.2 key** (`templates/worksheet/specs/phys_u01_s01.2_10q.json`, main session's account): Q2, final minus initial reversed, which flips the sign; Q3, t not squared; Q5, the v0t term dropped; Q8, the whole trip treated as accelerating. Under the current wording each of these is backed only by Matt's say-so. Under the proposed wording, Q2, Q3 and Q5 match the named kinds of slip (flipped sign, unsquared t, a dropped term). Q8 is a modelling slip, not a sign or exponent slip, so it qualifies only under the "genuinely and routinely" test. Matt may want to confirm Q8 specifically.
- **The words "or Matt" disappear from the sentence.** Matt's direct instruction still outranks any standard (`CLAUDE.md` §2 precedence, item 1), so he can still approve or veto a strike-through. The standard just stops naming him as a source. If Matt wants his name kept, that is a wording change for him to make before approving.
- **"Common" is still a judgment call, now with a tiebreaker.** The new text has no list of slips. "If it is in doubt, leave it out" is the safeguard. Nothing here asks any course to add a slip list to its `DECISIONS.md`. That would be a Path A course change, and it is not proposed here.
- **The alternative from 0043 §10 still exists:** reject this item, keep §3 as written, and have Matt confirm the four S1.2 slips himself, which the current wording already allows ("or Matt").
- SHULL-CHG-0043 is IMPLEMENTED and **is not edited** by this record. This record is the cross-reference. Its `Supersedes` field makes the change to 0043 C.4 visible.

### Item B — `standards/QA_GATE.md` §1: one pointer line for key files

Add **one** line directly after line 29, as a new paragraph at the end of the same blockquote:

> Key files may also carry the key-handwriting face (`typography.keyHandwriting`), per `standards/ANSWER_KEYS.md` §9; `scripts/audit_fonts.py --key` enforces it.

- It is a pointer. It does not restate the key rule, which is stated once in `standards/ANSWER_KEYS.md` §9 ("`scripts/audit_fonts.py --key` admits the key-handwriting face on `Key` files only; on a student file it is a fail").
- It names the token and no font, as SHULL-CHG-0044 Item F requires. A later font swap leaves this line correct.
- Lines 26-29 stay unchanged. Student files must still show Archivo or Archivo Narrow.
- This closes the open item recorded in SHULL-CHG-0043 §10 ("a one-line pointer there would need its own approval").

## 3. Reason in short

Item A: Matt's own words were only "but only if its a common mistake." The approved wording narrowed the source of "common" to a list that has no calculation slips in it. The new wording matches what he asked for and still bans invented mistakes. Item B: a checklist that tells an auditor to expect Archivo, with no mention of keys, will one day fail a correct key or teach the auditor to ignore the line. One pointer prevents both.

## 4. Scope limits

- Keys only. Student pages are not affected.
- No change to the strike-through look, the arrow-ink note, or any other section of `standards/ANSWER_KEYS.md`.
- No change to `scripts/audit_fonts.py`. It is tooling, and the `--key` behaviour already exists (main session's account, SHULL-CHG-0044 Verified field).
- No brand, skill, or course file is touched.

## 5. Conflicts with LOCKED rules (the Secretary does not resolve these; Matt decides)

| # | Rule | Where | Conflict |
|---|---|---|---|
| 1 | SHULL-CHG-0043 Item C.4, last sentence (approved, IMPLEMENTED) | `governance/proposals/SHULL-CHG-0043-handwritten-answer-keys.md` line 105; `standards/ANSWER_KEYS.md` lines 39-40 | Item A replaces an approved rule. It is not a LOCKED token, but it is an approved decision. That is why this needs its own record and not a quiet edit. |
| 2 | "Confirm the render used the right font ... Archivo or Archivo Narrow" | `standards/QA_GATE.md` lines 26-27 | **No conflict.** Item B adds a line and changes no existing text. |

No LOCKED token is changed. No CONFLICT, PROVISIONAL, or UNKNOWN item is converted to LOCKED. `typography.keyHandwriting` and the `keyInk` tokens stay PROVISIONAL.

## 6. Recommendation

Approve both items. Both are low risk, each is one revertible edit in one file, and neither changes what a student sees. Item A is the substantive one. Before approving it, Matt should decide whether to keep "or Matt" in the sentence (see Item A notes). The items are independent, and either can be approved alone.

## 7. Questions for Matt (one at a time as needed)

1. Item A: approve the new §3 sentence as written (it drops "or Matt"), or keep your name in it?
2. Item A: do you confirm Q8 on the S1.2 key ("whole trip treated as accelerating") as a slip your students routinely make?
3. Item B: approve the one-line pointer in `standards/QA_GATE.md` §1?

## 8. Verification plan (for the Secretary, after approval)

- `standards/ANSWER_KEYS.md` §3: only the last sentence differs (`git diff` shows that sentence and nothing else in the file). Grep finds the old sentence nowhere in `standards/`.
- `standards/QA_GATE.md` §1: one added line and no other change. Grep of the added line shows no font name and no hex value.
- `scripts/validate_references.py`, `validate_layers.py`, `validate_tokens.py` pass (main session runs them; the Secretary has no shell).
- `git diff` limited to the approved file(s), this record, and the changelog row. One commit carrying SHULL-CHG-0045.
- Fill in `Implemented By` with the commit SHA and `Verified` with the result.

## 9. Not done by this record

No standard, skill, brand, governance, or course file was edited. SHULL-CHG-0043 was not edited. `change-log/CHANGELOG.md` was not edited (the main session does that when it records the decision). Nothing was committed. This is a proposal only. Implementation waits for a committed record with `Status: APPROVED` and a verbatim `Decision:` quote (`governance/CHANGE_CONTROL.md` §4).

## 10. Implementation note (Secretary, 2026-10-16)

**Authority.** The committed approval. The record was committed PENDING at b82a03e, and the decision was recorded at 5db92b1 ("governance: record user decision on SHULL-CHG-0045"; that is HEAD per `.git/logs/HEAD`). The working-tree record reads `Status: APPROVED`, with a Decision quoting Matt verbatim: "option 1, and yes to the QA_GATE line". The Secretary has no shell and could not diff the committed blob. The commit check rests on the reflog and on the file as it is on disk.

**Context for the Q8 question (§7 Q2), main session's account.** Matt chose option 1 after the main session showed him all four S1.2 strike-throughs by name, Q8 included ("whole trip treated as accelerating"). The main session described option 1 to him as letting well-known calculation slips like these count. The Secretary records this as context only. It is not a separate decision.

**On "or Matt" (§7 Q1).** No wording change was made. Matt's direct instruction outranks any standard (`CLAUDE.md` §2, precedence item 1), so he can still approve or veto any strike-through without being named in §3.

**Applied.**

| Item | File | Change |
|---|---|---|
| A | `standards/ANSWER_KEYS.md` §3 | Last sentence replaced with the approved wording, verbatim. The first two sentences are unchanged. |
| A | `standards/ANSWER_KEYS.md` header | "SHULL-CHG-0045 Item A (§3, what counts as a common mistake)" added to the **Authority** line, which is how this file cites its changes. |
| B | `standards/QA_GATE.md` §1 | The approved pointer line, verbatim, added as a final paragraph of the existing blockquote after "system until 2026-09-08." Lines 26-29 are unchanged. It names the token, not a font. |

**Checks done (grep).** Neither form of the old sentence ("\"Common\" comes from", "or from Matt; if neither") remains anywhere in `standards/`. The added QA_GATE line names no font and no hex value.

**Not done here.** No commit (main session). No validator run (main session; see §8). `change-log/CHANGELOG.md` not edited. No skill, brand, course, or `scripts/` file touched. SHULL-CHG-0043 gets a one-line superseded-by pointer in its §10 and nothing else.
