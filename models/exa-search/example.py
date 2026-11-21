"""Exa Search, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/exa-search
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/search",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={
        "model": "exa-search",
        "query": "latest developments in solid-state batteries",
    },
)
print(response.json())
