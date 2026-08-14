# Umer Sajid — Public Portfolio Case-Study Context

## Purpose

This reference gives Claude the **public-safe** context for Umer Sajid’s entry-level machine-learning portfolio. It must be used to draft, review, or structure portfolio content without inventing client details, production impact, or unsupported metrics.

## Primary case study

**Title:** Leakage-aware content-prioritisation prototype

**Decision problem:** The project investigates whether public-safe content signals can help prioritise which content should be reviewed first. It is a prototype and case study, not a production deployment or a claim of causal business impact.

**Verified result:** On seven held-out clients, the reported Precision@50 was **0.340** for the baseline and **0.540** for the model. This is a model-evaluation result, not a revenue, traffic, or business-outcome claim.

**Method principles:**

1. Keep the data framing public-safe and avoid client-identifying information.
2. Use leakage-aware evaluation controls.
3. Show the result before listing tools.
4. Name the prototype boundary and limitations clearly.
5. Prefer inspection: link readers to the public paper, report, notebook, charts, and repository rather than making broad claims.

## Public evidence links

| Evidence | URL | What it supports |
|---|---|---|
| Live case-study paper | <https://umersajid842.github.io/flyrankmlproject/> | Public explanation of the decision problem, methodology, result, limitation, and recommendation. |
| Capstone repository | <https://github.com/UmerSajid842/flyrankmlproject> | Public code and project history. |
| Capstone report | <https://github.com/UmerSajid842/flyrankmlproject/blob/main/work/capstone_report.md> | Detailed public-safe framing and reported evaluation. |
| AI Fluency work repository | <https://github.com/UmerSajid842/flyrank-ai-fluency> | Identity kit, content map, and workflow evidence. |

## Approved portfolio claim

> I build inspectable ML prototypes that turn messy content signals into a clearer prioritisation decision.

## Portfolio writing rules

- Use precise language: **prototype**, **reported evaluation**, **held-out clients**, **Precision@50**, and **public-safe**.
- Never say the project was productionised, improved SEO, increased revenue, or caused client outcomes.
- Do not name clients, upload datasets, include client identifiers, or expose private credentials.
- Lead with the case study and provide the next action: **Open the case study.**
- When uncertain, state what evidence is missing rather than filling gaps with plausible text.

## Suggested verification prompt

> Using only the project knowledge, draft a 120-word home-page case-study introduction. Include the approved claim, the verified Precision@50 comparison, one limitation, and the CTA “Open the case study.” Do not invent any client, business, production, or causal-impact claim.
