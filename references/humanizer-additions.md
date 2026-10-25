# Additions merged from academic-humanizer

These rules come from [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) (v0.3.3, commit `94b88b2`, MIT, copyright 2026 AIScientists-Dev), restated in this skill's terms. `SKILL.md` stays the primary rule set. Where the two disagree, this skill wins, and the conflicts are listed at the end so nobody re-imports the other side by accident.

## Extra tells to catch

| Tell | What it looks like | Fix |
|---|---|---|
| Significance hype | "paves the way for", "sheds light on", "of paramount importance", "bridges the gap", "has the potential to revolutionize" | Name the one problem the work addresses and where it is shown ("error accumulation in long rollouts, Section 4"). |
| Novelty padding | "novel" more than once per section, "to the best of our knowledge", "for the first time" | Say what prior work does not do, with the citation that shows it. |
| Formulaic openers | "In recent years, X has attracted increasing attention", "With the rapid development of ...", "Despite recent advances, ..." | Open with the limitation or the question itself. |
| Empty intensifiers | "extensive experiments", "a wide range of datasets", "numerous", "various" | Count and name them ("three datasets: ..."). |
| Contribution-list cliché | "(1) a novel method; (2) extensive experiments; (3) strong results" | Each contribution states a specific result with its number. |
| Citation dumping | "Many methods exist [3, 7, 9, 12, 15]." | Cite the one or two works that matter and say how this work differs. |
| Hedging by vagueness | "somewhat", "relatively", "fairly", "to some extent", "quite" | Give the magnitude, or cut the word. Honest uncertainty hedges ("I believe", "suggests") stay. |
| Copula avoidance and "-ing" tails | "serves as", "stands as"; "..., highlighting its importance" | "is"; delete the tail or make it its own claim with evidence. |
| Elegant variation | Cycling synonyms for one referent ("the guard", "the enforcer", "the checker") | One name per object. This differs from rotating process verbs, which `SKILL.md` asks for. |

The audit script flags most of the phrases above in its machine-lexicon line. "Novel", "various" and the vague hedges are left to the manual pass because they are often legitimate.

## Claim and evidence discipline

For every empirical claim, ask two things: is there a number, table, figure or citation for it in the text, and is the verb no stronger than that evidence? An unbacked claim gets an evidence pointer or is softened. A vague magnitude ("a large improvement") becomes a number or a range attributed to its metric and baseline ("2 to 6 points of balanced accuracy over the strongest baseline"). Compare against the strongest competitor first, not the trivial one. Prefer a range over a single average unless the averaging is stated.

## Matching the author and the venue

When earlier writing by the student is available, read a sample before editing and note sentence rhythm, connectives, where hedges sit, how sections open, notation and recurring phrasings; then match them. Match the register of the venue as well: a conference paper is terse and results-first, a course report follows the brief and the rubric.

## Proposal mode

A research or funding proposal (NSF, NIH, a thesis proposal, a project plan) is judged on vision and feasibility, not finished results, so the ambition words this skill would trim in a report ("long-term goal", "establish a foundation") are acceptable there if a plan backs them. The discipline shifts to claim against feasibility: every aim needs a footing (preliminary data, a prior result, a named classical method, a collaborator) or it is scaled down. The opening page carries the hook, the gap, the central idea, parallel aims that do not collapse if the first fails, and the payoff. Aims are questions or outcomes, not techniques ("Determine whether ...", not "Apply transfer learning"). Never invent preliminary results, funding, partners or letters; flag the gap to the author instead.

## Ethics

Neither skill exists to hide AI assistance. Follow the course's AI-use disclosure rules and keep the disclosure in the submission.

## Conflicts, resolved in favour of this skill

- **Person.** academic-humanizer keeps "we" and forbids first-person personality in manuscripts. This skill uses first person singular for a single author's judgments and impersonal phrasing for facts, because coursework is single-authored and the absence of an author's voice was itself a reviewer flag. For a co-authored paper, use "we" consistently instead.
- **Long sentences.** academic-humanizer splits sentences past about 30 words. This skill allows a 35 to 45 word sentence for a complex idea and steers by the burstiness target (SD/mean at least 0.45), so split only clause-stacked sentences that carry no extra weight.
- **Triples.** academic-humanizer tolerates an occasional triple. This skill avoids reflexive triplets and announced counts; keep three items only when there are three.
