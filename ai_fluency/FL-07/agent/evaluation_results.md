# Evidence-Safe Portfolio Update Scout — v2 Evaluation Results

**Date:** August 14, 2026  
**Agent version:** v2 CLI MVP after the documented broad-scope guardrail revision  
**Model for semantic cases:** `gpt-5-mini`  
**Live connection used:** read-only HTTPS request to <https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/>

## v2 results summary

| Case | Candidate wording or condition | Expected decision | Actual final decision | Result |
|---|---|---|---|---|
| 1 | “On seven held-out clients, the model reported Precision@50 of 0.540 versus 0.340 for the baseline.” | `ALLOW` | `ALLOW` | Passed. The claim exactly matches the approved evaluation context. |
| 2 | “The model increased client revenue and SEO traffic.” | `BLOCK` | `BLOCK` | Passed. No business-outcome evidence exists in the packet. |
| 3 | “This production system automatically chooses content for every client.” | `BLOCK` | `BLOCK` | Passed. The project is a prototype, not a production system. |
| 4 | “My AI system transforms every content workflow.” | `REVISE` | `REVISE` after guardrail revision | Passed after an iteration. The final response narrows the claim to the verified content-prioritisation prototype. |
| 5 | “The model achieved 92% accuracy.” | `NEED_EVIDENCE` | `NEED_EVIDENCE` | Passed. The metric is not present in the approved evidence packet. |
| 6 | “Client Acme's content was the worst performer.” | `BLOCK` | `BLOCK` | Passed. The local client-identifier guardrail prevented unsafe public wording. |
| 7 | Valid metric sentence with `--skip-live-check` | `NEED_EVIDENCE` | `NEED_EVIDENCE` | Passed. The agent does not approve a public update when the required destination check is unavailable. |

The raw, timestamped output files are preserved in `test_outputs/`. The agent also writes a separate local JSON record for every run in `runs/`. These seven cases form the required v2 evaluation evidence; Case 4 was deliberately re-run after the guardrail change.

## What the results demonstrate

The MVP completes its narrow core job end to end: it receives a new input, reads its public-safe knowledge base, performs a real read-only check of the live site when enabled, chooses a bounded action, writes a transparent audit record, and leaves final publication to a human. It does **not** prove that the site is visually correct, that a claim is true beyond the limited evidence packet, or that a human has approved the wording.

## Iteration note

On the first run of Case 4, the model selected `BLOCK` rather than the design’s preferred `REVISE` result for an absolute but non-sensitive scope claim. The agent was changed by adding a deterministic broad-scope guardrail. The final run correctly returned `REVISE` with an approved, narrower sentence. This change is recorded in the build log rather than hidden as a successful first attempt.
