#!/usr/bin/env bash
# Tavily Research, cURL
# https://empiriolabs.ai/models/tavily-research
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/research \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tavily-research",
    "prompt": "Your input here."
  }'
