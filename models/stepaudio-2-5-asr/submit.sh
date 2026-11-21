#!/usr/bin/env bash
# StepAudio 2.5 ASR, cURL: submit the job
# https://empiriolabs.ai/models/stepaudio-2-5-asr
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-2-5-asr",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
