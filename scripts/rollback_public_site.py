#!/usr/bin/env python3
"""
Rollback helper for the public Stockarithm site repo.

Default strategy is safe: create one or more git revert commits in the public
repo, then optionally push. It does not use reset --hard or force-push.

Examples:
    python scripts/rollback_public_site.py --repo-dir ../stockarithm-site --dry-run
    python scripts/rollback_public_site.py --repo-dir ../stockarithm-site --count 1 --push
    python scripts/rollback_public_site.py --repo-dir ../stockarithm-site --commit abc123 --push --reason "bad public publish"
    python scripts/rollback_public_site.py --remote-url git@github.com:teebuphilip/stockarithm-site.git --push
"""
from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import tempfile
from pathlib import Path

DEFAULT_REMOTE = os.getenv("PUBLIC_SITE_REMOTE", "git@github.com:teebuphilip/stockarithm-site.git")
DEFAULT_BRANCH = os.getenv("PUBLIC_SITE_BRANCH", "main")


def _run(cmd: list[str], cwd: Path | None = None, dry_run: bool = False, check: bool = True) -> subprocess.CompletedProcess[str]:
    printable = " ".join(shlex.quote(part) for part in cmd)
    location = f" (cwd={cwd})" if cwd else ""
    if dry_run:
        print(f"[dry-run] {printable}{location}")
        return subprocess.CompletedProcess(cmd, 0, "", "")
    print(f"[run] {printable}{location}")
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=check)


def _git(repo: Path, args: list[str], dry_run: bool = False, check: bool = True) -> subprocess.CompletedProcess[str]:
    return _run(["git", *args], cwd=repo, dry_run=dry_run, check=check)


def _stdout(repo: Path, args: list[str]) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def _ensure_repo(repo: Path, branch: str) -> None:
    if not (repo / ".git").exists():
        raise SystemExit(f"not a git repo: {repo}")
    status = _stdout(repo, ["status", "--porcelain"])
    if status:
        raise SystemExit(f"public repo has uncommitted changes; refusing rollback:\n{status}")
    current_branch = _stdout(repo, ["branch", "--show-current"])
    if current_branch != branch:
        raise SystemExit(f"public repo is on branch {current_branch!r}, expected {branch!r}")


def _clone_if_needed(repo_dir: str | None, remote_url: str, branch: str, dry_run: bool) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    if repo_dir:
        return Path(repo_dir).expanduser().resolve(), None
    tmp = tempfile.TemporaryDirectory(prefix="stockarithm-site-rollback-")
    repo = Path(tmp.name) / "stockarithm-site"
    _run(["git", "clone", "--branch", branch, remote_url, str(repo)], dry_run=dry_run)
    return repo, tmp


def _commits_to_revert(repo: Path, commit: str | None, count: int) -> list[str]:
    if commit:
        return [commit]
    raw = _stdout(repo, ["rev-list", f"--max-count={count}", "HEAD"])
    return [line.strip() for line in raw.splitlines() if line.strip()]


def _show_plan(repo: Path, commits: list[str]) -> None:
    print("[plan] public rollback will revert these commits, newest first:")
    for commit in commits:
        line = _stdout(repo, ["log", "--format=%h %cI %s", "-n", "1", commit])
        print(f"  - {line}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Safely rollback the public Stockarithm site repo with git revert.")
    parser.add_argument("--repo-dir", help="Existing local checkout of stockarithm-site. If omitted, clone --remote-url to a temp dir.")
    parser.add_argument("--remote-url", default=DEFAULT_REMOTE, help=f"Public site git remote. Default: {DEFAULT_REMOTE}")
    parser.add_argument("--branch", default=DEFAULT_BRANCH, help=f"Public site branch. Default: {DEFAULT_BRANCH}")
    parser.add_argument("--commit", help="Specific commit to revert. Defaults to HEAD or last --count commits.")
    parser.add_argument("--count", type=int, default=1, help="Number of latest commits to revert when --commit is not set. Default: 1")
    parser.add_argument("--reason", default="rollback public site publish", help="Reason added to the revert commit message.")
    parser.add_argument("--push", action="store_true", help="Push rollback commit(s) to origin after revert.")
    parser.add_argument("--dry-run", action="store_true", help="Print the plan and commands without changing anything.")
    args = parser.parse_args()

    if args.count < 1:
        raise SystemExit("--count must be >= 1")

    repo, tmp = _clone_if_needed(args.repo_dir, args.remote_url, args.branch, args.dry_run)
    try:
        if args.dry_run and not repo.exists():
            print(f"[dry-run] would inspect repo at {repo}")
            return 0
        _ensure_repo(repo, args.branch)
        _git(repo, ["fetch", "origin", args.branch], dry_run=args.dry_run)
        if not args.dry_run:
            local_head = _stdout(repo, ["rev-parse", "HEAD"])
            remote_head = _stdout(repo, ["rev-parse", f"origin/{args.branch}"])
            if local_head != remote_head:
                raise SystemExit(f"local public repo is not at origin/{args.branch}; pull or clone fresh before rollback")
        commits = _commits_to_revert(repo, args.commit, args.count)
        _show_plan(repo, commits)

        for commit in commits:
            _git(repo, ["revert", "--no-commit", commit], dry_run=args.dry_run)

        _git(
            repo,
            ["commit", "-m", "Rollback public site publish", "-m", args.reason],
            dry_run=args.dry_run,
        )

        if args.push:
            _git(repo, ["push", "origin", args.branch], dry_run=args.dry_run)
        else:
            print("[rollback] not pushed. Re-run with --push after reviewing the public repo log.")
        return 0
    finally:
        if tmp is not None:
            tmp.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
