#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import urllib.parse
import urllib.request
from urllib.error import HTTPError
from datetime import datetime
from pathlib import Path
from functools import lru_cache
from zoneinfo import ZoneInfo


FOLDER_ID = os.environ.get("GOOGLE_DRIVE_FOLDER_ID", "")
ACCESS_TOKEN = os.environ.get("GDRIVE_ACCESS_TOKEN", "")
OAUTH_CLIENT_ID = os.environ.get("GOOGLE_DRIVE_OAUTH_CLIENT_ID", "")
OAUTH_CLIENT_SECRET = os.environ.get("GOOGLE_DRIVE_OAUTH_CLIENT_SECRET", "")
OAUTH_REFRESH_TOKEN = os.environ.get("GOOGLE_DRIVE_OAUTH_REFRESH_TOKEN", "")
ET_REPORT_DATE = os.environ.get("ET_REPORT_DATE") or datetime.now(ZoneInfo("America/New_York")).date().isoformat()


def _api_request(url: str, method: str = "GET", data: bytes | None = None, content_type: str | None = None) -> dict:
    req = urllib.request.Request(url, method=method, data=data)
    req.add_header("Authorization", f"Bearer {_access_token()}")
    if content_type:
        req.add_header("Content-Type", content_type)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else {}
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        message = f"HTTP {exc.code} {exc.reason}"
        if body:
            message += f": {body}"
        raise RuntimeError(message) from exc


def _exchange_refresh_token() -> str:
    if not OAUTH_CLIENT_ID or not OAUTH_CLIENT_SECRET or not OAUTH_REFRESH_TOKEN:
        raise RuntimeError(
            "Missing OAuth credentials. Set GOOGLE_DRIVE_OAUTH_CLIENT_ID, "
            "GOOGLE_DRIVE_OAUTH_CLIENT_SECRET, and GOOGLE_DRIVE_OAUTH_REFRESH_TOKEN."
        )
    payload = urllib.parse.urlencode(
        {
            "client_id": OAUTH_CLIENT_ID,
            "client_secret": OAUTH_CLIENT_SECRET,
            "refresh_token": OAUTH_REFRESH_TOKEN,
            "grant_type": "refresh_token",
        }
    ).encode("utf-8")
    req = urllib.request.Request("https://oauth2.googleapis.com/token", method="POST", data=payload)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        message = f"HTTP {exc.code} {exc.reason}"
        if body:
            message += f": {body}"
        raise RuntimeError(message) from exc
    token = data.get("access_token")
    if not token:
        raise RuntimeError(f"OAuth token response missing access_token: {data}")
    return token


@lru_cache(maxsize=1)
def _access_token() -> str:
    if ACCESS_TOKEN:
        return ACCESS_TOKEN
    return _exchange_refresh_token()


def _find_existing(remote_name: str) -> str | None:
    query = f"name = '{remote_name}' and '{FOLDER_ID}' in parents and trashed = false"
    params = urllib.parse.urlencode(
        {
            "q": query,
            "fields": "files(id,name)",
            "pageSize": 10,
            "supportsAllDrives": "true",
            "includeItemsFromAllDrives": "true",
        }
    )
    data = _api_request(f"https://www.googleapis.com/drive/v3/files?{params}")
    files = data.get("files", [])
    return files[0]["id"] if files else None


def _multipart_body(remote_name: str, content: bytes, mime_type: str) -> tuple[bytes, str]:
    boundary = "stockarithm-boundary"
    metadata = json.dumps({"name": remote_name, "parents": [FOLDER_ID]}).encode("utf-8")
    body = (
        b"--" + boundary.encode() + b"\r\n"
        b"Content-Type: application/json; charset=UTF-8\r\n\r\n" + metadata + b"\r\n"
        b"--" + boundary.encode() + b"\r\n"
        + f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8")
        + content + b"\r\n"
        b"--" + boundary.encode() + b"--\r\n"
    )
    return body, f"multipart/related; boundary={boundary}"


def _upload(path: Path) -> None:
    remote_name = path.name
    mime_type = mimetypes.guess_type(remote_name)[0] or "application/octet-stream"
    content = path.read_bytes()
    file_id = _find_existing(remote_name)
    body, content_type = _multipart_body(remote_name, content, mime_type)
    if file_id:
        url = f"https://www.googleapis.com/upload/drive/v3/files/{file_id}?uploadType=multipart"
        _api_request(url, method="PATCH", data=body, content_type=content_type)
        print(f"Updated {remote_name}")
        return
    url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&supportsAllDrives=true"
    _api_request(url, method="POST", data=body, content_type=content_type)
    print(f"Created {remote_name}")


def _expand_placeholders(path: str) -> str:
    return path.replace("YYYY-MM-DD", ET_REPORT_DATE)


def _load_paths_from_config(config_path: Path) -> list[str]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    push_set = config.get("push_set")
    if not isinstance(push_set, list):
        raise ValueError(f"Config {config_path} is missing a push_set list")
    paths: list[str] = []
    for item in push_set:
        if not isinstance(item, str):
            raise ValueError(f"Config {config_path} contains a non-string push_set entry: {item!r}")
        paths.append(_expand_placeholders(item))
    return paths


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--config", type=Path)
    args, extras = parser.parse_known_args(argv[1:])

    if not FOLDER_ID:
        print("Missing GOOGLE_DRIVE_FOLDER_ID", file=sys.stderr)
        return 1

    if args.config:
        if not args.config.exists():
            print(f"Missing config file: {args.config}", file=sys.stderr)
            return 1
        items = _load_paths_from_config(args.config)
    else:
        if not extras:
            print("Usage: push_ops_files_to_drive.py [--config CONFIG] <file> [<file>...]", file=sys.stderr)
            return 1
        items = extras

    for item in items:
        path = Path(_expand_placeholders(item))
        if not path.exists():
            print(f"Missing file: {path}", file=sys.stderr)
            return 1
        _upload(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
