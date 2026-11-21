# StepAudio 2.5 ASR API examples

StepFun streaming speech recognition model for Chinese and English audio transcription.

StepAudio 2.5 ASR runs through `POST /v1/audio/transcriptions`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `stepaudio-2-5-asr` |
| Provider | StepFun |
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
# StepAudio 2.5 ASR, cURL: submit the job
# https://empiriolabs.ai/models/stepaudio-2-5-asr
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-2-5-asr",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# StepAudio 2.5 ASR, cURL: poll for the result
# https://empiriolabs.ai/models/stepaudio-2-5-asr
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""StepAudio 2.5 ASR, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/stepaudio-2-5-asr
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/transcriptions",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "stepaudio-2-5-asr",
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

- [StepAudio 2.5 ASR pricing and specs](https://empiriolabs.ai/models/stepaudio-2-5-asr)
- [StepAudio 2.5 ASR API reference](https://docs.empiriolabs.ai/models/stepaudio-2-5-asr)
- [Try StepAudio 2.5 ASR in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=stepaudio-2-5-asr)

[All EmpirioLabs AI examples](../../README.md)
