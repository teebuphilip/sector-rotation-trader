"""
scanner_polygon.py — Drop-in replacement for scanner.py using Polygon.io free tier.

Swap instructions (Week 3):
  1. pip install requests  (already present in most envs)
  2. Set POLYGON_API_KEY in GitHub Actions secrets
  3. Replace `import scanner` with `import scanner_polygon as scanner` in daily_run.py + seed.py
  4. Delete scanner.py (or keep as fallback)

Polygon free tier: 15-min delayed data, unlimited calls, no credit card required.
Endpoint: GET /v2/aggs/ticker/{ticker}/range/1/day/{from}/{to}
"""
import os
import time
from datetime import date, timedelta

import pandas as pd
import numpy as np
from config import (SECTOR_ETFS, PERF_SHORT_DAYS, PERF_LONG_DAYS, DATA_PERIOD)

_POLYGON_BASE = "https://api.polygon.io"

# Map each sector ETF to its component tickers (identical to scanner.py)
SECTOR_STOCKS = {
    'XLK':  ['AAPL','MSFT','NVDA','AVGO','ORCL','CRM','AMD','INTC','QCOM','TXN'],
    'XLV':  ['UNH','JNJ','LLY','ABBV','MRK','TMO','ABT','DHR','BMY','AMGN'],
    'XLF':  ['BRK-B','JPM','V','MA','BAC','WFC','GS','MS','BLK','SPGI'],
    'XLY':  ['AMZN','TSLA','HD','MCD','NKE','LOW','SBUX','TGT','BKNG','CMG'],
    'XLI':  ['GE','RTX','CAT','HON','UNP','DE','LMT','UPS','BA','MMM'],
    'XLC':  ['META','GOOGL','GOOG','NFLX','DIS','CMCSA','T','VZ','CHTR','TMUS'],
    'XLP':  ['PG','KO','PEP','COST','WMT','PM','MO','MDLZ','CL','GIS'],
    'XLE':  ['XOM','CVX','COP','EOG','SLB','MPC','PSX','VLO','OXY','FANG'],
    'XLB':  ['LIN','APD','SHW','FCX','NEM','NUE','VMC','MLM','CF','MOS'],
    'XLRE': ['PLD','AMT','EQIX','CCI','PSA','O','WELL','AVB','EQR','DLR'],
    'XLU':  ['NEE','DUK','SO','D','AEP','EXC','SRE','XEL','ED','ETR'],
}

# DATA_PERIOD → calendar days (Polygon uses date strings, not yfinance period strings)
_PERIOD_TO_DAYS = {
    "1y": 365, "2y": 730, "6mo": 183, "3mo": 91, "1mo": 30, "5d": 5,
}


def _period_to_date_range(period):
    days = _PERIOD_TO_DAYS.get(period, 365)
    end = date.today()
    start = end - timedelta(days=days)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")


def _get_api_key():
    key = os.getenv("POLYGON_API_KEY", "")
    if not key:
        raise EnvironmentError("POLYGON_API_KEY not set")
    return key


def _fetch_ticker_aggs(ticker, from_date, to_date, api_key, retries=2):
    """
    Fetch daily OHLCV bars for one ticker from Polygon.
    Returns list of result dicts or [] on failure.
    """
    import requests
    # Polygon uses dots for class B shares: BRK-B → BRK.B
    poly_ticker = ticker.replace("-", ".")
    url = (
        f"{_POLYGON_BASE}/v2/aggs/ticker/{poly_ticker}/range/1/day"
        f"/{from_date}/{to_date}"
        f"?adjusted=true&sort=asc&limit=5000&apiKey={api_key}"
    )
    for attempt in range(retries):
        try:
            import requests as req
            resp = req.get(url, timeout=20)
            if resp.status_code == 200:
                data = resp.json()
                return data.get("results") or []
            if resp.status_code == 429:
                time.sleep(12)  # free tier rate limit: 5 req/min
        except Exception as e:
            print(f"  Polygon fetch error {ticker} attempt {attempt+1}: {e}")
        if attempt < retries - 1:
            time.sleep(12)
    return []


def _aggs_to_series(results, ticker):
    """Convert Polygon aggs results to (close_series, volume_series)."""
    if not results:
        return pd.Series(dtype=float, name=ticker), pd.Series(dtype=float, name=ticker)
    rows = [{"date": pd.Timestamp(r["t"], unit="ms"), "c": r["c"], "v": r["v"]}
            for r in results]
    df = pd.DataFrame(rows).set_index("date")
    return df["c"].rename(ticker), df["v"].rename(ticker)


def safe_download(tickers, period="1y", retries=2, delay=12, **kwargs):
    """
    Polygon replacement for yf.download().
    Returns DataFrame with MultiIndex columns (field, ticker) matching yfinance output.
    Free tier: 5 requests/minute — sleeps 12s between ticker fetches.
    """
    if isinstance(tickers, str):
        tickers = [tickers]

    try:
        api_key = _get_api_key()
    except EnvironmentError as e:
        print(f"  ✖ {e}")
        return pd.DataFrame()

    from_date, to_date = _period_to_date_range(period)
    closes = {}
    volumes = {}

    for i, ticker in enumerate(tickers):
        if i > 0:
            time.sleep(12)  # respect 5 req/min free tier limit
        results = _fetch_ticker_aggs(ticker, from_date, to_date, api_key, retries=retries)
        c, v = _aggs_to_series(results, ticker)
        if not c.empty:
            closes[ticker] = c
            volumes[ticker] = v
        else:
            print(f"  ⚠ No data returned for {ticker}")

    if not closes:
        print("  ✖ No data fetched from Polygon")
        return pd.DataFrame()

    close_df  = pd.DataFrame(closes)
    volume_df = pd.DataFrame(volumes)

    # Build MultiIndex columns identical to yfinance multi-ticker output
    close_df.columns  = pd.MultiIndex.from_tuples([("Close",  t) for t in close_df.columns])
    volume_df.columns = pd.MultiIndex.from_tuples([("Volume", t) for t in volume_df.columns])

    return pd.concat([close_df, volume_df], axis=1)


# ── Everything below is identical to scanner.py ───────────────────────────────

def get_sector_data(period=DATA_PERIOD):
    """Download sector ETF price data."""
    data = safe_download(SECTOR_ETFS, period=period)
    if data.empty:
        return pd.DataFrame()
    return data['Close']


def find_leading_sector(sector_data):
    """
    Find sector with highest 3M-6M performance spread (acceleration).
    Returns (etf_ticker, spread, all_sectors_df).
    """
    perf_3m = sector_data.pct_change(PERF_SHORT_DAYS).iloc[-1]
    perf_6m = sector_data.pct_change(PERF_LONG_DAYS).iloc[-1]

    df = pd.DataFrame({"3M": perf_3m, "6M": perf_6m})
    df.dropna(inplace=True)

    leaders = df[df["3M"] > df["6M"]].copy()
    if leaders.empty:
        return None, None, df

    leaders["Spread"] = leaders["3M"] - leaders["6M"]
    leaders.sort_values("Spread", ascending=False, inplace=True)

    top_etf    = leaders.index[0]
    top_spread = float(leaders["Spread"].iloc[0])
    return top_etf, top_spread, leaders


def get_stock_data(tickers, period=DATA_PERIOD):
    """Download individual stock price + volume data."""
    if not tickers:
        return pd.DataFrame(), pd.DataFrame()
    raw = safe_download(tickers, period=period)
    if raw.empty:
        return pd.DataFrame(), pd.DataFrame()
    if isinstance(raw.columns, pd.MultiIndex):
        prices  = raw['Close']
        volumes = raw['Volume']
    else:
        prices  = raw[['Close']]
        volumes = raw[['Volume']]
    return prices, volumes


def filter_sector_leaders(etf_ticker, price_data_etf, price_data_stocks):
    """
    Keep only stocks outperforming their sector ETF over PERF_SHORT_DAYS.
    Returns list of qualifying tickers.
    """
    if price_data_etf is None or price_data_stocks.empty:
        return []

    etf_ret    = float(price_data_etf.pct_change(PERF_SHORT_DAYS).iloc[-1])
    stock_ret  = price_data_stocks.pct_change(PERF_SHORT_DAYS).iloc[-1]

    leaders = stock_ret[stock_ret > etf_ret].dropna()
    return list(leaders.index)


def scan(as_of_date=None):
    """
    Full scan pipeline.
    Returns dict with keys: sector, spread, candidates, sector_df, prices, volumes
    """
    sector_data = get_sector_data()

    if as_of_date:
        sector_data = sector_data[sector_data.index <= as_of_date]

    top_etf, spread, sector_df = find_leading_sector(sector_data)

    if top_etf is None:
        return {"sector": None, "spread": None, "candidates": [],
                "sector_df": sector_df, "prices": pd.DataFrame(), "volumes": pd.DataFrame()}

    tickers = SECTOR_STOCKS.get(top_etf, [])
    prices, volumes = get_stock_data(tickers)

    if as_of_date:
        prices  = prices[prices.index <= as_of_date]
        volumes = volumes[volumes.index <= as_of_date]

    etf_series = sector_data[top_etf]
    qualifying = filter_sector_leaders(top_etf, etf_series, prices)

    return {
        "sector":     top_etf,
        "spread":     spread,
        "candidates": qualifying,
        "sector_df":  sector_df,
        "prices":     prices,
        "volumes":    volumes,
    }
