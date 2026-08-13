# FL-02 — Prompting Fundamentals on a Real Task

## Real target task

**Target task from FL-01:** Draft an honest portfolio case-study introduction for the capstone. The audience is an entry-level ML hiring manager at an SEO or content-intelligence company. The task is to communicate an inspectable ML evaluation and a human editorial-review decision without inventing production or traffic results.

The verified fact pack came from the public capstone report: approximately 30,000 anonymised pages across 32 pseudonymised clients; seven held-out clients; model Precision@50 of 0.540 versus a transparent baseline at 0.340; and a review-for-refresh—not autonomous-editing—use boundary.[1]

## Saved prompt and output evidence

All six Claude runs, including the exact prompts and full unedited outputs, are saved in [`week2_claude_prompt_runs.json`](../_evidence/week2_claude_prompt_runs.json). The final prompt was also run in a real public ChatGPT guest session; its exact prompt and output are saved in [`week2_chatgpt_final_prompt_run.md`](../_evidence/week2_chatgpt_final_prompt_run.md). These files are the raw record supporting the iteration notes below.

| Version | Named technique added | Actual observed output difference | Iteration note |
|---|---|---|---|
| **Baseline** | None — naive one-line prompt | Claude asked for missing project details rather than drafting text. | The vague task had no facts, audience, or boundary. Refusing to invent was appropriate, but it did not meet the writing need. |
| **V1** | **Role assignment** | Claude still asked for facts, but framed the refusal around portfolio credibility and not fabricating results. | The role improved the quality standard, not task completion. The largest remaining need was real context. |
| **V2** | **Context and motivation** | Claude drafted a fact-rich, multi-section case study with the held-out-client result and limitation. | Audience, decision purpose, and verified facts made a usable draft possible. It was too long and unconstrained in format. |
| **V3** | **Few-shot examples** | Claude opened with a clearer triage framing and placed the limitation directly after the quantitative comparison. | The miniature evidence-first example improved voice and claim boundaries. It still exceeded the likely homepage-introduction length. |
| **V4** | **Output structure** | Claude returned a headline, 130–160 word introduction, and limitation. | Structure made output comparable and ready to edit. It also revealed a factual-quality problem: it labelled the baseline “rule-based” and inferred counts not in the supplied facts. |
| **V5** | **Step decomposition** | Claude silently checked the fact pack before returning the three requested sections. | The response was shorter and preserved the limitation, but still used unsupplied interpretive language (“standard precaution,” “simple rule,” “meaningful signal”) and missed the exact headline word target. This confirms that step decomposition helps but does not replace a human evidence review. |

## Cross-model comparison — final prompt

The final reusable prompt was run once in Claude Sonnet 4.6 and once in a public ChatGPT guest session on 13 August 2026. Both outputs are preserved in the raw evidence files above.

| Criterion | Claude Sonnet 4.6 | ChatGPT guest session | Practical decision |
|---|---|---|---|
| **Tone** | Technical and cautious; it emphasised generalisation and evaluation design. | Direct and reader-facing; it posed the editorial decision as a narrow practical question. | Use ChatGPT’s plainer framing as an editing reference, then verify all facts. |
| **Accuracy** | Preserved core metrics and limitations but introduced “standard precaution,” “simple rule,” and “meaningful signal,” none of which were supplied facts. | Preserved supplied metrics, client holdout, and no-traffic/no-automation limit; it did not label the baseline type or infer counts. | For this run, ChatGPT stayed closer to the supplied fact boundary. Still verify every claim against the report. |
| **Structure** | Returned the requested headline/introduction/limitation sections, but the headline missed the exact 30-word request. | Returned all three sections; the headline was longer than the requested target. | Both need a final mechanical length check. |
| **Failure points** | Interpreted the baseline and model result beyond the provided wording. | Produced a long, dense headline (despite requested brevity). | Add explicit restrictions on baseline labels, derived counts, interpretive adjectives, and headline length. |

## Final reusable prompt template

> You are an evidence-first portfolio editor. Draft a case-study introduction for **[audience]**. The intended decision is **[human decision/action]**, not automated action. Use only the verified facts below. Do not invent employers, tools, data fields, outcomes, causal claims, production use, baseline types, derived counts, or interpretive adjectives. Do not convert metrics into counts unless the count is explicitly supplied.
>
> **Verified facts:** [paste fact pack]
>
> Return exactly: (1) a headline of at most 24 words, (2) a 130–160 word introduction, and (3) a one-sentence limitation. Use plain English. Before writing, silently list the allowed facts; then draft; then silently remove any claim that is not in the allowed facts. Do not reveal the internal check.

## Verification checklist

Before publishing an output from this template, I will check it against the source report for: the correct model and baseline description; the correct held-out-client evaluation; the exact reported metrics; the distinction between ranking for review and taking action; and the absence of traffic, causal, production, employer, or automation claims.

## Tutorial completion boundary

FL-02 also asks for completion of the basics chapters of Anthropic’s Prompt Engineering Interactive Tutorial. This repository contains the applied prompt work and the real model-output evidence above. It **does not claim** completion of the tutorial because no completion record was supplied for it. That prerequisite should be completed in the user’s own Academy account before presenting FL-02 as fully complete.

## References

[1] [Umer Sajid, *Capstone Report: Refresh / Content Opportunity Scoring*](https://github.com/UmerSajid842/flyrankmlproject/blob/main/work/capstone_report.md)
