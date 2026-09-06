#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "python-dotenv"]
# ///
"""Grade one submission against one exercise's rubric.md.

rubric.md is written as an LLM evaluator prompt -- each exercise defines its own
dimensions and weights, so nothing here hardcodes them. Also asks for a `verdict` on a
fixed 6-point scale (strong/good/mixed/weak/poor/unsafe), since rubrics phrase their own
`overall_label` differently and a consistent field is needed for display.

Credentials: reads AIPIPE_BASE_URL / AIPIPE_TOKEN from .env.

CLI usage (for a one-off manual check):
  uv run grade.py --exercise exercises/1a-dth-month-end --submission path/to/submission.md
"""
import argparse
import asyncio
import json
import os
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

load_dotenv()

SCHEMA = {
    "type": "object",
    "properties": {
        "dimensions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "weight_pct": {"type": "number"},
                    "score_0_4": {"type": "integer"},
                    "citations": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["name", "weight_pct", "score_0_4", "citations"],
                "additionalProperties": False,
            },
        },
        "weighted_total_0_100": {"type": "number"},
        "unsupported_or_overstated_claims": {"type": "array", "items": {"type": "string"}},
        "strongest_alternative_interpretation": {"type": "string"},
        "single_most_valuable_next_improvement": {"type": "string"},
        "overall_label": {"type": "string"},
        "verdict": {
            "type": "string",
            "enum": ["strong", "good", "mixed", "weak", "poor", "unsafe"],
            "description": "Fixed 6-point scale, independent of overall_label, for consistent display.",
        },
    },
    "additionalProperties": False,
    "required": [
        "dimensions", "weighted_total_0_100", "unsupported_or_overstated_claims",
        "strongest_alternative_interpretation", "single_most_valuable_next_improvement",
        "overall_label", "verdict",
    ],
}

def _validate(result):
    """Catch schema-valid-but-garbage output: a model that stalls mid-rubric can still
    emit valid JSON with most dimensions missing. Real rubrics always return 5-6
    dimensions; weight_pct sums and citation wording vary too much across genuine
    gradings to check reliably, so dimension count is the only stable signal."""
    dims = result.get("dimensions", [])
    if len(dims) < 3:
        raise ValueError(f"only {len(dims)} dimensions (expected >=3)")


_INSTRUCTION = (
    "Evaluate this analyst submission per the rubric above. Use exactly the dimension "
    "names and weights the rubric defines. Respond with the required evaluator output "
    "as JSON matching the given schema, nothing else. In addition to whatever overall_label "
    "convention the rubric itself asks for, also set `verdict` to exactly one of: strong, "
    "good, mixed, weak, poor, unsafe -- a fixed scale used consistently across every exercise "
    "regardless of that rubric's own label wording.\n\n--- SUBMISSION ---\n"
)


def _payload(rubric_text, submission_text, model):
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": rubric_text},
            {"role": "user", "content": _INSTRUCTION + submission_text},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {"name": "evaluator_output", "strict": True, "schema": SCHEMA},
        },
    }


def grade(rubric_text, submission_text, model, timeout=60, retries=3):
    """Synchronous single-call grader -- manual checks, small scripts."""
    base_url = os.environ["AIPIPE_BASE_URL"]
    token = os.environ["AIPIPE_TOKEN"]
    headers = {"Authorization": f"Bearer {token}", "User-Agent": "Mozilla/5.0"}
    payload = _payload(rubric_text, submission_text, model)
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            resp = httpx.post(f"{base_url}/chat/completions", json=payload, headers=headers, timeout=timeout)
            resp.raise_for_status()
            content = resp.json()["choices"][0]["message"]["content"]
            result = json.loads(content)
            _validate(result)
            return result
        except (httpx.TimeoutException, httpx.HTTPStatusError, ValueError) as e:
            last_exc = e
            if attempt < retries:
                time.sleep(2**attempt)
    raise last_exc


async def grade_async(client, rubric_text, submission_text, model, timeout=60, retries=3):
    """Concurrent-friendly grader -- pass a shared httpx.AsyncClient (base_url=AIPIPE_BASE_URL),
    call many of these via asyncio.gather, bounded by a semaphore at the call site."""
    token = os.environ["AIPIPE_TOKEN"]
    headers = {"Authorization": f"Bearer {token}", "User-Agent": "Mozilla/5.0"}
    payload = _payload(rubric_text, submission_text, model)
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            resp = await client.post("/chat/completions", json=payload, headers=headers, timeout=timeout)
            resp.raise_for_status()
            content = resp.json()["choices"][0]["message"]["content"]
            result = json.loads(content)
            _validate(result)
            return result
        except (httpx.TimeoutException, httpx.HTTPStatusError, ValueError) as e:
            last_exc = e
            if attempt < retries:
                await asyncio.sleep(2**attempt)
    raise last_exc


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exercise", required=True, help="path to exercises/<slug>/")
    ap.add_argument("--submission", required=True, help="path to a submission .md file")
    ap.add_argument("--model", default="gpt-5.6-luna")
    args = ap.parse_args()

    rubric_text = Path(args.exercise, "rubric.md").read_text()
    submission_text = Path(args.submission).read_text()
    result = grade(rubric_text, submission_text, args.model)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
