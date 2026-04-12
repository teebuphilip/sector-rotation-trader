#!/usr/bin/env bash
set -euo pipefail

SPEC_FILE=""
OUT_FILE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --spec-file)
      SPEC_FILE="$2"; shift 2;;
    --output-path)
      OUT_FILE="$2"; shift 2;;
    *)
      echo "Unknown arg: $1" >&2
      exit 1;;
  esac
done

if [[ -z "$SPEC_FILE" || -z "$OUT_FILE" ]]; then
  echo "Usage: $0 --spec-file <spec-file.md> --output-path <output-algo.py>"
  exit 1
fi

if [[ ! -f "$SPEC_FILE" ]]; then
  echo "Spec not found: $SPEC_FILE"
  exit 1
fi

RUN_DIR="data/algos_codegen/structural_$(date +%Y-%m-%d_%H%M%S)"
mkdir -p "$RUN_DIR"
echo "[run] dir=$RUN_DIR"
echo "[run] spec=$SPEC_FILE"
echo "[run] out=$OUT_FILE"

echo "[step] grill"
python scripts/grill_algo_spec.py --spec-file "$SPEC_FILE" --out-spec "$RUN_DIR/grilled_spec.json" --out-report "$RUN_DIR/grill_report.json"
echo "[grill] wrote $RUN_DIR/grilled_spec.json"
echo "[grill] wrote $RUN_DIR/grill_report.json"

echo "[step] adapter route"
ADAPTERS_JSON=$(python scripts/adapter_router.py --spec-file "$SPEC_FILE")
ADAPTERS=$(python - <<PY
import json,sys
data=json.loads('''$ADAPTERS_JSON''')
print(",".join(data.get("adapters") or []))
PY
)
echo "[route] adapters=${ADAPTERS:-none}"

if [[ -z "$ADAPTERS" ]]; then
  echo "[route] no adapter match; parking"
  echo "{\"spec_file\":\"$SPEC_FILE\",\"reason\":\"no_adapter_match\"}" >> data/ideas/adapter_queue.jsonl
  exit 2
fi

echo "[step] slice"
python scripts/slice_algo_spec.py --spec "$RUN_DIR/grilled_spec.json" --adapters "$ADAPTERS" --out "$RUN_DIR/sliced_spec.json"
echo "[slice] wrote $RUN_DIR/sliced_spec.json"

echo "[step] build structural"
python scripts/build_structural_algo.py --sliced "$RUN_DIR/sliced_spec.json" --out "$OUT_FILE"
echo "[build] wrote $OUT_FILE"

echo "[step] validate structural"
FIRST_ADAPTER=$(python - <<PY
print("$ADAPTERS".split(",")[0])
PY
)
python scripts/validate_structural_algo.py --file "$OUT_FILE" --adapter "$FIRST_ADAPTER"

echo "[step] patch"
python scripts/patch_algo.py --file "$OUT_FILE" --spec "$RUN_DIR/sliced_spec.json" --out-report "$RUN_DIR/patch_report.json"
echo "[patch] wrote $RUN_DIR/patch_report.json"

echo "[step] validate llm"
set +e
python scripts/validate_algo_llm.py --file "$OUT_FILE" --spec "$RUN_DIR/sliced_spec.json" --out-report "$RUN_DIR/validate_llm_report.json" --strict
LLM_STATUS=$?
set -e
echo "[validate-llm] wrote $RUN_DIR/validate_llm_report.json"

if [[ $LLM_STATUS -ne 0 ]]; then
  echo "[step] patch (fix)"
  ISSUES=$(python - <<PY
import json
from pathlib import Path
p=Path("$RUN_DIR/validate_llm_report.json")
if not p.exists():
    print("")
    raise SystemExit(0)
data=json.loads(p.read_text())
issues=data.get("verdict", {}).get("issues", []) or []
print("\\n".join(issues))
PY
)
  python scripts/patch_algo.py --file "$OUT_FILE" --spec "$RUN_DIR/sliced_spec.json" --out-report "$RUN_DIR/patch_fix_report.json" --issues "$ISSUES"
  echo "[patch] wrote $RUN_DIR/patch_fix_report.json"
  echo "[step] validate llm (fix)"
  set +e
  python scripts/validate_algo_llm.py --file "$OUT_FILE" --spec "$RUN_DIR/sliced_spec.json" --out-report "$RUN_DIR/validate_llm_fix_report.json" --strict
  LLM_FIX_STATUS=$?
  set -e
  echo "[validate-llm] wrote $RUN_DIR/validate_llm_fix_report.json"
  # If fix validation still fails, stop before final validation
  if [[ $LLM_FIX_STATUS -ne 0 ]]; then
    echo "[error] LLM validation failed after fix pass; skipping final validation."
    echo "[step] patch (deterministic fallback)"
    python scripts/patch_deterministic.py --file "$OUT_FILE" --spec "$RUN_DIR/sliced_spec.json"
    echo "[step] validate final (fallback)"
    python scripts/validate_final.py --file "$OUT_FILE" --spec "$RUN_DIR/sliced_spec.json"
    echo "[done] deterministic fallback complete -> $OUT_FILE"
    exit 0
  fi
fi

echo "[step] validate final"
python scripts/validate_final.py --file "$OUT_FILE" --spec "$RUN_DIR/sliced_spec.json"

OPENAI_COST=$(python - <<PY
import json
import math
from pathlib import Path
cost = 0.0
for p in ["$RUN_DIR/grill_report.json", "$RUN_DIR/patch_report.json", "$RUN_DIR/patch_fix_report.json", "$RUN_DIR/validate_llm_report.json", "$RUN_DIR/validate_llm_fix_report.json"]:
    path = Path(p)
    if not path.exists():
        continue
    try:
        data = json.loads(path.read_text())
        cost += float(data.get("cost_usd", 0.0))
    except Exception:
        pass
rounded = math.ceil(cost * 100.0) / 100.0
print(f"{rounded:.2f}")
PY
)

echo "[costs][openai]=$OPENAI_COST [costs][total]=$OPENAI_COST"

echo "[done] structural build complete -> $OUT_FILE"
