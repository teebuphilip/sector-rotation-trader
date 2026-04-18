#!/usr/bin/env bash
set -euo pipefail

MODEL="${OPENAI_MODEL:-gpt-4.1-mini}"
MAX_TOKENS="${OPENAI_MAX_TOKENS:-6000}"
PROMPT_FILE="${1:-prompts/crazy_ideas_prompt.txt}"
TMP_JSON="$(mktemp)"
RESPONSE_DIR="${RESPONSE_DIR:-}"

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "❌ Prompt file not found: $PROMPT_FILE" >&2
  exit 1
fi

PROMPT="$(cat "$PROMPT_FILE")"

REQUEST_JSON=$(jq -n \
  --arg model "$MODEL" \
  --arg prompt "$PROMPT" \
  --arg max_tokens "$MAX_TOKENS" \
  '{
    model: $model,
    max_tokens: ($max_tokens | tonumber),
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
  if [[ -n "$RESPONSE_DIR" ]]; then
    mkdir -p "$RESPONSE_DIR"
    cp "$TMP_JSON" "$RESPONSE_DIR/chatgpt_response.json"
    echo "$HTTP_CODE" > "$RESPONSE_DIR/chatgpt_http_code.txt"
  fi
  rm -f "$TMP_JSON"
  exit 1
fi

if ! python3 scripts/json_array_to_jsonl.py "$TMP_JSON" "$MODEL" "openai" 15; then
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
