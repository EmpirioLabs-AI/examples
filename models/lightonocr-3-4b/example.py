"""LightOnOCR-3 4B, Python.

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
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
