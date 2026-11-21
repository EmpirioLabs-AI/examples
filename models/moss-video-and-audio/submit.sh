#!/usr/bin/env bash
# MOSS Video and Audio, cURL: submit the job
# https://empiriolabs.ai/models/moss-video-and-audio
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moss-video-and-audio",
    "prompt": "Describe what you want MOSS Video and Audio to generate."
  }'
