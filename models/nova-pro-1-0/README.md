# Nova Pro 1.0 API examples

Multimodal foundation model balancing accuracy, speed, and cost for text, images, and video on 300K context (up to ~30 min video).

Nova Pro 1.0 serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `nova-pro-1-0`.

| | |
| --- | --- |
| Model id | `nova-pro-1-0` |
| Provider | Amazon |
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
# Nova Pro 1.0, cURL
# https://empiriolabs.ai/models/nova-pro-1-0
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nova-pro-1-0",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Nova Pro 1.0, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/nova-pro-1-0
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="nova-pro-1-0",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Nova Pro 1.0 pricing and specs](https://empiriolabs.ai/models/nova-pro-1-0)
- [Nova Pro 1.0 API reference](https://docs.empiriolabs.ai/models/nova-pro-1-0)
- [Try Nova Pro 1.0 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=nova-pro-1-0)

[All EmpirioLabs AI examples](../../README.md)
