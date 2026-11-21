# Skylark Embedding Vision API examples

Multimodal embedding that fuses text, images, and video into one 1024 or 2048 dimension vector for cross-modal search and retrieval.

Skylark Embedding Vision serves the OpenAI-compatible Embeddings API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` and use the model id `skylark-embedding-vision`.

| | |
| --- | --- |
| Model id | `skylark-embedding-vision` |
| Provider | ByteDance |
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
# Skylark Embedding Vision, cURL
# https://empiriolabs.ai/models/skylark-embedding-vision
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/embeddings \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "skylark-embedding-vision",
    "input": "The quick brown fox jumps over the lazy dog."
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Skylark Embedding Vision, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/skylark-embedding-vision
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

embedding = client.embeddings.create(
    model="skylark-embedding-vision",
    input="The quick brown fox jumps over the lazy dog.",
)
print(embedding.data[0].embedding[:8])
```

## Links

- [Skylark Embedding Vision pricing and specs](https://empiriolabs.ai/models/skylark-embedding-vision)
- [Skylark Embedding Vision API reference](https://docs.empiriolabs.ai/models/skylark-embedding-vision)
- [Try Skylark Embedding Vision in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=skylark-embedding-vision)
