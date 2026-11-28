# Seed Live Interpretation 2.0 API examples

Simultaneous interpretation over a WebSocket: speech in, its translation out as text or as speech in the speaker's own voice, between Chinese or English and 46 languages.

Seed Live Interpretation 2.0 holds a live conversation over a WebSocket at `wss://api.empiriolabs.ai/v1/realtime?model=seed-live-interpretation-2-0`, not over the HTTP endpoints. Connect with the model id `seed-live-interpretation-2-0` and send your EmpirioLabs API key as an `Authorization: Bearer` header on the handshake. Audio travels both ways as base64 16-bit PCM. A browser cannot set headers on a WebSocket, so open this connection from your server and relay audio to the browser over your own socket.

| | |
| --- | --- |
| Model id | `seed-live-interpretation-2-0` |
| Provider | ByteDance |
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
"""Seed Live Interpretation 2.0, Python (websockets).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install websockets
https://empiriolabs.ai/models/seed-live-interpretation-2-0
"""

import asyncio, json, os, websockets

async def main():
    async with websockets.connect(
        "wss://api.empiriolabs.ai/v1/realtime?model=seed-live-interpretation-2-0",
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

- [Seed Live Interpretation 2.0 pricing and specs](https://empiriolabs.ai/models/seed-live-interpretation-2-0)
- [Seed Live Interpretation 2.0 API reference](https://docs.empiriolabs.ai/models/seed-live-interpretation-2-0)

[All EmpirioLabs AI examples](../../README.md)
