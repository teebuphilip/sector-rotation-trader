import os
import re
import time
from datetime import datetime, timedelta, date

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import feedparser

from scanner import safe_download
from config import SECTOR_ETFS
from crazy.utils import cached_fetch, load_history, append_history, load_json, save_json
from crazy.config import CRAZY_CACHE_DIR
from crazy.blocked import record_blocked


class CrazyAlgoBase:
    algo_id = "base"
    name = "Base"
    rebalance_frequency = "daily"  # daily | weekly | monthly
    supports_historical_seed = False

    def universe(self):
        return []

    def meta(self, state: dict) -> dict:
        state.setdefault("meta", {})
        state["meta"].setdefault(self.algo_id, {})
        return state["meta"][self.algo_id]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        return None

    def should_rebalance(self, as_of: date, state: dict, signal: str) -> bool:
        meta = self.meta(state)
        last_signal = meta.get("last_signal")
        if last_signal != signal:
            return True

        # honor frequency even if signal unchanged
        if self.rebalance_frequency == "weekly":
            return as_of.weekday() == 0  # Monday
        if self.rebalance_frequency == "monthly":
            return as_of.day == 1
        return False


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
            df = pd.read_html(str(table))[0]
            df["date"] = pd.to_datetime(df["Date"])
            df["throughput"] = df.iloc[:, 1].astype(str).str.replace(",", "").astype(int)
            df["throughput_yoy"] = df.iloc[:, 2].astype(str).str.replace(",", "").astype(int)
            df["yoy_pct"] = (df["throughput"] - df["throughput_yoy"]) / df["throughput_yoy"]
            df = df.sort_values("date")
            return df.to_dict(orient="records")

        data = cached_fetch(cache_path, ttl_hours=25, fetch_fn=_fetch)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        df = self._fetch_tsa_df()
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


class CardboardAlgo(CrazyAlgoBase):
    algo_id = "cardboard"
    name = "Cardboard Box Index"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    BOX_ACCEL_BULL = 0.02
    BOX_ACCEL_BEAR = -0.015
    IP_CONFIRM = 0.0

    def universe(self):
        return ["XLB", "XLI", "XLE", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        from fredapi import Fred
        fred = Fred(api_key=api_key)
        box_ppi = fred.get_series("PCU3221213221213")
        mfg_ip = fred.get_series("IPMAN")
        df = pd.DataFrame({"box_ppi": box_ppi, "mfg_ip": mfg_ip}).dropna()
        df["box_ppi_3m_chg"] = df["box_ppi"].pct_change(3)
        df["box_ppi_accel"] = df["box_ppi_3m_chg"].diff()
        df["ip_3m_chg"] = df["mfg_ip"].pct_change(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        box_accel = latest["box_ppi_accel"]
        ip_chg = latest["ip_3m_chg"]

        if box_accel > self.BOX_ACCEL_BULL and ip_chg > self.IP_CONFIRM:
            return "EXPANSION"
        if box_accel < self.BOX_ACCEL_BEAR and ip_chg < self.IP_CONFIRM:
            return "CONTRACTION"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "EXPANSION":
            return {"XLB": 0.35, "XLI": 0.35, "XLE": 0.30}
        if signal == "CONTRACTION":
            return {"XLP": 0.50, "XLU": 0.25, "XLV": 0.25}
        return None


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
                # If fetch fails, fall back to history
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
            baseline = np.mean([v for v in baseline_weeks if v > 0]) if baseline_weeks else 0
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


class GlassdoorAlgo(CrazyAlgoBase):
    algo_id = "glassdoor"
    name = "Glassdoor Misery Gradient"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    SENTIMENT_BULL_THRESHOLD = 0.15
    SENTIMENT_BEAR_THRESHOLD = -0.15

    def universe(self):
        return list(SECTOR_ETFS)

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

        # Minimal monthly snapshot across top holdings per sector
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

        # Persist history
        hist_path = "data/crazy/glassdoor_history.json"
        history = load_json(hist_path, default={})
        history[as_of.isoformat()] = sector_scores
        save_json(hist_path, history)

        # Need at least 2 months
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
            # 15% cash to represent XLRE underweight
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
        # Best-effort PDF parsing; if it fails, return empty
        try:
            page = requests.get("https://economicgraph.linkedin.com/research/linkedin-workforce-report", timeout=30).text
            m = re.search(r'href="([^"]+\.pdf)"', page)
            if not m:
                return pd.DataFrame()
            pdf_url = m.group(1)
            if pdf_url.startswith("/"):
                pdf_url = "https://economicgraph.linkedin.com" + pdf_url
            pdf_bytes = requests.get(pdf_url, timeout=30).content
            cache_path = os.path.join(CRAZY_CACHE_DIR, "linkedin_workforce.pdf")
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
            # Parsing is highly format-dependent; leave empty on failure
            return pd.DataFrame()
        except Exception:
            return pd.DataFrame()

    def _map_sector(self, industry: str):
        s = industry.lower()
        for etf, keywords in self.SECTOR_KEYWORDS.items():
            if any(k in s for k in keywords):
                return etf
        return None


class LiquorAlgo(CrazyAlgoBase):
    algo_id = "liquor"
    name = "Liquor Store Leading Indicator"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    def universe(self):
        return ["XLY", "XLK", "XLF", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        from fredapi import Fred
        fred = Fred(api_key=api_key)
        total_sales = fred.get_series("MRTSSM4453USN")
        df = pd.DataFrame({"sales": total_sales}).dropna()
        if len(df) < 4:
            return "HOLD"
        sales_chg = df["sales"].pct_change(3).iloc[-1]

        # Basic proxy: sales up = risk-on, sales down = risk-off
        if sales_chg > 0.02:
            return "RISK_ON"
        if sales_chg < -0.02:
            return "RISK_OFF"
        return "NEUTRAL"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {"XLY": 0.50, "XLK": 0.30, "XLF": 0.20}
        if signal == "RISK_OFF":
            return {"XLP": 0.50, "XLU": 0.30, "XLV": 0.20}
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
        meta["signal_key"] = "|".join(f\"{k}:{v[0]}\" for k, v in sorted(signals.items()))
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
            # 60% defensive overlay, 40% to top buys
            if buy:
                scale = 0.4
                for s in list(weights.keys()):
                    weights[s] = weights[s] * scale
            defensive = {"XLP": 0.25, "XLU": 0.20, "XLV": 0.15}
            for k, v in defensive.items():
                weights[k] = weights.get(k, 0) + v
        return weights


class CongressAlgo(CrazyAlgoBase):
    algo_id = "congress"
    name = "Congress Trading Fade"
    rebalance_frequency = "daily"
    supports_historical_seed = True

    CLUSTER_BUY_THRESHOLD = 500000
    CLUSTER_SELL_THRESHOLD = -300000

    def universe(self):
        return list(SECTOR_ETFS)

    def _cache_path(self):
        return os.path.join(CRAZY_CACHE_DIR, "congress.json")

    def _fetch_trades(self):
        def _fetch():
            house_url = "https://house-stock-watcher-data.s3-us-east-2.amazonaws.com/data/all_transactions.json"
            senate_url = "https://senatestockwatcher.com/api/transactions"
            house_df = pd.DataFrame(requests.get(house_url, timeout=30).json())
            senate_df = pd.DataFrame(requests.get(senate_url, timeout=30).json())
            df = pd.concat([house_df, senate_df], ignore_index=True)
            return df.to_dict(orient="records")

        data = cached_fetch(self._cache_path(), ttl_hours=24, fetch_fn=_fetch)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def _sector_map(self):
        return {
            "Technology": "XLK",
            "Financial Services": "XLF",
            "Financial": "XLF",
            "Energy": "XLE",
            "Healthcare": "XLV",
            "Health Care": "XLV",
            "Industrials": "XLI",
            "Industrial": "XLI",
            "Consumer Defensive": "XLP",
            "Consumer Staples": "XLP",
            "Consumer Cyclical": "XLY",
            "Consumer Discretionary": "XLY",
            "Communication Services": "XLC",
            "Materials": "XLB",
            "Real Estate": "XLRE",
            "Utilities": "XLU",
        }

    def _ticker_sector_cache(self):
        path = os.path.join(CRAZY_CACHE_DIR, "ticker_sector.json")
        return load_json(path, default={}), path

    def _map_ticker_to_sector(self, ticker: str):
        cache, path = self._ticker_sector_cache()
        if ticker in cache:
            return cache[ticker]

        sector_etf = None
        try:
            import yfinance as yf
            info = yf.Ticker(ticker).info
            sector = info.get("sector")
            if sector:
                sector_etf = self._sector_map().get(sector)
        except Exception:
            sector_etf = None

        cache[ticker] = sector_etf
        save_json(path, cache)
        return sector_etf

    def _aggregate_flow(self, df: pd.DataFrame, start: date, end: date):
        if df.empty:
            return {}

        df = df.copy()
        df["disclosure_date"] = pd.to_datetime(df["disclosure_date"], errors="coerce")
        df = df.dropna(subset=["disclosure_date"]).copy()
        df = df[(df["disclosure_date"] >= pd.Timestamp(start)) & (df["disclosure_date"] <= pd.Timestamp(end))]

        amount_map = {
            "$1,001 - $15,000": 8000,
            "$15,001 - $50,000": 32500,
            "$50,001 - $100,000": 75000,
            "$100,001 - $250,000": 175000,
            "$250,001 - $500,000": 375000,
            "$500,001 - $1,000,000": 750000,
            "Over $1,000,000": 1500000,
        }

        if "amount" in df.columns:
            df["amount_est"] = df["amount"].map(amount_map).fillna(32500)
        else:
            df["amount_est"] = 32500
        if "ticker" in df.columns:
            df["ticker"] = df["ticker"].astype(str)
        else:
            df["ticker"] = ""
        df["sector_etf"] = df["ticker"].apply(self._map_ticker_to_sector)
        df = df.dropna(subset=["sector_etf"]).copy()

        def _signed(row):
            t = str(row.get("type", ""))
            return row["amount_est"] if "purchase" in t.lower() else -row["amount_est"]

        df["signed_amount"] = df.apply(_signed, axis=1)
        flow = df.groupby("sector_etf")["signed_amount"].sum().to_dict()
        return flow

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        df = self._fetch_trades()
        if df.empty:
            return "HOLD"

        current_flow = self._aggregate_flow(df, as_of - timedelta(days=30), as_of)
        past_flow = self._aggregate_flow(df, as_of - timedelta(days=60), as_of - timedelta(days=30))

        signals = {}
        for sector in SECTOR_ETFS:
            current_net = current_flow.get(sector, 0)
            past_net = past_flow.get(sector, 0)
            if current_net < self.CLUSTER_SELL_THRESHOLD:
                signals[sector] = "SELL_FOLLOW"
            elif past_net > self.CLUSTER_BUY_THRESHOLD:
                signals[sector] = "BUY_FADE"
            else:
                signals[sector] = "NEUTRAL"

        meta = self.meta(state)
        meta["signals"] = signals
        sells = [k for k, v in signals.items() if v == "SELL_FOLLOW"]
        fades = [k for k, v in signals.items() if v == "BUY_FADE"]
        meta["signal_label"] = f\"SELL:{','.join(sells) or '-'} FADE:{','.join(fades) or '-'}\"
        meta["signal_key"] = \"|\".join(f\"{k}:{v}\" for k, v in sorted(signals.items()))
        return "READY"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        meta = self.meta(state)
        signals = meta.get("signals", {})
        if not signals:
            return None

        base_weight = 1.0 / len(SECTOR_ETFS)
        weights = {etf: base_weight for etf in SECTOR_ETFS}

        defensive_pool = 0.0
        cash_pool = 0.0
        for etf, sig in signals.items():
            if sig == "SELL_FOLLOW":
                defensive_pool += weights.get(etf, 0)
                weights[etf] = 0
            elif sig == "BUY_FADE":
                cash_pool += weights.get(etf, 0)
                weights[etf] = 0

        if defensive_pool > 0:
            weights["XLP"] = weights.get("XLP", 0) + defensive_pool * 0.6
            weights["XLU"] = weights.get("XLU", 0) + defensive_pool * 0.4

        if cash_pool > 0:
            # leave in cash by not reallocating
            pass

        return weights


class BiscottiAlgo(CrazyAlgoBase):
    algo_id = "biscotti"
    name = "Algo Biscotti (Unconditional Loyalty)"
    rebalance_frequency = "monthly_eom"
    supports_historical_seed = True

    def universe(self):
        return list(SECTOR_ETFS)

    def _is_month_end(self, as_of: date) -> bool:
        import pandas as pd
        return (pd.Timestamp(as_of) + pd.tseries.offsets.BMonthEnd(0)).date() == as_of

    def should_rebalance(self, as_of: date, state: dict, signal: str) -> bool:
        return self._is_month_end(as_of)

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        raw = safe_download(SECTOR_ETFS, period="3mo")
        if raw.empty:
            return "HOLD"
        prices = raw["Close"] if "Close" in raw.columns else raw
        prices = prices.dropna(how="all")
        if len(prices) < 31:
            return "HOLD"

        returns = prices.pct_change(30).iloc[-1].dropna()
        if returns.empty:
            return "HOLD"

        worst = returns.sort_values().index[0]
        meta = self.meta(state)
        meta["target_sector"] = worst
        meta["signal_label"] = f"BUY:{worst}"
        meta["signal_key"] = worst
        return "BISCOTTI"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal != "BISCOTTI":
            return None
        meta = self.meta(state)
        sector = meta.get("target_sector")
        if not sector:
            return None
        return {sector: 1.0}


class BaileyAlgo(CrazyAlgoBase):
    algo_id = "baileymol"
    name = "Algo Baileymol (Chaos Monger)"
    rebalance_frequency = "weekly"
    supports_historical_seed = True

    STOP_LOSS_PCT = 0.08

    def universe(self):
        return list(SECTOR_ETFS)

    def _is_monday(self, as_of: date) -> bool:
        return as_of.weekday() == 0

    def _is_friday(self, as_of: date) -> bool:
        return as_of.weekday() == 4

    def should_rebalance(self, as_of: date, state: dict, signal: str) -> bool:
        # Enter on Monday, exit on Friday, or if stop-loss triggers
        return self._is_monday(as_of) or self._is_friday(as_of) or signal == "STOP_LOSS"

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

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        if self._stop_loss_triggered(state):
            meta = self.meta(state)
            meta["signal_label"] = "STOP_LOSS"
            meta["signal_key"] = "STOP_LOSS"
            return "STOP_LOSS"

        # Friday = exit to cash
        if self._is_friday(as_of):
            meta = self.meta(state)
            meta["signal_label"] = "FRIDAY_EXIT"
            meta["signal_key"] = "FRIDAY_EXIT"
            return "FRIDAY_EXIT"

        # Monday = pick top 3 by 30D volatility
        if not self._is_monday(as_of):
            return "HOLD"

        raw = safe_download(SECTOR_ETFS, period="1y")
        if raw.empty:
            return "HOLD"
        prices = raw["Close"] if "Close" in raw.columns else raw
        returns = prices.pct_change().dropna()
        rolling = returns.rolling(30).std()
        current_vol = rolling.iloc[-1].dropna()
        if current_vol.empty:
            return "HOLD"

        hist_avg = float(rolling.stack().mean())
        current_avg = float(current_vol.mean())
        meta = self.meta(state)
        if current_avg < hist_avg:
            meta["signal_label"] = "CHAOS_SLEEPING"
            meta["signal_key"] = "CHAOS_SLEEPING"
            return "CHAOS_SLEEPING"

        top3 = current_vol.sort_values(ascending=False).head(3).index.tolist()
        meta["target_sectors"] = top3
        meta["signal_label"] = f"TOP:{','.join(top3)}"
        meta["signal_key"] = "|".join(top3)
        return "CHAOS_ON"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal in ("STOP_LOSS", "FRIDAY_EXIT", "CHAOS_SLEEPING"):
            return {}
        if signal != "CHAOS_ON":
            return None
        meta = self.meta(state)
        top3 = meta.get("target_sectors", [])
        if not top3:
            return None
        per = 1.0 / len(top3)
        return {t: per for t in top3}


def get_crazy_algos():
    return [
        TSAAlgo(),
        CardboardAlgo(),
        CraigslistAlgo(),
        GlassdoorAlgo(),
        Calls311Algo(),
        LiquorAlgo(),
        LinkedInAlgo(),
        CongressAlgo(),
        BiscottiAlgo(),
        BaileyAlgo(),
    ]
