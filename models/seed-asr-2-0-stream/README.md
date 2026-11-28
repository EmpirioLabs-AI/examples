# Seed ASR 2.0 Stream API examples

Live transcription over a WebSocket in 67 languages: Chinese and English arrive word by word while the speaker talks, other languages in passages, priced per hour of audio.

Seed ASR 2.0 Stream transcribes a live audio stream over a WebSocket at `wss://api.empiriolabs.ai/v1/realtime?model=seed-asr-2-0-stream`, not over the HTTP endpoints. Connect with the model id `seed-asr-2-0-stream` and send your EmpirioLabs API key as an `Authorization: Bearer` header on the handshake. Append base64 16-bit PCM audio and read transcript events back while the speaker is still talking. A browser cannot set headers on a WebSocket, so open this connection from your server and relay audio to the browser over your own socket.

| | |
| --- | --- |
| Model id | `seed-asr-2-0-stream` |
| Provider | ByteDance |
| Category | Transcription |
| Endpoint | `WEBSOCKET /v1/realtime` |

## Run

```bash
eval "$(python ../../login.py)"   # sign in, or: export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."
pip install websockets && python realtime.py
```

## Python (websockets)

[`realtime.py`](realtime.py)

```python
"""Seed ASR 2.0 Stream, Python (websockets).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install websockets
https://empiriolabs.ai/models/seed-asr-2-0-stream
"""

import asyncio, json, os, websockets

async def main():
    async with websockets.connect(
        "wss://api.empiriolabs.ai/v1/realtime?model=seed-asr-2-0-stream",
        additional_headers=[
            ("Authorization", f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"),
        ],
        max_size=None,
    ) as ws:
        print(json.loads(await ws.recv())["type"])  # session.created

        import base64

        # 16-bit PCM microphone audio, base64 encoded, in small chunks.
        for chunk in read_microphone_chunks():
            await ws.send(json.dumps({
                "type": "input_audio_buffer.append",
                "audio": base64.b64encode(chunk).decode(),
            }))

        await ws.send(json.dumps({"type": "input_audio_buffer.commit"}))

        async for raw in ws:
            event = json.loads(raw)
            if event["type"].endswith("input_audio_transcription.delta"):
                # "text" is settled transcript; "stash" is still in progress.
                if event.get("text"):
                    print(event["text"], end="", flush=True)

asyncio.run(main())
```

## Links

- [Seed ASR 2.0 Stream pricing and specs](https://empiriolabs.ai/models/seed-asr-2-0-stream)
- [Seed ASR 2.0 Stream API reference](https://docs.empiriolabs.ai/models/seed-asr-2-0-stream)

[All EmpirioLabs AI examples](../../README.md)
