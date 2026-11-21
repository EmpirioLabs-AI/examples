# PixVerse V6 Max API examples

Text- and image-to-video up to 15 seconds at 1080p, with 5,000-character prompts, shot-by-shot direction, and native synchronized audio.

PixVerse V6 Max runs through `POST /v1/videos/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `pixverse-v6-max` |
| Provider | PixVerse |
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
# PixVerse V6 Max, cURL: submit the job
# https://empiriolabs.ai/models/pixverse-v6-max
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "pixverse-v6-max",
    "prompt": "Describe what you want PixVerse V6 Max to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# PixVerse V6 Max, cURL: poll for the result
# https://empiriolabs.ai/models/pixverse-v6-max
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""PixVerse V6 Max, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/pixverse-v6-max
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/videos/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "pixverse-v6-max",
        "prompt": "Describe what you want PixVerse V6 Max to generate.",
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

- [PixVerse V6 Max pricing and specs](https://empiriolabs.ai/models/pixverse-v6-max)
- [PixVerse V6 Max API reference](https://docs.empiriolabs.ai/models/pixverse-v6-max)
- [Try PixVerse V6 Max in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=pixverse-v6-max)
