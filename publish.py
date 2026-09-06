#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Build the public-facing output tree from already-graded results.

- results/<code>.json -- one file per student, keyed by their 16-digit lookup code, not
  their email. Run this after batch.py has graded everyone.
- revealed/<slug>/{rubric.md,tests/} -- each exercise's rubric and calibration examples,
  published once grading is complete.

(index.html, the lookup page, is a permanently-committed root file -- not generated here.)

Usage:
  uv run publish.py --out .
"""
import argparse
import json
import shutil
from pathlib import Path

from common import (
    EXERCISES_DIR,
    PARTICIPATION_PER_QUESTION,
    PRIVATE_DIR,
    exercise_slugs,
    slugify,
)


def build_student_result(student_slug, grades_dir):
    student_dir = grades_dir / student_slug
    if not student_dir.exists():
        return None
    per_question = []
    participation = 0.0
    analytical = 0.0
    for f in sorted(student_dir.glob("*.json")):
        if f.name.endswith(".error.json"):
            continue
        result = json.loads(f.read_text())
        slug = f.stem
        q_analytical = round(result["weighted_total_0_100"] / 10, 1)
        participation += PARTICIPATION_PER_QUESTION
        analytical += q_analytical
        per_question.append({
            "exercise": slug,
            "participation": PARTICIPATION_PER_QUESTION,
            "analytical": q_analytical,
            "verdict": result.get("verdict"),
            "dimensions": result.get("dimensions"),
            "unsupported_or_overstated_claims": result.get("unsupported_or_overstated_claims"),
            "strongest_alternative_interpretation": result.get("strongest_alternative_interpretation"),
            "single_most_valuable_next_improvement": result.get("single_most_valuable_next_improvement"),
        })
    return {
        "questions_answered": len(per_question),
        "participation": round(participation, 2),
        "analytical": round(analytical, 2),
        "final": round(participation + analytical, 2),
        "per_question": per_question,
    }


def publish_results(codes_csv, grades_dir, out_dir):
    import csv

    results_dir = out_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    n_written, n_missing = 0, 0
    with open(codes_csv, newline="") as f:
        for row in csv.DictReader(f):
            email, code = row["email"].strip(), row["code"].strip()
            result = build_student_result(slugify(email), grades_dir)
            if result is None:
                n_missing += 1
                continue
            (results_dir / f"{code}.json").write_text(json.dumps(result, indent=2))
            n_written += 1
    print(f"Wrote {n_written} student results to {results_dir} ({n_missing} in codes.csv had no grades yet)")


EXERCISE_NAMES = {
    "1a-dth-month-end": "1A — DTH Month-End Mystery",
    "1b-dth-complaints-quiet": "1B — DTH Complaints Went Quiet",
    "2a-solar-smell-test": "2A — Solar Inverter Smell Test",
    "2b-solar-impact-claim": "2B — Solar 31.6% Impact Claim",
    "3a-customs-mismatch": "3A — Swiss Mismatch Control",
    "3b-customs-preference": "3B — Irish Preference Claim",
    "4a-consumer-qc-queue": "4A — QC Queue Smell Test",
    "4b-consumer-spares-search": "4B — Spare-Parts Search",
}


def publish_revealed(out_dir):
    revealed_dir = out_dir / "revealed"
    for slug in exercise_slugs():
        src = EXERCISES_DIR / slug
        dst = revealed_dir / slug
        (dst / "tests" / "submissions").mkdir(parents=True, exist_ok=True)
        shutil.copy(src / "rubric.md", dst / "rubric.md")
        shutil.copy(src / "tests" / "expected.md", dst / "tests" / "expected.md")
        for sub in (src / "tests" / "submissions").glob("*.md"):
            shutil.copy(sub, dst / "tests" / "submissions" / sub.name)

    # GitHub Pages doesn't auto-generate directory listings, so /revealed/ needs its own index.
    rows = "\n".join(
        f'<li><a href="{slug}/rubric.md">{EXERCISE_NAMES.get(slug, slug)}</a> '
        f'&mdash; <a href="{slug}/tests/expected.md">calibration notes</a></li>'
        for slug in exercise_slugs()
    )
    (revealed_dir / "index.html").write_text(
        "<!doctype html><meta charset=utf-8><title>Revealed rubrics</title>"
        "<body style='font:16px system-ui;max-width:640px;margin:48px auto;padding:0 20px'>"
        "<h1>Revealed rubrics</h1>"
        "<p>What each Project 2 question was actually graded against, published once "
        "grading was complete. <a href='../'>&larr; Back to results lookup</a></p>"
        f"<ul style='line-height:2'>{rows}</ul></body>"
    )
    print(f"Wrote rubric.md + tests/{{submissions,expected.md}} for {len(exercise_slugs())} exercises to {revealed_dir}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--codes", default=str(PRIVATE_DIR / "codes.csv"))
    ap.add_argument("--grades-dir", default=str(PRIVATE_DIR / "grades"))
    ap.add_argument("--out", default=".")
    ap.add_argument("--skip-reveal", action="store_true", help="only publish results, not the rubric reveal")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    publish_results(args.codes, Path(args.grades_dir), out_dir)
    if not args.skip_reveal:
        publish_revealed(out_dir)


if __name__ == "__main__":
    main()
