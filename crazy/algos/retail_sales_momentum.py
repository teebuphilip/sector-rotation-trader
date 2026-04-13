import os
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class RetailSalesMomentumAlgo(CrazyAlgoBase):
    algo_id = "retail-sales-momentum"
    name = "Retail Sales Momentum"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    # 3-month rate of change on retail sales ex food services
    ROC_BULL = 0.02    # rising retail sales → consumer spending up
    ROC_BEAR = -0.02   # falling retail sales → pullback

    def universe(self):
        return ["XLY", "XLK", "XLF", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        try:
            from fredapi import Fred
            fred = Fred(api_key=api_key)
            retail = fred.get_series("RSXFS")
        except Exception:
            return "HOLD"

        if retail is None or len(retail) < 6:
            return "HOLD"

        df = pd.DataFrame({"retail": retail}).dropna()
        df["roc_3m"] = df["retail"].pct_change(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        roc = latest["roc_3m"]

        meta = self.meta(state)
        meta["retail_level"] = int(latest["retail"])
        meta["roc_3m"] = round(float(roc), 4)

        if roc > self.ROC_BULL:
            meta["signal_label"] = "EXPANDING"
            meta["signal_key"] = "EXPANDING"
            return "EXPANDING"
        if roc < self.ROC_BEAR:
            meta["signal_label"] = "CONTRACTING"
            meta["signal_key"] = "CONTRACTING"
            return "CONTRACTING"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "EXPANDING":
            return {"XLY": 0.40, "XLK": 0.35, "XLF": 0.25}
        if signal == "CONTRACTING":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
