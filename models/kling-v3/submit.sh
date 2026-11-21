#!/usr/bin/env bash
# Kling V3, cURL: submit the job
# https://empiriolabs.ai/models/kling-v3
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v3",
    "prompt": "Describe what you want Kling V3 to generate."
  }'
