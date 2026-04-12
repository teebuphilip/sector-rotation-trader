from datetime import datetime, timedelta

import pandas as pd
from pytrends.request import TrendReq


def fetch_google_trends(keyword: str, days_back: int = 30) -> pd.DataFrame:
    """
    Fetch Google Trends interest over time for a keyword.
    Returns DataFrame with columns: date, interest.
    """
    pytrends = TrendReq(hl="en-US", tz=0)
    end = datetime.utcnow()
    start = end - timedelta(days=days_back)
    timeframe = f"{start.strftime('%Y-%m-%d')} {end.strftime('%Y-%m-%d')}"
    pytrends.build_payload([keyword], timeframe=timeframe)
    df = pytrends.interest_over_time()
    if df.empty:
        return df
    df = df.reset_index().rename(columns={keyword: "interest", "date": "date"})
    return df[["date", "interest"]]
