#!/usr/bin/env bash
# Meshy Rigging, cURL: submit the job
# https://empiriolabs.ai/models/meshy-rigging
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meshy-rigging",
    "prompt": "Describe what you want Meshy Rigging to generate."
  }'
