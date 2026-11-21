# SoulX Podcast API examples

Open-source voice model for long-form, multi-speaker podcast dialogue with paralinguistic control (laughter, sighs) and zero-shot voice cloning.

SoulX Podcast serves speech through `POST /v1/audio/speech` and returns playable audio. Send the text to speak as `input` with the model id `soulx-podcast`.

| | |
| --- | --- |
| Model id | `soulx-podcast` |
| Provider | Soul AI Lab |
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
# SoulX Podcast, cURL
# https://empiriolabs.ai/models/soulx-podcast
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/audio/speech \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "soulx-podcast",
    "input": "Welcome to EmpirioLabs. Your build just finished."
  }' \
  --output speech.mp3
```

## Python

[`example.py`](example.py)

```python
"""SoulX Podcast, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/soulx-podcast
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "soulx-podcast", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
```

## Links

- [SoulX Podcast pricing and specs](https://empiriolabs.ai/models/soulx-podcast)
- [SoulX Podcast API reference](https://docs.empiriolabs.ai/models/soulx-podcast)
- [Try SoulX Podcast in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=soulx-podcast)

[All EmpirioLabs AI examples](../../README.md)
