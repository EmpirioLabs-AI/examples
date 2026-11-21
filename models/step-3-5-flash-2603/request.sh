#!/usr/bin/env bash
# Step 3.5 Flash 2603, cURL
# https://empiriolabs.ai/models/step-3-5-flash-2603
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "step-3-5-flash-2603",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
