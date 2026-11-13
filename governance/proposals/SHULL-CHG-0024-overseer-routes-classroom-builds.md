---
id: SHULL-CHG-0024
title: Every classroom deliverable routes through the Overseer from the start
status: APPROVED
opened: 2026-09-22
decided: 2026-09-22
source: User
decided_by: Matthew Shull
---

# SHULL-CHG-0024 — The Overseer is the entry point for a classroom build

## What he asked for

> "Ure using my repo with overseer to build this right"

and then, told that the Overseer had **not** been used — that the deliverable had been built
single-threaded and checked by its own builder:

> "No always run school items through overseer"

> — 2026-09-22, two turns in sequence.

## What produced it

A Physics lab for `U01/S01.4` — reaction-time free fall, student handout and teacher key, on branch
`claude/reaction-time-free-fall-lab-jfktxs` — was built by going straight to `templates/lab/`.

The repository's own assets were used correctly: the locked lab template, `standards/NAMING.md`,
`brand/tokens.json` through the generated CSS, and `courses/physics/DECISIONS.md` to confirm the
section code exists. That is not the defect.

The defect is that no Overseer, no Designer and no Auditor were involved.
`.claude/skills/build-lab/SKILL.md` step 7 says "Then run `audit-deliverable`." It was not run.
Every quality claim made about that lab — page budget, embedded fonts, independent recomputation of
the key's arithmetic — was **the builder checking its own build.** That is exactly the separation
`standards/QA_GATE.md` names: "An auditor that patches its own findings is not an audit."

This is the known failure mode here, not a hypothetical one.
`reports/T-7_acceptance-test_2026-09-08.md` records that building one real deliverable through the
chain surfaced **nine defects, seven of them in the system rather than the deck** — including a deck
built for a section that does not exist, and a task report that accepted WORK COMPLETE over a failed
step. **Five of the nine were found by the Auditor**, the step a self-checking build does not have.

## Why the gap existed

The chain was written. The requirement to enter it was not.

| Where | What it says | Why it did not bind |
|---|---|---|
| `workflows/build-deliverable.md` | "The completion chain. Every document-producing task runs it." | Describes the chain's shape once you are in it. Nothing says a request must start at the Overseer, and a workflow file is not read by an agent that never asked for one. |
| `.claude/agents/overseer.md` front matter | "Use for any multi-step SHULL request — building a unit, a section bundle, or **anything requiring more than one agent**." | This is the loophole. A single lab looks like one deliverable, one agent, one step — so the trigger never fires. The condition is circular: it takes more than one agent only if you route it to the Overseer. |
| `CLAUDE.md` §6 | "A returned message is not a completed task." | Governs how a build is reported, not who runs it. |
| `.claude/skills/build-lab/SKILL.md` §7 | "Then run `audit-deliverable`." | Tells the builder to audit itself. Even followed exactly, it is the wrong separation. |

## Current Rule

None states this. `.claude/agents/overseer.md` scopes the Overseer to "any multi-step SHULL request
… or anything requiring more than one agent," which leaves a single-deliverable build outside it.

## Proposed Rule

**Every classroom deliverable routes through the Overseer from the start.**

Any request to build, revise, extend or QA a classroom artifact for Chemistry, Physics or Geology —
document, slide deck, assessment, lab, activity, guided or Cornell notes, practice set, study guide,
reference sheet, rubric, unit plan, pacing calendar — is handed to the Overseer as the entry point.
The Overseer plans, delegates to the specialists, confirms the QA gate actually ran, and verifies
the deliverable exists at a verified location before reporting.

**Building first and auditing afterwards is not the workflow. Neither is the builder auditing its
own build.**

### Scope, stated so it is enforceable

**In scope — anything that ends in an artifact a student or a substitute teacher would hold.**
That is the test. It does not depend on size, format, or how many agents it looks like it needs.

**Out of scope:**

- repository maintenance — validators, scripts, templates, build tooling;
- governance and change records, including this one;
- answering a question about the system or the curriculum where no artifact is produced.

**A question is not a build.** "Which unit is Plate Tectonics in?" is answered directly. "Make me a
page on Plate Tectonics" is routed.

### Small changes

**A one-line revision to an existing artifact is still an artifact, and it routes.** The call is
deliberate: the cost of routing a one-line fix is one planning step, and the cost of not routing it
is a re-render nobody looked at. A typo fix still changes reflow, page count and ink, and the lab
above proves the builder is the worst-placed party to judge that.

What the Overseer may do is **mark steps `— not required` with a reason**, which
`workflows/build-deliverable.md` already permits. A one-word correction legitimately skips the
Researcher. It does not skip the Auditor, and it does not skip verification of the rebuilt file.

**Supersedes:** nothing. Checked — no existing rule requires this, and no rule contradicts it. The
closest text is `.claude/agents/overseer.md` front matter, which narrows the Overseer to multi-step
work; that is the wording this change closes, not a rule it replaces. Recorded as new ground rather
than inventing a superseded rule.

## Affected

| Field | Value |
|---|---|
| **Affected Agents** | `overseer` (front-matter trigger — needs rewording, **not edited in this pass**), `designer`, `auditor`, `librarian` |
| **Affected Skills** | `build-lab`, `build-document`, `build-presentation`, `audit-deliverable` — every `SKILL.md` whose procedure ends "then run `audit-deliverable`" is telling a builder to audit itself. **Not edited in this pass.** |
| **Affected Courses** | All three, equally. No course carve-out. |
| **Affected Standards** | None. `standards/QA_GATE.md` and `workflows/build-deliverable.md` already say the right thing; nothing in them changes. |
| **Risk** | Low |

## What this change touches, and what it does not

Touched now:

- `CLAUDE.md` §6 — the rule, stated once, pointing here. This is what `46deedc` carries, and it
  carries nothing else: the rule lands first, the record's SHA and the index row follow, which is
  the order `SHULL-CHG-0023` used.
- `change-log/CHANGELOG.md` — the index row, `PARTIAL`.

**Named, not touched** — `.claude/` was deliberately left alone this pass, and these are the reason
this record exists rather than a patch:

1. **`.claude/agents/overseer.md` front matter.** "Use for any multi-step SHULL request … or
   anything requiring more than one agent" should read so that a classroom artifact of any size
   triggers it. As written, the rule in `CLAUDE.md` and the agent's own trigger disagree, and the
   trigger is what an agent selector actually reads.
2. **The `audit-deliverable` handoff in the build skills.** `build-lab` §7, and the equivalent step
   in the other build skills, should route the audit rather than instruct the builder to perform it.

Until (1) lands, this rule is enforced by `CLAUDE.md` and by the user, not by the agent trigger.
**That is a real gap and it is stated here rather than implied.**

## Risk

**Low.** No standard, template, brand token or course decisions file is touched. No deliverable
changes. The only cost is a planning step in front of small builds, which is the cost the rule is
buying.

The honest counter-risk: routing everything through one orchestrator makes the Overseer the single
point of failure, and T-7 found defects in the Overseer's own reading of standards (row 1, a stale
`NAMING.md`). The mitigation is the Auditor, which is the step this change exists to guarantee runs.

## Verification

- `grep -rho "SHULL-CHG-[0-9]\{4\}" --include=*.md .` — 0023 was the highest allocated ID; 0024 is
  unused.
- Searched for an existing rule requiring Overseer entry: `workflows/build-deliverable.md`,
  `.claude/agents/overseer.md`, `standards/QA_GATE.md`, `governance/GOVERNANCE.md`, `CLAUDE.md`.
  None states it. Nothing contradicts it.
- `CLAUDE.md` §6 states the rule once and points here; the record is the only place the reasoning
  and the scope boundaries live. Checked against rule 1 in the diff before the commit — the scope
  list is **not** restated in `CLAUDE.md`.
- `change-log/CHANGELOG.md` carries one index row, `PARTIAL`, with no rule text in it.

**Not verified: that the rule actually fires.** `.claude/agents/overseer.md` still carries the old
multi-step wording, so the trigger an agent selector reads has not changed. Today the rule is
enforced by the operator reading `CLAUDE.md`, not by the system. That is the gap named above and it
is why the changelog row is `PARTIAL`.

**Implemented By:** 46deedcc23e90005713fc083d60b5c7f647e845d
**Verified:** partial — `CLAUDE.md` §6 carries the rule and a pointer to this record with no
restatement of the scope list; `change-log/CHANGELOG.md` carries one `PARTIAL` index row with no
rule text. **Not verified that the rule fires:** the `.claude/agents/overseer.md` description is
unchanged, so enforcement is by the operator, not the agent selector.

## The lab that produced this record has now been audited

It was run through an independent audit before the rule was committed. Verdict
**PASS-WITH-DEFECTS**, one of them blocking. Nine defects fixed in
`8295e097e6b6402ee6dd5e1220bd8ff423701c5d` — the commit immediately before this rule.

**The blocking defect, and why it is the argument for this change.** The teacher key rendered in
**Chemistry's** accent. `<body>` carried no course class, so `--accent` fell through to the `:root`
default. A Physics lab key printed in the wrong subject's colour, and the builder that made it
reported it as checked.

**The root cause is upstream of that one file.**
`templates/lab/SHULL_Lab_TEMPLATE_TEACHER_KEY.html` line 84 is a bare `<body>`. **Every lab teacher
key ever built from that template has printed in Chemistry's colour.**
`templates/lab/build_lab.py` cannot catch it — it validates unfilled tokens and page count, nothing
else. `build-lab` §3 does say to set the course class on `<body>`, so the template quietly depends
on the builder remembering what the template itself omits.

## Follow-ups from that audit — governance, not build defects

Two findings were fixed in the artifact but are **standing conflicts that will recur on the next
lab.** They are recorded here and deliberately have **no change record yet**, because Matt has not
seen them. Do not open one on this record's authority.

1. **The fillable-data-table waiver.** It was applied as a Physics course decision, but the rule it
   overrides lives in `templates/lab/README.md` and `standards/QA_GATE.md` — **all-three-courses
   rules.** Precedence rule 1 covers the single artifact built under direct instruction; it does not
   settle the standing conflict, and nothing records which way it goes next time.
2. **The Alconox and disposal deletion was an inference, not an instruction.** Matt asked for no
   safety section. He said nothing about disposal. `templates/lab/README.md` locks that block
   "keep verbatim." A block locked as standing boilerplate was removed on a builder's judgement,
   which is the same class of error as auditing your own build.

## Still outstanding on this record

The two `.claude/` changes in "What this change touches" are **Matt's call, not the Secretary's** —
rewording the Overseer trigger changes when an agent fires, and changing the `audit-deliverable`
handoff in `build-lab`, `build-document` and `build-presentation` changes what the build skills
instruct. The changelog row stays `PARTIAL` until both land.
