# Teacher Brand — Assessment Formatting Spec

Matt's classroom document standards, applied to assessments. Consistent with the
teacher-upgrade skill.

## Typography & Base Format
- Font: **Trade Gothic Next, 11pt** for all body text (fallback chain in docx:
  "Trade Gothic Next", "Franklin Gothic Book", Arial)
- Answer blanks: **underline style** (bordered empty paragraphs, NOT underscore
  strings — underscores wrap unpredictably)
- Margins: 0.75" all around; single spacing with 6pt after paragraphs
- Page numbers bottom-right on multi-page documents

## Header Block (page 1)
Name/Date/Period line at top:
```
Name: ______________________    Date: ____________    Period: ______
```
Then a title block: Assessment title (bold, 14pt), subject + unit line, and
**"Version A"** or **"Version B"** clearly marked top-right (also repeat the version
letter in the footer of every page so shuffled papers can be re-sorted).

Point total and time estimate under the title: "___ / 52 points • ~35 minutes"

## Section Structure
- Part A, Part B, Part C... with section headers as single-cell full-width tables
  with light shading (`ShadingType.CLEAR` fill) — renders more consistently than
  Heading styles across Word versions
- Each section header states question type and point value:
  "Part A — Multiple Choice (2 points each)"
- Directions in italic under each section header, one to two sentences, teacher voice

## Question Layout
- Multiple choice: two-column layout for short-stem questions using borderless
  `Table` objects (`BorderStyle.NONE`); single column for long stems or those with
  diagrams/data tables
- Answer choices: A. B. C. D. (period, not parenthesis), aligned
- Calculations: full width, generous whitespace below each for work
  ("Show your work for full credit" in section directions), answer line with units:
  `Answer: ______________ (units)`
- Short answer: 3–5 bordered blank lines per question
  (`border.bottom = BorderStyle.SINGLE` on empty paragraphs with spacing.before)

## Data & Reference
- If calculations need constants (R, g, molar masses, formulas), include a boxed
  reference block at the start of that section — students shouldn't need to memorize
  constants to demonstrate the skill unless that IS the skill
- Periodic table note where relevant: "You may use your periodic table."

## Answer Key Files
- Same header/branding, "ANSWER KEY" in red bold in title and as a diagonal-feel
  header note (no watermark — just unmistakable labeling)
- Table format: Q# | Answer | Points | Standard | Notes/Worked solution
- Calculations: full worked solution steps, final answer bolded with correct sig figs
  and units
- Short answer: model response + "accept if student includes:" bullet criteria

## File Naming
`<Unit Name> - <Topic> <Quiz|Test|Exam> - Version <A|B>[ - ANSWER KEY] - <Season Year>.docx`
Example: `Unit 4 - Stoichiometry Quiz - Version A - Summer 2026.docx`

## Anti-AI Appearance Rules
- No emoji, no decorative icons, no gradient anything
- Vary question stem phrasing — never five questions in a row starting "Which of
  the following"
- Directions sound like a teacher, not documentation: "Answer in complete sentences"
  not "Please provide your response utilizing complete sentence structure"
