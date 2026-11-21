#!/usr/bin/env bash
# Wan2.2 Image, cURL: submit the job
# https://empiriolabs.ai/models/wan2-2-image
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "wan2-2-image",
    "prompt": "Describe what you want Wan2.2 Image to generate."
  }'
