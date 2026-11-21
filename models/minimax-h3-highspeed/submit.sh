#!/usr/bin/env bash
# MiniMax H3 Highspeed, cURL: submit the job
# https://empiriolabs.ai/models/minimax-h3-highspeed
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-h3-highspeed",
    "prompt": "Describe what you want MiniMax H3 Highspeed to generate."
  }'
