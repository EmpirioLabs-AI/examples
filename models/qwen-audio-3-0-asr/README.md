# Qwen Audio 3.0 ASR API examples

Speech-to-text for short clips and long recordings, with timed sentence segments and recognition of 30 languages and the major Chinese dialects.

Qwen Audio 3.0 ASR runs through `POST /v1/audio/transcriptions`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `qwen-audio-3-0-asr` |
| Provider | Alibaba Cloud |
| Category | Transcription |
| Endpoint | `POST /v1/audio/transcriptions` |

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
# Qwen Audio 3.0 ASR, cURL: submit the job
# https://empiriolabs.ai/models/qwen-audio-3-0-asr
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-audio-3-0-asr",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# Qwen Audio 3.0 ASR, cURL: poll for the result
# https://empiriolabs.ai/models/qwen-audio-3-0-asr
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""Qwen Audio 3.0 ASR, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/qwen-audio-3-0-asr
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/transcriptions",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "qwen-audio-3-0-asr",
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

- [Qwen Audio 3.0 ASR pricing and specs](https://empiriolabs.ai/models/qwen-audio-3-0-asr)
- [Qwen Audio 3.0 ASR API reference](https://docs.empiriolabs.ai/models/qwen-audio-3-0-asr)
- [Try Qwen Audio 3.0 ASR in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=qwen-audio-3-0-asr)

[All EmpirioLabs AI examples](../../README.md)
