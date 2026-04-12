import pandas as pd


def fetch_fred_series(series_id: str, api_key: str) -> pd.DataFrame:
    """
    Fetch a FRED series into a DataFrame with columns: date, value.
    """
    from fredapi import Fred

    fred = Fred(api_key=api_key)
    series = fred.get_series(series_id)
    df = pd.DataFrame({"value": series}).dropna()
    df.index = pd.to_datetime(df.index)
    df = df.reset_index().rename(columns={"index": "date"})
    return df
