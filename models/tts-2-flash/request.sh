#!/usr/bin/env bash
# TTS 2 Flash, cURL
# https://empiriolabs.ai/models/tts-2-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-2-flash",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
