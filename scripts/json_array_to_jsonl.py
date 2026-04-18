#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from typing import Any


def _extract_balanced_objects(text: str) -> list[dict[str, Any]]:
    items = []
    depth = 0
    start = None
    in_string = False
    escape = False

    for i, ch in enumerate(text):
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue

        if ch == '"':
            in_string = True
        elif ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            if depth > 0:
                depth -= 1
                if depth == 0 and start is not None:
                    raw = text[start:i + 1]
                    try:
                        obj = json.loads(raw)
                    except json.JSONDecodeError:
                        start = None
                        continue
                    if isinstance(obj, dict):
                        items.append(obj)
                    start = None
    return items


def parse_items(text: str) -> list[dict[str, Any]]:
    try:
        data = json.loads(text)
        if isinstance(data, list):
            return [x for x in data if isinstance(x, dict)]
        if isinstance(data, dict):
            return [data]
    except json.JSONDecodeError:
        pass
    return _extract_balanced_objects(text)


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: json_array_to_jsonl.py RESPONSE_JSON [model] [provider] [limit]", file=sys.stderr)
        return 2

    src = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else ""
    provider = sys.argv[3] if len(sys.argv) > 3 else ""
    limit = int(sys.argv[4]) if len(sys.argv) > 4 else 0

    raw = open(src, encoding="utf-8").read().strip()
    obj = json.loads(raw)
    if isinstance(obj, dict) and "error" in obj:
        raise SystemExit(f"API error: {obj['error']}")

    if "choices" in obj:
        text = obj["choices"][0]["message"]["content"]
    elif "content" in obj:
        text = obj["content"][0]["text"]
    else:
        text = raw

    items = parse_items(text)
    if limit:
        items = items[:limit]
    if not items:
        raise SystemExit("No JSON objects parsed from model response")

    for item in items:
        if provider:
            item["source_provider"] = provider
        if model:
            item["source_model"] = model
        print(json.dumps(item, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
