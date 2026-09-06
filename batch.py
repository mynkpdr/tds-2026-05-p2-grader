#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "python-dotenv"]
# ///
"""Grade every fetched submission (run fetch.py first).

Reads private/submissions/<student>.json, grades every answered question against its
exercise's rubric, and writes one result file per (student, question) as soon as it
completes:

  private/grades/<student_slug>/<exercise_slug>.json         -- on success
  private/grades/<student_slug>/<exercise_slug>.error.json   -- on failure after retries

Resumable: re-running skips any (student, question) whose result file already exists.
Concurrency is bounded (default 20), not unlimited.

Usage:
  uv run batch.py                    # grade everyone in private/submissions/
  uv run batch.py --limit 5          # only the first 5 students (testing)
  uv run batch.py --concurrency 10   # more conservative
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

from common import PRIVATE_DIR, QID_TO_SLUG, rubric_path, slugify
from grade import _validate, grade_async


async def grade_job(client, sem, rubric_text, text, model, out_path):
    if out_path.exists():
        try:
            _validate(json.loads(out_path.read_text()))
            return "cached"
        except ValueError:
            pass  # cached file is schema-valid but semantically bad -- regrade it
    async with sem:
        try:
            result = await grade_async(client, rubric_text, text, model)
        except Exception as e:  # noqa: BLE001 -- one bad grading must not crash the whole batch; recorded, not swallowed
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.with_suffix(".error.json").write_text(json.dumps({"error": repr(e)}))
            return "failed"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2))
    return "graded"


async def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--submissions-dir", default=str(PRIVATE_DIR / "submissions"))
    ap.add_argument("--grades-dir", default=str(PRIVATE_DIR / "grades"))
    ap.add_argument("--concurrency", type=int, default=20)
    ap.add_argument("--model", default="gpt-5.6-luna")
    ap.add_argument("--limit", type=int, default=None, help="only process the first N students (testing)")
    args = ap.parse_args()

    sub_files = sorted(Path(args.submissions_dir).glob("*.json"))
    if args.limit:
        sub_files = sub_files[: args.limit]

    grades_dir = Path(args.grades_dir)
    rubric_cache = {}

    jobs = []
    for f in sub_files:
        d = json.loads(f.read_text())
        student_slug = slugify(d["email"])
        answers = d.get("result", {}).get("answers", {})
        for qid, text in answers.items():
            if not text or not text.strip():
                continue
            slug = QID_TO_SLUG.get(qid)
            if not slug:
                continue
            if slug not in rubric_cache:
                rubric_cache[slug] = rubric_path(slug).read_text()
            out_path = grades_dir / student_slug / f"{slug}.json"
            jobs.append((rubric_cache[slug], text, out_path))

    print(f"{len(sub_files)} students, {len(jobs)} question-submissions to grade "
          f"(concurrency={args.concurrency}, model={args.model})")

    base_url = os.environ["AIPIPE_BASE_URL"]
    sem = asyncio.Semaphore(args.concurrency)
    t0 = time.time()
    async with httpx.AsyncClient(base_url=base_url, timeout=60) as client:
        results = await asyncio.gather(
            *(grade_job(client, sem, rubric, text, args.model, out_path) for rubric, text, out_path in jobs)
        )
    dt = time.time() - t0

    counts = {"cached": 0, "graded": 0, "failed": 0}
    for r in results:
        counts[r] += 1
    print(f"Done in {dt:.1f}s -- {counts['graded']} graded, {counts['cached']} already cached, "
          f"{counts['failed']} failed (see private/grades/*/*.error.json)")


if __name__ == "__main__":
    asyncio.run(main())
