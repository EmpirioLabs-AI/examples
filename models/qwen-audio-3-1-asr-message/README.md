# Qwen Audio 3.1 ASR Message API examples

Transcription tuned for voice messages and voice input over a socket, returning each utterance as one complete transcript when the speaker pauses.

Qwen Audio 3.1 ASR Message transcribes a live audio stream over a WebSocket at `wss://api.empiriolabs.ai/v1/realtime?model=qwen-audio-3-1-asr-message`, not over the HTTP endpoints. Connect with the model id `qwen-audio-3-1-asr-message` and send your EmpirioLabs API key as an `Authorization: Bearer` header on the handshake. Append base64 16-bit PCM audio and read transcript events back while the speaker is still talking. A browser cannot set headers on a WebSocket, so open this connection from your server and relay audio to the browser over your own socket.

| | |
| --- | --- |
| Model id | `qwen-audio-3-1-asr-message` |
| Provider | Alibaba Cloud |
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
"""Qwen Audio 3.1 ASR Message, Python (websockets).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install websockets
https://empiriolabs.ai/models/qwen-audio-3-1-asr-message
"""

import asyncio, json, os, websockets

async def main():
    async with websockets.connect(
        "wss://api.empiriolabs.ai/v1/realtime?model=qwen-audio-3-1-asr-message",
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

- [Qwen Audio 3.1 ASR Message pricing and specs](https://empiriolabs.ai/models/qwen-audio-3-1-asr-message)
- [Qwen Audio 3.1 ASR Message API reference](https://docs.empiriolabs.ai/models/qwen-audio-3-1-asr-message)

[All EmpirioLabs AI examples](../../README.md)
