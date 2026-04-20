from datetime import date

import pandas as pd
from typing import Optional
from crazy.algos.base import CrazyAlgoBase
from crazy.adapters.openchargemap import fetch_openchargemap_counts


class TechnologySectorDailyEvChargerCountSurgeAlgo(CrazyAlgoBase):
    algo_id = "technology-sector-daily-ev-charger-count-surge"
    name = "Technology Sector Daily Ev Charger Count Surge"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ['XLK']

    def _value_column(self, df: pd.DataFrame) -> Optional[str]:
        for col in ['count']:
            if col in df.columns:
                return col
        numeric_cols = [
            c for c in df.columns
            if c != "date" and pd.api.types.is_numeric_dtype(df[c])
        ]
        return numeric_cols[0] if numeric_cols else None

    def _position_held(self, state: dict) -> bool:
        positions = state.get("positions", {}) if isinstance(state, dict) else {}
        return any(t in positions for t in self.universe())

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        meta = self.meta(state)
        df = fetch_openchargemap_counts(country_code="US", max_results=1000)
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
        lookback_start = latest["date"] - pd.Timedelta(days=7)
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
            should_exit = days_held >= 7
            if "up" == "up":
                should_exit = should_exit or change < (0.05 / 2.0)
            else:
                should_exit = should_exit or change > -(0.05 / 2.0)
            if should_exit:
                meta.pop("entry_date", None)
                meta["signal_label"] = "RISK_OFF"
                return "RISK_OFF"
            meta["signal_label"] = "HOLD"
            return "HOLD"

        if "up" == "up":
            triggered = change > 0.05
        else:
            triggered = change < -0.05
        if triggered:
            meta["entry_date"] = as_of_ts.date().isoformat()
            meta["signal_label"] = "RISK_ON"
            return "RISK_ON"

        meta["signal_label"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_OFF":
            return {}
        if signal == "RISK_ON":
            targets = list(self.universe())
            if not targets:
                return {}
            allocation_per_signal = 0.05
            max_total_exposure = 0.20
            allocation = {t: allocation_per_signal for t in targets}
            total_alloc = sum(allocation.values())
            if total_alloc > max_total_exposure:
                scale = max_total_exposure / total_alloc
                allocation = {k: v * scale for k, v in allocation.items()}
            return allocation
        return {}
