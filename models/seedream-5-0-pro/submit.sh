#!/usr/bin/env bash
# Seedream 5.0 Pro, cURL: submit the job
# https://empiriolabs.ai/models/seedream-5-0-pro
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedream-5-0-pro",
    "prompt": "Describe what you want Seedream 5.0 Pro to generate."
  }'
