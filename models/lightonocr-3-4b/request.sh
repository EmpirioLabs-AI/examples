#!/usr/bin/env bash
# LightOnOCR-3 4B, cURL
# https://empiriolabs.ai/models/lightonocr-3-4b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/ocr \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lightonocr-3-4b",
    "document": {
      "type": "document_url",
      "document_url": "https://arxiv.org/pdf/2412.13663"
    },
    "pages": [0, 1],
    "include_image_base64": false
  }'
