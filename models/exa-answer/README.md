# Exa Answer API examples

Quick LLM-style answer to a natural-language question, grounded in fresh Exa web search results with inline citations and source links.

Exa Answer serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `exa-answer`.

| | |
| --- | --- |
| Model id | `exa-answer` |
| Provider | Exa |
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
# Exa Answer, cURL
# https://empiriolabs.ai/models/exa-answer
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "exa-answer",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Exa Answer, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/exa-answer
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="exa-answer",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Exa Answer pricing and specs](https://empiriolabs.ai/models/exa-answer)
- [Exa Answer API reference](https://docs.empiriolabs.ai/models/exa-answer)
- [Try Exa Answer in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=exa-answer)

[All EmpirioLabs AI examples](../../README.md)
