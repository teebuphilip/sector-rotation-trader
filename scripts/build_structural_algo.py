#!/usr/bin/env python3
"""
Build a structurally-correct algo file using adapters and a fixed skeleton.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ADAPTER_FUNCS = {
    "reddit_activity": "fetch_reddit_activity",
    "twitter_activity": "fetch_twitter_activity",
    "weather_series": "fetch_weather_series",
    "earthquake_activity": "fetch_earthquake_activity",
    "google_trends": "fetch_google_trends",
    "openchargemap": "fetch_openchargemap_counts",
    "fred_series": "fetch_fred_series",
    "tsa_table": "fetch_tsa_table",
    "socrata_311": "fetch_311_counts",
    "rss_count": "fetch_rss_counts",
    "html_table": "fetch_html_table",
    "price_only": "fetch_prices",
    "eia_electricity": "fetch_eia_electricity",
    "port_container_volume": "fetch_port_container_volume",
    "bts_airline_load_factor": "fetch_bts_airline_load_factor",
}


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sliced", required=True, help="Path to sliced_spec.json")
    parser.add_argument("--out", required=True, help="Output algo file")
    args = parser.parse_args()

    sliced = _read_json(Path(args.sliced))
    adapters = sliced.get("adapters") or []
    spec = sliced.get("sliced_spec") or {}

    if not adapters:
        raise SystemExit("No adapters in sliced spec")

    adapter = adapters[0]
    func = ADAPTER_FUNCS.get(adapter, "")
    if not func:
        raise SystemExit(f"Unknown adapter: {adapter}")

    algo_id = spec.get("id", "new-algo")
    name = spec.get("name", "New Algo")
    universe = spec.get("universe", [])
    universe_list = ", ".join([f"\"{u}\"" for u in universe]) or ""
    supports_hist = "False" if adapter == "reddit_activity" else "True"

    adapter_args = ""
    if adapter == "reddit_activity":
        adapter_args = "subreddits=[\"r/gaming\", \"r/pcgaming\", \"r/games\"]"
    elif adapter == "eia_electricity":
        adapter_args = "api_key=\"\""

    code = f"""from datetime import date
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.adapters.{adapter} import {func}


class {''.join([w.title() for w in algo_id.replace('-', ' ').split()])}Algo(CrazyAlgoBase):
    algo_id = "{algo_id}"
    name = "{name}"
    rebalance_frequency = "daily"
    supports_historical_seed = {supports_hist}

    def universe(self):
        return [{universe_list}]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        # === SIGNAL_LOGIC_START ===
        data = {func}({adapter_args})
        df = data if isinstance(data, pd.DataFrame) else pd.DataFrame()
        if df.empty:
            return "HOLD"
        return "HOLD"
        # === SIGNAL_LOGIC_END ===

    def target_allocations(self, signal: str, state: dict, as_of: date):
        # === ALLOCATION_LOGIC_START ===
        if signal == "RISK_ON":
            weight = 0.20 / len(self.universe()) if self.universe() else 0.0
            return {{t: weight for t in self.universe()}}
        if signal == "RISK_OFF":
            return {{}}
        return None
        # === ALLOCATION_LOGIC_END ===
"""

    _write(Path(args.out), code)
    print(f"[build] adapter={adapter} algo_id={algo_id} out={args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
