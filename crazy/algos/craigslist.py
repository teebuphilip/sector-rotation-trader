import time
from datetime import date, timedelta

import feedparser
import numpy as np

from .base import CrazyAlgoBase
from crazy.utils import load_history, append_history


class CraigslistAlgo(CrazyAlgoBase):
    algo_id = "craigslist"
    name = "Craigslist Desperation Index"
    rebalance_frequency = "weekly"
    supports_historical_seed = False

    CITIES = [
        "newyork", "losangeles", "chicago", "houston", "phoenix",
        "sfbay", "seattle", "boston", "denver", "atlanta",
        "miami", "detroit", "portland", "sandiego", "lasvegas",
        "austin", "dallas", "nashville", "philadelphia", "minneapolis",
    ]
    CATEGORIES = {
        "electronics": "ela",
        "furniture": "fua",
        "cars": "cto",
        "baby_stuff": "baa",
    }

    DISTRESS_THRESHOLD = 0.20
    RECOVERY_THRESHOLD = -0.10
    CITIES_THRESHOLD = 3

    def universe(self):
        return ["XLP", "XLU", "XLV", "GLD", "XLY", "XLK", "XLF"]

    def _history_path(self):
        return "data/crazy/craigslist_history.json"

    def _fetch_counts(self, as_of: date):
        rows = []
        for city in self.CITIES:
            for _, code in self.CATEGORIES.items():
                url = f"https://{city}.craigslist.org/search/{code}?format=rss&postedToday=1"
                feed = feedparser.parse(url)
                rows.append({
                    "date": as_of.isoformat(),
                    "city": city,
                    "category": code,
                    "count": len(feed.entries),
                })
                time.sleep(0.5)
        return rows

    def _weighted_count(self, category: str, count: int) -> int:
        return count * 2 if category == "cto" else count

    def _compute_city_week_total(self, history: list, as_of: date, city: str, days: int = 7):
        start = as_of - timedelta(days=days - 1)
        total = 0
        for row in history:
            if row.get("city") != city:
                continue
            row_date = date.fromisoformat(row["date"])
            if start <= row_date <= as_of:
                total += self._weighted_count(row["category"], row.get("count", 0))
        return total

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        history = load_history(self._history_path())
        if not historical:
            try:
                rows = self._fetch_counts(as_of)
                for row in rows:
                    history = append_history(self._history_path(), row)
            except Exception:
                pass

        if not history:
            return "HOLD"

        city_scores = {}
        for city in self.CITIES:
            current_week = self._compute_city_week_total(history, as_of, city, days=7)
            baseline_weeks = []
            for i in range(1, 5):
                week_end = as_of - timedelta(days=7 * i)
                baseline_weeks.append(self._compute_city_week_total(history, week_end, city, days=7))
            positive_baseline = [v for v in baseline_weeks if v > 0]
            baseline = np.mean(positive_baseline) if positive_baseline else 0
            city_scores[city] = (current_week - baseline) / baseline if baseline else 0

        distressed = sum(1 for v in city_scores.values() if v > self.DISTRESS_THRESHOLD)
        recovering = sum(1 for v in city_scores.values() if v < self.RECOVERY_THRESHOLD)
        velocity_spike = any(v > 0.50 for v in city_scores.values())

        if velocity_spike:
            return "OVERRIDE_DEFENSIVE"
        if distressed >= self.CITIES_THRESHOLD:
            return "DISTRESS"
        if recovering >= self.CITIES_THRESHOLD:
            return "RECOVERY"
        return "NEUTRAL"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        meta = self.meta(state)
        if signal == "DISTRESS":
            meta["recovery_weeks"] = 0
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.20, "GLD": 0.10}
        if signal == "OVERRIDE_DEFENSIVE":
            meta["recovery_weeks"] = 0
            return {"XLP": 0.20, "XLU": 0.15, "XLV": 0.10, "GLD": 0.05}
        if signal == "RECOVERY":
            meta["recovery_weeks"] = meta.get("recovery_weeks", 0) + 1
            scale = 0.5 if meta["recovery_weeks"] == 1 else 1.0
            return {
                "XLY": 0.35 * scale,
                "XLK": 0.35 * scale,
                "XLF": 0.30 * scale,
            }
        if signal == "NEUTRAL":
            meta["recovery_weeks"] = 0
        return None
