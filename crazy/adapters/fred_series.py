import pandas as pd


def fetch_fred_series(series_id: str, api_key: str) -> pd.DataFrame:
    """
    Fetch a FRED series into a DataFrame with columns: date, value.
    Returns empty DataFrame if api_key is missing or on any failure.
    """
    if not api_key:
        return pd.DataFrame()
    try:
        from fredapi import Fred
        fred = Fred(api_key=api_key)
        series = fred.get_series(series_id)
        df = pd.DataFrame({"value": series}).dropna()
        df.index = pd.to_datetime(df.index)
        df = df.reset_index().rename(columns={"index": "date"})
        return df
    except Exception:
        return pd.DataFrame()
