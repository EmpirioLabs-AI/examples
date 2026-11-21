# Qwen3.5 Omni Flash Realtime API examples

Speech in, speech out, over one socket, with separate text and audio token rates and per-turn billing.

Qwen3.5 Omni Flash Realtime holds a live conversation over a WebSocket at `wss://api.empiriolabs.ai/v1/realtime?model=qwen3-5-omni-flash-realtime`, not over the HTTP endpoints. Connect with the model id `qwen3-5-omni-flash-realtime` and send your EmpirioLabs API key as an `Authorization: Bearer` header on the handshake. Audio travels both ways as base64 16-bit PCM. A browser cannot set headers on a WebSocket, so open this connection from your server and relay audio to the browser over your own socket.

| | |
| --- | --- |
| Model id | `qwen3-5-omni-flash-realtime` |
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
"""Qwen3.5 Omni Flash Realtime, Python (websockets).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install websockets
https://empiriolabs.ai/models/qwen3-5-omni-flash-realtime
"""

import asyncio, json, os, websockets

async def main():
    async with websockets.connect(
        "wss://api.empiriolabs.ai/v1/realtime?model=qwen3-5-omni-flash-realtime",
        additional_headers=[
            ("Authorization", f"Bearer {os.environ['EMPIRIOLABS_API_KEY']}"),
        ],
        max_size=None,
    ) as ws:
        print(json.loads(await ws.recv())["type"])  # session.created

        await ws.send(json.dumps({
            "type": "conversation.item.create",
            "item": {
                "type": "message",
                "role": "user",
                "content": [{"type": "input_text", "text": "Say hello."}],
            },
        }))
        await ws.send(json.dumps({"type": "response.create"}))

        async for raw in ws:
            event = json.loads(raw)
            if event["type"] == "response.audio.delta":
                ...  # base64 audio chunk, append to your playback buffer
            elif event["type"] == "response.done":
                break

asyncio.run(main())
```

## Links

- [Qwen3.5 Omni Flash Realtime pricing and specs](https://empiriolabs.ai/models/qwen3-5-omni-flash-realtime)
- [Qwen3.5 Omni Flash Realtime API reference](https://docs.empiriolabs.ai/models/qwen3-5-omni-flash-realtime)

[All EmpirioLabs AI examples](../../README.md)
