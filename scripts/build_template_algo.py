#!/usr/bin/env python3
"""
Build a crazy algo from deterministic adapter templates.

This intentionally does not ask an LLM to write Python. It parses the published
markdown enough to pick adapter kwargs, thresholds, frequency, and universe, then
emits a boring long/flat algo that uses the selected adapter contract correctly.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote_plus

from adapter_router import route_text


ADAPTER_FUNCS = {
    "earthquake_activity": "fetch_earthquake_activity",
    "openchargemap": "fetch_openchargemap_counts",
    "google_trends": "fetch_google_trends",
    "rss_count": "fetch_rss_counts",
    "weather_series": "fetch_weather_series",
    "tsa_table": "fetch_tsa_table",
    "price_only": "fetch_prices",
    "eia_electricity": "fetch_eia_electricity",
    "port_container_volume": "fetch_port_container_volume",
}


VALUE_COLUMNS = {
    "earthquake_activity": ["quakes"],
    "openchargemap": ["count"],
    "google_trends": ["interest"],
    "rss_count": ["count"],
    "weather_series": ["temp_max", "precipitation"],
    "tsa_table": ["throughput"],
    "price_only": ["value"],
    "eia_electricity": ["value"],
    "port_container_volume": ["value", "total_teus"],
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _section(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        return ""
    start = match.end()
    next_match = re.search(r"^## .+?$", text[start:], flags=re.MULTILINE)
    end = start + next_match.start() if next_match else len(text)
    return text[start:end].strip()


def _title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _idea_id(text: str, fallback: str) -> str:
    match = re.search(r"\*\*Idea ID:\*\*\s*`([^`]+)`", text)
    return match.group(1).strip() if match else fallback


def _frequency(text: str) -> str:
    match = re.search(r"\*\*Frequency:\*\*\s*([A-Za-z]+)", text)
    value = match.group(1).strip().lower() if match else "daily"
    return value if value in {"daily", "weekly", "monthly"} else "daily"


def _universe(text: str) -> list[str]:
    sec = _section(text, "Universe")
    tickers = []
    for line in sec.splitlines():
        line = line.strip()
        if line.startswith("-"):
            ticker = line[1:].strip().upper()
            if ticker:
                tickers.append(ticker)
    return tickers or ["SPY"]


def _class_name(idea_id: str) -> str:
    return "".join(w.title() for w in idea_id.replace("-", " ").replace("_", " ").split()) + "Algo"


def _module_name(idea_id: str) -> str:
    return idea_id.replace("-", "_")


def _first_percent(text: str, default: float = 0.10) -> float:
    matches = re.findall(r"(\d+(?:\.\d+)?)\s*%", text)
    if not matches:
        return default
    value = float(matches[0]) / 100.0
    if value <= 0:
        return default
    return min(value, 2.0)


def _hold_period(text: str, frequency: str) -> int:
    lower = text.lower()
    week = re.search(r"after\s+(\d+)\s+weeks?", lower)
    day = re.search(r"after\s+(\d+)\s+(?:trading\s+)?days?", lower)
    if frequency == "weekly":
        if week:
            return max(int(week.group(1)) * 7, 7)
        if day:
            return max(int(day.group(1)), 7)
        return 21
    if day:
        return max(int(day.group(1)), 1)
    if week:
        return max(int(week.group(1)) * 7, 7)
    return 7


def _lookback_days(frequency: str) -> int:
    if frequency == "weekly":
        return 28
    if frequency == "monthly":
        return 90
    return 7


def _trend_direction(text: str) -> str:
    lower = text.lower()
    up_terms = ["increase", "increases", "rise", "rises", "surge", "surges", "above", "gain", "gains", "exceeds"]
    if any(term in lower for term in up_terms):
        return "up"
    drop_terms = ["drop", "drops", "decline", "declines", "falls", "below", "decrease", "decreases"]
    if any(term in lower for term in drop_terms):
        return "down"
    return "up"


def _keyword(text: str, title: str) -> str:
    quoted = re.findall(r"'([^']+)'|\"([^\"]+)\"", text)
    flat = [a or b for a, b in quoted if (a or b)]
    for item in flat:
        if 2 <= len(item) <= 60 and not item.startswith("http"):
            return item
    title_words = re.sub(r"[^A-Za-z0-9 ]+", " ", title).strip()
    return title_words or "market interest"


def _rss_urls(text: str, title: str) -> list[str]:
    urls = re.findall(r"https?://[^\s)]+", text)
    rss_urls = [u.strip(".,") for u in urls if "rss" in u.lower() or "feed" in u.lower()]
    if rss_urls:
        return rss_urls[:5]
    query = quote_plus(_keyword(text, title))
    return [f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"]


def _adapter_call(adapter: str, text: str, title: str, universe: list[str]) -> str:
    if adapter == "price_only":
        return f"fetch_prices(tickers={universe!r}, period=\"2y\")"
    if adapter == "google_trends":
        return f"fetch_google_trends(keyword={_keyword(text, title)!r}, days_back=180)"
    if adapter == "rss_count":
        return f"fetch_rss_counts(feed_urls={_rss_urls(text, title)!r}, days_back=180)"
    if adapter == "weather_series":
        return "fetch_weather_series(latitude=39.8283, longitude=-98.5795, days_back=180)"
    if adapter == "earthquake_activity":
        return "fetch_earthquake_activity(days_back=30)"
    if adapter == "openchargemap":
        return "fetch_openchargemap_counts(country_code=\"US\", max_results=1000)"
    if adapter == "tsa_table":
        return "fetch_tsa_table()"
    if adapter == "port_container_volume":
        return "fetch_port_container_volume()"
    if adapter == "eia_electricity":
        return "fetch_eia_electricity(api_key=os.getenv(\"EIA_API_KEY\", \"\"), days_back=180)"
    raise ValueError(f"Unsupported adapter: {adapter}")


def _validate_template_compatibility(adapter: str, text: str) -> None:
    lower = text.lower()
    short_terms = ["enter short", "short ", "shorting", "inverse exposure", "bearish allocation"]
    if any(term in lower for term in short_terms):
        raise SystemExit("Template builder does not support native short strategies yet")
    if adapter == "price_only" and "volume" in lower:
        raise SystemExit("price_only template does not support volume-based signals")


def _supports_historical_seed(adapter: str) -> bool:
    return adapter not in {"rss_count", "openchargemap"}


def _imports(adapter: str) -> str:
    func = ADAPTER_FUNCS[adapter]
    extra = "\nimport os" if adapter == "eia_electricity" else ""
    return f"""from datetime import date
{extra}
import pandas as pd
from typing import Optional
from crazy.algos.base import CrazyAlgoBase
from crazy.adapters.{adapter} import {func}
"""


def _code(
    *,
    adapter: str,
    idea_id: str,
    name: str,
    universe: list[str],
    frequency: str,
    threshold: float,
    direction: str,
    hold_days: int,
    adapter_call: str,
) -> str:
    class_name = _class_name(idea_id)
    value_columns = VALUE_COLUMNS[adapter]
    supports_hist = _supports_historical_seed(adapter)
    lookback_days = _lookback_days(frequency)

    return f'''{_imports(adapter)}

class {class_name}(CrazyAlgoBase):
    algo_id = "{idea_id}"
    name = "{name}"
    rebalance_frequency = "{frequency}"
    supports_historical_seed = {supports_hist}

    def universe(self):
        return {universe!r}

    def _value_column(self, df: pd.DataFrame) -> Optional[str]:
        for col in {value_columns!r}:
            if col in df.columns:
                return col
        numeric_cols = [
            c for c in df.columns
            if c != "date" and pd.api.types.is_numeric_dtype(df[c])
        ]
        return numeric_cols[0] if numeric_cols else None

    def _position_held(self, state: dict) -> bool:
        positions = state.get("positions", {{}}) if isinstance(state, dict) else {{}}
        return any(t in positions for t in self.universe())

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        meta = self.meta(state)
        df = {adapter_call}
        df = df if isinstance(df, pd.DataFrame) else pd.DataFrame()
        if df.empty or "date" not in df.columns:
            meta["signal_label"] = "HOLD"
            return "HOLD"

        df = df.copy()
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)
        if df.empty:
            meta["signal_label"] = "HOLD"
            return "HOLD"
        as_of_ts = pd.Timestamp(as_of)
        df = df[df["date"] <= as_of_ts]
        if df.empty:
            meta["signal_label"] = "HOLD"
            return "HOLD"

        value_col = self._value_column(df)
        if not value_col:
            meta["signal_label"] = "HOLD"
            return "HOLD"
        df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
        df = df.dropna(subset=[value_col])
        if len(df) < 3:
            meta["signal_label"] = "HOLD"
            return "HOLD"

        latest = df.iloc[-1]
        lookback_start = latest["date"] - pd.Timedelta(days={lookback_days})
        prior = df[(df["date"] < latest["date"]) & (df["date"] >= lookback_start)]
        if prior.empty:
            prior = df.iloc[:-1].tail(4)
        prior_avg = float(prior[value_col].mean()) if not prior.empty else 0.0
        latest_value = float(latest[value_col])
        if prior_avg == 0 or pd.isna(prior_avg):
            meta["signal_label"] = "HOLD"
            return "HOLD"

        change = (latest_value - prior_avg) / abs(prior_avg)
        meta["latest_value"] = round(latest_value, 4)
        meta["prior_avg"] = round(prior_avg, 4)
        meta["signal_change"] = round(change, 4)

        held = self._position_held(state)
        entry_date = meta.get("entry_date")
        days_held = 0
        if entry_date:
            entry_ts = pd.to_datetime(entry_date, errors="coerce")
            if not pd.isna(entry_ts):
                days_held = max((as_of_ts - entry_ts).days, 0)

        if held:
            should_exit = days_held >= {hold_days}
            if "{direction}" == "up":
                should_exit = should_exit or change < ({threshold} / 2.0)
            else:
                should_exit = should_exit or change > -({threshold} / 2.0)
            if should_exit:
                meta.pop("entry_date", None)
                meta["signal_label"] = "RISK_OFF"
                return "RISK_OFF"
            meta["signal_label"] = "HOLD"
            return "HOLD"

        if "{direction}" == "up":
            triggered = change > {threshold}
        else:
            triggered = change < -{threshold}
        if triggered:
            meta["entry_date"] = as_of_ts.date().isoformat()
            meta["signal_label"] = "RISK_ON"
            return "RISK_ON"

        meta["signal_label"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_OFF":
            return {{}}
        if signal == "RISK_ON":
            targets = list(self.universe())
            if not targets:
                return {{}}
            allocation_per_signal = 0.05
            max_total_exposure = 0.20
            allocation = {{t: allocation_per_signal for t in targets}}
            total_alloc = sum(allocation.values())
            if total_alloc > max_total_exposure:
                scale = max_total_exposure / total_alloc
                allocation = {{k: v * scale for k, v in allocation.items()}}
            return allocation
        return {{}}
'''


def build(spec_file: Path, out: Path, adapter: str | None = None) -> dict:
    text = _read(spec_file)
    idea_id = _idea_id(text, spec_file.stem.split("_", 1)[-1])
    name = _title(text, idea_id.replace("-", " ").title())
    universe = _universe(text)
    frequency = _frequency(text)
    signal_logic = _section(text, "Signal Logic")
    signal_text = "\n".join([
        signal_logic,
        _section(text, "Entry / Exit"),
        _section(text, "Data Sources"),
    ])
    selected = adapter or (route_text(text)[0] if route_text(text) else "")
    if selected not in ADAPTER_FUNCS:
        raise SystemExit(f"Unsupported or missing adapter for template build: {selected}")
    _validate_template_compatibility(selected, text)

    threshold = _first_percent(signal_text)
    direction = _trend_direction(signal_logic or signal_text)
    hold_days = _hold_period(signal_text, frequency)
    adapter_call = _adapter_call(selected, signal_text + "\n" + text, name, universe)

    code = _code(
        adapter=selected,
        idea_id=idea_id,
        name=name,
        universe=universe,
        frequency=frequency,
        threshold=threshold,
        direction=direction,
        hold_days=hold_days,
        adapter_call=adapter_call,
    )
    _write(out, code)
    return {
        "spec_file": str(spec_file),
        "out": str(out),
        "adapter": selected,
        "idea_id": idea_id,
        "name": name,
        "universe": universe,
        "frequency": frequency,
        "threshold": threshold,
        "direction": direction,
        "hold_days": hold_days,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec-file", required=True)
    parser.add_argument("--output-path", required=True)
    parser.add_argument("--adapter", default=None)
    parser.add_argument("--report", default=None)
    args = parser.parse_args()

    report = build(Path(args.spec_file), Path(args.output_path), adapter=args.adapter)
    print(
        f"[template-build] adapter={report['adapter']} "
        f"algo_id={report['idea_id']} out={report['out']}"
    )
    if args.report:
        _write(Path(args.report), json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
