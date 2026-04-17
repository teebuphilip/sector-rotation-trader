from __future__ import annotations

import pandas as pd


EIA_DAILY_REGION_URL = "https://api.eia.gov/v2/electricity/rto/daily-region-data/data/"


def fetch_eia_electricity(
    api_key: str,
    respondent: str = "US48",
    days_back: int = 180,
    type_id: str = "D",
) -> pd.DataFrame:
    """
    Fetch EIA daily regional electricity demand.

    Standard output:
      - date: pd.Timestamp
      - value: numeric demand value
      - respondent: EIA balancing/region id when returned
      - type: EIA metric type when returned

    Returns an empty DataFrame on missing key or any I/O/schema failure.
    Source: EIA Open Data API v2 electricity/rto/daily-region-data.
    """
    if not api_key:
        return pd.DataFrame(columns=["date", "value"])

    try:
        import requests

        params = {
            "api_key": api_key,
            "frequency": "daily",
            "data[]": "value",
            "facets[respondent][]": respondent,
            "facets[type][]": type_id,
            "sort[0][column]": "period",
            "sort[0][direction]": "desc",
            "length": str(max(int(days_back), 1)),
        }
        resp = requests.get(EIA_DAILY_REGION_URL, params=params, timeout=20)
        resp.raise_for_status()
        rows = resp.json().get("response", {}).get("data", [])
        if not rows:
            return pd.DataFrame(columns=["date", "value"])

        df = pd.DataFrame(rows)
        if "period" not in df.columns or "value" not in df.columns:
            return pd.DataFrame(columns=["date", "value"])

        df = df.rename(columns={"period": "date"})
        df.columns = [str(c).strip().lower().replace("-", "_").replace(" ", "_") for c in df.columns]
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        df = df.dropna(subset=["date", "value"])
        if df.empty:
            return pd.DataFrame(columns=["date", "value"])
        return df.sort_values("date").reset_index(drop=True)
    except Exception:
        return pd.DataFrame(columns=["date", "value"])
