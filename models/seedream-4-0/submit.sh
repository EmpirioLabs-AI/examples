#!/usr/bin/env bash
# Seedream 4.0, cURL: submit the job
# https://empiriolabs.ai/models/seedream-4-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedream-4-0",
    "prompt": "Describe what you want Seedream 4.0 to generate."
  }'
