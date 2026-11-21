# Qwen Audio 3.1 TTS Next API examples

Audio generation from a written description, with narration, dialogue in up to three cloned voices, sound effects, ambience, and music in one file.

Qwen Audio 3.1 TTS Next serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `qwen-audio-3-1-tts-next`.

| | |
| --- | --- |
| Model id | `qwen-audio-3-1-tts-next` |
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
# Qwen Audio 3.1 TTS Next, cURL
# https://empiriolabs.ai/models/qwen-audio-3-1-tts-next
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-audio-3-1-tts-next",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""Qwen Audio 3.1 TTS Next, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/qwen-audio-3-1-tts-next
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "qwen-audio-3-1-tts-next", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [Qwen Audio 3.1 TTS Next pricing and specs](https://empiriolabs.ai/models/qwen-audio-3-1-tts-next)
- [Qwen Audio 3.1 TTS Next API reference](https://docs.empiriolabs.ai/models/qwen-audio-3-1-tts-next)
- [Try Qwen Audio 3.1 TTS Next in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=qwen-audio-3-1-tts-next)
