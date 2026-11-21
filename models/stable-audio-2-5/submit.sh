#!/usr/bin/env bash
# Stable Audio 2.5, cURL: submit the job
# https://empiriolabs.ai/models/stable-audio-2-5
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stable-audio-2-5",
    "prompt": "Describe what you want Stable Audio 2.5 to generate."
  }'
