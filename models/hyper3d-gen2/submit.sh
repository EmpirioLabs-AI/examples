#!/usr/bin/env bash
# Hyper3D Gen2, cURL: submit the job
# https://empiriolabs.ai/models/hyper3d-gen2
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "hyper3d-gen2",
    "prompt": "Describe what you want Hyper3D Gen2 to generate."
  }'
