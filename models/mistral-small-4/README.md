# Mistral Small 4 API examples

Hybrid model unifying Instruct, Reasoning (Magistral), and Devstral families: 40% lower completion time and 3x throughput vs Small 3.

Mistral Small 4 serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `mistral-small-4`.

| | |
| --- | --- |
| Model id | `mistral-small-4` |
| Provider | Mistral AI |
| Category | Text Generation |
| Endpoint | `POST /v1/chat/completions` |

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
# Mistral Small 4, cURL
# https://empiriolabs.ai/models/mistral-small-4
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mistral-small-4",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Mistral Small 4, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/mistral-small-4
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="mistral-small-4",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Mistral Small 4 pricing and specs](https://empiriolabs.ai/models/mistral-small-4)
- [Mistral Small 4 API reference](https://docs.empiriolabs.ai/models/mistral-small-4)
- [Try Mistral Small 4 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=mistral-small-4)

[All EmpirioLabs AI examples](../../README.md)
