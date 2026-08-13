# Workflow Run: image_curation

| Field | Value |
|---|---|
| Source | `/home/ubuntu/flyrank-ai-fluency/ai_fluency/CUSTOM-MQX033TI-DE712A19/image_curation.md` |
| Run time (UTC) | 2026-08-13T17:58:32.455336+00:00 |
| Model | `gpt-5-mini` |
| Measured workflow time | 59.75 seconds |
| Publication status | **Not published — human review required** |

## Step 1 — Source packet

**Purpose:** Guidance for selecting and publishing images for the Umer Sajid portfolio, prioritizing real work captures over generated imagery and specifying exact files and presentation rules.

## Step 2 — Structured evidence extraction

### Verified facts

- Curation principle: 'Show the actual work first.' Generated visuals may provide a small connective cue, but they never stand in for the model, the data process, or the result.
- Home hero: use a compact U monogram and a short evidence-first claim; decision: AI-generated connective visual (monogram) to give a repeatable navigation cue without pretending to represent technical work.
- Featured case-study card: use a Precision@50 comparison chart as a real work capture. The document reports a baseline Precision@50 of 0.340 and a model Precision@50 of 0.540.[1]
- Case-study methodology section: include a feature-importance chart as a real work capture; it is an output of the capstone analysis.
- Case-study detail: include notebook/report/repository links as real links (not images).
- About section: personal portrait is not included yet; a real portrait must be supplied by Umer before adding; no generated avatar will be used.
- Contact / CTA: no additional visual is needed.
- Final keepers: (1) Precision@50 comparison — file path 'real_work_captures/precision_at_50_real_capture.png' described as proving the model's held-out-client Precision@50 was higher than the baseline in the reported experiment.[1]; (2) Feature-importance chart — file path 'real_work_captures/feature_importance_real_capture.png' showing which features the reported model ranked as influential; (3) U monogram — file path '../CUSTOM-MQX00WJN-0CE9EDFA/assets/umer_sajid_monogram_clean.png' intended as portfolio identity only and explicitly noted as not proving ML work.
- Rejected image: an AI-generated hero illustration of abstract dashboards, neural networks, or a person coding was explicitly rejected because it would not show actual work or method and could reduce trust; the real Precision@50 chart is preferred.
- Real capture over AI policy: for the featured project card, the real Precision@50 chart is used instead of an AI-generated image; generated imagery is limited to the small U monogram, which should not be presented as model output.
- Presentation rules: keep chart labels and axes visible; do not crop away context; use alt text that states what the chart shows rather than an inflated conclusion (example given: 'Precision@50 comparison: baseline 0.340; model 0.540 on seven held-out clients.'); do not apply decorative filters, fake dashboard frames, or modifications that change the charts' meaning; add a real portrait only after Umer supplies one and approves its use.
- Reference: the document cites a public case study link: https://umersajid842.github.io/flyrankmlproject/ [1].

### Limits or unknowns

- The document does not include a personal portrait image — it states the portrait must be supplied by Umer but does not provide that file.
- The document lists file paths for keepers but does not provide proof within this source that those files are accessible or their contents (we cannot verify the images themselves from this document alone).
- The document reports Precision@50 values (baseline 0.340; model 0.540) and cites a public case study, but this source does not itself provide the raw data, notebooks, or independent verification of the experiment beyond the cited link.
- The document does not state whether Umer has approved the listed assets for publication beyond the stated rules (e.g., portrait approval is pending).
- The content and current state of the external reference (the cited URL) are not included in this document and cannot be verified from this source alone.

### Publishable artifacts

- real_work_captures/precision_at_50_real_capture.png
- real_work_captures/feature_importance_real_capture.png
- ../CUSTOM-MQX00WJN-0CE9EDFA/assets/umer_sajid_monogram_clean.png
- Recommended alt text example: 'Precision@50 comparison: baseline 0.340; model 0.540 on seven held-out clients.'
- Public case study reference URL: https://umersajid842.github.io/flyrankmlproject/ [1]

## Step 3 — Draft for human review

> Draft evidence note: For the Umer Sajid portfolio, present real work captures first: include the Precision@50 comparison (real_work_captures/precision_at_50_real_capture.png) showing baseline 0.340 and model 0.540 as reported in the case study [1]; include the feature-importance chart (real_work_captures/feature_importance_real_capture.png); add the U monogram (../CUSTOM-MQX00WJN-0CE9EDFA/assets/umer_sajid_monogram_clean.png) as identity only, not as model output. Keep chart labels/axes visible and use the recommended alt text. Limitation: portrait not yet supplied and file contents/access/raw data are not independently verified here.

## Step 4 — Claim audit

| Audit status | Required human check |
|---|---|
| `revise_before_review` | Checklist for reviewer before publishing: (1) Verify each keeper file exists at the stated path and open each image to confirm it matches the described chart (precision_at_50 and feature_importance). (2) Confirm alt text for the Precision@50 image matches the recommended example or an evidence-first equivalent (state the numbers and context). (3) Ensure charts are not cropped, axes/labels are fully visible, and no decorative filters/frames have been applied. (4) Confirm the U monogram is used only as identity (label it accordingly) and is not presented as model output or evidence of technical work. (5) Ensure no AI-generated hero illustrations are used in place of real work captures. (6) Confirm notebook/report/repository links are present as real, clickable links (not images) and are included on the case-study detail page. (7) Verify whether a personal portrait has been supplied by Umer and that Umer has approved its use; if not supplied, do not add a generated avatar. (8) Optionally check the cited public case study URL (https://umersajid842.github.io/flyrankmlproject/) to corroborate the reported Precision@50 values and methodology; note any discrepancies for correction. |

### Supported claims

- Present real work captures first as a curation principle.
- Include the Precision@50 comparison image at real_work_captures/precision_at_50_real_capture.png showing baseline 0.340 and model 0.540 as reported in the case study [1].
- Include the feature-importance chart at real_work_captures/feature_importance_real_capture.png as a real work capture.
- Add the U monogram at ../CUSTOM-MQX00WJN-0CE9EDFA/assets/umer_sajid_monogram_clean.png for portfolio identity only, not as model output.
- Keep chart labels and axes visible and use the recommended alt text (example: 'Precision@50 comparison: baseline 0.340; model 0.540 on seven held-out clients.').
- Note the limitation that a personal portrait has not yet been supplied.
- Note the limitation that file contents/access/raw data are not independently verified in this document.

### Risks or missing support

- The draft does not explicitly require including notebook/report/repository links as real, clickable links (the extracted facts require repository links be provided as real links, not images).
- This source does not verify that the listed image files exist at the given paths or that their visual contents match the described charts.
- The draft does not explicitly restate presentation prohibitions from the guidance (do not crop away context, do not apply decorative filters or fake dashboard frames, and do not present the monogram as model output).
- The draft does not explicitly prohibit using an AI-generated hero illustration; the guidance rejected such generated hero images and prefers the real Precision@50 chart instead.
- The document does not confirm that Umer has approved the use of the monogram and other assets for publication (portrait approval is explicitly pending).
- The source does not provide the raw data, notebooks, or independent verification of the reported Precision@50 experiment beyond citing the external case study URL.

## Step 5 — Required human handoff

The workflow stops here. A human must compare each draft sentence with the original source, confirm the document is public-safe, verify no planned work is described as complete, and decide whether to publish, revise, or discard the draft.

## Timing record

This measured time covers the automated source-to-audit run only. It does **not** claim that human review can be removed or that the automation replaces manual source reading. Token counts are retained in the corresponding JSON record for reproducibility.
