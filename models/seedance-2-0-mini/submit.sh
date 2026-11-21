#!/usr/bin/env bash
# Seedance 2.0 Mini, cURL: submit the job
# https://empiriolabs.ai/models/seedance-2-0-mini
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2-0-mini",
    "prompt": "Describe what you want Seedance 2.0 Mini to generate."
  }'
