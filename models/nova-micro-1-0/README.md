# Nova Micro 1.0 API examples

Text-only foundation model tuned for ultra-low latency and cost on 128K context. Strong for summarization, translation, and chat with 44% cache discount.

Nova Micro 1.0 serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `nova-micro-1-0`.

| | |
| --- | --- |
| Model id | `nova-micro-1-0` |
| Provider | Amazon |
| Category | Text Generation |
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
# Nova Micro 1.0, cURL
# https://empiriolabs.ai/models/nova-micro-1-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nova-micro-1-0",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Nova Micro 1.0, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/nova-micro-1-0
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="nova-micro-1-0",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Nova Micro 1.0 pricing and specs](https://empiriolabs.ai/models/nova-micro-1-0)
- [Nova Micro 1.0 API reference](https://docs.empiriolabs.ai/models/nova-micro-1-0)
- [Try Nova Micro 1.0 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=nova-micro-1-0)

[All EmpirioLabs AI examples](../../README.md)
