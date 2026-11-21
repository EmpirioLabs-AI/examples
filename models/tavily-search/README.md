# Tavily Search API examples

Web search with crawl, extract, and URL mapping for fast, structured retrieval across pages and domains for downstream pipelines.

Tavily Search answers live queries through `POST /v1/search`. Send the search query with the model id `tavily-search` and read structured results from the response.

| | |
| --- | --- |
| Model id | `tavily-search` |
| Provider | Tavily |
| Category | Research & Search |
| Endpoint | `POST /v1/search` |

## Run

```bash
eval "$(python ../../login.py)"   # sign in, or: export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."
bash request.sh
pip install requests && python example.py
```

## cURL

[`request.sh`](request.sh)

```bash
#!/usr/bin/env bash
# Tavily Search, cURL
# https://empiriolabs.ai/models/tavily-search
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/search \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tavily-search",
    "query": "latest developments in solid-state batteries"
  }'
```

## Python

[`example.py`](example.py)

```python
"""Tavily Search, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install requests
https://empiriolabs.ai/models/tavily-search
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/search",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "tavily-search",
        "query": "latest developments in solid-state batteries",
    },
)
print(response.json())
```

## Links

- [Tavily Search pricing and specs](https://empiriolabs.ai/models/tavily-search)
- [Tavily Search API reference](https://docs.empiriolabs.ai/models/tavily-search)
- [Try Tavily Search in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=tavily-search)

[All EmpirioLabs AI examples](../../README.md)
