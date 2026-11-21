#!/usr/bin/env bash
# Wan2.7 Image, cURL: submit the job
# https://empiriolabs.ai/models/wan2-7-image
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "wan2-7-image",
    "prompt": "Describe what you want Wan2.7 Image to generate."
  }'
