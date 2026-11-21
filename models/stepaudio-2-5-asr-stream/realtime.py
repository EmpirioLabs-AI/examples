"""StepAudio 2.5 ASR Stream, Python (websockets).

Sign in first with login.py at the repository root, or set EMPIRIOLABS_API_KEY to an API key from
https://platform.empiriolabs.ai/dashboard/api-keys.
Requires: pip install websockets
https://empiriolabs.ai/models/stepaudio-2-5-asr-stream
"""

import asyncio, json, os, websockets

async def main():
    async with websockets.connect(
        "wss://api.empiriolabs.ai/v1/realtime?model=stepaudio-2-5-asr-stream",
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
