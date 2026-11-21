# Gemini 2.5 Pro TTS API examples

High-quality TTS preview for podcasts, audiobooks, and customer support, with expressive multi-speaker voices across 23+ languages.

Gemini 2.5 Pro TTS serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `gemini-2-5-pro-tts`.

| | |
| --- | --- |
| Model id | `gemini-2-5-pro-tts` |
| Provider | Google |
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
# Gemini 2.5 Pro TTS, cURL
# https://empiriolabs.ai/models/gemini-2-5-pro-tts
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2-5-pro-tts",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""Gemini 2.5 Pro TTS, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/gemini-2-5-pro-tts
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "gemini-2-5-pro-tts", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [Gemini 2.5 Pro TTS pricing and specs](https://empiriolabs.ai/models/gemini-2-5-pro-tts)
- [Gemini 2.5 Pro TTS API reference](https://docs.empiriolabs.ai/models/gemini-2-5-pro-tts)
- [Try Gemini 2.5 Pro TTS in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=gemini-2-5-pro-tts)
