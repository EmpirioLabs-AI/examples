# Hyper3D Gen2 API examples

Rodin Gen-2 engine that turns a text prompt or up to five reference images into production 3D assets with PBR materials and quad or raw meshes.

Hyper3D Gen2 runs through `POST /v1/3d/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `hyper3d-gen2` |
| Provider | Deemos |
| Category | 3D Generation |
| Endpoint | `POST /v1/3d/generations` |

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
# Hyper3D Gen2, cURL: submit the job
# https://empiriolabs.ai/models/hyper3d-gen2
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "hyper3d-gen2",
    "prompt": "Describe what you want Hyper3D Gen2 to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# Hyper3D Gen2, cURL: poll for the result
# https://empiriolabs.ai/models/hyper3d-gen2
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""Hyper3D Gen2, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/hyper3d-gen2
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/3d/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "hyper3d-gen2",
        "prompt": "Describe what you want Hyper3D Gen2 to generate.",
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

- [Hyper3D Gen2 pricing and specs](https://empiriolabs.ai/models/hyper3d-gen2)
- [Hyper3D Gen2 API reference](https://docs.empiriolabs.ai/models/hyper3d-gen2)
- [Try Hyper3D Gen2 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=hyper3d-gen2)
