# Adapter Rules

Rules for writing and maintaining adapters in `crazy/adapters/`.

## What is an adapter?

An adapter is a single-purpose function that fetches external data and returns it as a pandas DataFrame (or dict). Adapters are called by algo `compute_signal()` and `target_allocations()` methods. They are the **only** place where external HTTP calls, API keys, and third-party libraries should live.

## Required contract

Every adapter function MUST follow this contract:

1. **Return type**: `pd.DataFrame` (or `dict` for aggregation adapters like `socrata_311`).
2. **Never raise exceptions to the caller.** Wrap all I/O in `try/except Exception` and return an empty DataFrame/dict on failure. An adapter failure should never crash the pipeline.
3. **Return empty on missing credentials.** If the adapter needs an API key (`os.getenv(...)`), check it early and return empty if missing. Do not let the HTTP call fail with an auth error.
4. **Timeout all HTTP requests.** Use `timeout=20` to `timeout=30` on every `requests.get()` call.
5. **No bare top-level imports of optional packages.** If the adapter uses a package not in the core deps (yfinance, pandas, numpy), import it inside the function body so a missing package returns empty instead of crashing on import. Examples: `feedparser`, `pytrends`, `fredapi`, `sodapy`.

## Python compatibility

- **No `X | None` union syntax.** Use `Optional[X]` from `typing` if needed.
- **No `list[str]` or `dict[str, int]` generic syntax.** Use `list`, `dict` (unparameterized) or `List[str]`, `Dict[str, int]` from `typing`.
- The repo runs on Python 3.9 locally and Python 3.11 in CI. Code must work on both.

## Output format

- DataFrame adapters should return columns named: `date` plus one or more value columns.
- The `date` column should be `pd.Timestamp` type (call `pd.to_datetime()` before returning).
- Sort by date ascending before returning.
- Column names should be lowercase, snake_case.

## Naming conventions

- File: `snake_case.py` (e.g., `google_trends.py`, `earthquake_activity.py`)
- Function: `fetch_<data_source>` (e.g., `fetch_google_trends`, `fetch_earthquake_activity`)
- One public function per adapter file.

## Registration

After creating a new adapter:
1. Add an import line to `crazy/adapters/__init__.py`
2. Add the function name to the `__all__` list

## Template

```python
import os
from datetime import datetime, timedelta

import pandas as pd


def fetch_my_data_source(param: str, days_back: int = 7) -> pd.DataFrame:
    """
    Fetch data from MySource.
    Returns DataFrame with columns: date, value.
    Returns empty DataFrame on any failure.
    """
    # Check credentials early
    api_key = os.getenv("MY_API_KEY")
    if not api_key:
        return pd.DataFrame()

    try:
        import requests  # or any optional dep
        resp = requests.get(
            "https://api.example.com/data",
            params={"key": api_key, "q": param},
            timeout=20,
        )
        resp.raise_for_status()
        data = resp.json()

        rows = []
        cutoff = datetime.utcnow().date() - timedelta(days=days_back)
        for item in data:
            day = datetime.fromisoformat(item["timestamp"]).date()
            if day < cutoff:
                continue
            rows.append({"date": day.isoformat(), "value": item["value"]})

        df = pd.DataFrame(rows)
        if df.empty:
            return df
        df["date"] = pd.to_datetime(df["date"])
        return df.sort_values("date")
    except Exception:
        return pd.DataFrame()
```

## Anti-patterns (do NOT do these)

- `from pytrends.request import TrendReq` at module top level — crashes on import if package missing
- `resp.raise_for_status()` without a surrounding try/except — crashes pipeline on HTTP error
- `list[str]` type hints — breaks Python 3.9
- Returning `None` instead of empty DataFrame — caller gets AttributeError on `.empty`
- Hardcoding API keys — always use `os.getenv()`
