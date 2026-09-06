"""Shared constants and helpers for the P2 grading pipeline."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
EXERCISES_DIR = ROOT / "exercises"
PRIVATE_DIR = ROOT / "private"

# Server-side question id -> our exercise slug.
QID_TO_SLUG = {
    "q-case-dth-month-end-server": "1a-dth-month-end",
    "q-case-dth-complaints-quiet-server": "1b-dth-complaints-quiet",
    "q-case-solar-smell-test-server": "2a-solar-smell-test",
    "q-case-solar-impact-claim-server": "2b-solar-impact-claim",
    "q-case-customs-mismatch-server": "3a-customs-mismatch",
    "q-case-customs-preference-server": "3b-customs-preference",
    "q-case-consumer-qc-queue-server": "4a-consumer-qc-queue",
    "q-case-consumer-spares-search-server": "4b-consumer-spares-search",
}

PARTICIPATION_PER_QUESTION = 2.5


def slugify(email):
    """email -> filesystem-safe slug."""
    return re.sub(r"[^a-zA-Z0-9]+", "_", email.strip().lower()).strip("_")


def rubric_path(slug):
    return EXERCISES_DIR / slug / "rubric.md"


def exercise_slugs():
    return sorted(p.name for p in EXERCISES_DIR.iterdir() if p.is_dir())
