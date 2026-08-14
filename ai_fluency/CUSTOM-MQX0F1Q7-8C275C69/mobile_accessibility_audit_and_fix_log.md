# Mobile Accessibility Audit and Fix Log

**Assignment:** `CUSTOM-MQX0F1Q7-8C275C69`  
**Site:** <https://flyrank-ai-fluency-public-site-umer-sajids-projects.vercel.app/>  
**Scope:** Shared static-site layout, navigation, links, and case-study presentation.

> **Integrity boundary:** The source review and local keyboard preview below are complete. They do not replace the required real-phone test. No physical-phone, touchscreen, or screen-reader test is claimed in this file.

## AI-assisted source audit

I ran a structured audit with `gpt-5-mini` over the actual `docs/index.html`, `docs/case-study.html`, and `docs/site.css`. The model catalog used for that run, the executable audit script, source-grounded raw output before and after the changes, and the deterministic contrast check are preserved in this assignment folder.

| Initial source-grounded finding | Change made | Current evidence |
|---|---|---|
| Keyboard users had no direct route past repetitive navigation. | Added a visible-on-focus **Skip to main content** link and `id="main-content"` target to every public page. | Local keyboard preview reached and revealed the skip link on the first `Tab` press. |
| Navigation links did not define an adequately sized, clearly interactive hit area. | Added inline-flex navigation links with `min-height: 2.75rem`, padding, and persistent underlines. | The navigation remains fully visible in the local preview; the shared CSS supplies the same rules across all pages. |
| Interactive elements had no dedicated focus-visible styling. | Added a dark outline for links plus a white inner outline and dark outer ring for buttons. | Local keyboard preview showed the focusable skip link with its clear focus treatment. |
| Link-list items could be awkward to tap on a small screen. | Added a `2.75rem` minimum height to evidence-list links. | Shared CSS applies the larger target on the case-study evidence list. |
| Coral metric text needed a deterministic contrast check. | Changed the large metric value to `#B64231` while retaining the identity system’s coral accent elsewhere. | `check_contrast.py` records a normal-text contrast check for the metric against white. |

## Local preview result

On August 14, 2026, I opened the local `docs/index.html` preview and verified that the revised header, underlined navigation, content hierarchy, buttons, and the new skip link rendered together. I then pressed `Tab`: focus reached the skip link and revealed it at the top-left of the page. This verifies the new keyboard pattern only in the local browser preview.

## Remaining real-phone test

Umer must open the final live URL on a real phone after deployment, take an unedited screenshot, and answer these two questions in his own words:

1. What was easy to tap, read, or understand?
2. What was confusing, cramped, slow, or visually weak?

Any issue reported by that real-device test will be recorded and fixed before this card is submitted. Browser resizing or local previews are not presented as a substitute for that evidence.

## Evidence files

| File | Purpose |
|---|---|
| `run_accessibility_audit.py` | Reproducible structured source-audit script. |
| `ai_accessibility_audit_before_fixes.json` | Raw initial audit output. |
| `ai_accessibility_audit.json` | Raw audit output after the applied improvements. |
| `check_contrast.py` and `contrast_check.json` | Deterministic color-contrast calculation. |
| `live_model_catalog.json` | Verified model catalog used to select `gpt-5-mini`. |
