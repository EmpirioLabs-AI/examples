# StepAudio 3 Chat API examples

Audio and text conversation model that reasons before answering, with function calling and JSON output.

StepAudio 3 Chat serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `stepaudio-3-chat`.

| | |
| --- | --- |
| Model id | `stepaudio-3-chat` |
| Provider | StepFun |
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
# StepAudio 3 Chat, cURL
# https://empiriolabs.ai/models/stepaudio-3-chat
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stepaudio-3-chat",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""StepAudio 3 Chat, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/stepaudio-3-chat
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="stepaudio-3-chat",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [StepAudio 3 Chat pricing and specs](https://empiriolabs.ai/models/stepaudio-3-chat)
- [StepAudio 3 Chat API reference](https://docs.empiriolabs.ai/models/stepaudio-3-chat)
- [Try StepAudio 3 Chat in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=stepaudio-3-chat)

[All EmpirioLabs AI examples](../../README.md)
