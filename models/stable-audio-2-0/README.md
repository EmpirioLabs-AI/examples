# Stable Audio 2.0 API examples

Generates audio up to 3 minutes from text prompts, supporting text-to-audio and audio-to-audio with adjustable duration, steps, and CFG scale.

Stable Audio 2.0 runs through `POST /v1/audio/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `stable-audio-2-0` |
| Provider | Stability AI |
| Category | Audio Generation |
| Endpoint | `POST /v1/audio/generations` |

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
# Stable Audio 2.0, cURL: submit the job
# https://empiriolabs.ai/models/stable-audio-2-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stable-audio-2-0",
    "prompt": "Describe what you want Stable Audio 2.0 to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# Stable Audio 2.0, cURL: poll for the result
# https://empiriolabs.ai/models/stable-audio-2-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""Stable Audio 2.0, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/stable-audio-2-0
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "stable-audio-2-0",
        "prompt": "Describe what you want Stable Audio 2.0 to generate.",
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

- [Stable Audio 2.0 pricing and specs](https://empiriolabs.ai/models/stable-audio-2-0)
- [Stable Audio 2.0 API reference](https://docs.empiriolabs.ai/models/stable-audio-2-0)
- [Try Stable Audio 2.0 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=stable-audio-2-0)

[All EmpirioLabs AI examples](../../README.md)
