#!/usr/bin/env bash
# Seed TTS 3.0, cURL
# https://empiriolabs.ai/models/seed-tts-3-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seed-tts-3-0",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
