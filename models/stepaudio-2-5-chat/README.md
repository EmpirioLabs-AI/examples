# StepAudio 2.5 Chat API examples

StepFun audio and text conversation model with text output and paralinguistic understanding.

StepAudio 2.5 Chat serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `stepaudio-2-5-chat`.

| | |
| --- | --- |
| Model id | `stepaudio-2-5-chat` |
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
# StepAudio 2.5 Chat, cURL
# https://empiriolabs.ai/models/stepaudio-2-5-chat
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-2-5-chat",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""StepAudio 2.5 Chat, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/stepaudio-2-5-chat
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="stepaudio-2-5-chat",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [StepAudio 2.5 Chat pricing and specs](https://empiriolabs.ai/models/stepaudio-2-5-chat)
- [StepAudio 2.5 Chat API reference](https://docs.empiriolabs.ai/models/stepaudio-2-5-chat)
- [Try StepAudio 2.5 Chat in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=stepaudio-2-5-chat)

[All EmpirioLabs AI examples](../../README.md)
