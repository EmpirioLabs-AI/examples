#!/usr/bin/env bash
# Meshy 7.1, cURL: submit the job
# https://empiriolabs.ai/models/meshy-7-1
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meshy-7-1",
    "prompt": "Describe what you want Meshy 7.1 to generate."
  }'
