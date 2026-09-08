# The Anti-AI-Slop Standard

**This is a binding production standard, not a style preference.**
**Applies to:** every artifact — documents, slides, assessments, labs, activities, and interactive
tools.
**Source:** `legacy/drive-standards/ANTI_AI_SLOP_EDUCATOR_STANDARD.md`, decomposed. Voice moved to
`standards/VOICE.md`. Format-specific procedure moved to the `build-*` skills. Classroom defaults
moved to `courses/*/DECISIONS.md`, where course facts belong.

> **In the legacy system this standard was unreachable.** `shull-studio` said "do not skip" loading
> it, then pointed at Claude Project Knowledge, which Claude Code cannot read, and at a fallback
> reference file that did not exist. The system's most important quality rule could not be loaded by
> the router that mandated it. That is CONFLICT-10, and putting this file here is the fix.

---

## 1. The definition and the test

> **AI slop is "generic with no soul."**

That phrase is the central quality-control principle of SHULL Studio. Every finished artifact faces
one question:

> **Would this actually look like something the teacher would hand to students?**

If not, revise it.

## 2. The prime directive

Create materials that feel deliberately written by a real classroom teacher for a specific group of
students — not generated from a generic education template.

The finished product should sound like a teacher who knows what students have already learned, knows
where they get confused, has a plan for how this will be used in a 50-minute period, speaks plainly,
values accuracy and useful practice over decoration, and makes purposeful choices instead of filling
space.

> **Never imitate human writing by inserting mistakes, fake anecdotes, awkward grammar, or random
> quirks. Never add intentional typos to evade AI detection. Never write around a detector.**

Authenticity comes from specificity, judgment, restraint, and classroom awareness. Nothing else.

## 3. Specificity before polish

Generic material is the strongest single sign of slop. Every artifact reflects the actual course,
unit, section, students, available time, and classroom routine.

Before drafting, establish: course and grade level · unit and section · prior knowledge · what is
being practiced or assessed · available class time · individual, partner, or group · materials and
what is allowed · expected student product · grading method and point value · likely misconceptions ·
whether a modified or challenge version is needed.

If a missing detail would materially change the assignment, **ask**. If it would not, make a
reasonable teacher-like assumption and state it briefly in the teacher notes — **never on the
student page**.

> **Never pad. Every question, box, heading, graphic, and instruction must earn its place.**

## 4. Accuracy and integrity — absolute

- **Never fabricate** sources, quotations, data origins, standards, accepted values, chemical
  properties, safety guidance, or local policies.
- **Never invent a safety claim.** Flag uncertain handling or disposal for teacher verification.
- **Never invent a statement, event, opinion, or classroom story and attribute it to Mr. Shull.**
- **Never present a PROVISIONAL, CARRIED OVER, or UNKNOWN item as confirmed.**
- A wrong standard code is worse than no standard code. If uncertain, say so.
- Verify every calculation, formula, unit, equation, graph, label, and answer choice. Solve every
  problem rather than generating answers by pattern.
- Distinguish observations from inferences.

## 5. Visual tells to avoid

Each of these is a defect on its own:

an emoji or icon before every heading · excessive rounded cards and boxes · a coloured banner for
every subsection · generic science clip art · fake sticky notes, speech bubbles, lightbulb callouts ·
rainbow palettes · five font styles · unnecessary cover pages · **repeated
"Objective / Materials / Instructions / Reflection" templates regardless of task** · perfectly
symmetrical grids the content does not call for · huge titles wasting half a page · decorative
footer slogans · overuse of bold · tables used for paragraphs of prose · **answer blanks clearly too
small for the expected response** · obvious template repetition across a long deck.

The positive form of these rules — density, decoration, imagery, hierarchy — is in
`brand/SHULL_DESIGN_SYSTEM.md`. This list is what failure looks like.

## 6. The audit list

Search every draft for these habits and revise unless genuinely necessary:

repeated "Students will…" · repeated "Your task is to…" · excessive colon headings · identical
three-bullet lists under every heading · sentence after sentence opening with an imperative ·
"Additionally / Furthermore / Moreover" · "ensure, utilize, delve, foster, showcase, comprehensive,
robust, seamless, dynamic, meaningful" where a simpler word works · "exciting, engaging, fun,
powerful, unique" · inflated claims about routine work · conclusions restating the introduction ·
"What did you learn?" · sets of questions with identical length and rhythm · "Why do you think…?"
where evidence-based wording is better · "Key Takeaways" on an ordinary assignment · a reflection
section added by default rather than by instructional need.

> **This is an audit list, not a word ban. Natural language beats mechanical compliance.**

A literal banned-word filter produces its own kind of slop. Read the sentence and judge it.

## 7. Task design

- **Vary the thinking, not just the numbers.** Mix calculation, explanation, comparison, prediction,
  diagram and graph interpretation, error analysis, evidence-based claims, and transfer. Ten
  consecutive questions with identical structure and different numbers is a defect — unless
  repetition is genuinely needed for fluency, in which case say so.
- **Use believable contexts.** Scientifically accurate and useful to the question. No fake companies,
  contrived student characters, implausibly perfect data, or decorative stories that add reading
  without adding meaning.
- **Put imperfection in the data, not in the quality.** Believable measurements with appropriate
  precision and modest variation. Clean arithmetic only where calculation practice is the goal.
- **Do not label student copies "easy / medium / hard."** Use content-based headings or none.
- **Replace vague prompts.** Not "Explain your answer" but "Use the particle diagram and the
  temperature data in your explanation."
- **No false rigor.** Extra reading, ugly numbers, and vague prompts do not make a question harder.

## 8. Interactive and digital output

Applies to HTML tools, self-check widgets, and dashboards. Print, decks, and Word documents follow
the sections above instead.

- **Reject generic template UI.** No purple or indigo gradients, no floating pill cards with
  arbitrary rounded corners, no generic SaaS landing-page layouts.
- **Structure is information.** Grid, dividers, alignment, and typographic weight map to real data
  relationships. Never add decorative "01 / 02 / 03" numbering or iconography unless the data model
  dictates a sequence.
- **Density matters.** Operational tools optimise for information density over padding. A teacher
  needs to see data, not scroll past white space. *(This agrees with the design system's
  clean-and-moderately-dense rule — it is the same instinct applied to a screen.)*
- Educational and staff tools: professional high-contrast typography, clean tabular structures,
  predictable navigation, strict semantic borders.
- **One styling approach only** — native utility classes or clean CSS variables, never both. Safe
  null handling on optional attributes. Dry, modular, semantic markup over nested generic `div`
  stacks.

## 9. Revising existing work

> **When revising an existing teacher-created file, preserve its useful personality and routines.
> Improve weak areas without replacing everything with a generic template.**

This rule governs the whole legacy migration, not just documents. A file that has been used in a
classroom carries decisions in it. Find out what they were before overwriting them.

## 10. The final audit

Complete this silently before delivering any artifact. It is the qualitative half of
`standards/QA_GATE.md`, which covers the mechanical half.

**Voice** — Does this sound like a teacher speaking to his own students? Is any sentence performing
enthusiasm instead of communicating? Could a generic phrase be plainer?

**Instructional design** — Does every question measure something intentional? Is the progression
sensible? Are directions specific enough to prevent avoidable confusion? Is the workload realistic
for the time? Are the contexts believable and necessary?

**Accuracy** — Have all calculations and answer choices been checked independently? Are units, sig
figs, formulas, labels, and terminology correct? Are safety and disposal statements reliable? Is the
key fully aligned with the student version?

**Appearance** — Is the page easy to scan and photocopy? Is there enough working space where students
need it? Have decorative boxes, icons, headings, and colours been reduced to only those with a
purpose? Does it avoid the polished-template sameness associated with AI output?

**Authenticity** — Does this reflect *this* course, *this* unit, *these* students? Are there filler
sections that could be deleted? Did the design come from the learning goal or from a template? Is
anything falsely presented as Mr. Shull's own experience or opinion?

If any answer reveals a problem, revise before delivery.

## 11. Delivery

1. Deliver the usable student version first.
2. Keep the teacher key, prep notes, and rationale separate.
3. **Do not preface the artifact with a long explanation of what was created.**
4. Do not add optional sections, extensions, standards, reflections, differentiation, or rubrics
   unless requested or clearly necessary.
5. Briefly flag any important assumption, scientific uncertainty, or safety item needing teacher
   verification.
6. Preserve established formatting and conventions across related materials.
