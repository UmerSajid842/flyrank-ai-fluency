# Week 2 — ChatGPT Final Prompt Run

**Run date:** 2026-08-13  
**Interface:** Public ChatGPT guest session in the browser  
**Purpose:** Required final-prompt comparison for FL-02. The transcript below preserves the actual prompt and output.

## Prompt

> You are an evidence-first portfolio editor for a junior machine-learning candidate. Write a portfolio case study introduction for a hiring manager at an SEO or content-intelligence company. The aim is to show leakage-aware evaluation and a useful editorial-review decision, not to market an automated SEO product. Use only these verified facts: Umer Sajid built a leakage-aware random-forest prototype for prioritising anonymised content pages for editorial review. The public-safe starter release contains about 30,000 pages across 32 pseudonymised clients. Validation held out seven pseudonymised clients. On that held-out split, Precision@50 was 0.540 for the model and 0.340 for a transparent baseline. The result supports a review-for-refresh queue; it does not prove traffic recovery, causation, or autonomous page changes. Use this miniature style example only for voice and evidence discipline: 'I evaluated a ranking prototype on data it had not seen, compared it with a transparent baseline, and stated the boundary of what the comparison can show.' Do not copy its wording and do not add facts. Return exactly: (1) a 30-word headline, (2) a 130–160 word introduction, and (3) a one-sentence limitation. Use plain English. First silently list the allowed facts, then draft, then silently check every factual claim against the allowed facts; if a claim is unsupported, remove it. Do not reveal the internal check.

## Actual output

### (1) Headline

A leakage-aware random-forest prototype prioritised anonymised pages for editorial review, with client-held-out validation showing stronger Precision@50 than a transparent baseline without claiming traffic recovery or autonomous page changes as an outcome.

### (2) Introduction

Umer Sajid built a leakage-aware random-forest prototype to prioritise anonymised content pages for editorial review. The public-safe starter release contains about 30,000 pages across 32 pseudonymised clients. To test whether the ranking held up beyond the clients used for development, validation held out seven pseudonymised clients. On that held-out split, the model achieved Precision@50 of 0.540, compared with 0.340 for a transparent baseline. The practical editorial question is therefore narrow and useful: which pages should enter a review-for-refresh queue? The comparison provides evidence for that prioritisation decision on unseen clients, while keeping the evaluation boundary clear. It does not establish that refreshing pages will recover traffic, that the model causes any traffic outcome, or that pages should be changed automatically. The prototype is presented as a way to support editorial review, with leakage-aware validation and a transparent comparison at its core.

### (3) Limitation

The held-out Precision@50 result supports a review-for-refresh queue, but does not prove traffic recovery, causation, or autonomous page changes.

## Evidence boundary

This is a genuine ChatGPT guest-session run. It is not presented as a login, certificate, or persistent account activity.
