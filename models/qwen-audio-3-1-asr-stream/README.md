# Qwen Audio 3.1 ASR Stream API examples

Live transcription over a socket, streaming partial words while the speaker talks and a settled sentence at each pause, priced per token.

Qwen Audio 3.1 ASR Stream transcribes a live audio stream over a WebSocket at `wss://api.empiriolabs.ai/v1/realtime?model=qwen-audio-3-1-asr-stream`, not over the HTTP endpoints. Connect with the model id `qwen-audio-3-1-asr-stream` and send your EmpirioLabs API key as an `Authorization: Bearer` header on the handshake. Append base64 16-bit PCM audio and read transcript events back while the speaker is still talking. A browser cannot set headers on a WebSocket, so open this connection from your server and relay audio to the browser over your own socket.

| | |
| --- | --- |
| Model id | `qwen-audio-3-1-asr-stream` |
| Provider | Alibaba Cloud |
| Category | Transcription |
| Endpoint | `WEBSOCKET /v1/realtime` |

## Run

```bash
export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."   # https://platform.empiriolabs.ai/dashboard/api-keys
pip install websockets && python realtime.py
```

## Python (websockets)

[`realtime.py`](realtime.py)

```python
"""Qwen Audio 3.1 ASR Stream, Python (websockets).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install websockets
https://empiriolabs.ai/models/qwen-audio-3-1-asr-stream
"""

import asyncio, json, os, websockets

async def main():
    async with websockets.connect(
        "wss://api.empiriolabs.ai/v1/realtime?model=qwen-audio-3-1-asr-stream",
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

- [Qwen Audio 3.1 ASR Stream pricing and specs](https://empiriolabs.ai/models/qwen-audio-3-1-asr-stream)
- [Qwen Audio 3.1 ASR Stream API reference](https://docs.empiriolabs.ai/models/qwen-audio-3-1-asr-stream)

[All EmpirioLabs AI examples](../../README.md)
