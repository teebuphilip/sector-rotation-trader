from datetime import date
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.adapters.google_trends import fetch_google_trends


class HealthcareSectorGoogleTrendsFluSurgeAlgo(CrazyAlgoBase):
    algo_id = "healthcare-sector-google-trends-flu-surge"
    name = "Healthcare Sector Google Trends Flu Surge"
    rebalance_frequency = "weekly"
    supports_historical_seed = True

    def universe(self):
        return ["XLV"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        # === SIGNAL_LOGIC_START ===
        data = fetch_google_trends(keyword="Healthcare Sector Google Trends", days_back=90)
        df = data if isinstance(data, pd.DataFrame) else pd.DataFrame()
        meta = self.meta(state)
        positions = state.get("positions", {}) if isinstance(state, dict) else {}
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
# === SIGNAL_LOGIC_END ===

    def target_allocations(self, signal: str, state: dict, as_of: date):
        # === ALLOCATION_LOGIC_START ===
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
# === ALLOCATION_LOGIC_END ===