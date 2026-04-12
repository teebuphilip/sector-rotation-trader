import os
from datetime import datetime

import pandas as pd


def fetch_openchargemap_counts(country_code: str = "US", max_results: int = 1000) -> pd.DataFrame:
    """
    Fetch OpenChargeMap POI count as a simple daily series.
    Returns DataFrame with columns: date, count.
    Requires OPENCHARGEMAP_API_KEY env var.
    Returns empty DataFrame if key is missing or on any failure.
    """
    api_key = os.getenv("OPENCHARGEMAP_API_KEY")
    if not api_key:
        return pd.DataFrame()

    try:
        import requests
        url = "https://api.openchargemap.io/v3/poi/"
        params = {
            "output": "json",
            "countrycode": country_code,
            "maxresults": max_results,
            "key": api_key,
        }
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json() or []
        count = len(data)
        df = pd.DataFrame([{"date": datetime.utcnow().date().isoformat(), "count": count}])
        df["date"] = pd.to_datetime(df["date"])
        return df
    except Exception:
        return pd.DataFrame()
