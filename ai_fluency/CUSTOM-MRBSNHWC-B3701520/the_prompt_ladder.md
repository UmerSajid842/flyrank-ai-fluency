# The Prompt Ladder: From Vague Request to Evidence-Bound Case Introduction

## Real task and evidence boundary

The real task is to draft a concise portfolio introduction for the public capstone case study. The source of truth is the public capstone report: an anonymised content-page dataset, client-grouped evaluation, and a Precision@50 comparison between a random-forest model (0.540) and a transparent baseline (0.340).[1]

All six prompts below were run in **Claude Sonnet 4.6** through a programmatic Claude environment on 13 August 2026. The full, unedited prompts and outputs are preserved in [`week2_claude_prompt_runs.json`](../_evidence/week2_claude_prompt_runs.json). Summaries below describe what the model actually returned; they are not simulated outputs.

## Run log

| Run | Exactly one added layer | Representative actual output | What changed | What improved | What still failed | What to try next |
|---|---|---|---|---|---|---|
| **Baseline** | None — deliberately weak one-line prompt | “I’d be happy to help … but I need some details from you first …” | No added layer. | The model correctly refused to invent details. | It produced no usable case introduction and gave the user a generic questionnaire. | Add a role that sets evidence discipline. |
| **V1** | **Role assignment** | “I won’t invent metrics, outcomes, employers, datasets, or technical choices …” | Added: *evidence-first portfolio editor for a junior ML candidate*. | The refusal became more specific about portfolio risk and credibility. | The output was longer but still no usable introduction because the prompt contained no factual context. | Add the real audience, decision purpose, and fact pack. |
| **V2** | **Context and motivation** | “This case study documents a random-forest prototype … holding out seven pseudonymised clients …” | Added the hiring-manager audience, the editorial-review purpose, and verified metric/data boundary. | The model used the correct broad facts and named the no-traffic/no-automation boundary. | It produced a long multi-section mini-report rather than a portfolio introduction; no output length or layout was controlled. | Add a brief style example that demonstrates evidence-first voice. |
| **V3** | **Few-shot example** | “Editorial teams that refresh ageing content face a triage problem …” | Added one miniature example of validation + baseline + claim boundary, for voice only. | The opening became more coherent and the limitation was brought nearer to the result. | The output was still too long for a homepage-facing introduction and began with an unsourced generalisation about editorial teams. | Add an exact return structure and length target. |
| **V4** | **Output structure** | Headline + introduction + limitation, including “27 of the top 50” and a “rule-based baseline.” | Added an exact three-part return format and an introduction word range. | The response became easy to scan and compare side by side. | **This change did not fully help.** The headline missed the requested 30-word target, and the output introduced unsupported specificity: the source says “transparent baseline,” not “rule-based baseline,” and the prompt did not ask the model to convert Precision@50 into candidate counts. | Add a final fact-checking step and explicit ban on extrapolating beyond the fact pack. |
| **V5** | **Step decomposition** | “I built a random-forest prototype designed to rank anonymised content pages …” | Added silent steps: list allowed facts, draft, then remove unsupported claims. | The response was shorter and retained the three requested sections and the no-traffic limitation. | The headline still missed the exact 30-word target. It also added interpretive language (“standard precaution,” “simple rule,” “meaningful signal”) not stated in the supplied fact pack. | In the reusable template, explicitly prohibit baseline-type labels, derived counts, and interpretive adjectives unless supplied as facts. |

## Final reusable prompt template

> You are an evidence-first portfolio editor. Draft a case-study introduction for **[audience]**. The intended decision is **[human decision/action]**, not automated action. Use **only** the verified facts below. Do not invent employers, tools, data fields, outcomes, causal claims, production use, baseline types, derived counts, or interpretive adjectives. Do not convert metrics into counts unless the count is explicitly supplied. 
>
> **Verified facts:** [paste verified fact pack]
>
> Return exactly: (1) a headline of **at most 24 words**, (2) a 130–160 word introduction, and (3) a one-sentence limitation. Use plain English. Before writing, silently list the allowed facts; then draft; then silently remove any claim that is not in the allowed facts. Do not reveal the internal check.

## What I learned

Adding more text to a prompt was not automatically an improvement. Role, context, and a style example made the output usable, but output structure exposed a new issue: a polished format can still include unsupported details. The reusable prompt therefore makes the verification boundary explicit rather than assuming a model will infer it.

## References

[1] [Umer Sajid, *Capstone Report: Refresh / Content Opportunity Scoring*](https://github.com/UmerSajid842/flyrankmlproject/blob/main/work/capstone_report.md)
