# Perplexity Sonar Reasoning Pro API examples

Reasoning model that researches over several rounds of web search, chaining evidence across many sources before it answers, with inline citations.

Perplexity Sonar Reasoning Pro serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `perplexity-sonar-reasoning-pro`.

| | |
| --- | --- |
| Model id | `perplexity-sonar-reasoning-pro` |
| Provider | Perplexity |
| Category | Research & Search |
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
# Perplexity Sonar Reasoning Pro, cURL
# https://empiriolabs.ai/models/perplexity-sonar-reasoning-pro
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "perplexity-sonar-reasoning-pro",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Perplexity Sonar Reasoning Pro, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/perplexity-sonar-reasoning-pro
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="perplexity-sonar-reasoning-pro",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Perplexity Sonar Reasoning Pro pricing and specs](https://empiriolabs.ai/models/perplexity-sonar-reasoning-pro)
- [Perplexity Sonar Reasoning Pro API reference](https://docs.empiriolabs.ai/models/perplexity-sonar-reasoning-pro)
- [Try Perplexity Sonar Reasoning Pro in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=perplexity-sonar-reasoning-pro)

[All EmpirioLabs AI examples](../../README.md)
