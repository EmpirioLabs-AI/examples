#!/usr/bin/env bash
# Text Embedding v4, cURL
# https://empiriolabs.ai/models/text-embedding-v4
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/embeddings \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-v4",
    "input": "The quick brown fox jumps over the lazy dog."
  }'
