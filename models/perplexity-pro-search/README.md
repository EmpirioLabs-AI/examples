# Perplexity Pro Search API examples

Sonar Pro as an agentic researcher: chains web searches, fetches full pages, and streams live reasoning, adapting strategy for complex queries.

Perplexity Pro Search serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `perplexity-pro-search`.

| | |
| --- | --- |
| Model id | `perplexity-pro-search` |
| Provider | Perplexity |
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
# Perplexity Pro Search, cURL
# https://empiriolabs.ai/models/perplexity-pro-search
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "perplexity-pro-search",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Perplexity Pro Search, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/perplexity-pro-search
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="perplexity-pro-search",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Perplexity Pro Search pricing and specs](https://empiriolabs.ai/models/perplexity-pro-search)
- [Perplexity Pro Search API reference](https://docs.empiriolabs.ai/models/perplexity-pro-search)
- [Try Perplexity Pro Search in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=perplexity-pro-search)

[All EmpirioLabs AI examples](../../README.md)
