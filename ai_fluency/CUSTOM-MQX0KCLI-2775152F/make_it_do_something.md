# Make It Do Something — Live Public Repository Check

**Live page:** <https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/case-study.html>  
**Feature location:** the **“Check the live repository record”** card in the case-study page.  
**Source:** [`docs/evidence-status.js`](../../docs/evidence-status.js) and [`docs/case-study.html`](../../docs/case-study.html)

## The one feature

The portfolio already links to the ML project repository. The useful addition is a small **evidence-freshness check**: when a visitor clicks one button, the case-study page retrieves the current public record for the source repository and displays its visibility, default branch, and GitHub-reported update time.

This makes the evidence trail easier to inspect without inventing a business-impact dashboard or asking visitors to give contact details. It is deliberately narrow: it verifies the public repository record, not model quality, production use, SEO impact, traffic, revenue, or causality.

## What happens, in plain words

1. A visitor opens the public HTTPS case-study page and selects **Check the live repository record**.
2. The page sends a read-only request to GitHub’s public repository endpoint for `UmerSajid842/flyrankmlproject`.
3. GitHub returns the repository’s public metadata in the visitor’s browser.
4. The page formats three useful fields—whether the repository is public, its default branch, and its reported last-updated timestamp—and shows them in an on-page status message.
5. If GitHub is temporarily unavailable, the page shows a clear fallback message and keeps the direct repository link available.

> **Data path:** Visitor’s browser → GitHub public API → Visitor’s browser → visible status message. No form data, credentials, analytics, dataset, client information, or repository write is involved.

## Backend and free-tier choice

There is no private backend because this feature only needs data that GitHub already exposes publicly. The site is static HTML, CSS, and JavaScript on a free HTTPS Vercel deployment; the browser calls GitHub’s free public API directly. This reduces maintenance and means no API key or secret is embedded in the site.

The browser request uses `GET` only. It does not create issues, commit code, alter settings, or trigger an external workflow. Visitors can always use the nearby repository link if the API request fails.

## Real end-to-end test

On August 14, 2026, the feature was tested on the deployed HTTPS page. The button returned a visible success message reporting that the repository was public, that its default branch was `main`, and GitHub’s reported update time. The button then returned to its ready state. The browser screenshot in [`evidence/public_feature_success.webp`](evidence/public_feature_success.webp) shows the result, and [`feature_test_log.md`](feature_test_log.md) records the local and public test sequence.

## Limits and future improvements

This is an evidence-navigation feature, not a project monitor. GitHub may rate-limit anonymous requests or be unavailable, and the displayed time is GitHub’s repository metadata rather than a promise that every linked report changed at that time. A future version could retrieve a specific release or commit hash, but it should preserve the same public-only, read-only scope.
