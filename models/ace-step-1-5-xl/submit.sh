#!/usr/bin/env bash
# ACE-Step 1.5 XL, cURL: submit the job
# https://empiriolabs.ai/models/ace-step-1-5-xl
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ace-step-1-5-xl",
    "prompt": "Describe what you want ACE-Step 1.5 XL to generate."
  }'
