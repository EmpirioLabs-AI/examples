#!/usr/bin/env bash
# Perplexity Advanced Deep Research, cURL
# https://empiriolabs.ai/models/perplexity-advanced-deep-research
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "perplexity-advanced-deep-research",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
