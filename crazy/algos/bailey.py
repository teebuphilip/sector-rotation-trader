from datetime import date

import pandas as pd

from config import SECTOR_ETFS
from scanner import safe_download
from .base import CrazyAlgoBase


class BaileyAlgo(CrazyAlgoBase):
    algo_id = "baileymol"
    name = "Algo Baileymol (Chaos Monger)"
    rebalance_frequency = "weekly"
    supports_historical_seed = True

    STOP_LOSS_PCT = 0.08

    def universe(self):
        return list(SECTOR_ETFS)

    def _is_monday(self, as_of: date) -> bool:
        return as_of.weekday() == 0

    def _is_friday(self, as_of: date) -> bool:
        return as_of.weekday() == 4

    def should_rebalance(self, as_of: date, state: dict, signal: str) -> bool:
        return self._is_monday(as_of) or self._is_friday(as_of) or signal == "STOP_LOSS"

    def _stop_loss_triggered(self, state: dict) -> bool:
        if not state.get("positions"):
            return False
        tickers = list(state["positions"].keys())
        raw = safe_download(tickers, period="2mo")
        if raw.empty:
            return False
        prices = raw["Close"] if "Close" in raw.columns else raw
        for t, pos in state["positions"].items():
            if t not in prices.columns:
                continue
            s = prices[t].dropna()
            if s.empty:
                continue
            cur = float(s.iloc[-1])
            loss_pct = (cur - pos["entry_price"]) / pos["entry_price"]
            if loss_pct <= -self.STOP_LOSS_PCT:
                return True
        return False

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        if self._stop_loss_triggered(state):
            meta = self.meta(state)
            meta["signal_label"] = "STOP_LOSS"
            meta["signal_key"] = "STOP_LOSS"
            return "STOP_LOSS"

        if self._is_friday(as_of):
            meta = self.meta(state)
            meta["signal_label"] = "FRIDAY_EXIT"
            meta["signal_key"] = "FRIDAY_EXIT"
            return "FRIDAY_EXIT"

        if not self._is_monday(as_of):
            return "HOLD"

        raw = safe_download(SECTOR_ETFS, period="1y")
        if raw.empty:
            return "HOLD"
        prices = raw["Close"] if "Close" in raw.columns else raw
        returns = prices.pct_change().dropna()
        rolling = returns.rolling(30).std()
        current_vol = rolling.iloc[-1].dropna()
        if current_vol.empty:
            return "HOLD"

        hist_avg = float(rolling.stack().mean())
        current_avg = float(current_vol.mean())
        meta = self.meta(state)
        if current_avg < hist_avg:
            meta["signal_label"] = "CHAOS_SLEEPING"
            meta["signal_key"] = "CHAOS_SLEEPING"
            return "CHAOS_SLEEPING"

        top3 = current_vol.sort_values(ascending=False).head(3).index.tolist()
        meta["target_sectors"] = top3
        meta["signal_label"] = f"TOP:{','.join(top3)}"
        meta["signal_key"] = "|".join(top3)
        return "CHAOS_ON"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal in ("STOP_LOSS", "FRIDAY_EXIT", "CHAOS_SLEEPING"):
            return {}
        if signal != "CHAOS_ON":
            return None
        meta = self.meta(state)
        top3 = meta.get("target_sectors", [])
        if not top3:
            return None
        per = 1.0 / len(top3)
        return {t: per for t in top3}
