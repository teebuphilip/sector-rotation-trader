import pandas as pd

from scanner import safe_download


def fetch_prices(tickers: list, period: str = "2y") -> pd.DataFrame:
    """
    Fetch price history via Yahoo Finance (safe_download).
    Returns Close price DataFrame.
    """
    raw = safe_download(tickers, period=period)
    if raw.empty:
        return pd.DataFrame()
    return raw["Close"] if "Close" in raw.columns else raw
