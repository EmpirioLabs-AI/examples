# Tavily Research API examples

Multi-search research assistant that explores a topic, analyzes sources, and produces a detailed research report with citations.

Tavily Research is served through `POST /v1/research` with the model id `tavily-research` and your EmpirioLabs API key.

| | |
| --- | --- |
| Model id | `tavily-research` |
| Provider | Tavily |
| Category | Research & Search |
| Endpoint | `POST /v1/research` |

## Run

```bash
eval "$(python ../../login.py)"   # sign in, or: export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."
bash request.sh
```

## cURL

[`request.sh`](request.sh)

```bash
#!/usr/bin/env bash
# Tavily Research, cURL
# https://empiriolabs.ai/models/tavily-research
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Sign in first with login.py at the repository root, or set an API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/research \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tavily-research",
    "prompt": "Your input here."
  }'
```

## Links

- [Tavily Research pricing and specs](https://empiriolabs.ai/models/tavily-research)
- [Tavily Research API reference](https://docs.empiriolabs.ai/models/tavily-research)
- [Try Tavily Research in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=tavily-research)

[All EmpirioLabs AI examples](../../README.md)
