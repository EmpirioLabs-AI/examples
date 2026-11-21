# MiMo V2.6 Flash API examples

Low-cost full-modality reasoner with native image, video, and audio understanding on a 1M context, built for high-frequency production workloads.

MiMo V2.6 Flash serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `mimo-v2-6-flash`.

| | |
| --- | --- |
| Model id | `mimo-v2-6-flash` |
| Provider | Xiaomi |
| Category | Text Generation |
| Endpoint | `POST /v1/chat/completions` |

## Run

```bash
eval "$(python ../../login.py)"   # sign in, or: export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."
bash request.sh
pip install openai && python example.py
```

## cURL

[`request.sh`](request.sh)

```bash
#!/usr/bin/env bash
# MiMo V2.6 Flash, cURL
# https://empiriolabs.ai/models/mimo-v2-6-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2-6-flash",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""MiMo V2.6 Flash, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/mimo-v2-6-flash
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="mimo-v2-6-flash",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [MiMo V2.6 Flash pricing and specs](https://empiriolabs.ai/models/mimo-v2-6-flash)
- [MiMo V2.6 Flash API reference](https://docs.empiriolabs.ai/models/mimo-v2-6-flash)
- [Try MiMo V2.6 Flash in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=mimo-v2-6-flash)

[All EmpirioLabs AI examples](../../README.md)
