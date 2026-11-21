#!/usr/bin/env bash
# Hunyuan Video 1.5, cURL: submit the job
# https://empiriolabs.ai/models/hunyuan-video-1-5
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "hunyuan-video-1-5",
    "prompt": "Describe what you want Hunyuan Video 1.5 to generate."
  }'
