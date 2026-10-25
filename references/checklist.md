# Manual pass and verification

Run the audit first (`python3 scripts/style_audit.py paper.tex --sentences`), then walk the document once for each item below. Fix the source, re-run, and stop when the remaining flags are deliberate.

## A. Openings and closings
- [ ] The abstract, the introduction and the conclusion do not begin with "This document/paper/section ...".
- [ ] The conclusion says what is now known and what comes next; it does not mirror the abstract.
- [ ] Each section's first sentence states something, not that something will be stated.

## B. Lists and counting
- [ ] No sentence announces a count that the next sentences then enumerate, unless the labels are reused later.
- [ ] No "First, ... Second, ... Third, ..." chains in the body.
- [ ] Remaining numbered lists (assumptions, risks, robustness checks) are referred to by their labels somewhere.

## C. Sentences
- [ ] No fragment in body text; every sentence has a subject and a finite verb.
- [ ] No colon-chained noun phrases standing in for sentences.
- [ ] No three consecutive sentences with the same skeleton.
- [ ] Audit statistics inside the targets: mean 18 to 26 words, SD/mean at least 0.45, under one in ten sentences above 40 words or below 8.
- [ ] Sentences above 45 words are split unless the clause structure carries them.

## D. Paragraphs
- [ ] Paragraph openers vary (question, concession, cause, example, judgment, back-reference).
- [ ] Each paragraph has one job; the sentence that states that job exists.
- [ ] Transitions are causal or logical ("so", "because", "which is why"), not additive filler ("Moreover", "Additionally").

## E. Words
- [ ] Machine lexicon absent (see `ai-tells.md`, row 10).
- [ ] No signature phrase appears more than twice; check the "repeated words" and "repeated bigrams" lines of the audit.
- [ ] No em-dashes.
- [ ] Verbs no stronger than the evidence (consistent with, suggests, shows).

## F. Voice
- [ ] Judgments, choices and worries are in the first person singular with honest hedges.
- [ ] Facts and results are impersonal.
- [ ] No stray "we", "our" or "my" that breaks the voice; no parenthetical patches.
- [ ] Where the logic is hard, one plain-words restatement or a back-reference to earlier work exists.

## G. Verification after editing
- [ ] Recompile; page count and float positions are within the brief.
- [ ] The multiset of numbers in the body is unchanged (apart from edits you intended). Example:

```python
import re, collections
def nums(path):
    t = open(path, encoding="utf8").read().split("\\begin{document}")[1]
    return collections.Counter(re.findall(r"[-+]?\d[\d,.]*\d|\b\d\b", t))
A, B = nums("before.tex"), nums("after.tex")
print("removed", dict(A - B)); print("added", dict(B - A))
```

- [ ] The set of citation keys is unchanged: `grep -o '\\cite{[^}]*}' file.tex | sort | uniq -c` before and after.
- [ ] A change log lists every paragraph touched and why, and the before/after audit table is in the report.

## H. Report

Write the report in the user's language. Lead with what changed and what the metrics now are; then the files. Name the rules applied. Do not claim a detector score; the audit measures tells, it does not predict a classifier.
