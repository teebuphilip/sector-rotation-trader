from datetime import datetime, timedelta
import logging
import os

import pandas as pd


CITY_CONFIG = {
    "nyc": {"domain": "data.cityofnewyork.us", "endpoint": "erm2-nwe9"},
    "chicago": {"domain": "data.cityofchicago.org", "endpoint": "v6vf-nfjy"},
    "la": {"domain": "data.lacity.org", "endpoint": "aub4-z4ir"},
    "sf": {"domain": "data.sfgov.org", "endpoint": "vw6y-z8j6"},
    "boston": {"domain": "data.boston.gov", "endpoint": "wc8w-nujj"},
}


def fetch_311_counts(days_back: int = 7) -> dict:
    """
    Fetch recent 311 complaint counts (raw by complaint_type) across major cities.
    Returns dict of complaint_type -> count.
    Returns empty dict on any failure.
    """
    try:
        from sodapy import Socrata
    except ImportError:
        return {}

    cutoff = (datetime.utcnow() - timedelta(days=days_back)).isoformat()
    counts = {}
    for _, cfg in CITY_CONFIG.items():
        try:
            app_token = os.getenv("SOCRATA_APP_TOKEN")
            if app_token:
                client = Socrata(cfg["domain"], app_token, timeout=30)
            else:
                previous_disable = logging.root.manager.disable
                logging.disable(logging.WARNING)
                try:
                    client = Socrata(cfg["domain"], None, timeout=30)
                finally:
                    logging.disable(previous_disable)
            results = client.get(
                cfg["endpoint"],
                where=f"created_date > '{cutoff}'",
                select="complaint_type",
                limit=50000,
            )
            if not results:
                continue
            df = pd.DataFrame.from_records(results)
            if df.empty or "complaint_type" not in df.columns:
                continue
            df["complaint_type"] = df["complaint_type"].astype(str)
            for val, cnt in df["complaint_type"].value_counts().to_dict().items():
                counts[val] = counts.get(val, 0) + int(cnt)
        except Exception:
            continue
    return counts
