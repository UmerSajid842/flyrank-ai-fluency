# Three Roads: Choose Your Stack with AI

**Assignment:** `CUSTOM-MQX06U8B-9AAA4FBA`  
**Author:** Umer Sajid  
**Decision date:** August 13, 2026

## The constraints I gave the AI

I need a portfolio that is free to publish and simple enough for me to understand and maintain myself. My current skill level is early-stage web development: I can read HTML, CSS, Markdown, repository files, and deployment steps, but I should not choose a stack that depends on a database, a server, or paid hosting just to show a case study. The site must support the sitemap I already planned: a home page, an ML case study, an about/contact area, and links to the public repository and professional profile. My work must display as readable writing with real charts and screenshots—not as a flashy application that hides the evidence.

The portfolio does not currently need logins, private data, payments, user accounts, or a database. Therefore, the honest backend decision is **no backend for the first version**. A simple contact link is enough until I have a genuine need for a form or another interactive feature.

## Three genuine options

| Road | Build method and free host | Backend need | What it would do well | Main trade-off |
|---|---|---|---|---|
| **1. Static HTML/CSS on GitHub Pages** | Hand-written HTML/CSS in this public repository; host from the repository’s `docs/` folder using GitHub Pages. | None. | Gives me a fast, public, low-maintenance portfolio with complete control over layout, images, and links. GitHub Pages can serve a project site from a repository branch/folder. [1] | I need to make page updates directly in files, and a contact form would require a later external service. |
| **2. Static-site generator on GitHub Pages** | Write content in Markdown and generate the site with a static-site framework such as Jekyll, then host on GitHub Pages. | None. | Makes it easier to add repeated case-study pages or blog posts while keeping content separate from layouts. GitHub Pages supports Jekyll as its built-in static-site generator. [2] | More moving pieces: templates, local preview, configuration, and debugging builds would slow down my two-week build. |
| **3. React app on Vercel** | Build a React/Vite front end, connect the GitHub repository, and deploy on Vercel’s free hosting. | Not for the first portfolio; optional later for interactive features. | Gives room for richer interactions and previews. Vercel can create a project linked to a Git repository for deployment. [3] | It introduces JavaScript tooling, dependency management, and more places for a simple evidence portfolio to break before the content is strong. |

## Pressure test of the preferred option

I tested Road 1 against the four questions that matter to this assignment. It passes the simplicity test because the production page is a small set of files I can open and understand. It passes the maintenance test because updating a sentence, chart, or link means editing the same public repository where I already keep the evidence; there is no server state or separate CMS to maintain. It passes the two-week feasibility test because the page can be deployed before the full visual design is complete, leaving time to improve content and gather honest proof. Finally, it passes the work-display test because real charts can be stored as project assets and shown beside concise explanations, with the detailed method retained in the linked repository.

## My decision, in my own words

I choose **static HTML/CSS in this repository, deployed with GitHub Pages**. I declined the generator option because I do not yet have enough repeated content to justify additional build configuration. I also declined the React/Vercel option because an interactive app would solve a problem I do not currently have and would make the first version harder for me to understand end to end.

This choice keeps the portfolio honest and maintainable. The page will lead with the result and link to the source work, while real charts and public-safe explanations carry the proof. I can add a backend only after I can name a real feature that needs one. For now, a responsive static site is the best match for my skills, budget, and the job the portfolio has to do.

## Implementation record

The near-blank deployment foundation is at `docs/index.html` in this repository. It uses the Week 3 identity choices: Manrope, teal `#0F766E`, near-black `#172033`, off-white `#FAFAF8`, and coral `#F9735B`. The initial page is intentionally restrained while the case-study material is checked for public safety and accuracy.

## References

[1]: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages "GitHub Docs — What is GitHub Pages?"
[2]: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll "GitHub Docs — Setting up a GitHub Pages site with Jekyll"
[3]: https://vercel.com/docs/projects/overview "Vercel Docs — Projects overview"
