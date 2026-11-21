#!/usr/bin/env bash
# StepAudio 3 Gen, cURL: submit the job
# https://empiriolabs.ai/models/stepaudio-3-gen
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-3-gen",
    "prompt": "Describe what you want StepAudio 3 Gen to generate."
  }'
