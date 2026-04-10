#!/usr/bin/env python3
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from normal.algos import get_normal_algos
from crazy.algos import get_crazy_algos


def main() -> int:
    normals = get_normal_algos()
    crazies = get_crazy_algos()

    lines = []
    lines.append("# Algo Index")
    lines.append("")
    lines.append(f"Updated (UTC): {datetime.utcnow().isoformat(timespec='seconds')}")
    lines.append("")
    lines.append(f"Normal models: {len(normals)}")
    lines.append("")
    lines.append("| Algo ID | Name | Frequency |")
    lines.append("| --- | --- | --- |")
    for a in normals:
        lines.append(f"| {a.algo_id} | {a.name} | {a.rebalance_frequency} |")
    lines.append("")
    lines.append(f"Crazy models: {len(crazies)}")
    lines.append("")
    lines.append("| Algo ID | Name | Frequency |")
    lines.append("| --- | --- | --- |")
    for a in crazies:
        lines.append(f"| {a.algo_id} | {a.name} | {a.rebalance_frequency} |")

    out_path = Path("docs") / "algos" / "index.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
