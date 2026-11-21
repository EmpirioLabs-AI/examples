#!/usr/bin/env bash
# Grok Imagine Video 1.5, cURL: submit the job
# https://empiriolabs.ai/models/grok-imagine-video-1-5
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "grok-imagine-video-1-5",
    "prompt": "Describe what you want Grok Imagine Video 1.5 to generate."
  }'
