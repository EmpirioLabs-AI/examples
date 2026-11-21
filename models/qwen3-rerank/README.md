# Qwen3 Rerank API examples

Semantic document reranker. Sorts up to 500 candidates per query by relevance, supports 100+ languages, and accepts a custom sorting instruction.

Qwen3 Rerank ranks candidate documents against a query through `POST /v1/reranks` with the model id `qwen3-rerank`.

| | |
| --- | --- |
| Model id | `qwen3-rerank` |
| Provider | Alibaba Cloud |
| Category | Rerankers |
| Endpoint | `POST /v1/reranks` |

## Run

```bash
export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."   # https://platform.empiriolabs.ai/dashboard/api-keys
bash request.sh
pip install requests && python example.py
```

## cURL

[`request.sh`](request.sh)

```bash
#!/usr/bin/env bash
# Qwen3 Rerank, cURL
# https://empiriolabs.ai/models/qwen3-rerank
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/reranks \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-rerank",
    "query": "How do I rotate an API key?",
    "documents": ["Rotate keys from the dashboard.", "Billing is pay as you go."]
  }'
```

## Python

[`example.py`](example.py)

```python
"""Qwen3 Rerank, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/qwen3-rerank
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/reranks",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "qwen3-rerank",
        "query": "How do I rotate an API key?",
        "documents": ["Rotate keys from the dashboard.", "Billing is pay as you go."],
    },
)
print(response.json())
```

## Links

- [Qwen3 Rerank pricing and specs](https://empiriolabs.ai/models/qwen3-rerank)
- [Qwen3 Rerank API reference](https://docs.empiriolabs.ai/models/qwen3-rerank)
- [Try Qwen3 Rerank in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=qwen3-rerank)
