import os
import time
from datetime import date

import pandas as pd
import requests

from scanner import SECTOR_STOCKS
from .base import CrazyAlgoBase
from crazy.blocked import record_blocked
from crazy.utils import load_json, save_json


class GlassdoorAlgo(CrazyAlgoBase):
    algo_id = "glassdoor"
    name = "Glassdoor Misery Gradient"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    def universe(self):
        return list(SECTOR_STOCKS.keys())

    def _glassdoor_keys(self):
        pid = os.getenv("GLASSDOOR_PARTNER_ID")
        key = os.getenv("GLASSDOOR_KEY")
        return pid, key

    def _company_name(self, ticker: str) -> str | None:
        try:
            import yfinance as yf
            info = yf.Ticker(ticker).info
            return info.get("shortName") or info.get("longName")
        except Exception:
            return None

    def _get_company_rating(self, name: str, pid: str, key: str):
        url = "https://api.glassdoor.com/api/api.htm"
        params = {
            "t.p": pid,
            "t.k": key,
            "format": "json",
            "v": "1",
            "action": "employers",
            "q": name,
            "ps": 1,
        }
        r = requests.get(url, params=params, timeout=30)
        data = r.json()
        if data.get("response", {}).get("employers"):
            emp = data["response"]["employers"][0]
            return emp.get("overallRating")
        return None

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        pid, key = self._glassdoor_keys()
        if not pid or not key:
            record_blocked(self.algo_id, self.name, ["GLASSDOOR_PARTNER_ID", "GLASSDOOR_KEY"], "Missing Glassdoor keys")
            return "HOLD"

        sector_scores = {}
        for etf, tickers in list(SECTOR_STOCKS.items()):
            ratings = []
            for t in tickers[:5]:
                name = self._company_name(t)
                if not name:
                    continue
                rating = self._get_company_rating(name, pid, key)
                if rating:
                    ratings.append(float(rating))
                time.sleep(0.5)
            if ratings:
                sector_scores[etf] = float(sum(ratings) / len(ratings))

        if not sector_scores:
            return "HOLD"

        hist_path = "data/crazy/glassdoor_history.json"
        history = load_json(hist_path, default={})
        history[as_of.isoformat()] = sector_scores
        save_json(hist_path, history)

        dates = sorted(history.keys())
        if len(dates) < 2:
            return "HOLD"

        current = history[dates[-1]]
        prev = history[dates[-2]]
        deltas = {}
        for etf, cur in current.items():
            if etf in prev:
                deltas[etf] = cur - prev[etf]
        if not deltas:
            return "HOLD"

        ranked = sorted(deltas.items(), key=lambda x: x[1], reverse=True)
        top3 = [r[0] for r in ranked[:3]]
        bottom3 = [r[0] for r in ranked[-3:]]
        meta = self.meta(state)
        meta["top3"] = top3
        meta["bottom3"] = bottom3
        meta["signal_label"] = f"TOP:{','.join(top3)} BOT:{','.join(bottom3)}"
        meta["signal_key"] = "|".join(top3 + bottom3)
        return "READY"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        meta = self.meta(state)
        top3 = meta.get("top3", [])
        if not top3:
            return None
        per = 1.0 / len(top3)
        return {t: per for t in top3}
