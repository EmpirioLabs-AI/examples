#!/usr/bin/env bash
# Qwen3.5 35B-A3B, cURL
# https://empiriolabs.ai/models/qwen3-5-35b-a3b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-5-35b-a3b",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
