# Aplomb 1 API examples

Answers yes/no, choice, score and tool questions about text, JSON, images, video and audio in up to 1M tokens, and can tell when the input lacks the answer.

Aplomb 1 answers questions about your content through `POST /v1/decisions`. Send the content in `state` and your questions in `questions` with the model id `aplomb-1`. Each answer returns probabilities and a confidence value instead of generated text.

| | |
| --- | --- |
| Model id | `aplomb-1` |
| Provider | EmpirioLabs |
| Category | Decision Models |
| Endpoint | `POST /v1/decisions` |

## Run

```bash
export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."   # https://platform.empiriolabs.ai/dashboard/api-keys
bash request.sh
pip install requests && python example.py
```

## cURL

[`request.sh`](request.sh)

```bash
#!/usr/bin/env bash
# Aplomb 1, cURL
# https://empiriolabs.ai/models/aplomb-1
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/decisions \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "aplomb-1",
    "state": "I was charged twice for my subscription this month. Please refund the duplicate charge today.",
    "questions": {
      "is_urgent": {"type": "noul", "instructions": "Does the customer need a resolution today?"},
      "department": {
        "type": "choice",
        "instructions": "Which team should handle this message?",
        "criteria": {"billing": null, "technical": null, "sales": null}
      }
    }
  }'
```

## Python

[`example.py`](example.py)

```python
"""Aplomb 1, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/aplomb-1
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/decisions",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "aplomb-1",
        "state": "I was charged twice for my subscription this month. Please refund the duplicate charge today.",
        "questions": {
            "is_urgent": {"type": "noul", "instructions": "Does the customer need a resolution today?"},
            "department": {
                "type": "choice",
                "instructions": "Which team should handle this message?",
                "criteria": {"billing": None, "technical": None, "sales": None},
            },
        },
    },
)
answers = response.json()["answers"]
print(answers["is_urgent"]["noul"], answers["department"]["choice"])
```

## Links

- [Aplomb 1 pricing and specs](https://empiriolabs.ai/models/aplomb-1)
- [Aplomb 1 API reference](https://docs.empiriolabs.ai/models/aplomb-1)
- [Try Aplomb 1 in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=aplomb-1)
