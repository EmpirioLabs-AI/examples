# Kimi K2.7 Code API examples

Kimi K2.7 Code is Moonshot's trillion-parameter agentic coding model with 256K context, always-on reasoning, and text, image, and video inputs.

Kimi K2.7 Code serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `kimi-k2-7-code`.

| | |
| --- | --- |
| Model id | `kimi-k2-7-code` |
| Provider | Moonshot AI |
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
# Kimi K2.7 Code, cURL
# https://empiriolabs.ai/models/kimi-k2-7-code
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k2-7-code",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Kimi K2.7 Code, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/kimi-k2-7-code
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="kimi-k2-7-code",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Kimi K2.7 Code pricing and specs](https://empiriolabs.ai/models/kimi-k2-7-code)
- [Kimi K2.7 Code API reference](https://docs.empiriolabs.ai/models/kimi-k2-7-code)
- [Try Kimi K2.7 Code in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=kimi-k2-7-code)

[All EmpirioLabs AI examples](../../README.md)
