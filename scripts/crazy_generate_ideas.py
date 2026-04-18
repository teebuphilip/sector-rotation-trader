#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path


def _today_iso() -> str:
    return dt.date.today().isoformat()


def _validate_jsonl(text: str, label: str) -> None:
    if not text.strip():
        raise RuntimeError(f"Empty output for {label}")
    for idx, line in enumerate(text.splitlines(), start=1):
        s = line.strip()
        if not s:
            continue
        try:
            json.loads(s)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Invalid JSONL in {label} line {idx}: {e}") from e


def _run(cmd: list[str], env: dict[str, str], label: str) -> str:
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed ({label}): {proc.stderr.strip() or '(no stderr)'}")
    _validate_jsonl(proc.stdout, label)
    return proc.stdout


def _write_error(run_dir: Path, label: str, err: Exception) -> None:
    err_dir = run_dir / "errors"
    err_dir.mkdir(parents=True, exist_ok=True)
    (err_dir / f"{label}.txt").write_text(str(err) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=_today_iso())
    parser.add_argument("--prompt", default="prompts/crazy_ideas_prompt.txt")
    parser.add_argument("--schema-mode", choices=["standard", "high-action"], default="standard")
    args = parser.parse_args()

    try:
        dt.date.fromisoformat(args.date)
    except ValueError:
        print("❌ Invalid --date, expected YYYY-MM-DD", file=sys.stderr)
        return 2

    repo_root = Path.cwd()
    run_dir = repo_root / "data" / "ideas" / "runs" / args.date
    raw_dir = run_dir / "raw"
    filtered_dir = run_dir / "filtered"
    rejected_dir = run_dir / "rejected"
    raw_dir.mkdir(parents=True, exist_ok=True)
    filtered_dir.mkdir(parents=True, exist_ok=True)
    rejected_dir.mkdir(parents=True, exist_ok=True)
    err_dir = run_dir / "errors"
    err_dir.mkdir(parents=True, exist_ok=True)
    for p in err_dir.glob("*.txt"):
        p.unlink()

    chat_out = raw_dir / f"chatgpt_{args.date}.jsonl"
    claude_out = raw_dir / f"claude_{args.date}.jsonl"
    for stale in [
        chat_out,
        claude_out,
        filtered_dir / f"chatgpt_{args.date}.jsonl",
        filtered_dir / f"claude_{args.date}.jsonl",
        rejected_dir / f"chatgpt_{args.date}.jsonl",
        rejected_dir / f"claude_{args.date}.jsonl",
    ]:
        if stale.exists():
            stale.unlink()

    chat_script = Path("scripts/crazy_generate_chatgpt.sh")
    claude_script = Path("scripts/crazy_generate_claude.sh")
    if not chat_script.exists() or not claude_script.exists():
        print("❌ Missing generator scripts", file=sys.stderr)
        return 2

    env = dict(os.environ)
    env["ERROR_DIR"] = str(run_dir / "errors")
    env["RESPONSE_DIR"] = str(run_dir / "responses")

    success = False

    try:
        chat_stdout = _run(["/bin/bash", str(chat_script), args.prompt], env, "chatgpt")
        chat_out.write_text(chat_stdout)
        # schema gate
        subprocess.run([
            "python", "scripts/crazy_schema_gate.py",
            "--in", str(chat_out),
            "--out", str(filtered_dir / f"chatgpt_{args.date}.jsonl"),
            "--rejects", str(rejected_dir / f"chatgpt_{args.date}.jsonl"),
            "--mode", args.schema_mode,
        ], check=False)
        err_file = err_dir / "chatgpt.txt"
        if err_file.exists():
            err_file.unlink()
        success = True
    except Exception as e:
        _write_error(run_dir, "chatgpt", e)
        chat_out.write_text("")

    try:
        claude_stdout = _run(["/bin/bash", str(claude_script), args.prompt], env, "claude")
        claude_out.write_text(claude_stdout)
        # schema gate
        subprocess.run([
            "python", "scripts/crazy_schema_gate.py",
            "--in", str(claude_out),
            "--out", str(filtered_dir / f"claude_{args.date}.jsonl"),
            "--rejects", str(rejected_dir / f"claude_{args.date}.jsonl"),
            "--mode", args.schema_mode,
        ], check=False)
        err_file = err_dir / "claude.txt"
        if err_file.exists():
            err_file.unlink()
        success = True
    except Exception as e:
        _write_error(run_dir, "claude", e)
        claude_out.write_text("")

    if not success:
        print("❌ Both generators failed. See data/ideas/runs/<date>/errors/", file=sys.stderr)
        return 1

    print(f"✅ Wrote:\n  {chat_out}\n  {claude_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
