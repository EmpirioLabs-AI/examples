# MiniMax H3 Lite API examples

Lower-cost 4 to 15 second clips at 480p or 768p with native stereo audio, from text, a first and last frame, or image, video, and audio references.

MiniMax H3 Lite runs through `POST /v1/videos/generations`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `minimax-h3-lite` |
| Provider | MiniMax |
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
# MiniMax H3 Lite, cURL: submit the job
# https://empiriolabs.ai/models/minimax-h3-lite
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/videos/generations \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "minimax-h3-lite",
    "prompt": "Describe what you want MiniMax H3 Lite to generate."
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# MiniMax H3 Lite, cURL: poll for the result
# https://empiriolabs.ai/models/minimax-h3-lite
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""MiniMax H3 Lite, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/minimax-h3-lite
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/videos/generations",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "minimax-h3-lite",
        "prompt": "Describe what you want MiniMax H3 Lite to generate.",
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

- [MiniMax H3 Lite pricing and specs](https://empiriolabs.ai/models/minimax-h3-lite)
- [MiniMax H3 Lite API reference](https://docs.empiriolabs.ai/models/minimax-h3-lite)
- [Try MiniMax H3 Lite in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=minimax-h3-lite)
