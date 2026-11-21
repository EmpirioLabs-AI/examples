#!/usr/bin/env bash
# TRELLIS.2 4B, cURL: submit the job
# https://empiriolabs.ai/models/trellis-2-4b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "trellis-2-4b",
    "prompt": "Describe what you want TRELLIS.2 4B to generate."
  }'
