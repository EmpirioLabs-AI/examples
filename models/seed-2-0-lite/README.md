# Seed 2.0 Lite API examples

Balanced general-purpose model for high-frequency enterprise workloads: information processing, content, search, and data analysis.

Seed 2.0 Lite serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `seed-2-0-lite`.

| | |
| --- | --- |
| Model id | `seed-2-0-lite` |
| Provider | ByteDance |
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
# Seed 2.0 Lite, cURL
# https://empiriolabs.ai/models/seed-2-0-lite
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seed-2-0-lite",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Seed 2.0 Lite, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/seed-2-0-lite
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="seed-2-0-lite",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Seed 2.0 Lite pricing and specs](https://empiriolabs.ai/models/seed-2-0-lite)
- [Seed 2.0 Lite API reference](https://docs.empiriolabs.ai/models/seed-2-0-lite)
- [Try Seed 2.0 Lite in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=seed-2-0-lite)

[All EmpirioLabs AI examples](../../README.md)
