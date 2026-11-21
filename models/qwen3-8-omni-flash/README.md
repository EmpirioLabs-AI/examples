# Qwen3.8 Omni Flash API examples

Omni-modal reasoner that reads text, images, audio, and video and answers in text, with a 1M token context, thinking, and native web search.

Qwen3.8 Omni Flash serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `qwen3-8-omni-flash`.

| | |
| --- | --- |
| Model id | `qwen3-8-omni-flash` |
| Provider | Alibaba Cloud |
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
# Qwen3.8 Omni Flash, cURL
# https://empiriolabs.ai/models/qwen3-8-omni-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-8-omni-flash",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Qwen3.8 Omni Flash, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/qwen3-8-omni-flash
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="qwen3-8-omni-flash",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Qwen3.8 Omni Flash pricing and specs](https://empiriolabs.ai/models/qwen3-8-omni-flash)
- [Qwen3.8 Omni Flash API reference](https://docs.empiriolabs.ai/models/qwen3-8-omni-flash)
- [Try Qwen3.8 Omni Flash in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=qwen3-8-omni-flash)

[All EmpirioLabs AI examples](../../README.md)
