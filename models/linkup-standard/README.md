# Linkup Standard API examples

AI-powered web search with detailed overviews and answers, faster than Deep Search.

Linkup Standard serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `linkup-standard`.

| | |
| --- | --- |
| Model id | `linkup-standard` |
| Provider | Linkup |
| Category | Research & Search |
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
# Linkup Standard, cURL
# https://empiriolabs.ai/models/linkup-standard
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "linkup-standard",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Linkup Standard, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/linkup-standard
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="linkup-standard",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Linkup Standard pricing and specs](https://empiriolabs.ai/models/linkup-standard)
- [Linkup Standard API reference](https://docs.empiriolabs.ai/models/linkup-standard)
- [Try Linkup Standard in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=linkup-standard)

[All EmpirioLabs AI examples](../../README.md)
