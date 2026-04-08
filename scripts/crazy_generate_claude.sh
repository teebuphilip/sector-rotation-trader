#!/usr/bin/env bash
set -euo pipefail

MODEL="${ANTHROPIC_MODEL:-claude-3-haiku-20240307}"
PROMPT_FILE="${1:-prompts/crazy_ideas_prompt.txt}"

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
obj = json.loads(raw)
text = obj["content"][0]["text"]
ideas = json.loads(text)

for item in ideas:
    if not isinstance(item, dict):
        continue
    item["source_provider"] = "anthropic"
    item["source_model"] = model
    print(json.dumps(item, ensure_ascii=False))
PY
