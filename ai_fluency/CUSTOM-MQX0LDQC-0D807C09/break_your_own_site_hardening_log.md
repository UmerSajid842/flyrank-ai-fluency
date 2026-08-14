# Week 9 — Break Your Own Site: Hardening Log

**Public site:** <https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/>
**Test date:** 2026-08-14
**Scope:** The public ML Work portfolio and its optional live GitHub repository-record check.

## Testing approach

This portfolio is a static, read-only site. It has **no visitor form, account creation, data submission, or server-side mutation endpoint**. Accordingly, an empty or malformed visitor-form test is not applicable. The closest interactive surface is the optional “Check the live repository record” button on the case-study page. The review therefore tested link resolution, public response status, interaction boundaries, mobile presentation, metadata, findability, and a speed-check route.

| Test area | Test performed | Baseline result | Classification |
|---|---|---|---|
| Public-page availability | Requested the home page, five site pages, the public paper, and the two public repositories | All nine URLs returned HTTP 200 | Pass / no fix needed |
| Internal and evidence links | Reviewed the site navigation and public-paper/repository destinations | No broken link was identified in the checked set | Pass / no fix needed |
| Repository-check interaction | Reviewed the button code and its error path | The control disables itself during an in-progress request, preventing rapid repeat requests; error text tells visitors to use the direct repository link and retry later | Pass / known external dependency boundary |
| Empty or malformed submission | Checked the deployed portfolio for a visitor form or other data-submission endpoint | Not applicable: the site exposes no visitor-input form or mutation endpoint | Known limitation, intentionally out of scope |
| SEO and social preview | Inspected all six public HTML pages | Each page had a title and description, but canonical URLs, Open Graph metadata, and Twitter preview metadata were missing | **Fix now** |
| Findability | Searched public results for Umer’s name plus the ML Work/case-study wording | The specific public portfolio was not returned in the observed search results | Known limitation: new static deployments need search-engine discovery time; metadata and canonical URLs are being added to improve indexability |
| Speed-check provider | Requested the Google PageSpeed Insights API and web interface, then tried WebPageTest | The unauthenticated API returned a quota error; the web interface returned no usable score; WebPageTest presented a CAPTCHA | Known limitation: third-party provider availability prevented a score at this test time; a transparent response-timing check will be recorded separately |

## Fix-now work completed locally

The following metadata hardening was added locally to `index.html`, `case-study.html`, `ai-work.html`, `about.html`, `contact.html`, and `notes.html`:

- A canonical public URL for each page.
- Open Graph type, title, description, and URL metadata.
- Twitter card, title, and description metadata.

## Local verification before publication

| Check | Result |
|---|---|
| Static metadata and internal-link validator | Passed for all six portfolio pages: all required title/description, canonical, Open Graph, and Twitter metadata values were present; no relative internal link target was missing. |
| Public response timing (three sequential home-page samples) | HTTP 200 each time. Total transfer times were 0.057535 s, 0.061422 s, and 0.055240 s; these are environment-dependent response timings, not Lighthouse or field-performance scores. |
| Live rapid-repeat repository check | On the deployed case-study page, two immediate programmatic activations were attempted. The button was disabled immediately after the first activation; the second activation did not create a concurrent request. The first request returned the success state, then the button reset. |
| Live repository-check result | The deployed control reported that `UmerSajid842/flyrankmlproject` is public, its default branch is `main`, and GitHub returned a current update timestamp. |

## Post-publication check

The metadata hardening was published in commit `c4e6786`. On the live homepage, the canonical URL, Open Graph type/title/description/URL, and Twitter card/title/description were all present and matched the published page. The deployed homepage also remained reachable and readable after the update.



## Known limitations retained intentionally

| Limitation | Reason it remains | Visitor-facing boundary |
|---|---|---|
| The repository-record button depends on GitHub’s public API | GitHub availability and rate limiting are outside this static site’s control | The page displays a plain-language fallback and retains a direct repository link |
| No visitor form exists | The portfolio is intentionally read-only and does not collect visitor data | There is no empty-input or malformed-input path to submit |
| Search indexing is not immediate | Search-engine crawl timing cannot be forced by a static-site owner | Canonical and social metadata improve the public indexability signals, without claiming an indexed result exists |
| Third-party PageSpeed scoring was unavailable during this audit | Public-provider quota/CAPTCHA controls were encountered | The report will label any local response timing separately and will not claim a Lighthouse/PageSpeed score |

## Hardening-review request

A mentor or structured peer review is still required by the assignment. The reviewer should receive this log and be asked whether any listed fix-now or known-limitation item is inaccurate, incomplete, or needs a further user-facing change. Any genuine must-fix response will be recorded and addressed before submission.
