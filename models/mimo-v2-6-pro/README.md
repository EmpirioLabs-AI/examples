# MiMo V2.6 Pro API examples

Trillion-parameter flagship for agentic work, with native image, video, and audio understanding and reasoning across a 1M context.

MiMo V2.6 Pro serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `mimo-v2-6-pro`.

| | |
| --- | --- |
| Model id | `mimo-v2-6-pro` |
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
# MiMo V2.6 Pro, cURL
# https://empiriolabs.ai/models/mimo-v2-6-pro
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2-6-pro",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""MiMo V2.6 Pro, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/mimo-v2-6-pro
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="mimo-v2-6-pro",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [MiMo V2.6 Pro pricing and specs](https://empiriolabs.ai/models/mimo-v2-6-pro)
- [MiMo V2.6 Pro API reference](https://docs.empiriolabs.ai/models/mimo-v2-6-pro)
- [Try MiMo V2.6 Pro in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=mimo-v2-6-pro)

[All EmpirioLabs AI examples](../../README.md)
