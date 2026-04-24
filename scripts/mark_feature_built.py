#!/usr/bin/env python3
"""
mark_feature_built.py

Moves a feature PRD from drafts/features/<date>/ to drafts/features/built/
so it is excluded from future virality rankings.
Also removes it from the score cache.

Usage:
    python scripts/mark_feature_built.py openai-feature-04-receipts-guy-s-trade-history-scroll.md
    python scripts/mark_feature_built.py receipts-guy   # partial match, interactive confirm
    python scripts/mark_feature_built.py --list         # show all unbuilt features
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

DRAFTS_DIR = Path("drafts/features")
BUILT_DIR = Path("drafts/features/built")
CACHE_FILE = Path("reports/virality/.score_cache.json")


def find_all_drafts():
    import re
    files = []
    for subdir in sorted(DRAFTS_DIR.iterdir()):
        if subdir.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}", subdir.name):
            files.extend(subdir.glob("*.md"))
    return sorted(files)


def load_cache():
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_cache(cache):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def move_to_built(path: Path) -> Path:
    BUILT_DIR.mkdir(parents=True, exist_ok=True)
    dest = BUILT_DIR / path.name
    if dest.exists():
        # avoid collision — prefix with source date dir
        dest = BUILT_DIR / f"{path.parent.name}_{path.name}"
    shutil.move(str(path), str(dest))
    return dest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", nargs="?", help="Filename or partial match")
    parser.add_argument("--list", action="store_true", help="List all unbuilt features")
    args = parser.parse_args()

    drafts = find_all_drafts()

    if args.list or not args.name:
        cache = load_cache()
        print(f"Unbuilt features ({len(drafts)}):\n")
        for p in drafts:
            cached = cache.get(str(p), {})
            score = cached.get("adjusted_score", "—")
            verdict = cached.get("verdict", "unscored")
            name = cached.get("feature_name") or p.stem
            print(f"  {p.name}")
            print(f"    {name} — {verdict} (score={score})")
        return

    # Match by partial filename
    matches = [p for p in drafts if args.name.lower() in p.name.lower()]

    if not matches:
        print(f"No draft found matching: {args.name}")
        sys.exit(1)

    if len(matches) > 1:
        print(f"Multiple matches for '{args.name}':")
        for i, p in enumerate(matches):
            print(f"  {i+1}. {p}")
        choice = input("Pick number: ").strip()
        try:
            path = matches[int(choice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice.")
            sys.exit(1)
    else:
        path = matches[0]

    cache = load_cache()
    cached = cache.get(str(path), {})
    name = cached.get("feature_name") or path.stem
    score = cached.get("adjusted_score", "—")
    verdict = cached.get("verdict", "unscored")

    print(f"\nMarking as BUILT: {path.name}")
    print(f"  {name} — {verdict} (score={score})")
    confirm = input("Confirm? [y/N] ").strip().lower()
    if confirm != "y":
        print("Aborted.")
        sys.exit(0)

    dest = move_to_built(path)

    # Remove from cache so it doesn't linger in master_rank
    if str(path) in cache:
        del cache[str(path)]
        save_cache(cache)
        print(f"Removed from score cache.")

    print(f"Moved to: {dest}")
    print(f"\nRun 'python scripts/rank_features_nightly.py' to rebuild master_rank without it.")


if __name__ == "__main__":
    main()
