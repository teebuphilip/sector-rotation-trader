from datetime import date, timedelta

import requests

from crazy.algos.base import CrazyAlgoBase


_EDGAR_HEADERS = {"User-Agent": "sector-rotation-research research@example.com"}
_EDGAR_SEARCH = (
    "https://efts.sec.gov/LATEST/search-index?"
    "q=%22transactionCode%3A+P%22&forms=4"
    "&dateRange=custom&startdt={start}&enddt={end}"
    "&hits.hits.total.value=true"
)

BUY_SURGE_THRESHOLD = 200
BUY_DROUGHT_THRESHOLD = 40
LOOKBACK_DAYS = 30


def _count_form4_purchases(as_of: date) -> int:
    start = (as_of - timedelta(days=LOOKBACK_DAYS)).isoformat()
    end = as_of.isoformat()
    try:
        r = requests.get(
            _EDGAR_SEARCH.format(start=start, end=end),
            headers=_EDGAR_HEADERS,
            timeout=15,
        )
        data = r.json()
        return int(data.get("hits", {}).get("total", {}).get("value", 0))
    except Exception:
        return -1


class InsiderTradingSignalsAlgo(CrazyAlgoBase):
    algo_id = "insider-trading-signals"
    name = "Insider Trading Signals"
    family = "political_insider_filing"
    rebalance_frequency = "weekly"
    supports_historical_seed = False

    def universe(self):
        return ["XLF", "XLK", "XLY", "XLP", "XLU"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        count = _count_form4_purchases(as_of)
        meta = self.meta(state)
        meta["form4_buys_30d"] = count

        if count < 0:
            meta["signal_label"] = "HOLD"
            return "HOLD"

        if count >= BUY_SURGE_THRESHOLD:
            meta["signal_label"] = "INSIDER_SURGE"
            return "INSIDER_SURGE"
        if count <= BUY_DROUGHT_THRESHOLD:
            meta["signal_label"] = "INSIDER_DROUGHT"
            return "INSIDER_DROUGHT"

        meta["signal_label"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "INSIDER_SURGE":
            return {"XLF": 0.35, "XLK": 0.35, "XLY": 0.30}
        if signal == "INSIDER_DROUGHT":
            return {"XLP": 0.50, "XLU": 0.50}
        return None
