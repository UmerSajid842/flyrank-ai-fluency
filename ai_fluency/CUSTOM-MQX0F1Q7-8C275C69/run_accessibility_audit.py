#!/usr/bin/env python3
"""Run a narrow, reproducible accessibility audit over the public static site source."""
import json
from pathlib import Path
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
OUT = Path(__file__).with_name("ai_accessibility_audit.json")

source = "\n\n".join([
    "--- docs/index.html ---\n" + (DOCS / "index.html").read_text(encoding="utf-8"),
    "--- docs/case-study.html ---\n" + (DOCS / "case-study.html").read_text(encoding="utf-8"),
    "--- docs/site.css ---\n" + (DOCS / "site.css").read_text(encoding="utf-8"),
])

schema = {
    "name": "static_site_accessibility_audit",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "scope": {"type": "string"},
            "strengths": {"type": "array", "items": {"type": "string"}},
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "severity": {"type": "string", "enum": ["critical", "important", "minor"]},
                        "evidence": {"type": "string"},
                        "risk": {"type": "string"},
                        "recommended_change": {"type": "string"}
                    },
                    "required": ["severity", "evidence", "risk", "recommended_change"],
                    "additionalProperties": False
                }
            },
            "limitations": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["scope", "strengths", "findings", "limitations"],
        "additionalProperties": False
    }
}

prompt = f"""You are auditing only the supplied static HTML and CSS for practical mobile accessibility.
Do not claim to have used a physical phone, screen reader, or live network. Identify only issues supported by this source.
Prioritize focus indication, touch target sizing, responsive layout, link clarity, heading/navigation structure, color reliance, and image alt text.
Return concise JSON matching the supplied schema.

SOURCE:\n{source}"""

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "You are a rigorous accessibility reviewer. Do not invent test results."},
        {"role": "user", "content": prompt},
    ],
    response_format={"type": "json_schema", "json_schema": schema},
    max_completion_tokens=1800,
)
result = json.loads(response.choices[0].message.content)
record = {
    "model": "gpt-5-mini",
    "input_files": ["docs/index.html", "docs/case-study.html", "docs/site.css"],
    "audit": result,
    "usage": {
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
    },
}
OUT.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, indent=2))
