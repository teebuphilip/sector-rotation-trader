import os
from datetime import timedelta, date

import pandas as pd
import requests

from config import SECTOR_ETFS
from .base import CrazyAlgoBase
from crazy.utils import cached_fetch, load_json, save_json
from crazy.config import CRAZY_CACHE_DIR


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
        meta["signal_label"] = f"SELL:{','.join(sells) or '-'} FADE:{','.join(fades) or '-'}"
        meta["signal_key"] = "|".join(f"{k}:{v}" for k, v in sorted(signals.items()))
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

        return weights
