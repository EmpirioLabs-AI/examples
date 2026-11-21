#!/usr/bin/env bash
# Aplomb 1, cURL
# https://empiriolabs.ai/models/aplomb-1
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/decisions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "aplomb-1",
    "state": "I was charged twice for my subscription this month. Please refund the duplicate charge today.",
    "questions": {
      "is_urgent": {"type": "noul", "instructions": "Does the customer need a resolution today?"},
      "department": {
        "type": "choice",
        "instructions": "Which team should handle this message?",
        "criteria": {"billing": null, "technical": null, "sales": null}
      }
    }
  }'
