# FLUX.2 Klein 4B API examples

Apache-licensed 4B FLUX.2 Klein image generation and editing model with text-to-image, reference-image editing, and creative workflow support.

FLUX.2 Klein 4B runs through `POST /v1/images/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result. Or add `"sync": true` to skip polling: the request stays open and returns the finished OpenAI-style image response directly, so OpenAI SDKs work as-is.

| | |
| --- | --- |
| Model id | `flux-2-klein-4b` |
| Provider | Black Forest Labs |
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
# FLUX.2 Klein 4B, cURL: submit the job
# https://empiriolabs.ai/models/flux-2-klein-4b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/images/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "flux-2-klein-4b",
    "prompt": "Describe what you want FLUX.2 Klein 4B to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# FLUX.2 Klein 4B, cURL: poll for the result
# https://empiriolabs.ai/models/flux-2-klein-4b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""FLUX.2 Klein 4B, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/flux-2-klein-4b
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/images/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "flux-2-klein-4b",
        "prompt": "Describe what you want FLUX.2 Klein 4B to generate.",
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

- [FLUX.2 Klein 4B pricing and specs](https://empiriolabs.ai/models/flux-2-klein-4b)
- [FLUX.2 Klein 4B API reference](https://docs.empiriolabs.ai/models/flux-2-klein-4b)
- [Try FLUX.2 Klein 4B in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=flux-2-klein-4b)

[All EmpirioLabs AI examples](../../README.md)
