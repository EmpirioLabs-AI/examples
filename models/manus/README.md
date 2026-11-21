# Manus API examples

Autonomous AI agent that turns a high-level prompt into subtasks, calls tools and APIs, and delivers end-to-end results without manual orchestration.

Manus is served through `POST /v1/agents/run` with the model id `manus` and your EmpirioLabs API key.

| | |
| --- | --- |
| Model id | `manus` |
| Provider | Manus |
| Category | Tools & Agents |
| Endpoint | `POST /v1/agents/run` |

## Run

```bash
export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."   # https://platform.empiriolabs.ai/dashboard/api-keys
bash request.sh
```

## cURL

[`request.sh`](request.sh)

```bash
#!/usr/bin/env bash
# Manus, cURL
# https://empiriolabs.ai/models/manus
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/agents/run \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "manus",
    "prompt": "Your input here."
  }'
```

## Links

- [Manus pricing and specs](https://empiriolabs.ai/models/manus)
- [Manus API reference](https://docs.empiriolabs.ai/models/manus)
- [Try Manus in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=manus)
