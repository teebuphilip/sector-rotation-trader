#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "reports" / "morning_status"
ET = ZoneInfo("America/New_York")

REPO = os.environ.get("GITHUB_REPOSITORY", "teebuphilip/sector-rotation-trader")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

WORKFLOW_CHECKS = {
    "daily_sector_rotation_run": "Daily Sector Rotation Run",
    "preview_site_publish": "Preview Site Publish",
}

FILE_CHECKS = {
    "daily_json_freshness": ROOT / "docs" / "data" / "public" / "daily.json",
    "today_json_freshness": ROOT / "docs" / "comparison" / "today.json",
    "deep_validation_freshness": ROOT / "reports" / "deep_validation" / "latest.json",
}


@dataclass
class CheckResult:
    color: str
    detail: str


def _github_get(url: str) -> dict:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _fetch_recent_runs() -> list[dict]:
    url = f"https://api.github.com/repos/{REPO}/actions/runs?per_page=100"
    data = _github_get(url)
    return data.get("workflow_runs", [])


def _parse_iso(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)


def _check_workflow(runs: list[dict], workflow_name: str, now_utc: datetime) -> CheckResult:
    matching = [run for run in runs if run.get("name") == workflow_name]
    if not matching:
        return CheckResult("RED", f"{workflow_name}: no recent run found")
    latest = matching[0]
    created_at = _parse_iso(latest["created_at"])
    age = now_utc - created_at
    if latest.get("conclusion") != "success":
        return CheckResult(
            "RED",
            f"{workflow_name}: latest run {latest.get('conclusion') or latest.get('status')} at {created_at.astimezone(ET).strftime('%Y-%m-%d %I:%M %p ET')}",
        )
    if age > timedelta(hours=12):
        return CheckResult(
            "RED",
            f"{workflow_name}: latest success too old ({created_at.astimezone(ET).strftime('%Y-%m-%d %I:%M %p ET')})",
        )
    return CheckResult("GREEN", f"{workflow_name}: success at {created_at.astimezone(ET).strftime('%Y-%m-%d %I:%M %p ET')}")


def _parse_json_freshness(path: Path, now_et: datetime) -> CheckResult:
    if not path.exists():
        return CheckResult("RED", f"{path.name}: file missing")
    try:
        payload = json.loads(path.read_text())
    except Exception as exc:  # pragma: no cover
        return CheckResult("RED", f"{path.name}: unreadable JSON ({exc})")

    value = None
    for key in ("generated_at", "run_date", "as_of", "date"):
        if isinstance(payload, dict) and payload.get(key):
            value = str(payload[key])
            break
    if not value:
        return CheckResult("RED", f"{path.name}: no freshness field")

    try:
        if "T" in value or value.endswith("Z"):
            stamp = _parse_iso(value).astimezone(ET)
            if now_et - stamp > timedelta(hours=36):
                return CheckResult("RED", f"{path.name}: stale timestamp {stamp.strftime('%Y-%m-%d %I:%M %p ET')}")
            return CheckResult("GREEN", f"{path.name}: fresh timestamp {stamp.strftime('%Y-%m-%d %I:%M %p ET')}")
        stamp_date = datetime.fromisoformat(value).date()
        if (now_et.date() - stamp_date).days > 2:
            return CheckResult("RED", f"{path.name}: stale date {stamp_date.isoformat()}")
        return CheckResult("GREEN", f"{path.name}: fresh date {stamp_date.isoformat()}")
    except Exception as exc:  # pragma: no cover
        return CheckResult("RED", f"{path.name}: bad freshness field {value!r} ({exc})")


def _write_outputs(report: dict, now_et: datetime) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    day_key = now_et.strftime("%Y-%m-%d")
    latest_json = OUT_DIR / "latest.json"
    latest_md = OUT_DIR / "latest.md"
    dated_json = OUT_DIR / f"{day_key}.json"
    dated_md = OUT_DIR / f"{day_key}.md"

    json_text = json.dumps(report, indent=2) + "\n"
    md_lines = [f"OVERNIGHT STATUS: {report['overnight_status']}", ""]
    for key, result in report["checks"].items():
        md_lines.append(f"- {result['label']}: {result['color']}")
    if report["red_reasons"]:
        md_lines.extend(["", "Reasons:"])
        for reason in report["red_reasons"]:
            md_lines.append(f"- {reason}")
    md_text = "\n".join(md_lines) + "\n"

    for path in (latest_json, dated_json):
        path.write_text(json_text)
    for path in (latest_md, dated_md):
        path.write_text(md_text)


def main() -> int:
    now_utc = datetime.now(UTC)
    now_et = now_utc.astimezone(ET)

    try:
        runs = _fetch_recent_runs()
    except Exception as exc:
        report = {
            "overnight_status": "RED",
            "generated_at_utc": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "generated_at_et": now_et.strftime("%Y-%m-%d %I:%M %p ET"),
            "checks": {},
            "red_reasons": [f"GitHub Actions query failed: {exc}"],
        }
        _write_outputs(report, now_et)
        return 1

    checks: dict[str, dict[str, str]] = {}
    red_reasons: list[str] = []

    for key, workflow_name in WORKFLOW_CHECKS.items():
        result = _check_workflow(runs, workflow_name, now_utc)
        checks[key] = {"label": workflow_name, "color": result.color, "detail": result.detail}
        if result.color == "RED":
            red_reasons.append(result.detail)

    for key, path in FILE_CHECKS.items():
        result = _parse_json_freshness(path, now_et)
        checks[key] = {"label": path.name + " freshness", "color": result.color, "detail": result.detail}
        if result.color == "RED":
            red_reasons.append(result.detail)

    report = {
        "overnight_status": "GREEN" if not red_reasons else "RED",
        "generated_at_utc": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generated_at_et": now_et.strftime("%Y-%m-%d %I:%M %p ET"),
        "checks": checks,
        "red_reasons": red_reasons,
    }
    _write_outputs(report, now_et)
    return 0 if not red_reasons else 1


if __name__ == "__main__":
    raise SystemExit(main())
