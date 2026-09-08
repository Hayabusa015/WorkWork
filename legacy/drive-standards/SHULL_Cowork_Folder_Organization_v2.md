# SHULL Classroom Files — Folder Organization (v2)

Supersedes `SHULL_Cowork_Folder_Organization.md`. Read this before saving any file.
Changes in v2 are marked **NEW**.

---

## Folder structure

```
_Brand/                                    NEW — shared, not course-specific
├── Templates/
│   ├── SHULL_Science_Slide_Template.pptx
│   └── [future: reference sheet, lab doc templates]
├── Image Library/                         NEW
│   ├── Chemistry/
│   ├── Physics/
│   ├── Geology/
│   └── Shared/                            glassware, notebooks, benches
└── Standards/
    ├── SHULL_Slide_System_v2.md
    ├── SHULL_Image_Prompt_Pack.md
    └── ANTI_AI_SLOP_EDUCATOR_STANDARD.md

[Course]/                                  Chemistry, Physics, Geology
├── Unit 01 - [Unit Name]/
│   ├── Section 01.1 - [Section Name]/
│   │   ├── Homework/
│   │   ├── Presentations/
│   │   ├── Guided Notes/
│   │   ├── Tests-Quizizz/
│   │   └── Labs-Case Studies-Projects/
│   └── Section 01.2 - [Section Name]/
└── Unit 02 - [Unit Name]/
```

`_Brand` sorts to the top with the leading underscore. It holds anything used by
more than one course — one copy, not three drifting copies.

---

## Naming

**Folders**
- Units: `Unit ##` zero-padded + short title — `Unit 08 - Chemical Reactions`
- Sections: `Section ##.#` + short title — `Section 08.4 - Balancing Equations`
- Content folders: exactly these five, same spelling and order, every time —
  `Homework`, `Presentations`, `Guided Notes`, `Tests-Quizizz`,
  `Labs-Case Studies-Projects`

**Files**
`SHULL_[COURSE]_[Type]_U##_S##.#_[Descriptor].[ext]`

- `SHULL_CHEM_Slides_U08_S08.2.pptx`
- `SHULL_PHYS_Guided_Notes_U02_S02.3.docx`
- `SHULL_GEO_Practice_Set_U04_S04.1.pdf`

**Images — NEW.** Slide art is not a course document and does not take a
`SHULL_` prefix. It lives in `_Brand/Image Library/` and uses the slot name it
was generated for:

`[course]_u##_s##.#_[subject].png` → `chem_u01_s1.2_rutherford.png`

Shared backgrounds drop the unit code: `bg_glassware.png`, `bg_notebook.png`.

---

## What goes where

| Folder | Contents |
|---|---|
| Homework | Practice sets, worksheets, take-home work, homework keys |
| Presentations | Decks built on the slide template, plus exported PDFs |
| Guided Notes | Cornell/guided packets, student copy **and** filled teacher key |
| Tests-Quizizz | Quizzes, unit tests, exit tickets, bell ringers, A–D versions, keys |
| Labs-Case Studies-Projects | Lab handouts, case studies, project instructions, rubrics |

---

## Rules

1. Resolve Course → Unit → Section → content type **before** saving.
2. Reuse existing folders exactly, checking case-insensitively. Never create
   `Tests` beside `Tests-Quizizz`.
3. Create missing Unit/Section folders using the rules above.
4. If the unit or section is unclear, **ask** — do not default to a misc folder.
5. `U##` / `S##.#` codes must match the slide footer, the notes header, and the
   course organizer. These are one system.
6. **NEW —** Never copy a template into a course folder. Course decks reference
   `_Brand/Templates/`. One template, one place to fix it.
7. **NEW —** An image used by two courses moves to `Image Library/Shared/`
   rather than being duplicated.
