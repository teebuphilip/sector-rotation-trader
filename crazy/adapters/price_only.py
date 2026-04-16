from __future__ import annotations

import pandas as pd


def fetch_prices(tickers: list, period: str = "2y") -> pd.DataFrame:
    """
    Fetch close prices via Yahoo Finance and return the adapter envelope.

    Standard output:
      - date: pd.Timestamp
      - value: first ticker close, for generic single-series signal logic
      - one lowercase snake_case column per ticker when available

    The legacy wide ticker columns are preserved in lowercase form so existing
    generated algos can still reference individual series if needed.
    """
    try:
        if not tickers:
            return pd.DataFrame(columns=["date", "value"])

        from scanner import safe_download

        raw = safe_download(tickers, period=period)
        if raw.empty:
            return pd.DataFrame(columns=["date", "value"])

        close = raw["Close"] if "Close" in raw.columns else raw
        if isinstance(close, pd.Series):
            close = close.to_frame(name=tickers[0] if tickers else "value")
        if close.empty:
            return pd.DataFrame(columns=["date", "value"])

        df = close.copy()
        df.index = pd.to_datetime(df.index, errors="coerce")
        df = df[~df.index.isna()]
        if df.empty:
            return pd.DataFrame(columns=["date", "value"])

        df = df.reset_index()
        first_col = df.columns[0]
        df = df.rename(columns={first_col: "date"})
        df.columns = [str(c).strip().lower().replace("-", "_").replace(" ", "_") for c in df.columns]

        value_cols = [c for c in df.columns if c != "date"]
        if value_cols and "value" not in df.columns:
            df["value"] = pd.to_numeric(df[value_cols[0]], errors="coerce")

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])
        return df.sort_values("date").reset_index(drop=True)
    except Exception:
        return pd.DataFrame(columns=["date", "value"])
