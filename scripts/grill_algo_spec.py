#!/usr/bin/env python3
"""
Grill algo spec: normalize a markdown idea into a strict JSON spec and flag gaps.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List

from langchain_openai import ChatOpenAI


REQUIRED_FIELDS = [
    "id",
    "name",
    "frequency",
    "universe",
    "data_sources",
    "signal_logic",
    "entry_exit",
    "position_sizing",
]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _acceptance_complete(spec: Dict[str, Any]) -> bool:
    for key in REQUIRED_FIELDS:
        if key not in spec or spec[key] in (None, "", [], {}):
            return False
    # basic nested checks
    if not isinstance(spec.get("universe"), list) or len(spec["universe"]) == 0:
        return False
    if "entry" not in spec.get("entry_exit", {}) or "exit" not in spec.get("entry_exit", {}):
        return False
    if "trigger" not in spec.get("signal_logic", {}):
        return False
    return True


def _find_missing(spec: Dict[str, Any]) -> List[str]:
    missing = []
    for key in REQUIRED_FIELDS:
        if key not in spec or spec[key] in (None, "", [], {}):
            missing.append(key)
    if "entry_exit" in spec:
        if "entry" not in spec["entry_exit"]:
            missing.append("entry_exit.entry")
        if "exit" not in spec["entry_exit"]:
            missing.append("entry_exit.exit")
    if "signal_logic" in spec and "trigger" not in spec["signal_logic"]:
        missing.append("signal_logic.trigger")
    return missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec-file", required=True)
    parser.add_argument("--out-spec", required=True, dest="out_spec")
    parser.add_argument("--out-report", required=True, dest="out_report")
    args = parser.parse_args()

    spec_path = Path(args.spec_file)
    if not spec_path.exists():
        raise SystemExit(f"Spec file not found: {spec_path}")

    raw = _read_text(spec_path)
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    llm = ChatOpenAI(model=model, temperature=0.1)

    prompt = (
        "Normalize the following algo idea into a strict JSON spec. "
        "Return ONLY JSON. Required keys: "
        "id, name, frequency, universe (list), data_sources (object), "
        "signal_logic (object with trigger), entry_exit (entry+exit), "
        "position_sizing (object), required_keys (list). "
        "Do not invent data sources; if unknown, leave empty values.\n\n"
        f"IDEA:\n{raw}\n"
    )
    resp = llm.invoke(prompt)
    text = resp.content.strip()
    # Strip fenced code blocks if present
    if text.startswith("```"):
        parts = text.split("```")
        if len(parts) >= 2:
            text = parts[1]
            if text.lstrip().startswith("json"):
                text = "\n".join(text.splitlines()[1:])
            text = text.strip()
    try:
        spec = json.loads(text)
    except Exception:
        spec = {"error": "failed_to_parse_json", "raw": text}

    issues = []
    if "error" in spec:
        issues.append("parse_error")
        complete = False
    else:
        missing = _find_missing(spec)
        if missing:
            issues.extend([f"missing:{m}" for m in missing])
        complete = _acceptance_complete(spec)

    usage = {}
    meta = getattr(resp, "response_metadata", None) or {}
    token_usage = meta.get("token_usage") or {}
    if token_usage:
        usage = {
            "input_tokens": token_usage.get("input_tokens") or token_usage.get("prompt_tokens") or 0,
            "output_tokens": token_usage.get("output_tokens") or token_usage.get("completion_tokens") or 0,
        }
    in_rate = float(os.getenv("OPENAI_INPUT_PER_MTOK", "2.50"))
    out_rate = float(os.getenv("OPENAI_OUTPUT_PER_MTOK", "10.00"))
    cost = (usage.get("input_tokens", 0) * in_rate + usage.get("output_tokens", 0) * out_rate) / 1_000_000

    report = {
        "spec_file": str(spec_path),
        "complete": complete,
        "issues": issues,
        "usage": usage,
        "cost_usd": cost,
    }

    _write_json(Path(args.out_spec), spec)
    _write_json(Path(args.out_report), report)
    print(f"[grill][openai] cost=${cost:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
