#!/usr/bin/env bash
# Seed 2.0 Pro, cURL
# https://empiriolabs.ai/models/seed-2-0-pro
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seed-2-0-pro",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
