# GLM 5.3 Flash API examples

Natively multimodal flash model with a 1M token context, image and video input, always-on reasoning, native web search, and tool calling.

GLM 5.3 Flash serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `glm-5-3-flash`.

| | |
| --- | --- |
| Model id | `glm-5-3-flash` |
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
# GLM 5.3 Flash, cURL
# https://empiriolabs.ai/models/glm-5-3-flash
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-5-3-flash",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""GLM 5.3 Flash, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/glm-5-3-flash
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="glm-5-3-flash",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [GLM 5.3 Flash pricing and specs](https://empiriolabs.ai/models/glm-5-3-flash)
- [GLM 5.3 Flash API reference](https://docs.empiriolabs.ai/models/glm-5-3-flash)
- [Try GLM 5.3 Flash in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=glm-5-3-flash)

[All EmpirioLabs AI examples](../../README.md)
