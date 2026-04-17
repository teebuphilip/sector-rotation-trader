#!/usr/bin/env python3
"""
Deterministic adapter router for crazy ideas.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ADAPTER_KEYWORDS = {
    "earthquake_activity": ["earthquake", "seismic", "usgs", "tectonic"],
    "openchargemap": ["openchargemap", "ev charger", "charging station", "charge station", "ev charging", "ev station"],
    "twitter_activity": ["twitter", "x.com", "tweet", "tweets", "hashtag", "social media", "superbowl"],
    "reddit_activity": ["reddit", "subreddit", "posts", "comments", "upvotes", "r/"],
    "weather_series": ["weather", "temperature", "precipitation", "storm", "rainfall", "hurricane"],
    "fred_series": ["fred", "economic data", "series id", "federal reserve"],
    "tsa_table": ["tsa", "passenger", "throughput", "airport"],
    "socrata_311": ["311", "socrata", "city complaints", "complaint_type"],
    "google_trends": ["google trends", "trends", "search interest", "search volume"],
    "rss_count": ["rss", "feed", "news feed"],
    "html_table": ["html table", "scrape", "table", "web table", "insider", "form 4", "sec", "capitol trades"],
    "eia_electricity": ["eia", "electricity", "power demand", "electric power", "grid demand"],
    "port_container_volume": ["port of los angeles", "container", "containers", "teu", "shipping volume", "port volume"],
    "bts_airline_load_factor": ["bts", "airline load factor", "airline traffic", "air traffic", "aviation traffic", "t-100"],
    "price_only": ["price", "momentum", "returns", "yahoo finance", "technical"],
}

MIN_SCORE = 2


def route_text(text: str) -> list[str]:
    text_l = text.lower()

    scores = {}
    for adapter, keys in ADAPTER_KEYWORDS.items():
        score = 0
        for k in keys:
            if k in text_l:
                if adapter == "twitter_activity":
                    score += 2
                else:
                    score += 1
        if score:
            scores[adapter] = score

    if not scores:
        return []

    # Pick highest score, then apply deterministic tie-breakers
    max_score = max(scores.values())
    top = [a for a, s in scores.items() if s == max_score]

    # Allow multi-adapter combos for known multi-source specs
    multi_adapters = set()
    if "fred" in text_l or "federal reserve" in text_l or "freight transportation" in text_l or "usda" in text_l:
        multi_adapters.add("fred_series")
    if "google trends" in text_l or "search interest" in text_l or "search volume" in text_l:
        multi_adapters.add("google_trends")
    if "twitter" in text_l or "x.com" in text_l or "tweet" in text_l or "social media" in text_l:
        multi_adapters.add("twitter_activity")
    if "eia" in text_l or "electricity" in text_l or "power demand" in text_l:
        multi_adapters.add("eia_electricity")
    if "port of los angeles" in text_l or "teu" in text_l or "container volume" in text_l:
        multi_adapters.add("port_container_volume")
    if "bts" in text_l or "airline load factor" in text_l or "airline traffic" in text_l:
        multi_adapters.add("bts_airline_load_factor")
    if multi_adapters:
        return sorted(list(set(top) | multi_adapters))

    if len(top) == 1:
        return [top[0]]

    # Tie-breaker priority (AFH-style)
    priority = [
        "html_table",
        "eia_electricity",
        "port_container_volume",
        "bts_airline_load_factor",
        "fred_series",
        "earthquake_activity",
        "openchargemap",
        "weather_series",
        "google_trends",
        "reddit_activity",
        "twitter_activity",
        "price_only",
        "rss_count",
        "socrata_311",
        "tsa_table",
    ]
    for p in priority:
        if p in top:
            return [p]

    # Fallback: return all top adapters for multi-adapter specs
    return top


def score_text(text: str) -> dict:
    text_l = text.lower()
    scores = {}
    for adapter, keys in ADAPTER_KEYWORDS.items():
        score = 0
        for k in keys:
            if k in text_l:
                if adapter == "twitter_activity":
                    score += 2
                else:
                    score += 1
        if score:
            scores[adapter] = score
    return scores


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec-file", required=True)
    args = parser.parse_args()

    spec_path = Path(args.spec_file)
    if not spec_path.exists():
        raise SystemExit(f"Spec file not found: {spec_path}")

    text = spec_path.read_text(encoding="utf-8")
    adapters = route_text(text)
    scores = score_text(text)
    top_score = max(scores.values()) if scores else 0
    confidence = "low" if top_score < MIN_SCORE else "ok"
    out = {"adapters": adapters, "scores": scores, "top_score": top_score, "confidence": confidence}
    print(json.dumps(out))
    if not adapters or top_score < MIN_SCORE:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
