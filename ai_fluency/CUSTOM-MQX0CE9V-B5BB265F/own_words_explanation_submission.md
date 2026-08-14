# Explain It Like You Built It — Own-Words Submission

**Assignment:** `CUSTOM-MQX0CE9V-B5BB265F`
**Build examined:** [ML Work portfolio](https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/)
**Real implementation:** [`docs/site.css`](../../docs/site.css)

## Umer’s own-words explanation

> I use a maximum width so the content stays comfortable to read on large screens instead of becoming too wide. On smaller screens like phones, the two-column layout changes to one column so the content does not become cramped. The site can be hosted as static files because it only needs HTML, CSS, and images, with no database or backend server required.

The quoted explanation above was supplied by Umer in the task chat on 2026-08-14. It is preserved verbatim; it has not been rewritten or expanded as a claimed personal explanation.

## Verification against the real build

| Point Umer explained | Verified implementation |
|---|---|
| A maximum width keeps wide-screen reading comfortable. | The shared header, main content, and footer use `width: min(100% - 2.25rem, var(--max))`; `--max` is `70rem` in [`docs/site.css`](../../docs/site.css). |
| The two-column layout becomes one column on narrow phones. | `.grid.two` is two equal columns by default; the `@media (max-width: 43rem)` rule changes it to `grid-template-columns: 1fr`. |
| Static hosting does not require a database or backend. | The deployed portfolio is built from public HTML, CSS, JavaScript, and image assets in [`docs/`](../../docs/). It does not contain a database-backed form or server-side application feature. |

## Evidence links

- [Live ML Work portfolio](https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/)
- [Shared responsive stylesheet](https://github.com/UmerSajid842/flyrank-ai-fluency/blob/main/docs/site.css)
- [Week 6 study worksheet](explain_it_like_you_built_it.md)

## References

[1] [Live ML Work portfolio](https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/)

[2] [Repository: shared responsive stylesheet](https://github.com/UmerSajid842/flyrank-ai-fluency/blob/main/docs/site.css)
