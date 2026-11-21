#!/usr/bin/env bash
# StepAudio 3 ASR Max, cURL: submit the job
# https://empiriolabs.ai/models/stepaudio-3-asr-max
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-3-asr-max",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
