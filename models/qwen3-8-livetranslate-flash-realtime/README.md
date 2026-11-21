# Qwen3.8 LiveTranslate Flash Realtime API examples

Simultaneous spoken translation over a WebSocket. Set the target language, then speak; the model replies in that language with text and audio.

Qwen3.8 LiveTranslate Flash Realtime is spoken translation over a WebSocket at `wss://api.empiriolabs.ai/v1/realtime?model=qwen3-8-livetranslate-flash-realtime`, not over the HTTP endpoints. Connect with the model id `qwen3-8-livetranslate-flash-realtime` and send your EmpirioLabs API key as an `Authorization: Bearer` header on the handshake. Set the target language with a session.update before you send audio. Audio travels both ways as base64 16-bit PCM. A browser cannot set headers on a WebSocket, so open this connection from your server and relay audio to the browser over your own socket.

| | |
| --- | --- |
| Model id | `qwen3-8-livetranslate-flash-realtime` |
| Provider | Alibaba Cloud |
| Category | Audio Generation |
| Endpoint | `WEBSOCKET /v1/realtime` |

## Run

```bash
eval "$(python ../../login.py)"   # sign in, or: export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."
pip install websockets && python realtime.py
```

## Python (websockets)

[`realtime.py`](realtime.py)

```python
"""Qwen3.8 LiveTranslate Flash Realtime, Python (websockets).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install websockets
https://empiriolabs.ai/models/qwen3-8-livetranslate-flash-realtime
"""

import asyncio, json, os, websockets

async def main():
    async with websockets.connect(
        "wss://api.empiriolabs.ai/v1/realtime?model=qwen3-8-livetranslate-flash-realtime",
        additional_headers=[
            ("Authorization", f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"),
        ],
        max_size=None,
    ) as ws:
        print(json.loads(await ws.recv())["type"])  # session.created

        import base64

        await ws.send(json.dumps({
            "type": "session.update",
            "session": {
                "voice": "Tina",
                "translation": {"language": "en"},
                "modalities": ["text", "audio"],
            },
        }))

        # 16-bit PCM microphone audio, base64 encoded, in small chunks.
        for chunk in read_microphone_chunks():
            await ws.send(json.dumps({
                "type": "input_audio_buffer.append",
                "audio": base64.b64encode(chunk).decode(),
            }))

        async for raw in ws:
            event = json.loads(raw)
            if event["type"] == "response.audio.delta":
                ...  # base64 audio chunk, append to your playback buffer
            elif event["type"] in ("response.audio_transcript.text", "response.text.text"):
                print(event.get("text") or "")
            elif event["type"] == "response.done":
                break

asyncio.run(main())
```

## Links

- [Qwen3.8 LiveTranslate Flash Realtime pricing and specs](https://empiriolabs.ai/models/qwen3-8-livetranslate-flash-realtime)
- [Qwen3.8 LiveTranslate Flash Realtime API reference](https://docs.empiriolabs.ai/models/qwen3-8-livetranslate-flash-realtime)

[All EmpirioLabs AI examples](../../README.md)
