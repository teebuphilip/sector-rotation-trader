from __future__ import annotations

import inspect
from dataclasses import dataclass
from pathlib import Path

from config import SECTOR_ETFS

SUPPORTED_PRICE_TICKERS = set(SECTOR_ETFS) | {"SPY"}
NON_PRICE_ADAPTER_MARKERS = [
    "crazy.adapters.google_trends",
    "crazy.adapters.fred_series",
    "crazy.adapters.rss_count",
    "crazy.adapters.weather_series",
    "crazy.adapters.earthquake_activity",
    "crazy.adapters.openchargemap",
    "crazy.adapters.eia_electricity",
    "crazy.adapters.socrata_311",
    "crazy.adapters.tsa_table",
    "crazy.adapters.html_table",
    "crazy.adapters.reddit",
    "crazy.adapters.twitter",
]


@dataclass
class BacktestClassification:
    status: str
    reason: str
    backtestable: bool = False


def _source_for_algo(algo) -> str:
    try:
        path = Path(inspect.getfile(algo.__class__))
        return path.read_text(encoding="utf-8")
    except Exception:
        try:
            return inspect.getsource(algo.__class__)
        except Exception:
            return ""


def classify_algo(algo, family: str = "crazy") -> BacktestClassification:
    universe = [str(t).upper() for t in (algo.universe() or [])]
    if not universe:
        return BacktestClassification("LIVE_ONLY_NON_PRICE", "Algo has no tradable ETF universe")

    unsupported_tickers = sorted(set(universe) - SUPPORTED_PRICE_TICKERS)
    if unsupported_tickers:
        return BacktestClassification(
            "UNSUPPORTED_UNIVERSE",
            f"V1 only supports SPY/sector ETFs; unsupported tickers: {', '.join(unsupported_tickers)}",
        )

    source = _source_for_algo(algo)
    # Native short exposure is rejected at runtime if target_allocations returns
    # negative weights. Static source checks are too noisy because long-only
    # mean-reversion logic often compare against negative thresholds.

    if family == "normal":
        if hasattr(algo, "compute_target"):
            return BacktestClassification("BACKTESTABLE", "Normal price-based algo interface", True)
        return BacktestClassification("LIVE_ONLY_NON_PRICE", "Normal algo lacks compute_target")

    for marker in NON_PRICE_ADAPTER_MARKERS:
        if marker in source:
            return BacktestClassification("LIVE_ONLY_NON_PRICE", f"Uses non-price adapter: {marker}")

    if "crazy.adapters.price_only" in source:
        if 'df[df["date"] <= as_of_ts]' in source or "df[df['date'] <= as_of_ts]" in source:
            return BacktestClassification("BACKTESTABLE", "Uses price_only adapter with as_of date filter", True)
        return BacktestClassification("NEEDS_HISTORY", "Uses price data but no visible as_of cutoff")

    if "safe_download" in source:
        return BacktestClassification(
            "NEEDS_HISTORY",
            "Uses direct safe_download; V1 requires refactor to point-in-time cached prices",
        )

    if getattr(algo, "supports_historical_seed", False):
        return BacktestClassification(
            "NEEDS_HISTORY",
            "Historical seed exists, but V1 cannot prove point-in-time price-only behavior",
        )

    return BacktestClassification("LIVE_ONLY_NON_PRICE", "No supported V1 price-only backtest path")
