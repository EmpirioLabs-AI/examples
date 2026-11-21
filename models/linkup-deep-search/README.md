# Linkup Deep Search API examples

Iterative AI search that keeps querying when initial results are insufficient, returning more comprehensive answers than Standard mode.

Linkup Deep Search serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `linkup-deep-search`.

| | |
| --- | --- |
| Model id | `linkup-deep-search` |
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
# Linkup Deep Search, cURL
# https://empiriolabs.ai/models/linkup-deep-search
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "linkup-deep-search",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Linkup Deep Search, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/linkup-deep-search
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="linkup-deep-search",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Linkup Deep Search pricing and specs](https://empiriolabs.ai/models/linkup-deep-search)
- [Linkup Deep Search API reference](https://docs.empiriolabs.ai/models/linkup-deep-search)
- [Try Linkup Deep Search in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=linkup-deep-search)

[All EmpirioLabs AI examples](../../README.md)
