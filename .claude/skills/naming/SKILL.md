---
name: naming
description: Construct or check a SHULL filename and document code. Use before saving any deliverable, when renaming files, or when auditing whether existing filenames follow the convention. Produces a filename, or a list of what is wrong with one.
---

# naming

Rules: `standards/NAMING.md`. This is the procedure.

## Building a filename

1. **Resolve the course** — `CHEM` · `PHYS` · `GEO`.
2. **Resolve unit and section.** Read `courses/<course>/DECISIONS.md` and confirm the code exists
   there. **If it does not, stop and ask.** Never build against a code that appears only in a skill.
3. **Pick the type** from the fixed list in the standard. Do not invent one.
4. **Zero-pad both** the unit and the section: `U08_S08.2`, never `U8_S8.2`.
5. **Add a descriptor** only if it disambiguates. Most files do not need one.
6. **Version letter last**, before `_Key`.
7. **A key is always its own file**, ending `_Key`.

## Checking an existing filename

Report as a table, not prose:

| File | Problem | Correct name |
|---|---|---|

Check, in order: `SHULL_` prefix · valid course · valid type · both codes zero-padded · the section
exists in that course's decisions file · a separate key exists if the document has answers · the
code matches the folder path it sits in.

## Before renaming anything

**Log the object ID, prior name, and prior parent to `reports/drive-operations/` first.** A rename
that was not logged cannot be rolled back.

**Never batch-rename without confirmation.** Renames break links that may exist in a gradebook, a
Classroom post, or a student's bookmark.

## Currently blocked

Nothing. Geology renaming was blocked on section numbering and is now unblocked (SHULL-CHG-0009).

## Images are not course documents

No prefix, lowercase, named for the slot. See the standard.
