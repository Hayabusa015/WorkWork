# SHULL-CHG-0100 — New document type: `Roadmap` (the Unit Roadmap page)

> **No conflict with a LOCKED rule.** This adds one type to the fixed list in `standards/NAMING.md`
> §2. It changes no existing type and no grammar.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0100 |
| **Date** | 2026-11-23 |
| **Source** | User. Matt, in conversation, 2026-11-23, about the one-page Unit 6 overview built that week, verbatim: "For each unit I want to create this. This was a great template id like to add at the beginning of my unit binder I have in my classroom.. What can we call it". Offered `Organizer` (existing type) or a new type; he chose a new one by name. |
| **Current Rule** | `standards/NAMING.md` §2: "**Types:** `Slides` · `Guided_Notes` · `Practice_Set` · `Quiz` · `Test` · `Lab` · `Study_Guide` · `Reference` · `Key` · `Rubric` · `Activity` · `Organizer`" |
| **Proposed Rule** | Same list with `Roadmap` added after `Organizer`, and one sentence: "`Roadmap` is the one-page unit opener filed at the front of a unit's binder section: unit header, big idea, prerequisites, every section with its I-can statements and standards, and how learning is measured. Always unit-level, never keyed: `Unit 6 Roadmap - [Unit Title].pdf`." |
| **Supersedes** | `standards/NAMING.md` §2, Types list (extends it). |
| **Reason** | Matt wants the page for every unit, all three courses, as the first page of each unit's binder section. No existing type fits cleanly: `Reference` is test-usable packet material, and `Organizer` is a student-completed sheet. A naming type affects all three courses, so it is a standard (CLAUDE.md §2 test). |
| **Affected Agents** | Designer (builds it), Librarian (files it), Auditor. |
| **Affected Skills** | naming (reads `standards/NAMING.md`; no copy of the list found in `.claude/skills/naming/`). `templates/_shull_name.py` and `templates/shull_name.cjs` accept any type string, so no code change is needed. |
| **Affected Courses** | All three. |
| **Risk** | Low. One naming collision to note: the Chemistry course-level front-of-binder guide is also called a "Roadmap" in `courses/chemistry/DECISIONS.md` ("Matthew's front-of-binder Chemistry Roadmap"). The filenames cannot collide: that one is course-level, a Unit Roadmap always starts `Unit N`. |
| **Recommendation** | Approve. Builder: `templates/unit-roadmap/`. |
| **Decision** | Approved by the user in chat, 2026-11-23: "Unit Roadmap", answering "For the Unit Launch page in WorkWork, which filename type should it use?" (offered: Organizer, or a new 'Unit Launch' type). Names the type `Roadmap`; the page is the Unit Roadmap. Recorded by the main session (§4.1). |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |
