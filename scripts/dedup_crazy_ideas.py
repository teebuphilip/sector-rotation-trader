#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any


STOPWORDS = {
    "the", "a", "an", "to", "for", "of", "and", "or", "with", "by", "on", "in", "at",
    "from", "into", "using", "use", "via", "after", "before", "under", "over",
}
TITLE_SIM_THRESHOLD = 0.60
TEXT_SIM_THRESHOLD = 0.72
STRUCT_SIM_THRESHOLD = 0.48


def _today_iso() -> str:
    return dt.date.today().isoformat()


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if not path.exists():
        return items
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s:
            continue
        try:
            obj = json.loads(s)
        except Exception:
            continue
        if isinstance(obj, dict):
            items.append(obj)
    return items


def _norm_text(text: str) -> str:
    text = re.sub(r"\s+", " ", str(text or "").strip().lower())
    text = re.sub(r"[^a-z0-9\s:/._-]", " ", text)
    return " ".join(text.split())


def _tokenize(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", _norm_text(text))
    return {w for w in words if w not in STOPWORDS}


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def _primary_source(idea: dict[str, Any]) -> str:
    sources = idea.get("data_sources")
    if isinstance(sources, list) and sources:
        return _norm_text(sources[0])
    return ""


def _primary_universe(idea: dict[str, Any]) -> str:
    universe = idea.get("universe")
    if isinstance(universe, list) and universe:
        return _norm_text(universe[0])
    return ""


def _title(idea: dict[str, Any]) -> str:
    return _norm_text(idea.get("title") or idea.get("idea") or idea.get("name") or "")


def _thesis_text(idea: dict[str, Any]) -> str:
    parts = [
        idea.get("title", ""),
        idea.get("family", ""),
        idea.get("thesis", ""),
        " ".join(idea.get("data_sources", []) if isinstance(idea.get("data_sources"), list) else []),
        idea.get("signal_logic", ""),
        idea.get("entry_exit", ""),
        " ".join(idea.get("universe", []) if isinstance(idea.get("universe"), list) else []),
        idea.get("frequency", ""),
    ]
    return _norm_text(" ".join(str(x) for x in parts if x))


def _struct_signature(idea: dict[str, Any]) -> str:
    return "|".join(
        [
            _norm_text(idea.get("family", "")),
            _norm_text(idea.get("frequency", "")),
            _primary_universe(idea),
            _primary_source(idea),
        ]
    )


def _richness(idea: dict[str, Any]) -> int:
    lengths = [
        len(str(idea.get("thesis", "")).strip()),
        len(str(idea.get("signal_logic", "")).strip()),
        len(str(idea.get("entry_exit", "")).strip()),
        len(str(idea.get("implementation_notes", "")).strip()),
        len(str(idea.get("reason_it_will_fire_in_30_days", "")).strip()),
    ]
    return sum(lengths) + 25 * len(idea.get("data_sources", []) or []) + 10 * len(idea.get("universe", []) or [])


def _candidate_record(idea: dict[str, Any], source: str, origin: str) -> dict[str, Any]:
    title = _title(idea)
    text = _thesis_text(idea)
    return {
        "idea": idea,
        "source": source,
        "origin": origin,
        "idea_id": str(idea.get("idea_id") or ""),
        "title": title,
        "title_tokens": _tokenize(title),
        "text": text,
        "text_tokens": _tokenize(text),
        "struct": _struct_signature(idea),
        "richness": _richness(idea),
    }


def _existing_algo_records() -> list[dict[str, Any]]:
    path = Path("data/product/algos_index.json")
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    rows = []
    for item in payload.get("algos", []):
        if not isinstance(item, dict):
            continue
        pseudo = {
            "idea_id": item.get("algo_id"),
            "title": item.get("name"),
            "family": item.get("family"),
            "data_sources": [],
            "signal_logic": item.get("status", ""),
            "entry_exit": item.get("evidence_class", ""),
            "universe": [],
            "frequency": item.get("rebalance_frequency", ""),
            "thesis": item.get("name", ""),
        }
        rows.append(_candidate_record(pseudo, str(item.get("algo_type") or "algo"), "existing_algo"))
    return rows


def _history_records(run_date: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    base = Path("data/ideas/runs")
    if not base.exists():
        return rows
    for run_dir in sorted(base.iterdir()):
        if not run_dir.is_dir() or run_dir.name >= run_date:
            continue
        deduped = run_dir / "deduped"
        filtered = run_dir / "filtered"
        src_dir = deduped if deduped.exists() else filtered
        for src in ("chatgpt", "claude"):
            for idea in _load_jsonl(src_dir / f"{src}_{run_dir.name}.jsonl"):
                rows.append(_candidate_record(idea, src, f"history:{run_dir.name}"))
    return rows


def _match_reason(candidate: dict[str, Any], existing: dict[str, Any]) -> tuple[bool, str, float]:
    if candidate["idea_id"] and candidate["idea_id"] == existing["idea_id"]:
        return True, "same_idea_id", 1.0
    if candidate["title"] and candidate["title"] == existing["title"]:
        return True, "same_title", 1.0

    title_sim = _jaccard(candidate["title_tokens"], existing["title_tokens"])
    text_sim = _jaccard(candidate["text_tokens"], existing["text_tokens"])
    struct_match = candidate["struct"] and candidate["struct"] == existing["struct"]

    if struct_match and text_sim >= STRUCT_SIM_THRESHOLD:
        return True, "same_structure", text_sim
    if title_sim >= TITLE_SIM_THRESHOLD and text_sim >= STRUCT_SIM_THRESHOLD:
        return True, "high_title_overlap", max(title_sim, text_sim)
    if text_sim >= TEXT_SIM_THRESHOLD:
        return True, "high_text_overlap", text_sim
    return False, "", max(title_sim, text_sim)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=_today_iso())
    args = parser.parse_args()

    run_dir = Path("data") / "ideas" / "runs" / args.date
    filtered_dir = run_dir / "filtered"
    deduped_dir = run_dir / "deduped"
    dup_dir = run_dir / "duplicates"
    deduped_dir.mkdir(parents=True, exist_ok=True)
    dup_dir.mkdir(parents=True, exist_ok=True)

    candidates: list[dict[str, Any]] = []
    for src in ("chatgpt", "claude"):
        for idea in _load_jsonl(filtered_dir / f"{src}_{args.date}.jsonl"):
            candidates.append(_candidate_record(idea, src, "current_run"))

    candidates.sort(key=lambda row: (row["richness"], row["title"]), reverse=True)

    existing = _existing_algo_records() + _history_records(args.date)
    kept: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []

    for candidate in candidates:
        matched = None
        for ref in existing + kept:
            is_dup, reason, score = _match_reason(candidate, ref)
            if is_dup:
                matched = {
                    "reason": reason,
                    "score": round(score, 3),
                    "matched_title": ref["title"],
                    "matched_idea_id": ref["idea_id"],
                    "matched_origin": ref["origin"],
                    "matched_source": ref["source"],
                }
                break
        if matched:
            rejected.append(
                {
                    "source": candidate["source"],
                    "idea_id": candidate["idea_id"],
                    "title": candidate["idea"].get("title"),
                    "family": candidate["idea"].get("family"),
                    "duplicate_of": matched,
                    "idea": candidate["idea"],
                }
            )
        else:
            kept.append(candidate)

    by_source = {"chatgpt": [], "claude": []}
    for item in kept:
        by_source[item["source"]].append(item["idea"])

    for src, rows in by_source.items():
        out = deduped_dir / f"{src}_{args.date}.jsonl"
        out.write_text("\n".join(json.dumps(x) for x in rows) + ("\n" if rows else ""), encoding="utf-8")

    report = {
        "date": args.date,
        "input_count": len(candidates),
        "kept_count": len(kept),
        "duplicate_count": len(rejected),
        "kept_by_source": {src: len(rows) for src, rows in by_source.items()},
        "duplicates": rejected,
    }
    (dup_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(
        f"[dedup] input={len(candidates)} kept={len(kept)} duplicates={len(rejected)} "
        f"chatgpt={len(by_source['chatgpt'])} claude={len(by_source['claude'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
