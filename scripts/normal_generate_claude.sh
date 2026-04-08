#!/usr/bin/env bash
set -euo pipefail

MODEL="${ANTHROPIC_MODEL:-claude-3-haiku-20240307}"
PROMPT_FILE="${1:-prompts/normal_ideas_prompt.txt}"
TMP_JSON="$(mktemp)"
ERROR_DIR="${ERROR_DIR:-}"
RESPONSE_DIR="${RESPONSE_DIR:-}"

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "❌ Prompt file not found: $PROMPT_FILE" >&2
  exit 1
fi

PROMPT="$(cat "$PROMPT_FILE")"
ESCAPED_PROMPT="$(jq -Rs . <<<"$PROMPT")"

HTTP_CODE=$(curl -sS -w "%{http_code}" \
  -o "$TMP_JSON" \
  https://api.anthropic.com/v1/messages \
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
)

if [[ "$HTTP_CODE" != "200" ]]; then
  echo "❌ Claude HTTP $HTTP_CODE" >&2
  cat "$TMP_JSON" >&2
  if [[ -n "$ERROR_DIR" ]]; then
    mkdir -p "$ERROR_DIR"
    cp "$TMP_JSON" "$ERROR_DIR/claude_response.json"
    echo "$HTTP_CODE" > "$ERROR_DIR/claude_http_code.txt"
  fi
  if [[ -n "$RESPONSE_DIR" ]]; then
    mkdir -p "$RESPONSE_DIR"
    cp "$TMP_JSON" "$RESPONSE_DIR/claude_response.json"
    echo "$HTTP_CODE" > "$RESPONSE_DIR/claude_http_code.txt"
  fi
  rm -f "$TMP_JSON"
  exit 1
fi

if ! python3 - <<'PY' "$TMP_JSON" "$MODEL"; then
import json
import sys

src = sys.argv[1]
model = sys.argv[2]
raw = open(src).read().strip()
if not raw:
    raise SystemExit("Empty Claude response")

obj = json.loads(raw)
if isinstance(obj, dict) and "error" in obj:
    raise SystemExit(f"Claude API error: {obj['error']}")
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
  if [[ -n "$ERROR_DIR" ]]; then
    mkdir -p "$ERROR_DIR"
    cp "$TMP_JSON" "$ERROR_DIR/claude_response.json"
    echo "$HTTP_CODE" > "$ERROR_DIR/claude_http_code.txt"
  fi
  if [[ -n "$RESPONSE_DIR" ]]; then
    mkdir -p "$RESPONSE_DIR"
    cp "$TMP_JSON" "$RESPONSE_DIR/claude_response.json"
    echo "$HTTP_CODE" > "$RESPONSE_DIR/claude_http_code.txt"
  fi
  rm -f "$TMP_JSON"
  exit 1
fi

# Save response even on success
if [[ -n "$RESPONSE_DIR" ]]; then
  mkdir -p "$RESPONSE_DIR"
  cp "$TMP_JSON" "$RESPONSE_DIR/claude_response.json"
  echo "$HTTP_CODE" > "$RESPONSE_DIR/claude_http_code.txt"
fi

# Log cost
python3 - <<'PY' "$TMP_JSON" "$MODEL"
import json
import os
from datetime import datetime
from pathlib import Path
import sys

raw = Path(sys.argv[1]).read_text()
model = sys.argv[2]

log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)
log_path = log_dir / "ai_costs_claude_normal.csv"
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

rm -f "$TMP_JSON"
