#!/usr/bin/env bash
# Fugu Ultra v2.0, cURL
# https://empiriolabs.ai/models/fugu-ultra-v2-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "fugu-ultra-v2-0",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
