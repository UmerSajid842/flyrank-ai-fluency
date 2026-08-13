# Workflow Run: stack_decision

| Field | Value |
|---|---|
| Source | `/home/ubuntu/flyrank-ai-fluency/ai_fluency/CUSTOM-MQX06U8B-9AAA4FBA/three_roads_stack_decision.md` |
| Run time (UTC) | 2026-08-13T18:00:41.109656+00:00 |
| Model | `gpt-5-mini` |
| Measured workflow time | 70.13 seconds |
| Publication status | **Not published — human review required** |

## Step 1 — Source packet

**Purpose:** Record and justify a technology-stack decision for a personal portfolio site, comparing three options and selecting a simple, publishable approach.

## Step 2 — Structured evidence extraction

### Verified facts

- Assignment: CUSTOM-MQX06U8B-9AAA4FBA
- Author: Umer Sajid
- Decision date: August 13, 2026
- Primary constraint: portfolio must be free to publish and simple enough for the author to understand and maintain; author is an early-stage web developer who can read HTML, CSS, Markdown, repository files, and deployment steps, and wants to avoid stacks that require a database, a server, or paid hosting for the first version
- Required sitemap: a home page, an ML case study, an about/contact area, and links to the public repository and professional profile
- Backend decision for first version: no backend; a simple contact link is sufficient
- Three options considered: Road 1 — Static HTML/CSS on GitHub Pages (host from the repository's docs/ folder), Road 2 — Static-site generator (Jekyll) on GitHub Pages, Road 3 — React app on Vercel
- Reasoning summary for Road 1: simplicity, maintainability (editing files in the same public repository), two-week feasibility (can deploy before full visual design is complete), and suitability for displaying real charts and screenshots as public assets
- Chosen option: static HTML/CSS in this repository, deployed with GitHub Pages (Road 1)
- Reasons for declining Road 2: not enough repeated content to justify extra build configuration; it would add templates, local preview, and configuration overhead
- Reasons for declining Road 3: would introduce JavaScript tooling, dependency management, and more failure points for a first-version evidence portfolio
- Implementation record: a near-blank deployment foundation is at docs/index.html in this repository
- Design identity used on the initial page: Manrope font; colors teal #0F766E, near-black #172033, off-white #FAFAF8, coral #F9735B
- The initial page is intentionally restrained while case-study material is checked for public safety and accuracy
- References included in the source: GitHub Pages overview, GitHub Pages + Jekyll setup, and Vercel Projects overview (three cited URLs)

### Limits or unknowns

- The source does not provide the repository URL or the repository name
- The source does not confirm that GitHub Pages publishing is enabled or that the site is already live from docs/
- No full site content, case-study files, charts, or screenshots are included in this document beyond the note that a near-blank docs/index.html exists
- No deployment logs, build outputs, or live-site verification are provided in this source
- No editor/workflow details or exact update steps are provided (beyond the general statement that updates require editing repository files)
- No detailed plan or timeline for adding a backend in the future is provided—only the statement that a backend can be added later when needed

### Publishable artifacts

- This decision document: three_roads_stack_decision.md
- Near-blank deployment foundation file mentioned: docs/index.html (in the repository)
- Design identity notes included in the source: font Manrope and color palette (teal #0F766E, near-black #172033, off-white #FAFAF8, coral #F9735B)
- Planned sitemap description: home page, ML case study, about/contact, links to public repository and professional profile
- Rationale and comparison table of the three considered options (Road 1, Road 2, Road 3) and the pressure-test analysis for the chosen option

## Step 3 — Draft for human review

> Draft note for review (Assignment CUSTOM-MQX06U8B-9AAA4FBA). Author Umer Sajid. Decision date: August 13, 2026. Primary constraint: free, simple, avoid DB/server/paid hosting for first version. Compared three roads: Road 1 — static HTML/CSS on GitHub Pages (chosen); Road 2 — Jekyll on GitHub Pages (declined: extra build/config overhead); Road 3 — React on Vercel (declined: JS tooling and dependency risk). Implementation: near-blank docs/index.html exists; design: Manrope, colors teal #0F766E, #172033, #FAFAF8, #F9735B. Limitation: repository URL and live-publishing status are not provided; full site content is not included.

## Step 4 — Claim audit

| Audit status | Required human check |
|---|---|
| `revise_before_review` | Please verify the missing operational details before approving: (1) supply the repository name/URL and confirm the path to docs/index.html; (2) confirm whether GitHub Pages publishing is enabled for that repository and whether the site is currently live; (3) inspect docs/index.html to confirm it matches the described 'near-blank deployment foundation'; (4) confirm which contact mechanism will be used (mailto link, external form, etc.) since no backend is planned; (5) verify that the listed design tokens (Manrope font and the four color hex values) are applied as intended; and (6) if a timeline or plan for adding a backend later is required, provide that detail. Any claims about live publishing, repository access, or complete site content need explicit evidence (URLs, screenshots, or logs) before this decision record is considered fully validated. |

### Supported claims

- Assignment: CUSTOM-MQX06U8B-9AAA4FBA
- Author: Umer Sajid
- Decision date: August 13, 2026
- Primary constraint: portfolio must be free to publish and simple enough for the author to understand and maintain; author is an early-stage web developer who can read HTML, CSS, Markdown, repository files, and deployment steps, and wants to avoid stacks that require a database, a server, or paid hosting for the first version
- Required sitemap: a home page, an ML case study, an about/contact area, and links to the public repository and professional profile
- Backend decision for first version: no backend; a simple contact link is sufficient
- Three options considered: Road 1 — Static HTML/CSS on GitHub Pages (host from the repository's docs/ folder), Road 2 — Static-site generator (Jekyll) on GitHub Pages, Road 3 — React app on Vercel
- Chosen option: static HTML/CSS in this repository, deployed with GitHub Pages (Road 1)
- Reasoning summary for Road 1: simplicity, maintainability (editing files in the same public repository), two-week feasibility (can deploy before full visual design is complete), and suitability for displaying real charts and screenshots as public assets
- Reasons for declining Road 2: not enough repeated content to justify extra build configuration; it would add templates, local preview, and configuration overhead
- Reasons for declining Road 3: would introduce JavaScript tooling, dependency management, and more failure points for a first-version evidence portfolio
- Implementation record: a near-blank deployment foundation is at docs/index.html in this repository
- Design identity used on the initial page: Manrope font; colors teal #0F766E, near-black #172033, off-white #FAFAF8, coral #F9735B
- The initial page is intentionally restrained while case-study material is checked for public safety and accuracy
- References included in the source: GitHub Pages overview, GitHub Pages + Jekyll setup, and Vercel Projects overview (three cited URLs)
- Publishable artifacts listed: three_roads_stack_decision.md, docs/index.html, design identity notes, planned sitemap description, and a rationale/comparison table

### Risks or missing support

- The repository URL or repository name is not provided in the source
- The source does not confirm that GitHub Pages publishing is enabled or that the site is already live from docs/
- No full site content, case-study files, charts, or screenshots are included in the document beyond the note that a near-blank docs/index.html exists
- No deployment logs, build outputs, or live-site verification are provided
- No editor/workflow details or exact update steps are provided (beyond the general statement that updates require editing repository files)
- No detailed plan or timeline for adding a backend in the future is provided

## Step 5 — Required human handoff

The workflow stops here. A human must compare each draft sentence with the original source, confirm the document is public-safe, verify no planned work is described as complete, and decide whether to publish, revise, or discard the draft.

## Timing record

This measured time covers the automated source-to-audit run only. It does **not** claim that human review can be removed or that the automation replaces manual source reading. Token counts are retained in the corresponding JSON record for reproducibility.
