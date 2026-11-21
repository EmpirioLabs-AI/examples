# Tongyi Embedding Vision Flash API examples

Speed-optimised multimodal embedding, same shape as Vision-Plus, 3× cheaper image/video tokens.

Tongyi Embedding Vision Flash serves the OpenAI-compatible Embeddings API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` and use the model id `tongyi-embedding-vision-flash`.

| | |
| --- | --- |
| Model id | `tongyi-embedding-vision-flash` |
| Provider | Alibaba Cloud |
| Category | Embeddings |
| Endpoint | `POST /v1/embeddings` |

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
# Tongyi Embedding Vision Flash, cURL
# https://empiriolabs.ai/models/tongyi-embedding-vision-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/embeddings \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tongyi-embedding-vision-flash",
    "input": "The quick brown fox jumps over the lazy dog."
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Tongyi Embedding Vision Flash, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/tongyi-embedding-vision-flash
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

embedding = client.embeddings.create(
    model="tongyi-embedding-vision-flash",
    input="The quick brown fox jumps over the lazy dog.",
)
print(embedding.data[0].embedding[:8])
```

## Links

- [Tongyi Embedding Vision Flash pricing and specs](https://empiriolabs.ai/models/tongyi-embedding-vision-flash)
- [Tongyi Embedding Vision Flash API reference](https://docs.empiriolabs.ai/models/tongyi-embedding-vision-flash)
- [Try Tongyi Embedding Vision Flash in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=tongyi-embedding-vision-flash)

[All EmpirioLabs AI examples](../../README.md)
