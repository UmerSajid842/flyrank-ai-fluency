#!/usr/bin/env python3
"""Run a public-safe, source-grounded evidence-writing workflow on local Markdown files.

The workflow never publishes and always ends with a human-review requirement.
"""

from __future__ import annotations

import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "runs"
MODEL = "gpt-5-mini"

SOURCES = [
    ("capstone_model_report", Path("/home/ubuntu/flyrankmlproject-source/outputs/model_report.md")),
    ("identity_kit", Path("/home/ubuntu/flyrank-ai-fluency/ai_fluency/CUSTOM-MQX00WJN-0CE9EDFA/identity_kit.md")),
    ("image_curation", Path("/home/ubuntu/flyrank-ai-fluency/ai_fluency/CUSTOM-MQX033TI-DE712A19/image_curation.md")),
    ("content_cta_map", Path("/home/ubuntu/flyrank-ai-fluency/ai_fluency/CUSTOM-MQWZXUQU-B5F087BE/content_and_cta_map.md")),
    ("stack_decision", Path("/home/ubuntu/flyrank-ai-fluency/ai_fluency/CUSTOM-MQX06U8B-9AAA4FBA/three_roads_stack_decision.md")),
]

EXTRACTION_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "evidence_extract",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "source_purpose": {"type": "string"},
                "verified_facts": {"type": "array", "items": {"type": "string"}},
                "limits_or_unknowns": {"type": "array", "items": {"type": "string"}},
                "publishable_artifacts": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["source_purpose", "verified_facts", "limits_or_unknowns", "publishable_artifacts"],
            "additionalProperties": False,
        },
    },
}

AUDIT_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "claim_audit",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "status": {"type": "string", "enum": ["safe_for_human_review", "revise_before_review"]},
                "supported_claims": {"type": "array", "items": {"type": "string"}},
                "risks_or_missing_support": {"type": "array", "items": {"type": "string"}},
                "human_check": {"type": "string"},
            },
            "required": ["status", "supported_claims", "risks_or_missing_support", "human_check"],
            "additionalProperties": False,
        },
    },
}


def clean_text(text: str) -> str:
    """Remove only obvious secret-like values; do not alter claims."""
    text = re.sub(r"(?i)(api[_ -]?key|token|password)\s*[:=]\s*\S+", r"\1: [redacted]", text)
    return text[:18000]


def call_json(client: OpenAI, prompt: str, schema: dict) -> tuple[dict, dict]:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful evidence assistant. Use only statements directly supported by the supplied "
                    "source. Never invent metrics, people, URLs, actions, or outcomes. When support is missing, say so."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        response_format=schema,
    )
    usage = {
        "prompt_tokens": getattr(response.usage, "prompt_tokens", None),
        "completion_tokens": getattr(response.usage, "completion_tokens", None),
        "total_tokens": getattr(response.usage, "total_tokens", None),
    }
    return json.loads(response.choices[0].message.content), usage


def call_draft(client: OpenAI, extracted: dict) -> tuple[str, dict]:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Write a 55-85 word draft portfolio evidence note using only the verified facts provided. "
                    "Do not make performance claims beyond the facts. Mention a limitation when it is material. "
                    "This is a draft for human review, not publication."
                ),
            },
            {"role": "user", "content": json.dumps(extracted, ensure_ascii=False)},
        ],
        max_completion_tokens=350,
    )
    usage = {
        "prompt_tokens": getattr(response.usage, "prompt_tokens", None),
        "completion_tokens": getattr(response.usage, "completion_tokens", None),
        "total_tokens": getattr(response.usage, "total_tokens", None),
    }
    return response.choices[0].message.content.strip(), usage


def run_one(client: OpenAI, slug: str, source_path: Path) -> dict:
    started = time.perf_counter()
    source = clean_text(source_path.read_text(encoding="utf-8"))
    extraction, extraction_usage = call_json(
        client,
        f"STEP 1 — SOURCE PACKET\nSource name: {source_path.name}\n\n{source}",
        EXTRACTION_SCHEMA,
    )
    draft, draft_usage = call_draft(client, extraction)
    audit, audit_usage = call_json(
        client,
        "STEP 3 — CLAIM AUDIT\nAudit this draft against the extracted facts. The output must require "
        "human review even if the draft is supported.\n\nEXTRACTED FACTS:\n"
        f"{json.dumps(extraction, ensure_ascii=False)}\n\nDRAFT:\n{draft}",
        AUDIT_SCHEMA,
    )
    elapsed = round(time.perf_counter() - started, 2)
    return {
        "run": slug,
        "source_path": str(source_path),
        "ran_at_utc": datetime.now(timezone.utc).isoformat(),
        "model": MODEL,
        "workflow_steps": [
            "1. Prepare local public-safe source packet",
            "2. Extract structured, source-grounded evidence",
            "3. Draft a portfolio evidence note from extracted facts",
            "4. Audit claims against the extracted facts",
            "5. Require human evidence and privacy review before any publication",
        ],
        "elapsed_seconds": elapsed,
        "extraction": extraction,
        "draft_for_human_review": draft,
        "claim_audit": audit,
        "usage": {"extraction": extraction_usage, "draft": draft_usage, "audit": audit_usage},
        "publication_status": "not_published_human_review_required",
    }


def markdown_report(result: dict) -> str:
    facts = "\n".join(f"- {item}" for item in result["extraction"]["verified_facts"]) or "- None extracted"
    limits = "\n".join(f"- {item}" for item in result["extraction"]["limits_or_unknowns"]) or "- None identified"
    artifacts = "\n".join(f"- {item}" for item in result["extraction"]["publishable_artifacts"]) or "- None identified"
    risks = "\n".join(f"- {item}" for item in result["claim_audit"]["risks_or_missing_support"]) or "- No additional risks identified by the automated audit; human review still required"
    return f"""# Workflow Run: {result['run']}

| Field | Value |
|---|---|
| Source | `{result['source_path']}` |
| Run time (UTC) | {result['ran_at_utc']} |
| Model | `{result['model']}` |
| Measured workflow time | {result['elapsed_seconds']} seconds |
| Publication status | **Not published — human review required** |

## Step 1 — Source packet

**Purpose:** {result['extraction']['source_purpose']}

## Step 2 — Structured evidence extraction

### Verified facts

{facts}

### Limits or unknowns

{limits}

### Publishable artifacts

{artifacts}

## Step 3 — Draft for human review

> {result['draft_for_human_review']}

## Step 4 — Claim audit

| Audit status | Required human check |
|---|---|
| `{result['claim_audit']['status']}` | {result['claim_audit']['human_check']} |

### Supported claims

{"\n".join(f"- {item}" for item in result['claim_audit']['supported_claims']) or "- None"}

### Risks or missing support

{risks}

## Step 5 — Required human handoff

The workflow stops here. A human must compare each draft sentence with the original source, confirm the document is public-safe, verify no planned work is described as complete, and decide whether to publish, revise, or discard the draft.

## Timing record

This measured time covers the automated source-to-audit run only. It does **not** claim that human review can be removed or that the automation replaces manual source reading. Token counts are retained in the corresponding JSON record for reproducibility.
"""


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    client = OpenAI()
    manifest = []
    for slug, source_path in SOURCES:
        result = run_one(client, slug, source_path)
        (OUTPUT_DIR / f"{slug}.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        (OUTPUT_DIR / f"{slug}.md").write_text(markdown_report(result), encoding="utf-8")
        manifest.append({"run": slug, "elapsed_seconds": result["elapsed_seconds"], "status": result["claim_audit"]["status"]})
        print(f"Completed {slug}: {result['elapsed_seconds']} seconds")
    (OUTPUT_DIR / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
