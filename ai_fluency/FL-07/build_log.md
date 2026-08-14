# Build Log — Evidence-Safe Portfolio Update Scout

**Assignment:** `FL-07`  
**Author:** Umer Sajid  
**Build date:** August 14, 2026

## Goal and scope cut

The original personal-agent goal was narrowed to one small job: audit proposed public ML portfolio wording against an approved public-safe evidence packet. The MVP does not try to write an entire portfolio, browse for new sources, update a site, deploy, email, post, book meetings, or use private data. That scope cut made an end-to-end version feasible and safer.

## Build record

| Stage | What happened | Result and decision |
|---|---|---|
| 1. Design | Defined the Evidence-Safe Portfolio Update Scout as a read-only reviewer of candidate portfolio copy. | Chosen because it addresses a repeated real risk: turning a model-evaluation result into an unsupported public claim. |
| 2. Knowledge base | Connected the agent to `portfolio_case_study_context.md` and the current `docs/index.html`. | The only source context is public-safe and inspectable in the repository. No dataset or client material was added. |
| 3. Live data connection | Added one read-only HTTPS request to the live ML Work site. | The tool records whether the known public URL responded. It has no authentication or deployment authority. |
| 4. Structured reasoning | Implemented a `gpt-5-mini` call using a strict JSON schema with four allowed actions: `ALLOW`, `REVISE`, `BLOCK`, and `NEED_EVIDENCE`. | The model cannot call tools or publish. Every result requires human review. |
| 5. Local guardrails | Added deterministic checks for secret-related terms and apparent client/customer identifiers before the model request. | Potentially sensitive candidate wording is blocked locally instead of being sent to the model. |
| 6. First code validation | Ran `python3 -m py_compile ai_fluency/FL-07/agent/audit_portfolio_copy.py`. | Passed. |
| 7. First end-to-end run | Ran the verified Precision@50 sentence through the agent with the live URL check. | Passed with `ALLOW`; a timestamped audit record was written. |
| 8. Test-output failure | The first attempt to redirect test output failed because `agent/test_outputs/` did not exist. | Created the missing folder, then reran the same intended test successfully. No agent code was changed for this filesystem setup issue. |
| 9. Evaluation run | Ran impact, production, broad-scope, unsupported-metric, privacy, and simulated unreachable-site cases. | All actions were safe. The broad-scope case required an iteration. |
| 10. Guardrail iteration | The first semantic review of “My AI system transforms every content workflow” returned `BLOCK`, while the desired behavior was a narrower revision. | Added a deterministic broad-scope guardrail that returns `REVISE` and a public-safe replacement. The rerun passed. |

## Final implemented behavior

The final agent accepts a candidate sentence or a text file, reads the approved public-safe context, checks the known live URL, applies local safety checks, uses structured model output only when appropriate, and writes a JSON record under `agent/runs/`. It never changes the public site. See [`agent/README.md`](agent/README.md) and [`agent/evaluation_results.md`](agent/evaluation_results.md) for setup and results.

## Known limitations

| Limitation | Consequence | Human check |
|---|---|---|
| The evidence packet is intentionally narrow. | The agent cannot validate any new metric, production status, business outcome, or client-specific statement. | Add a public-safe source first, then review it manually before expanding the packet. |
| URL status is shallow. | A `200` response does not prove layout quality, link integrity beyond the requested page, accessibility, or content accuracy. | Open the site and review it on real devices. |
| Local identifier detection is heuristic. | It can miss or falsely flag a name pattern. | Never enter private information; manually review every input and output. |
| No write tools are available. | The agent cannot finish publication by itself. | A human intentionally makes every site change and deployment. |
| The required demonstration is personal. | An unedited approximately two-minute capture cannot be truthfully created from logs or substituted with slides. | Umer must record one raw screen capture of a successful run. |

## Pending personal evidence

The functional CLI and test records are complete. The required raw, unedited screen recording remains pending Umer’s action. A truthful recording should show: start the command, input one candidate sentence, the live site status, the structured result, the saved audit path, and the statement that no publication occurred. It should also point out one guardrail, such as the blocked revenue/SEO claim or the client-identifier stop.
