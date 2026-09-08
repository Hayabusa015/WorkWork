# SHULL Studio — Architecture (v2)

Supersedes `SHULL_Studio_Install_and_Architecture.md`. The install section is
gone — it's done. This is now a status and routing document.

---

## Current state

**Installed and enabled, account-wide:**

```
                        shull-studio  ← load FIRST, every time
                             │
     ┌────────────────────┼─────────────────┬──────────────────┐
     │                    │                 │                  │
slide-deck-builder  guided-notes-builder  course-librarian  test-quiz-generator
     │                    │                 │
     └──── course profile: chemistry · physics · geology ────┘
                             ▲
                    shull-student  ← scheduled sweep, drafts back into the profile
```

Also live: `shull-practice-set-generator`, `anti-ai`.

**Not built yet:** Reference Sheet Generator, Lab Document skill.

---

## Changes since install

**1. The slide system was rebuilt.** The prototype deck Matt approved became a
real template — twelve layouts in the slide master, Poppins instead of Aptos,
16pt type floor. Details in `SHULL_Slide_System_v2.md`. `shull-slide-deck-builder`
should be updated to build against this template rather than generating decks
from scratch.

**2. There are now two palettes**, split by medium. Amber on ink for projection,
Bio Lime on parchment for print. This is the largest open item in the system —
see the sign-off note in the slide system doc.

**3. The image workflow is settled.** Claude cannot download images and
Higgsfield is dry, so the loop is prompt → Matt generates → Matt attaches →
Claude places. Diagrams stay hand-built. `SHULL_Image_Prompt_Pack.md` holds the
style block and per-slide prompts.

**4. Print margins are codified.** Top 0.30in, left/right 0.35in, bottom 0.45in.

**5. Guided notes page conventions are confirmed.** Every section starts on a
new page. Every section ends with a summary box plus self-check checkboxes.
Worked problems use an open bordered box with a faint `SHOW WORK HERE` prompt,
never ruled lines — ruled lines are for prose, boxes are for math, in notes and
practice sets alike.

**6. The connector directive was lost and restored.** Section 19 of the
Chemistry guidelines disappeared during a skill reinstall. See the warning below.

---

## ⚠ Skill files are not durable storage

A skill reinstall overwrote user-level edits once already. Anything the
`shull-student` sweep writes into a course `SKILL.md` is one reinstall away from
being erased.

**Until this is resolved, treat Project Knowledge as the system of record** and
the installed skill as a cache. Sweep output goes into the packaged `.skill`
Matt re-uploads, not only into the live copy.

---

## Routing

Add to each project's instructions, swapping the course profile:

> This project uses the SHULL Studio skill set. Load `shull-studio` first for
> any request to build, revise, plan, name, file, or audit a classroom document.
> Then load `shull-[course]-guidelines` for course content, and the specialist
> skill for the deliverable: `shull-slide-deck-builder` for decks,
> `shull-guided-notes-builder` for notes, `test-quiz-generator` for assessments,
> `shull-course-librarian` for planning, gap audits, filing, and pacing. Slide
> decks build on `_Brand/Templates/SHULL_Science_Slide_Template.pptx` — never
> from scratch. Do not build a SHULL document without loading `shull-studio`.
>
> Scheduled overnight runs in this project invoke `shull-student`.

**Verify it took.** Ask in each project: *"What skills would you use to build a
practice set for U8/S8.2, and why?"* A correct answer names `shull-studio` plus
the course profile and explains the routing.

---

## The sweep

Three scheduled tasks, one per course project — past-chat search cannot cross
project boundaries. 3:00 AM, staggered so each morning has at most one report.

> Run the shull-student learning sweep for this project. Cover everything since
> the last sweep report. Draft the updated guidelines file and the sweep report.
> Hold any finding that conflicts with a CONFIRMED entry for my review — do not
> apply it.

---

## Open items

| Item | Owner | Blocking |
|---|---|---|
| Physics unit/section map | Matt | Every Physics document — no valid `U#/S#.#` code without it |
| Two-palette split sign-off | Matt | The slide builder's default behavior |
| Skill-file durability | Matt | Every future sweep |
| Remove `SHULL_Chemistry_Claude_Project_Export.md` from Project Knowledge | Matt | Redundant with the skill file |
| Reference Sheet Generator | Claude | Sig figs / reactions / electron config queue |
| Lab Document skill | Claude | Units 1+ labs |
| Chemistry section 9.6 | Matt | Binder header says six, only 9.1–9.5 listed |
