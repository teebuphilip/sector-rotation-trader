from __future__ import annotations

from io import StringIO

import pandas as pd


PORT_LA_TEU_CSV_URL = "https://data.lacity.org/api/views/tsuv-4rgh/rows.csv?accessType=DOWNLOAD"
PORT_LA_HISTORY_URL = "https://www.portoflosangeles.org/business/statistics/container-statistics/historical-teu-statistics-{year}"


def _snake(value: object) -> str:
    return str(value).strip().lower().replace("/", "_").replace("-", "_").replace(" ", "_")


def _parse_month_year(df: pd.DataFrame) -> pd.Series:
    cols = set(df.columns)
    if "date" in cols:
        return pd.to_datetime(df["date"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce").fillna(
            pd.to_datetime(df["date"], errors="coerce")
        )
    if "period" in cols:
        return pd.to_datetime(df["period"], errors="coerce")
    if "month" in cols and "year" in cols:
        return pd.to_datetime(df["year"].astype(str) + " " + df["month"].astype(str), errors="coerce")
    if "month_year" in cols:
        return pd.to_datetime(df["month_year"], errors="coerce")
    return pd.Series(pd.NaT, index=df.index)


def _get_text(url: str, timeout: int = 20) -> str:
    import requests

    try:
        return requests.get(url, timeout=timeout).text
    except requests.exceptions.SSLError:
        from requests.packages.urllib3.exceptions import InsecureRequestWarning

        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        return requests.get(url, timeout=timeout, verify=False).text


def _fetch_recent_port_site(years_back: int = 4) -> pd.DataFrame:
    rows = []
    current_year = pd.Timestamp.utcnow().year
    for year in range(current_year - years_back + 1, current_year + 1):
        html = _get_text(PORT_LA_HISTORY_URL.format(year=year))
        tables = pd.read_html(StringIO(html))
        if len(tables) < 2:
            continue
        table = tables[1].copy()
        if table.empty or table.shape[1] < 8:
            continue
        for _, row in table.iloc[1:].iterrows():
            month = str(row.iloc[0]).strip()
            if not month or month.lower() == "nan" or "calendar" in month.lower() or "fiscal" in month.lower():
                continue
            value = pd.to_numeric(str(row.iloc[7]).replace(",", ""), errors="coerce")
            date = pd.to_datetime(f"{year} {month} 1", errors="coerce")
            if pd.isna(date) or pd.isna(value):
                continue
            rows.append({"date": date, "value": float(value), "total_teus": float(value)})
    if not rows:
        return pd.DataFrame(columns=["date", "value"])
    return pd.DataFrame(rows).drop_duplicates("date").sort_values("date").reset_index(drop=True)


def _fetch_legacy_lacity_csv() -> pd.DataFrame:
    df = pd.read_csv(StringIO(_get_text(PORT_LA_TEU_CSV_URL)))
    if df.empty:
        return pd.DataFrame(columns=["date", "value"])

    df.columns = [_snake(c) for c in df.columns]
    df["date"] = _parse_month_year(df)

    value_col = None
    candidates = [
        "monthly_total_teus",
        "total_teus",
        "total_teu",
        "total",
        "teus",
        "total_containers",
        "container_count",
    ]
    for col in candidates:
        if col in df.columns:
            value_col = col
            break
    if value_col is None:
        teu_cols = [c for c in df.columns if "teu" in c and "ytd" not in c and "change" not in c]
        if teu_cols:
            value_col = teu_cols[0]
    if value_col is None:
        return pd.DataFrame(columns=["date", "value"])

    df["value"] = pd.to_numeric(df[value_col].astype(str).str.replace(",", "", regex=False), errors="coerce")
    if "total_teus" not in df.columns:
        df["total_teus"] = df["value"]
    df = df.dropna(subset=["date", "value"])
    if df.empty:
        return pd.DataFrame(columns=["date", "value"])
    keep = [c for c in ["date", "value", "total_teus"] if c in df.columns]
    return df[keep].sort_values("date").reset_index(drop=True)


def fetch_port_container_volume() -> pd.DataFrame:
    """
    Fetch Port of Los Angeles monthly TEU container volume.

    Standard output:
      - date: pd.Timestamp
      - value: total TEUs
      - total_teus: same as value when available

    Returns an empty DataFrame on any I/O/schema failure.
    Primary source: Port of Los Angeles historical TEU tables.
    Fallback source: data.lacity.org dataset tsuv-4rgh.
    """
    try:
        df = _fetch_recent_port_site()
        if not df.empty:
            return df
        return _fetch_legacy_lacity_csv()
    except Exception:
        try:
            return _fetch_legacy_lacity_csv()
        except Exception:
            return pd.DataFrame(columns=["date", "value"])
