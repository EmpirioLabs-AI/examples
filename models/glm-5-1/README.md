# GLM 5.1 API examples

Long-context Zhipu AI reasoning model with 202K context, 128K output, tool calling, structured output, and cache support.

GLM 5.1 serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `glm-5-1`.

| | |
| --- | --- |
| Model id | `glm-5-1` |
| Provider | Z.ai |
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
# GLM 5.1, cURL
# https://empiriolabs.ai/models/glm-5-1
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-5-1",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""GLM 5.1, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/glm-5-1
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="glm-5-1",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [GLM 5.1 pricing and specs](https://empiriolabs.ai/models/glm-5-1)
- [GLM 5.1 API reference](https://docs.empiriolabs.ai/models/glm-5-1)
- [Try GLM 5.1 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=glm-5-1)

[All EmpirioLabs AI examples](../../README.md)
