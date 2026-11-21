# TTS 1.5 Mini API examples

Sub-130ms TTFB voice synthesis with 271+ voices across 15 languages, expressive prosody, and real-time SSE streaming for low-latency voice agents.

TTS 1.5 Mini serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `tts-1-5-mini`.

| | |
| --- | --- |
| Model id | `tts-1-5-mini` |
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
# TTS 1.5 Mini, cURL
# https://empiriolabs.ai/models/tts-1-5-mini
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1-5-mini",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""TTS 1.5 Mini, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/tts-1-5-mini
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "tts-1-5-mini", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [TTS 1.5 Mini pricing and specs](https://empiriolabs.ai/models/tts-1-5-mini)
- [TTS 1.5 Mini API reference](https://docs.empiriolabs.ai/models/tts-1-5-mini)
- [Try TTS 1.5 Mini in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=tts-1-5-mini)

[All EmpirioLabs AI examples](../../README.md)
