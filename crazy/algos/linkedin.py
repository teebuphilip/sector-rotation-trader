import os
import re
from datetime import date

import pandas as pd
import requests

from .base import CrazyAlgoBase
from crazy.utils import load_json


class LinkedInAlgo(CrazyAlgoBase):
    algo_id = "linkedin"
    name = "LinkedIn Layoff Propagation"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    LAYOFF_SPIKE_THRESHOLD = 0.25
    HIRING_SURGE_THRESHOLD = 0.30

    SECTOR_KEYWORDS = {
        "XLK": ["technology", "software", "internet"],
        "XLF": ["financial", "banking", "insurance"],
        "XLE": ["energy", "oil", "gas"],
        "XLV": ["healthcare", "pharma", "biotech"],
        "XLI": ["manufacturing", "industrial"],
        "XLC": ["telecom", "media", "communications"],
    }

    def universe(self):
        return ["XLK", "XLF", "XLE", "XLV", "XLI", "XLC", "XLP", "XLU"]

    def _load_workforce_csv(self):
        path = "data/crazy/linkedin_workforce.csv"
        if os.path.exists(path):
            df = pd.read_csv(path)
            df["date"] = pd.to_datetime(df["date"])
            return df
        return pd.DataFrame()

    def _fetch_pdf_workforce(self):
        try:
            page = requests.get("https://economicgraph.linkedin.com/research/linkedin-workforce-report", timeout=30).text
            m = re.search(r'href="([^"]+\.pdf)"', page)
            if not m:
                return pd.DataFrame()
            pdf_url = m.group(1)
            if pdf_url.startswith("/"):
                pdf_url = "https://economicgraph.linkedin.com" + pdf_url
            pdf_bytes = requests.get(pdf_url, timeout=30).content
            cache_path = "cache/crazy/linkedin_workforce.pdf"
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            with open(cache_path, "wb") as f:
                f.write(pdf_bytes)

            import pdfplumber
            rows = []
            with pdfplumber.open(cache_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text() or ""
                    for line in text.splitlines():
                        if "%" not in line:
                            continue
                        rows.append(line)
            return pd.DataFrame()
        except Exception:
            return pd.DataFrame()

    def _map_sector(self, industry: str):
        s = industry.lower()
        for etf, keywords in self.SECTOR_KEYWORDS.items():
            if any(k in s for k in keywords):
                return etf
        return None

    def _get_workforce_df(self):
        df = self._load_workforce_csv()
        if df.empty:
            df = self._fetch_pdf_workforce()
        return df

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        df = self._get_workforce_df()
        if df.empty:
            return "HOLD"

        if "sector" not in df.columns:
            if "industry" in df.columns:
                df["sector"] = df["industry"].apply(self._map_sector)

        df = df.dropna(subset=["sector"]).copy()
        if "hire_rate" in df.columns:
            df["hire_rate"] = pd.to_numeric(df["hire_rate"], errors="coerce")
        if "layoff_rate" in df.columns:
            df["layoff_rate"] = pd.to_numeric(df["layoff_rate"], errors="coerce")
        df = df.dropna(subset=["hire_rate", "layoff_rate"]).copy()
        if df.empty:
            return "HOLD"

        df = df.sort_values("date")
        signals = {}
        for sector in df["sector"].unique():
            sector_df = df[df["sector"] == sector]
            if len(sector_df) < 6:
                continue
            current = sector_df.iloc[-1]
            avg_layoff = sector_df["layoff_rate"].tail(6).mean()
            avg_hire = sector_df["hire_rate"].tail(6).mean()
            layoff_z = (current["layoff_rate"] - avg_layoff) / avg_layoff if avg_layoff else 0
            hire_z = (current["hire_rate"] - avg_hire) / avg_hire if avg_hire else 0
            if layoff_z > self.LAYOFF_SPIKE_THRESHOLD:
                signals[sector] = ("AVOID", hire_z, layoff_z)
            elif hire_z > self.HIRING_SURGE_THRESHOLD:
                signals[sector] = ("BUY", hire_z, layoff_z)
            else:
                signals[sector] = ("NEUTRAL", hire_z, layoff_z)

        meta = self.meta(state)
        meta["signals"] = {k: v[0] for k, v in signals.items()}
        buy = [k for k, v in signals.items() if v[0] == "BUY"]
        avoid = [k for k, v in signals.items() if v[0] == "AVOID"]
        meta["signal_label"] = f"BUY:{','.join(buy) or '-'} AVOID:{','.join(avoid) or '-'}"
        meta["signal_key"] = "|".join(f"{k}:{v[0]}" for k, v in sorted(signals.items()))
        return "READY"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        meta = self.meta(state)
        signals = meta.get("signals", {})
        if not signals:
            return None

        avoid = [s for s, v in signals.items() if v == "AVOID"]
        buy = [s for s, v in signals.items() if v == "BUY"]
        buy = buy[:3]
        weights = {}
        if buy:
            per = 1.0 / len(buy)
            for s in buy:
                weights[s] = per

        if len(avoid) >= 3:
            if buy:
                for s in list(weights.keys()):
                    weights[s] = weights[s] * 0.4
            defensive = {"XLP": 0.25, "XLU": 0.20, "XLV": 0.15}
            for k, v in defensive.items():
                weights[k] = weights.get(k, 0) + v
        return weights
