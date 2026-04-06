"""
signals.py — Entry (volatility compression + breakout) and exit (2x below 20MA) signals
"""
import pandas as pd
import numpy as np
from config import (
    BREAKOUT_LOOKBACK, VOLUME_MULT, VOLUME_AVG_DAYS,
    BB_PERIOD, BB_STD, EXIT_MA_PERIOD, EXIT_CONSEC_DAYS
)


def bollinger_bands(series, period=BB_PERIOD, num_std=BB_STD):
    """Return (upper, middle, lower) BB series."""
    mid   = series.rolling(period).mean()
    std   = series.rolling(period).std()
    upper = mid + num_std * std
    lower = mid - num_std * std
    return upper, mid, lower


def bb_bandwidth(series, period=BB_PERIOD, num_std=BB_STD):
    """Bandwidth = (upper - lower) / mid — proxy for volatility compression."""
    upper, mid, lower = bollinger_bands(series, period, num_std)
    return (upper - lower) / mid


def check_entry(prices: pd.Series, volumes: pd.Series) -> bool:
    """
    All 3 entry conditions must be True on the latest bar:
      1. Close > 10-day high (breakout)
      2. Volume > 150% of 20-day avg volume
      3. BB bandwidth expanding (today > yesterday)
    """
    if len(prices) < max(BREAKOUT_LOOKBACK, VOLUME_AVG_DAYS, BB_PERIOD) + 2:
        return False

    close   = prices.iloc[-1]
    high_n  = prices.iloc[-(BREAKOUT_LOOKBACK + 1):-1].max()   # exclude today
    vol     = volumes.iloc[-1]
    vol_avg = volumes.iloc[-VOLUME_AVG_DAYS:].mean()

    bw      = bb_bandwidth(prices)
    bw_now  = bw.iloc[-1]
    bw_prev = bw.iloc[-2]

    cond1 = close > high_n                         # price breakout
    cond2 = vol >= VOLUME_MULT * vol_avg           # volume surge
    cond3 = bw_now > bw_prev and bw_now > 0        # BB expanding upward

    return bool(cond1 and cond2 and cond3)


def check_exit(prices: pd.Series, existing_consec: int = 0) -> tuple[bool, int]:
    """
    Exit when price closes below 20-day MA for EXIT_CONSEC_DAYS consecutive days.
    Returns (should_exit: bool, new_consecutive_count: int).
    """
    if len(prices) < EXIT_MA_PERIOD + 1:
        return False, 0

    ma    = prices.rolling(EXIT_MA_PERIOD).mean()
    close = prices.iloc[-1]
    ma_v  = ma.iloc[-1]

    if close < ma_v:
        new_consec = existing_consec + 1
    else:
        new_consec = 0

    should_exit = new_consec >= EXIT_CONSEC_DAYS
    return should_exit, new_consec


def get_entry_price(prices: pd.Series) -> float:
    """Latest close as entry price."""
    return float(prices.iloc[-1])


def get_current_price(prices: pd.Series) -> float:
    return float(prices.iloc[-1])
