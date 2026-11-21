#!/usr/bin/env bash
# MOSS-Image Turbo, cURL: submit the job
# https://empiriolabs.ai/models/moss-image-turbo
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moss-image-turbo",
    "prompt": "Describe what you want MOSS-Image Turbo to generate."
  }'
