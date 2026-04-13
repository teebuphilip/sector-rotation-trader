#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default="data/blocked/algos.jsonl")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print("No blocked queue file found.")
        return 0

    kept = []
    removed = 0
    kept_ids = []
    removed_ids = []
    kept_meta = {}
    removed_meta = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s:
            continue
        obj = json.loads(s)
        keys = obj.get("keys", []) or []
        # Keep if any key is still missing
        missing = [k for k in keys if not os.getenv(k)]
        if missing:
            obj["keys"] = missing
            kept.append(obj)
            kept_ids.append(obj.get("algo_id", obj.get("name", "unknown")))
            key = obj.get("algo_id", obj.get("name", "unknown"))
            kept_meta[key] = {"name": obj.get("name", ""), "keys": missing}
        else:
            removed += 1
            removed_ids.append(obj.get("algo_id", obj.get("name", "unknown")))
            key = obj.get("algo_id", obj.get("name", "unknown"))
            removed_meta[key] = {"name": obj.get("name", ""), "keys": obj.get("keys", [])}

    if args.dry_run:
        if removed_ids:
            print("Would remove:")
            for r in sorted(set(removed_ids)):
                meta = removed_meta.get(r, {})
                keys = ", ".join(meta.get("keys", []))
                name = meta.get("name", "")
                print(f"  - {r} | {name} | keys: {keys}")
        if kept_ids:
            print("Would keep:")
            for k in sorted(set(kept_ids)):
                meta = kept_meta.get(k, {})
                keys = ", ".join(meta.get("keys", []))
                name = meta.get("name", "")
                print(f"  - {k} | {name} | keys: {keys}")
        print(f"Would remove {removed} entries. Kept {len(kept)}.")
        return 0

    path.write_text("\n".join(json.dumps(x) for x in kept) + ("\n" if kept else ""), encoding="utf-8")
    if removed_ids:
        print("Removed:")
        for r in sorted(set(removed_ids)):
            meta = removed_meta.get(r, {})
            keys = ", ".join(meta.get("keys", []))
            name = meta.get("name", "")
            print(f"  - {r} | {name} | keys: {keys}")
    if kept_ids:
        print("Kept:")
        for k in sorted(set(kept_ids)):
            meta = kept_meta.get(k, {})
            keys = ", ".join(meta.get("keys", []))
            name = meta.get("name", "")
            print(f"  - {k} | {name} | keys: {keys}")
    print(f"Removed {removed} entries. Kept {len(kept)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
