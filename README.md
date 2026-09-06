# TDS 2026-05 Project 2 — grading pipeline

Grades the 8 case-study questions in Project 2 against their rubrics using an LLM
judge, run as a public GitHub Actions batch after the submission deadline.

## Pipeline

```
fetch.py     -- pull every student's latest accepted submission from the exam server
batch.py     -- grade every answered question against its exercise's rubric.md
                (concurrent, retries with backoff, resumable across runs)
codes.py     -- generate each student's 16-digit lookup code
publish.py   -- write results/<code>.json and revealed/<slug>/rubric.md
```

`calibrate.py` + `tests/test_calibration.py` check the grader against 6 known-distinct
sample submissions per exercise before it's trusted on real students:

```
uv run calibrate.py    # generate calibration results (costs API calls)
uv run pytest tests/   # check them (free, no network)
```

`index.html` (repo root, permanently committed, not generated) is the student-facing
result page — paste your code, see your mark, per-question breakdown, and a link to
that question's rubric.

## Running it

```
uv run fetch.py --quiz tds-2026-05-p2
uv run batch.py                    # or --limit N
uv run codes.py --emails private/roster.csv
uv run publish.py --out .          # once batch.py has graded everyone
```

`private/` (submissions, grades, the email↔code mapping) is gitignored and never
committed — only `results/`, `revealed/`, and `index.html` are public.

The real run is `.github/workflows/grade.yml` (`workflow_dispatch`, run manually in
batches). Needs three repo secrets (`AIPIPE_BASE_URL`, `AIPIPE_TOKEN`, `CODE_SECRET`)
and Pages set to deploy from `main` / root.
