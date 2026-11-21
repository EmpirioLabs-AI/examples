# Step 3.5 Flash 2603 API examples

Agent-optimized Step 3.5 Flash variant with low and high reasoning effort modes.

Step 3.5 Flash 2603 serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `step-3-5-flash-2603`.

| | |
| --- | --- |
| Model id | `step-3-5-flash-2603` |
| Provider | StepFun |
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
# Step 3.5 Flash 2603, cURL
# https://empiriolabs.ai/models/step-3-5-flash-2603
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "step-3-5-flash-2603",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""Step 3.5 Flash 2603, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/step-3-5-flash-2603
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="step-3-5-flash-2603",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [Step 3.5 Flash 2603 pricing and specs](https://empiriolabs.ai/models/step-3-5-flash-2603)
- [Step 3.5 Flash 2603 API reference](https://docs.empiriolabs.ai/models/step-3-5-flash-2603)
- [Try Step 3.5 Flash 2603 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=step-3-5-flash-2603)

[All EmpirioLabs AI examples](../../README.md)
