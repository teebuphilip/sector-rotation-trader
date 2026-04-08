#!/usr/bin/env bash
set -euo pipefail

MODEL="${ANTHROPIC_MODEL:-claude-3-haiku-20240307}"
PROMPT_FILE="${1:-prompts/crazy_ideas_prompt.txt}"
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

if [[ -n "$RESPONSE_DIR" ]]; then
  mkdir -p "$RESPONSE_DIR"
  cp "$TMP_JSON" "$RESPONSE_DIR/claude_response.json"
  echo "$HTTP_CODE" > "$RESPONSE_DIR/claude_http_code.txt"
fi

rm -f "$TMP_JSON"
