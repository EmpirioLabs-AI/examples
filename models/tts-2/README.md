# TTS 2 API examples

Realtime voice model that takes plain-English delivery direction, holds one voice identity across 200+ languages, and streams with word timestamps.

TTS 2 serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `tts-2`.

| | |
| --- | --- |
| Model id | `tts-2` |
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
# TTS 2, cURL
# https://empiriolabs.ai/models/tts-2
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-2",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""TTS 2, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/tts-2
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "tts-2", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [TTS 2 pricing and specs](https://empiriolabs.ai/models/tts-2)
- [TTS 2 API reference](https://docs.empiriolabs.ai/models/tts-2)
- [Try TTS 2 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=tts-2)

[All EmpirioLabs AI examples](../../README.md)
