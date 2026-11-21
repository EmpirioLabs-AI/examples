# DeepSeek V4 Pro 0813 API examples

Official 0813 Pro release with major gains across coding, repository work, tool use, and agent tasks, plus hybrid thinking and a 1M context window.

DeepSeek V4 Pro 0813 serves the OpenAI-compatible Chat Completions API. Point any OpenAI SDK at `https://api.empiriolabs.ai/v1` with your EmpirioLabs API key and use the model id `deepseek-v4-pro-0813`.

| | |
| --- | --- |
| Model id | `deepseek-v4-pro-0813` |
| Provider | DeepSeek |
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
# DeepSeek V4 Pro 0813, cURL
# https://empiriolabs.ai/models/deepseek-v4-pro-0813
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/chat/completions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-pro-0813",
    "messages": [
      {"role": "user", "content": "Write a haiku about the ocean."}
    ]
  }'
```

## Python (OpenAI SDK)

[`example.py`](example.py)

```python
"""DeepSeek V4 Pro 0813, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/deepseek-v4-pro-0813
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="deepseek-v4-pro-0813",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
```

## Links

- [DeepSeek V4 Pro 0813 pricing and specs](https://empiriolabs.ai/models/deepseek-v4-pro-0813)
- [DeepSeek V4 Pro 0813 API reference](https://docs.empiriolabs.ai/models/deepseek-v4-pro-0813)
- [Try DeepSeek V4 Pro 0813 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=deepseek-v4-pro-0813)
