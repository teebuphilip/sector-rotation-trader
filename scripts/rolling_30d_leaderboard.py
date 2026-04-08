#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import pandas as pd

from scanner import safe_download


def _load_state(path: Path) -> dict | None:
    if not path.exists():
        return None
    with path.open() as f:
        return json.load(f)


def _snap_df(state: dict) -> pd.DataFrame:
    snaps = state.get("daily_snapshots", [])
    if not snaps:
        return pd.DataFrame()
    df = pd.DataFrame(snaps)
    if "date" not in df.columns:
        return pd.DataFrame()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    return df.sort_values("date")


def _rolling_30d_return(df: pd.DataFrame) -> float | None:
    if df.empty:
        return None
    cutoff = df["date"].max() - pd.Timedelta(days=30)
    window = df[df["date"] >= cutoff]
    if len(window) < 2:
        return None
    start = float(window.iloc[0]["equity"])
    end = float(window.iloc[-1]["equity"])
    if start <= 0:
        return None
    return (end / start) - 1


def _rolling_sharpe(df: pd.DataFrame) -> float | None:
    if df.empty:
        return None
    cutoff = df["date"].max() - pd.Timedelta(days=30)
    window = df[df["date"] >= cutoff]
    if len(window) < 2:
        return None
    returns = window["equity"].pct_change().dropna()
    if returns.empty or returns.std() == 0:
        return 0.0
    excess = returns.mean() - (0.045 / 252)
    return float(excess / returns.std() * (252 ** 0.5))


def _rolling_max_dd(df: pd.DataFrame) -> float | None:
    if df.empty:
        return None
    cutoff = df["date"].max() - pd.Timedelta(days=30)
    window = df[df["date"] >= cutoff]
    if window.empty:
        return None
    peak = -1e18
    max_dd = 0.0
    for _, row in window.iterrows():
        eq = float(row["equity"])
        if eq > peak:
            peak = eq
        dd = (eq - peak) / peak if peak > 0 else 0
        if dd < max_dd:
            max_dd = dd
    return max_dd


def _spy_30d_return() -> float | None:
    raw = safe_download(["SPY"], period="3mo")
    if raw.empty:
        return None
    prices = raw["Close"] if "Close" in raw.columns else raw
    s = prices["SPY"].dropna()
    if len(s) < 2:
        return None
    cutoff = s.index.max() - pd.Timedelta(days=30)
    window = s[s.index >= cutoff]
    if len(window) < 2:
        return None
    return (float(window.iloc[-1]) / float(window.iloc[0])) - 1


def main() -> int:
    entries = []

    # Baseline NRWise
    base_state = _load_state(Path("state.json"))
    if base_state:
        df = _snap_df(base_state)
        entries.append({
            "algo_id": "nrwise",
            "name": "NRWise Acceleration",
            "category": "standard",
            "ret_30d": _rolling_30d_return(df),
            "sharpe_30d": _rolling_sharpe(df),
            "max_dd_30d": _rolling_max_dd(df),
        })

    # Normal algos
    normal_dir = Path("data/normal/state")
    if normal_dir.exists():
        for path in normal_dir.glob("*.json"):
            state = _load_state(path)
            if not state:
                continue
            algo_id = path.stem
            meta = state.get("meta", {}).get(algo_id, {})
            name = meta.get("name") or algo_id
            df = _snap_df(state)
            entries.append({
                "algo_id": algo_id,
                "name": name,
                "category": "standard",
                "ret_30d": _rolling_30d_return(df),
                "sharpe_30d": _rolling_sharpe(df),
                "max_dd_30d": _rolling_max_dd(df),
            })

    # Crazy algos
    crazy_dir = Path("data/crazy/state")
    if crazy_dir.exists():
        for path in crazy_dir.glob("*.json"):
            state = _load_state(path)
            if not state:
                continue
            algo_id = path.stem
            meta = state.get("meta", {}).get(algo_id, {})
            name = meta.get("name") or algo_id
            df = _snap_df(state)
            entries.append({
                "algo_id": algo_id,
                "name": name,
                "category": "crazy",
                "ret_30d": _rolling_30d_return(df),
                "sharpe_30d": _rolling_sharpe(df),
                "max_dd_30d": _rolling_max_dd(df),
            })

    spy_ret = _spy_30d_return()

    def _sort_key(e):
        r = e.get("ret_30d")
        return -999 if r is None else r

    entries_sorted = sorted(entries, key=_sort_key, reverse=True)

    out_dir = Path("docs/leaderboards")
    out_dir.mkdir(parents=True, exist_ok=True)

    out_json = {
        "as_of": datetime.utcnow().isoformat(),
        "spy_ret_30d": spy_ret,
        "entries": entries_sorted,
    }
    (out_dir / "rolling_30d.json").write_text(json.dumps(out_json, indent=2))

    # Markdown summary
    lines = ["# 30-Day Rolling Leaderboard", "", f"SPY 30D Return: {spy_ret:+.2%}" if spy_ret is not None else "SPY 30D Return: n/a", "", "| Rank | Algo | Category | 30D Return | 30D Sharpe | 30D Max DD |", "| --- | --- | --- | --- | --- | --- |"]
    for i, e in enumerate(entries_sorted, start=1):
        r = e.get("ret_30d")
        s = e.get("sharpe_30d")
        d = e.get("max_dd_30d")
        lines.append(
            "| {rank} | {name} | {cat} | {ret} | {sharpe} | {dd} |".format(
                rank=i,
                name=e.get("name"),
                cat=e.get("category"),
                ret=f"{r:+.2%}" if r is not None else "n/a",
                sharpe=f"{s:.2f}" if s is not None else "n/a",
                dd=f"{d:.2%}" if d is not None else "n/a",
            )
        )

    (out_dir / "rolling_30d.md").write_text("\n".join(lines) + "\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
