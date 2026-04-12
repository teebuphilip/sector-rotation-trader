from datetime import datetime

import pandas as pd


def fetch_weather_series(latitude: float, longitude: float, days_back: int = 14) -> pd.DataFrame:
    """
    Fetch daily weather series from Open-Meteo.
    Returns DataFrame with columns: date, temp_max, precipitation.
    Returns empty DataFrame on any failure.
    """
    try:
        import requests
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": "temperature_2m_max,precipitation_sum",
            "timezone": "UTC",
            "past_days": days_back,
        }
        resp = requests.get(url, params=params, timeout=20)
        resp.raise_for_status()
        payload = resp.json()
        daily = payload.get("daily", {})
        dates = daily.get("time", [])
        temps = daily.get("temperature_2m_max", [])
        prec = daily.get("precipitation_sum", [])
        rows = []
        for d, t, p in zip(dates, temps, prec):
            rows.append({"date": d, "temp_max": t, "precipitation": p})
        df = pd.DataFrame(rows)
        if df.empty:
            return df
        df["date"] = pd.to_datetime(df["date"])
        return df.sort_values("date")
    except Exception:
        return pd.DataFrame()
