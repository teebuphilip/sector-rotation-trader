import os
from datetime import datetime, timedelta
from typing import Iterable

import pandas as pd
import requests

from crazy.config import CRAZY_CACHE_DIR
from crazy.utils import cached_fetch


def fetch_twitter_activity(
    query: str,
    days_back: int = 7,
    cache_key: str = "twitter_activity.json",
) -> pd.DataFrame:
    """
    Fetch recent tweet activity using Twitter/X v2 recent search.
    Returns DataFrame with columns: date, tweets.
    Requires TWITTER_BEARER_TOKEN or TWITTER_API_KEY.
    """
    token = os.getenv("TWITTER_BEARER_TOKEN") or os.getenv("TWITTER_API_KEY")
    if not token:
        return pd.DataFrame()

    cache_path = os.path.join(CRAZY_CACHE_DIR, cache_key)

    def _fetch():
        rows = []
        headers = {"Authorization": f"Bearer {token}"}
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=days_back)
        url = "https://api.twitter.com/2/tweets/search/recent"
        params = {
            "query": query,
            "max_results": 100,
            "start_time": start_time.isoformat(timespec="seconds") + "Z",
            "end_time": end_time.isoformat(timespec="seconds") + "Z",
            "tweet.fields": "created_at",
        }
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=20)
            if resp.status_code != 200:
                return []
            data = resp.json()
        except Exception:
            return []

        for item in data.get("data", []):
            created = item.get("created_at")
            if not created:
                continue
            try:
                day = datetime.fromisoformat(created.replace("Z", "+00:00")).date()
            except Exception:
                continue
            rows.append({"date": day.isoformat(), "tweets": 1})
        return rows

    try:
        data = cached_fetch(cache_path, ttl_hours=2, fetch_fn=_fetch) or []
        df = pd.DataFrame(data)
        if df.empty:
            return df
        df["date"] = pd.to_datetime(df["date"])
        df = df.groupby("date")["tweets"].sum().reset_index()
        return df.sort_values("date")
    except Exception:
        return pd.DataFrame()
