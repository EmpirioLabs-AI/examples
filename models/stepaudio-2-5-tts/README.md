# StepAudio 2.5 TTS API examples

Contextual StepFun text-to-speech model with natural-language voice direction and expressive delivery.

StepAudio 2.5 TTS serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `stepaudio-2-5-tts`.

| | |
| --- | --- |
| Model id | `stepaudio-2-5-tts` |
| Provider | StepFun |
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
# StepAudio 2.5 TTS, cURL
# https://empiriolabs.ai/models/stepaudio-2-5-tts
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-2-5-tts",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""StepAudio 2.5 TTS, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/stepaudio-2-5-tts
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "stepaudio-2-5-tts", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [StepAudio 2.5 TTS pricing and specs](https://empiriolabs.ai/models/stepaudio-2-5-tts)
- [StepAudio 2.5 TTS API reference](https://docs.empiriolabs.ai/models/stepaudio-2-5-tts)
- [Try StepAudio 2.5 TTS in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=stepaudio-2-5-tts)

[All EmpirioLabs AI examples](../../README.md)
