# Documentation and Demo Video — Evidence-Safe Portfolio Update Scout

## Completed documentation

The agent documentation is available in [`../FL-07/agent/README.md`](../FL-07/agent/README.md). It covers the agent’s purpose and audience, required public-safe inputs, reproducible setup, command-line usage examples, architecture, authority limits, evaluation evidence, and limitations. The post-iteration validation is documented in [`../FL-07/agent/evaluation_results.md`](../FL-07/agent/evaluation_results.md).

| Requirement | Evidence location | Status |
|---|---|---|
| Purpose and audience | Agent README: “Audience and use” | Complete |
| Reproducible setup | Agent README: “Setup” | Complete |
| Usage example | Agent README: “Run a review” | Complete |
| Architecture sketch | Agent README: Mermaid flowchart | Complete |
| v2 evaluation results | `agent/evaluation_results.md` | Complete |
| Limits and guardrails | Agent README: “Guardrails and limitations” | Complete |
| 3–5 minute narrated, unlisted YouTube video | User recording and upload | Pending user action |

## Recording plan for Umer

The video must be **one unedited 3–5 minute screen recording with voice narration**, not slides. It should show a real end-to-end run, one limitation or guardrail, and one design decision. Do not cut away, speed up, add music, or claim the agent can publish work.

### Before recording

1. Open a terminal in the `flyrank-ai-fluency` repository.
2. Confirm the environment has `OPENAI_API_KEY` and `OPENAI_API_BASE` set. Never show either value on-screen.
3. Open the agent README in a browser or editor for brief reference.
4. Start a screen recorder and leave it running until the end.

### Suggested 3–5 minute narration and run

| Time | Show | Say in your own words |
|---:|---|---|
| 0:00–0:35 | `agent/README.md` title and purpose | “This is my Evidence-Safe Portfolio Update Scout. I use it before I put a result statement on my ML portfolio. It reviews wording; it cannot publish anything.” |
| 0:35–1:05 | Architecture diagram and approved context path | “The agent reads only an approved public-safe context file and the current public page. It first checks local safety rules, then performs a read-only site check, then produces a structured recommendation.” |
| 1:05–2:15 | Run the verified claim command below | “Here I am giving it a statement that matches the documented Precision@50 comparison. The output should be an allow decision, but I still review it myself before publishing.” |
| 2:15–3:15 | Run the unsupported business-outcome command below | “This claim says the model increased revenue and SEO traffic. That evidence is not in my public case study, so the guardrail should block it rather than invent support.” |
| 3:15–3:50 | Open a generated local audit record | “Each run writes a transparent local record. It does not edit my site, deploy code, email anyone, or change data.” |
| 3:50–4:30 | Show evaluation results and build log | “I tested seven cases. One broad claim initially needed an iteration, so I added a deterministic guardrail. That limitation and change are documented rather than hidden.” |

Run these commands from the repository root, one at a time:

```bash
python3 ai_fluency/FL-07/agent/audit_portfolio_copy.py \
  "On seven held-out clients, the model reported Precision@50 of 0.540 versus 0.340 for the baseline."

python3 ai_fluency/FL-07/agent/audit_portfolio_copy.py \
  "The model increased client revenue and SEO traffic."
```

## Upload and handoff

After recording, upload the unedited video to YouTube as **Unlisted**, copy its URL, and save it in a new file named `ai_fluency/FL-09/demo_video_link.md` using this template:

```markdown
# Unlisted Demo Video

**YouTube URL:** <paste the unlisted YouTube link here>

**Recorded by:** Umer Sajid
**Date:** <date>
**Notes:** One unedited narrated recording showing two live agent runs, an unsupported-claim guardrail, and the documented broad-scope iteration.
```

> The video has not been fabricated or substituted. It remains a required personal recording and upload action before FL-09 can be submitted.
