import json
import os
from datetime import datetime


def _load_state(path: str):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def _collect_trade_log(state: dict, algo_id: str, algo_name: str):
    trades = []
    for t in state.get("trade_log", []):
        t2 = dict(t)
        t2["algo_id"] = algo_id
        t2["algo_name"] = algo_name
        trades.append(t2)
    return trades


def write_normal_ledger():
    ledger = []

    # Algo1 (existing baseline) from state.json
    baseline = _load_state("state.json")
    if baseline:
        ledger.extend(_collect_trade_log(baseline, "nrwise", "NRWise Acceleration"))

    # Algo2-4 normal states
    normal_dir = "data/normal/state"
    if os.path.isdir(normal_dir):
        for fname in os.listdir(normal_dir):
            if not fname.endswith(".json"):
                continue
            algo_id = fname.replace(".json", "")
            state = _load_state(os.path.join(normal_dir, fname))
            if not state:
                continue
            meta = state.get("meta", {}).get(algo_id, {})
            algo_name = meta.get("name") or algo_id
            ledger.extend(_collect_trade_log(state, algo_id, algo_name))

    def _parse_date(x):
        try:
            return datetime.fromisoformat(x)
        except Exception:
            return datetime.min

    ledger.sort(key=lambda x: _parse_date(x.get("date", "")))

    os.makedirs("docs/ledgers", exist_ok=True)
    with open("docs/ledgers/normal_ledger.json", "w") as f:
        json.dump(ledger, f, indent=2, default=str)
