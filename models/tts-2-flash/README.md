# TTS 2 Flash API examples

Latency-first realtime voice synthesis holding one voice identity across 200+ languages, tuned for high-volume streaming workloads.

TTS 2 Flash serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `tts-2-flash`.

| | |
| --- | --- |
| Model id | `tts-2-flash` |
| Provider | Inworld |
| Category | Audio Generation |
| Endpoint | `POST /v1/audio/speech` |

## Run

```bash
eval "$(python ../../login.py)"   # sign in, or: export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."
bash request.sh
pip install requests && python example.py
```

## cURL

[`request.sh`](request.sh)

```bash
#!/usr/bin/env bash
# TTS 2 Flash, cURL
# https://empiriolabs.ai/models/tts-2-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-2-flash",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""TTS 2 Flash, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/tts-2-flash
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "tts-2-flash", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [TTS 2 Flash pricing and specs](https://empiriolabs.ai/models/tts-2-flash)
- [TTS 2 Flash API reference](https://docs.empiriolabs.ai/models/tts-2-flash)
- [Try TTS 2 Flash in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=tts-2-flash)

[All EmpirioLabs AI examples](../../README.md)
