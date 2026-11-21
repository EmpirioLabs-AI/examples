#!/usr/bin/env bash
# Pixverse Avatar, cURL: submit the job
# https://empiriolabs.ai/models/pixverse-avatar
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "pixverse-avatar",
    "prompt": "Describe what you want Pixverse Avatar to generate."
  }'
