#!/usr/bin/env bash
set -euo pipefail

MODEL="${OPENAI_MODEL:-gpt-4.1-mini}"
PROMPT_FILE="${1:-prompts/crazy_ideas_prompt.txt}"
TMP_JSON="$(mktemp)"
ERROR_DIR="${ERROR_DIR:-}"
RESPONSE_DIR="${RESPONSE_DIR:-}"

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "❌ Prompt file not found: $PROMPT_FILE" >&2
  exit 1
fi

PROMPT="$(cat "$PROMPT_FILE")"

REQUEST_JSON=$(jq -n \
  --arg model "$MODEL" \
  --arg prompt "$PROMPT" \
  '{
    model: $model,
    temperature: 0.7,
    messages: [{ role: "user", content: $prompt }]
  }'
)

HTTP_CODE=$(curl -sS -w "%{http_code}" \
  -o "$TMP_JSON" \
  https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer ${OPENAI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$REQUEST_JSON"
)

if [[ "$HTTP_CODE" != "200" ]]; then
  echo "❌ OpenAI HTTP $HTTP_CODE" >&2
  cat "$TMP_JSON" >&2
  if [[ -n "$ERROR_DIR" ]]; then
    mkdir -p "$ERROR_DIR"
    cp "$TMP_JSON" "$ERROR_DIR/chatgpt_response.json"
    echo "$HTTP_CODE" > "$ERROR_DIR/chatgpt_http_code.txt"
  fi
  if [[ -n "$RESPONSE_DIR" ]]; then
    mkdir -p "$RESPONSE_DIR"
    cp "$TMP_JSON" "$RESPONSE_DIR/chatgpt_response.json"
    echo "$HTTP_CODE" > "$RESPONSE_DIR/chatgpt_http_code.txt"
  fi
  rm -f "$TMP_JSON"
  exit 1
fi

if ! python3 - <<'PY' "$TMP_JSON" "$MODEL"; then
import json
import sys

src = sys.argv[1]
model = sys.argv[2]

with open(src) as f:
    raw = f.read().strip()

obj = json.loads(raw)
content = obj["choices"][0]["message"]["content"]
ideas = json.loads(content)

for item in ideas:
    if not isinstance(item, dict):
        continue
    item["source_provider"] = "openai"
    item["source_model"] = model
    print(json.dumps(item, ensure_ascii=False))
PY
  if [[ -n "$ERROR_DIR" ]]; then
    mkdir -p "$ERROR_DIR"
    cp "$TMP_JSON" "$ERROR_DIR/chatgpt_response.json"
    echo "$HTTP_CODE" > "$ERROR_DIR/chatgpt_http_code.txt"
  fi
  if [[ -n "$RESPONSE_DIR" ]]; then
    mkdir -p "$RESPONSE_DIR"
    cp "$TMP_JSON" "$RESPONSE_DIR/chatgpt_response.json"
    echo "$HTTP_CODE" > "$RESPONSE_DIR/chatgpt_http_code.txt"
  fi
  rm -f "$TMP_JSON"
  exit 1
fi

if [[ -n "$RESPONSE_DIR" ]]; then
  mkdir -p "$RESPONSE_DIR"
  cp "$TMP_JSON" "$RESPONSE_DIR/chatgpt_response.json"
  echo "$HTTP_CODE" > "$RESPONSE_DIR/chatgpt_http_code.txt"
fi

rm -f "$TMP_JSON"
