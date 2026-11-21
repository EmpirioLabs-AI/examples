# StepAudio 3 ASR Max API examples

Context-aware transcription for proper nouns, technical terms, dialects, and difficult audio including whispers, fast speech, and singing.

StepAudio 3 ASR Max runs through `POST /v1/audio/transcriptions`. The request returns a `job_id` right away; poll `GET /v1/jobs/{job_id}` until the job completes and read the output URLs from the result.

| | |
| --- | --- |
| Model id | `stepaudio-3-asr-max` |
| Provider | StepFun |
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
# StepAudio 3 ASR Max, cURL: submit the job
# https://empiriolabs.ai/models/stepaudio-3-asr-max
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/transcriptions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-3-asr-max",
    "audio_url": "https://example.com/meeting-recording.mp3"
  }'
```

## cURL: poll for the result

[`poll.sh`](poll.sh)

```bash
#!/usr/bin/env bash
# StepAudio 3 ASR Max, cURL: poll for the result
# https://empiriolabs.ai/models/stepaudio-3-asr-max
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/jobs/${JOB_ID:?Set JOB_ID to the job_id that submit.sh returned} \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY"
```

## Python

[`example.py`](example.py)

```python
"""StepAudio 3 ASR Max, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/stepaudio-3-asr-max
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/transcriptions",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "stepaudio-3-asr-max",
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

- [StepAudio 3 ASR Max pricing and specs](https://empiriolabs.ai/models/stepaudio-3-asr-max)
- [StepAudio 3 ASR Max API reference](https://docs.empiriolabs.ai/models/stepaudio-3-asr-max)
- [Try StepAudio 3 ASR Max in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=stepaudio-3-asr-max)

[All EmpirioLabs AI examples](../../README.md)
