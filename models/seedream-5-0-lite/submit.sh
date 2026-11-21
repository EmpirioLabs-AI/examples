#!/usr/bin/env bash
# Seedream 5.0 Lite, cURL: submit the job
# https://empiriolabs.ai/models/seedream-5-0-lite
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedream-5-0-lite",
    "prompt": "Describe what you want Seedream 5.0 Lite to generate."
  }'
