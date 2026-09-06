#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["python-dotenv"]
# ///
"""Generate a 16-digit lookup code per student email.

code = HMAC-SHA256(email, CODE_SECRET), truncated to 16 decimal digits. Deterministic,
but not reversible or guessable without CODE_SECRET (kept only in .env).

Input: a CSV with an "email" column (private/roster.csv, from fetch.py).
Output: private/codes.csv (email,code) -- gitignored, never committed.

Usage:
  uv run codes.py --emails private/roster.csv
"""
import argparse
import csv
import hashlib
import hmac
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from common import PRIVATE_DIR

load_dotenv()


def make_code(email, secret):
    digest = hmac.new(secret.encode(), email.strip().lower().encode(), hashlib.sha256).hexdigest()
    n = int(digest, 16) % (10**16)
    return f"{n:016d}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--emails", required=True, help="CSV with an 'email' column")
    ap.add_argument("--out", default=str(PRIVATE_DIR / "codes.csv"))
    args = ap.parse_args()

    secret = os.environ.get("CODE_SECRET")
    if not secret:
        sys.exit("CODE_SECRET not set in .env -- generate one first (see README).")

    with open(args.emails, newline="") as f:
        emails = [row["email"].strip() for row in csv.DictReader(f) if row.get("email", "").strip()]

    if len(emails) != len({e.lower() for e in emails}):
        sys.exit("Duplicate emails in input (case-insensitive) -- dedupe before generating codes.")

    rows = [(email, make_code(email, secret)) for email in emails]

    codes = [c for _, c in rows]
    if len(codes) != len(set(codes)):
        sys.exit("Code collision detected -- extremely unlikely at this scale; investigate before proceeding.")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["email", "code"])
        writer.writerows(rows)

    print(f"Wrote {len(rows)} codes to {out_path}")


if __name__ == "__main__":
    main()
