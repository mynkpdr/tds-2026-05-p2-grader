"""Calibration gate: each exercise's 6 sample submissions (already graded and cached
under exercises/<slug>/tests/results-<model>/*.json) must satisfy structural invariants:

  - 01 (strong) and 04 (supported alternative) both rank in the top half (<=3rd of 6)
  - 02 (polished but shallow) and 06 (decoy) both rank in the bottom half (>=4th of 6)
  - 03 (lucky right, no evidence) never ranks in the top half -- a correct conclusion
    without traceable evidence must not be rewarded
  - 05 (insufficient evidence + right ask) outranks both 02 and 06
  - scores actually spread out (catches an undiscriminating judge that scores
    everyone near-identically)

Run with cached results only (no network, no cost): `uv run pytest tests/`. Skips (not
fails) any exercise/model that hasn't been calibrated yet.
"""
import json

import pytest

from common import EXERCISES_DIR, exercise_slugs

MODEL = "gpt-5.6-luna"
MIN_SPREAD = 30  # weighted_total_0_100 points between best and worst of the 6


def _load_results(slug):
    res_dir = EXERCISES_DIR / slug / "tests" / f"results-{MODEL}"
    if not res_dir.exists():
        pytest.skip(f"no cached {MODEL} calibration results for {slug} -- run calibrate.py first")
    scores = {}
    for f in res_dir.glob("*.json"):
        scores[f.stem] = json.loads(f.read_text())["weighted_total_0_100"]
    missing = {"01", "02", "03", "04", "05", "06"} - set(scores)
    if missing:
        pytest.skip(f"{slug}: missing cached results for {sorted(missing)}")
    return scores


def _rank(scores, stem):
    """1 = highest score. Ties broken by score order, stable enough for this purpose."""
    ordered = sorted(scores, key=lambda s: -scores[s])
    return ordered.index(stem) + 1


@pytest.mark.parametrize("slug", exercise_slugs())
class TestCalibration:
    def test_strong_and_alternative_rank_top_half(self, slug):
        scores = _load_results(slug)
        assert _rank(scores, "01") <= 3, f"{slug}: 'strong' (01) should rank in the top half"
        assert _rank(scores, "04") <= 3, f"{slug}: 'supported alternative' (04) should rank in the top half"

    def test_shallow_and_decoy_rank_bottom_half(self, slug):
        scores = _load_results(slug)
        assert _rank(scores, "02") >= 4, f"{slug}: 'polished but shallow' (02) should rank in the bottom half"
        assert _rank(scores, "06") >= 4, f"{slug}: 'decoy' (06) should rank in the bottom half"

    def test_lucky_right_not_rewarded(self, slug):
        scores = _load_results(slug)
        assert _rank(scores, "03") >= 4, (
            f"{slug}: 'lucky right' (03, correct conclusion but no traceable evidence) "
            "must not rank in the top half -- rewarding it means the grader isn't checking evidence"
        )

    def test_insufficient_evidence_beats_shallow_and_decoy(self, slug):
        scores = _load_results(slug)
        assert scores["05"] > scores["02"], f"{slug}: 'insufficient evidence + right ask' (05) should beat 'shallow' (02)"
        assert scores["05"] > scores["06"], f"{slug}: 'insufficient evidence + right ask' (05) should beat 'decoy' (06)"

    def test_scores_actually_discriminate(self, slug):
        scores = _load_results(slug)
        spread = max(scores.values()) - min(scores.values())
        assert spread >= MIN_SPREAD, (
            f"{slug}: only {spread:.1f} points between best and worst of 6 known-distinct submissions -- "
            f"looks like the P1 ceiling-clustering failure (judge not discriminating), needs at least {MIN_SPREAD}"
        )
