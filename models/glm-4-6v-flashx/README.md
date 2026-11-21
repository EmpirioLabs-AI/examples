# GLM 4.6V FlashX API examples

High-speed GLM-4.6V vision model for image, video, file, and text understanding, with 128K context and native function calling.

GLM 4.6V FlashX serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `glm-4-6v-flashx`.

| | |
| --- | --- |
| Model id | `glm-4-6v-flashx` |
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
# GLM 4.6V FlashX, cURL
# https://empiriolabs.ai/models/glm-4-6v-flashx
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-4-6v-flashx",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""GLM 4.6V FlashX, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/glm-4-6v-flashx
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="glm-4-6v-flashx",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [GLM 4.6V FlashX pricing and specs](https://empiriolabs.ai/models/glm-4-6v-flashx)
- [GLM 4.6V FlashX API reference](https://docs.empiriolabs.ai/models/glm-4-6v-flashx)
- [Try GLM 4.6V FlashX in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=glm-4-6v-flashx)
