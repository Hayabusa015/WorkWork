# Build and review a printed unit textbook

Use this route for “create a unit textbook,” “write a textbook-style unit reading,” or a revision to an existing chapter in Chemistry, Physics, or Geology. A worksheet, reference sheet, slide deck, or request for advice keeps its normal route. The Overseer owns intake and filing under `workflows/build-deliverable.md`. In its task report, record the specialist under the existing designer step.

## Commission the chapter

1. The Overseer verifies the course, unit, section sequence, prerequisites, and learning targets against the course decisions. For a revision, retrieve the current artifact and honor the requested scope. Preserve any edition the teacher designated as a draft.
2. The Researcher checks the science for the planned examples and assembles traceable sources for factual claims, values, data and figures. Supply source title, edition or date where relevant, and a page, table, or URL with the relevant excerpt or data. Prefer primary authorities suited to the claim, e.g. IUPAC or NIST for chemistry terms and constants, BIPM for SI conventions, USGS for geologic observations and the International Commission on Stratigraphy for time boundaries. Label illustrative datasets and identify image rights and credits where needed.
3. The textbook-page-designer authors the reading and builds the pages. For a standalone unit opener, use the teacher’s textbook-specific grade 11–12 target while retaining the direct instructional voice in `standards/VOICE.md`. Explain unfamiliar terms at first use, develop a causal argument across paragraphs, and keep the intellectual demand in the science. Plan each section around what students should be able to explain or infer. A page count is a production constraint, not a measure of instructional depth.

## Page decisions and their research basis

| Decision | Use in the chapter | Removes a barrier |
|---|---|---|
| Worked examples and practice | Model the consequential decision, show intermediate reasoning, interpret the result, then pose a nearby problem with a changed condition. Fade supplied steps as earlier skills recur. | A row of solved substitutions can conceal which relationship the student needs to select. [IES practice guide, recommendation 2](https://ies.ed.gov/ncee/WWC/PracticeGuide/1) |
| Words and figures | Place the figure beside its first substantive reference. Tell students what to compare; label the feature directly. Connect the observation to a diagram, graph, or equation in the prose. | A decorative picture or a remote legend gives students little help connecting the representations. [IES, recommendations 3 and 4](https://ies.ed.gov/ncee/WWC/PracticeGuide/1) |
| Scientific models | Explain what a symbol, boundary, arrow, or scale represents and which inference it supports. State the relevant idealization when it changes interpretation. | A realistic-looking drawing can suggest false size, spacing, or motion. [National Research Council, science and engineering practices](https://www.nationalacademies.org/skim.php?chap=41-82&record_id=13165) |
| Reading in print | Use clear hierarchy, left-aligned body prose and sufficient contrast. Preserve reading order through columns; move the break when an equation, caption, or worked step would split. | Crowded lines, text over pictures, and distinctions carried only by hue become especially hard to read on a copy. [UKAAF clear-print guidance](https://www.ukaaf.org/wp-content/uploads/2024/12/G003-UKAAF-Creating-clear-print-and-large-print-documents-v4.pdf) |

The IES guide rates the evidence for recommendations 2–4 as moderate. UKAAF supplies accessibility guidance. Exact fonts, page margins, binding space, header, and toner limits are SHULL production decisions; obtain them from `brand/SHULL_DESIGN_SYSTEM.md`, the print components, and `.claude/skills/build-document/SKILL.md`.

## Build for the discipline

Open with a phenomenon, sample, or observation students can revisit. Use each section to advance the question. Include a worked example and a short transfer or explanation check where a section introduces a new reasoning move. A qualitative section can model an inference from evidence. Use a separate key for student questions. Keep the answer to a transfer question out of its prompt.

| Course | A worked example worth printing | Inspect closely |
|---|---|---|
| Chemistry | Move from a macroscopic measurement to a particle model and a symbolic calculation. Show the named entity, the conversion fractions with units, and a magnitude check. | Counts and charge, formula units versus molecules, subscripts, balanced equations, precision, and whether the diagram depicts a molecule or an extended structure. Use the repository molecular-structure builder where applicable. |
| Physics | Define the system and positive direction, draw and label forces or interpret a graph, choose a physical law, carry units, and test the sign or a limiting case. | Arrow directions and points of application, vector versus scalar quantities, dimensions, sign convention, valid model conditions, and what graph slope or area means. |
| Geology | Start with an outcrop, map, or cross-section. Work from visible evidence to an ordered sequence, then identify an observation that could distinguish two interpretations. | Map orientation, legend, scale and vertical exaggeration where applicable, cross-cutting relations, age units, and observed versus inferred boundaries. Identify a schematic or reconstruction as such. |

Use a photograph when the texture or observation is the evidence. Generated illustrations may establish a scene; use verified data and controlled drawings for a graph, a structure, a map location, or a measured comparison. Describe the meaningful contrast in words and encode it with labels, patterns or distinct lines. Keep captions and callouts legible on a grayscale page at the intended print size.

## Independent accuracy and print review

The Overseer gives the existing Auditor the **actual exported edition**, its source dossier, scoped objectives, and separate key. The Auditor opens the edition and follows `.claude/skills/verify-content/SKILL.md` and `standards/QA_GATE.md`. The Researcher can retrieve additional evidence; the Auditor owns the verdict.

- Work page by page. Trace material claims to a source and locator. Independently solve every example and student item from the printed givens before comparing the solution and key. Check qualitative reasoning with the same care as arithmetic.
- Read the figures as student evidence. Check every label, structure, axis, unit, sign, scale, legend and caption against the prose or source data. A correct paragraph cannot rescue a misleading figure.
- Render the final PDF at its intended size in grayscale, inspect each page and its reading order, and run the existing font and ink audits. Recheck formula glyphs, superscripts, page references, and binder margins. Identify the proof method accurately: a screen proof and a physical photocopy are different checks.
- Record the artifact version and coverage. Use a findings table with page/item, claim or calculation, independent evidence or result, severity, and disposition. Mark unsupported claims, incorrect science, a wrong key, or unreadable information as blocking. A missing source or uninspected page stays open.
- The Overseer returns findings to the textbook-page-designer. The Auditor reviews the corrected export and affected references or answers before signing off. A layout-only revision can reuse verified content evidence for unaffected pages after confirming their identity; check the changed rendering and pagination. Use the ordinary approval-to-file gate after QA passes.
