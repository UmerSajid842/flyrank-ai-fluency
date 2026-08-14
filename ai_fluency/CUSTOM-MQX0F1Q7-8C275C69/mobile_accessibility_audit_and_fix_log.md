# Mobile Accessibility Audit and Fix Log

**Assignment:** `CUSTOM-MQX0F1Q7-8C275C69`  
**Site:** <https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/>  
**Scope:** Shared static-site layout, navigation, links, and case-study presentation.

> **Integrity boundary:** The source review, local keyboard preview, and physical-phone evidence are recorded separately below. The phone screenshots substantiate the visible captured views; they do not claim screen-reader testing or every possible interaction.

## AI-assisted source audit

I ran a structured audit with `gpt-5-mini` over the actual `docs/index.html`, `docs/case-study.html`, and `docs/site.css`. The model catalog used for that run, the executable audit script, source-grounded raw output before and after the changes, and the deterministic contrast check are preserved in this assignment folder.

| Initial source-grounded finding | Change made | Current evidence |
|---|---|---|
| Keyboard users had no direct route past repetitive navigation. | Added a visible-on-focus **Skip to main content** link and `id="main-content"` target to every public page. | Local keyboard preview reached and revealed the skip link on the first `Tab` press. |
| Navigation links did not define an adequately sized, clearly interactive hit area. | Added inline-flex navigation links with `min-height: 2.75rem`, padding, and persistent underlines. | The navigation remains fully visible in the local preview; the shared CSS supplies the same rules across all pages. |
| Interactive elements had no dedicated focus-visible styling. | Added a dark outline for links plus a white inner outline and dark outer ring for buttons. | Local keyboard preview showed the focusable skip link with its clear focus treatment. |
| Link-list items could be awkward to tap on a small screen. | Added a `2.75rem` minimum height to evidence-list links. | Shared CSS applies the larger target on the case-study evidence list. |
| Coral metric text needed a deterministic contrast check. | Changed the large metric value to `#B64231` while retaining the identity system’s coral accent elsewhere. | `check_contrast.py` records a normal-text contrast check for the metric against white. |

## Local keyboard-preview result

On August 14, 2026, I opened the local `docs/index.html` preview and verified that the revised header, underlined navigation, content hierarchy, buttons, and the new skip link rendered together. I then pressed `Tab`: focus reached the skip link and revealed it at the top-left of the page. This verifies the keyboard pattern only in the local browser preview.

## Real-phone test and feedback

On August 14, 2026, Umer provided three unedited 720 × 1600 pixel portrait screenshots from an Android phone while viewing the deployed public site. The screenshots show the mobile header, five navigation destinations, landing-page call-to-action buttons, featured-work content, the method cards, and the ML Work / AI Work distinction. The detailed, bounded observation is in `phone_evidence_observation.md`.

> “The site was easy to use on my phone, and the main sections were readable and accessible without any major issues.” — Umer Sajid
>
> “The site was generally easy to use on my phone, although some elements felt slightly cramped on the smaller screen.” — Umer Sajid

The second observation is a genuine mobile usability finding. I treated the header navigation and adjacent calls to action as the high-frequency controls most likely to feel cramped and made the following small-screen fix in `docs/site.css` for widths at or below `34rem` (544 px).

| User-reported issue | Change made | Intended effect | Verification status |
|---|---|---|---|
| Some elements felt slightly cramped on the smaller phone screen. | Increased the narrow-screen usable width from `100% - 2.25rem` to `100% - 1.5rem` for the header, main content, and footer. | Gives text and controls 0.75rem more total horizontal room without touching the desktop layout. | Verified on the published site at a 390-pixel-wide render. |
| The five-link navigation could feel dense in a single wrapping row. | Changed navigation at `≤ 34rem` to a full-width, two-column grid with a `0.65rem` gap, visible control boundaries, and `3.1rem` minimum link height. | Separates choices visually and improves touch comfort while retaining every navigation destination. | Verified on the published site: all five links appear as spaced two-column controls without horizontal clipping. |
| The two hero actions could feel crowded beside each other. | Stacked hero actions into a single column with a `0.9rem` gap; each action is full width and at least `3.25rem` high. | Makes each call to action easier to target and read on a narrow screen. | Verified on the published site: both actions are full-width, separated, and visible. |

## Published-site verification

After commit `c9565c6` was pushed to `main`, I confirmed that the public site served the new `@media (max-width: 34rem)` stylesheet rules. I rendered the live URL at a 390 × 844 pixel viewport. The header brand, all five navigation links, heading, body copy, and both hero actions were visible without horizontal clipping. The navigation rendered as five spacious two-column controls, and the hero actions rendered as separately spaced full-width controls. The desktop page retained its flex navigation and side-by-side actions.

## Evidence files

| File | Purpose |
|---|---|
| `phone_screenshots/phone-home.jpeg` | User-provided Android capture of the deployed mobile landing page. |
| `phone_screenshots/phone-featured-work.jpeg` | User-provided Android capture of the deployed featured-work section. |
| `phone_screenshots/phone-method-and-ai-work.jpeg` | User-provided Android capture of the deployed method and AI Work section. |
| `phone_evidence_observation.md` | Bounded observations from the three real-phone screenshots. |
| `post_fix_live_render_390.png` | Post-fix desktop-browser render of the published page at a 390 × 844 pixel viewport; supporting layout verification, not presented as a physical-phone screenshot. |
| `run_accessibility_audit.py` | Reproducible structured source-audit script. |
| `ai_accessibility_audit_before_fixes.json` | Raw initial audit output. |
| `ai_accessibility_audit.json` | Raw audit output after the first applied improvements. |
| `check_contrast.py` and `contrast_check.json` | Deterministic color-contrast calculation. |
| `live_model_catalog.json` | Verified model catalog used to select `gpt-5-mini`. |
