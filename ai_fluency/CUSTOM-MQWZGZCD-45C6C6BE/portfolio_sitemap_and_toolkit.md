# Draw the Path: Portfolio Sitemap + Toolkit

## Purpose

This sitemap is designed for one person and one action. The target reader is an **entry-level machine-learning hiring manager at an SEO or content-intelligence company**. The claim is: **I build leakage-aware machine-learning prototypes for content-prioritisation problems.** The single primary action is: **Open the capstone case study.**

## Small portfolio sitemap

```text
Home
└── Primary CTA: Open the capstone case study
    └── Capstone Case Study
        ├── Editorial problem
        ├── Data and public-safety boundary
        ├── Leakage risks and client-grouped validation
        ├── Model and transparent baseline
        ├── Measured results
        ├── How the output becomes editorial review priorities
        ├── Limitations and failure modes
        └── Reproducibility

About
└── Short background, the verified tools used, and a link back to the capstone

Contact
└── Email and GitHub; secondary only after the reader has seen the case study
```

## Why each page earns its place

| Page | Reader question it answers | Decision |
|---|---|---|
| **Home** | What does this candidate claim, and where is the proof? | Keeps a concise claim and one CTA. It does not compete with multiple “learn more” actions. |
| **Capstone Case Study** | Can this candidate frame an ML problem, avoid leakage, evaluate honestly, and connect the output to a real decision? | Carries the proof. Its internal sections make the claim inspectable rather than branded. |
| **About** | Who made the work and what is the relevant technical context? | Remains short and subordinate to the case study. It does not become a second portfolio. |
| **Contact** | How can an interested reviewer continue the conversation? | Appears after the evidence. GitHub is available for reproducibility review. |

The sitemap intentionally excludes a generic projects grid, blog, certificates page, separate skills page, testimonial page, and multiple unrelated case studies. None of those pages would make the one proof path clearer at this stage.

## Evidence inside the case-study path

The capstone uses only a public-safe anonymised starter release and evaluates a leakage-aware random-forest model against a transparent baseline on seven held-out pseudonymised clients. The measured Precision@50 values are 0.540 for the model and 0.340 for the baseline. The paper explicitly states that this supports ranking pages for editorial review rather than automated refresh decisions or traffic-recovery claims. [1]

## Toolkit and project instructions

| Tool | Intended use in this portfolio build | Boundary |
|---|---|---|
| **Claude Project** | Tutor-style questioning, case-study editing, and checking each page against the claim/action. | Do not paste raw data, client identifiers, credentials, private URLs, or unredacted screenshots. |
| **ChatGPT** | Pressure-testing the sitemap, generating alternatives to critique, and reviewing clarity. | Treat outputs as drafts; verify factual statements against the capstone report. |
| **Gemini** | Optional second opinion on information hierarchy and reader comprehension. | Do not use it to invent evidence or results. |
| **Perplexity** | Optional source lookup when an external claim needs citation. | Cite the primary source; do not rely on a search summary alone. |

### Claude Project instructions to add

> You are a tutor and critical editor for Umer Sajid’s public-safe Machine Learning portfolio. Keep the work aimed at one audience: an entry-level ML hiring manager at an SEO or content-intelligence company. Preserve one primary action: open the capstone case study. Ask one question at a time before proposing major changes. Use a direct, plain, evidence-first voice. Never invent results, employers, credentials, tools, or data. Treat raw datasets, client identifiers, URLs, credentials, private queries, and personal information as private. Check technical claims against the capstone report, label assumptions, and point out where evidence is insufficient. The proof statement is: “I build leakage-aware machine-learning prototypes for content-prioritisation problems.”

## Real pressure test and revision

### Prompt used

> Act as a portfolio reviewer for a junior machine-learning candidate applying to an SEO or content-intelligence company. Review this deliberately small portfolio sitemap against one claim and one CTA. Claim: I build leakage-aware machine-learning prototypes that turn anonymized content signals into honest editorial review priorities. Audience: a hiring manager for an entry-level ML role at an SEO or content-intelligence company. CTA: Open the capstone case study. Sitemap: Home (claim + CTA); Capstone Case Study (problem, method, results, limitations, reproducibility); About (short background and tools); Contact (email + GitHub). Answer in a table with: what works, any page that does not earn its place, any missing proof, and one specific revision. Do not invent experience or results.

### Saved output summary

A real ChatGPT guest-session review found that the four-page structure was appropriately small and the CTA was clear. It said the case study strongly supported the leakage-aware part of the claim, but did not yet visibly support the “editorial review priorities” part. The review recommended making the decision chain explicit: content signals → model/ranking → editorial review priority → caveats. It also advised retaining limitations and reproducibility while keeping About subordinate to the case study.

### Documented revision

**Before:** The Capstone Case Study branch listed only “problem, method, results, limitations, reproducibility.”

**After:** The case-study branch now explicitly contains “How the output becomes editorial review priorities,” placed after measured results and before limitations. It will explain that the model produces a review-for-refresh ranking, not an automated content change; an editor must diagnose the page before selecting refresh, expansion, monitoring, or deferral. This revision makes the second half of the claim testable and connects the model to the real FlyRank content decision.

### Evidence status

The portfolio sitemap and the actual ChatGPT pressure-test prompt/output record are present in this document. A redacted screenshot of the previously created Claude Project exists in `ai_fluency/FL-01/evidence/`. The browser sessions available during this task were not authenticated to Claude, Gemini, or Perplexity, so this document does **not** claim fresh runs or account setup for those tools. The user should paste the standing instructions above into the existing Claude Project and capture an expanded Instructions-panel screenshot before presenting this assignment as fully evidenced.

## References

[1] [Umer Sajid, *Capstone Report: Refresh / Content Opportunity Scoring*](https://github.com/UmerSajid842/flyrankmlproject/blob/main/work/capstone_report.md)
