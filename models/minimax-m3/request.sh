#!/usr/bin/env bash
# MiniMax M3, cURL
# https://empiriolabs.ai/models/minimax-m3
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-m3",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
