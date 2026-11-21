#!/usr/bin/env bash
# MiniMax Music 3, cURL: submit the job
# https://empiriolabs.ai/models/minimax-music-3
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-music-3",
    "prompt": "Describe what you want MiniMax Music 3 to generate."
  }'
