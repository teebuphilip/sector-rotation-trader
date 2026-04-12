from datetime import date
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.adapters.google_trends import fetch_google_trends


class CloudStorageDemandSurgeAlgo(CrazyAlgoBase):
    algo_id = "cloud-storage-demand-surge"
    name = "Cloud Storage Demand Surge"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["BOX", "DBX", "GOOGL", "MSFT"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        # === SIGNAL_LOGIC_START ===
        try:
            data = fetch_google_trends(keyword="cloud storage", days_back=400)
        except Exception:
            return "HOLD"
        df = data if isinstance(data, pd.DataFrame) else pd.DataFrame()
        if df.empty:
            return "HOLD"
        # Calculate 90th percentile of past 12 months (approx 365 days)
        df['date'] = pd.to_datetime(df['date'])
        cutoff_date = df['date'].max() - pd.Timedelta(days=365)
        recent_data = df[df['date'] > cutoff_date]
        if recent_data.empty:
            return "HOLD"
        threshold = recent_data['interest'].quantile(0.9)
        latest_date = df['date'].max()
        latest_interest = df.loc[df['date'] == latest_date, 'interest'].values
        if len(latest_interest) == 0:
            return "HOLD"
        latest_interest = latest_interest[0]
        # Placeholder for Alexa and SEC signals
        alexa_signal = getattr(self, 'get_alexa_signal', lambda: False)()
        sec_signal = getattr(self, 'get_sec_signal', lambda: False)()
        # If no position, check entry condition: all signals confirm surge
        if not hasattr(self, 'position_entry_date') or self.position_entry_date is None:
            if latest_interest > threshold and alexa_signal and sec_signal:
                self.position_entry_date = latest_date
                return "RISK_ON"
            else:
                return "HOLD"
        else:
            # Position is open, check exit condition:
            # Exit if interest below threshold for 5 consecutive days OR position held for more than 90 days
            last_5_days = df[(df['date'] > latest_date - pd.Timedelta(days=5)) & (df['date'] <= latest_date)]
            if len(last_5_days) < 5:
                return "HOLD"
            sustained_decline = (last_5_days['interest'] < threshold).all()
            days_held = (latest_date - self.position_entry_date).days
            if sustained_decline or days_held > 90:
                self.position_entry_date = None
                return "RISK_OFF"
            else:
                return "RISK_ON"
        # === SIGNAL_LOGIC_END ===

    def target_allocations(self, signal: str, state: dict, as_of: date):
        # === ALLOCATION_LOGIC_START ===
        if signal == "RISK_ON":
            try:
                data = fetch_google_trends(keyword="cloud storage", days_back=400)
            except Exception:
                return {}
            df = data if isinstance(data, pd.DataFrame) else pd.DataFrame()
            if df.empty:
                return {}
            df['date'] = pd.to_datetime(df['date'])
            cutoff_date = df['date'].max() - pd.Timedelta(days=365)
            recent_data = df[df['date'] > cutoff_date]
            if recent_data.empty:
                return {}
            threshold = recent_data['interest'].quantile(0.9)
            latest_date = df['date'].max()
            latest_interest = df.loc[df['date'] == latest_date, 'interest'].values
            if len(latest_interest) == 0:
                return {}
            latest_interest = latest_interest[0]
            # Placeholder for Alexa and SEC signals strength
            alexa_strength = getattr(self, 'get_alexa_strength', lambda: 0.0)()
            sec_strength = getattr(self, 'get_sec_strength', lambda: 0.0)()
            # Combine strengths weighted equally
            interest_strength = max(0.0, min((latest_interest - threshold) / threshold, 1.0))
            combined_strength = (interest_strength + alexa_strength + sec_strength) / 3
            total_allocation = 0.2 + 0.2 * combined_strength  # between 20% and 40%
            universe = self.universe()
            if not universe:
                return {}
            weight = total_allocation / len(universe)
            return {t: weight for t in universe}
        if signal == "RISK_OFF":
            return {}
        if signal == "HOLD":
            return {}
        return None
        # === ALLOCATION_LOGIC_END ===
