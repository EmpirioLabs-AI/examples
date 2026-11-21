#!/usr/bin/env bash
# PixVerse V6 Max, cURL: submit the job
# https://empiriolabs.ai/models/pixverse-v6-max
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "pixverse-v6-max",
    "prompt": "Describe what you want PixVerse V6 Max to generate."
  }'
