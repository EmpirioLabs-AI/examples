# GLM TTS API examples

LLM-based text-to-speech with zero-shot voice cloning and emotion-expressive, controllable output via multi-reward RL.

GLM TTS serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `glm-tts`.

| | |
| --- | --- |
| Model id | `glm-tts` |
| Provider | Z.ai |
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
# GLM TTS, cURL
# https://empiriolabs.ai/models/glm-tts
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-tts",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""GLM TTS, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/glm-tts
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "glm-tts", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [GLM TTS pricing and specs](https://empiriolabs.ai/models/glm-tts)
- [GLM TTS API reference](https://docs.empiriolabs.ai/models/glm-tts)
- [Try GLM TTS in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=glm-tts)
