from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Iterable

import pandas as pd

from scanner import safe_download


@dataclass
class PriceData:
    open: pd.DataFrame
    close: pd.DataFrame
    volume: pd.DataFrame

    @property
    def dates(self) -> list[pd.Timestamp]:
        if self.close.empty:
            return []
        return list(self.close.index)


_CACHE: dict[tuple[tuple[str, ...], str, str], PriceData] = {}


def download_price_data(tickers: Iterable[str], start: str | date, end: str | date) -> PriceData:
    symbols = sorted({str(t).upper() for t in tickers if t})
    if not symbols:
        return PriceData(pd.DataFrame(), pd.DataFrame(), pd.DataFrame())

    cache_key = (tuple(symbols), str(start), str(end))
    if cache_key in _CACHE:
        return _CACHE[cache_key]

    raw = safe_download(symbols, period=None, start=str(start), end=str(end), retries=1, delay=0)
    if raw is None or raw.empty:
        return PriceData(pd.DataFrame(), pd.DataFrame(), pd.DataFrame())

    def field(name: str) -> pd.DataFrame:
        if isinstance(raw.columns, pd.MultiIndex):
            if name not in raw.columns.get_level_values(0):
                return pd.DataFrame()
            df = raw[name].copy()
        else:
            if name not in raw.columns:
                return pd.DataFrame()
            col_name = symbols[0] if len(symbols) == 1 else name
            df = raw[[name]].rename(columns={name: col_name})
        df.index = pd.to_datetime(df.index, errors="coerce").tz_localize(None)
        df = df[~df.index.isna()].sort_index()
        df.columns = [str(c).upper() for c in df.columns]
        return df

    open_df = field("Open")
    close_df = field("Close")
    volume_df = field("Volume")
    data = PriceData(open=open_df, close=close_df, volume=volume_df)
    _CACHE[cache_key] = data
    return data


def price_adapter_frame(close: pd.DataFrame, tickers: list[str]) -> pd.DataFrame:
    cols = [t.upper() for t in tickers if t and t.upper() in close.columns]
    if not cols:
        return pd.DataFrame(columns=["date", "value"])
    df = close[cols].copy().reset_index()
    df = df.rename(columns={df.columns[0]: "date"})
    df.columns = [str(c).strip().lower().replace("-", "_").replace(" ", "_") for c in df.columns]
    value_cols = [c for c in df.columns if c != "date"]
    if value_cols:
        df["value"] = pd.to_numeric(df[value_cols[0]], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)
