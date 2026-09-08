---
name: test-quiz-generator
description: >
  Generates complete, print-ready science assessments — tests, quizzes, exit tickets,
  bell ringers, and unit exams — for Matt's Chemistry, Physics, and Geology classes at
  James A. Garfield Local Schools (Ohio). Use this skill whenever the user asks to
  create, write, or generate a test, quiz, assessment, exam, exit ticket, or question
  bank, or says things like "make me a quiz on stoichiometry", "I need a unit test for
  plate tectonics", "generate A and B versions", "write 10 questions on Newton's laws",
  "build an exam with an answer key", or names a science topic plus an assessment type.
  Also trigger for requests to convert notes/materials into an assessment or to make an
  alternate version of an existing test. Produces Word (.docx) files in Matt's Teacher
  Brand format with A/B versions and separate answer keys. Always use this skill for
  any assessment-generation request.
---

# Test & Quiz Generator

Generates original science assessments formatted to Matt's classroom document
standards, with **A/B versions** (shuffled order AND changed numeric values where
applicable) and **answer keys as separate files, always**.

The sequel to teacher-upgrade: that skill reformats existing materials; this one
creates assessments from scratch.

---

## Step 0 — Required Reading

Before generating anything:
1. Read `/mnt/skills/public/docx/SKILL.md` — all output is .docx.
2. Read `references/formatting-spec.md` — Matt's Teacher Brand document standards.
3. Read `references/question-design.md` — Bloom's weighting, question construction
   rules, and the anti-AI quality bar.
4. Skim the relevant subject section of `references/ohio-standards.md` for standards
   tagging.

---

## Step 1 — Gather Requirements

Infer from the request; ask ONE compact question only if truly ambiguous. Defaults:

- **Subject & topic** (required — the only thing that can't default)
- **Assessment type**: quiz (default if <20 min), test, unit exam, exit ticket, bell ringer
- **Length**: quiz = 10–15 questions / test = 25–35 / exit ticket = 3–5
- **Question mix** (default): multiple choice 50%, short answer 25%, problems/calculations
  25% for Chemistry & Physics; swap calculations for diagram-interpretation in Geology
- **Versions**: A and B by default for quizzes and tests; single version for exit
  tickets/bell ringers unless asked
- **Difficulty**: standard high school unless Matt says honors/intervention
- **Time available**: match question count to class period if stated

If Matt uses the "Teacher —" prefix, proceed immediately with defaults, no questions.

---

## Step 2 — Blueprint Before Writing

Build a quick internal blueprint (include it in the chat summary, not the document):

- Map each question to a learning objective and an Ohio Learning Standard code
  (see `references/ohio-standards.md`)
- Apply Bloom's weighting from `references/question-design.md`
  (default: 30% Remember/Understand, 45% Apply/Analyze, 25% Evaluate/Create-adjacent)
- Order: easiest opener → mixed middle → highest-cognitive-demand near the end,
  calculation section grouped with data/constants provided

---

## Step 3 — Write the Questions

Follow ALL rules in `references/question-design.md`. The non-negotiables:

- Scientifically accurate — double-check constants, units, sig figs, formulas
- Calculations must be solved BY YOU during generation; if the numbers produce ugly
  or unrealistic answers, change the numbers
- Distractors must represent real student misconceptions, not random wrong values
- No "All of the above" / "None of the above"; no trick questions on wording
- Real-world contexts current and Ohio-relevant where natural (see standards file
  for hooks) — never forced
- Reading level appropriate for HS; define genuinely new vocabulary in the stem

---

## Step 4 — Build Version B

Version B is NOT just shuffled A:

- **Multiple choice**: reorder questions AND shuffle answer positions
- **Calculations**: change the given values (keep the same skill and comparable
  difficulty; re-solve to verify clean answers)
- **Short answer**: reorder; where possible swap the scenario while testing the
  identical concept
- Both versions must map to the same blueprint — identical standards coverage and
  point totals

---

## Step 5 — Generate Files

Output per assessment (to `/mnt/user-data/outputs/`, following
`references/formatting-spec.md` exactly):

1. `<Unit> - <Topic> <Type> - Version A - <Season Year>.docx`
2. `... Version B ...` (if applicable)
3. `... Version A - ANSWER KEY ...` — always a separate file
4. `... Version B - ANSWER KEY ...`

Answer keys include: correct answer, point value, full worked solutions for every
calculation (with units and sig figs), model responses with grading guidance for
short answers, and the standard code per question.

In chat, give a compact summary: question count, point total, standards covered,
estimated completion time, and anything Matt should review (e.g., "Q14 assumes you
covered limiting reactants").

---

## Quality Bar

The document must not look AI-generated: varied question stems, natural teacher voice
in directions, no em-dash-heavy phrasing, no bolded-buzzword clutter, professional
restraint. A colleague picking it up should assume Matt wrote it on a good day.
