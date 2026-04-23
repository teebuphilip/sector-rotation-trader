from __future__ import annotations

from io import BytesIO
import re
import zipfile

import pandas as pd


BTS_DOMESTIC_SEGMENT_PAGE = "https://www.bts.gov/browse-statistical-products-and-data/bts-publications/data-bank-28ds-t-100-domestic-segment-data"
BTS_MTS_AIRLINE_TRAFFIC_URL = (
    "https://data.bts.gov/resource/crem-w557.json?"
    "$select=date,system_use_u_s_airline&"
    "$where=system_use_u_s_airline is not null&"
    "$order=date desc&$limit=120"
)


def _snake(value: object) -> str:
    return str(value).strip().lower().replace("/", "_").replace("-", "_").replace(" ", "_")


def _latest_zip_url(html: str) -> str:
    matches = re.findall(r'https://www\.bts\.gov/sites/bts\.dot\.gov/files/docs/airline-data/domestic-segments/[^"\']+?\.zip', html)
    return matches[0] if matches else ""


def _get(url: str, timeout: int = 20):
    import requests

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Stockarithm/1.0; +https://stockarithm.com)"
    }
    try:
        return requests.get(url, headers=headers, timeout=timeout)
    except requests.exceptions.SSLError:
        from requests.packages.urllib3.exceptions import InsecureRequestWarning

        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        return requests.get(url, headers=headers, timeout=timeout, verify=False)


def _fetch_mts_airline_traffic() -> pd.DataFrame:
    resp = _get(BTS_MTS_AIRLINE_TRAFFIC_URL, timeout=20)
    resp.raise_for_status()
    rows = resp.json()
    if not rows:
        return pd.DataFrame(columns=["date", "value"])
    df = pd.DataFrame(rows)
    if "date" not in df.columns or "system_use_u_s_airline" not in df.columns:
        return pd.DataFrame(columns=["date", "value"])
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["value"] = pd.to_numeric(df["system_use_u_s_airline"], errors="coerce")
    df["airline_traffic"] = df["value"]
    df = df.dropna(subset=["date", "value"])
    if df.empty:
        return pd.DataFrame(columns=["date", "value"])
    return df[["date", "value", "airline_traffic"]].sort_values("date").reset_index(drop=True)


def fetch_bts_airline_load_factor() -> pd.DataFrame:
    """
    Fetch latest BTS T-100 domestic segment data and aggregate load factor.

    Standard output:
      - date: pd.Timestamp month start
      - passengers: summed passengers
      - seats: summed seats
      - value: passengers / seats
      - load_factor: same as value

    Returns an empty DataFrame on any I/O/schema failure.
    Primary source: BTS Data Bank 28DS T-100 Domestic Segment Data.
    Fallback source: BTS Monthly Transportation Statistics domestic airline traffic.
    """
    try:
        page = _get(BTS_DOMESTIC_SEGMENT_PAGE, timeout=20)
        page.raise_for_status()
        zip_url = _latest_zip_url(page.text)
        if not zip_url:
            return _fetch_mts_airline_traffic()

        data = _get(zip_url, timeout=40)
        data.raise_for_status()
        with zipfile.ZipFile(BytesIO(data.content)) as zf:
            names = [n for n in zf.namelist() if n.lower().endswith((".csv", ".txt"))]
            if not names:
                return pd.DataFrame(columns=["date", "value"])
            with zf.open(names[0]) as fh:
                df = pd.read_csv(fh, low_memory=False)

        if df.empty:
            return pd.DataFrame(columns=["date", "value"])
        df.columns = [_snake(c) for c in df.columns]

        year_col = "year" if "year" in df.columns else None
        month_col = "month" if "month" in df.columns else None
        passenger_col = "passengers" if "passengers" in df.columns else None
        seats_col = "seats" if "seats" in df.columns else None
        if not all([year_col, month_col, passenger_col, seats_col]):
            return pd.DataFrame(columns=["date", "value"])

        work = df[[year_col, month_col, passenger_col, seats_col]].copy()
        work["year"] = pd.to_numeric(work[year_col], errors="coerce")
        work["month"] = pd.to_numeric(work[month_col], errors="coerce")
        work["passengers"] = pd.to_numeric(work[passenger_col], errors="coerce")
        work["seats"] = pd.to_numeric(work[seats_col], errors="coerce")
        work = work.dropna(subset=["year", "month", "passengers", "seats"])
        if work.empty:
            return pd.DataFrame(columns=["date", "value"])

        grouped = work.groupby(["year", "month"], as_index=False)[["passengers", "seats"]].sum()
        grouped = grouped[grouped["seats"] > 0]
        if grouped.empty:
            return pd.DataFrame(columns=["date", "value"])
        grouped["date"] = pd.to_datetime(
            grouped["year"].astype(int).astype(str) + "-" + grouped["month"].astype(int).astype(str) + "-01",
            errors="coerce",
        )
        grouped["load_factor"] = grouped["passengers"] / grouped["seats"]
        grouped["value"] = grouped["load_factor"]
        grouped = grouped.dropna(subset=["date", "value"])
        keep = ["date", "value", "load_factor", "passengers", "seats"]
        return grouped[keep].sort_values("date").reset_index(drop=True)
    except Exception:
        try:
            return _fetch_mts_airline_traffic()
        except Exception:
            return pd.DataFrame(columns=["date", "value"])
