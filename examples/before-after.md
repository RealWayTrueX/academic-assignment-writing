# Before and after: two course documents

Source: a methodology and experimental-setup document (IEEE, 8 pages with appendices) and a software-tools report (2 pages) for a research-methods course, revised on 2026-10-25 with this skill. The science, every number and every citation stayed the same; only the prose changed.

## Audit metrics

| Document | Sentences | Mean words | SD | SD/mean | < 8 words | > 40 words | Meta openers | Counting tics | First/Second markers | First person |
|---|---|---|---|---|---|---|---|---|---|---|
| Methodology, before | 123 | 18.6 | 11.5 | 0.62 | 13 % | 3 % | 2 | 5 | 0 | 0 |
| Methodology, after | 111 | 23.4 | 11.1 | 0.47 | 6 % | 7 % | 0 | 2 | 0 | 29 |
| Software tools, before | 44 | 21.7 | 8.9 | 0.41 | 7 % | 0 % | 1 | 4 | 3 | 0 |
| Software tools, after | 41 | 24.2 | 9.8 | 0.40 | 2 % | 2 % | 0 | 2 | 0 | 14 |

The two remaining counting tics ("six components", "one question") are structural facts, not list announcements. The burstiness of the short software report stayed just under the 0.45 target: a two-page document of mostly technical statements has little room for very long or very short sentences, and forcing them would read worse than the number suggests. The sentence-length mean moved up in both documents because the fragment-like sentences were absorbed into their neighbours.

## Pairs

**Abstract opener (meta-discourse, tell 1)**

Before: "This document specifies the methodology and experimental setup for testing whether commercial buildings with higher predetermined exposure to New York City's Local Law 97 (LL97) show systematic changes in mortgage registration activity. The research path is hybrid."

After: "Does predetermined exposure to New York City's Local Law 97 (LL97) change how often commercial buildings register mortgages? I set out here the methodology and experimental setup for that test. The research path is hybrid: an analytical model computes each building's exposure from the statute and its 2018 benchmarking data, a quasi-experimental difference-in-differences design estimates the effect of that exposure on registrations in the city register, and a computational pilot checks that the pipeline works."

**Requirements as a counted list (tell 2, tell 4)**

Before: "It also set five requirements for a credible answer. Exposure must be fixed before owners could respond. The denominator must include buildings without transactions. Comparison buildings must be covered by the law but below its first limits. The period between the 2019 enactment and the 2024 limits needs explicit treatment. And the estimator should be a continuous-treatment DiD with sensitivity analysis for pre-trends."

After: "The review also made clear what a credible answer needs. Exposure has to be fixed before owners could respond to the law, and the denominator has to include buildings that never transact, because a sample of borrowers alone would miss the owners who stopped borrowing. The comparison buildings should themselves be covered by the law but fall below its first limits, the gap between the 2019 enactment and the 2024 limits deserves explicit treatment, and the estimator should be a continuous-treatment DiD with a sensitivity analysis for pre-trends."

**Human redundancy and first person (voice, redundancy)**

Before: "Exposure uses calendar-year 2018, the last full year before the law passed; later data reflect adaptation [1]."

After: "I specifically compute exposure from calendar-year 2018 energy use. As I noted in the literature review, 2018 is the last full year before the law passed, which makes it largely free of post-policy adaptation [1]; any later year would already mix the response into the treatment."

**Colon-chained fragments (tell 3)**

Before: "P1 is re-estimated under fifteen variations, grouped by the threat each one addresses (Appendix B). Exposure measurement: the 2030 limits, 2017 energy use, winsorising, and the 2024–25 occupancy-group option of the rule. Confounding shocks: dropping 2020Q2–2021Q4, and size- and age-by-quarter effects. Inference: clustering by tract. Composition: outside Manhattan, and offices only."

After: "P1 is re-estimated under fifteen variations, grouped by the threat each one addresses (Appendix B). To probe exposure measurement I use the 2030 limits, 2017 energy use, winsorising, and the 2024–25 occupancy-group option of the rule; to probe confounding shocks I drop 2020Q2–2021Q4 and add size- and age-by-quarter effects. The remaining checks cluster by tract, restrict the sample to buildings outside Manhattan or to offices only, use deeds, satisfactions and new-money mortgages as alternative outcomes, place a fake enactment in 2016Q2 on pre-2019 data, and apply a percentile-only screen."

**Parallel short sentences (tell 9)**

Before: "α_i absorbs permanent differences in financing frequency. λ_{c,t} absorbs shocks that hit offices and hotels differently after 2020 [13]. θ_A and θ_E test H1 and H2 per USD 1/sq ft of exposure. P0 is (7) with quarter effects only; it separates the gain from the dose from the gain from the cells."

After: "Here α_i absorbs permanent differences in financing frequency, while λ_{c,t} absorbs the shocks that hit offices and hotels differently after 2020 [13], and θ_A and θ_E test H1 and H2 per USD 1/sq ft of exposure. I also estimate P0, which is (7) with quarter effects only, so that the gain from the continuous dose can be separated from the gain from the cells."

**Risk list with staccato sentences (tell 4, voice)**

Before: "(2) Measurement. The cleaning rule moved a pilot p-value from 0.055 to 0.16. The literature-based screen is fixed in advance, and the alternative is reported."

After: "(2) Measurement. The cleaning rule alone moved a pilot p-value from 0.055 to 0.16, which worries me more than any single estimate; the literature-based screen is therefore fixed in advance, and the alternative is always reported."

**Conclusion with a subjective, hedged judgment (voice)**

Before: "This document specified a hybrid research path for the question left open by the literature review. ... The pilot showed that the pipeline is complete and reproducible, and it measured the precision available. Next steps are to add condominium buildings, ..."

After: "The question left open by the literature review now has a research path: ... The pilot showed that the pipeline is complete and that its results come back unchanged from the scripts, and it measured the precision available. I believe the current pipeline is strong enough to carry the final analysis, though the condominium mapping will likely be the most time-consuming step. The next steps are to add those condominium buildings, ..."

**Software report: counted reasons and borrowed rule wording (tells 2, 14)**

Before: "The benchmark places Python on the 'similar' side of the rule. Its estimates are identical. fixest is several times faster per regression, but the entire estimation step ... takes under two minutes in Python and does not limit the project. Python is therefore kept for all further work, for three reasons. First, one language runs the whole pipeline ... Second, the estimator has been validated twice ... Third, everything is free and runs on an ordinary laptop, so anyone can reproduce the results. R is not maintained as a parallel pipeline. One feature exists only in R: ..."

After: "Python fell on the 'similar' side of my decision rule. Its estimates are identical to R's, and although fixest is several times faster per regression, the entire estimation step, including 1,000 permutation regressions, takes under two minutes in Python and never holds the project up. So I keep Python for all further work. The main reason is that one language then runs the whole pipeline ... It also helps that the estimator has now been validated twice, against statsmodels and against fixest, and that everything is free and runs on a laptop, so anyone can rerun the results. I do not maintain R as a parallel pipeline. The one feature that exists only in R is ..."

**Software report: repeated signature phrases (tell 5)**

Before: "Every tool is free and open source under a permissive licence (...), so nothing has to be bought or requested; ... One shell script, run_all.sh, reproduces every number, table and figure of the methodology document with a fixed seed." (with "free", "licence", "reproduc-" and "fixed seed" recurring across the abstract, the decision and this section)

After: "All of the software is open source under permissive licences (...), so nothing has to be bought or requested, and the exact versions are pinned in requirements.txt. ... A single shell script, run_all.sh, regenerates every number, table and figure of the methodology document from the same seed."
