# TRELLIS.2 4B API examples

TRELLIS.2 image-to-3D model that turns a reference image into a textured GLB asset with resolution, seed, mesh, texture, and export controls.

TRELLIS.2 4B runs through `POST /v1/3d/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `trellis-2-4b` |
| Provider | Microsoft |
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
# TRELLIS.2 4B, cURL: submit the job
# https://empiriolabs.ai/models/trellis-2-4b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "trellis-2-4b",
    "prompt": "Describe what you want TRELLIS.2 4B to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# TRELLIS.2 4B, cURL: poll for the result
# https://empiriolabs.ai/models/trellis-2-4b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""TRELLIS.2 4B, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/trellis-2-4b
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/3d/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "trellis-2-4b",
        "prompt": "Describe what you want TRELLIS.2 4B to generate.",
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

- [TRELLIS.2 4B pricing and specs](https://empiriolabs.ai/models/trellis-2-4b)
- [TRELLIS.2 4B API reference](https://docs.empiriolabs.ai/models/trellis-2-4b)
- [Try TRELLIS.2 4B in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=trellis-2-4b)
