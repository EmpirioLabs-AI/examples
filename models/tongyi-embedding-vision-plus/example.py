"""Tongyi Embedding Vision Plus, Python (OpenAI SDK).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install openai
https://empiriolabs.ai/models/tongyi-embedding-vision-plus
"""

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.empiriolabs.ai/v1",
    api_key=os.environ["EMPIRIOLABS_API_KEY"],
)

embedding = client.embeddings.create(
    model="tongyi-embedding-vision-plus",
    input="The quick brown fox jumps over the lazy dog.",
)
print(embedding.data[0].embedding[:8])
