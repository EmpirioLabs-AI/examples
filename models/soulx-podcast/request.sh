#!/usr/bin/env bash
# SoulX Podcast, cURL
# https://empiriolabs.ai/models/soulx-podcast
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "soulx-podcast",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
