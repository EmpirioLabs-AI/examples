#!/usr/bin/env bash
# Sonilo Audio Ducking, cURL: submit the job
# https://empiriolabs.ai/models/sonilo-audio-ducking
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonilo-audio-ducking",
    "prompt": "Describe what you want Sonilo Audio Ducking to generate."
  }'
