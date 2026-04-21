from datetime import date, timedelta

import pandas as pd
import requests

from crazy.algos.base import CrazyAlgoBase


# FINRA RegSHO daily short volume — free, no key needed
_FINRA_URL = "https://cdn.finra.org/equity/regsho/daily/CNMSshvol{date}.txt"

# Sector ETF tickers to monitor for dark pool activity
_MONITOR = ["SPY", "QQQ", "XLK", "XLF", "XLY", "XLP", "XLU", "XLV", "XLI", "XLB", "XLRE"]

SHORT_RATIO_HIGH = 0.55
SHORT_RATIO_LOW = 0.35
LOOKBACK_DAYS = 5


def _fetch_short_ratio(as_of: date) -> float:
    """Return mean short-volume ratio across monitored tickers for the most recent available day."""
    for lag in range(7):
        day = as_of - timedelta(days=lag)
        if day.weekday() >= 5:
            continue
        url = _FINRA_URL.format(date=day.strftime("%Y%m%d"))
        try:
            r = requests.get(url, timeout=15)
            if r.status_code != 200:
                continue
            lines = r.text.strip().splitlines()
            if len(lines) < 2:
                continue
            header = lines[0].split("|")
            rows = [dict(zip(header, l.split("|"))) for l in lines[1:] if l.strip()]
            df = pd.DataFrame(rows)
            df = df[df["Symbol"].isin(_MONITOR)].copy()
            if df.empty:
                continue
            df["ShortVolume"] = pd.to_numeric(df.get("ShortVolume", pd.Series()), errors="coerce")
            df["TotalVolume"] = pd.to_numeric(df.get("TotalVolume", pd.Series()), errors="coerce")
            df = df.dropna(subset=["ShortVolume", "TotalVolume"])
            df = df[df["TotalVolume"] > 0]
            if df.empty:
                continue
            df["ratio"] = df["ShortVolume"] / df["TotalVolume"]
            return float(df["ratio"].mean())
        except Exception:
            continue
    return -1.0


class FinraDarkPoolSignalAlgo(CrazyAlgoBase):
    algo_id = "finra-dark-pool-signal"
    name = "FINRA Dark Pool Signal"
    family = "political_insider_filing"
    rebalance_frequency = "weekly"
    supports_historical_seed = False

    def universe(self):
        return ["XLK", "XLF", "XLY", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        ratio = _fetch_short_ratio(as_of)
        meta = self.meta(state)
        meta["short_ratio"] = round(ratio, 4) if ratio >= 0 else None

        if ratio < 0:
            meta["signal_label"] = "HOLD"
            return "HOLD"

        if ratio >= SHORT_RATIO_HIGH:
            meta["signal_label"] = "HIGH_SHORT"
            return "HIGH_SHORT"
        if ratio <= SHORT_RATIO_LOW:
            meta["signal_label"] = "LOW_SHORT"
            return "LOW_SHORT"

        meta["signal_label"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "HIGH_SHORT":
            return {"XLP": 0.40, "XLU": 0.35, "XLV": 0.25}
        if signal == "LOW_SHORT":
            return {"XLK": 0.40, "XLF": 0.35, "XLY": 0.25}
        return None
