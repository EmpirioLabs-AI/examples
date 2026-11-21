# Fugu Ultra v1.1 API examples

Updated multi-agent conductor for hard reasoning, coding, and research, with distinct max effort, 1M context, image input, and web search.

Fugu Ultra v1.1 serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `fugu-ultra-v1-1`.

| | |
| --- | --- |
| Model id | `fugu-ultra-v1-1` |
| Provider | Sakana AI |
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
# Fugu Ultra v1.1, cURL
# https://empiriolabs.ai/models/fugu-ultra-v1-1
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "fugu-ultra-v1-1",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Fugu Ultra v1.1, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/fugu-ultra-v1-1
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="fugu-ultra-v1-1",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Fugu Ultra v1.1 pricing and specs](https://empiriolabs.ai/models/fugu-ultra-v1-1)
- [Fugu Ultra v1.1 API reference](https://docs.empiriolabs.ai/models/fugu-ultra-v1-1)
- [Try Fugu Ultra v1.1 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=fugu-ultra-v1-1)
