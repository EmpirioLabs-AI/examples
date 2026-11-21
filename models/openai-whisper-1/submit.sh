#!/usr/bin/env bash
# OpenAI Whisper 1, cURL: submit the job
# https://empiriolabs.ai/models/openai-whisper-1
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai-whisper-1",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
