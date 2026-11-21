# Gemma 4 26B-A4B API examples

Gemma 4 26B A4B is a Google open multimodal model with 256K context, text, image, and video input, tools, and structured output.

Gemma 4 26B-A4B serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `gemma-4-26b-a4b`.

| | |
| --- | --- |
| Model id | `gemma-4-26b-a4b` |
| Provider | Google |
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
# Gemma 4 26B-A4B, cURL
# https://empiriolabs.ai/models/gemma-4-26b-a4b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma-4-26b-a4b",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Gemma 4 26B-A4B, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/gemma-4-26b-a4b
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="gemma-4-26b-a4b",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Gemma 4 26B-A4B pricing and specs](https://empiriolabs.ai/models/gemma-4-26b-a4b)
- [Gemma 4 26B-A4B API reference](https://docs.empiriolabs.ai/models/gemma-4-26b-a4b)
- [Try Gemma 4 26B-A4B in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=gemma-4-26b-a4b)

[All EmpirioLabs AI examples](../../README.md)
