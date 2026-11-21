#!/usr/bin/env bash
# Tavily Search, cURL
# https://empiriolabs.ai/models/tavily-search
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/search \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tavily-search",
    "query": "latest developments in solid-state batteries"
  }'
