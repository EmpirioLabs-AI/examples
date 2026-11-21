# HappyHorse 1.0 API examples

Video model offering Text-to-Video, Image-to-Video, Reference-to-Video, and Video Edit modes with high-fidelity, motion-smooth output.

HappyHorse 1.0 runs through `POST /v1/videos/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `happyhorse-1-0` |
| Provider | Alibaba Cloud |
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
# HappyHorse 1.0, cURL: submit the job
# https://empiriolabs.ai/models/happyhorse-1-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "happyhorse-1-0",
    "prompt": "Describe what you want HappyHorse 1.0 to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# HappyHorse 1.0, cURL: poll for the result
# https://empiriolabs.ai/models/happyhorse-1-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""HappyHorse 1.0, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/happyhorse-1-0
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/videos/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "happyhorse-1-0",
        "prompt": "Describe what you want HappyHorse 1.0 to generate.",
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

- [HappyHorse 1.0 pricing and specs](https://empiriolabs.ai/models/happyhorse-1-0)
- [HappyHorse 1.0 API reference](https://docs.empiriolabs.ai/models/happyhorse-1-0)
- [Try HappyHorse 1.0 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=happyhorse-1-0)
