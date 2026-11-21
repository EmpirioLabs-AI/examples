#!/usr/bin/env bash
# Kimi K2.6, cURL
# https://empiriolabs.ai/models/kimi-k2-6
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k2-6",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
