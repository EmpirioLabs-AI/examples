# Tongyi Embedding Vision Plus API examples

Multimodal embedding producing independent vectors for text, image, and video inputs.

Tongyi Embedding Vision Plus serves the OpenAI-compatible Embeddings API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` and use the model id `tongyi-embedding-vision-plus`.

| | |
| --- | --- |
| Model id | `tongyi-embedding-vision-plus` |
| Provider | Alibaba Cloud |
| Category | Embeddings |
| Endpoint | `POST /v1/embeddings` |

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
# Tongyi Embedding Vision Plus, cURL
# https://empiriolabs.ai/models/tongyi-embedding-vision-plus
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/embeddings \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tongyi-embedding-vision-plus",
    "input": "The quick brown fox jumps over the lazy dog."
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Tongyi Embedding Vision Plus, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/tongyi-embedding-vision-plus
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

embedding = client.embeddings.create(
    model="tongyi-embedding-vision-plus",
    input="The quick brown fox jumps over the lazy dog.",
)
print(embedding.data[0].embedding[:8])
```

## Links

- [Tongyi Embedding Vision Plus pricing and specs](https://empiriolabs.ai/models/tongyi-embedding-vision-plus)
- [Tongyi Embedding Vision Plus API reference](https://docs.empiriolabs.ai/models/tongyi-embedding-vision-plus)
- [Try Tongyi Embedding Vision Plus in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=tongyi-embedding-vision-plus)

[All EmpirioLabs AI examples](../../README.md)
