#!/usr/bin/env bash
# SVI 2.0 Pro, cURL: submit the job
# https://empiriolabs.ai/models/svi-2-0-pro
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "svi-2-0-pro",
    "prompt": "Describe what you want SVI 2.0 Pro to generate."
  }'
