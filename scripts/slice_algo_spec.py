#!/usr/bin/env python3
"""
Deterministic slicer: reduce grilled spec to adapter-specific minimal schema.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict


def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def slice_spec(spec: Dict[str, Any], adapters: list[str]) -> Dict[str, Any]:
    base = {
        "id": spec.get("id"),
        "name": spec.get("name"),
        "frequency": spec.get("frequency"),
        "universe": spec.get("universe", []),
        "entry_exit": spec.get("entry_exit", {}),
        "signal_logic": spec.get("signal_logic", {}),
        "position_sizing": spec.get("position_sizing", {}),
        "data_sources": {},
        "adapter_contracts": {},
    }

    data_sources = spec.get("data_sources", {}) or {}
    for adapter in adapters:
        if adapter == "reddit_activity":
            base["data_sources"]["reddit"] = data_sources.get("reddit", {})
            base["adapter_contracts"]["reddit_activity"] = {
                "func": "fetch_reddit_activity",
                "allowed_kwargs": ["subreddits", "days_back", "cache_key"],
                "returns": ["date", "posts", "comments"],
            }
        elif adapter == "twitter_activity":
            base["data_sources"]["twitter"] = data_sources.get("twitter", {})
            base["adapter_contracts"]["twitter_activity"] = {
                "func": "fetch_twitter_activity",
                "allowed_kwargs": ["query", "days_back", "cache_key"],
                "returns": ["date", "tweets"],
            }
        elif adapter == "fred_series":
            base["data_sources"]["fred"] = data_sources.get("fred", {})
            base["adapter_contracts"]["fred_series"] = {
                "func": "fetch_fred_series",
                "allowed_kwargs": ["series_id", "api_key"],
                "returns": ["date", "value"],
            }
        elif adapter == "google_trends":
            base["data_sources"]["google_trends"] = data_sources.get("google_trends", {})
            base["adapter_contracts"]["google_trends"] = {
                "func": "fetch_google_trends",
                "allowed_kwargs": ["keyword", "days_back"],
                "returns": ["date", "interest"],
            }
        elif adapter == "weather_series":
            base["data_sources"]["weather"] = data_sources.get("weather", {})
            base["adapter_contracts"]["weather_series"] = {
                "func": "fetch_weather_series",
                "allowed_kwargs": ["latitude", "longitude", "days_back"],
                "returns": ["date", "temp_max", "precipitation"],
            }
        elif adapter == "earthquake_activity":
            base["data_sources"]["earthquake"] = data_sources.get("earthquake", {})
            base["adapter_contracts"]["earthquake_activity"] = {
                "func": "fetch_earthquake_activity",
                "allowed_kwargs": ["days_back"],
                "returns": ["date", "quakes"],
            }
        elif adapter == "openchargemap":
            base["data_sources"]["openchargemap"] = data_sources.get("openchargemap", {})
            base["adapter_contracts"]["openchargemap"] = {
                "func": "fetch_openchargemap_counts",
                "allowed_kwargs": ["country_code", "max_results"],
                "returns": ["date", "count"],
            }
        elif adapter == "tsa_table":
            base["data_sources"]["tsa"] = data_sources.get("tsa", {})
            base["adapter_contracts"]["tsa_table"] = {
                "func": "fetch_tsa_table",
                "allowed_kwargs": [],
                "returns": ["date", "throughput", "throughput_yoy", "yoy_pct"],
            }
        elif adapter == "socrata_311":
            base["data_sources"]["socrata_311"] = data_sources.get("socrata_311", {})
            base["adapter_contracts"]["socrata_311"] = {
                "func": "fetch_311_counts",
                "allowed_kwargs": ["days_back"],
                "returns": ["complaint_type", "count"],
            }
        elif adapter == "rss_count":
            base["data_sources"]["rss"] = data_sources.get("rss", {})
            base["adapter_contracts"]["rss_count"] = {
                "func": "fetch_rss_counts",
                "allowed_kwargs": ["feed_urls", "days_back"],
                "returns": ["date", "count"],
            }
        elif adapter == "html_table":
            base["data_sources"]["html_table"] = data_sources.get("html_table", {})
            base["adapter_contracts"]["html_table"] = {
                "func": "fetch_html_table",
                "allowed_kwargs": ["url", "table_index"],
                "returns": ["table"],
            }
        elif adapter == "price_only":
            base["data_sources"]["price"] = data_sources.get("price", {})
            base["adapter_contracts"]["price_only"] = {
                "func": "fetch_prices",
                "allowed_kwargs": ["tickers", "period"],
                "returns": ["date", "value"],
            }

    return {"adapters": adapters, "sliced_spec": base}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--adapters", required=True, help="Comma-separated adapters")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    spec = _read_json(Path(args.spec))
    adapters = [a.strip() for a in args.adapters.split(",") if a.strip()]
    sliced = slice_spec(spec, adapters)
    _write_json(Path(args.out), sliced)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
