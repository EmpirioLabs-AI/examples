"""Muse Glimmer 30B, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/muse-glimmer-30b
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

response = client.chat.completions.create(
    model="muse-glimmer-30b",
    messages=[{"role": "user", "content": "Write a haiku about the ocean."}],
)
print(response.choices[0].message.content)
