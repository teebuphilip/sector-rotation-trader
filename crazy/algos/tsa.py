import os
from datetime import date

import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

from scanner import safe_download
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from .base import CrazyAlgoBase


class TSAAlgo(CrazyAlgoBase):
    algo_id = "tsa"
    name = "TSA Body Count"
    rebalance_frequency = "daily"
    supports_historical_seed = True

    LOOKBACK_DAYS = 14
    ACCEL_ENTRY_THRESHOLD = 0.05
    ACCEL_EXIT_THRESHOLD = -0.03
    CONSECUTIVE_DAYS_CONFIRM = 3
    HARD_EXIT_YOY = -0.20

    def universe(self):
        return ["XLY", "XLK", "XLI", "XLP", "XLU", "XLV"]

    def _fetch_tsa_df(self):
        cache_path = os.path.join(CRAZY_CACHE_DIR, "tsa.json")

        def _fetch():
            url = "https://www.tsa.gov/travel/passenger-volumes"
            r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            table = soup.find("table")
            if table is None:
                return []
            df = pd.read_html(StringIO(str(table)))[0]
            # Normalize columns (TSA table uses Date + year columns)
            df.columns = [str(c).strip() for c in df.columns]
            date_col = next((c for c in df.columns if c.lower() == "date"), df.columns[0])

            year_cols = [c for c in df.columns if c != date_col]
            year_nums = []
            for c in year_cols:
                try:
                    year_nums.append((int(c), c))
                except ValueError:
                    continue

            if len(year_nums) >= 2:
                year_nums.sort()
                cur_col = year_nums[-1][1]
                prev_col = year_nums[-2][1]
            else:
                # Fallback to last two non-date columns
                cur_col = year_cols[-1] if year_cols else None
                prev_col = year_cols[-2] if len(year_cols) > 1 else None

            if not cur_col or not prev_col:
                return []

            df["date"] = pd.to_datetime(df[date_col], errors="coerce")
            df["throughput"] = pd.to_numeric(df[cur_col].astype(str).str.replace(",", ""), errors="coerce")
            df["throughput_yoy"] = pd.to_numeric(df[prev_col].astype(str).str.replace(",", ""), errors="coerce")
            df = df.dropna(subset=["date", "throughput", "throughput_yoy"])
            df["yoy_pct"] = (df["throughput"] - df["throughput_yoy"]) / df["throughput_yoy"]
            df = df.sort_values("date")
            return df.to_dict(orient="records")

        data = cached_fetch(cache_path, ttl_hours=25, fetch_fn=_fetch)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        try:
            df = self._fetch_tsa_df()
        except Exception:
            return "HOLD"
        if df.empty:
            return "HOLD"

        df = df[df["date"] <= pd.Timestamp(as_of)]
        if len(df) < (self.LOOKBACK_DAYS + 14):
            return "HOLD"

        df = df.copy()
        df["rolling_yoy"] = df["yoy_pct"].rolling(self.LOOKBACK_DAYS).mean()
        df["acceleration"] = df["rolling_yoy"].diff(7)

        latest = df.iloc[-1]
        prev_n = df.tail(self.CONSECUTIVE_DAYS_CONFIRM)

        meta = self.meta(state)
        if latest["yoy_pct"] <= self.HARD_EXIT_YOY:
            meta["hard_exit"] = True
            meta["risk_on_streak"] = 0
            return "HARD_EXIT"

        if meta.get("hard_exit"):
            if (prev_n["acceleration"] > self.ACCEL_ENTRY_THRESHOLD).all():
                meta["risk_on_streak"] = meta.get("risk_on_streak", 0) + 1
            else:
                meta["risk_on_streak"] = 0
            if meta.get("risk_on_streak", 0) < 5:
                return "HOLD"
            meta["hard_exit"] = False

        if (prev_n["acceleration"] > self.ACCEL_ENTRY_THRESHOLD).all():
            return "RISK_ON"
        if (prev_n["acceleration"] < self.ACCEL_EXIT_THRESHOLD).all():
            return "RISK_OFF"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {"XLY": 0.40, "XLK": 0.30, "XLI": 0.30}
        if signal == "RISK_OFF":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        if signal == "HARD_EXIT":
            return {}
        return None
