# SHULL-CHG-0119 — Unit readings use a stacked single-column cover

> **No conflict with a LOCKED rule.** The workflow does not currently state a cover layout. This
> record adds one paragraph to item 1 (Cover) and leaves the Key Refreshers paragraph
> (SHULL-CHG-0117) word for word. The ten-term limit, the tear-off format (SHULL-CHG-0107,
> SHULL-CHG-0118) and the cover breakdown stay as they are. No item marked CONFLICT, PROVISIONAL or
> UNKNOWN is converted.
>
> **One layer: Path B, a build rule** (`governance/CHANGE_CONTROL.md` §1). The rule applies to unit
> readings in all three courses, so it belongs in the workflow (CLAUDE.md §2 test). No course fact
> changes, and no `DECISIONS.md` entry is needed.
>
> **The builder is already ahead of the rule.** This is Auditor finding R4-4. Commit `0947c27` made
> `front.layout: "stacked"` the default in `templates/reading/build_reading_docx.py`, so every new
> reading already gets this cover without a written rule. The record makes the rule explicit. If it
> is rejected, the builder default has to be reverted or changed (see Risk).
>
> **ID allocation.** SHULL-CHG-0118 is the highest ID in the local checkout of
> `governance/proposals/`, and no file in the working tree mentions SHULL-CHG-0119 or a higher
> number. The main session has to confirm 0119 is free on a freshly fetched `origin/main` before
> committing (§2). Until that push, this ID is not allocated.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0119 |
| **Date** | 2026-11-25 |
| **Source** | Auditor and User. **Auditor**, Round 4 finding R4-4: "builder now makes the stacked cover the default for every new reading; a change affecting all three courses belongs in a standard or skill". **User**: Matt, main session, 2026-11-25, about the Chemistry U6 cover: "I feel like this needs structured better". He was then asked "How should the Unit 6 cover be reorganized? (This layout would carry over to future readings.)" and chose "Stacked, top to bottom". That option's text read: "Everything in one column in reading order: title, Why It Matters (short), Key Refreshers (with the charge table), In This Unit, then How to Use. Simple, but uses more of page 1." Asked next where Key Refreshers should sit, he chose "After 'In This Unit' (Recommended)": "Title → Why It Matters → In This Unit → Key Refreshers → How to Use → 6.1. Matches the rule as approved; no rule change needed." **Note on the order:** the first option listed Key Refreshers *before* In This Unit. The second answer put it *after*, and that is the order this record uses. **Not in Matt's words:** the caps labels, the rules between blocks, "no fills", "about four lines" and "one to four steps" come from the builder as built (commit `0947c27`), not from anything Matt said. "All three courses" comes from the question's parenthetical ("would carry over to future readings") and from R4-4. Matt did not name courses. Approving this record approves these details too. |
| **Current Rule** | `workflows/unit-textbook.md`, "Prepare the unit reading and its detachable submission", item 1. First paragraph: "**Cover.** Introduce the unit and give students its breakdown: list the confirmed numbered sections in order with their short topic titles. Use those same section numbers and sequence throughout the reading and response sheet." Second paragraph: the **Key Refreshers** paragraph from SHULL-CHG-0117, which begins "After the section list and Why It Matters, and before the first section…". No written rule sets the cover layout. In practice the builder sets it: before `0947c27`, `front()` drew the two-column cover (title, section list and a one-paragraph how-to on the left, Why It Matters on the right, Key Refreshers full width below). That cover is still available as `front.layout: "columns"`, and `templates/reading/specs/chem_u07_reading.json` pins it. |
| **Proposed Rule** | A third paragraph, **Cover layout**, appended to item 1 (Cover) after the Key Refreshers paragraph. The full text is under "Exact text" below. The first two paragraphs of item 1 do not change. |
| **Supersedes** | Nothing in the workflow text is replaced; this adds to `workflows/unit-textbook.md` item 1. It replaces the unwritten two-column cover, which until `0947c27` was the builder's default (`templates/reading/build_reading_docx.py` `front_columns()`), as the cover for new readings. SHULL-CHG-0117 is unchanged. Its rule text still holds under the stacked order, because Key Refreshers comes after both the section list and Why It Matters and before the first section. Its "Choices" table describes placement in terms of the two-column cover table. That reasoning described the cover at the time. This record does not edit it. |
| **Reason** | Matt found the U6 two-column cover poorly structured ("I feel like this needs structured better"), and chose a single column read straight down. The builder change already applies that cover to every new reading in every course. Under CLAUDE.md §2, a change that affects all three courses belongs in a standard or skill or the workflow, not only in a builder default (R4-4). Writing it down means a builder default is no longer the only place the rule exists, and the Auditor has something to check the cover against. |
| **Affected Agents** | Textbook Page Designer (builds the cover). Auditor (checks it against the workflow). Overseer (commissions readings under the workflow). Secretary (implementation only, after approval). `.claude/agents/textbook-page-designer.md` needs no change, because it defers to the workflow. |
| **Affected Skills** | None. `.claude/skills/verify-content/SKILL.md`, `.claude/skills/build-document/SKILL.md` and `standards/QA_GATE.md` do not describe the reading cover. |
| **Affected Courses** | Chemistry, Physics and Geology (all unit readings). No course fact changes. |
| **Risk** | Low. (1) **Page 1 space.** Matt's chosen option says the stacked cover "uses more of page 1". The chapter starts lower, so a reading near its page budget may gain a page, and the even-page and tear-off parity checks still apply. (2) **Builder vs. rule.** The builder enforces 1–4 steps for `front.how` and the block order. It does **not** check the "about four lines" length of Why It Matters, so the designer and the Auditor have to check that by eye. (3) **If rejected.** The builder default added in `0947c27` would contradict the decision. It would need reverting to `"columns"`, or changing to whatever Matt chooses instead, before the next reading is built. (4) **Older readings.** Chemistry U7 is pinned to `"columns"`. The proposed text keeps covers on readings filed before this rule unless the teacher asks, so U7 has no forced reprint. |
| **Recommendation** | Approve. It records what Matt chose for U6 and what the builder already does. Matt has not yet agreed to the scope-in-time sentence or to the builder-derived details named in Source. If he wants either changed, it can be changed before approval. |
| **Decision** | 2026-11-25, user, in the main session, answering "Approve SHULL-CHG-0119, the stacked cover layout for every new or revised unit reading in all three courses, with the wording shown above?" (the proposed Cover layout paragraph was shown verbatim): "Approve". |
| **Status** | **APPROVED** |
| **Implemented By** | — |
| **Verified** | — |

---

## Exact text to add to `workflows/unit-textbook.md`

**Appended to item 1 (Cover)** as a third paragraph, after the Key Refreshers paragraph and with the
same indentation. It is not a new numbered item, so items 2–5 keep their numbers (the builder cites
"workflows/unit-textbook.md steps 3-5").

> **Cover layout.** Set the cover in one column, in this order: the unit title; **Why It Matters**,
> a short paragraph of about four lines; **In This Unit**, the section list; **Key Refreshers**, when
> the block applies; **How to Use This Reading**, one to four short numbered steps that describe the
> reading and its tear-off leaf as they are printed; then the first section. Start each block with a
> caps label, put a rule between blocks, and use no fills. This applies to every new or revised unit
> reading in all three courses. A reading filed before SHULL-CHG-0119 keeps its cover unless the
> teacher asks for this layout at a revision.

## The choices this record makes

| Question | Answer in the rule | Why |
|---|---|---|
| Block order | Title → Why It Matters → In This Unit → Key Refreshers → How to Use → first section | Matt's second answer ("After 'In This Unit' (Recommended)"). It replaces the order in the first option's text. |
| Key Refreshers paragraph | Left word for word | Its placement words ("after the section list and Why It Matters, and before the first section") already fit the stacked order. Matt's chosen option said "no rule change needed" for placement. |
| How to Use | 1–4 short numbered steps, true to the printed tear-off | Builder check (`check_front`: "a list of 1-4 short numbered steps"). The steps must match the leaf as it is actually printed, e.g. written vocabulary definitions under SHULL-CHG-0118, not printed ones. |
| Labels, rules, fills | Caps label per block, rules between blocks, no fills | Builder as built (`front_stacked()`). Not in Matt's words, so it is named in Source for him to approve. |
| Why It Matters length | About four lines | Matt's "(short)". The builder does not enforce the four lines (see Risk 2). |
| Scope in time | New and revised readings. Covers on earlier readings stay unless the teacher asks. | Matches the SHULL-CHG-0117 pattern. The U7 pin (`"columns"`) is recorded only here and in its spec, so the course case is stated in one place. |
| Audit bullet | None proposed | The task was kept to a minimal addition to item 1. The existing audit bullets do not check cover layout. If Matt wants the Auditor to check it explicitly, that would be a separate bullet, added either before approval or under a later record. |

## Affected files and implementation (after approval)

| File | Change |
|---|---|
| `workflows/unit-textbook.md` | The paragraph above, verbatim, appended to item 1 |
| `templates/reading/build_reading_docx.py` | None. The stacked default and the U7 `"columns"` pin already exist (`0947c27`). |

1. **Secretary:** append the paragraph verbatim in one commit that carries SHULL-CHG-0119, and update
   this record's changelog row.
2. **Not part of this record:** rebuilding or refiling any reading. That is classroom work, and it
   goes through the Overseer (CLAUDE.md §6).

## Verification plan (for a checker other than the implementer)

1. The implementing diff to `workflows/unit-textbook.md` adds only the paragraph above. The first
   two paragraphs of item 1 are byte-identical, and items 1–5 keep their numbers.
2. `python3 scripts/validate_references.py` and `python3 scripts/validate_change_ids.py` pass.
3. `git show 0947c27 -- templates/reading/build_reading_docx.py` shows `FRONT_LAYOUTS = ("stacked",
   "columns")` with stacked first, and `templates/reading/specs/chem_u07_reading.json` sets
   `"layout": "columns"`.
4. Fill in `Implemented By` with the commit SHA and `Verified` with the results.
