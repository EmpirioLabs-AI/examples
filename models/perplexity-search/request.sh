#!/usr/bin/env bash
# Perplexity Search, cURL
# https://empiriolabs.ai/models/perplexity-search
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/search \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "perplexity-search",
    "query": "latest developments in solid-state batteries"
  }'
