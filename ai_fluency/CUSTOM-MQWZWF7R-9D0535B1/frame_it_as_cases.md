# Frame It as Cases: Work That Speaks for Itself

> **Voice card:** Plainspoken, curious, evidence-first, honest about limits.

## Audience and one action

This portfolio is for an **entry-level machine-learning hiring manager at an SEO or content-intelligence company**. The action is simple: **open the capstone case study**. The case below is the one work piece in the portfolio sitemap; the sitemap intentionally avoids a generic projects grid that would dilute the proof path.[1]

## Case: Leakage-aware content-prioritisation prototype

### The problem

Content teams may have far more candidate pages than they can inspect in a review cycle. I framed the task as prioritisation for **editorial review**, not automatic refresh decisions. The important technical risk was misleading validation: if pages from the same client appeared in both training and evaluation, the model could appear stronger because client-level patterns leaked across the split.[2]

### What I did and decided

I worked with a public-safe anonymised starter release of about 30,000 content pages across 32 pseudonymised clients. I built a random-forest ranking prototype and compared it with a transparent baseline. Instead of a random page-level split, I held out seven pseudonymised clients from the evaluation set. That decision made the comparison test whether the model carried useful ranking signal to client groups it had not seen in training.[2]

I also placed an interpretation boundary around the output: the ranking should create a **review-for-refresh queue**. An editor still diagnoses each page and decides whether to refresh, expand, monitor, defer, or take no action. The prototype does not choose or publish changes automatically.[2]

### What came of it

On the seven held-out clients, the model achieved **Precision@50 of 0.540**, compared with **0.340** for the transparent baseline. This is evidence that the top of the model’s queue was more concentrated with review candidates under this evaluation design. It is not evidence of traffic recovery, a causal effect from edits, or a production-ready autonomous system.[2]

## Bio

I am Umer Sajid, an early-career machine-learning practitioner building public, reproducible prototypes. My work focuses on making evaluation choices inspectable—especially when a model is used to prioritise human review rather than replace it.

## Contact / CTA

If you are assessing how I reason about applied ML for content systems, **open the capstone case study** first. It shows the data boundary, validation design, model comparison, measured result, and limits in one place.[2]

## Voice revision

| Stage | Sentence |
|---|---|
| Generic machine draft | “I delivered a results-driven ML solution that optimised content performance and drove measurable business impact.” |
| Evidence-first portfolio version | “I evaluated a ranking prototype on held-out clients and found higher Precision@50 than a transparent baseline; the result supports an editor’s review queue, not a traffic or automation claim.” |

The revision removes unverified “business impact” language, names the evaluation boundary, and states what the result can and cannot support.

## Evidence boundary

This document derives its factual claims from the public capstone report. It does not claim access to raw client data, production deployment, traffic impact, employer work, or outcomes not measured in the report.

## References

[1] [Umer Sajid, *Portfolio Sitemap + Toolkit*](https://github.com/UmerSajid842/flyrank-ai-fluency/blob/main/ai_fluency/CUSTOM-MQWZGZCD-45C6C6BE/portfolio_sitemap_and_toolkit.md)

[2] [Umer Sajid, *Capstone Report: Refresh / Content Opportunity Scoring*](https://github.com/UmerSajid842/flyrankmlproject/blob/main/work/capstone_report.md)
