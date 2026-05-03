#!/usr/bin/env python3
from __future__ import annotations

import json
import mimetypes
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path


FOLDER_ID = os.environ.get("GOOGLE_DRIVE_FOLDER_ID", "")
ACCESS_TOKEN = os.environ.get("GDRIVE_ACCESS_TOKEN", "")


def _api_request(url: str, method: str = "GET", data: bytes | None = None, content_type: str | None = None) -> dict:
    req = urllib.request.Request(url, method=method, data=data)
    req.add_header("Authorization", f"Bearer {ACCESS_TOKEN}")
    if content_type:
        req.add_header("Content-Type", content_type)
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8")
        return json.loads(body) if body else {}


def _find_existing(remote_name: str) -> str | None:
    query = f"name = '{remote_name}' and '{FOLDER_ID}' in parents and trashed = false"
    params = urllib.parse.urlencode({"q": query, "fields": "files(id,name)", "pageSize": 10})
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
    url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
    _api_request(url, method="POST", data=body, content_type=content_type)
    print(f"Created {remote_name}")


def main(argv: list[str]) -> int:
    if not FOLDER_ID or not ACCESS_TOKEN:
        print("Missing GOOGLE_DRIVE_FOLDER_ID or GDRIVE_ACCESS_TOKEN", file=sys.stderr)
        return 1
    if len(argv) < 2:
        print("Usage: push_ops_files_to_drive.py <file> [<file>...]", file=sys.stderr)
        return 1
    for item in argv[1:]:
        path = Path(item)
        if not path.exists():
            print(f"Missing file: {path}", file=sys.stderr)
            return 1
        _upload(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
