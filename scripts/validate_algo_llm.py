#!/usr/bin/env python3
"""
LLM validation pass: check if code matches sliced spec and adapter contract.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict

from langchain_openai import ChatOpenAI


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--spec", required=True)
    parser.add_argument("--out-report", required=True)
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on FAIL")
    args = parser.parse_args()

    code = _read_text(Path(args.file))
    spec = _read_text(Path(args.spec))

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    llm = ChatOpenAI(model=model, temperature=0.0)

    prompt = (
        "You are validating an algo implementation against a sliced spec.\n"
        "Return ONLY JSON in the format: {\"pass\": bool, \"issues\": [..]}.\n"
        "Treat RISK_ON as BUY, RISK_OFF as SELL, HOLD as no action.\n"
        "PASS if code imports the correct adapter, uses adapter output columns, "
        "and the signal/alloc logic follows the spec intent. Be strict on logic, "
        "but do NOT fail just because signal names are RISK_ON/RISK_OFF/HOLD.\n\n"
        f"SLICED_SPEC:\n{spec}\n\n"
        f"CODE:\n{code}\n"
    )
    resp = llm.invoke(prompt)
    text = resp.content.strip()
    if text.startswith("```"):
        parts = text.split("```")
        if len(parts) >= 2:
            text = parts[1]
            if text.lstrip().startswith("json"):
                text = "\n".join(text.splitlines()[1:])
            text = text.strip()
    try:
        verdict = json.loads(text)
    except Exception:
        verdict = {"pass": False, "issues": ["failed_to_parse_llm_json"], "raw": text}

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
        "file": str(args.file),
        "spec": str(args.spec),
        "model": model,
        "verdict": verdict,
        "usage": usage,
        "cost_usd": cost,
    }
    _write_json(Path(args.out_report), report)
    print(f"[validate-llm][openai] cost=${cost:.6f}")

    passed = bool(verdict.get("pass"))
    if passed:
        print("PASS")
        return 0
    print("FAIL")
    for issue in verdict.get("issues", []) or []:
        print(f"- {issue}")
    return 2 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
