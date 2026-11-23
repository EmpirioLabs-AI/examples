#!/usr/bin/env bash
# Meshy 6, cURL: poll for the result
# https://empiriolabs.ai/models/meshy-6
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
