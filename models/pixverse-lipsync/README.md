# Pixverse Lip Sync API examples

Aligns mouth movement in an existing video to an uploaded audio track or to text spoken by one of fourteen built-in voices.

Pixverse Lip Sync runs through `POST /v1/videos/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `pixverse-lipsync` |
| Provider | PixVerse |
| Category | Video Generation |
| Endpoint | `POST /v1/videos/generations` |

## Run

```bash
eval "$(python ../../login.py)"   # sign in, or: export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."
bash submit.sh
JOB_ID=<the job_id submit.sh returned> bash poll.sh
pip install requests && python example.py
```

## cURL: submit the job

[`submit.sh`](submit.sh)

```bash
#!/usr/bin/env bash
# Pixverse Lip Sync, cURL: submit the job
# https://empiriolabs.ai/models/pixverse-lipsync
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "pixverse-lipsync",
    "prompt": "Describe what you want Pixverse Lip Sync to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# Pixverse Lip Sync, cURL: poll for the result
# https://empiriolabs.ai/models/pixverse-lipsync
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""Pixverse Lip Sync, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/pixverse-lipsync
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/videos/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "pixverse-lipsync",
        "prompt": "Describe what you want Pixverse Lip Sync to generate.",
    },
)
job = response.json()

# Generation runs as an async job. Poll until it completes.
import time
while True:
    status = requests.get(
        f"https://api.empiriolabs.ai/v1/jobs/{job['job_id']}",
        headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    ).json()
    if status.get("status") in ("completed", "failed"):
        print(status)
        break
    time.sleep(5)
```

## Links

- [Pixverse Lip Sync pricing and specs](https://empiriolabs.ai/models/pixverse-lipsync)
- [Pixverse Lip Sync API reference](https://docs.empiriolabs.ai/models/pixverse-lipsync)
- [Try Pixverse Lip Sync in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=pixverse-lipsync)

[All EmpirioLabs AI examples](../../README.md)
