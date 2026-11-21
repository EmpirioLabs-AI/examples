# Fugu Ultra v2.0 API examples

Flagship multi-agent conductor for the hardest reasoning, coding, and research work, with 1M context, image input, and web search.

Fugu Ultra v2.0 serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `fugu-ultra-v2-0`.

| | |
| --- | --- |
| Model id | `fugu-ultra-v2-0` |
| Provider | Sakana AI |
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
# Fugu Ultra v2.0, cURL
# https://empiriolabs.ai/models/fugu-ultra-v2-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "fugu-ultra-v2-0",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Fugu Ultra v2.0, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/fugu-ultra-v2-0
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="fugu-ultra-v2-0",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Fugu Ultra v2.0 pricing and specs](https://empiriolabs.ai/models/fugu-ultra-v2-0)
- [Fugu Ultra v2.0 API reference](https://docs.empiriolabs.ai/models/fugu-ultra-v2-0)
- [Try Fugu Ultra v2.0 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=fugu-ultra-v2-0)

[All EmpirioLabs AI examples](../../README.md)
