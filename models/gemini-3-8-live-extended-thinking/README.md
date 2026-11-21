# Gemini 3.8 Live Extended Thinking API examples

Voice conversation that keeps talking while it reasons in the background, with 30 voices, live video input, tool calling, and adjustable reasoning effort.

Gemini 3.8 Live Extended Thinking holds a live conversation over a WebSocket at `wss://api.empiriolabs.ai/v1/realtime?model=gemini-3-8-live-extended-thinking`, not over the HTTP endpoints. Connect with the model id `gemini-3-8-live-extended-thinking` and send your EmpirioLabs API key as an `Authorization: Bearer` header on the handshake. Audio travels both ways as base64 16-bit PCM. A browser cannot set headers on a WebSocket, so open this connection from your server and relay audio to the browser over your own socket.

| | |
| --- | --- |
| Model id | `gemini-3-8-live-extended-thinking` |
| Provider | Google |
| Category | Audio Generation |
| Endpoint | `WEBSOCKET /v1/realtime` |

## Run

```bash
export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."   # https://platform.empiriolabs.ai/dashboard/api-keys
pip install websockets && python realtime.py
```

## Python (websockets)

[`realtime.py`](realtime.py)

```python
"""Gemini 3.8 Live Extended Thinking, Python (websockets).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install websockets
https://empiriolabs.ai/models/gemini-3-8-live-extended-thinking
"""

import asyncio, json, os, websockets

async def main():
    async with websockets.connect(
        "wss://api.empiriolabs.ai/v1/realtime?model=gemini-3-8-live-extended-thinking",
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

- [Gemini 3.8 Live Extended Thinking pricing and specs](https://empiriolabs.ai/models/gemini-3-8-live-extended-thinking)
- [Gemini 3.8 Live Extended Thinking API reference](https://docs.empiriolabs.ai/models/gemini-3-8-live-extended-thinking)

[All EmpirioLabs AI examples](../../README.md)
