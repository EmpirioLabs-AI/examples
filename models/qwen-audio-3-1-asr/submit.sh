#!/usr/bin/env bash
# Qwen Audio 3.1 ASR, cURL: submit the job
# https://empiriolabs.ai/models/qwen-audio-3-1-asr
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-audio-3-1-asr",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
