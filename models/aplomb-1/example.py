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
