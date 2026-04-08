#!/usr/bin/env bash
set -euo pipefail

MODEL="${OPENAI_MODEL:-gpt-4.1-mini}"
PROMPT_FILE="${1:-prompts/crazy_ideas_prompt.txt}"
TMP_JSON="$(mktemp)"

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
  rm -f "$TMP_JSON"
  exit 1
fi

python3 - <<'PY' "$TMP_JSON" "$MODEL"
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

rm -f "$TMP_JSON"
