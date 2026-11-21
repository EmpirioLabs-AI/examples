#!/usr/bin/env bash
# Seedance 2.0 Fast, cURL: submit the job
# https://empiriolabs.ai/models/seedance-2-0-fast
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2-0-fast",
    "prompt": "Describe what you want Seedance 2.0 Fast to generate."
  }'
