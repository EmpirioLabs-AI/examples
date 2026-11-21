"""Gemini 2.5 Flash TTS, Python.

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install requests
https://empiriolabs.ai/models/gemini-2-5-flash-tts
"""

import os
import requests

response = requests.post(
    "https://api.empiriolabs.ai/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"},
    json={"model": "gemini-2-5-flash-tts", "input": "Welcome to EmpirioLabs."},
)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
