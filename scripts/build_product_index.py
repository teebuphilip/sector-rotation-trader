#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from crazy.algos import get_crazy_algos
from normal.algos import get_normal_algos


PRODUCT_DIR = ROOT / "data" / "product"
CRAZY_STATE_DIR = ROOT / "data" / "crazy" / "state"
NORMAL_STATE_DIR = ROOT / "data" / "normal" / "state"
BACKTEST_LATEST = ROOT / "reports" / "backtests" / "latest.json"
NEW_ALGOS_LOG = ROOT / "data" / "algos" / "new_algos.jsonl"
IDEAS_RUNS_DIR = ROOT / "data" / "ideas" / "runs"


FAMILY_RULES = [
    ("travel_mobility", [
        "tsa", "airport", "airline", "travel", "hotel", "mobility", "uber",
        "booking", "shopping-spree",
    ]),
    ("freight_logistics", [
        "truck", "rail", "port", "container", "warehouse", "shipping",
        "freight", "cardboard", "logistics",
    ]),
    ("labor_jobs", [
        "job", "jobs", "hiring", "resume", "linkedin", "glassdoor", "layoff",
        "office-occupancy",
    ]),
    ("political_insider_filing", [
        "congress", "insider", "sec", "filing", "executive", "turnover",
    ]),
    ("local_economy_weirdness", [
        "craigslist", "311", "calls311", "liquor", "restaurant", "yelp",
        "parking", "refund", "local",
    ]),
    ("consumer_stress", [
        "bankruptcy", "delinquency", "consumer", "mortgage", "retail",
        "coupon", "rent", "used-car", "formation", "small-business", "credit",
        "home-buying", "homebuilder", "sale-keywords",
    ]),
    ("attention_sentiment", [
        "reddit", "twitter", "social", "wikipedia", "google-trends", "trends",
        "rss", "sentiment", "mention", "silence", "buzz", "emoji",
    ]),
    ("macro_input_pressure", [
        "weather", "earthquake", "electricity", "utility", "yield", "spread",
        "commodity", "copper", "lumber", "volatility", "energy", "ev", "charger",
        "flu", "fed-funds", "temperature", "cold-snap",
    ]),
]


def _load_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s:
            continue
        try:
            obj = json.loads(s)
        except Exception:
            continue
        if isinstance(obj, dict):
            rows.append(obj)
    return rows


def _backtest_map() -> dict[tuple[str, str], dict]:
    data = _load_json(BACKTEST_LATEST)
    out: dict[tuple[str, str], dict] = {}
    if not isinstance(data, dict):
        return out
    for item in data.get("results", []):
        if not isinstance(item, dict):
            continue
        key = (str(item.get("family") or ""), str(item.get("algo_id") or ""))
        if key[0] and key[1]:
            out[key] = item
    return out


def _new_algo_dates() -> dict[tuple[str, str], str]:
    out: dict[tuple[str, str], str] = {}
    for row in _load_jsonl(NEW_ALGOS_LOG):
        category = str(row.get("category") or "")
        algo_id = str(row.get("algo_id") or "")
        stamp = str(row.get("date") or "")
        if category and algo_id and stamp:
            out[(category, algo_id)] = stamp
    return out


def _pending_seed_ids() -> set[str]:
    pending: set[str] = set()
    if not IDEAS_RUNS_DIR.exists():
        return pending
    for root in sorted(IDEAS_RUNS_DIR.glob("*/factory_results")):
        if not root.is_dir():
            continue
        for path in root.glob("*.json"):
            if path.name == "summary.json" or path.name.endswith("_template_build.json"):
                continue
            obj = _load_json(path)
            if not isinstance(obj, dict):
                continue
            if obj.get("seeded") is False and obj.get("idea_id"):
                pending.add(str(obj["idea_id"]))
    return pending


def _algo_source_path(algo_family: str, algo_id: str) -> Path:
    return ROOT / algo_family / "algos" / f"{algo_id.replace('-', '_')}.py"


def _classify_family(algo_family: str, algo_id: str, name: str) -> str:
    if algo_family == "normal":
        return "core_rotation"
    text = f"{algo_id} {name}".lower()
    for family, keys in FAMILY_RULES:
        if any(key in text for key in keys):
            return family
    return "macro_input_pressure"


def _state_summary(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {
            "exists": False,
            "equity": 100000.0,
            "trade_count": 0,
            "last_snapshot": None,
            "last_signal": None,
            "has_live_trades": False,
            "positions": 0,
        }
    data = _load_json(path) or {}
    snaps = data.get("daily_snapshots") or []
    latest = snaps[-1] if snaps else {}
    trades = data.get("trade_log") or []
    eq = float(latest.get("equity", data.get("cash", 100000.0) or 100000.0))
    return {
        "exists": True,
        "equity": eq,
        "trade_count": len(trades),
        "last_snapshot": latest.get("date"),
        "last_signal": (data.get("meta") or {}).get("last_signal") or None,
        "has_live_trades": len(trades) > 0,
        "positions": len(data.get("positions") or {}),
    }


def _evidence_class(backtest: dict | None, state: dict, pending_seed: bool) -> str:
    if pending_seed:
        return "pending_seed"
    status = str((backtest or {}).get("status") or "")
    if status.startswith("BACKTEST_") or status == "INSUFFICIENT_ACTIVITY":
        return "v1_backtested"
    if status == "UNSUPPORTED_SHORT":
        return "short_model_pending"
    if status in {"UNSUPPORTED_DATA", "LIVE_ONLY_NON_PRICE", "NEEDS_HISTORY", "UNSUPPORTED_UNIVERSE"}:
        if state.get("has_live_trades"):
            return "live_receipts_only"
        return "needs_history"
    if state.get("has_live_trades"):
        return "live_receipts_only"
    return "pending_seed" if pending_seed else "needs_history"


def _status(algo_family: str, backtest: dict | None, state: dict, pending_seed: bool) -> str:
    if algo_family == "normal":
        return "promoted"
    if pending_seed or not state.get("exists"):
        return "parked"
    bt = str((backtest or {}).get("status") or "")
    if bt == "BACKTEST_PASS":
        return "promoted" if state.get("trade_count", 0) > 0 else "backtest_pass"
    if bt == "BACKTEST_WEAK":
        return "backtest_weak"
    if bt == "BACKTEST_FAIL":
        return "failed"
    if state.get("trade_count", 0) > 0:
        return "live_only"
    return "sandbox"


def _watchlist_item(item: dict) -> bool:
    return item["status"] in {"promoted", "backtest_pass", "backtest_weak", "live_only"}


def _promoted_item(item: dict) -> bool:
    return item["status"] == "promoted"


def _graveyard_item(item: dict) -> bool:
    return item["status"] in {"failed", "parked"}


def main() -> int:
    PRODUCT_DIR.mkdir(parents=True, exist_ok=True)

    algos = [("normal", a) for a in get_normal_algos()] + [("crazy", a) for a in get_crazy_algos()]
    backtests = _backtest_map()
    new_algo_dates = _new_algo_dates()
    pending_seed = _pending_seed_ids()

    items: list[dict[str, Any]] = []
    for algo_family, algo in algos:
        algo_id = str(algo.algo_id)
        state_path = (NORMAL_STATE_DIR if algo_family == "normal" else CRAZY_STATE_DIR) / f"{algo_id}.json"
        state = _state_summary(state_path)
        backtest = backtests.get((algo_family, algo_id))
        family = getattr(algo, "family", "") or _classify_family(algo_family, algo_id, algo.name)
        evidence_class = _evidence_class(backtest, state, algo_id in pending_seed)
        status = _status(algo_family, backtest, state, algo_id in pending_seed)

        bt_metrics = dict((backtest or {}).get("metrics") or {})
        item = {
            "key": f"{algo_family}:{algo_id}",
            "algo_type": algo_family,
            "algo_id": algo_id,
            "name": algo.name,
            "family": family,
            "status": status,
            "evidence_class": evidence_class,
            "rebalance_frequency": getattr(algo, "rebalance_frequency", None),
            "universe": list(algo.universe()),
            "equity": round(float(state["equity"]), 2),
            "ytd_pct": round((float(state["equity"]) / 100000.0 - 1.0) * 100.0, 2),
            "trade_count": int(state["trade_count"]),
            "positions": int(state["positions"]),
            "last_snapshot": state["last_snapshot"],
            "last_signal": state["last_signal"],
            "new_algo_date": new_algo_dates.get((algo_family, algo_id)),
            "backtest_status": (backtest or {}).get("status"),
            "backtest_reason": (backtest or {}).get("reason"),
            "backtest_alpha_vs_spy_pct": bt_metrics.get("alpha_vs_spy_pct"),
            "backtest_trade_count": bt_metrics.get("trade_count"),
        }
        items.append(item)

    items.sort(key=lambda x: (x["algo_type"], x["family"], x["algo_id"]))

    family_rollup: dict[str, dict[str, Any]] = {}
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        grouped[item["family"]].append(item)
    for family, members in sorted(grouped.items()):
        family_rollup[family] = {
            "family": family,
            "count": len(members),
            "by_status": dict(sorted(Counter(m["status"] for m in members).items())),
            "by_evidence_class": dict(sorted(Counter(m["evidence_class"] for m in members).items())),
            "leaders": sorted(members, key=lambda m: m["ytd_pct"], reverse=True)[:5],
        }

    watchlist = [m for m in items if _watchlist_item(m)]
    promoted = [m for m in items if _promoted_item(m)]
    graveyard = [m for m in items if _graveyard_item(m)]

    run_date = max((m["last_snapshot"] for m in items if m.get("last_snapshot")), default=datetime.utcnow().date().isoformat())
    daily_summary = {
        "run_date": run_date,
        "generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "counts": {
            "total": len(items),
            "normal": sum(1 for m in items if m["algo_type"] == "normal"),
            "crazy": sum(1 for m in items if m["algo_type"] == "crazy"),
            "watchlist": len(watchlist),
            "promoted": len(promoted),
            "graveyard": len(graveyard),
        },
        "by_status": dict(sorted(Counter(m["status"] for m in items).items())),
        "by_evidence_class": dict(sorted(Counter(m["evidence_class"] for m in items).items())),
        "new_algos_today": [m for m in items if m.get("new_algo_date") == run_date],
        "top_live_ytd": sorted(items, key=lambda m: m["ytd_pct"], reverse=True)[:10],
    }

    outputs = {
        "algos_index.json": {"generated_at": daily_summary["generated_at"], "algos": items},
        "families.json": {"generated_at": daily_summary["generated_at"], "families": family_rollup},
        "watchlist.json": {"generated_at": daily_summary["generated_at"], "algos": watchlist},
        "promoted.json": {"generated_at": daily_summary["generated_at"], "algos": promoted},
        "graveyard.json": {"generated_at": daily_summary["generated_at"], "algos": graveyard},
        "daily_summary.json": daily_summary,
    }
    for name, payload in outputs.items():
        (PRODUCT_DIR / name).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"[write] {PRODUCT_DIR / 'algos_index.json'}")
    print(f"[write] {PRODUCT_DIR / 'families.json'}")
    print(f"[write] {PRODUCT_DIR / 'watchlist.json'}")
    print(f"[write] {PRODUCT_DIR / 'promoted.json'}")
    print(f"[write] {PRODUCT_DIR / 'graveyard.json'}")
    print(f"[write] {PRODUCT_DIR / 'daily_summary.json'}")
    print(f"[done] algos={len(items)} watchlist={len(watchlist)} promoted={len(promoted)} graveyard={len(graveyard)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
