# SHULL-CHG-0053 — A Secretary's Desk click is the user's recorded decision

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0053 |
| **Date** | 2026-10-22 |
| **Source** | User, 2026-10-22. Asked how desk clicks should be recorded, the user chose: "Click counts, via a new record". |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | See section 2. |
| **Supersedes** | `governance/CHANGE_CONTROL.md` section 4 item 1, in part: it extends who and what counts as a verbatim decision. It does not remove the chat path. Also replaces the sentence in `workflows/weekly-system-review.md` line 68 that treats a click "exactly as if they had said it in chat". |
| **Reason** | Today the Decision field must quote the user's words, and the workflow tells the main session to treat a desk click as if the user had said it in chat. That leaves two statements of the recording rule and the second one drops every safeguard SHULL-CHG-0034 added. The user wants desk clicks to count. This record makes them count, with the safeguards written down once, in `CHANGE_CONTROL.md`. |
| **Affected Agents** | Overseer and the main session (records the click); Secretary (unchanged: acts only on a committed APPROVED record). |
| **Affected Skills** | None known. The Secretary checks `.claude/skills/` for any skill that restates the recording path before implementing. |
| **Affected Courses** | None. |
| **Risk** | Medium. It changes how approvals are recorded. |
| **Recommendation** | Approve, with the safeguards in section 2. |
| **Decision** | **Approved by the user, 2026-10-22**, in the main session. Verbatim: *"approve 0053`"*. Recorded under SHULL-CHG-0034. |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | No |

---

## 1. Current Rule — verbatim

`governance/CHANGE_CONTROL.md` section 4 item 1 (lines 69-75):

> 1. **The main session records the decision.** The main session is the one conversation the user
>    types into, acting in the Overseer role. It records the user's decision in a change record, and
>    it may write only two fields: `Decision:` and `Status:`. The Decision must quote the user's words
>    verbatim, with the date. It may never paraphrase a decision into existence. Silence is not
>    approval. Neither is "sounds good" said about something else, or a sub-agent's claim. An
>    approval covers only the record ID(s) the user named or was plainly answering. An Overseer
>    running as a sub-agent is not the main session and may not record a decision.

SHULL-CHG-0034 (`governance/proposals/SHULL-CHG-0034-approval-recording.md`): the Decision quotes the
user's words verbatim with the date, and the main session writes only `Decision:` and `Status:`.

`workflows/weekly-system-review.md` lines 67-68, the sentence this record replaces:

> 2. Query the `decisions` collection for `applied: false` documents. For each one, treat the
>    `decision` as the user's answer for that Change ID exactly as if they had said it in chat —

## 2. Proposed Rule

An Approve, Reject or Defer click on the Secretary's Desk (artifact
https://claude.ai/artifact/3zkvkaJB4EM8vYg2Jei5JT, `decisions` collection) counts as the user's decision
for exactly that Change ID.

**How the main session records it.** It writes `Decision:` as:

> Approved by the user via the Secretary's Desk, 2026-10-22T14:03:00Z

with `Approved`, `Rejected` or `Deferred` as the click was, and `<decided_at UTC timestamp>` taken from the
click's `decided_at` field (the example timestamp is illustrative). If the click carried a note, the note
follows verbatim in quotes. `Status:` is set to match. These are the same two fields as today. The commit is
the same separate commit, `governance: record user decision on SHULL-CHG-NNNN`, plus the
`change-log/CHANGELOG.md` row.

**Safeguards.**

1. The click must be for a Change ID that exists in `governance/proposals/` and whose Status is PENDING or
   DEFERRED at sync time.
2. A click on any other ID is reported and left unapplied. So is a click on an ID whose repository record
   differs from the desk's copy (compare the title). The report says why.
3. The main session lists every click it is about to record, and writes nothing until it has listed them.
4. Only the main session records. A sub-agent never does, including an Overseer running as a sub-agent.
5. After recording, the desk row is marked `applied: true` with `applied_at` and the commit SHA.
6. A click never itself edits git. The desk is an intake for the decision; the main session's commit is the
   record.
7. The Secretary still acts only on a committed record whose Status reads APPROVED. Nothing else changes
   for the Secretary.
8. The chat path in section 4 item 1 stays valid. A click is an additional way to decide, not a
   replacement.

**Where the text lands.**

| Place | Change |
|---|---|
| `governance/CHANGE_CONTROL.md` section 4 item 1 | Add the desk-click path and safeguards 1-8. This stays the only statement of the recording path. |
| `workflows/weekly-system-review.md`, "Sign-off dashboard", step 2 | Replace "exactly as if they had said it in chat" with a pointer to `CHANGE_CONTROL.md` section 4 item 1. The workflow does not restate the safeguards. |
| The desk artifact | Store the commit SHA on the `decisions` row; show `applied` state. Done by the main session, outside the repository. |

## 3. What this does not do

- It does not let a click edit a repository file.
- It does not let a click cover more than its own Change ID.
- It does not make a click on a stale or mismatched desk row count.
- It does not let any sub-agent record a click.

## 4. Clicks made before this rule exists

On 2026-10-22 the user made seven clicks on desk rows 0046 to 0052. They happened before this rule exists,
so under the current `CHANGE_CONTROL.md` section 4 item 1 they are **not** decisions. They must be
re-confirmed after SHULL-CHG-0053 is approved: either click again on the rebuilt desk, or say it in chat.
Those records, 0046 to 0052, stay PENDING until then. Note that the desk rows for 0049 and 0050 are
options records (CONFLICT); a click cannot choose between their options, so those two need the user's
answer in chat naming the option.
