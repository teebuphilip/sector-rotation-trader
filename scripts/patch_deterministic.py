#!/usr/bin/env python3
"""
Deterministic patcher fallback that guarantees syntactically valid code.

This is intentionally boring. The LLM patcher can try to express the full spec;
this fallback exists to produce a validator-compliant, low-risk algo that can be
seeded instead of failing the whole factory on indentation/spec drift.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _extract_between(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0]


def _replace_between(text: str, start: str, end: str, replacement: str) -> str:
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return before + start + replacement + end + after


def _indent(lines: str, spaces: int = 8) -> str:
    prefix = " " * spaces
    out = []
    for line in lines.splitlines():
        if line.strip() == "":
            out.append("")
        else:
            out.append(prefix + line)
    return "\n" + "\n".join(out) + "\n"


def _adapter_call(adapter: str, func: str, universe: list[str], spec: dict) -> str:
    name = spec.get("name") or spec.get("id") or "market signal"
    first_ticker = (universe or ["SPY"])[0]
    if adapter == "reddit_activity":
        return f'{func}(subreddits=["r/stocks", "r/investing", "r/wallstreetbets"], days_back=30)'
    if adapter == "twitter_activity":
        return f'{func}(query="{name}", days_back=30)'
    if adapter == "weather_series":
        return f"{func}(latitude=40.7128, longitude=-74.0060, days_back=30)"
    if adapter == "earthquake_activity":
        return f"{func}(days_back=30)"
    if adapter == "google_trends":
        keyword = " ".join(str(name).replace("-", " ").split()[:4]) or first_ticker
        return f'{func}(keyword="{keyword}", days_back=90)'
    if adapter == "openchargemap":
        return f'{func}(country_code="US", max_results=1000)'
    if adapter == "fred_series":
        return f'{func}(series_id="DGS10", api_key="")'
    if adapter == "tsa_table":
        return f"{func}()"
    if adapter == "socrata_311":
        return f"{func}(days_back=30)"
    if adapter == "rss_count":
        return f'{func}(feed_urls=[], days_back=30)'
    if adapter == "html_table":
        return f'{func}(url="", table_index=0)'
    if adapter == "price_only":
        tickers = universe or [first_ticker]
        return f'{func}(tickers={tickers!r}, period="2y")'
    if adapter == "eia_electricity":
        return f'{func}(api_key="", respondent="US48", days_back=30, type_id="D")'
    if adapter == "port_container_volume":
        return f"{func}()"
    if adapter == "bts_airline_load_factor":
        return f"{func}()"
    return f"{func}()"


def _set_rebalance_frequency(code: str, spec: dict) -> str:
    frequency = str(spec.get("frequency") or "daily").lower()
    if frequency not in {"daily", "weekly", "monthly", "monthly_eom"}:
        frequency = "daily"
    return re.sub(
        r'rebalance_frequency\s*=\s*"[^"]+"',
        f'rebalance_frequency = "{frequency}"',
        code,
        count=1,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--spec", required=True)
    args = parser.parse_args()

    path = Path(args.file)
    code = _read(path)
    sliced = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    adapters = sliced.get("adapters") or []
    spec = sliced.get("sliced_spec") or {}

    adapter = adapters[0] if adapters else ""
    contract = (spec.get("adapter_contracts") or {}).get(adapter, {})
    func = contract.get("func") or ""
    universe = spec.get("universe", []) or []
    call = _adapter_call(adapter, func, universe, spec) if func else "pd.DataFrame()"

    signal_block = f"""
data = {call}
df = data if isinstance(data, pd.DataFrame) else pd.DataFrame()
meta = self.meta(state)
positions = state.get("positions", {{}}) if isinstance(state, dict) else {{}}
held = any(t in positions for t in self.universe())
if held:
    meta["signal_label"] = "RISK_OFF"
    meta["signal_key"] = "RISK_OFF"
    return "RISK_OFF"
if df.empty:
    meta["signal_label"] = "HOLD"
    meta["signal_key"] = "HOLD"
    return "HOLD"
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)
numeric_cols = [c for c in df.columns if c != "date" and pd.api.types.is_numeric_dtype(df[c])]
if not numeric_cols or len(df) < 2:
    meta["signal_label"] = "HOLD"
    meta["signal_key"] = "HOLD"
    return "HOLD"
series = pd.to_numeric(df[numeric_cols[0]], errors="coerce").dropna()
if len(series) < 2:
    meta["signal_label"] = "HOLD"
    meta["signal_key"] = "HOLD"
    return "HOLD"
latest_value = float(series.iloc[-1])
prev_value = float(series.iloc[-2])
if prev_value == 0:
    meta["signal_label"] = "HOLD"
    meta["signal_key"] = "HOLD"
    return "HOLD"
change = (latest_value - prev_value) / abs(prev_value)
meta["latest_value"] = round(latest_value, 4)
meta["signal_change"] = round(change, 4)
if change > 0.02:
    meta["signal_label"] = "RISK_ON"
    meta["signal_key"] = "RISK_ON"
    return "RISK_ON"
meta["signal_label"] = "HOLD"
meta["signal_key"] = "HOLD"
return "HOLD"
"""

    alloc_block = """
allocation_per_signal = 0.05
max_total_exposure = 0.20
if signal == "RISK_OFF":
    return {}
if signal == "RISK_ON":
    targets = list(self.universe())
    if not targets:
        return {}
    allocation = {t: allocation_per_signal for t in targets}
    total_alloc = sum(allocation.values())
    if total_alloc > max_total_exposure:
        scale = max_total_exposure / total_alloc
        allocation = {k: v * scale for k, v in allocation.items()}
    return allocation
return {}
"""

    code = _set_rebalance_frequency(code, spec)
    code = _replace_between(code, "# === SIGNAL_LOGIC_START ===", "# === SIGNAL_LOGIC_END ===", _indent(signal_block.strip()))
    code = _replace_between(code, "# === ALLOCATION_LOGIC_START ===", "# === ALLOCATION_LOGIC_END ===", _indent(alloc_block.strip()))
    _write(path, code)
    print("[patch-deterministic] applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
