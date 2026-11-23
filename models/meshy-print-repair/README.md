# Meshy Print Repair API examples

Repairs an existing 3D model for 3D printing, fixing holes and non-manifold geometry and thickening walls that are too thin at the planned print size.

Meshy Print Repair runs through `POST /v1/3d/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `meshy-print-repair` |
| Provider | Meshy |
| Category | 3D Generation |
| Endpoint | `POST /v1/3d/generations` |

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
# Meshy Print Repair, cURL: submit the job
# https://empiriolabs.ai/models/meshy-print-repair
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/3d/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meshy-print-repair",
    "prompt": "Describe what you want Meshy Print Repair to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# Meshy Print Repair, cURL: poll for the result
# https://empiriolabs.ai/models/meshy-print-repair
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""Meshy Print Repair, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/meshy-print-repair
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/3d/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "meshy-print-repair",
        "prompt": "Describe what you want Meshy Print Repair to generate.",
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

- [Meshy Print Repair pricing and specs](https://empiriolabs.ai/models/meshy-print-repair)
- [Meshy Print Repair API reference](https://docs.empiriolabs.ai/models/meshy-print-repair)
- [Try Meshy Print Repair in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=meshy-print-repair)

[All EmpirioLabs AI examples](../../README.md)
