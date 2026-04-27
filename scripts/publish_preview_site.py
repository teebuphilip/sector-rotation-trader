#!/usr/bin/env python3
"""
Publish the private Stockarithm preview site bundle to the separate stockarithm-preview repo.

This is for private Vercel review only. It intentionally includes public + premium/internal
static artifacts that should never be pushed to stockarithm-site.

Default behavior is dry-run. Use --push to commit and push.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from build_vercel_preview_site import build

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REMOTE = os.getenv("PREVIEW_SITE_REMOTE", "https://github.com/teebuphilip/stockarithm-preview.git")
DEFAULT_BRANCH = os.getenv("PREVIEW_SITE_BRANCH", "main")
DEFAULT_GIT_NAME = os.getenv("PREVIEW_SITE_GIT_NAME", "Teebu Philip")
DEFAULT_GIT_EMAIL = os.getenv("PREVIEW_SITE_GIT_EMAIL", "teebu.philip@gmail.com")


def run(cmd: list[str], cwd: Path | None = None, dry_run: bool = False) -> None:
    label = " ".join(cmd)
    where = f" (cwd={cwd})" if cwd else ""
    if dry_run:
        print(f"[dry-run] {label}{where}")
        return
    print(f"[run] {label}{where}")
    subprocess.run(cmd, cwd=cwd, check=True)


def load_run_date() -> str:
    path = ROOT / "docs" / "data" / "public" / "daily.json"
    if not path.exists():
        return "unknown-date"
    try:
        import json

        data = json.loads(path.read_text(encoding="utf-8"))
        return str(data.get("run_date") or "unknown-date")
    except Exception:
        return "unknown-date"


def prepare_repo(repo_dir: Path, remote_url: str, branch: str, dry_run: bool) -> None:
    if repo_dir.exists() and (repo_dir / ".git").exists():
        status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_dir, text=True).strip()
        if status:
            raise SystemExit(f"preview repo checkout has uncommitted changes:\n{status}")
        run(["git", "fetch", "origin", branch], cwd=repo_dir, dry_run=dry_run)
        run(["git", "checkout", branch], cwd=repo_dir, dry_run=dry_run)
        run(["git", "pull", "--ff-only", "origin", branch], cwd=repo_dir, dry_run=dry_run)
    else:
        repo_dir.parent.mkdir(parents=True, exist_ok=True)
        try:
            run(["git", "clone", "--branch", branch, remote_url, str(repo_dir)], dry_run=dry_run)
        except subprocess.CalledProcessError:
            run(["git", "clone", remote_url, str(repo_dir)], dry_run=dry_run)
            run(["git", "checkout", "-B", branch], cwd=repo_dir, dry_run=dry_run)


def clear_repo_contents(repo_dir: Path) -> None:
    for child in repo_dir.iterdir():
        if child.name == ".git":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def copy_tree(src_dir: Path, dest_dir: Path) -> None:
    for item in src_dir.iterdir():
        target = dest_dir / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def publish(repo_dir: Path, branch: str, message: str, git_name: str, git_email: str, dry_run: bool, push: bool) -> None:
    run(["git", "add", "-A"], cwd=repo_dir, dry_run=dry_run)
    if dry_run:
        run(["git", "status", "--short"], cwd=repo_dir, dry_run=True)
        return
    status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_dir, text=True).strip()
    if not status:
        print("[publish] no preview site changes to commit")
        return
    run(["git", "config", "user.name", git_name], cwd=repo_dir)
    run(["git", "config", "user.email", git_email], cwd=repo_dir)
    run(["git", "commit", "-m", message], cwd=repo_dir)
    if push:
        run(["git", "push", "origin", branch], cwd=repo_dir)
    else:
        print("[publish] committed locally but not pushed; rerun with --push or push manually")


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish Stockarithm preview site artifacts to stockarithm-preview.")
    parser.add_argument("--repo-dir", default="../stockarithm-preview", help="Local checkout path for stockarithm-preview")
    parser.add_argument("--remote-url", default=DEFAULT_REMOTE)
    parser.add_argument("--branch", default=DEFAULT_BRANCH)
    parser.add_argument("--git-name", default=DEFAULT_GIT_NAME)
    parser.add_argument("--git-email", default=DEFAULT_GIT_EMAIL)
    parser.add_argument("--push", action="store_true", help="Commit and push to preview repo")
    parser.add_argument("--dry-run", action="store_true", help="Build/validate a temp preview bundle only")
    args = parser.parse_args()

    run_date = load_run_date()
    message = f"Publish Stockarithm preview site for {run_date}"

    if args.dry_run:
        with tempfile.TemporaryDirectory(prefix="stockarithm-preview-site-") as tmp:
            out_dir = Path(tmp) / "preview"
            build(out_dir)
            count = sum(1 for p in out_dir.rglob("*") if p.is_file())
            print(f"[dry-run] built {count} files for preview publish in {out_dir}")
        return 0

    with tempfile.TemporaryDirectory(prefix="stockarithm-preview-build-") as tmp:
        bundle_dir = Path(tmp) / "bundle"
        build(bundle_dir)

        repo_dir = Path(args.repo_dir).expanduser().resolve()
        prepare_repo(repo_dir, args.remote_url, args.branch, dry_run=False)
        clear_repo_contents(repo_dir)
        copy_tree(bundle_dir, repo_dir)
        publish(repo_dir, args.branch, message, args.git_name, args.git_email, dry_run=False, push=args.push)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
