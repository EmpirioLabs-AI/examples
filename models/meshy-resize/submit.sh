#!/usr/bin/env bash
# Meshy Resize, cURL: submit the job
# https://empiriolabs.ai/models/meshy-resize
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meshy-resize",
    "prompt": "Describe what you want Meshy Resize to generate."
  }'
