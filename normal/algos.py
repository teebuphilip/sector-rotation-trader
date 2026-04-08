from datetime import date
import pandas as pd

from scanner import safe_download
from config import SECTOR_ETFS


class NormalAlgoBase:
    algo_id = "base"
    name = "Base"
    rebalance_frequency = "monthly_eom"  # daily | monthly_eom

    def universe(self):
        return []

    def meta(self, state: dict) -> dict:
        state.setdefault("meta", {})
        state["meta"].setdefault(self.algo_id, {})
        return state["meta"][self.algo_id]

    def should_rebalance(self, as_of: date, is_eom: bool) -> bool:
        if self.rebalance_frequency == "daily":
            return True
        if self.rebalance_frequency == "monthly_eom":
            return is_eom
        return False

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        return {}


class FaberMomentumAlgo(NormalAlgoBase):
    algo_id = "faber"
    name = "Faber Momentum Rotation"
    rebalance_frequency = "monthly_eom"

    def universe(self):
        return list(SECTOR_ETFS) + ["SPY"]

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        monthly = prices.resample("M").last().dropna(how="all")
        if len(monthly) < 12:
            return {}

        # SPY 10-month SMA filter
        spy = monthly["SPY"].dropna()
        if len(spy) < 10:
            return {}
        spy_sma10 = spy.rolling(10).mean().iloc[-1]
        if spy.iloc[-1] < spy_sma10:
            return {}

        sectors = monthly[SECTOR_ETFS].dropna(how="all")
        if len(sectors) < 4:
            return {}

        returns_3m = sectors.iloc[-1] / sectors.iloc[-4] - 1
        top3 = returns_3m.sort_values(ascending=False).head(3).index.tolist()
        weight = 1.0 / len(top3)
        return {t: weight for t in top3}


class DMSRAlgo(NormalAlgoBase):
    algo_id = "dmsr"
    name = "Antonacci Dual Momentum Sector Rotation"
    rebalance_frequency = "monthly_eom"

    def universe(self):
        return list(SECTOR_ETFS) + ["SPY", "AGG"]

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        monthly = prices.resample("M").last().dropna(how="all")
        if len(monthly) < 13:
            return {}

        spy = monthly["SPY"].dropna()
        if len(spy) < 13:
            return {}
        spy_12m = spy.iloc[-1] / spy.iloc[-13] - 1
        if spy_12m < 0:
            return {"AGG": 1.0}

        sectors = monthly[SECTOR_ETFS].dropna(how="all")
        returns_12m = sectors.iloc[-1] / sectors.iloc[-13] - 1
        top4 = returns_12m.sort_values(ascending=False).head(4).index.tolist()
        weight = 1.0 / len(top4)
        return {t: weight for t in top4}


class SimpleMonthlyAlgo(NormalAlgoBase):
    algo_id = "simple_monthly"
    name = "Quantified Simple Monthly Rotation"
    rebalance_frequency = "monthly_eom"

    def universe(self):
        return ["SPY", "EEM", "TLT"]

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        monthly = prices.resample("M").last().dropna(how="all")
        if len(monthly) < 2:
            return {}

        last = monthly.iloc[-1]
        prev = monthly.iloc[-2]
        returns_1m = (last / prev) - 1
        top = returns_1m.sort_values(ascending=False).head(1).index.tolist()
        return {top[0]: 1.0} if top else {}


class BiscottiAlgo(NormalAlgoBase):
    algo_id = "biscotti"
    name = "Algo Biscotti (Unconditional Loyalty)"
    rebalance_frequency = "monthly_eom"

    def universe(self):
        return list(SECTOR_ETFS)

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        if prices.empty:
            return {}
        window = prices[list(SECTOR_ETFS)].dropna(how="all")
        if len(window) < 31:
            return {}
        last = window.iloc[-1]
        first = window.iloc[-31]
        returns = (last / first) - 1
        returns = returns.dropna()
        if returns.empty:
            return {}
        worst = returns.sort_values().index[0]
        return {worst: 1.0}


def get_normal_algos():
    return [FaberMomentumAlgo(), DMSRAlgo(), SimpleMonthlyAlgo(), BiscottiAlgo(), BaileyAlgo()]


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

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        # Friday exit
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
