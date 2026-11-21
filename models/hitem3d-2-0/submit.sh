#!/usr/bin/env bash
# Hitem3D 2.0, cURL: submit the job
# https://empiriolabs.ai/models/hitem3d-2-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "hitem3d-2-0",
    "prompt": "Describe what you want Hitem3D 2.0 to generate."
  }'
