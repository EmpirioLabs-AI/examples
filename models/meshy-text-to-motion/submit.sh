#!/usr/bin/env bash
# Meshy Text to Motion, cURL: submit the job
# https://empiriolabs.ai/models/meshy-text-to-motion
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meshy-text-to-motion",
    "prompt": "Describe what you want Meshy Text to Motion to generate."
  }'
