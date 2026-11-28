#!/usr/bin/env bash
# Seed Audio 1.0, cURL: submit the job
# https://empiriolabs.ai/models/seed-audio-1-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seed-audio-1-0",
    "prompt": "Describe what you want Seed Audio 1.0 to generate."
  }'
