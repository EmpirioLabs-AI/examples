"""Skylark Embedding Vision, Python (OpenAI SDK).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install openai
https://empiriolabs.ai/models/skylark-embedding-vision
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

embedding = client.embeddings.create(
    model="skylark-embedding-vision",
    input="The quick brown fox jumps over the lazy dog.",
)
print(embedding.data[0].embedding[:8])
