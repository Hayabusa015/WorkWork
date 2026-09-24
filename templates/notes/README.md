# Guided / Cornell notes

**Authority:** `governance/proposals/SHULL-CHG-0025-notes-paged-redesign.md` for the paged layout
described here. Approved 2026-09-23.
`governance/proposals/SHULL-CHG-0030-notes-old-headers.md` for the headers on it: the
SHULL-CHG-0014 packet opening, section title bar, learning target line and course-colour row
labels, restored on 0025's pages. Approved 2026-09-23. Also
`governance/proposals/SHULL-CHG-0014-guided-notes-template.md` (the template, and `.docx` as the
production format), SHULL-CHG-0015 (bare list numbers), SHULL-CHG-0016 (work boxes),
SHULL-CHG-0017 (course profiles, stacked fractions), SHULL-CHG-0018 (the cue column).

## Build

```bash
python3 templates/notes/build_notes_docx.py specs/<spec>.json out.docx --verify   # Option A
python3 templates/notes/build_notes.py      specs/<spec>.json out.pdf             # Option B
```

**Option A is the production path.** It is a `.docx` because guided notes are the one document
Matthew edits before class (SHULL-CHG-0014). `--verify` converts the file with LibreOffice and
**fails if any designed page spilled onto a second sheet.** It also fails if LibreOffice is not
installed, rather than skipping the check.

The Chemistry U1 packet is the reference spec:

```bash
python3 templates/notes/specs/make_chem_u01_s01.1-s01.5_notes.py   # writes the _student and _key JSON
```

Edit the generator, not the JSON. Images a spec uses live in `templates/notes/assets/` and are
named per `standards/NAMING.md` §3 (lowercase, no `SHULL_` prefix).

**Option B is the old layout and reads only the old flat schema** (rows directly under each section).
It has no work box, equation toolbox, cover, or concept review page. It refuses a spec that uses
`problem`, `equations` or `diagram` rather than dropping them. Do not use it for a paged spec.

Both builders check every section code against that course's `DECISIONS.md` before building, and
both take colour from `brand/tokens.json`. No hex is typed in either.

## The page, and why it is this way

A packet is a set of **designed pages. Each designed page is one sheet of paper.**

| Page | What is on it |
|---|---|
| **Cover** | The SHULL-CHG-0014 packet opening (SHULL-CHG-0030): the course-colour `SHULL SCIENCE · JAMES A. GARFIELD LOCAL SCHOOLS` line, the unit title in caps (read from `DECISIONS.md` and never typed in a spec), the `GUIDED NOTES · PHASE nn · N SECTIONS` kicker, closed by a heavy course-accent rule, with an optional image at the right. Then Name/Date/Period in a hairline outline; **Unit learning targets ∥ Key terms**; **How these notes work**, with the accent rule down its left; **Sections in this unit**, a box to tick per section with its difficulty rating at the right; and the **Equation toolbox** at the foot. |
| **Content pages** | A new page per section. **Its first page opens with the section title bar**: the section title, the code at the right (`U01 / S01.2`, zero-padded per SHULL-CHG-0007), an ink rule above and a heavy course-accent rule below. Then the **`LEARNING TARGET` line**, closed by a hairline. **Continuation pages carry no head** (SHULL-CHG-0030 choice c); they start on their blocks. About three **blocks** a page; a section usually spans two pages. |
| **Concept review** | The standing last page, opened by the same title bar with the unit code (`U01`) and the spec's subtitle under it: per section, a short explanation, an optional two-column comparison, and a *Watch out* line. Then **Quick recall / cover the explanations above**. |

**A block is open, not boxed.** It has two columns split by one thin vertical rule, and one
horizontal rule separates it from the next block. It has no outer box and no cell borders.

- **Cue side (1.28 in, SHULL-CHG-0018):** the **cue label** in bold caps in the course's text-safe
  colour, then the cue questions in small grey type. RECALL / RECAP / REVIEW blocks put their tag
  above the label. **No block number** (`01`, `02`): SHULL-CHG-0030 dropped it (choice d). **No
  line under a cue.** Recall happens in the RECALL block and on the concept review page.
- **Capture side (6.22 in):** the **notes heading** in tracked bold caps in the same colour, then
  prompts with a writing line, fill-in tables, the flowchart, worked examples and must-write
  lines.
- **Where the two labels come from.** An old spec names both, `cueLabel` and `notesLabel`, and each
  is printed as written. A paged spec's block has a `title` and at most a `notesLabel`. The title,
  in caps, becomes the cue label. The notes heading is printed only when the spec gives a
  `notesLabel` or the heading differs from the cue label, so a block never shows the same words
  on both sides. A label the spec wrote is never upper-cased by the builder (Physics has a
  variable `a` in one).
- **Foot:** one quiet `Extra notes:` line, for whatever goes on the board that the prompts did not
  plan for.

**Every section ends with a RECALL block**: *close your notes before you write*, a summary prompt,
ruled writing lines (`"lines"`, default 3, sized to the key's answer), and the self-check boxes. A
RECALL block is never stretched to fill a page, because blank space under a checklist reads as an
unfinished box. Other kinds of block are **RECAP** (a short set of
reminders) and **REVIEW** (the unit close: big picture, checklist, *Still fuzzy on*).

**Greyscale, with a thin course accent in the headers** (SHULL-CHG-0030, choice a). Body type is ink
or label grey, and body rules are the hairline token. Course colour appears in two forms only,
both from `brand/tokens.json`, and never as a fill (`SHULL_DESIGN_SYSTEM.md` §8):

- **Rules** in the course `primary` (`pal.rule_accent`): the heavy rule under the cover masthead and
  under each section title bar, and the rule down the left of *How these notes work*. `primary` is
  never used for type; its measured `onWhiteVerdict` is *NOT TYPE* in all three courses.
- **Label type** in the course `primaryDeep` (`pal.type_accent`, text-safe on white): the school
  line, cover labels, the section code, `LEARNING TARGET`, and the cue label and notes heading.

Everything else is greyscale, including the must-write rule, work boxes and fill-in tables. The
shared primitives get a grey palette (`GreyPalette`), so they draw in the notes' voice.

`SHULL_DESIGN_SYSTEM.md` §8 sanctions a very light tint in only two places, and this template uses
exactly those two. Both use `pal.surface` (`ground.parchment`) through `shade()`:

1. the **header row of a fill-in table**, and
2. the small **RECALL / RECAP / REVIEW tags**. These are labels, not list numbers.

Nothing else is shaded: not the cue column, not a row, not a title bar, not any section-sized area.
`audit_print_ink.py` checks it.

**Must-write lines** (the highlighted must-write blocks on the slide) print in bold with a **grey rule down the left
edge**.

**A problem to solve gets a box to solve it in** (SHULL-CHG-0016). It is laid out as bold inline
`Given:` / `Find:` lines, then a bordered box labelled *WORK / show your reasoning and units*, then
the answer line. The box is **at least 1.4 in** tall and grows but never splits. A spec can ask for
a taller box, never a shorter one. If a page cannot hold the box, re-balance the page instead.

**A flowchart** (one root, two branches, two leaves under each; the S1.1 matter chart is the first)
is drawn as a picture: Pillow, Archivo from `brand/fonts/`, ink only, hairline boxes, thin diagonal
connectors. Word cannot draw a diagonal connector inside a table reliably. **The labels come from
the spec**; the template owns only the shape. The student copy prints only the root, and the key
fills every box. Both use the same geometry.

**Difficulty ratings are a standard cover feature.** Every section in the *Sections in this unit*
checklist carries a 1–10 difficulty, printed `n / 10` at the right under a `DIFFICULTY` label, with
the spec's `difficultyNote` under the list. The
values are course content, so they come from the spec (`cover.sections[].difficulty`). The
template never assigns them, and the build warns if a section in a paged spec has none. An old flat
spec has no ratings to carry over, so its cover drops the column rather than inventing numbers.

**The cover prints only what the spec holds** (SHULL-CHG-0030). A paged spec may give the 0014
front matter under `cover` (`kicker`, `fields`, `unitTargets`, `keyTerms`, `howItWorks`,
`sectionList`). What it leaves out is derived from the spec, and the build lists what it derived:

| Missing | Derived from |
|---|---|
| `kicker` | `GUIDED NOTES · PHASE nn · N SECTIONS`. The phase is read from the course `DECISIONS.md` phase headings (`unit_phase()`); a course with no phases (Geology) drops it. A key adds `· TEACHER KEY`. |
| `unitTargets` | The sections' own `learningTarget`s, in order. If there are none, and no key terms, the box is left out. |
| `howItWorks` | `howToUse`, one bullet per sentence. |
| `sectionList` | Each section's code and title. |
| `fields` | `NAME ___ DATE ___ PERIOD ___`. |

`cover.sections[].blurb` is no longer printed. The unit learning targets carry that role on the
same page. A page's `subtitle` is no longer printed either: continuation pages have no head.

**Isotope names never break at the hyphen.** `Cl-35`, `Cu-63` and `Iron-56` are written with the
non-breaking hyphen (U+2011, in Archivo), so a line cannot end on "Cl-".

**Footer on every page:** `SHULL SCIENCE / <COURSE> / UNIT ##` on the left and a two-digit page
number on the right. The page number is a Word `PAGE` field, so it stays right after an edit. Word
honours its `\# "00"` switch, and LibreOffice honours the section's `decimalZero` format. The
builder sets both.

## How a page is held to one sheet

A `.docx` has no layout of its own; the reader lays it out. So the builder predicts it:

- Every paragraph is pinned to an **exact line height**. At "single" spacing Word sizes an Archivo
  line at 1.51× the point size and LibreOffice at 1.09×, so an unpinned page is a different height
  in each.
- `estimate_height()` (in `_shull_docx.py`) measures the XML that was actually written. It uses the
  shipped Archivo metrics for line wrap.
- Each page's spare height is shared across its blocks. Every block rises to a common level, up to
  `MAX_STRETCH_PT` above its own height, so the blocks fill the sheet and end at its foot.
- A page predicted to overflow is reported at build time. `--verify` confirms it against the real
  render.

If a page is over, **move a block to the section's other page or tighten spacing.** Never shrink
type to fit, and never shrink the work box.

## Spec schema

```jsonc
{
  "course": "chemistry",               // chemistry | physics | geology
  "unit": 1,                           // the unit title is read from DECISIONS.md
  "key": false,                        // true = teacher key: answers shown, flowchart filled
  "cover": {
    "image": {"path": "../assets/x.png", "widthIn": 1.95},   // optional; relative to the spec
    "sections": [{"code": "1.1", "blurb": "…", "difficulty": 1}],   // difficulty 1–10, course content
    "difficultyNote": "Estimated for …",
    "equationToolbox": {
      "label": "Equation toolbox",
      "columns": [{"heading": "…", "lines": ["protons = Z",
                                            {"lhs": "Fractional abundance",
                                             "num": "percent", "den": "100"}]}],
      "notes": ["Z = atomic number; A = mass number."]
    },
    "keyTerms": [{"code": "1.1", "terms": ["Matter", "pure substance"]}],   // one line per section
    "howToUse": "One short paragraph.",          // a bullet per sentence under "How these notes work"
    // Optional, SHULL-CHG-0030. Derived from the spec when absent - see "The cover prints only
    // what the spec holds".
    "kicker": "GUIDED NOTES  ·  PHASE 01  ·  3 SECTIONS",
    "fields": "NAME  ____   DATE  ____   PERIOD  ____",
    "unitTargets": ["I can …"],
    "howItWorks": ["…", "…"],                    // takes precedence over howToUse
    "sectionList": ["S01.1   Title"]            // replaces the derived list; drops difficulty
  },
  "sectionsContent": [{
    "code": "1.1", "title": "…", "learningTarget": "…",
    "pages": [{
      "subtitle": "…",                             // not printed since SHULL-CHG-0030
      "rows": [
        {"title": "Vocabulary", "cues": ["…?"],
         "cueLabel": "BASICS",                        // optional; default: title in caps
         "notesLabel": "COPY THE FLOWCHART",          // optional; default: title in caps. Printed as written
         "notes": [
           "DEFINE: matter",                             // prompt + 1 writing line (2 if it ends in ?)
           {"prompt": "DEFINE: matter", "answer": "…"},  // the key prints the answer, bold, in the line's place
           "*A must-write line.",                        // bold, grey rule down the left
           {"text": "**Bold lead:** plain rest."},       // a statement, no writing line
           {"check": "I can …"}, {"label": "…"}, {"lines": 2}
         ],
         "table": {"headers": [], "rows": [[]], "widths": [], "rowHeightIn": 0.34},
         "flowchart": {"root": "MATTER", "branches": ["…", "…"],   // labels are content: the
                       "leaves": ["…", "…", "…", "…"]},            // student copy prints only the root
         "problem": {"statement": "…", "given": ["line 1", "line 2"], "find": "…",
                     "workHeightIn": 1.4, "answer": "… = _____",
                     "solution": ["key only: lines written inside the work box"]},
         "diagram": {},                                  // Geology figure-to-label, unchanged
         "noWorkBox": true,                              // explicit opt-out, see below
         "extraNotes": false},                           // default true for notes/recap blocks
        {"kind": "example", "title": "Neutral iron-56", "cues": ["…"],
         "problem": {}},                                 // a worked example: MUST carry a problem
        {"kind": "recall", "title": "Section summary", "cues": ["…"], "lines": 3,
         "prompt": "…", "answer": "key only", "selfCheck": ["…"]},
        {"kind": "recap",  "title": "…", "cues": ["…"], "notes": [{"text": "…"}]},
        {"kind": "review", "title": "Pulling it together", "cues": ["…"],
         "bigPicture": "…", "checklist": ["…"], "fuzzyLabel": "Still fuzzy on / bring to review day:"}
      ]
    }]
  }],
  "conceptReview": {
    "title": "…", "subtitle": "…",                   // title bar with the unit code, U##; subtitle under it
    "sections": [{"code": "1.1", "heading": "…",
                  "paragraphs": [["line", "line"], ["next group"]],   // **bold** allowed
                  "compare": {"left": {"heading": "…", "lines": []},
                              "right": {"heading": "…", "lines": []}},
                  "watchOut": "…"}],
    "quickRecall": ["…?"]
  }
}
```

`**bold**` works in any text. Use Unicode subscripts (O₂, mass₁) and the minus sign (−); Archivo
carries them. **Do not use ☐ or emoji.** They are not in Archivo and pull a second font into the
PDF. Checkboxes are drawn by `checkbox()`.

A student copy and its key are **the same structure with answers filled**. Generate both from one
source so they cannot drift.

**Old flat specs still build.** A spec with `rows` directly under each section and no `pages` is
upgraded at build time by `normalize_legacy()`:

- Each row keeps its `cueLabel` and `notesLabel`, printed as written in course colour. Its `title`
  (the `cueLabel` in title case) names it in build messages. A row with a problem becomes
  `"kind": "example"`.
- Rows are packed onto pages by measured height, three blocks per page at most. A closing RECALL
  or REVIEW block joins the page before it whenever it fits.
- The first page of each section opens with its title bar and learning target. Later pages have no
  head.
- `summaryPrompt` / `selfCheck` become a RECALL block, and `close` becomes a REVIEW block.
- The cover carries the old front matter as written (SHULL-CHG-0030): `kicker`, `fields`,
  `unitTargets`, `keyTerms`, `howItWorks` and `sectionList`. Three corrections only:
  - section codes in the kicker and section list are zero-padded (`S1.2` → `S01.2`,
    SHULL-CHG-0007);
  - `howItWorks` names the rule the page actually draws: "a teal rule" or "a gold rule" becomes
    "a gray rule", because the must-write rule is grey (SHULL-CHG-0025, kept by 0030);
  - "summary box" becomes "RECALL block", there and in the closing checklist.

Nothing else is rewritten. The build warns when there is no `conceptReview`.

## Refused at build time

- A section code (in the sections, the cover, key terms, or the concept review) that is not in
  `courses/<course>/DECISIONS.md`.
- **The work-box check (SHULL-CHG-0016), which does not depend on how a block is titled:**
  - a `"kind": "example"` row with no `problem`;
  - a `problem` on a row that is not `"kind": "example"`, so the declaration and the box always
    agree;
  - a notes block with nothing on its capture side;
  - as a second net, a notes block titled or labelled EXAMPLE / PRACTICE / PROBLEM / SOLVE /
    CALCULATE / YOUR TURN with no `problem`. Opt out with `"noWorkBox": true`, explicitly.

  **Known limit.** The check reads structure, not intent. A worked example stripped of *both*
  `"kind": "example"` and its `problem`, whose title carries none of those keywords (for example
  "Neutral iron-56"), and which still has a prompt on its capture side, is an ordinary notes block
  as far as the builder can tell. It builds, and it has no work box. Nothing in the row says it
  was a problem to solve. Reviewing a spec diff that deletes a `problem` block is the guard
  for this case.
- Geology with an equation toolbox or a problem block. Geology has no math (SHULL-CHG-0017).
- Physics or Chemistry with problems but no equation toolbox, unless `"noEquationBar": true`.

## Print ink: measured

```bash
python3 scripts/audit_print_ink.py out.pdf
```

`SHULL_DESIGN_SYSTEM.md` §8 bans full-page banners, shaded section backgrounds, and **solid-fill
headers.** The audit reports three things, and they are not the same:

- **`toner`** is ink volume, the mean darkness of the page. This is the budget.
- **`marked`** is the share of the page carrying any mark. It measures density, not ink: a pale tint
  marks every pixel it covers and spends almost no toner. It is reported but fails only at an
  extreme.
- **`widest solid band`** is geometry. This is the one the standard fails immediately, and it
  catches a header going back to a fill. The parchment tints on table headers and tags stay far
  above its darkness threshold and measure 0.00 in.

The thresholds are calibrated to Matthew's own files: his GEO packet ran 3.09% toner, his old PHYS
practice set 8.15%. Reading `marked` as the ink budget was a separate mistake, corrected in
SHULL-CHG-0020.

## QA

```bash
python3 templates/notes/build_notes_docx.py spec.json out.docx --verify
soffice --headless --convert-to pdf out.docx
python3 scripts/audit_fonts.py out.pdf          # Archivo only
python3 scripts/audit_print_ink.py out.pdf
```

Then look at every page, next to the slide deck it belongs to.
