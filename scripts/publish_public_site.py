#!/usr/bin/env python3
"""
Publish the public Stockarithm static site to the separate stockarithm-site repo.

This is allowlist-only by design. Never mirror docs/ wholesale.

Default behavior is dry-run. Use --push to commit and push.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REMOTE = os.getenv("PUBLIC_SITE_REMOTE", "https://github.com/teebuphilip/stockarithm-site.git")
DEFAULT_BRANCH = os.getenv("PUBLIC_SITE_BRANCH", "main")
DEFAULT_GIT_NAME = os.getenv("PUBLIC_SITE_GIT_NAME", "Teebu Philip")
DEFAULT_GIT_EMAIL = os.getenv("PUBLIC_SITE_GIT_EMAIL", "teebu.philip@gmail.com")

ALLOWLIST_FILES = [
    "docs/index.html",
    "docs/landing.html",
    "docs/leaderboard.html",
    "docs/families.html",
    "docs/daily.html",
    "docs/premium.html",
    "docs/legal.html",
    "docs/app.html",
    "docs/signals/lookup.html",
]

ALLOWLIST_DIRS = [
    "docs/blog",
    "docs/data/public",
]

BANNED_PATH_PARTS = {
    "data/crazy",
    "data/normal",
    "data/ideas",
    "data/algos_codegen",
    "crazy/",
    "normal/",
    "scripts/",
    "backend/",
    "private_artifacts",
    "reports/",
    "state.json",
    "docs/algos",
    "docs/normal",
    "docs/crazy",
    "docs/ledgers",
    "docs/signals/_sectors",
}

BANNED_TEXT = [
    "STRIPE_SECRET_KEY",
    "STRIPE_WEBHOOK_SECRET",
    "JWT_SECRET",
    "ANTHROPIC_API_KEY",
    "OPENAI_API_KEY",
    "FRED_API_KEY",
    "POLYGON_API_KEY",
    "PRIVATE_ARTIFACT_DIR",
    "data/crazy/state",
    "data/normal/state",
    "data/ideas/runs",
    "backend.stockarithm_api",
]

TEXT_SUFFIXES = {".html", ".json", ".js", ".css", ".txt", ".md", ".xml", ".csv"}


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
        return str(json.loads(path.read_text(encoding="utf-8")).get("run_date") or "unknown-date")
    except Exception:
        return "unknown-date"


def copy_allowed(publish_dir: Path) -> None:
    for rel in ALLOWLIST_FILES:
        src = ROOT / rel
        if not src.exists():
            raise SystemExit(f"allowlisted file missing: {rel}")
        dest = publish_dir / Path(rel).relative_to("docs")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    for rel in ALLOWLIST_DIRS:
        src = ROOT / rel
        if not src.exists():
            raise SystemExit(f"allowlisted dir missing: {rel}")
        dest = publish_dir / Path(rel).relative_to("docs")
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src, dest, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc"))

    (publish_dir / "CNAME").write_text("stockarithm.com\n", encoding="utf-8")
    (publish_dir / ".nojekyll").write_text("", encoding="utf-8")


def validate_publish_dir(publish_dir: Path) -> None:
    failures: list[str] = []
    for path in publish_dir.rglob("*"):
        if path.is_dir():
            continue
        rel = path.relative_to(publish_dir).as_posix()
        for banned in BANNED_PATH_PARTS:
            if banned in rel:
                failures.append(f"banned path: {rel} contains {banned}")
        if path.suffix.lower() in TEXT_SUFFIXES:
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            for needle in BANNED_TEXT:
                if needle in text:
                    failures.append(f"banned text: {rel} contains {needle}")
    if failures:
        raise SystemExit("public publish validation failed:\n" + "\n".join(failures[:50]))


def prepare_repo(repo_dir: Path, remote_url: str, branch: str, dry_run: bool) -> None:
    if repo_dir.exists() and (repo_dir / ".git").exists():
        status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_dir, text=True).strip()
        if status:
            raise SystemExit(f"public repo checkout has uncommitted changes:\n{status}")
        run(["git", "fetch", "origin", branch], cwd=repo_dir, dry_run=dry_run)
        run(["git", "checkout", branch], cwd=repo_dir, dry_run=dry_run)
        run(["git", "pull", "--ff-only", "origin", branch], cwd=repo_dir, dry_run=dry_run)
    else:
        repo_dir.parent.mkdir(parents=True, exist_ok=True)
        try:
            run(["git", "clone", "--branch", branch, remote_url, str(repo_dir)], dry_run=dry_run)
        except subprocess.CalledProcessError:
            # New empty GitHub repos do not have main yet. Clone default, then create it.
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


def publish(repo_dir: Path, branch: str, message: str, git_name: str, git_email: str, dry_run: bool, push: bool) -> None:
    run(["git", "add", "-A"], cwd=repo_dir, dry_run=dry_run)
    if dry_run:
        run(["git", "status", "--short"], cwd=repo_dir, dry_run=True)
        return
    status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_dir, text=True).strip()
    if not status:
        print("[publish] no public site changes to commit")
        return
    run(["git", "config", "user.name", git_name], cwd=repo_dir)
    run(["git", "config", "user.email", git_email], cwd=repo_dir)
    run(["git", "commit", "-m", message], cwd=repo_dir)
    if push:
        run(["git", "push", "origin", branch], cwd=repo_dir)
    else:
        print("[publish] committed locally but not pushed; rerun with --push or push manually")


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish allowlisted public Stockarithm site artifacts to stockarithm-site.")
    parser.add_argument("--repo-dir", default="../stockarithm-site", help="Local checkout path for stockarithm-site")
    parser.add_argument("--remote-url", default=DEFAULT_REMOTE)
    parser.add_argument("--branch", default=DEFAULT_BRANCH)
    parser.add_argument("--git-name", default=DEFAULT_GIT_NAME)
    parser.add_argument("--git-email", default=DEFAULT_GIT_EMAIL)
    parser.add_argument("--push", action="store_true", help="Commit and push to public repo")
    parser.add_argument("--dry-run", action="store_true", help="Build/validate a temp publish bundle only")
    args = parser.parse_args()

    run_date = load_run_date()
    message = f"Publish Stockarithm public site for {run_date}"

    if args.dry_run:
        with tempfile.TemporaryDirectory(prefix="stockarithm-public-site-") as tmp:
            publish_dir = Path(tmp) / "site"
            publish_dir.mkdir(parents=True)
            copy_allowed(publish_dir)
            validate_publish_dir(publish_dir)
            count = sum(1 for p in publish_dir.rglob("*") if p.is_file())
            print(f"[dry-run] validated {count} files for public publish in {publish_dir}")
        return 0

    repo_dir = Path(args.repo_dir).expanduser().resolve()
    prepare_repo(repo_dir, args.remote_url, args.branch, dry_run=False)
    clear_repo_contents(repo_dir)
    copy_allowed(repo_dir)
    validate_publish_dir(repo_dir)
    publish(repo_dir, args.branch, message, args.git_name, args.git_email, dry_run=False, push=args.push)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
