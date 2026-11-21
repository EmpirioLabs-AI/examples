# Seedance 2.5 Flash API examples

Faster, lower-cost Seedance 2.5 for coherent clips up to 30 seconds at 480p or 720p, with image, video, and audio references, native audio, editing, and extension.

Seedance 2.5 Flash runs through `POST /v1/videos/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `seedance-2-5-flash` |
| Provider | ByteDance |
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
# Seedance 2.5 Flash, cURL: submit the job
# https://empiriolabs.ai/models/seedance-2-5-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2-5-flash",
    "prompt": "Describe what you want Seedance 2.5 Flash to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# Seedance 2.5 Flash, cURL: poll for the result
# https://empiriolabs.ai/models/seedance-2-5-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""Seedance 2.5 Flash, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/seedance-2-5-flash
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/videos/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "seedance-2-5-flash",
        "prompt": "Describe what you want Seedance 2.5 Flash to generate.",
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

- [Seedance 2.5 Flash pricing and specs](https://empiriolabs.ai/models/seedance-2-5-flash)
- [Seedance 2.5 Flash API reference](https://docs.empiriolabs.ai/models/seedance-2-5-flash)
- [Try Seedance 2.5 Flash in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=seedance-2-5-flash)

[All EmpirioLabs AI examples](../../README.md)
