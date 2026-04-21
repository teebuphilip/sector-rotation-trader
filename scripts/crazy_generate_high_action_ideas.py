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
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Invalid JSONL in {label} line {idx}: {exc}") from exc


def _run_capture(cmd: list[str], env: dict[str, str], label: str) -> str:
    print("[run] " + " ".join(cmd))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed ({label}): {proc.stderr.strip() or '(no stderr)'}")
    _validate_jsonl(proc.stdout, label)
    return proc.stdout


def _run(cmd: list[str]) -> None:
    print("[run] " + " ".join(cmd))
    subprocess.run(cmd, check=True)


def _write_error(run_dir: Path, label: str, err: Exception) -> None:
    err_dir = run_dir / "errors"
    err_dir.mkdir(parents=True, exist_ok=True)
    (err_dir / f"{label}.txt").write_text(str(err) + "\n")


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _recent_idea_titles(limit: int = 60) -> list[str]:
    titles: list[str] = []

    product = _load_json(Path("data/product/algos_index.json"))
    for item in product.get("algos", []):
        if isinstance(item, dict) and item.get("name"):
            titles.append(str(item["name"]))

    runs_root = Path("data/ideas/runs")
    if runs_root.exists():
        for run_dir in sorted(runs_root.iterdir(), reverse=True):
            if not run_dir.is_dir():
                continue
            src_dir = run_dir / "deduped"
            if not src_dir.exists():
                src_dir = run_dir / "filtered"
            for src in ("chatgpt", "claude"):
                path = src_dir / f"{src}_{run_dir.name}.jsonl"
                if not path.exists():
                    continue
                for line in path.read_text(encoding="utf-8").splitlines():
                    s = line.strip()
                    if not s:
                        continue
                    try:
                        obj = json.loads(s)
                    except Exception:
                        continue
                    title = obj.get("title") or obj.get("idea")
                    if title:
                        titles.append(str(title))

    seen = set()
    out = []
    for title in titles:
        norm = " ".join(str(title).strip().lower().split())
        if not norm or norm in seen:
            continue
        seen.add(norm)
        out.append(str(title).strip())
        if len(out) >= limit:
            break
    return out


def _prompt_with_history(prompt_path: str, run_dir: Path, label: str) -> str:
    base = Path(prompt_path).read_text(encoding="utf-8")
    existing = _recent_idea_titles()
    if not existing:
        return prompt_path

    appendix = [
        "",
        "ANTI-DUPLICATE CONTEXT",
        "----------------------",
        "The lab already has these existing or recently generated ideas/titles.",
        "Do not output the same idea again with cosmetic wording changes.",
        "If your idea is materially similar to any item below, replace it with a different one.",
        "",
    ]
    appendix.extend(f"- {title}" for title in existing)
    text = base.rstrip() + "\n" + "\n".join(appendix) + "\n"

    tmp = run_dir / f"{label}_prompt_with_history.txt"
    tmp.write_text(text, encoding="utf-8")
    return str(tmp)


def _gate(src: str, date: str) -> None:
    run_dir = Path("data") / "ideas" / "runs" / date
    _run([
        "python", "scripts/crazy_schema_gate.py",
        "--in", str(run_dir / "raw" / f"{src}_{date}.jsonl"),
        "--out", str(run_dir / "filtered" / f"{src}_{date}.jsonl"),
        "--rejects", str(run_dir / "rejected" / f"{src}_{date}.jsonl"),
        "--mode", "high-action",
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=_today_iso())
    parser.add_argument("--chatgpt-prompt", default="prompts/high_action_crazy_ideas_prompt.txt")
    parser.add_argument("--claude-prompt", default="prompts/high_action_crazy_ideas_prompt_claude.txt")
    parser.add_argument("--no-publish", action="store_true", help="Generate/filter only; do not score or publish markdown")
    args = parser.parse_args()

    try:
        dt.date.fromisoformat(args.date)
    except ValueError:
        print("Invalid --date, expected YYYY-MM-DD", file=sys.stderr)
        return 2

    for prompt in [args.chatgpt_prompt, args.claude_prompt]:
        if not Path(prompt).exists():
            print(f"Prompt not found: {prompt}", file=sys.stderr)
            return 2

    run_dir = Path("data") / "ideas" / "runs" / args.date
    raw_dir = run_dir / "raw"
    filtered_dir = run_dir / "filtered"
    rejected_dir = run_dir / "rejected"
    for d in [raw_dir, filtered_dir, rejected_dir, run_dir / "errors", run_dir / "responses"]:
        d.mkdir(parents=True, exist_ok=True)

    for stale in [
        raw_dir / f"chatgpt_{args.date}.jsonl",
        raw_dir / f"claude_{args.date}.jsonl",
        filtered_dir / f"chatgpt_{args.date}.jsonl",
        filtered_dir / f"claude_{args.date}.jsonl",
        rejected_dir / f"chatgpt_{args.date}.jsonl",
        rejected_dir / f"claude_{args.date}.jsonl",
        run_dir / "errors" / "chatgpt.txt",
        run_dir / "errors" / "claude.txt",
    ]:
        if stale.exists():
            stale.unlink()

    env = dict(os.environ)
    env["ERROR_DIR"] = str(run_dir / "errors")
    env["RESPONSE_DIR"] = str(run_dir / "responses")

    chatgpt_prompt = _prompt_with_history(args.chatgpt_prompt, run_dir, "chatgpt")
    claude_prompt = _prompt_with_history(args.claude_prompt, run_dir, "claude")

    success = False

    try:
        chat_stdout = _run_capture(["/bin/bash", "scripts/crazy_generate_chatgpt.sh", chatgpt_prompt], env, "chatgpt")
        (raw_dir / f"chatgpt_{args.date}.jsonl").write_text(chat_stdout)
        _gate("chatgpt", args.date)
        success = True
    except Exception as exc:
        _write_error(run_dir, "chatgpt", exc)
        (raw_dir / f"chatgpt_{args.date}.jsonl").write_text("")

    try:
        claude_stdout = _run_capture(["/bin/bash", "scripts/crazy_generate_claude.sh", claude_prompt], env, "claude")
        (raw_dir / f"claude_{args.date}.jsonl").write_text(claude_stdout)
        _gate("claude", args.date)
        success = True
    except Exception as exc:
        _write_error(run_dir, "claude", exc)
        (raw_dir / f"claude_{args.date}.jsonl").write_text("")

    if not success:
        print(f"Both generators failed. See {run_dir / 'errors'}", file=sys.stderr)
        return 1

    _run(["python", "scripts/dedup_crazy_ideas.py", "--date", args.date])

    if not args.no_publish:
        _run(["python", "scripts/crazy_score_ideas.py", "--date", args.date])
        _run(["python", "scripts/crazy_publish_markdown.py", "--date", args.date])

    print(f"[done] high-action crazy ideas -> {run_dir}")
    print(f"[next] publish dir: {run_dir / 'publish'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
