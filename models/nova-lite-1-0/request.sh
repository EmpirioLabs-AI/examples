#!/usr/bin/env bash
# Nova Lite 1.0, cURL
# https://empiriolabs.ai/models/nova-lite-1-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nova-lite-1-0",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
