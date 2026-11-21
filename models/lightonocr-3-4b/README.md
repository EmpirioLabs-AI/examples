# LightOnOCR-3 4B API examples

Document OCR that reads PDFs and images into structured Markdown, page by page, with tables, math, charts, image regions, and layout.

LightOnOCR-3 4B reads PDFs and images through POST /v1/ocr and returns each page as Markdown. Send the PDF's URL in document with the model id lightonocr-3-4b, and list zero-based page numbers in pages to process only those pages. An image works the same way with {"type": "image_url", "image_url": "https://..."}, and either URL can be a base64 data URI. The response lists each page in pages with its index, markdown, images, tables, and dimensions; usage_info.pages_processed counts the pages processed. A request still running after a few minutes returns a job_id to poll at GET /v1/jobs/{job_id}, and a Prefer: respond-async header asks for the job id at once.

| | |
| --- | --- |
| Model id | `lightonocr-3-4b` |
| Provider | LightOn |
| Category | Document OCR |
| Endpoint | `POST /v1/ocr` |

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
# LightOnOCR-3 4B, cURL
# https://empiriolabs.ai/models/lightonocr-3-4b
set -euo pipefail
: "${EMPIRIOLABS_API_KEY:?Set EMPIRIOLABS_API_KEY to your API key from https://platform.empiriolabs.ai/dashboard/api-keys}"

curl https://api.empiriolabs.ai/v1/ocr \
  -H "Authorization: Bearer $EMPIRIOLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lightonocr-3-4b",
    "document": {
      "type": "document_url",
      "document_url": "https://arxiv.org/pdf/2412.13663"
    },
    "pages": [0, 1],
    "include_image_base64": false
  }'
```

## Python

[`example.py`](example.py)

```python
"""LightOnOCR-3 4B, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/lightonocr-3-4b
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/ocr",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "lightonocr-3-4b",
        "document": {
            "type": "document_url",
            "document_url": "https://arxiv.org/pdf/2412.13663",
        },
        "pages": [0, 1],
        "include_image_base64": False,
    },
)
result = response.json()
for page in result["pages"]:  # index, markdown, images, tables, dimensions
    print(page["index"], page["markdown"][:200])
print(result["usage_info"]["pages_processed"])
```

## Links

- [LightOnOCR-3 4B pricing and specs](https://empiriolabs.ai/models/lightonocr-3-4b)
- [LightOnOCR-3 4B API reference](https://docs.empiriolabs.ai/models/lightonocr-3-4b)
- [Try LightOnOCR-3 4B in the Playground](https://platform.empiriolabs.ai/dashboard/playground?model=lightonocr-3-4b)
