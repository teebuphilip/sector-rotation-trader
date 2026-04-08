#!/usr/bin/env bash
set -euo pipefail

MODEL="${OPENAI_MODEL:-gpt-4.1-mini}"
PROMPT_FILE="${1:-prompts/normal_ideas_prompt.txt}"
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
    temperature: 0.5,
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

# Log cost
python3 - <<'PY' "$TMP_JSON" "$MODEL"
import json
import os
from datetime import datetime
from pathlib import Path
import sys

src = sys.argv[1]
model = sys.argv[2]

log_path = Path("logs") / "ai_costs_chatgpt_normal.csv"
new_file = not log_path.exists()

try:
    data = json.loads(Path(src).read_text())
except Exception:
    sys.exit(0)

usage = data.get("usage", {})
in_tokens = usage.get("prompt_tokens", 0) or 0
out_tokens = usage.get("completion_tokens", 0) or 0
in_rate = float(os.getenv("OPENAI_INPUT_PER_MTOK", "2.50"))
out_rate = float(os.getenv("OPENAI_OUTPUT_PER_MTOK", "10.00"))
total = (in_tokens * in_rate + out_tokens * out_rate) / 1_000_000

now = datetime.utcnow()
with log_path.open("a", newline="") as f:
    if new_file:
        f.write("date,time,provider,model,input_tokens,output_tokens,cost_usd\n")
    f.write(
        f"{now.strftime('%Y-%m-%d')},"
        f"{now.strftime('%H:%M:%S')},"
        f"openai,{model},{in_tokens},{out_tokens},{total:.6f}\n"
    )
PY

rm -f "$TMP_JSON"
