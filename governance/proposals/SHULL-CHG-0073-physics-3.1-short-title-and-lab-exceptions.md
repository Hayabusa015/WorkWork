# SHULL-CHG-0073 — Physics: short title for 3.1, one-time lab-template exceptions for "3.1 Lab - Newton's Laws", and lab equipment inventory

> **Path A (course change).** Every edit proposed here is to `courses/physics/DECISIONS.md`. The
> shared lab template (`templates/lab/`), the `build-lab` skill and `standards/NAMING.md` are **not**
> changed.
>
> **Departs from template rules the template itself calls locked. Marked, not resolved.** Part 2
> asks for one-time departures from rules that `templates/lab/README.md` files under "What's locked
> and why", and that the `build-lab` skill lists under "The rules that are not yours to change".
> Matt gave the instructions himself (CLAUDE.md precedence 1), but only Matt can confirm the scope.
> Section 3 lists two places where his instructions meet a **CONFIRMED Physics course rule**. They
> are open questions for him, and this record does not settle them.
>
> **Resolved by the Decision (`d54b28e`).** Departure 1: the post-lab keeps one short error-source
> question, so no exception to the Physics **Labs** rule is taken. Departure 2: covered by Matt's
> direct request for the example table. The text above is kept as written when proposed.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0073. The main session reports the ID was checked free against a freshly fetched `origin/main` before the push of `d54b28e` (branch `claude/focused-mendel-cefeca`). The Secretary confirmed from `.git` refs that `d54b28e` is the branch head and was pushed, but could not re-run the ID check. |
| **Date** | 2026-11-12 |
| **Source** | User. Matt, in chat on 2026-11-12, while building the Physics 3.1 lab. His words are quoted verbatim in sections 1, 2 and 4. |
| **Current Rule** | (1) `courses/physics/DECISIONS.md`, "Short titles": no row for `3.1`. `standards/NAMING.md` line 38: "**No row, no topic**: the name is `1.3 Lab.pdf`." (2) Lab template rules, quoted verbatim in section 2.2. (3) `courses/physics/DECISIONS.md`, Open questions, item 7: "**Lab equipment inventory** and realistic lab frequency." |
| **Proposed Rule** | Sections 1.2, 2.3 and 4.2. These are three edits to `courses/physics/DECISIONS.md`: one table row and two decision-log entries. |
| **Supersedes** | Short title: nothing (adds a row). Lab exceptions: nothing. They are a one-time exception for one lab, like the 2026-09-14 S1.3 entry, and every template rule continues to govern every other lab. Inventory: partly answers Open question 7. The question stays open for "realistic lab frequency". |
| **Reason** | (1) Without a row, the lab must be named `3.1 Lab.pdf`, with no topic. Matt approved "Newton's Laws" so the topic can appear. (2) The lab uses only carts, sensors and masses. Matt said directly that a safety section and a disposal section do not apply, and asked for a more useful data example and shorter question sets. (3) Matt confirmed the equipment in chat. Recording it in DECISIONS means future Physics labs do not have to ask again. |
| **Affected Agents** | Designer (builds the lab). Auditor (checks it against the template). Secretary (implements). |
| **Affected Skills** | `build-lab` (its rules are departed from for this one lab only, and the skill file is not edited). |
| **Affected Courses** | Physics only. |
| **Risk** | Low for the short title and the inventory. Medium for the lab exceptions. They depart from rules the template calls locked, and two of them meet CONFIRMED Physics course rules (section 3). The scope is one document, and it is stated as not a precedent. |
| **Recommendation** | Approve part 1 and part 3 as written. Approve part 2 once Matt has answered the two questions in section 3. Where his chat instructions already cover a point, the record follows them. |
| **Decision** | Approved by the user in chat. Short title, 2026-11-12: "yes use Newton's Laws as the short title". Lab exceptions A-D by his direct instructions of 2026-11-12, quoted in this record ("Remove safety section, its just carts", "remove disposal, nothing is disposed of", "create a better example of the data and what the table should actually look like in their lab notebook", "Reduce reduce the amount of prelab questions to just whats important", "i want this simple and straightforward"). Equipment inventory as he confirmed it in chat 2026-11-12. Departure 1 (error-source item): the main session keeps one short error-source question in the post-lab, so no exception to the Physics Labs rule is taken. Recorded by the main session (§4.1). |
| **Status** | **APPROVED** |
| **Implemented By** | Decision recorded in `d54b28e` (branch `claude/focused-mendel-cefeca`). The Secretary wrote the edits on 2026-11-12 and did not commit them: `courses/physics/DECISIONS.md` (the `3.1` short-title row, two 2026-11-12 decision-log entries, Open question 7 reworded, "Last updated" date), a `change-log/CHANGELOG.md` row, and this record. The main session commits them. **SHA of that commit: pending, add it here.** |
| **Verified** | Partly. The Secretary checked by reading and searching the changed files. The `3.1` row uses a straight ASCII apostrophe (U+0027), and no U+2019 appears in `courses/physics/DECISIONS.md`. Both entries sit at the top of the log, above the 2026-11-11 entries. No validator was run, because the Secretary has no shell. Still to check: run the repository validators, and confirm the commit diff touches only the three files listed. Templates and outputs were not touched. |

---

## 1. Short title for 3.1

### 1.1 Matt's answer (verbatim)

Asked: "approve 'Newton's Laws' as the short title for 3.1, so it can appear in the file name?"

> "yes use Newton's Laws as the short title"

2026-11-12.

### 1.2 Proposed edit

Add one row to the "Short titles" table in `courses/physics/DECISIONS.md`, in code order after `1.4`:

```
| 3.1 | Newton's Laws |
```

Checks against `standards/NAMING.md` §2 / SHULL-CHG-0041:

- 13 characters, within the 20-character limit.
- No character from the forbidden list `: / \ * ? " < > |`.
- It is the full section title from the curriculum map (`3.1` Newton's Laws), not shortened.

**Note for implementation.** Use the straight ASCII apostrophe (U+0027), as the curriculum map
does. A curly apostrophe (U+2019) would make the filename differ from what someone types. No
existing short title contains an apostrophe, so there is no precedent to follow.

Resulting filenames: `3.1 Lab - Newton's Laws.html`/`.pdf` and `3.1 Lab Key - Newton's Laws.html`/`.pdf`.

## 2. One-time lab-template exceptions: "3.1 Lab - Newton's Laws" only

### 2.1 Matt's instructions (verbatim, 2026-11-12)

| # | Exception | Matt |
|---|---|---|
| A | Remove the Safety section | "Remove safety section, its just carts." |
| B | Remove the Disposal section, including the Alconox items 4–6 | "remove disposal, nothing is disposed of." |
| C | The data-table section shows a filled EXAMPLE table instead of skeletons only | "can you create a better example of the data and what the table should actually look like in their lab notebook." |
| D | A reduced pre-lab and a simplified post-lab | "Reduce reduce the amount of prelab questions to just whats important" and "i want this simple and straightforward." |

These are by Matt's direct instruction (CLAUDE.md precedence 1, `governance/GOVERNANCE.md` §3).

### 2.2 The rules being departed from, and their labels

No file attaches a `governance/GOVERNANCE.md` §4 label (LOCKED / INHERITED / PROVISIONAL) to any
lab-template rule. The table gives the strongest wording each source uses. Where that wording says
"locked", the record treats the rule as locked. The template is built from Matt's confirmed Intro
Skills Lab ("That lab's structure is the standard", README line 8).

| Exc. | Rule (verbatim) | Where | Label |
|---|---|---|---|
| A | Student section order: "→ **Safety** (specific PPE and named hazards, spill and exposure response) →" | `templates/lab/README.md` line 112, "Student section order" | No formal label. It is outside the README's "What's locked and why" heading. The skill says "**Do not redesign the lab template.** ... its structure is the standard." Treated as **confirmed structure, not labelled LOCKED**. |
| A | "Never generic. One bullet per real hazard. Include the disposal-of-broken-glass line and the spill line every time." | `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` lines 333–335, `BLOCK: SAFETY` | Same as above. Line 18 of the template says "Delete any block you do not need", but the README section order lists Safety as a required section for Chemistry and Physics. Only Geology is allowed to drop it ("without the full pre-lab, safety, and disposal apparatus unless a real hazard is present", README lines 146–148). |
| B | "**Alconox cleanup block.** Disposal items 4–6 are standing boilerplate. **Keep them verbatim.** Only items 1–3 change per lab." | `templates/lab/README.md` lines 102–103, under "What's locked and why" | **Locked** in the template's own words. |
| B | "**The Alconox block** — disposal items 4–6 — is standing boilerplate. **Keep it verbatim.**" | `.claude/skills/build-lab/SKILL.md` lines 31–32, under "The rules that are not yours to change" | **Locked** in the skill's own words. |
| B | "Keep items 4-6 verbatim on every lab." | Template lines 551–553, `BLOCK: DISPOSAL AND CLEANUP` | Same. |
| B | Student section order: "→ **Disposal and Cleanup** (exact location and method) →" | README lines 115–116 | Confirmed structure, not labelled. |
| C | "**No write space on the handout.** No ruled lines, no answer blanks, no fillable data tables. ... the table skeletons on page 2 exist to be copied, not filled." | README lines 89–91, under "What's locked and why" | **Locked** in the template's own words. |
| C | "No write space on the handout. ... Table skeletons exist to be **copied**, not filled." | Skill lines 26–28, under "The rules that are not yours to change" | **Locked** in the skill's own words. |
| C | "These are for students to COPY into the notebook. They are never filled in on this handout." | Template lines 375–377, `BLOCK: DATA-TABLE SKELETONS`. Template header lines 22–27: "RULES BAKED IN — DO NOT OVERRIDE ... no fillable data tables on the handout." | **Locked** ("DO NOT OVERRIDE"). |
| D | "**Pre-Lab** (2–3 conceptual, 3–4 procedural-reading, at least one safety or disposal check)" | README lines 113–114 | Confirmed structure, not labelled. |
| D | "Confirmed mix: 2–3 conceptual · 3–4 procedural-reading · 1 safety/disposal · 1 final item that makes them draw their own data tables." | Template lines 355–357, `BLOCK: PRE-LAB QUESTIONS` | "Confirmed", not labelled LOCKED. |
| D | "**Post-Lab Analysis** (2–3 "what happened and why", calculations with work and units, percent error with the accepted value supplied, error analysis naming a real procedural cause)" | README lines 116–118 | Confirmed structure, not labelled. |
| D | "Confirmed mix: 2–3 "what happened and why" tied to the lesson · the required calculation with percent error · 2 error-analysis items that name a real procedural cause · 1 item connecting back to an earlier section." | Template lines 580–583, `BLOCK: POST-LAB QUESTIONS` | "Confirmed", not labelled LOCKED. |

Exception C does **not** depart from the ink rule (README lines 84–87). The example table stays
outline-and-rule only, with no filled header.

### 2.3 Proposed decision-log entry (top of the Physics decision log)

```markdown
### 2026-11-12 — One-time lab-template exceptions: "3.1 Lab - Newton's Laws"
Matt asked for four departures from the lab template (`templates/lab/README.md`,
`.claude/skills/build-lab/SKILL.md`) for this one lab, by direct instruction:

1. **No Safety section.** Matt: "Remove safety section, its just carts." The README section order
   lists Safety for every Chemistry and Physics lab.
2. **No Disposal and Cleanup section, Alconox items 4–6 included.** Matt: "remove disposal, nothing
   is disposed of." The README and the skill call items 4–6 standing boilerplate, kept verbatim on
   every lab.
3. **The data-table section shows a filled EXAMPLE table.** It shows the column headings with units
   and 1–2 sample rows, labelled "Example – your numbers will differ", instead of a blank skeleton.
   Matt: "can you create a better example of the data and what the table should actually look like
   in their lab notebook." The table is still for copying into the notebook. It is not a space to
   write in, and the ink rule is unchanged.
4. **Reduced pre-lab and simplified post-lab.** The pre-lab has a few questions, including "State
   each of Newton's three laws". The post-lab has one question per law plus the percent
   calculations. Matt: "Reduce reduce the amount of prelab questions to just whats important" and
   "i want this simple and straightforward." This replaces the template's question mix for the
   pre-lab (2–3 conceptual · 3–4 procedural · 1 safety/disposal · 1 table set-up) and the post-lab
   (2–3 what-happened · calculation with percent error · 2 error analysis · 1 connection).

The teacher key states each omission as deliberate, as the S1.3 key did for the Alconox block.

**Scope, stated plainly:**
1. Scoped to this one lab: `3.1 Lab - Newton's Laws.html`/`.pdf` and its `3.1 Lab Key - Newton's
   Laws` files.
2. **Not a precedent** for future Physics or Chemistry labs. A future lab needing any of these
   exceptions needs its own explicit request and its own record. It may not cite this one.
3. The shared lab template files (`templates/lab/SHULL_Lab_TEMPLATE_MASTER.html`,
   `templates/lab/SHULL_Lab_TEMPLATE_TEACHER_KEY.html`, `templates/lab/build_lab.py`), the
   `build-lab` skill and the README are **not** modified.

Supersedes: None.
Status: CONFIRMED · SHULL-CHG-0073 — Path A (course-specific; shared lab template untouched).
```

The entry's wording for items 4 and the error-analysis point depends on Matt's answers to section 3.
Adjust it before implementing.

## 3. Open questions for Matt (not resolved here)

Ask one at a time. Each answer changes what the lab contains.

1. **Error analysis in the post-lab.** "One question per law plus the percent calculations" leaves no
   error-analysis item. `courses/physics/DECISIONS.md`, "Physics-specific build rules — CONFIRMED",
   **Labs**: "require a **specific** named source of error. "Human error" is not an answer." Read
   literally, Matt's instruction (precedence 1) wins for this lab. But that course rule is
   CONFIRMED, and he did not mention it. Suggested question: "Keep one error-source question in the
   3.1 post-lab, or drop it for this lab only?"
2. **The example table and the Physics worksheet rule.** `courses/physics/DECISIONS.md`, "Worksheets
   — CONFIRMED": "Pre-lab and post-lab prompts follow the same rule: procedure and prompts only, no
   data tables or answer space. Students set up their own tables in the notebook as a pre-lab step."
   A labelled example with sample rows is not answer space. Read strictly, though, it is a data
   table with data in it. Matt asked for it directly, so this is likely covered. It is listed so the
   departure is visible.

Smaller points the builder should settle, not Matt unless they are unclear:

- **Table set-up item.** The template's last pre-lab item ("Set up your N data tables in your
  notebook") is how the Physics worksheet rule above is met. Recommended: keep it in the reduced
  pre-lab.
- **Percent error or percent difference.** "Percent calculations" does not say which. The S1.3 entry
  set the pattern: use percent error only where a real accepted value exists, and percent difference
  otherwise. The builder must not invent an accepted value.
- **Teacher key.** The README's teacher section includes "safety and disposal notes". Recommended:
  the key keeps a one-line teacher note saying the student sections were removed by Matt's
  instruction. It invents no hazard claim either way ("Never invent a safety claim").

## 4. Lab equipment inventory (partly answers Open question 7)

### 4.1 What Matt confirmed (chat, 2026-11-12)

| Item | Count / note |
|---|---|
| Vernier Go Direct Sensor Carts | 10, of which 2 are broken |
| Lab groups | 5 |
| Go Direct Force and Acceleration Sensor (GDX-FOR) | 5. These are Matt's separate force sensors. He uploaded its product photo on 2026-11-12. |
| Mass bars | Present. Count not given. |
| Pulley with hanging masses | Present. Count not given. |
| Spring bumpers | Present. Count not given. |
| Balance | Present. Count not given. |

The product photo was shared in chat. It is not in the repository. The sensor's specifications are
not recorded here, because none were confirmed.

### 4.2 Proposed edits to `courses/physics/DECISIONS.md`

**(a)** Under "Open questions", replace item 7 with:

```markdown
7. **Realistic lab frequency.** The equipment inventory is recorded (2026-11-12 decision-log
   entry, SHULL-CHG-0073). How often a lab can run is still open.
```

This is an edit to the open-questions list, not to the log. The original wording stays in git
history and is quoted in this record.

**(b)** Add a decision-log entry at the top of the log:

```markdown
### 2026-11-12 — Lab equipment inventory
Confirmed by Matt in chat: 10 Vernier Go Direct Sensor Carts, 2 of them broken · 5 lab groups ·
5 Go Direct Force and Acceleration Sensors (GDX-FOR), the separate force sensors · mass bars · a
pulley with hanging masses · spring bumpers · a balance. Counts for mass bars, hanging masses,
bumpers and balances were not given. Partly answers Open question 7. Lab frequency is still open.
Supersedes: Open question 7, for the inventory half only.
Status: CONFIRMED · SHULL-CHG-0073
```

**Placement question for implementation.** The 2026-09-14 S1.3 entry already records that students
use the Go Direct Sensor Cart on a Vernier Dynamics Track. Matt did not list the Dynamics Track on
2026-11-12. The entry above records only what he confirmed on that date, and it does not remove the
track.

## 5. What this record does not do

- It does not edit `courses/`, `templates/`, `standards/` or any skill.
- It does not change the lab template for any other lab.
- It does not answer the section 3 questions.
- It does not add a `change-log/CHANGELOG.md` row. The main session adds that when it commits this
  record.
