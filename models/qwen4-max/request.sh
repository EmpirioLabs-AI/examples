#!/usr/bin/env bash
# Qwen4 Max, cURL
# https://empiriolabs.ai/models/qwen4-max
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen4-max",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
