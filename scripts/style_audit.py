#!/usr/bin/env python3
"""Style audit for academic prose (.tex, .md, .txt): the statistical and lexical tells that make
a text read as machine-written. Standard library only.

    python3 style_audit.py paper.tex [more files] [--json] [--sentences]

Reported per file
  sentences, words, mean and SD of sentence length (SD/mean is the burstiness ratio; human
  academic prose usually sits around 0.5 or above), share of very short (< 8 words) and very
  long (> 40 words) sentences, meta-discourse openers ("This document specifies..."),
  counting tics ("three reasons", "First, ... Second, ..."), AI-flavoured vocabulary,
  em-dashes, first-person markers, and the most repeated content words and bigrams.
The script measures; it does not rewrite. Read the flagged sentences and decide.
"""
import argparse
import collections
import json
import re
import sys

AI_WORDS = [
    "delve", "crucial", "pivotal", "tapestry", "testament", "moreover", "furthermore", "additionally",
    "notably", "leverage", "utilize", "utilise", "comprehensive", "intricate", "multifaceted", "underscore",
    "underscores", "foster", "landscape", "realm", "paradigm", "synergy", "holistic", "seamless", "robust",
    "nuanced", "showcase", "elevate", "unlock", "navigate", "embark", "journey", "transformative",
    "groundbreaking", "cutting-edge", "state-of-the-art", "it is worth noting", "it is important to note",
    "in conclusion", "in summary", "plays a vital role", "plays a crucial role", "not only", "but also",
    "a wide range of", "in today's", "ever-evolving", "game-changer", "meticulous", "meticulously",
]
META_OPENERS = re.compile(
    r"\b(This|The present|The following) (document|paper|report|section|chapter|study|work|thesis|essay)"
    r" (specifies|specified|states|stated|defines|defined|describes|described|presents|presented|provides|"
    r"provided|outlines|outlined|aims|is organi[sz]ed|discusses|explores|summari[sz]es|concludes)\b", re.I)
NUMBER_WORDS = r"(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|several|a number of)"
COUNT_NOUNS = (r"(reasons?|requirements?|criteria|criterion|components?|steps?|ways?|points?|factors?|"
               r"conclusions?|actors?|sources?|aspects?|dimensions?|features?|advantages?|benefits?|"
               r"limitations?|challenges?|stages?|phases?|elements?|parts?|hypotheses|questions?|goals?)")
COUNTING = re.compile(rf"\b{NUMBER_WORDS}\s+(main\s+|key\s+|major\s+|principal\s+)?{COUNT_NOUNS}\b", re.I)
ORDINALS = re.compile(r"(^|[.;:]\s+)(First(ly)?|Second(ly)?|Third(ly)?|Fourth(ly)?|Fifth(ly)?|Finally|Lastly),", re.M)
FIRST_PERSON = re.compile(r"\b(I|my|me|mine|we|our|us)\b")
STOP = set("""a an the and or but so of to in on for with by at from as is are was were be been being it its this
that these those which who whom whose what when where why how not no nor than then there here also only such each
each other into over under between within without about after before during per via while if because therefore
thus hence can could may might must shall should will would do does did done has have had having more most less
least very much many few all any some both either neither own same too s t""".split())


def detex(text):
    """Rough LaTeX to prose. Drops floats, math and preamble, keeps the words of text commands."""
    text = re.sub(r"(?<!\\)%.*", "", text)
    m = re.search(r"\\begin\{document\}", text)
    if m:
        text = text[m.end():]
    text = re.split(r"\\bibliographystyle|\\begin\{thebibliography\}", text)[0]
    for env in ("table\\*?", "figure\\*?", "tabular[xy]?", "align\\*?", "equation\\*?", "gather\\*?",
                "IEEEdescription", "IEEEkeywords", "thebibliography", "tikzpicture", "lstlisting", "verbatim"):
        text = re.sub(rf"\\begin\{{{env}\}}.*?\\end\{{{env}\}}", " ", text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", " X ", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", " X ", text, flags=re.S)
    text = re.sub(r"\$[^$]*\$", " X ", text)
    text = re.sub(r"\\(cite|ref|eqref|label|autoref|cref|url|includegraphics|input|bibliography|graphicspath)"
                  r"\*?(\[[^\]]*\])?\{[^}]*\}", " ", text)
    text = re.sub(r"\\(section|subsection|subsubsection|paragraph|title|author|caption)\*?(\[[^\]]*\])?\{([^}]*)\}",
                  "\n", text)   # headings, title block and captions are not prose
    text = re.sub(r"\\IEEEPARstart\{(\w)\}\{(\w+)\}", r"\1\2", text)
    for _ in range(3):
        text = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?\{([^{}]*)\}", r"\2", text)
    text = re.sub(r"\\[A-Za-z]+\*?", " ", text)
    text = text.replace("~", " ").replace("``", '"').replace("''", '"').replace("--", "-")
    text = re.sub(r"[{}]", "", text)
    return text


def demark(text):
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.S)           # front matter
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"^\s*\|.*\|\s*$", " ", text, flags=re.M)       # tables
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.M)
    text = re.sub(r"[*_`>]", "", text)
    return text


ABBR = re.compile(r"\b(e\.g|i\.e|cf|vs|etc|Fig|Figs|Eq|Eqs|Sec|Tab|No|Prof|Dr|Mr|Ms|St|Apr|Jan|Feb|Mar|Jun|Jul|Aug|"
                  r"Sep|Sept|Oct|Nov|Dec|U\.S|al)\.")


def sentences(prose):
    prose = ABBR.sub(lambda m: m.group(0).replace(".", "<dot>"), prose)
    prose = re.sub(r"(\d)\.(\d)", r"\1<dot>\2", prose)
    prose = re.sub(r"\s+", " ", prose)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\"'])", prose)
    out = []
    for p in parts:
        p = p.replace("<dot>", ".").strip()
        if len(words(p)) >= 3:          # drop run-in labels such as "(1) Interpretation."
            out.append(p)
    return out


def words(s):
    return re.findall(r"[A-Za-z][A-Za-z'-]*|\d[\d,.]*", s)


def audit(path):
    raw = open(path, encoding="utf8", errors="replace").read()
    prose = detex(raw) if path.endswith(".tex") else demark(raw) if path.endswith((".md", ".markdown")) else raw
    sents = sentences(prose)
    lens = [len(words(s)) for s in sents]
    n = len(lens) or 1
    mean = sum(lens) / n
    sd = (sum((x - mean) ** 2 for x in lens) / n) ** 0.5
    low = prose.lower()
    ai_hits = {w: len(re.findall(rf"\b{re.escape(w)}\b", low)) for w in AI_WORDS}
    ai_hits = {w: c for w, c in ai_hits.items() if c}
    toks = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]+", prose)]
    content = [w for w in toks if w not in STOP and len(w) > 3]
    uni = collections.Counter(content).most_common(12)
    bigrams = collections.Counter(zip(content, content[1:]))
    bi = [(" ".join(b), c) for b, c in bigrams.most_common(40) if c >= 3][:10]
    return {
        "file": path,
        "sentences": len(sents),
        "words": sum(lens),
        "mean_len": round(mean, 1),
        "sd_len": round(sd, 1),
        "burstiness": round(sd / mean, 2) if mean else 0,
        "short_lt8_share": round(sum(1 for x in lens if x < 8) / n, 3),
        "long_gt40_share": round(sum(1 for x in lens if x > 40) / n, 3),
        "max_len": max(lens) if lens else 0,
        "meta_openers": META_OPENERS.findall(prose) and [m[0] + " " + m[1] + " " + m[2] for m in META_OPENERS.findall(prose)],
        "counting_tics": [m.group(0) for m in COUNTING.finditer(prose)],
        "ordinal_markers": len(ORDINALS.findall(prose)),
        "ai_words": ai_hits,
        "em_dashes": prose.count("\u2014") + (len(re.findall(r"(?<!-)---(?!-)", raw)) if path.endswith(".tex") else 0),
        "first_person": len(FIRST_PERSON.findall(prose)),
        "top_words": uni,
        "top_bigrams": bi,
        "_sents": sents, "_lens": lens,
    }


def report(a, show_sentences=False):
    print(f"\n== {a['file']}")
    print(f"sentences {a['sentences']}  words {a['words']}  mean {a['mean_len']}  sd {a['sd_len']}  "
          f"burstiness {a['burstiness']}  <8w {a['short_lt8_share']:.0%}  >40w {a['long_gt40_share']:.0%}  max {a['max_len']}")
    print(f"meta-discourse openers: {a['meta_openers'] or 'none'}")
    print(f"counting tics ({len(a['counting_tics'])}): {', '.join(a['counting_tics']) or 'none'}")
    print(f"First/Second/Third markers: {a['ordinal_markers']}   em-dashes: {a['em_dashes']}   first person: {a['first_person']}")
    print(f"AI-flavoured words: {a['ai_words'] or 'none'}")
    print("repeated words: " + ", ".join(f"{w} {c}" for w, c in a["top_words"]))
    print("repeated bigrams: " + (", ".join(f"{w} {c}" for w, c in a["top_bigrams"]) or "none"))
    if show_sentences:
        print("-- very short:")
        for s, l in zip(a["_sents"], a["_lens"]):
            if l < 8:
                print(f"   [{l}] {s}")
        print("-- very long:")
        for s, l in zip(a["_sents"], a["_lens"]):
            if l > 40:
                print(f"   [{l}] {s}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--sentences", action="store_true", help="list very short and very long sentences")
    args = ap.parse_args()
    results = [audit(f) for f in args.files]
    if args.json:
        print(json.dumps([{k: v for k, v in r.items() if not k.startswith("_")} for r in results], indent=1))
    else:
        for r in results:
            report(r, args.sentences)


if __name__ == "__main__":
    main()
