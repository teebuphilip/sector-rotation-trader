#!/usr/bin/env bash
set -euo pipefail

MODEL="${ANTHROPIC_MODEL:-claude-3-haiku-20240307}"
PROMPT_FILE="${1:-prompts/normal_ideas_prompt.txt}"

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "❌ Prompt file not found: $PROMPT_FILE" >&2
  exit 1
fi

PROMPT="$(cat "$PROMPT_FILE")"
ESCAPED_PROMPT="$(jq -Rs . <<<"$PROMPT")"

RESPONSE="$(curl -sS https://api.anthropic.com/v1/messages \
  -H "x-api-key: ${ANTHROPIC_API_KEY:?ANTHROPIC_API_KEY not set}" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d "{
    \"model\": \"$MODEL\",
    \"max_tokens\": 2000,
    \"messages\": [
      {\"role\": \"user\", \"content\": $ESCAPED_PROMPT}
    ]
  }"
)"

echo "$RESPONSE" | python3 - <<'PY' "$MODEL"
import json
import sys

model = sys.argv[1]
raw = sys.stdin.read().strip()
if not raw:
    raise SystemExit("Empty Claude response")

obj = json.loads(raw)
text = obj["content"][0]["text"]
ideas = json.loads(text)
if isinstance(ideas, dict):
    if isinstance(ideas.get("ideas"), list):
        ideas = ideas["ideas"]
    else:
        ideas = [ideas]

if not isinstance(ideas, list) or len(ideas) == 0:
    raise SystemExit("Expected a non-empty JSON list for ideas")

for item in ideas:
    if not isinstance(item, dict):
        continue
    item["source_provider"] = "anthropic"
    item["source_model"] = model
    print(json.dumps(item, ensure_ascii=False))
PY

# Log cost
python3 - <<'PY' "$RESPONSE" "$MODEL"
import json
import os
from datetime import datetime
from pathlib import Path
import sys

raw = sys.argv[1]
model = sys.argv[2]

log_path = Path("logs") / "ai_costs_claude_normal.csv"
new_file = not log_path.exists()

try:
    data = json.loads(raw)
except Exception:
    sys.exit(0)

usage = data.get("usage", {})
in_tokens = usage.get("input_tokens", 0) or 0
out_tokens = usage.get("output_tokens", 0) or 0
in_rate = float(os.getenv("ANTHROPIC_INPUT_PER_MTOK", "3.00"))
out_rate = float(os.getenv("ANTHROPIC_OUTPUT_PER_MTOK", "15.00"))
total = (in_tokens * in_rate + out_tokens * out_rate) / 1_000_000

now = datetime.utcnow()
with log_path.open("a", newline="") as f:
    if new_file:
        f.write("date,time,provider,model,input_tokens,output_tokens,cost_usd\n")
    f.write(
        f"{now.strftime('%Y-%m-%d')},"
        f"{now.strftime('%H:%M:%S')},"
        f"anthropic,{model},{in_tokens},{out_tokens},{total:.6f}\n"
    )
PY
