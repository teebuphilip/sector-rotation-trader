from datetime import datetime, timedelta, date

import numpy as np
import pandas as pd

from .base import CrazyAlgoBase
from crazy.utils import load_history, append_history


class Calls311Algo(CrazyAlgoBase):
    algo_id = "calls311"
    name = "311 Call Rotation"
    rebalance_frequency = "weekly"
    supports_historical_seed = False

    COMPLAINT_CATEGORIES = {
        "infrastructure": [
            "Street Light Condition", "Pothole", "Street Condition",
            "Water System", "Broken Muni Meter", "Sidewalk Condition",
        ],
        "noise": [
            "Noise - Residential", "Noise - Street/Sidewalk",
            "Noise - Commercial", "Noise - Vehicle",
        ],
        "housing_stress": [
            "HEAT/HOT WATER", "Plumbing", "Paint/Plaster",
            "Rodent", "Unsanitary Condition",
        ],
        "business": [
            "Illegal Parking", "Blocked Driveway", "Derelict Vehicle",
            "Food Establishment", "Sidewalk Cafe",
        ],
    }

    WEIGHTS = {
        "infrastructure": 0.35,
        "housing_stress": 0.30,
        "noise": 0.20,
        "business": 0.15,
    }

    STRESS_DEFENSIVE_THRESHOLD = 0.15
    STRESS_RECOVERY_THRESHOLD = -0.05
    NOISE_HIGH_THRESHOLD = 0.20

    CITY_CONFIG = {
        "nyc": {"domain": "data.cityofnewyork.us", "endpoint": "erm2-nwe9"},
        "chicago": {"domain": "data.cityofchicago.org", "endpoint": "v6vf-nfjy"},
        "la": {"domain": "data.lacity.org", "endpoint": "aub4-z4ir"},
        "sf": {"domain": "data.sfgov.org", "endpoint": "vw6y-z8j6"},
        "boston": {"domain": "data.boston.gov", "endpoint": "wc8w-nujj"},
    }

    def universe(self):
        return ["XLP", "XLU", "XLV", "XLF", "XLI", "XLY"]

    def _history_path(self):
        return "data/crazy/311_history.json"

    def _fetch_city(self, domain: str, endpoint: str, days_back: int = 7):
        from sodapy import Socrata
        client = Socrata(domain, None, timeout=30)
        cutoff = (datetime.utcnow() - timedelta(days=days_back)).isoformat()
        results = client.get(
            endpoint,
            where=f"created_date > '{cutoff}'",
            select="complaint_type, created_date",
            limit=50000,
        )
        return pd.DataFrame.from_records(results)

    def _fetch_weekly_counts(self):
        rows = []
        for _, cfg in self.CITY_CONFIG.items():
            df = self._fetch_city(cfg["domain"], cfg["endpoint"], days_back=7)
            if df.empty:
                continue
            df["complaint_type"] = df["complaint_type"].astype(str)
            for cat, types in self.COMPLAINT_CATEGORIES.items():
                rows.append({"category": cat, "count": int(df["complaint_type"].isin(types).sum())})
        if not rows:
            return {}
        agg = {}
        for row in rows:
            agg[row["category"]] = agg.get(row["category"], 0) + row["count"]
        return agg

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        history = load_history(self._history_path())
        if not historical:
            try:
                counts = self._fetch_weekly_counts()
                if counts:
                    entry = {"date": as_of.isoformat(), "counts": counts}
                    history = append_history(self._history_path(), entry)
            except Exception:
                pass

        if not history:
            return "HOLD"

        current = history[-1]["counts"]
        baseline = {}
        last4 = history[-4:] if len(history) >= 4 else history
        for cat in self.COMPLAINT_CATEGORIES:
            values = [h["counts"].get(cat, 0) for h in last4]
            baseline[cat] = float(np.mean(values)) if values else 0

        category_scores = {}
        for cat in self.COMPLAINT_CATEGORIES:
            curr = current.get(cat, 0)
            base = baseline.get(cat, curr)
            category_scores[cat] = (curr - base) / base if base else 0

        stress_index = sum(category_scores[cat] * self.WEIGHTS[cat] for cat in self.WEIGHTS)
        noise_signal = -1 * category_scores.get("noise", 0)

        meta = self.meta(state)
        meta["noise_signal"] = round(noise_signal, 4)

        if stress_index > self.STRESS_DEFENSIVE_THRESHOLD:
            return "HIGH_STRESS"
        if stress_index < self.STRESS_RECOVERY_THRESHOLD:
            return "RECOVERY"
        return "NEUTRAL"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        meta = self.meta(state)
        noise_signal = meta.get("noise_signal", 0)

        if signal == "HIGH_STRESS":
            weights = {"XLP": 0.35, "XLU": 0.25, "XLV": 0.25}
            if noise_signal > self.NOISE_HIGH_THRESHOLD:
                weights["XLP"] += 0.05
                weights["XLV"] += 0.05
                weights["XLU"] += 0.05
            return weights

        if signal == "RECOVERY":
            weights = {"XLF": 0.35, "XLI": 0.35, "XLY": 0.30}
            if noise_signal > self.NOISE_HIGH_THRESHOLD:
                reduction = weights["XLI"] * 0.5
                weights["XLI"] -= reduction
                weights["XLP"] = weights.get("XLP", 0) + reduction * 0.75
                weights["XLV"] = weights.get("XLV", 0) + reduction * 0.25
            return weights

        return None
