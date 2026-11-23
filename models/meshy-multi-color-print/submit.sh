#!/usr/bin/env bash
# Meshy Multi-Color Print, cURL: submit the job
# https://empiriolabs.ai/models/meshy-multi-color-print
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meshy-multi-color-print",
    "prompt": "Describe what you want Meshy Multi-Color Print to generate."
  }'
