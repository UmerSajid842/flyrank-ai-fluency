# Explain It Like You Built It: Why the ML Work Site Stays Readable on Different Screens

**Assignment:** `CUSTOM-MQX0CE9V-B5BB265F`  
**Build examined:** the public ML Work site in [`docs/`](../../docs/)  
**Live URL:** <https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/>

> **Integrity note:** This is an AI-assisted study draft based on the real HTML and CSS in this repository. The explanation is ready for Umer to read, verify against the files, and express in his own words. It does not claim that a personal learning conversation or independent understanding occurred without that review.

## The real part of the build I studied

I focused on the **shared page layout and responsive navigation**. This is a real part of the site, not an abstract example. Each page uses the same `site.css` file, and the CSS controls the maximum reading width, the two-column content cards, the navigation row, and the change to a one-column layout on smaller screens. The reason this was initially worth understanding is that the site needs to look intentional on a laptop without becoming cramped or difficult to read on a phone.

## Short AI tutoring trace

| Question I used to study the code | Answer grounded in this build |
|---|---|
| Why does the header and main area use `width: min(100% - 2.25rem, var(--max))` instead of one fixed width? | `100% - 2.25rem` keeps a gap at the left and right edges on narrow screens. `var(--max)` caps the content at 70rem on wide screens, so lines do not become uncomfortably long. The browser chooses the smaller of those two values. |
| Why is `.grid.two` defined as two columns and later changed to one? | On larger screens, `repeat(2, minmax(0, 1fr))` creates two equal flexible columns for a text block and evidence card. At `max-width: 43rem`, the media query changes it to `1fr`, stacking the same content vertically so neither column becomes too narrow. |
| Why does the navigation wrap and then become a vertical header on small screens? | `flex-wrap: wrap` lets the links occupy more than one line instead of overflowing. The small-screen media query changes `.site-header` to a column, which gives the brand and navigation their own rows. |
| What happens after a change is pushed? | The static files in `docs/` are committed to the GitHub repository. The linked Vercel project builds and serves the updated HTML, CSS, and public chart images over HTTPS. No database or server process is needed for these pages. |

## Plain-language explanation for a friend

A webpage is not one rigid picture. It is more like a set of rules that the browser applies to whatever screen it gets. On my ML Work site, I first give the content a comfortable maximum width so it does not stretch across a large monitor. I also subtract a little space from both sides so the text does not touch the edge of a small phone screen.

For the featured-work area, I use two equal columns when there is room. That lets the explanation sit beside the evaluation result. When the screen becomes narrow, a CSS media query changes the rule from two columns to one column. The content does not disappear or get rewritten; it simply stacks vertically. The same idea is used for the header: the links can wrap, and on a smaller screen the brand and navigation move into separate rows.

That is why the site is easier to read across screen sizes without needing a separate mobile website. The HTML keeps the content and links in one place. The shared CSS decides how that content is arranged. When I update the files in the repository, the static host publishes the new version, so the same layout rules are used by people visiting the live URL.

## My understanding check before I submit

I should be able to answer these questions without rereading the draft:

1. What does `min(100% - 2.25rem, var(--max))` protect against on small and large screens?
2. Why is stacking the two-column grid preferable to shrinking both columns indefinitely?
3. Which CSS rule changes the layout below 43rem, and what visible change should a visitor notice?
4. Why can this portfolio be hosted as static files without a backend?

## Evidence in the repository

| Build evidence | What it shows |
|---|---|
| [`docs/site.css`](../../docs/site.css) | The shared width rule, flexible navigation, two-column grid, and the `43rem` media query. |
| [`docs/index.html`](../../docs/index.html) | The header/navigation structure and the Home page’s two-column featured-work section. |
| [`docs/case-study.html`](../../docs/case-study.html) | A second real page that reuses the same stylesheet and public evidence structure. |
| [Live ML Work site](https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/) | The deployed site to inspect after reading the explanation. |
