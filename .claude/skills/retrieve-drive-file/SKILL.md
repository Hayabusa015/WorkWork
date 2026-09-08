---
name: retrieve-drive-file
description: Find and read a file in the SHULL Science Drive library. Use to locate a canonical document, check whether something already exists before building it, or read an existing file's content. Read-only.
---

# retrieve-drive-file

Tree and folder IDs: `standards/DRIVE_ARCHITECTURE.md`, `config/drive.json`.

## Finding

`parentId = '<ID>'` is the reliable query — it enumerates one folder exactly. Title and `fullText`
searches are for when you do not know where something lives.

Walk down: root → `_Brand/` or a course → unit → section → content folder. **One call per level.**
There is no recursive query, so scope the search rather than crawling the whole library.

## Before building anything

**Check whether it already exists.** A duplicate built because nobody looked is the most avoidable
kind of waste in this system, and the librarian's gap audits exist because it has happened.

Search the section's content folder first, then the whole unit, then the course by title.

## Reading

`read_file_content` handles Docs, Slides, Sheets, PDF, docx, xlsx, pptx, and images.
`download_file_content` returns raw bytes for anything else — build scripts, `.js`, `.py`, `.css`.

Drive returns markdown with escaped punctuation. **Normalise it before using the content**, and say
you did.

## What to report

The file's **ID**, title, full path, size, and modified time — not just "found it." The ID is what
every later operation needs, and the path is how the user finds it themselves.

If several candidates match, list them and ask. **Never guess which of two similarly-named files is
the real one.**

## Limits

Read-only. Creating, renaming, moving, or trashing is `shelve-drive-file` and the Librarian's
authority, not this skill's.
