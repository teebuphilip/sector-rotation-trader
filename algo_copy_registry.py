#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT_PATH = ROOT / "docs" / "data" / "public" / "algo_copy.json"
LEGACY_COPY_PATH = ROOT / "data" / "algos" / "legacy_copy.json"


SECTION_KEYS = {
    "Thesis": "thesis",
    "Universe": "universe",
    "Data Sources": "data_sources",
    "Signal Logic": "signal_logic",
    "Entry / Exit": "entry_exit",
    "Position Sizing": "position_sizing",
    "Risks": "risks",
    "Implementation Notes": "implementation_notes",
    "High Action Metadata": "high_action_metadata",
    "Required Keys": "required_keys",
}


def _parse_bullets(text: str) -> list[str]:
    items = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- "):
            stripped = stripped[2:].strip()
        items.append(stripped)
    return items


def _clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def _slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _public_summary(record: dict) -> str:
    thesis = _clean_text(str(record.get("thesis") or ""))
    if thesis:
        return thesis
    title = _clean_text(str(record.get("title") or ""))
    return title


def _parse_markdown(path: Path, category: str) -> dict | None:
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", text, flags=re.M)
    idea_match = re.search(r"^\*\*Idea ID:\*\*\s*`([^`]+)`", text, flags=re.M)
    if not title_match or not idea_match:
        return None

    record: dict[str, object] = {
        "title": _clean_text(title_match.group(1)),
        "algo_id": _clean_text(idea_match.group(1)),
        "category": category,
    }

    family_match = re.search(r"^\*\*Family:\*\*\s*`([^`]*)`", text, flags=re.M)
    if family_match and family_match.group(1).strip():
        record["family"] = family_match.group(1).strip()

    freq_match = re.search(r"^\*\*Frequency:\*\*\s*([^\n]+)", text, flags=re.M)
    if freq_match:
        record["rebalance_frequency"] = _clean_text(freq_match.group(1))

    source_match = re.search(r"^\*\*Source:\*\*\s*([^\n]+)", text, flags=re.M)
    if source_match:
        record["source"] = _clean_text(source_match.group(1))

    section_matches = list(re.finditer(r"^##\s+(.+)$", text, flags=re.M))
    for i, match in enumerate(section_matches):
        label = match.group(1).strip()
        key = SECTION_KEYS.get(label)
        if not key:
            continue
        start = match.end()
        end = section_matches[i + 1].start() if i + 1 < len(section_matches) else len(text)
        block = text[start:end].strip()
        if not block:
            continue
        if key in {"universe", "data_sources", "required_keys"}:
            record[key] = _parse_bullets(block)
        else:
            record[key] = _clean_text(block)

    record["public_summary"] = _public_summary(record)
    return record


def _iter_markdown_paths() -> list[tuple[str, Path]]:
    pairs: list[tuple[str, Path]] = []

    roots = (
        ("crazy", ROOT / "data" / "ideas" / "runs", "*/publish/*.md"),
        ("normal", ROOT / "data" / "normal_ideas" / "runs", "*/publish/*.md"),
        ("crazy", ROOT / "data" / "ideas" / "completed", "*/*.md"),
        ("crazy", ROOT / "data" / "ideas" / "failed", "*/*.md"),
        ("normal", ROOT / "data" / "normal_ideas" / "completed", "*/*.md"),
        ("normal", ROOT / "data" / "normal_ideas" / "failed", "*/*.md"),
    )

    for category, base, pattern in roots:
        if not base.exists():
            continue
        for md_path in sorted(base.glob(pattern)):
            pairs.append((category, md_path))
    return pairs


def build_algo_copy_registry() -> dict[str, dict]:
    records: dict[str, dict] = {}

    if LEGACY_COPY_PATH.exists():
        try:
            legacy_data = json.loads(LEGACY_COPY_PATH.read_text(encoding="utf-8"))
        except Exception:
            legacy_data = {}
        if isinstance(legacy_data, dict):
            for algo_id, payload in legacy_data.items():
                if not isinstance(payload, dict):
                    continue
                record = dict(payload)
                record.setdefault("algo_id", algo_id)
                record.setdefault("title", algo_id)
                record.setdefault("public_summary", _public_summary(record))
                records[str(algo_id)] = record

    for category, md_path in _iter_markdown_paths():
        parsed = _parse_markdown(md_path, category)
        if not parsed:
            continue
        algo_id = str(parsed["algo_id"])
        record = dict(parsed)
        records[f"{category}:{algo_id}"] = record
        records[algo_id] = record

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    return records


def lookup_algo_copy(
    *,
    key: str | None = None,
    algo_id: str | None = None,
    name: str | None = None,
    registry: dict | None = None,
) -> dict | None:
    data = registry
    if data is None:
        if OUT_PATH.exists():
            try:
                data = json.loads(OUT_PATH.read_text(encoding="utf-8"))
            except Exception:
                data = {}
        else:
            data = {}

    if key and key in data:
        return data[key]
    if algo_id:
        algo_id = str(algo_id)
        if algo_id in data:
            return data[algo_id]
        for prefix in ("crazy", "normal"):
            prefixed = f"{prefix}:{algo_id}"
            if prefixed in data:
                return data[prefixed]
    if name:
        slug = _slugify(name)
        if slug in data:
            return data[slug]
        for prefix in ("crazy", "normal"):
            prefixed = f"{prefix}:{slug}"
            if prefixed in data:
                return data[prefixed]
        for record in data.values():
            if not isinstance(record, dict):
                continue
            title_slug = _slugify(str(record.get("title") or ""))
            name_slug = _slugify(str(record.get("name") or ""))
            if slug and slug in {title_slug, name_slug}:
                return record
    return None
