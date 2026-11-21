# MiniMax Music 3 API examples

Generates complete stereo songs from lyrics and a style prompt, with duration, seed, and format controls up to 5 minutes.

MiniMax Music 3 runs through `POST /v1/audio/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `minimax-music-3` |
| Provider | MiniMax |
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
# MiniMax Music 3, cURL: submit the job
# https://empiriolabs.ai/models/minimax-music-3
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-music-3",
    "prompt": "Describe what you want MiniMax Music 3 to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# MiniMax Music 3, cURL: poll for the result
# https://empiriolabs.ai/models/minimax-music-3
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""MiniMax Music 3, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/minimax-music-3
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "minimax-music-3",
        "prompt": "Describe what you want MiniMax Music 3 to generate.",
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

- [MiniMax Music 3 pricing and specs](https://empiriolabs.ai/models/minimax-music-3)
- [MiniMax Music 3 API reference](https://docs.empiriolabs.ai/models/minimax-music-3)
- [Try MiniMax Music 3 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=minimax-music-3)

[All EmpirioLabs AI examples](../../README.md)
