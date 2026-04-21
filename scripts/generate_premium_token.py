#!/usr/bin/env python3
"""
Generate or verify the current monthly premium access token.

Usage:
    python scripts/generate_premium_token.py
        Print the current month's token to stdout.

    python scripts/generate_premium_token.py --verify TOKEN
        Exit 0 if TOKEN is valid for current month, 1 otherwise.

    python scripts/generate_premium_token.py --hash
        Print the SHA-256 hash of the current month's token (for embedding in pages).

The token is derived from PREMIUM_SECRET env var + current YYYY-MM.
Set PREMIUM_SECRET in GitHub secrets. Rotate the underlying secret yearly.

Tokens are valid for the current month only. On the 1st of each month the
new token is emailed to active MailerLite subscribers before the old one expires.
"""
from __future__ import annotations
import hashlib
import hmac
import os
import sys
from datetime import datetime

SECRET_ENV = "PREMIUM_SECRET"
FALLBACK_SECRET = "dev-secret-change-me"


def _get_secret() -> str:
    return os.environ.get(SECRET_ENV, FALLBACK_SECRET)


def token_for_month(year_month: str | None = None) -> str:
    """Return the access token for the given YYYY-MM (default: current month)."""
    if year_month is None:
        year_month = datetime.utcnow().strftime("%Y-%m")
    secret = _get_secret().encode()
    msg = year_month.encode()
    raw = hmac.new(secret, msg, hashlib.sha256).hexdigest()
    # First 12 chars — short enough to type, long enough to not brute-force
    return raw[:12]


def token_hash(token: str) -> str:
    """SHA-256 of the token — safe to embed in public HTML."""
    return hashlib.sha256(token.encode()).hexdigest()


def main():
    args = sys.argv[1:]
    if "--verify" in args:
        idx = args.index("--verify")
        candidate = args[idx + 1] if idx + 1 < len(args) else ""
        expected = token_for_month()
        if hmac.compare_digest(candidate.strip().lower(), expected):
            print("valid")
            sys.exit(0)
        else:
            print("invalid")
            sys.exit(1)
    elif "--hash" in args:
        tok = token_for_month()
        print(token_hash(tok))
    else:
        print(token_for_month())


if __name__ == "__main__":
    main()
