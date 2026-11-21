#!/usr/bin/env bash
# FLUX.2 Klein 4B, cURL: submit the job
# https://empiriolabs.ai/models/flux-2-klein-4b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "flux-2-klein-4b",
    "prompt": "Describe what you want FLUX.2 Klein 4B to generate."
  }'
