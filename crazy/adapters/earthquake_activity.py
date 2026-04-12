from datetime import datetime, timedelta

import pandas as pd


def fetch_earthquake_activity(days_back: int = 7) -> pd.DataFrame:
    """
    Fetch USGS earthquake feed counts per day.
    Returns DataFrame with columns: date, quakes.
    Returns empty DataFrame on any failure.
    """
    try:
        import requests
        if days_back <= 1:
            feed = "all_day"
        elif days_back <= 7:
            feed = "all_week"
        else:
            feed = "all_month"

        url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{feed}.geojson"
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        rows = []
        cutoff = datetime.utcnow().date() - timedelta(days=days_back)
        for feat in data.get("features", []):
            ts = feat.get("properties", {}).get("time")
            if ts is None:
                continue
            day = datetime.utcfromtimestamp(ts / 1000.0).date()
            if day < cutoff:
                continue
            rows.append({"date": day.isoformat(), "quakes": 1})
        df = pd.DataFrame(rows)
        if df.empty:
            return df
        df["date"] = pd.to_datetime(df["date"])
        df = df.groupby("date")["quakes"].sum().reset_index()
        return df.sort_values("date")
    except Exception:
        return pd.DataFrame()
