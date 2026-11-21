#!/usr/bin/env bash
# Seedream 4.5, cURL: submit the job
# https://empiriolabs.ai/models/seedream-4-5
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedream-4-5",
    "prompt": "Describe what you want Seedream 4.5 to generate."
  }'
