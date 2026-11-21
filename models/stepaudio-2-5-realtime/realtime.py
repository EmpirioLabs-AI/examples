"""StepAudio 2.5 Realtime, Python (websockets).

Set EMPIRIOLABS_API_KEY to your API key first: https://platform.empiriolabs.ai/dashboard/api-keys
Requires: pip install websockets
https://empiriolabs.ai/models/stepaudio-2-5-realtime
"""

import asyncio, json, os, websockets

async def main():
    async with websockets.connect(
        "wss://api.empiriolabs.ai/v1/realtime?model=stepaudio-2-5-realtime",
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
