#!/usr/bin/env bash
# Skylark Embedding Vision, cURL
# https://empiriolabs.ai/models/skylark-embedding-vision
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/embeddings \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "skylark-embedding-vision",
    "input": "The quick brown fox jumps over the lazy dog."
  }'
