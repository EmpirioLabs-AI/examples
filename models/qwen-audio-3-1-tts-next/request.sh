#!/usr/bin/env bash
# Qwen Audio 3.1 TTS Next, cURL
# https://empiriolabs.ai/models/qwen-audio-3-1-tts-next
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-audio-3-1-tts-next",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
