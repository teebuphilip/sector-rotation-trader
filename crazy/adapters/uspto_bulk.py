import pandas as pd


# CPC class prefixes that map to tech/innovation sectors
# G06 = Computing/Software, H01L = Semiconductors, H04 = Communications
TECH_CPC_GROUPS = ["G06", "H01L", "H04"]


def fetch_uspto_patent_counts(months_back=18):
    """
    Fetch quarterly US patent application counts via the PatentsView API (free, no key).

    Uses CPC class G06 (computing/software) as the primary tech sector proxy.
    Returns DataFrame with columns: date, patent_count, cpc_class.
    Returns empty DataFrame on any failure.

    PatentsView docs: https://patentsview.org/apis/api-endpoints/patents
    """
    try:
        import requests
        from datetime import date, timedelta

        cutoff = date.today() - timedelta(days=months_back * 30)
        cutoff_str = cutoff.strftime("%Y-%m-%d")

        # Query PatentsView for patents filed in G06 (computing) since cutoff
        url = "https://api.patentsview.org/patents/query"
        payload = {
            "q": {
                "_and": [
                    {"_gte": {"patent_date": cutoff_str}},
                    {"_contains": {"cpc_group_id": "G06"}},
                ]
            },
            "f": ["patent_id", "patent_date", "cpc_group_id"],
            "o": {"page": 1, "per_page": 10000},
        }

        resp = requests.post(url, json=payload, timeout=30)
        if not resp.ok:
            return pd.DataFrame()

        data = resp.json()
        patents = data.get("patents") or []
        if not patents:
            return pd.DataFrame()

        rows = []
        for p in patents:
            d = p.get("patent_date")
            if not d:
                continue
            rows.append({"date": d})

        if not rows:
            return pd.DataFrame()

        df = pd.DataFrame(rows)
        df["date"] = pd.to_datetime(df["date"])
        # Aggregate to quarterly counts
        df = df.set_index("date").resample("QS").size().reset_index()
        df.columns = ["date", "patent_count"]
        df["cpc_class"] = "G06"
        return df.sort_values("date")

    except Exception:
        return pd.DataFrame()
