# Sonilo Proofread API examples

Transcribes a video and translates the script into 24 languages, returning editable subtitle tracks you can correct before dubbing.

Sonilo Proofread runs through `POST /v1/audio/transcriptions`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `sonilo-proofread` |
| Provider | Sonilo |
| Category | Transcription |
| Endpoint | `POST /v1/audio/transcriptions` |

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
# Sonilo Proofread, cURL: submit the job
# https://empiriolabs.ai/models/sonilo-proofread
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonilo-proofread",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# Sonilo Proofread, cURL: poll for the result
# https://empiriolabs.ai/models/sonilo-proofread
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""Sonilo Proofread, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/sonilo-proofread
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/transcriptions",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "sonilo-proofread",
        "audio_url": "https://example.com/meeting-recording.mp3",
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

- [Sonilo Proofread pricing and specs](https://empiriolabs.ai/models/sonilo-proofread)
- [Sonilo Proofread API reference](https://docs.empiriolabs.ai/models/sonilo-proofread)
- [Try Sonilo Proofread in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=sonilo-proofread)

[All EmpirioLabs AI examples](../../README.md)
