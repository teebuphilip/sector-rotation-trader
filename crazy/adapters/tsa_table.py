import os
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

from crazy.config import CRAZY_CACHE_DIR
from crazy.utils import cached_fetch


def fetch_tsa_table() -> pd.DataFrame:
    """
    Fetch TSA passenger volume table.
    Returns DataFrame with columns: date, throughput, throughput_yoy, yoy_pct.
    """
    cache_path = os.path.join(CRAZY_CACHE_DIR, "tsa.json")

    def _fetch():
        url = "https://www.tsa.gov/travel/passenger-volumes"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("table")
        if table is None:
            return []
        df = pd.read_html(StringIO(str(table)))[0]
        df.columns = [str(c).strip() for c in df.columns]
        date_col = next((c for c in df.columns if c.lower() == "date"), df.columns[0])

        year_cols = [c for c in df.columns if c != date_col]
        year_nums = []
        for c in year_cols:
            try:
                year_nums.append((int(c), c))
            except ValueError:
                continue

        if len(year_nums) >= 2:
            year_nums.sort()
            cur_col = year_nums[-1][1]
            prev_col = year_nums[-2][1]
        else:
            cur_col = year_cols[-1] if year_cols else None
            prev_col = year_cols[-2] if len(year_cols) > 1 else None

        if not cur_col or not prev_col:
            return []

        df["date"] = pd.to_datetime(df[date_col], errors="coerce")
        df["throughput"] = pd.to_numeric(df[cur_col].astype(str).str.replace(",", ""), errors="coerce")
        df["throughput_yoy"] = pd.to_numeric(df[prev_col].astype(str).str.replace(",", ""), errors="coerce")
        df = df.dropna(subset=["date", "throughput", "throughput_yoy"])
        df["yoy_pct"] = (df["throughput"] - df["throughput_yoy"]) / df["throughput_yoy"]
        df = df.sort_values("date")
        return df.to_dict(orient="records")

    try:
        data = cached_fetch(cache_path, ttl_hours=25, fetch_fn=_fetch) or []
        return pd.DataFrame(data)
    except Exception:
        return pd.DataFrame()
