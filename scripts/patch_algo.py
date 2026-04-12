#!/usr/bin/env python3
"""
Patch an algo file by only editing between marker blocks.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from langchain_openai import ChatOpenAI


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _extract_between(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0]


def _replace_between(text: str, start: str, end: str, replacement: str) -> str:
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return before + start + replacement + end + after


def _normalize_markers(text: str) -> str:
    lines = text.splitlines()
    fixed = []
    for line in lines:
        raw = line.strip()
        if raw in ("# === SIGNAL_LOGIC_START ===:", "# === SIGNAL_LOGIC_START ==="):
            fixed.append("        # === SIGNAL_LOGIC_START ===")
            continue
        if raw in ("# === SIGNAL_LOGIC_END ===:", "# === SIGNAL_LOGIC_END ==="):
            fixed.append("        # === SIGNAL_LOGIC_END ===")
            continue
        if raw in ("# === ALLOCATION_LOGIC_START ===:", "# === ALLOCATION_LOGIC_START ==="):
            fixed.append("        # === ALLOCATION_LOGIC_START ===")
            continue
        if raw in ("# === ALLOCATION_LOGIC_END ===:", "# === ALLOCATION_LOGIC_END ==="):
            fixed.append("        # === ALLOCATION_LOGIC_END ===")
            continue
        fixed.append(line)
    return "\n".join(fixed)


def _reindent_blocks(text: str) -> str:
    lines = text.splitlines()
    out = []
    in_signal = False
    in_alloc = False
    for line in lines:
        raw = line.strip()
        if raw == "# === SIGNAL_LOGIC_START ===":
            in_signal = True
            out.append("        # === SIGNAL_LOGIC_START ===")
            continue
        if raw == "# === SIGNAL_LOGIC_END ===":
            in_signal = False
            out.append("        # === SIGNAL_LOGIC_END ===")
            continue
        if raw == "# === ALLOCATION_LOGIC_START ===":
            in_alloc = True
            out.append("        # === ALLOCATION_LOGIC_START ===")
            continue
        if raw == "# === ALLOCATION_LOGIC_END ===":
            in_alloc = False
            out.append("        # === ALLOCATION_LOGIC_END ===")
            continue
        if in_signal or in_alloc:
            if raw == "":
                out.append("")
            else:
                out.append("        " + raw)
        else:
            out.append(line)
    return "\n".join(out)


def _strip_fences(text: str) -> str:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        parts = cleaned.split("```")
        if len(parts) >= 2:
            cleaned = parts[1]
            if cleaned.lstrip().startswith("python"):
                cleaned = "\n".join(cleaned.splitlines()[1:])
            cleaned = cleaned.strip()
    return cleaned


def _indent_block(text: str, spaces: int = 8) -> str:
    indent = " " * spaces
    lines = text.splitlines()
    out = []
    for line in lines:
        if line.strip() == "":
            out.append("")
        else:
            out.append(indent + line.lstrip())
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--spec", required=True)
    parser.add_argument("--out-report", required=False, default="")
    parser.add_argument("--issues", required=False, default="")
    args = parser.parse_args()

    path = Path(args.file)
    spec = Path(args.spec).read_text(encoding="utf-8")
    code = _read(path)

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    llm = ChatOpenAI(model=model, temperature=0.0)

    signal_block = _extract_between(code, "# === SIGNAL_LOGIC_START ===", "# === SIGNAL_LOGIC_END ===")
    alloc_block = _extract_between(code, "# === ALLOCATION_LOGIC_START ===", "# === ALLOCATION_LOGIC_END ===")

    issues_text = ""
    if args.issues:
        issues_text = f"\nKNOWN_ISSUES:\n{args.issues}\n"

    prompt = (
        "Patch ONLY the logic inside the blocks. Return two sections: "
        "SIGNAL_BLOCK and ALLOCATION_BLOCK. Do not add any imports or change structure. "
        "Return plain Python only (NO markdown, NO code fences). "
        "Implement exit logic from entry_exit (e.g., time-based or threshold-based). "
        "Use signals RISK_ON, RISK_OFF, or HOLD consistently. "
        "Allocation must return {} for HOLD to avoid None. "
        "Never modify marker lines.\n\n"
        f"SPEC:\n{spec}\n\n"
        f"{issues_text}\n"
        f"SIGNAL_BLOCK:\n{signal_block}\n\n"
        f"ALLOCATION_BLOCK:\n{alloc_block}\n"
    )
    resp = llm.invoke(prompt)
    text = resp.content
    if "SIGNAL_BLOCK" not in text or "ALLOCATION_BLOCK" not in text:
        raise SystemExit("Patch response missing blocks")

    new_signal = text.split("SIGNAL_BLOCK", 1)[1].split("ALLOCATION_BLOCK", 1)[0]
    new_alloc = text.split("ALLOCATION_BLOCK", 1)[1]
    new_signal = _strip_fences(new_signal).lstrip()
    new_alloc = _strip_fences(new_alloc).lstrip()
    if new_signal.startswith(":"):
        new_signal = new_signal[1:].lstrip()
    if new_alloc.startswith(":"):
        new_alloc = new_alloc[1:].lstrip()
    new_signal = _indent_block(new_signal)
    new_alloc = _indent_block(new_alloc)

    code = _normalize_markers(code)
    code = _replace_between(code, "# === SIGNAL_LOGIC_START ===", "# === SIGNAL_LOGIC_END ===", "\n" + new_signal)
    code = _replace_between(code, "# === ALLOCATION_LOGIC_START ===", "# === ALLOCATION_LOGIC_END ===", "\n" + new_alloc)
    code = _reindent_blocks(code)
    _write(path, code)
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
    print(f"[patch][openai] cost=${cost:.6f}")

    if args.out_report:
        report = {
            "file": str(path),
            "spec": str(args.spec),
            "usage": usage,
            "cost_usd": cost,
        }
        Path(args.out_report).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out_report).write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
