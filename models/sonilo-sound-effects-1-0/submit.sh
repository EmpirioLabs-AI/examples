#!/usr/bin/env bash
# Sonilo Sound Effects 1.0, cURL: submit the job
# https://empiriolabs.ai/models/sonilo-sound-effects-1-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonilo-sound-effects-1-0",
    "prompt": "Describe what you want Sonilo Sound Effects 1.0 to generate."
  }'
