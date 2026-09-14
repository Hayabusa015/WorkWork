# SHULL-CHG-0023 — New lab master template (SHULL_Lab_Reference_Master.pdf)

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0023 |
| **Date** | 2026-09-14 |
| **Source** | User — Matt uploaded `SHULL_Lab_Reference_Master.pdf` (4 pages) and asked that it "become (or inform)" the authoritative `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` |
| **Current Rule** | See §1 below — verbatim, from `templates/lab/README.md` and `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` |
| **Proposed Rule** | See §2 below — verbatim, from the PDF as extracted |
| **Supersedes** | `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` (v1.1, adopted under SHULL-CHG-0010) in full structure, and the "Student section order" / "What's locked and why" sections of `templates/lab/README.md` — **partially, and not resolved by this record.** Several of the current LOCKED rules are in direct conflict with the new text; see §4. This record does not decide which side wins. |
| **Reason** | Matt wants a new reference master to become or inform the lab template used by the `build-lab` skill across Chemistry, Physics, and Geology. |
| **Affected Agents** | Secretary (implementation only, and only upon approval) |
| **Affected Skills** | `build-lab` |
| **Affected Courses** | All three — Chemistry, Physics, Geology |
| **Risk** | **High** — see §5 |
| **Recommendation** | Do not implement as a blind swap. Resolve the conflicts in §4 with Matt first — in particular, whether "become or inform" means full replacement or a partial merge, since large parts of the new text conflict with rules currently marked LOCKED. |
| **Decision** | *(pending)* |
| **Status** | **PENDING** |
| **Implemented By** | *(blank)* |
| **Verified** | no |

---

## 1. Current Rule — verbatim

### 1a. Student section order (`templates/lab/README.md`, "Student section order")

> Header (course, unit, section, lab code, Name/Date/Period, group line) → Topic/Goals → Purpose →
> Background (only the theory needed) → **Safety** (specific PPE and named hazards, spill and exposure
> response) → **Pre-Lab** (2–3 conceptual, 3–4 procedural-reading, at least one safety or disposal
> check) → Materials → **Procedure** (numbered major steps, bulleted substeps, exact quantities,
> times, temperatures, endpoints; formula name *and* formula) → Data/Observations → **Disposal and
> Cleanup** (exact location and method) → **Post-Lab Analysis** (2–3 "what happened and why",
> calculations with work and units, percent error with the accepted value supplied, error analysis
> naming a real procedural cause).

### 1b. What's locked and why (`templates/lab/README.md`, "What's locked and why")

> **Margins.** Per `brand/tokens.json` → `print.margins`. **Don't touch them to fix a page-count
> problem** — reduce body font size or line-height first.
>
> **Ink.** Outline and rule treatments only. No solid banners, no filled table headers, no shaded
> section backgrounds. Chips are outlined, not filled, and **a numbered list is just the number —
> no box** (SHULL-CHG-0015). This is the standing rule for every printed SHULL document, not a
> choice made for this template.
>
> **No write space on the handout.** No ruled lines, no answer blanks, no fillable data tables. **The
> lab notebook is the write-on surface and the carbonless copy is what gets graded.** The pre-lab
> makes students draw their own tables — the table skeletons on page 2 exist to be copied, not filled.
>
> **Colour** — *corrected from the original, which is superseded.* Values come from
> `brand/tokens.json`. White is the ground. Course identity colours apply across all media, not
> projection only. **Coloured type on a light ground uses the course `primaryDeep`** — the display
> colours fail as text on white.
>
> **The `<body>` course class** stays a structural hook. It may now carry a real colour difference,
> where it previously changed nothing visual.
>
> **Alconox cleanup block.** Disposal items 4–6 are standing boilerplate. **Keep them verbatim.** Only
> items 1–3 change per lab.
>
> **The teacher key is its own file.** Never appended to the student handout.

### 1c. From the HTML master itself (`templates/lab/SHULL_Lab_TEMPLATE_MASTER.html`, header comment)

> RULES BAKED IN — DO NOT OVERRIDE
> · Ink-friendly. Outline and rule treatments only. No solid fills, no shaded banners, no colored
>   table headers.
> · No write-lines, no answer spaces, no fillable data tables on the handout. The lab notebook is
>   the write-on surface. The pre-lab instructs students to draw their own tables.
> · Print palette is the same for all three courses. The per-course accent palettes are PROJECTION
>   ONLY and never touch a printed page. *(Corrected by SHULL-CHG-0010: this line is now false —
>   course colours apply to all media.)*
> · Margins are the confirmed SHULL print standard and are locked.

### 1d. Current structural facts (from the HTML, not restated as prose anywhere else)

- **Pre-Lab:** 9 numbered items (3 conceptual, 4 procedural-reading, 1 safety, 1 "set up your N data
  tables" item).
- **Procedure:** 4 parts, A through D, including `.flag` pills for cross-part timing ("START THIS
  BEFORE PART D" / "DO THIS WHILE PART C RUNS").
- **Reference data + figure:** a `.split` block pairing a reference-values table (`table.data`) with
  a hand-built SVG diagram side by side, each with its own caption.
- **Disposal and Cleanup:** 6 numbered items — items 1–3 lab-specific, items 4–6 the Alconox
  boilerplate, locked verbatim.
- **Post-Lab Analysis:** 6 numbered items, each carrying a `<span class="ref">` backlink tag naming
  the Part or section it draws on.
- **Footer/running head:** CSS `string-set` carriers. Bottom-left is fixed:
  `"SHULL SCIENCE · " string(coursename) " · " string(unitcode)`. Bottom-right is a free string set
  once (lab title + "CARBONLESS COPY GRADED INDIVIDUALLY"). Top-right running head changes per page
  via `.runhead` (e.g. "SAFETY & PRE-LAB", "PROCEDURE", "POST-LAB"). No per-page "LAB-0#" sub-code
  and no "n/4" page count appear anywhere.
- **QA checklist requirement** (`templates/lab/README.md`, "Before it goes to the copier"): *"U#/S#.#
  matches the document chip, the running footer, the filename, and the folder path. One system."*

---

## 2. Proposed Rule — verbatim, from SHULL_Lab_Reference_Master.pdf

*(The PDF binary is not saved in this repository. Per the convention at `templates/lab/README.md`
line 5–6, the original text is quoted here rather than snapshotted as a file.)*

### PAGE 1 — LAB-01 · LAB MASTER

```
SHULL SCIENCE · [[COURSE · UNIT · SECTION]]
[[Lab title and specific task]]
NAME / DATE / PERIOD
GROUP MEMBERS ____

GOALS
- [[Name two or three observable skills students will practice.]]
- [[State what they will determine, compare, or produce.]]

PURPOSE
[[Explain the actual job in two direct sentences. Say what students will find out and why the
measurements or observations matter.]]

BACKGROUND
[[Key idea]]. [[Give only the explanation needed to do the work. Connect the idea to the tool,
observation, or decision students will make.]]
[[A likely mix-up]]. [[Distinguish the two ideas students commonly confuse. State the consequence of
confusing them in this lab.]]

REFERENCE RELATIONSHIP
[[Formula name and formula with units, or a labeled visual model.]]
[[Interpreting the result]]. [[Explain what the result means and what it cannot establish. Define
any vocabulary used later in the analysis.]]

BEFORE LAB DAY
[[State exactly what students must read and prepare, where they should record it, and when it is
due. Retain notebook-based recording when the lab requires it.]]

Footer: SHULL SCIENCE · LAB-01 · LAB MASTER — 1/4
```

### PAGE 2 — LAB-02 · SAFETY AND PRE-LAB

```
SAFETY
- [[PPE and timing]]. [[Required protection and when it stays on.]]
- [[Named hazard]]. [[Specific behavior that controls it.]]
- [[Spill or exposure]]. [[Verified response and location of equipment.]]
- [[Equipment risk]]. [[Inspection or handling instruction.]]

PRE-LAB
[[Where to answer and when it is due. Explain the preparation students need before they can begin.]]
1 [[Compare two ideas needed for the lab.]]
2 [[Explain the expected observation using the background.]]
3 [[Find an exact quantity or instrument in the procedure.]]
4 [[Explain why one step must happen before another.]]
5 [[Identify the correct response to a stated hazard.]]
6 [[Set up the tables below in your notebook, with units in headings.]]

DATA TABLE TO PREPARE | COLUMN HEADING
[[Measurement and units]] | [[Record]]
[[Measurement and units]] | [[Record]]
[[Recordkeeping convention, such as how to correct an entry without hiding the original.]]

Footer: SHULL SCIENCE · LAB-02 · SAFETY AND PRE-LAB — 2/4
```

### PAGE 3 — LAB-03 · MATERIALS AND PROCEDURE

```
MATERIALS
Per group: [[Tools, sizes, quantities, reagents, and concentrations.]]

PROCEDURE
Part A — [[First task]]
1. [[Set up and check the tool or apparatus.]]
2. [[Take the measurement with units and precision stated.]]
3. [[Record the observation immediately and identify where it goes.]]

Part B — [[Second task]]
1. [[Give the exact quantities, time, and endpoint.]]
2. [[Place the caution beside the step that needs it.]]
3. [[Explain any parallel work needed while a process runs.]]

SETUP OR REFERENCE
[[Place the relevant labeled setup, reference values, or tool-reading diagram here. Include a
caption that tells students what to look for.]]
[[Continue on another procedure page when needed. Do not shrink the directions to fit.]]

Footer: SHULL SCIENCE · LAB-03 · MATERIALS AND PROCEDURE — 3/4
```

### PAGE 4 — LAB-04 · CLEANUP AND ANALYSIS

```
DATA AND OBSERVATIONS
[[Where and when to record measurements, observations, units, and uncertainty.]]

DISPOSAL AND CLEANUP
1 [[Verified destination and method for each waste stream.]]
2 [[Items retained for later measurements and how to label them.]]
3 [[Cleaning materials, rinse sequence, equipment return, and final checks.]]

POST-LAB ANALYSIS
1 [[Interpret a result using the observation or data.]]
2 [[Show the main calculation with units. Supply any accepted value needed.]]
3 [[Explain a result using the background model.]]
4 [[Trace a specific procedural mistake into the measured quantity and result.]]
5 [[Connect a tool or technique to earlier work.]]
[[Submission instructions. Keep teacher answers and preparation notes in a separate file.]]

Footer: SHULL SCIENCE · LAB-04 · CLEANUP AND ANALYSIS — 4/4
```

### Visual description (Matt's description, not the PDF's own text)

White background, thin hairline rules under section headers, small-caps green/label-colored eyebrow
headers, `[[ ]]` bracket-token placeholders identical to the current convention, no fills or shading,
per-page footer carrying its own "LAB-0#" sub-code and page count. Same overall visual register as
the current template — outline-only, ink-light.

---

## 3. Structural diff — section by section

| Section | Current master (v1.1) | Proposed master | Change |
|---|---|---|---|
| Masthead / header | Course·Unit·Section eyebrow, title with one accent word, `U#/S#` chip, Name/Date/Period, Group Members | Course·Unit·Section line, title, Name/Date/Period, Group Members | Chip and "one accent word" convention not mentioned in the new text — unclear if retained |
| GOALS | 4–6 bulleted items, "each starts with a verb" | 2–3 bullets ("name two or three... skills") | **Count reduced, 4–6 → 2–3** |
| PURPOSE | 2–3 sentences | "two direct sentences" | **2–3 → exactly 2** |
| BACKGROUND | 2 concept paragraphs **plus** up to 3 inline formula blocks (relationship, reaction/equation, percent error) | 2 paragraphs only (key idea, likely mix-up) — no formula content | **Formula content relocated out of Background** |
| REFERENCE RELATIONSHIP | Does not exist as a separate section (formulas live inside Background) | **New section** — formula/model + a paragraph on interpreting the result and defining vocabulary | **Addition** |
| BEFORE LAB DAY | Does not exist | **New section** — what to read/prepare, where to record, when due | **Addition** |
| SAFETY | 6 bullets (PPE, named chemical hazard, equipment hazard, glassware check, thermal/electrical, spill reporting) | 4 bullets (PPE/timing, named hazard, spill/exposure, equipment risk) | **Count reduced, 6 → 4** |
| PRE-LAB | 9 numbered items: 3 conceptual + 4 procedural-reading + 1 safety + 1 table-setup | 6 numbered items: 2 conceptual-ish (compare, explain) + 2 procedural (find quantity, explain order) + 1 safety + 1 table-setup | **Count reduced, 9 → 6; procedural-reading drops below the locked 3–4 minimum** |
| DATA TABLE(S) TO PREPARE | 2–3 side-by-side table skeletons (`.tables`/`.tbl`), each with several labeled rows, plus a separate standalone correction-convention note (`.rule-note`) | One "measurement / column heading" list plus the correction convention folded into the same block | **Multi-table side-by-side layout dropped; correction note merged in** |
| MATERIALS | Prose, "Per group:" middot-separated | Prose, "Per group:" | No structural change |
| PROCEDURE | **4 parts, A–D**, with `.flag` pills marking cross-part concurrency ("do this while Part C runs") | **2 parts, A–B**; concurrency handled as an instruction inside Part B ("explain any parallel work needed while a process runs") rather than as separate parts | **Parts reduced, 4 → 2; `.flag`/concurrent-part convention dropped** |
| Reference data + figure | `.split` block: reference-values `table.data` **and** a separate hand-built SVG diagram, side by side, each with its own caption | One merged "SETUP OR REFERENCE" block — "labeled setup, reference values, **or** tool-reading diagram," one caption; explicit note to continue on another page rather than shrink | **Two-column table+figure split dropped in favor of one merged block; explicit page-continuation allowance is new** |
| DATA TABLES (page-3 heading, "you built these...") | Own `<h2>` on page 3, between Procedure and Disposal | Not present as a separate section; folded into page-4 "DATA AND OBSERVATIONS" | **Moved from page 3 to page 4, merged into a renamed section** |
| DISPOSAL AND CLEANUP | 6 numbered items — items 1–3 lab-specific, **items 4–6 the Alconox boilerplate, locked verbatim** | 3 numbered items — waste-stream destination, retained items, "cleaning materials, rinse sequence, equipment return, final checks" (one generic item, not three fixed ones) | **Count reduced, 6 → 3; the Alconox standing-boilerplate block as a distinct, locked, verbatim item set does not appear** |
| POST-LAB ANALYSIS | 6 numbered items, each carrying a `<span class="ref">` backlink tag to a Part/section | 5 numbered items, no backlink tag shown | **Count reduced, 6 → 5; `.ref` backlink convention dropped** |
| Percent error | Explicit "PERCENT ERROR" formula block in Background; standing rule: "whenever an accepted value exists — and the accepted value is always supplied" | Not named explicitly; item 2 of Post-Lab says "supply any accepted value needed" for "the main calculation" | **Percent error is no longer named as its own line item — only implied** |
| Teacher/student separation | Enforced structurally: teacher key is a separate file, never appended | Explicit sentence added to the *student* page text: "Keep teacher answers and preparation notes in a separate file" | Reinforces the existing rule, now stated in-document rather than only in the README/build rule |
| Footer / running head | CSS `string-set`: bottom-left is `"SHULL SCIENCE · " coursename " · " unitcode`; bottom-right is a free string (title + "carbonless copy" line); top-right running head changes per page section name | Fixed per-page footer: `"SHULL SCIENCE · LAB-0# · [PAGE NAME] — #/4"` | **Full footer scheme change** — course/unit code and the "carbonless copy graded individually" line no longer appear in the footer as specified; replaced by a page-code/page-count scheme |
| Page sub-codes (LAB-01…04) | Do not exist | New identifier layer, one per physical page | **Addition — a second code system alongside `U#/S#.#`** |

---

## 4. Conflicts with currently-LOCKED rules — **not resolved here**

Per `governance/CHANGE_CONTROL.md` and this repository's own instruction to the Secretary, a
conflict with a LOCKED rule is flagged, not silently decided. These are open questions for Matt:

1. **Alconox cleanup block (LOCKED — "Keep them verbatim. Only items 1–3 change per lab.").**
   The new master's Disposal and Cleanup section has only 3 generic items and does not carry the
   fixed items 4–6. **Does the Alconox boilerplate survive as a locked addendum underneath the new
   3-item structure, or is it being replaced by the generic wording in item 3?**

2. **Pre-Lab locked mix ("2–3 conceptual, 3–4 procedural-reading, at least one safety or disposal
   check").** The new master's 6-item Pre-Lab supplies roughly 2 conceptual + 2 procedural + 1
   safety + 1 table-setup — procedural-reading questions drop below the locked minimum of 3.
   **Is the locked mix being revised downward, or does the new master need to add procedural items
   to stay compliant?**

3. **Student section order (LOCKED, per README).** The new master inserts two sections — "Reference
   Relationship" and "Before Lab Day" — into page 1, between Background and Safety, that do not
   appear anywhere in the current locked order. **Are these accepted as additions to the locked
   order, and if so, where exactly do they sit relative to Safety and Pre-Lab — is "Before Lab Day"
   read by students before or after Pre-Lab, given Pre-Lab already states its own due time?**

4. **No-write-space rule (LOCKED — "no ruled lines, no answer blanks, no fillable data tables... the
   lab notebook is the write-on surface").** The new master's page-4 "DATA AND OBSERVATIONS" section
   is worded as "[[Where and when to record measurements, observations, units, and uncertainty.]]"
   — this reads as consistent with notebook-only recording, but it is not stated as explicitly as
   the current README's "table skeletons exist to be copied, not filled." **Confirm this section is
   still instructions-only, not a fillable table on the handout.**

5. **Colour rule (LOCKED — course `primaryDeep` on white, not a single fixed hue).** Matt's visual
   description names "small caps green/label-colored eyebrow headers" specifically. **Is "green"
   describing the Chemistry-colored sample only (informal, illustrative), or is a single fixed green
   being proposed for the eyebrow across all three courses regardless of course accent — which would
   conflict with the "course identity colours apply across all media" rule?**

6. **QA checklist requirement ("`U#/S#.#` matches the document chip, the running footer, the
   filename, and the folder path. One system.").** The new footer scheme (`LAB-0# · [PAGE NAME] —
   #/4`) does not carry `U#/S#.#` anywhere in the visible footer text as specified. **Does `U#/S#.#`
   move to appear only in the masthead eyebrow/chip on page 1, with no per-page confirmation on
   pages 2–4 — and if so, does the QA checklist itself need to change, or does the footer need both
   the LAB-0# code and the U#/S#.# string?**

7. **Known unresolved defect (SHULL-CHG-0010, "recorded, not fixed").** The *current* master's own
   comments describe a 4-page document, but it renders 5 pages with placeholder content — never
   fixed. The new master hard-codes "1/4" … "4/4" directly into each page's footer text. **If a
   filled-in lab using the new master runs long and needs a 5th page (the current master's own
   README explicitly allows "continue on another procedure page when needed" for the new
   Setup/Reference block), the footer's own claim of "4" becomes false on the page.** Does the page
   count in the footer need to become dynamic, or is 4 pages now a hard, enforced ceiling?

8. **Procedure Parts C/D content.** The current master's Parts C and D carry a specific, tested
   pattern — a process that runs unattended while a second task proceeds in parallel (with `.flag`
   pills marking the timing) — used for labs where a reaction or filtration runs while an
   identification task happens alongside it. The new master folds this into a single sentence in
   Part B ("explain any parallel work needed while a process runs"). **Is the two-track,
   `.flag`-pilled Part C/D pattern being retired entirely, or does it still need to exist as an
   optional block for labs that require it (per the Geology and Chemistry course notes, which
   reference exactly this kind of parallel-task lab)?**

None of these are decided by this record. They are listed so Matt can answer them explicitly rather
than have any one of them resolved by implication during a build.

---

## 5. Risk

**High.** This is not a palette correction or a wording pass (compare SHULL-CHG-0010's "colour
finding," which touched one paragraph). Nearly every counted list in the document changes count
(Goals 4–6→2–3, Safety 6→4, Pre-Lab 9→6, Procedure parts 4→2, Disposal 6→3, Post-Lab 6→5), two new
sections are inserted into a currently-locked section order, one locked verbatim block (Alconox) has
no visible equivalent, the footer/traceability scheme changes entirely, and the reference-table+figure
split — a distinct, deliberately separate visual unit in the current build — is merged into one block.
Implementing this without resolving §4 first risks silently loosening at least two rules that were
locked for a stated reason (Alconox boilerplate, Pre-Lab conceptual/procedural mix) and losing the
one-system traceability check the QA gate depends on.

**Recommendation:** treat this as informing a v2.0 draft, built and shown to Matt before it replaces
the live master, rather than a drop-in swap — consistent with the user's own "become (or inform)"
phrasing, which leaves the door open to a partial merge rather than a full replacement.

---

## 6. Not done by this record

- `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` — untouched.
- `templates/lab/SHULL_Lab_TEMPLATE_TEACHER_KEY.html` — untouched.
- `templates/lab/README.md` — untouched.
- No course `DECISIONS.md` was touched — this is a build-mechanics (Layer 1) change, not a course
  fact.
- No decision-log entry was appended anywhere.
- `change-log/CHANGELOG.md` was not edited. Its "How a row is written" table defines a `PROPOSED`
  status for exactly this situation, but no row in the current file uses it — every existing row is
  `CONFIRMED`, `PARTIAL`, or (for SUPERSEDED cases) named as such. There is no established precedent
  in this repository for logging a still-PENDING record before a decision. Once Matt decides, this
  will need a row (`PROPOSED` today, or `CONFIRMED`/`PARTIAL` once implemented and verified) —
  flagged here for Matt, not written.
