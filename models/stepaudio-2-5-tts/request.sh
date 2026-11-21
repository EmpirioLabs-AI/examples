#!/usr/bin/env bash
# StepAudio 2.5 TTS, cURL
# https://empiriolabs.ai/models/stepaudio-2-5-tts
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-2-5-tts",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
