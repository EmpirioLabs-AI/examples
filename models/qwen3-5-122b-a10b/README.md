# Qwen3.5 122B-A10B API examples

Qwen3.5 122B-A10B is a multimodal reasoning model with 256K context, efficient sparse MoE inference, and text, image, and video input.

Qwen3.5 122B-A10B serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `qwen3-5-122b-a10b`.

| | |
| --- | --- |
| Model id | `qwen3-5-122b-a10b` |
| Provider | Alibaba Cloud |
| Category | Text Generation |
| Endpoint | `POST /v1/chat/completions` |

## Run

```bash
export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."   # https://platform.empiriolabs.ai/dashboard/api-keys
bash request.sh
pip install openai && python example.py
```

## cURL

[`request.sh`](request.sh)

```bash
#!/usr/bin/env bash
# Qwen3.5 122B-A10B, cURL
# https://empiriolabs.ai/models/qwen3-5-122b-a10b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-5-122b-a10b",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Qwen3.5 122B-A10B, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/qwen3-5-122b-a10b
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="qwen3-5-122b-a10b",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Qwen3.5 122B-A10B pricing and specs](https://empiriolabs.ai/models/qwen3-5-122b-a10b)
- [Qwen3.5 122B-A10B API reference](https://docs.empiriolabs.ai/models/qwen3-5-122b-a10b)
- [Try Qwen3.5 122B-A10B in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=qwen3-5-122b-a10b)
