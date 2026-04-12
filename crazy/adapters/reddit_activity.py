import os
from datetime import datetime, timedelta
from typing import Iterable

import pandas as pd
import requests

from crazy.config import CRAZY_CACHE_DIR
from crazy.utils import cached_fetch


def fetch_reddit_activity(
    subreddits: Iterable[str],
    days_back: int = 14,
    cache_key: str = "reddit_activity.json",
) -> pd.DataFrame:
    """
    Fetch recent Reddit activity using public JSON endpoints.
    Returns DataFrame with columns: date, posts, comments.
    Notes: num_comments is attached to posts, not separate comment objects.
    """
    cache_path = os.path.join(CRAZY_CACHE_DIR, cache_key)

    def _fetch():
        rows = []
        headers = {"User-Agent": "sector-rotation-trader/1.0"}
        cutoff = datetime.utcnow().date() - timedelta(days=days_back)
        for subreddit in subreddits:
            name = subreddit.replace("r/", "")
            url = f"https://www.reddit.com/r/{name}/new.json?limit=100"
            try:
                resp = requests.get(url, headers=headers, timeout=20)
                if resp.status_code != 200:
                    continue
                data = resp.json()
            except Exception:
                continue

            for child in data.get("data", {}).get("children", []):
                item = child.get("data", {})
                created = item.get("created_utc")
                if created is None:
                    continue
                day = datetime.utcfromtimestamp(created).date()
                if day < cutoff:
                    continue
                rows.append(
                    {
                        "date": day.isoformat(),
                        "posts": 1,
                        "comments": int(item.get("num_comments", 0) or 0),
                    }
                )
        return rows

    data = cached_fetch(cache_path, ttl_hours=6, fetch_fn=_fetch) or []
    df = pd.DataFrame(data)
    if df.empty:
        return df
    df["date"] = pd.to_datetime(df["date"])
    df = df.groupby("date")[["posts", "comments"]].sum().reset_index()
    return df.sort_values("date")
