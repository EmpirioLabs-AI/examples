#!/usr/bin/env bash
# Sonilo Video to Video, cURL: submit the job
# https://empiriolabs.ai/models/sonilo-video-to-video
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonilo-video-to-video",
    "prompt": "Describe what you want Sonilo Video to Video to generate."
  }'
