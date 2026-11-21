# TTS 1.5 Max API examples

Broadcast-quality voice synthesis with rich expressive prosody, 271+ voices across 15 languages, and real-time SSE streaming with per-word timestamps.

TTS 1.5 Max serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `tts-1-5-max`.

| | |
| --- | --- |
| Model id | `tts-1-5-max` |
| Provider | Inworld |
| Category | Audio Generation |
| Endpoint | `POST /v1/audio/speech` |

## Run

```bash
export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."   # https://platform.empiriolabs.ai/dashboard/api-keys
bash request.sh
pip install requests && python example.py
```

## cURL

[`request.sh`](request.sh)

```bash
#!/usr/bin/env bash
# TTS 1.5 Max, cURL
# https://empiriolabs.ai/models/tts-1-5-max
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1-5-max",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""TTS 1.5 Max, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/tts-1-5-max
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "tts-1-5-max", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [TTS 1.5 Max pricing and specs](https://empiriolabs.ai/models/tts-1-5-max)
- [TTS 1.5 Max API reference](https://docs.empiriolabs.ai/models/tts-1-5-max)
- [Try TTS 1.5 Max in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=tts-1-5-max)

[All EmpirioLabs AI examples](../../README.md)
