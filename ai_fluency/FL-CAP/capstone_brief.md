# Evidence-Safe Portfolio Companion

**FlyRank General AI Fluency · Impact Project**

**Author:** Umer Sajid
**Live capstone page:** <https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/ai-work.html>

## What I built

I built an **Evidence-Safe Portfolio Companion**: a public ML Work portfolio plus a small personal agent that reviews proposed portfolio wording before a human updates the site.

The public website presents a real, public-safe machine-learning case study. The companion CLI, **Evidence-Safe Portfolio Update Scout**, compares a proposed sentence or short paragraph with an approved case-study context and returns one structured recommendation: `ALLOW`, `REVISE`, `BLOCK`, or `NEED_EVIDENCE`.

## Why I built it

A portfolio can become less trustworthy when a real technical result is described with an unsupported business, production, or client-impact claim. I wanted a repeatable check that helps me keep public wording tied to inspectable evidence while preserving human control of every change.

## How it works

1. I provide a proposed public portfolio sentence or paragraph.
2. Local guardrails stop obvious secret-related terms, apparent client-identifying wording, and broad workflow claims.
3. The agent reads only an approved public-safe evidence packet and the current public home-page source.
4. It makes one fixed, read-only HTTPS reachability check to the live portfolio.
5. When no guardrail stops the input, a structured `gpt-5-mini` step returns a bounded recommendation.
6. The CLI saves a timestamped audit record. A person decides whether to revise or publish anything.

## Verified evidence

| Evidence | What it shows |
|---|---|
| [Live AI Work capstone page](https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/ai-work.html) | The public project narrative, workflow, tool stack, evaluation record, and limits. |
| [Agent source and run guide](https://github.com/UmerSajid842/flyrank-ai-fluency/tree/main/ai_fluency/FL-07/agent) | The actual Python CLI, bounded actions, public-safe inputs, and reproducible local run instructions. |
| [Build log](https://github.com/UmerSajid842/flyrank-ai-fluency/blob/main/ai_fluency/FL-07/build_log.md) | A documented scope cut, real setup failure, and guardrail iteration. |
| [Evaluation results](https://github.com/UmerSajid842/flyrank-ai-fluency/blob/main/ai_fluency/FL-07/agent/evaluation_results.md) | Seven documented cases that cover supported wording, overclaims, privacy, unavailable deployment, and the post-iteration revision case. |
| [Current capstone verification](capstone_verification.md) | A new end-to-end run: syntax check passed, the fixed public URL returned HTTP 200, the verified candidate received `ALLOW`, and human review remained required. |
| [Public ML Work case study](https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/case-study.html) | The public evidence base the agent is designed to protect. |

## Boundaries and limitations

> The agent is advisory only. It cannot edit the site, deploy, commit, post, email, book, or publish. It does not read datasets, private notebooks, raw queries, client information, credentials, or other secrets.

A reachable URL does not prove visual quality, accessibility, link integrity, or truth beyond the approved evidence packet. An `ALLOW` result is not permission to publish. Every result requires human review.

## Impact

The capstone creates a reusable workflow for protecting evidence quality during portfolio updates. Its demonstrated result is the safe, structured handling of seven documented evaluation cases; it does **not** claim revenue, traffic, SEO, production deployment, client outcomes, or causal business impact.
