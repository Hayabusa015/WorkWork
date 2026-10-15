---
id: SHULL-CHG-0027
title: Filing gate — documents are filed to Drive only after the user approves them
status: PENDING
opened: 2026-10-15
source: User
decided_by:
---

# SHULL-CHG-0027 — Filing gate

## What he asked for

"I need to work this into my rules for my WorkWork repo agents to file all documents once they have
been created and confirmed. It usually takes 3-4 iterations to get a document to where I want it, so
I need to check a box or something to file this, using the rules you have just created."

Answers on 2026-10-15: approval by **both** a chat phrase and a checklist; file the **student file,
key and PDF** together; if the folder is unclear, **stop and ask**.

## Current Rule

`.claude/agents/overseer.md` §Verification: the Librarian verifies the destination. Nothing says
*when* filing starts. `.claude/agents/librarian.md` §Filing a built binary (SHULL-CHG-0026) says
*how* to file.

## Proposed Rule

**1. Iteration never reaches Drive.** Drafts and revisions stay on the session's disk. Drive only
receives a version the user has approved.

**2. A document is ready when the QA gate has passed.** The Overseer then adds one row to
`reports/filing-queue.md`, unticked: document, course, unit, section, spec path, files, status.
It commits the final spec so the document can be rebuilt if the session ends first.

**3. The user approves in one of two ways:**
- **Chat:** "file it" (one document) or "file everything built this session". Agents also accept
  the same words in other phrasings that clearly mean approval of a named document.
- **Checklist:** tick the box on its row in `reports/filing-queue.md`.

Neither the Overseer nor any other agent ticks a box or files on its own judgement.

**4. On approval the Librarian files the set:** the student file, its separate key where one
exists, and the print PDF, all into the same folder, using the SHULL-CHG-0026 flow: log first,
upload to the Upload Inbox, reparent and rename with `update_file`, verify by independent lookup.
If a ticked row's file is gone, rebuild it from the committed spec first and re-run the QA gate.

**5. Unclear destination:** stop and ask. Never default to a misc folder or leave a file in the
Inbox without telling the user.

**6. After filing:** the Overseer marks the row Filed with the confirmed Drive path and file ID and
the date. A failed step leaves the row Not filed, with the reason.

**7. Revised after filing:** a new approval is required. The Librarian never overwrites a filed
file. The new version is filed as `Version N` (SHULL-CHG-0024) unless the user asks to replace
the old one, and trashing the old one needs the user's approval as always.

## Where it lands

| Place | Change |
|---|---|
| `standards/DRIVE_ARCHITECTURE.md` | New section "When to file": rules 1 to 7 above, once |
| `.claude/agents/overseer.md` | Add the queue row after QA; run the filing step on approval; completion needs "Filed" |
| `.claude/agents/librarian.md` | Files only against an approval; filing set; points to the standard |
| `.claude/skills/shelve-drive-file/SKILL.md` | Precondition: an approval exists |
| `reports/filing-queue.md` | New: the checklist |

## Supersedes

Nothing. Adds a gate in front of the SHULL-CHG-0026 flow.

## Risk

low. It only makes filing wait for the user. One real risk: a ticked box can mean the file is gone
after a session ends. The committed spec covers that; documents built outside the spec builders
(for example hand-edited .docx) cannot be rebuilt, and the agent must say so.

## Recommendation

Approve.

Decision:
Status: PENDING
Implemented By:
Verified:
