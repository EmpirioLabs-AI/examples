#!/usr/bin/env bash
# Seed Voice Replication 2.0, cURL: submit the job
# https://empiriolabs.ai/models/seed-voice-replication-2-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seed-voice-replication-2-0",
    "prompt": "Describe what you want Seed Voice Replication 2.0 to generate."
  }'
