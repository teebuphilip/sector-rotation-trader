import json
import os
from datetime import datetime, timedelta


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def load_json(path: str, default=None):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {} if default is None else default


def save_json(path: str, data):
    ensure_dir(os.path.dirname(path) or ".")
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


def load_history(path: str):
    return load_json(path, default=[])


def append_history(path: str, entry: dict, key: str = "date"):
    history = load_history(path)
    key_val = entry.get(key)
    if key_val is None:
        history.append(entry)
    else:
        found = False
        for i, row in enumerate(history):
            if row.get(key) == key_val:
                history[i] = entry
                found = True
                break
        if not found:
            history.append(entry)
    save_json(path, history)
    return history


def cached_fetch(cache_path: str, ttl_hours: int, fetch_fn):
    now = datetime.utcnow()
    cache = load_json(cache_path, default={})
    fetched_at = cache.get("fetched_at")
    if fetched_at:
        try:
            ts = datetime.fromisoformat(fetched_at)
            if now - ts < timedelta(hours=ttl_hours):
                return cache.get("data")
        except ValueError:
            pass
    data = fetch_fn()
    save_json(cache_path, {"fetched_at": now.isoformat(), "data": data})
    return data
