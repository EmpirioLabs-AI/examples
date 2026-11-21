# StepAudio 3 TTS API examples

Human-level speech synthesis across six languages, with 12 system voices, natural-language delivery direction, and streaming playback.

StepAudio 3 TTS serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `stepaudio-3-tts`.

| | |
| --- | --- |
| Model id | `stepaudio-3-tts` |
| Provider | StepFun |
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
# StepAudio 3 TTS, cURL
# https://empiriolabs.ai/models/stepaudio-3-tts
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-3-tts",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""StepAudio 3 TTS, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/stepaudio-3-tts
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "stepaudio-3-tts", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [StepAudio 3 TTS pricing and specs](https://empiriolabs.ai/models/stepaudio-3-tts)
- [StepAudio 3 TTS API reference](https://docs.empiriolabs.ai/models/stepaudio-3-tts)
- [Try StepAudio 3 TTS in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=stepaudio-3-tts)
