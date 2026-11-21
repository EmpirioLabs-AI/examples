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
