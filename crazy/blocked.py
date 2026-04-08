import json
import os
from datetime import datetime


def record_blocked(algo_id: str, name: str, keys: list[str], reason: str):
    os.makedirs("data/blocked", exist_ok=True)
    path = "data/blocked/algos.jsonl"
    entry = {
        "timestamp": datetime.utcnow().isoformat(timespec="seconds"),
        "algo_id": algo_id,
        "name": name,
        "keys": keys,
        "reason": reason,
    }
    with open(path, "a") as f:
        f.write(json.dumps(entry) + "\n")
