# Workflow — Build a deliverable

The completion chain. Every document-producing task runs it.

**A returned message is not a completed task.** A task is complete when the deliverable has been
verified to exist, at a verified location, having passed QA.

---

## The chain

```
USER
 ↓
OVERSEER      interpret · scope · plan · confirm the code exists
 ↓
RESEARCHER    content accuracy, where it matters
 ↓
DESIGNER      build to the design system
 ↓
AUDITOR       independent QA — reports, never fixes
 ↓
LIBRARIAN     file it, then VERIFY the destination
 ↓
OVERSEER      verify deployment · task report
```

## Step 0 — before anything is built

The Overseer:

1. Determines course and scope. **Ambiguous and not obvious from the topic → ask. One question.**
2. Reads `courses/<course>/DECISIONS.md`.
3. **Confirms the unit and section code exists there.** Not in a skill. Not in a filename someone
   suggested. In the decisions file. **If it does not, stop and ask.**
4. Reads `standards/ANTI_AI_SLOP_STANDARD.md` as a standing constraint.

> A "build me all of Unit 5" request is **a plan first.** Show the plan as a table — section,
> document type, filename, status, dependency. Get a yes. Then build.

## Build order within a section, and why

1. **Slide deck** — sets the vocabulary, worked examples, and must-write items
2. **Guided notes** — keyed one-to-one to the deck
3. **Practice set** — reuses the deck's worked-example patterns at higher difficulty
4. **Lab or activity** — where the section's content supports it
5. **Quiz** — draws only from what the deck and practice set covered
6. **Study guide** — after the last section of the unit
7. **Unit test, keys, item analysis** — last

> **Nothing later may introduce a term that does not appear earlier.** That is the entire reason for
> the order, and the first thing to check on a gap audit.

**One section at a time. Each document QA'd before the next starts.**

## Step 5 — the Librarian's verification

Filing is not "the create call succeeded." It is an **independent `parentId` lookup** confirming the
object is where it is claimed to be. The Librarian reports the confirmed path and ID.

## Step 6 — the task report

```
SHULL OS TASK REPORT

Task:          Subject:        Unit:        Deliverable:

OVERSEER      ✓
RESEARCHER    ✓
DESIGNER      ✓
AUDITOR       ✓
LIBRARIAN     ✓
DEPLOYMENT    ✓

STATUS:    WORK COMPLETE
LOCATION:  [actual verified location]
```

Shape enforced by `schemas/task-report.schema.json`.

**Any failed or skipped step → `STATUS: INCOMPLETE`**, naming what failed and what remains.
Never report WORK COMPLETE on unverified work. A partially-built deliverable reported as complete
is worse than one reported as incomplete, because nobody goes back to check it.

## When a step is legitimately skipped

Some deliverables do not need the Researcher — a filing correction, a rename. Mark the step
**`— not required`** with the reason, not `✓`. A tick that did not happen is a lie in a form that
looks like diligence.
