import os

import pandas as pd


def fetch_yelp_closure_rate(categories="restaurants,shopping,servicestothehome", location="US", sample_limit=200):
    """
    Estimate business closure velocity using the Yelp Fusion search API.

    Searches for businesses in consumer-facing categories and counts the
    fraction that are permanently closed. Returns a single-row DataFrame
    with today's sampled closure rate so the algo can track week-over-week
    change in state.

    Returns DataFrame with columns: date, closure_rate, closed_count, total_count.
    Returns empty DataFrame if YELP_API_KEY is missing or on any failure.
    """
    api_key = os.getenv("YELP_API_KEY")
    if not api_key:
        return pd.DataFrame()

    try:
        import requests
        from datetime import date

        headers = {"Authorization": f"Bearer {api_key}"}
        base_url = "https://api.yelp.com/v3/businesses/search"

        closed_count = 0
        total_count = 0
        offset = 0
        batch = 50  # Yelp max per request
        calls = 0
        max_calls = sample_limit // batch

        while calls < max_calls:
            params = {
                "location": "New York, NY",  # proxy for national trend
                "categories": categories,
                "limit": batch,
                "offset": offset,
            }
            resp = requests.get(base_url, headers=headers, params=params, timeout=20)
            if resp.status_code == 429:
                break
            if not resp.ok:
                break
            data = resp.json()
            businesses = data.get("businesses", [])
            if not businesses:
                break
            for b in businesses:
                total_count += 1
                if b.get("is_closed", False):
                    closed_count += 1
            offset += batch
            calls += 1

        if total_count == 0:
            return pd.DataFrame()

        closure_rate = closed_count / total_count
        today = pd.Timestamp(date.today())
        df = pd.DataFrame([{
            "date": today,
            "closure_rate": round(closure_rate, 4),
            "closed_count": closed_count,
            "total_count": total_count,
        }])
        df["date"] = pd.to_datetime(df["date"])
        return df

    except Exception:
        return pd.DataFrame()
