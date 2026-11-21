# Qwen Audio 3.1 TTS API examples

Real-time speech synthesis with 19 voices, delivery direction in plain language, inline emotion and sound tags, and audio streamed over SSE or WebSocket.

Qwen Audio 3.1 TTS serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `qwen-audio-3-1-tts`.

| | |
| --- | --- |
| Model id | `qwen-audio-3-1-tts` |
| Provider | Alibaba Cloud |
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
# Qwen Audio 3.1 TTS, cURL
# https://empiriolabs.ai/models/qwen-audio-3-1-tts
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-audio-3-1-tts",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""Qwen Audio 3.1 TTS, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/qwen-audio-3-1-tts
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "qwen-audio-3-1-tts", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [Qwen Audio 3.1 TTS pricing and specs](https://empiriolabs.ai/models/qwen-audio-3-1-tts)
- [Qwen Audio 3.1 TTS API reference](https://docs.empiriolabs.ai/models/qwen-audio-3-1-tts)
