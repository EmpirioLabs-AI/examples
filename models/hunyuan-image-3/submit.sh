#!/usr/bin/env bash
# Hunyuan Image 3, cURL: submit the job
# https://empiriolabs.ai/models/hunyuan-image-3
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "hunyuan-image-3",
    "prompt": "Describe what you want Hunyuan Image 3 to generate."
  }'
