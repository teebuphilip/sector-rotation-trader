from datetime import datetime, timedelta
from typing import Iterable

import pandas as pd
import feedparser


def fetch_rss_counts(feed_urls: Iterable[str], days_back: int = 7) -> pd.DataFrame:
    """
    Fetch RSS feeds and return counts per day.
    Columns: date, count
    """
    cutoff = datetime.utcnow().date() - timedelta(days=days_back)
    rows = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            published = entry.get("published_parsed") or entry.get("updated_parsed")
            if not published:
                continue
            day = datetime(*published[:6]).date()
            if day < cutoff:
                continue
            rows.append({"date": day.isoformat(), "count": 1})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["date"] = pd.to_datetime(df["date"])
    df = df.groupby("date")["count"].sum().reset_index()
    return df.sort_values("date")
