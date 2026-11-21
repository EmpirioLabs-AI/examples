# Fugu Max API examples

Cost-efficient multi-agent conductor that assembles a right-sized expert team per task, with 1M context, image input, and web search.

Fugu Max serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `fugu-max`.

| | |
| --- | --- |
| Model id | `fugu-max` |
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
# Fugu Max, cURL
# https://empiriolabs.ai/models/fugu-max
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "fugu-max",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Fugu Max, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/fugu-max
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="fugu-max",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Fugu Max pricing and specs](https://empiriolabs.ai/models/fugu-max)
- [Fugu Max API reference](https://docs.empiriolabs.ai/models/fugu-max)
- [Try Fugu Max in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=fugu-max)
