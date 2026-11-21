#!/usr/bin/env bash
# GLM 4.7 Flash, cURL
# https://empiriolabs.ai/models/glm-4-7-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-4-7-flash",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
