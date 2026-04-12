#!/usr/bin/env python3
"""
Deterministic patcher fallback that guarantees syntactically valid code.
Currently implements a generic reddit_activity template.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _extract_between(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0]


def _replace_between(text: str, start: str, end: str, replacement: str) -> str:
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return before + start + replacement + end + after


def _indent(lines: str, spaces: int = 8) -> str:
    prefix = " " * spaces
    out = []
    for line in lines.splitlines():
        if line.strip() == "":
            out.append("")
        else:
            out.append(prefix + line)
    return "\n" + "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--spec", required=True)
    args = parser.parse_args()

    path = Path(args.file)
    code = _read(path)
    sliced = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    adapters = sliced.get("adapters") or []
    spec = sliced.get("sliced_spec") or {}

    adapter = adapters[0] if adapters else ""
    universe = spec.get("universe", []) or []
    universe_list = ", ".join([f"\"{u}\"" for u in universe])

    if adapter == "reddit_activity":
        signal_block = f"""
data = fetch_reddit_activity(subreddits=["r/gaming", "r/pcgaming", "r/games"], days_back=14)
df = data if isinstance(data, pd.DataFrame) else pd.DataFrame()
if df.empty:
    return "HOLD"
df["total"] = df["posts"] + df["comments"]
df = df.sort_values("date").reset_index(drop=True)
if len(df) < 8:
    return "HOLD"
latest = df.iloc[-1]
ma7 = df["total"].iloc[-8:-1].mean()
if ma7 == 0 or pd.isna(ma7):
    return "HOLD"
position = self.position()
if position and position.get("entry_date"):
    days_held = (latest["date"] - position["entry_date"]).days
    if latest["total"] < ma7 or days_held >= 5:
        return "RISK_OFF"
    return "HOLD"
if latest["total"] > 1.5 * ma7:
    return "RISK_ON"
return "HOLD"
"""

        alloc_block = f"""
if signal == "RISK_ON":
    targets = [t for t in self.universe() if t in {{"ATVI", "EA", "NVDA"}}]
    if not targets:
        return {{}}
    weight = 0.05
    allocation = {{t: weight for t in targets}}
    total_alloc = sum(allocation.values())
    if total_alloc > 0.20:
        scale = 0.20 / total_alloc
        allocation = {{k: v * scale for k, v in allocation.items()}}
    return allocation
if signal == "RISK_OFF":
    return {{}}
return {{}}
"""
    else:
        # Generic safe fallback
        signal_block = """
return "HOLD"
"""
        alloc_block = """
if signal == "RISK_ON":
    return {}
if signal == "RISK_OFF":
    return {}
return {}
"""

    code = _replace_between(code, "# === SIGNAL_LOGIC_START ===", "# === SIGNAL_LOGIC_END ===", _indent(signal_block.strip()))
    code = _replace_between(code, "# === ALLOCATION_LOGIC_START ===", "# === ALLOCATION_LOGIC_END ===", _indent(alloc_block.strip()))
    _write(path, code)
    print("[patch-deterministic] applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
