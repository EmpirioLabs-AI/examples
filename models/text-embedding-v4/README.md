# Text Embedding v4 API examples

Multilingual text embedding with selectable output dimensions (64–2048). Up to 8,192 tokens per input.

Text Embedding v4 serves the OpenAI-compatible Embeddings API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` and use the model id `text-embedding-v4`.

| | |
| --- | --- |
| Model id | `text-embedding-v4` |
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
# Text Embedding v4, cURL
# https://empiriolabs.ai/models/text-embedding-v4
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/embeddings \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-v4",
    "input": "The quick brown fox jumps over the lazy dog."
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Text Embedding v4, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/text-embedding-v4
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

embedding = client.embeddings.create(
    model="text-embedding-v4",
    input="The quick brown fox jumps over the lazy dog.",
)
print(embedding.data[0].embedding[:8])
```

## Links

- [Text Embedding v4 pricing and specs](https://empiriolabs.ai/models/text-embedding-v4)
- [Text Embedding v4 API reference](https://docs.empiriolabs.ai/models/text-embedding-v4)
- [Try Text Embedding v4 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=text-embedding-v4)

[All EmpirioLabs AI examples](../../README.md)
