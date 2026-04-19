#!/usr/bin/env python3
"""
Final LLM gate for published crazy idea specs.

Reads markdown files from a publish directory, runs deterministic adapter routing,
asks one low-temperature LLM call for BUILD / INTERVENTION / REJECT, and places
each spec into build/, intervention/, or reject/.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path
from typing import Any, Dict, Iterable

from adapter_router import route_text, score_text


VALID_DECISIONS = {"BUILD", "INTERVENTION", "REJECT"}
DEFAULT_MODEL = "gpt-4.1-mini"
TEMPLATE_SUPPORTED_ADAPTERS = {
    "earthquake_activity",
    "openchargemap",
    "google_trends",
    "rss_count",
    "weather_series",
    "tsa_table",
    "price_only",
    "eia_electricity",
    "port_container_volume",
}


SYSTEM_PROMPT = """You are the final buildability gate for a high-action trading signal lab.

You are not writing code. You are not improving the idea. You are deciding where
the markdown spec should go next.

Return ONLY strict JSON:
{
  "decision": "BUILD|INTERVENTION|REJECT",
  "adapter_ok": true|false,
  "selected_adapter": "adapter_name_or_null",
  "needs_new_adapter": true|false,
  "reason": "one short sentence",
  "risk_flags": ["short flag", "..."]
}

Definitions:
- BUILD: The spec is understandable, deterministic, uses a real/current adapter,
  and can go straight into structural autobuild.
- INTERVENTION: The idea might be useful, but adapter mapping, data source,
  frequency, missing keys, or implementation details need manual review.
- REJECT: The idea is vague, not grounded in real data, not causally coherent,
  not buildable, or likely useless even as an experiment.

Decision rules:
1. If deterministic adapter routing confidence is low, prefer INTERVENTION.
2. If selected adapter does not actually match the data source, use INTERVENTION
   or REJECT.
3. If the idea needs a new adapter, use INTERVENTION and set needs_new_adapter true.
4. If behavior -> market impact -> trade logic is nonsense, use REJECT.
5. If the markdown is structurally valid but conceptually questionable, use
   INTERVENTION, not BUILD.
6. Do not reject just because the idea is weird. Weird is allowed. Unbuildable is not.
7. The adapter must directly measure the named data source. Do not approve a
   loose proxy just because it sounds event-like or macro-like.
8. earthquake_activity is only valid for earthquake/seismic/USGS/tectonic data.
   It is not valid for geopolitical conflict, war, sanctions, unrest, military
   activity, or international tension.
9. rss_count is only valid when the spec explicitly uses RSS/news-feed counts.
10. price_only is only valid when OHLCV/price/return/volume data is enough.
11. If a spec requires volume but the selected adapter is price_only, use
    INTERVENTION unless the adapter contract explicitly provides volume.
12. If a spec requires entering short, shorting, inverse exposure, or bearish
    allocation, use INTERVENTION. The current structural algo envelope supports
    long/flat allocation, not native short positions.
"""


def _strip_code_fence(text: str) -> str:
    text = text.strip()
    if not text.startswith("```"):
        return text
    parts = text.split("```")
    if len(parts) < 2:
        return text
    body = parts[1].strip()
    if body.lower().startswith("json"):
        body = "\n".join(body.splitlines()[1:]).strip()
    return body


def _extract_usage(resp: Any) -> Dict[str, int]:
    meta = getattr(resp, "response_metadata", None) or {}
    usage = meta.get("token_usage") or {}
    if not usage:
        usage = getattr(resp, "usage_metadata", None) or {}
    return {
        "input_tokens": int(
            usage.get("input_tokens")
            or usage.get("prompt_tokens")
            or usage.get("input_token_count")
            or 0
        ),
        "output_tokens": int(
            usage.get("output_tokens")
            or usage.get("completion_tokens")
            or usage.get("output_token_count")
            or 0
        ),
    }


def _cost_usd(usage: Dict[str, int]) -> float:
    in_rate = float(os.getenv("OPENAI_INPUT_PER_MTOK", "2.50"))
    out_rate = float(os.getenv("OPENAI_OUTPUT_PER_MTOK", "10.00"))
    return (
        usage.get("input_tokens", 0) * in_rate
        + usage.get("output_tokens", 0) * out_rate
    ) / 1_000_000


def _read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _iter_specs(publish_dir: Path) -> Iterable[Path]:
    return sorted(p for p in publish_dir.glob("*.md") if p.is_file())


def _default_output_dir(publish_dir: Path) -> Path:
    # For data/ideas/runs/YYYY-MM-DD/publish, write siblings:
    # data/ideas/runs/YYYY-MM-DD/{build,intervention,reject}
    if publish_dir.name == "publish":
        return publish_dir.parent
    return publish_dir / "final_gate"


def _deterministic_override(markdown: str, route: Dict[str, Any]) -> Dict[str, Any]:
    text = markdown.lower()
    adapter_list = route.get("adapters") or []
    adapters = set(adapter_list)
    flags = []
    decision = None
    reason = None
    needs_new_adapter = False

    geopolitical_terms = [
        "geopolitical",
        "conflict",
        "war",
        "sanction",
        "sanctions",
        "military",
        "invasion",
        "unrest",
        "international tension",
    ]
    seismic_terms = ["earthquake", "seismic", "usgs", "tectonic"]
    has_geopolitical = any(term in text for term in geopolitical_terms)
    has_seismic = any(term in text for term in seismic_terms)

    if "earthquake_activity" in adapters and has_geopolitical:
        decision = "INTERVENTION"
        reason = "Selected adapter measures earthquakes, not geopolitical conflict or war data."
        needs_new_adapter = True
        flags.append("adapter_behavior_mismatch")

    if "rss_count" in adapters and not any(term in text for term in ["rss", "news feed", "feed count", "news mentions", "news volume"]):
        decision = "INTERVENTION"
        reason = "rss_count selected but spec does not clearly define RSS/news-feed count data."
        flags.append("rss_adapter_unclear")

    if "fred_series" in adapters and "surprise" in text and "consensus" in text:
        decision = "INTERVENTION"
        reason = "FRED provides observed series, not consensus surprise data."
        flags.append("fred_consensus_surprise_gap")

    if adapter_list and adapter_list[0] not in TEMPLATE_SUPPORTED_ADAPTERS:
        decision = "INTERVENTION"
        reason = f"Template builder does not support {adapter_list[0]} yet."
        needs_new_adapter = True
        flags.append("unsupported_template_adapter")

    if "price_only" in adapters and "volume" in text:
        decision = "INTERVENTION"
        reason = "price_only currently provides close/value data, not volume."
        flags.append("price_only_volume_gap")

    short_terms = ["enter short", "short ", "shorting", "inverse exposure", "bearish allocation"]
    if any(term in text for term in short_terms):
        decision = "INTERVENTION"
        reason = "Current structural algo envelope supports long/flat allocation, not native short trades."
        flags.append("short_trade_not_supported")

    return {
        "decision": decision,
        "reason": reason,
        "needs_new_adapter": needs_new_adapter,
        "risk_flags": flags,
    }


def _normalize_verdict(raw: Dict[str, Any], route: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    decision = str(raw.get("decision") or "INTERVENTION").upper().strip()
    if decision not in VALID_DECISIONS:
        decision = "INTERVENTION"

    top_score = int(route.get("top_score") or 0)
    confidence = route.get("confidence")
    adapters = route.get("adapters") or []

    # Deterministic safety override: low/no adapter never goes straight to build.
    if decision == "BUILD" and (confidence == "low" or not adapters):
        decision = "INTERVENTION"

    selected_adapter = raw.get("selected_adapter")
    if selected_adapter in ("", "null", "None"):
        selected_adapter = None

    risk_flags = raw.get("risk_flags")
    if not isinstance(risk_flags, list):
        risk_flags = []
    risk_flags = [str(x) for x in risk_flags if str(x).strip()]
    if confidence == "low":
        risk_flags.append("low_adapter_confidence")
    if not adapters:
        risk_flags.append("no_adapter_route")
    risk_flags.extend(override.get("risk_flags") or [])

    if override.get("decision"):
        decision = override["decision"]
    if override.get("reason"):
        raw["reason"] = override["reason"]

    return {
        "decision": decision,
        "adapter_ok": bool(raw.get("adapter_ok")) and confidence != "low",
        "selected_adapter": selected_adapter or (adapters[0] if adapters else None),
        "needs_new_adapter": bool(raw.get("needs_new_adapter")) or bool(override.get("needs_new_adapter")) or not adapters,
        "reason": str(raw.get("reason") or "No reason supplied.").strip(),
        "risk_flags": sorted(set(risk_flags)),
        "route": {
            "adapters": adapters,
            "scores": route.get("scores") or {},
            "top_score": top_score,
            "confidence": confidence,
        },
    }


def _llm_verdict(llm: Any, spec_path: Path, markdown: str, route: Dict[str, Any]) -> tuple[Dict[str, Any], Dict[str, int], float, str]:
    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"SPEC_FILE: {spec_path}\n\n"
        f"DETERMINISTIC_ADAPTER_ROUTE:\n{json.dumps(route, indent=2)}\n\n"
        f"MARKDOWN_SPEC:\n{markdown}\n"
    )
    resp = llm.invoke(prompt)
    usage = _extract_usage(resp)
    cost = _cost_usd(usage)
    raw_text = str(getattr(resp, "content", "")).strip()
    text = _strip_code_fence(raw_text)
    try:
        parsed = json.loads(text)
        if not isinstance(parsed, dict):
            raise ValueError("LLM JSON was not an object")
    except Exception:
        parsed = {
            "decision": "INTERVENTION",
            "adapter_ok": False,
            "selected_adapter": None,
            "needs_new_adapter": False,
            "reason": "LLM response did not parse as JSON.",
            "risk_flags": ["failed_to_parse_llm_json"],
            "raw_response": raw_text,
        }
    return parsed, usage, cost, raw_text


def _route(markdown: str) -> Dict[str, Any]:
    scores = score_text(markdown)
    adapters = route_text(markdown)
    top_score = max(scores.values()) if scores else 0
    confidence = "low" if top_score < 2 else "ok"
    return {
        "adapters": adapters,
        "scores": scores,
        "top_score": top_score,
        "confidence": confidence,
    }


def _remove_stale_classifications(src: Path, decision_dirs: Iterable[Path], dry_run: bool) -> None:
    if dry_run:
        return
    for directory in decision_dirs:
        stale = directory / src.name
        if stale.exists():
            stale.unlink()


def _place_file(src: Path, dst_dir: Path, move: bool, dry_run: bool) -> Path:
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name
    if dry_run:
        return dst
    if move:
        shutil.move(str(src), str(dst))
    else:
        shutil.copy2(src, dst)
    return dst


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--date",
        default=None,
        help="Run date in YYYY-MM-DD format. Resolves to data/ideas/runs/<date>/publish.",
    )
    parser.add_argument(
        "--publish-dir",
        default=None,
        help="Directory containing published markdown specs. Overrides --date.",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory that will contain build/, intervention/, reject/. Defaults to publish parent.",
    )
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", DEFAULT_MODEL))
    parser.add_argument("--dry-run", action="store_true", help="Run LLM checks but do not copy/move files.")
    parser.add_argument("--move", action="store_true", help="Move files instead of copying them.")
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Only process the first N specs. Useful for testing.",
    )
    args = parser.parse_args()

    if args.publish_dir:
        publish_dir = Path(args.publish_dir)
    elif args.date:
        publish_dir = Path("data/ideas/runs") / args.date / "publish"
    else:
        raise SystemExit("Provide either --date YYYY-MM-DD or --publish-dir PATH")
    if not publish_dir.exists():
        raise SystemExit(f"Publish dir not found: {publish_dir}")

    output_dir = Path(args.output_dir) if args.output_dir else _default_output_dir(publish_dir)
    build_dir = output_dir / "build"
    intervention_dir = output_dir / "intervention"
    reject_dir = output_dir / "reject"
    report_dir = output_dir / "publish_gate_reports"
    if not args.dry_run:
        for path in (build_dir, intervention_dir, reject_dir, report_dir):
            path.mkdir(parents=True, exist_ok=True)

    specs = list(_iter_specs(publish_dir))
    if args.limit:
        specs = specs[: args.limit]

    print(f"[run] publish_dir={publish_dir}")
    print(f"[run] output_dir={output_dir}")
    print(f"[run] model={args.model}")
    print(f"[run] dry_run={args.dry_run} move={args.move}")
    print(f"[run] specs={len(specs)}")

    if not specs:
        print("[done] no markdown specs found")
        return 0

    try:
        from langchain_openai import ChatOpenAI
    except Exception as exc:
        raise SystemExit(
            "Missing dependency langchain_openai. Run inside the project venv, "
            "for example: /Users/teebuphilip/venvs/cd39/bin/python "
            "scripts/final_publish_llm_gate.py ..."
        ) from exc

    llm = ChatOpenAI(model=args.model, temperature=0.0)
    summary: Dict[str, Any] = {
        "publish_dir": str(publish_dir),
        "output_dir": str(output_dir),
        "model": args.model,
        "dry_run": args.dry_run,
        "move": args.move,
        "counts": {"BUILD": 0, "INTERVENTION": 0, "REJECT": 0},
        "costs": {"openai": 0.0, "total": 0.0},
        "files": [],
    }

    for idx, spec_path in enumerate(specs, start=1):
        markdown = _read_markdown(spec_path)
        route = _route(markdown)
        override = _deterministic_override(markdown, route)
        print(
            f"[{idx}/{len(specs)}] {spec_path.name} "
            f"route={route['adapters']} confidence={route['confidence']}"
        )

        parsed, usage, cost, raw_response = _llm_verdict(llm, spec_path, markdown, route)
        verdict = _normalize_verdict(parsed, route, override)
        decision = verdict["decision"]
        target_dir = {
            "BUILD": build_dir,
            "INTERVENTION": intervention_dir,
            "REJECT": reject_dir,
        }[decision]
        _remove_stale_classifications(spec_path, (build_dir, intervention_dir, reject_dir), args.dry_run)
        target_path = _place_file(spec_path, target_dir, move=args.move, dry_run=args.dry_run)

        report = {
            "source_file": str(spec_path),
            "target_file": str(target_path),
            "verdict": verdict,
            "usage": usage,
            "cost_usd": cost,
            "raw_llm_response": raw_response,
        }
        report_path = report_dir / f"{spec_path.stem}.json"
        if not args.dry_run:
            report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

        summary["counts"][decision] += 1
        summary["costs"]["openai"] += cost
        summary["costs"]["total"] += cost
        summary["files"].append(
            {
                "file": str(spec_path),
                "decision": decision,
                "target": str(target_path),
                "reason": verdict["reason"],
                "risk_flags": verdict["risk_flags"],
                "cost_usd": cost,
            }
        )

        print(
            f"[gate][openai] cost=${cost:.6f} decision={decision} "
            f"target={target_path}"
        )
        print(f"[gate] reason={verdict['reason']}")

    summary_path = report_dir / "summary.json"
    if not args.dry_run:
        summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print(f"[write] {summary_path}")

    print(
        "[done] "
        f"build={summary['counts']['BUILD']} "
        f"intervention={summary['counts']['INTERVENTION']} "
        f"reject={summary['counts']['REJECT']}"
    )
    print(
        f"[costs][openai]=${summary['costs']['openai']:.6f} "
        f"[costs][total]=${summary['costs']['total']:.6f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
