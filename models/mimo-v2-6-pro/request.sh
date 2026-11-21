#!/usr/bin/env bash
# MiMo V2.6 Pro, cURL
# https://empiriolabs.ai/models/mimo-v2-6-pro
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2-6-pro",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
