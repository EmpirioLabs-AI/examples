#!/usr/bin/env bash
# Seed ASR 2.0, cURL: submit the job
# https://empiriolabs.ai/models/seed-asr-2-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seed-asr-2-0",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
