# Seed TTS 3.0 API examples

Expressive speech in 119 languages and dialects, steered by 82 inline audio tags for emotion, delivery and vocal sounds, with 541 preset voices.

Seed TTS 3.0 serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `seed-tts-3-0`.

| | |
| --- | --- |
| Model id | `seed-tts-3-0` |
| Provider | ByteDance |
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
# Seed TTS 3.0, cURL
# https://empiriolabs.ai/models/seed-tts-3-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seed-tts-3-0",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""Seed TTS 3.0, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/seed-tts-3-0
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "seed-tts-3-0", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [Seed TTS 3.0 pricing and specs](https://empiriolabs.ai/models/seed-tts-3-0)
- [Seed TTS 3.0 API reference](https://docs.empiriolabs.ai/models/seed-tts-3-0)
- [Try Seed TTS 3.0 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=seed-tts-3-0)

[All EmpirioLabs AI examples](../../README.md)
