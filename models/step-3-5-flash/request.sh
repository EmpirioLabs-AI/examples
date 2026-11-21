#!/usr/bin/env bash
# Step 3.5 Flash, cURL
# https://empiriolabs.ai/models/step-3-5-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "step-3-5-flash",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
