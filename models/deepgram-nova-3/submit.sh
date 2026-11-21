#!/usr/bin/env bash
# Deepgram Nova-3, cURL: submit the job
# https://empiriolabs.ai/models/deepgram-nova-3
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepgram-nova-3",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
