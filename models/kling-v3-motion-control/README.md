# Kling v3 Motion Control API examples

Kling 3.0 model that transfers motion from a reference video onto a character from a reference image, with Standard 720p and Pro 1080p tiers.

Kling v3 Motion Control runs through `POST /v1/videos/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `kling-v3-motion-control` |
| Provider | Kling AI |
| Category | Video Generation |
| Endpoint | `POST /v1/videos/generations` |

## Run

```bash
export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."   # https://platform.empiriolabs.ai/dashboard/api-keys
bash submit.sh
JOB_ID=<the job_id submit.sh returned> bash poll.sh
pip install requests && python example.py
```

## cURL: submit the job

[`submit.sh`](submit.sh)

```bash
#!/usr/bin/env bash
# Kling v3 Motion Control, cURL: submit the job
# https://empiriolabs.ai/models/kling-v3-motion-control
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kling-v3-motion-control",
    "prompt": "Describe what you want Kling v3 Motion Control to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# Kling v3 Motion Control, cURL: poll for the result
# https://empiriolabs.ai/models/kling-v3-motion-control
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""Kling v3 Motion Control, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/kling-v3-motion-control
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/videos/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "kling-v3-motion-control",
        "prompt": "Describe what you want Kling v3 Motion Control to generate.",
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

- [Kling v3 Motion Control pricing and specs](https://empiriolabs.ai/models/kling-v3-motion-control)
- [Kling v3 Motion Control API reference](https://docs.empiriolabs.ai/models/kling-v3-motion-control)
- [Try Kling v3 Motion Control in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=kling-v3-motion-control)

[All EmpirioLabs AI examples](../../README.md)
