---
name: academic-assignment-writing
description: Draft and revise English academic coursework and research documents (methodology and experimental-setup sections, software and tool reports, decision records, verification plans, literature reviews) so they read as one careful human author's prose, with a measurable audit loop for the statistical and lexical tells of machine writing. Use when writing or de-AI-ing an assignment, thesis chapter, report or paper section in IEEE or similar format; not for marketing copy or fiction.
---

# Academic Assignment Writing

Write coursework that a reader takes for the student's own careful prose: specific, sourced, uneven in rhythm the way thinking is, and willing to say "I". The skill has three parts: how to build the document, how to write the sentences, and how to audit and fix a draft. The audit is measured with `scripts/style_audit.py`, not guessed.

## 1. Before writing

- Read the brief, the rubric and the student's earlier submissions for the same project. Every requirement in the brief maps to a named section, table or figure. Keep that mapping as a private list; never paste it into the document.
- Reuse the student's own vocabulary, notation and decisions from earlier work. A later assignment refers back to the earlier one ("As I noted in the literature review, ...") instead of restarting.
- Numbers, parameters and citations come from sources the reader can open. A parameter without a source is a design choice and is called one, with its reason.
- Decide in one sentence what the reader must take from each section. A section without such a sentence is a list, not a section.

## 2. Document structure

- The format follows the course: IEEE two-column (IEEEtran) unless the brief names a journal. The body length is what the brief says. Long parameter tables, full robustness tables and raw trends go to appendices; the body keeps one compact table and one or two figures.
- A methodology document states the system, its actors and outputs, the hypotheses, the model components with numbered equations, the assumptions and constraints, then the experimental setup (sample, parameters with sources, evaluation criteria, robustness plan, computing environment), a pilot or feasibility check, the risks, and the next steps.
- A software or tools document states the requirements, the chosen tools with versions and licences, the alternatives and why they lost, any benchmark that decided the choice, and how to obtain and rerun everything.
- Diagrams (architecture, flow, schematic) are drawn with the academic-diagram skill: editable vector objects, inspected at paper width. Quantitative charts share the diagram's typeface and palette.
- Every figure and table is referenced in the text before it appears, and every equation that is referred to carries a number.

## 3. Voice and sentences

These rules target the statistical and lexical tells of machine-written academic prose. They are about the writing, not the science. Numbers, hedges and citations are never changed to satisfy them.

**Openings.** No meta-discourse. Not "This document specifies ...", "This section presents ...", "In this paper we ...". Open with the question, the object or the claim ("Does predetermined exposure to LL97 change how often commercial buildings register mortgages?"). The conclusion does not restate the opening template either.

**Counting and lists.** Do not announce a number and then list ("Three requirements decide the software. First, ... Second, ... Third, ..."). Write the items as connected prose and let the reader count. Keep a numbered list only when the items will be referred to later by their labels (assumptions A1 to A5, risks (1) to (6), robustness checks R1 to R15) or when the brief asks for one.

**Complete sentences.** The body contains no telegraphic fragments and no colon-chained noun phrases ("Inference: clustering by tract. Composition: outside Manhattan."). A sentence under five words has to earn its place. Nomenclature entries, table cells and captions are exempt.

**Rhythm.** Vary sentence length on purpose. A complex idea may take 35 to 45 words with subordinate clauses, and then a short sentence lands the point. Never three consecutive sentences with the same skeleton ("X absorbs ... Y absorbs ... Z tests ..."). Paragraph openers rotate between a question, a concession, a cause, an example, a judgment and a back-reference; not "The X is ..." every time. Audit targets: mean sentence length 18 to 26 words, SD divided by mean at least 0.45 (careful human prose is often near 0.5 or above), fewer than one sentence in ten over 40 words and fewer than one in ten under 8.

**Vocabulary.** Rotate process words (reproduce, rerun, regenerate, replicate). Do not repeat a signature phrase ("ordinary laptop", "fixed seed", "no licence is needed") more than twice in a document. Avoid the machine lexicon: delve, crucial, pivotal, tapestry, testament, moreover, furthermore, additionally, notably, leverage, utilize, comprehensive, intricate, multifaceted, underscore, foster, landscape, realm, paradigm, seamless, robust as praise, "it is worth noting", "not only ... but also", "plays a vital role". No em-dashes; use commas, colons, parentheses or a new sentence. Do not echo a rule's own wording as if it were a phrase ("the similar side of the rule"); say what happened ("Python fell on the 'similar' side of my decision rule").

**Author voice.** Judgments, choices and worries are in the first person singular: "I treat D_i as an upper bound because ...", "I fixed the decision rule in advance", "which worries me more than any single estimate". Facts stay impersonal: "600 buildings (21.0 %) exceed their limit." Hedge honestly where there is uncertainty ("I believe", "likely", "unfortunately", "I would expect"), and never hedge a number. One voice throughout: not "we" in one section and no person in the next, and no stray "my effect" in an otherwise impersonal text.

**Human redundancy.** Where the logic is hard, say the reason once more in plain words or tie it to earlier work: "I specifically compute exposure from calendar-year 2018. As I noted in the literature review, this is the last full year before the law passed, so it is largely free of post-policy adaptation." One sentence of redundancy, not a paragraph. Never a parenthetical patch after the fact ("(not mortgages)", "only about imports, not totals") when the sentence itself can be written correctly.

**Claims no stronger than the evidence.** Use "is consistent with", "suggests" and "shows" rather than "confirms", "establishes", "validates" or "proves". Pilot estimates "check the design; they are not findings". Keep every number, unit, interval and citation exactly as the analysis produced it.

**Evidence, venue and proposals.** `references/humanizer-additions.md` adds the tells this list does not cover (significance hype, novelty padding, "In recent years" openers, citation dumping, vague hedges), the claim and evidence check, matching an earlier writing sample, and a proposal mode where ambition is judged against feasibility. Where it conflicts with this file, this file wins. Neither is a way to hide AI use; keep the course's disclosure.

**Keep what makes it credible.** Dense specific numbers, statute sections, equation numbers, script names, seeds, named data releases and dated decisions read as human and as careful. Never thin them out to improve flow.

## 4. Audit loop

1. Run `python3 scripts/style_audit.py file.tex --sentences` (also works on .md and .txt). It reports sentence statistics, meta-discourse openers, counting tics, First/Second markers, the machine lexicon, em-dashes, the first-person count and the most repeated words and bigrams, and it lists the very short and very long sentences.
2. Do the manual pass in `references/checklist.md`, plus the extra tells and the claim and evidence check in `references/humanizer-additions.md`: openers, paragraph starts, parallel runs, fragments, repeated phrases, parenthetical patches, voice consistency.
3. Fix the editable source (the .tex or .md), not the PDF. Re-run the audit. Stop when no flagged item remains that a reader would notice; do not chase a metric past the point where the prose would sound forced.
4. Recompile and look at the pages: length budget, float placement, no overfull lines.
5. Verify that nothing but prose changed. Diff the multiset of numbers and the citation keys before and after; a short script does this in a few lines (see the checklist).
6. Report the before and after metrics and a change log in the user's language, together with the files.

## 5. Revising a draft someone else wrote

Preserve the content and the author's decisions. Change sentences, not claims. Do not add results, examples or references that the draft and its sources do not contain. Log every paragraph you touched. When the draft's science looks wrong, say so separately; do not fix it silently under a style edit.

## 6. Deliverables

The compiled PDF with its source, the audit table before and after, the change log, and, where the course or the user asks for it, an explainer in the student's own language. Name the rules you applied, not the rules you considered.
