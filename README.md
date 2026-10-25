# Academic Assignment Writing

A skill for agents (Claude Code, Codex and other hosts that read `SKILL.md`) that write or revise English academic coursework: methodology and experimental-setup sections, software and tool reports, decision records, verification plans, literature reviews. It makes the text read as one careful human author's prose and measures the result instead of guessing.

The skill grew out of a research-methods course project and two rounds of reviewer feedback on what still read as machine-written: template openers ("This document specifies ..."), the counting tic ("three reasons: First ... Second ... Third"), telegraphic fragments, uniform sentence rhythm, recycled signature phrases, mirrored abstract and conclusion, and the absence of an author's voice. Each of those has a rule and a check here.

## What is inside

| Path | Purpose |
|---|---|
| `SKILL.md` | The skill: preparation, document structure, voice and sentence rules, the audit loop, how to revise someone else's draft, deliverables. |
| `scripts/style_audit.py` | Standard-library Python. Reports sentence statistics (mean, SD, burstiness, share of very short and very long sentences), meta-discourse openers, counting tics, First/Second markers, machine lexicon, em-dashes, first-person count and the most repeated words and bigrams for `.tex`, `.md` and `.txt` files. `--sentences` lists the offending sentences. |
| `references/ai-tells.md` | Catalogue of fourteen tells with examples, why each reads as machine output, and the fix; plus what never to remove. |
| `references/checklist.md` | The manual pass, the audit targets, and the verification that nothing but prose changed (numbers and citation keys). |
| `examples/before-after.md` | Paired passages and the audit table from the two documents the skill was first applied to. |

## Install

Claude Code, personal skill:

```sh
git clone https://github.com/RealWayTrueX/academic-assignment-writing.git ~/.claude/skills/academic-assignment-writing
```

Claude Code, project skill: clone into `.claude/skills/academic-assignment-writing` inside the project. Codex: clone into `~/.codex/skills/academic-assignment-writing`. Other hosts: point them at `SKILL.md`. Keep `scripts/`, `references/` and `examples/` next to it.

## Use

```text
Use the academic-assignment-writing skill. Revise paper/methodology.tex so it reads as my own
prose: remove template openers and counted lists, vary the rhythm, use first person for my
judgments, keep every number and citation unchanged. Run the audit before and after, recompile,
and give me the change log and the metrics table.
```

Or, for a new document:

```text
Use the academic-assignment-writing skill to draft the Software Tools report for this project
from code/, paper/methodology.tex and the course brief in docs/brief.pdf. IEEE two-column,
two pages.
```

The audit alone:

```sh
python3 scripts/style_audit.py paper/methodology.tex --sentences
python3 scripts/style_audit.py report.md other.tex --json
```

## Related skills

- Figures: [academic-diagram](https://github.com/plbbl/academic-diagram-skill) for editable architecture and schematic diagrams, referenced from the structure rules.
- Sentence-level humanising: [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) covers over-claiming verbs, over-long sentences and em-dashes; this skill keeps those rules and adds the document-level and statistical ones (openers, counting, rhythm, lexical repetition, author voice, measured audit).

## Licence

MIT. The example passages are from the author's own coursework.
