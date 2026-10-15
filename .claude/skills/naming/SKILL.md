---
name: naming
description: Construct or check a SHULL filename and document code. Use before saving any deliverable, when renaming files, or when auditing whether existing filenames follow the convention. Produces a filename, or a list of what is wrong with one.
---

# naming

Rules: `standards/NAMING.md`. This is the procedure.

## Building a filename

1. **Resolve the course** (chemistry, physics, geology). It selects the folder; it is not in the name.
2. **Resolve unit and section.** Read `courses/<course>/DECISIONS.md` and confirm the code exists
   there. **If it does not, stop and ask.** Never build against a code that appears only in a skill.
3. **Pick the type** from the fixed list in the standard. Do not invent one.
4. **One section** is `[S.S] [Type] - [Topic]`. **More than one** is `Unit [X] [Type] - [Unit Title]`.
5. **Topic and unit title come from the decisions file.** If it is not there, leave the topic off.
6. **Version letter** after the type, then `Key`: `1.4 Quiz A Key - Reaction Time`.
7. **A key is always its own file.**
8. No `: / \ * ? " < > |` in a name. Use the helpers in `templates/` rather than typing it.

## Checking an existing filename

Report as a table, not prose:

| File | Problem | Correct name |
|---|---|---|

Check, in order: valid type · section exists in that course's decisions file · topic matches the
decisions file · separate key exists if the document has answers · no illegal characters · the
folder it sits in is the right course and unit. Names in the old `SHULL_..._U##_S##.#` form are
legacy: report them as needing rename, not as errors in the content.

## Before renaming anything

**Log the object ID, prior name, and prior parent to `reports/drive-operations/` first.** A rename
that was not logged cannot be rolled back.

**Never batch-rename without confirmation.** Renames break links that may exist in a gradebook, a
Classroom post, or a student's bookmark.

## Nothing is blocked

Geology renaming was blocked on section numbering — unblocked by SHULL-CHG-0009. Moves were blocked
pending test T-3 — unblocked 2026-09-08; `update_file` reparents in place and keeps the file ID.

## Images are not course documents

No prefix, lowercase, named for the slot. See the standard.
