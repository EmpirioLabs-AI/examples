# Exa Search API examples

Web search engine for finding pages, retrieving similar pages, crawling, and dedicated code search across the open web for AI agents.

Exa Search answers live queries through `POST /v1/search`. Send the search query with the model id `exa-search` and read structured results from the response.

| | |
| --- | --- |
| Model id | `exa-search` |
| Provider | Exa |
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
# Exa Search, cURL
# https://empiriolabs.ai/models/exa-search
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/search \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "exa-search",
    "query": "latest developments in solid-state batteries"
  }'
```

## Python

[`example.py`](example.py)

```python
"""Exa Search, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/exa-search
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/search",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "exa-search",
        "query": "latest developments in solid-state batteries",
    },
)
print(response.json())
```

## Links

- [Exa Search pricing and specs](https://empiriolabs.ai/models/exa-search)
- [Exa Search API reference](https://docs.empiriolabs.ai/models/exa-search)
- [Try Exa Search in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=exa-search)

[All EmpirioLabs AI examples](../../README.md)
