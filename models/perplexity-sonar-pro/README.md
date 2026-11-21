# Perplexity Sonar Pro API examples

Search-grounded model with double the citations and a larger context window, tuned for complex queries needing in-depth, nuanced answers.

Perplexity Sonar Pro serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `perplexity-sonar-pro`.

| | |
| --- | --- |
| Model id | `perplexity-sonar-pro` |
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
# Perplexity Sonar Pro, cURL
# https://empiriolabs.ai/models/perplexity-sonar-pro
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "perplexity-sonar-pro",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Perplexity Sonar Pro, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/perplexity-sonar-pro
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="perplexity-sonar-pro",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Perplexity Sonar Pro pricing and specs](https://empiriolabs.ai/models/perplexity-sonar-pro)
- [Perplexity Sonar Pro API reference](https://docs.empiriolabs.ai/models/perplexity-sonar-pro)
- [Try Perplexity Sonar Pro in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=perplexity-sonar-pro)

[All EmpirioLabs AI examples](../../README.md)
