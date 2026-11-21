# Qwen3.5 397B-A17B API examples

Qwen3.5 397B-A17B is a flagship multimodal reasoning model for language, code, agents, GUI tasks, and image and video understanding.

Qwen3.5 397B-A17B serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `qwen3-5-397b-a17b`.

| | |
| --- | --- |
| Model id | `qwen3-5-397b-a17b` |
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
# Qwen3.5 397B-A17B, cURL
# https://empiriolabs.ai/models/qwen3-5-397b-a17b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-5-397b-a17b",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Qwen3.5 397B-A17B, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/qwen3-5-397b-a17b
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="qwen3-5-397b-a17b",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Qwen3.5 397B-A17B pricing and specs](https://empiriolabs.ai/models/qwen3-5-397b-a17b)
- [Qwen3.5 397B-A17B API reference](https://docs.empiriolabs.ai/models/qwen3-5-397b-a17b)
- [Try Qwen3.5 397B-A17B in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=qwen3-5-397b-a17b)

[All EmpirioLabs AI examples](../../README.md)
