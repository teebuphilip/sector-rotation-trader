import pandas as pd
import requests
from io import StringIO


def fetch_html_table(url: str, table_index: int = 0) -> pd.DataFrame:
    """
    Fetch an HTML table by index from a URL.
    """
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    resp.raise_for_status()
    tables = pd.read_html(StringIO(resp.text))
    if not tables:
        return pd.DataFrame()
    idx = min(max(table_index, 0), len(tables) - 1)
    return tables[idx]
