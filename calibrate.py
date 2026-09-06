#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "python-dotenv"]
# ///
"""Grade every exercise's 6 sample submissions and cache the results (one API call per
submission, skipped if already cached) for tests/test_calibration.py to check.

This script generates calibration data; it does not judge it -- run
`uv run pytest tests/` afterward for the pass/fail gate.

Usage:
  uv run calibrate.py                 # all exercises
  uv run calibrate.py --exercise 1a-dth-month-end
  uv run calibrate.py --model gpt-5.6-sol   # compare a different judge
"""
import argparse
import json

from common import EXERCISES_DIR, exercise_slugs, rubric_path
from grade import grade


def run_exercise(slug, model):
    rubric_text = rubric_path(slug).read_text()
    ex_dir = EXERCISES_DIR / slug
    submissions = sorted((ex_dir / "tests" / "submissions").glob("*.md"))
    out_dir = ex_dir / "tests" / f"results-{model}"
    out_dir.mkdir(exist_ok=True)

    for sub in submissions:
        out_path = out_dir / f"{sub.stem}.json"
        if out_path.exists():
            continue
        print(f"  grading {slug}/{sub.name}...")
        result = grade(rubric_text, sub.read_text(), model)
        out_path.write_text(json.dumps(result, indent=2))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exercise", help="a single exercise slug (e.g. 1a-dth-month-end); default: all")
    ap.add_argument("--model", default="gpt-5.6-luna")
    args = ap.parse_args()

    slugs = [args.exercise] if args.exercise else exercise_slugs()
    for slug in slugs:
        print(f"=== {slug} ===")
        run_exercise(slug, args.model)

    print("\nDone. Run `uv run pytest tests/` to check the results.")


if __name__ == "__main__":
    main()
