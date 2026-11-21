# Seedream 5.0 Lite API examples

Unified multimodal image model that reasons through prompts before rendering, producing high-resolution and consistent edits and brand visuals.

Seedream 5.0 Lite runs through `POST /v1/images/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result. Or add `"sync": true` to skip polling: the request stays open and returns the finished OpenAI-style image response directly, so OpenAI SDKs work as-is.

| | |
| --- | --- |
| Model id | `seedream-5-0-lite` |
| Provider | ByteDance |
| Category | Image Generation |
| Endpoint | `POST /v1/images/generations` |

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
# Seedream 5.0 Lite, cURL: submit the job
# https://empiriolabs.ai/models/seedream-5-0-lite
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedream-5-0-lite",
    "prompt": "Describe what you want Seedream 5.0 Lite to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# Seedream 5.0 Lite, cURL: poll for the result
# https://empiriolabs.ai/models/seedream-5-0-lite
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""Seedream 5.0 Lite, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/seedream-5-0-lite
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/images/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "seedream-5-0-lite",
        "prompt": "Describe what you want Seedream 5.0 Lite to generate.",
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

- [Seedream 5.0 Lite pricing and specs](https://empiriolabs.ai/models/seedream-5-0-lite)
- [Seedream 5.0 Lite API reference](https://docs.empiriolabs.ai/models/seedream-5-0-lite)
- [Try Seedream 5.0 Lite in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=seedream-5-0-lite)
