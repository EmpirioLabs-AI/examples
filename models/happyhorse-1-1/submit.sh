#!/usr/bin/env bash
# HappyHorse 1.1, cURL: submit the job
# https://empiriolabs.ai/models/happyhorse-1-1
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "happyhorse-1-1",
    "prompt": "Describe what you want HappyHorse 1.1 to generate."
  }'
