#!/usr/bin/env bash
set -euo pipefail

MODEL="${ANTHROPIC_MODEL:-claude-3-haiku-20240307}"
MAX_TOKENS="${ANTHROPIC_MAX_TOKENS:-4096}"
PROMPT_FILE="${1:-prompts/crazy_ideas_prompt.txt}"
TMP_JSON="$(mktemp)"
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
    \"max_tokens\": $MAX_TOKENS,
    \"messages\": [
      {\"role\": \"user\", \"content\": $ESCAPED_PROMPT}
    ]
  }"
)

if [[ "$HTTP_CODE" != "200" ]]; then
  echo "❌ Claude HTTP $HTTP_CODE" >&2
  cat "$TMP_JSON" >&2
  if [[ -n "$RESPONSE_DIR" ]]; then
    mkdir -p "$RESPONSE_DIR"
    cp "$TMP_JSON" "$RESPONSE_DIR/claude_response.json"
    echo "$HTTP_CODE" > "$RESPONSE_DIR/claude_http_code.txt"
  fi
  rm -f "$TMP_JSON"
  exit 1
fi

if ! python3 scripts/json_array_to_jsonl.py "$TMP_JSON" "$MODEL" "anthropic" 15; then
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
