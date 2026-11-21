# Perplexity Search API examples

Real-time web search with filtering by domain, language, date, and more. Returns search results, not LLM responses; no file uploads.

Perplexity Search answers live queries through `POST /v1/search`. Send the search query with the model id `perplexity-search` and read structured results from the response.

| | |
| --- | --- |
| Model id | `perplexity-search` |
| Provider | Perplexity |
| Category | Research & Search |
| Endpoint | `POST /v1/search` |

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
# Perplexity Search, cURL
# https://empiriolabs.ai/models/perplexity-search
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/search \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "perplexity-search",
    "query": "latest developments in solid-state batteries"
  }'
```

## Python

[`example.py`](example.py)

```python
"""Perplexity Search, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/perplexity-search
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/search",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "perplexity-search",
        "query": "latest developments in solid-state batteries",
    },
)
print(response.json())
```

## Links

- [Perplexity Search pricing and specs](https://empiriolabs.ai/models/perplexity-search)
- [Perplexity Search API reference](https://docs.empiriolabs.ai/models/perplexity-search)
- [Try Perplexity Search in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=perplexity-search)
