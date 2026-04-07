"""
scanner.py — Sector rotation detection + stock leadership filter
"""
import time
import yfinance as yf
import pandas as pd
import numpy as np
from config import (SECTOR_ETFS, PERF_SHORT_DAYS, PERF_LONG_DAYS, DATA_PERIOD)


def safe_download(tickers, period="1y", retries=2, delay=30, **kwargs):
    """Download with retry. Returns empty DataFrame on total failure."""
    kwargs.setdefault("auto_adjust", True)
    kwargs.setdefault("progress", False)
    for attempt in range(retries):
        try:
            data = yf.download(tickers, period=period, **kwargs)
            if data is not None and not data.empty:
                return data
        except Exception as e:
            print(f"  ⚠ yfinance download failed (attempt {attempt+1}/{retries}): {e}")
        if attempt < retries - 1:
            print(f"  Retrying in {delay}s...")
            time.sleep(delay)
    print("  ✖ Download failed after all retries")
    return pd.DataFrame()

# Map each sector ETF to its component tickers (top holdings subset for speed)
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

    # Only sectors where 3M > 6M (accelerating)
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

    etf_ret = float(price_data_etf.pct_change(PERF_SHORT_DAYS).iloc[-1])
    stock_ret = price_data_stocks.pct_change(PERF_SHORT_DAYS).iloc[-1]

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

    # ETF series for comparison
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
