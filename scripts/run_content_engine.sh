#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "[step] write deep validation report"
if [[ $# -gt 0 ]]; then
  python scripts/write_deep_validation_report.py "$@"
else
  python scripts/write_deep_validation_report.py
fi

echo "[step] generate content"
python scripts/generate_content.py --report reports/deep_validation/latest.json

echo "[done] content engine complete"
