#!/usr/bin/env bash
# Kling v3 Motion Control, cURL: submit the job
# https://empiriolabs.ai/models/kling-v3-motion-control
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v3-motion-control",
    "prompt": "Describe what you want Kling v3 Motion Control to generate."
  }'
