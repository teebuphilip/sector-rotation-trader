from datetime import date

import pandas as pd

from config import SECTOR_ETFS
from scanner import safe_download
from .base import NormalAlgoBase


class BaileyAlgo(NormalAlgoBase):
    algo_id = "baileymol"
    name = "Algo Baileymol (Chaos Monger)"
    rebalance_frequency = "weekly"

    STOP_LOSS_PCT = 0.08

    def universe(self):
        return list(SECTOR_ETFS)

    def _is_monday(self, as_of: date) -> bool:
        return as_of.weekday() == 0

    def _is_friday(self, as_of: date) -> bool:
        return as_of.weekday() == 4

    def _stop_loss_triggered(self, state: dict) -> bool:
        if not state.get("positions"):
            return False
        try:
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
        except Exception:
            return False

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        if self._is_friday(as_of):
            return {}

        state = getattr(self, "_state_ref", {})
        if self._stop_loss_triggered(state):
            return {}

        if not self._is_monday(as_of):
            return None

        if prices.empty:
            return {}
        returns = prices[list(SECTOR_ETFS)].pct_change().dropna()
        rolling = returns.rolling(30).std()
        current_vol = rolling.iloc[-1].dropna()
        if current_vol.empty:
            return {}
        hist_avg = float(rolling.stack().mean())
        current_avg = float(current_vol.mean())
        if current_avg < hist_avg:
            return {}
        top3 = current_vol.sort_values(ascending=False).head(3).index.tolist()
        per = 1.0 / len(top3)
        return {t: per for t in top3}
