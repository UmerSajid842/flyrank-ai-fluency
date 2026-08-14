# Design Your Personal Agent — Evidence-Safe Portfolio Update Scout

**Assignment:** `FL-06`  
**Author:** Umer Sajid  
**Design date:** August 14, 2026  
**Status:** Build specification for the narrowest useful MVP

## 1. The job

The **Evidence-Safe Portfolio Update Scout** reviews a proposed sentence or short section before it is added to Umer Sajid’s public ML Work site. Its job is not to write a whole portfolio, promise business outcomes, or publish anything. It compares the proposed wording with a small, approved public knowledge base; flags unsupported claims; chooses one safe next action; and produces a concise review report.

The personal problem is recurring: after building an ML project, it is easy to turn a real evaluation result into an overconfident public claim. The agent reduces that risk by checking every candidate update against the verified case-study boundary before a human edits the live site. Umer would use it whenever he drafts a home-page result, case-study sentence, note, application summary, or social-post line—roughly once or twice each week while maintaining the portfolio.

> **Success means:** the agent identifies whether a proposed sentence is supported, needs safer wording, must be blocked, or needs more source evidence; Umer still makes the final publish decision.

## 2. Scope and user flow

| Step | Agent action | Output | Human responsibility |
|---|---|---|---|
| 1. Receive candidate wording | Accept one sentence or a short paragraph from the command line. | Input text. | Do not submit private data or client details. |
| 2. Read approved context | Read the public-safe case-study context and site copy from specified local files. | Evidence packet. | Keep the knowledge files accurate and public-safe. |
| 3. Check the live destination | Request the public ML Work URL and record only its reachability status. | URL status. | Interpret a failed check before retrying or changing hosting. |
| 4. Decide the next action | Choose `ALLOW`, `REVISE`, `BLOCK`, or `NEED_EVIDENCE` using a structured response. | Audit result and reason. | Review every output; no automated edit occurs. |
| 5. Provide a safe draft when appropriate | Offer at most one revised sentence that keeps the verified meaning and limitations. | Suggested wording or a request for evidence. | Confirm accuracy before copying it anywhere. |

The behavior is agent-like rather than a fixed prompt chain because the tool selects the appropriate stop/action after inspecting both the supplied wording and evidence packet. For example, it can ask for source proof instead of revising, or block wording that exposes a client even if the surrounding sentence is otherwise well written. The action set is deliberately small.

## 3. Tools, data, and realistic access plan

| Resource | Why it is needed | Access plan | Boundary |
|---|---|---|---|
| `portfolio_case_study_context.md` | Holds the approved claim, verified Precision@50 comparison, and forbidden claim types. | Bundled local, public-safe knowledge file in the repository. | Read-only. Never includes datasets, client names, credentials, or raw queries. |
| Public `docs/` source files | Lets the agent see the portfolio framing that is currently intended for publishing. | Read-only local files in the public repository. | Read-only; the agent cannot modify them. |
| Public Vercel URL | Checks whether a referenced page is reachable. | One GET request to the known public URL. | Status-only; no login, account data, deployment control, or web posting. |
| `gpt-5-mini` | Produces the constrained structured classification and short revision when allowed. | OpenAI-compatible client through the configured sandbox environment; the model ID was verified against the live catalog. | No browsing, no tool authority, no autonomous publication, and no hidden source expansion. |

The MVP has **no write credential** for GitHub, Vercel, email, calendars, or social platforms. That is intentional. A suggested sentence is not a site change, and a positive audit is not permission to publish.

## 4. Draft operating instructions

> You are the Evidence-Safe Portfolio Update Scout. Review only the candidate wording and the approved public evidence packet. Return one action: `ALLOW`, `REVISE`, `BLOCK`, or `NEED_EVIDENCE`. Use `BLOCK` for client-identifying details, credentials, private data, or claims of production, SEO, revenue, traffic, causal business impact, or deployment that are not in the packet. Use `NEED_EVIDENCE` when a claim may be true but is not supported by the packet. Use `REVISE` when the core point is supportable but wording is too broad. Use `ALLOW` only when the claim is directly supported. Never fabricate a metric, source, company, role, or outcome. Provide one concise reason and, only for `REVISE`, one public-safe replacement. Never instruct the user to publish automatically.

## 5. Pre-build evaluation cases

| Case | Candidate wording | Expected action | Why it matters |
|---|---|---|---|
| 1. Verified result | “On seven held-out clients, the model reported Precision@50 of 0.540 versus 0.340 for the baseline.” | `ALLOW` | Directly matches the approved evidence. |
| 2. Overstated impact | “The model increased client revenue and SEO traffic.” | `BLOCK` | The public evidence has no causal business-outcome result. |
| 3. Production claim | “This production system automatically chooses content for every client.” | `BLOCK` | The work is an evaluation prototype, not production. |
| 4. Supportable but too broad | “My AI system transforms every content workflow.” | `REVISE` | The scope should be narrowed to the inspected prototype and ranking decision. |
| 5. Unsupported new metric | “The model achieved 92% accuracy.” | `NEED_EVIDENCE` | The metric does not appear in the approved packet. |
| 6. Privacy violation | “Client Acme’s content was the worst performer.” | `BLOCK` | Client-identifying language is disallowed. |
| 7. Reachability interruption | A valid sentence when the public URL does not respond. | `NEED_EVIDENCE` with a site-check note | Avoid linking or announcing a page that could not be checked. |

The MVP must pass the first six text cases and must report the live URL’s status without making any change to the site.

## 6. Risks and guardrails

| Risk | Guardrail |
|---|---|
| Hallucinated business or client claim | The model receives only the approved packet and must choose `NEED_EVIDENCE` when unsure. |
| Private data entering the agent | The input is rejected when it contains obvious credentials or client identifiers; user instructions prohibit private source files. |
| Unsafe automatic publishing | There is no GitHub/Vercel write tool and no post, email, or deployment action. |
| Model mistakes | The output is advisory only; every result ends with a human-review reminder. |
| Over-reliance on a URL check | The tool reports reachability status only; a human still checks copy, layout, and accessibility. |
| Prompt injection in candidate text | Candidate wording is treated as text to audit, never as instructions that can alter the system policy. |

## 7. Platform choice and alternative considered

I choose a **small Python command-line application** in the existing public AI Work repository. It is the most maintainable first version because it keeps the knowledge base visible as Markdown, runs with one command, stores a transparent JSON audit record, and has no server or database to protect. It can demonstrate one real data connection: the local public knowledge base, plus a read-only request to the live public URL.

I declined a Claude Project agent because I do not currently have an available Claude account session and it would make the assignment depend on a private account setup I cannot yet maintain. I also declined a hosted chat application because adding authentication, backend secrets, and deployment permissions would exceed the narrow auditing job and create unnecessary risk. A web interface can be added later only after the CLI has proven useful.

## 8. Definition of done for the MVP

The MVP is done when it can accept a new candidate sentence, read the approved knowledge file, check the public ML Work URL, return a structured decision plus a reason, store the audit output, and demonstrate the evaluation cases without changing any public content. The build log must retain failures, changes, and scope cuts. A raw unedited run capture remains a personal recording task for Umer and will not be fabricated.
