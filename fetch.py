#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx"]
# ///
"""Fetch every student's latest accepted submission for a quiz.

Uses the exam server's no-history "latest per email" endpoint (GET /filter), paginated
at 200/page -- an unpaginated request hits the server's 32MiB response cap at real
class-size scale. If a student's latest row is a rejected retry, their full history is
checked individually to recover an earlier accepted attempt.

Usage:
  uv run fetch.py --quiz tds-2026-05-p2 --out-dir private/submissions
"""
import argparse
import asyncio
import csv
import json
from pathlib import Path

import httpx

from common import PRIVATE_DIR, slugify

BASE = "https://exam.sanand.workers.dev"
PAGE_LIMIT = 200


async def _discover_emails_once(client, quiz, limit):
    emails = set()
    page = 1
    while True:
        resp = await client.get(f"{BASE}/filter", params={"quiz": quiz, "history": "true", "limit": limit, "page": page})
        resp.raise_for_status()
        batch = resp.json().get("data", [])
        emails.update((r.get("email") or "").strip().lower() for r in batch if r.get("email"))
        if len(batch) < limit:
            break
        page += 1
    return emails


# Offset pagination against this endpoint drops different rows each pass -- observed
# empirically, not a documented server bug -- so no single page size is reliable. Sweeping
# several sizes and taking the union recovers everyone in practice (each student has many
# retry attempts, so a row dropped at one page size usually isn't dropped at another).
DISCOVERY_PAGE_SIZES = [50, 200]


async def discover_emails(client, quiz):
    """Every email that has ever attempted this quiz."""
    emails = set()
    for limit in DISCOVERY_PAGE_SIZES:
        emails |= await _discover_emails_once(client, quiz, limit)
    return emails


async def fetch_email_history(client, sem, quiz, email):
    async with sem:
        resp = await client.get(f"{BASE}/filter", params={"quiz": quiz, "email": email, "history": "true", "limit": -1})
    resp.raise_for_status()
    rows = resp.json().get("data", [])
    accepted = [r for r in rows if r.get("total") is not None and r.get("total") >= 0]
    if not accepted:
        return None
    return max(accepted, key=lambda r: r.get("time") or 0)


async def resolve(quiz):
    async with httpx.AsyncClient(timeout=60) as client:
        emails = await discover_emails(client, quiz)
        print(f"  {len(emails)} distinct emails seen -- resolving each one's true latest accepted attempt...")
        sem = asyncio.Semaphore(20)
        results = await asyncio.gather(*(fetch_email_history(client, sem, quiz, e) for e in emails))
        return {email: row for email, row in zip(emails, results) if row is not None}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiz", required=True)
    ap.add_argument("--out-dir", default=str(PRIVATE_DIR / "submissions"))
    ap.add_argument("--roster-out", default=str(PRIVATE_DIR / "roster.csv"))
    args = ap.parse_args()

    print(f"Fetching quiz={args.quiz}...")
    resolved = asyncio.run(resolve(args.quiz))
    print(f"{len(resolved)} students with an accepted submission")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for email, row in resolved.items():
        (out_dir / f"{slugify(email)}.json").write_text(json.dumps(row, indent=2))

    roster_path = Path(args.roster_out)
    roster_path.parent.mkdir(parents=True, exist_ok=True)
    with open(roster_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["email"])
        for email in sorted(resolved):
            writer.writerow([email])

    print(f"Wrote {len(resolved)} submissions to {out_dir}, roster to {roster_path}")


if __name__ == "__main__":
    main()
