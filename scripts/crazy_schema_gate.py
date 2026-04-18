#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


VALID_TYPES = {"api", "scrape"}
VALID_FREQ = {"daily", "weekly"}
VALID_DIR = {"bullish", "bearish"}
VALID_EXPECTED = {"high", "medium", "low"}
VALID_FIRE_RATE = {"daily", "weekly", "monthly", "rare"}
VALID_ADAPTER_STATUS = {"existing", "new_required"}
VALID_TRIGGER_SENSITIVITY = {"high", "medium", "low"}
SECTOR_RE = re.compile(r"^X[A-Z]{2,4}$")


def _slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    text = re.sub(r"\s+", "-", text)
    return text[:60] or "idea"


def _title_case(text: str) -> str:
    return " ".join(w.capitalize() for w in re.sub(r"[^a-zA-Z0-9\s-]", "", text).split())


def _validate_schema(obj: dict, mode: str = "standard") -> list[str]:
    errors = []
    if not obj.get("idea") or not isinstance(obj.get("idea"), str):
        errors.append("missing idea")
    if not isinstance(obj.get("data"), dict):
        errors.append("missing data")
    else:
        data = obj["data"]
        if not data.get("source"):
            errors.append("data.source required")
        if data.get("type") not in VALID_TYPES:
            errors.append("data.type must be api|scrape")
        if data.get("frequency") not in VALID_FREQ:
            errors.append("data.frequency must be daily|weekly")
        if not isinstance(data.get("stable"), bool):
            errors.append("data.stable must be boolean")
    if not obj.get("behavior") or not isinstance(obj.get("behavior"), str):
        errors.append("missing behavior")
    impact = obj.get("market_impact")
    if not isinstance(impact, dict):
        errors.append("missing market_impact")
    else:
        if impact.get("direction") not in VALID_DIR:
            errors.append("market_impact.direction must be bullish|bearish")
        sector = impact.get("sector", "")
        if not sector or not SECTOR_RE.match(sector.strip()):
            errors.append("market_impact.sector must be single SPDR ETF like XLK")
        if not impact.get("rationale"):
            errors.append("market_impact.rationale required")
    logic = obj.get("trade_logic")
    if not isinstance(logic, dict):
        errors.append("missing trade_logic")
    else:
        if not logic.get("entry"):
            errors.append("trade_logic.entry required")
        if not logic.get("exit"):
            errors.append("trade_logic.exit required")
        if logic.get("expected_frequency") not in VALID_EXPECTED:
            errors.append("trade_logic.expected_frequency must be high|medium|low")

    # One sentence idea check (basic)
    if isinstance(obj.get("idea"), str) and obj["idea"].count(".") > 1:
        errors.append("idea should be one sentence")

    if mode == "high-action":
        logic = obj.get("trade_logic") if isinstance(obj.get("trade_logic"), dict) else {}
        data = obj.get("data") if isinstance(obj.get("data"), dict) else {}

        if logic.get("expected_frequency") == "low":
            errors.append("high-action expected_frequency must be high|medium")
        if data.get("stable") is not True:
            errors.append("high-action data.stable must be true")

        fire_rate = obj.get("expected_fire_rate")
        if fire_rate not in VALID_FIRE_RATE:
            errors.append("expected_fire_rate must be daily|weekly|monthly|rare")
        elif fire_rate == "rare":
            errors.append("high-action expected_fire_rate cannot be rare")

        if obj.get("historical_backfill") is not True:
            errors.append("high-action historical_backfill must be true")

        try:
            months = int(obj.get("minimum_history_months"))
        except (TypeError, ValueError):
            months = 0
        if months < 12:
            errors.append("high-action minimum_history_months must be >= 12")

        adapter_status = obj.get("adapter_status")
        if adapter_status not in VALID_ADAPTER_STATUS:
            errors.append("adapter_status must be existing|new_required")
        elif adapter_status != "existing":
            errors.append("high-action adapter_status must be existing")

        sensitivity = obj.get("trigger_sensitivity")
        if sensitivity not in VALID_TRIGGER_SENSITIVITY:
            errors.append("trigger_sensitivity must be high|medium|low")
        elif sensitivity == "low":
            errors.append("high-action trigger_sensitivity cannot be low")

        reason = obj.get("reason_it_will_fire_in_30_days", "")
        if not isinstance(reason, str) or len(reason.strip()) < 20:
            errors.append("reason_it_will_fire_in_30_days required")

    return errors


def _normalize(obj: dict) -> dict:
    idea = obj.get("idea", "").strip()
    idea_id = _slugify(idea)
    title = _title_case(idea)
    data = obj.get("data", {}) or {}
    impact = obj.get("market_impact", {}) or {}
    logic = obj.get("trade_logic", {}) or {}
    sector = (impact.get("sector") or "").strip()

    return {
        "idea_id": idea_id,
        "title": title or idea_id.replace("-", " ").title(),
        "source_provider": obj.get("source_provider", ""),
        "source_model": obj.get("source_model", ""),
        "thesis": f"{obj.get('behavior','').strip()} {impact.get('rationale','').strip()}".strip(),
        "data_sources": [data.get("source", "").strip()],
        "signal_logic": logic.get("entry", "").strip(),
        "entry_exit": f"Entry: {logic.get('entry','').strip()} Exit: {logic.get('exit','').strip()}".strip(),
        "position_sizing": "Allocate 5% per signal, max 20% total exposure.",
        "universe": [sector] if sector else [],
        "frequency": data.get("frequency", ""),
        "risks": "Data source instability, false positives, and regime shifts.",
        "implementation_notes": f"Use {data.get('source','')} via {data.get('type','')} ({data.get('frequency','')}).".strip(),
        "required_keys": [],
        "expected_fire_rate": obj.get("expected_fire_rate", ""),
        "historical_backfill": obj.get("historical_backfill", ""),
        "minimum_history_months": obj.get("minimum_history_months", ""),
        "adapter_status": obj.get("adapter_status", ""),
        "trigger_sensitivity": obj.get("trigger_sensitivity", ""),
        "reason_it_will_fire_in_30_days": obj.get("reason_it_will_fire_in_30_days", ""),
        "schema": obj,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", required=True)
    parser.add_argument("--out", dest="output_path", required=True)
    parser.add_argument("--rejects", required=True)
    parser.add_argument("--mode", choices=["standard", "high-action"], default="standard")
    args = parser.parse_args()

    in_path = Path(args.input_path)
    out_path = Path(args.output_path)
    rej_path = Path(args.rejects)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rej_path.parent.mkdir(parents=True, exist_ok=True)

    accepted = []
    rejected = []

    for line in in_path.read_text().splitlines():
        s = line.strip()
        if not s:
            continue
        obj = json.loads(s)
        errs = _validate_schema(obj, args.mode)
        if errs:
            rejected.append({"errors": errs, "schema": obj})
        else:
            accepted.append(_normalize(obj))

    out_path.write_text("\n".join(json.dumps(x) for x in accepted) + ("\n" if accepted else ""))
    rej_path.write_text("\n".join(json.dumps(x) for x in rejected) + ("\n" if rejected else ""))
    print(f"accepted={len(accepted)} rejected={len(rejected)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
