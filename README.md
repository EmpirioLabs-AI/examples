<div align="center">

<a href="https://empiriolabs.ai">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/EmpirioLabs-AI/assets/main/logo-white.png" />
    <img src="https://raw.githubusercontent.com/EmpirioLabs-AI/assets/main/logo-dark.png" alt="EmpirioLabs AI" width="280" />
  </picture>
</a>

# EmpirioLabs AI API examples

Runnable cURL and Python for every model in the EmpirioLabs AI catalog.

<p>
  <a href="https://empiriolabs.ai/models"><img alt="228 models" src="https://img.shields.io/badge/Models-228-1f6feb?style=flat-square"></a>
  <a href="https://docs.empiriolabs.ai/welcome"><img alt="Documentation" src="https://img.shields.io/badge/Docs-docs.empiriolabs.ai-0a66c2?style=flat-square"></a>
  <a href="https://platform.empiriolabs.ai/dashboard/api-keys"><img alt="Get an API key" src="https://img.shields.io/badge/API%20key-Get%20one-0b8a5a?style=flat-square"></a>
  <a href="LICENSE"><img alt="License: MIT-0" src="https://img.shields.io/badge/License-MIT--0-555555?style=flat-square"></a>
</p>

</div>

One folder per model on [EmpirioLabs AI](https://empiriolabs.ai), with the same code as the model's page on empiriolabs.ai. The repository is generated from the live model catalog and kept in sync automatically, so new models are added without manual updates.

## Get started

1. Sign in with your browser, no key to copy: `eval "$(python login.py)"` (PowerShell: `python login.py --powershell | iex`). The connection appears in Settings > Connected applications, where Disconnect revokes it.
2. Or create an API key at https://platform.empiriolabs.ai/dashboard/api-keys and set it: `export EMPIRIOLABS_API_KEY="sk-empiriolabs-..."`.
3. Open a model's folder and run a file, for example `bash models/kimi-k3/request.sh`, or follow the folder's README.

Requests are billed to your EmpirioLabs AI account at each model's listed price (https://empiriolabs.ai/pricing).

## Models

228 models in 12 categories: [3D Generation](#3d-generation-21), [Audio Generation](#audio-generation-44), [Decision Models](#decision-models-1), [Document OCR](#document-ocr-1), [Embeddings](#embeddings-4), [Image Generation](#image-generation-18), [Rerankers](#rerankers-1), [Research & Search](#research--search-13), [Text Generation](#text-generation-73), [Tools & Agents](#tools--agents-2), [Transcription](#transcription-13), [Video Generation](#video-generation-37).

### 3D Generation (21)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [Hitem3D 2.0](https://empiriolabs.ai/models/hitem3d-2-0) | Hitem3D | `POST /v1/3d/generations` | [models/hitem3d-2-0](models/hitem3d-2-0) |
| [Hyper3D Gen2](https://empiriolabs.ai/models/hyper3d-gen2) | Deemos | `POST /v1/3d/generations` | [models/hyper3d-gen2](models/hyper3d-gen2) |
| [Meshy 6](https://empiriolabs.ai/models/meshy-6) | Meshy | `POST /v1/3d/generations` | [models/meshy-6](models/meshy-6) |
| [Meshy 6 Lite](https://empiriolabs.ai/models/meshy-6-lite) | Meshy | `POST /v1/3d/generations` | [models/meshy-6-lite](models/meshy-6-lite) |
| [Meshy 7.1](https://empiriolabs.ai/models/meshy-7-1) | Meshy | `POST /v1/3d/generations` | [models/meshy-7-1](models/meshy-7-1) |
| [Meshy Animation](https://empiriolabs.ai/models/meshy-animation) | Meshy | `POST /v1/3d/generations` | [models/meshy-animation](models/meshy-animation) |
| [Meshy Auto Split](https://empiriolabs.ai/models/meshy-auto-split) | Meshy | `POST /v1/3d/generations` | [models/meshy-auto-split](models/meshy-auto-split) |
| [Meshy Convert](https://empiriolabs.ai/models/meshy-convert) | Meshy | `POST /v1/3d/generations` | [models/meshy-convert](models/meshy-convert) |
| [Meshy Multi-Color Print](https://empiriolabs.ai/models/meshy-multi-color-print) | Meshy | `POST /v1/3d/generations` | [models/meshy-multi-color-print](models/meshy-multi-color-print) |
| [Meshy Print Analysis](https://empiriolabs.ai/models/meshy-print-analysis) | Meshy | `POST /v1/3d/generations` | [models/meshy-print-analysis](models/meshy-print-analysis) |
| [Meshy Print Repair](https://empiriolabs.ai/models/meshy-print-repair) | Meshy | `POST /v1/3d/generations` | [models/meshy-print-repair](models/meshy-print-repair) |
| [Meshy Relief](https://empiriolabs.ai/models/meshy-relief) | Meshy | `POST /v1/3d/generations` | [models/meshy-relief](models/meshy-relief) |
| [Meshy Remesh](https://empiriolabs.ai/models/meshy-remesh) | Meshy | `POST /v1/3d/generations` | [models/meshy-remesh](models/meshy-remesh) |
| [Meshy Resize](https://empiriolabs.ai/models/meshy-resize) | Meshy | `POST /v1/3d/generations` | [models/meshy-resize](models/meshy-resize) |
| [Meshy Retexture](https://empiriolabs.ai/models/meshy-retexture) | Meshy | `POST /v1/3d/generations` | [models/meshy-retexture](models/meshy-retexture) |
| [Meshy Rigging](https://empiriolabs.ai/models/meshy-rigging) | Meshy | `POST /v1/3d/generations` | [models/meshy-rigging](models/meshy-rigging) |
| [Meshy T2](https://empiriolabs.ai/models/meshy-t2) | Meshy | `POST /v1/3d/generations` | [models/meshy-t2](models/meshy-t2) |
| [Meshy T2.5](https://empiriolabs.ai/models/meshy-t2-5) | Meshy | `POST /v1/3d/generations` | [models/meshy-t2-5](models/meshy-t2-5) |
| [Meshy Text to Motion](https://empiriolabs.ai/models/meshy-text-to-motion) | Meshy | `POST /v1/3d/generations` | [models/meshy-text-to-motion](models/meshy-text-to-motion) |
| [Meshy UV Unwrap](https://empiriolabs.ai/models/meshy-uv-unwrap) | Meshy | `POST /v1/3d/generations` | [models/meshy-uv-unwrap](models/meshy-uv-unwrap) |
| [TRELLIS.2 4B](https://empiriolabs.ai/models/trellis-2-4b) | Microsoft | `POST /v1/3d/generations` | [models/trellis-2-4b](models/trellis-2-4b) |

### Audio Generation (44)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [ACE-Step 1.5 XL](https://empiriolabs.ai/models/ace-step-1-5-xl) | ACE-Step | `POST /v1/audio/generations` | [models/ace-step-1-5-xl](models/ace-step-1-5-xl) |
| [Gemini 2.5 Flash TTS](https://empiriolabs.ai/models/gemini-2-5-flash-tts) | Google | `POST /v1/audio/speech` | [models/gemini-2-5-flash-tts](models/gemini-2-5-flash-tts) |
| [Gemini 2.5 Pro TTS](https://empiriolabs.ai/models/gemini-2-5-pro-tts) | Google | `POST /v1/audio/speech` | [models/gemini-2-5-pro-tts](models/gemini-2-5-pro-tts) |
| [Gemini 3.1 Flash TTS](https://empiriolabs.ai/models/gemini-3-1-flash-tts) | Google | `POST /v1/audio/speech` | [models/gemini-3-1-flash-tts](models/gemini-3-1-flash-tts) |
| [Gemini 3.8 Flash TTS](https://empiriolabs.ai/models/gemini-3-8-flash-tts) | Google | `POST /v1/audio/speech` | [models/gemini-3-8-flash-tts](models/gemini-3-8-flash-tts) |
| [Gemini 3.8 Flash-Lite TTS](https://empiriolabs.ai/models/gemini-3-8-flash-lite-tts) | Google | `POST /v1/audio/speech` | [models/gemini-3-8-flash-lite-tts](models/gemini-3-8-flash-lite-tts) |
| [Gemini 3.8 Live](https://empiriolabs.ai/models/gemini-3-8-live) | Google | `WEBSOCKET /v1/realtime` | [models/gemini-3-8-live](models/gemini-3-8-live) |
| [Gemini 3.8 Live Extended Thinking](https://empiriolabs.ai/models/gemini-3-8-live-extended-thinking) | Google | `WEBSOCKET /v1/realtime` | [models/gemini-3-8-live-extended-thinking](models/gemini-3-8-live-extended-thinking) |
| [GLM TTS](https://empiriolabs.ai/models/glm-tts) | Z.ai | `POST /v1/audio/speech` | [models/glm-tts](models/glm-tts) |
| [MiniMax Music 3](https://empiriolabs.ai/models/minimax-music-3) | MiniMax | `POST /v1/audio/generations` | [models/minimax-music-3](models/minimax-music-3) |
| [Qwen Audio 3.0 Realtime Flash](https://empiriolabs.ai/models/qwen-audio-3-0-realtime-flash) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen-audio-3-0-realtime-flash](models/qwen-audio-3-0-realtime-flash) |
| [Qwen Audio 3.0 Realtime Plus](https://empiriolabs.ai/models/qwen-audio-3-0-realtime-plus) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen-audio-3-0-realtime-plus](models/qwen-audio-3-0-realtime-plus) |
| [Qwen Audio 3.0 TTS](https://empiriolabs.ai/models/qwen-audio-3-0-tts) | Alibaba Cloud | `POST /v1/audio/speech` | [models/qwen-audio-3-0-tts](models/qwen-audio-3-0-tts) |
| [Qwen Audio 3.1 Live](https://empiriolabs.ai/models/qwen-audio-3-1-live) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen-audio-3-1-live](models/qwen-audio-3-1-live) |
| [Qwen Audio 3.1 Realtime Flash](https://empiriolabs.ai/models/qwen-audio-3-1-realtime-flash) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen-audio-3-1-realtime-flash](models/qwen-audio-3-1-realtime-flash) |
| [Qwen Audio 3.1 Realtime Plus](https://empiriolabs.ai/models/qwen-audio-3-1-realtime-plus) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen-audio-3-1-realtime-plus](models/qwen-audio-3-1-realtime-plus) |
| [Qwen Audio 3.1 TTS](https://empiriolabs.ai/models/qwen-audio-3-1-tts) | Alibaba Cloud | `POST /v1/audio/speech` | [models/qwen-audio-3-1-tts](models/qwen-audio-3-1-tts) |
| [Qwen Audio 3.1 TTS Next](https://empiriolabs.ai/models/qwen-audio-3-1-tts-next) | Alibaba Cloud | `POST /v1/audio/speech` | [models/qwen-audio-3-1-tts-next](models/qwen-audio-3-1-tts-next) |
| [Qwen Audio 3.1 TTS Plus](https://empiriolabs.ai/models/qwen-audio-3-1-tts-plus) | Alibaba Cloud | `POST /v1/audio/speech` | [models/qwen-audio-3-1-tts-plus](models/qwen-audio-3-1-tts-plus) |
| [Qwen3.5 Omni Flash Realtime](https://empiriolabs.ai/models/qwen3-5-omni-flash-realtime) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen3-5-omni-flash-realtime](models/qwen3-5-omni-flash-realtime) |
| [Qwen3.5 Omni Plus Realtime](https://empiriolabs.ai/models/qwen3-5-omni-plus-realtime) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen3-5-omni-plus-realtime](models/qwen3-5-omni-plus-realtime) |
| [Qwen3.8 LiveTranslate Flash Realtime](https://empiriolabs.ai/models/qwen3-8-livetranslate-flash-realtime) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen3-8-livetranslate-flash-realtime](models/qwen3-8-livetranslate-flash-realtime) |
| [Qwen3.8 Omni Flash Realtime](https://empiriolabs.ai/models/qwen3-8-omni-flash-realtime) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen3-8-omni-flash-realtime](models/qwen3-8-omni-flash-realtime) |
| [Seed Audio 1.0](https://empiriolabs.ai/models/seed-audio-1-0) | ByteDance | `POST /v1/audio/generations` | [models/seed-audio-1-0](models/seed-audio-1-0) |
| [Seed TTS 2.0](https://empiriolabs.ai/models/seed-tts-2-0) | ByteDance | `POST /v1/audio/speech` | [models/seed-tts-2-0](models/seed-tts-2-0) |
| [Seed TTS 3.0](https://empiriolabs.ai/models/seed-tts-3-0) | ByteDance | `POST /v1/audio/speech` | [models/seed-tts-3-0](models/seed-tts-3-0) |
| [Seed Voice Replication 2.0](https://empiriolabs.ai/models/seed-voice-replication-2-0) | ByteDance | `POST /v1/audio/generations` | [models/seed-voice-replication-2-0](models/seed-voice-replication-2-0) |
| [Sonilo Audio Ducking](https://empiriolabs.ai/models/sonilo-audio-ducking) | Sonilo | `POST /v1/audio/generations` | [models/sonilo-audio-ducking](models/sonilo-audio-ducking) |
| [Sonilo Sound Effects 1.0](https://empiriolabs.ai/models/sonilo-sound-effects-1-0) | Sonilo | `POST /v1/audio/generations` | [models/sonilo-sound-effects-1-0](models/sonilo-sound-effects-1-0) |
| [Sonilo v1.1](https://empiriolabs.ai/models/sonilo-v1-1) | Sonilo | `POST /v1/audio/generations` | [models/sonilo-v1-1](models/sonilo-v1-1) |
| [SoulX Podcast](https://empiriolabs.ai/models/soulx-podcast) | Soul AI Lab | `POST /v1/audio/speech` | [models/soulx-podcast](models/soulx-podcast) |
| [Stable Audio 2.0](https://empiriolabs.ai/models/stable-audio-2-0) | Stability AI | `POST /v1/audio/generations` | [models/stable-audio-2-0](models/stable-audio-2-0) |
| [Stable Audio 2.5](https://empiriolabs.ai/models/stable-audio-2-5) | Stability AI | `POST /v1/audio/generations` | [models/stable-audio-2-5](models/stable-audio-2-5) |
| [Stable Audio 3 Medium](https://empiriolabs.ai/models/stable-audio-3-medium) | Stability AI | `POST /v1/audio/generations` | [models/stable-audio-3-medium](models/stable-audio-3-medium) |
| [StepAudio 2.5 Realtime](https://empiriolabs.ai/models/stepaudio-2-5-realtime) | StepFun | `WEBSOCKET /v1/realtime` | [models/stepaudio-2-5-realtime](models/stepaudio-2-5-realtime) |
| [StepAudio 2.5 TTS](https://empiriolabs.ai/models/stepaudio-2-5-tts) | StepFun | `POST /v1/audio/speech` | [models/stepaudio-2-5-tts](models/stepaudio-2-5-tts) |
| [StepAudio 3 Gen](https://empiriolabs.ai/models/stepaudio-3-gen) | StepFun | `POST /v1/audio/generations` | [models/stepaudio-3-gen](models/stepaudio-3-gen) |
| [StepAudio 3 Music](https://empiriolabs.ai/models/stepaudio-3-music) | StepFun | `POST /v1/audio/generations` | [models/stepaudio-3-music](models/stepaudio-3-music) |
| [StepAudio 3 Realtime](https://empiriolabs.ai/models/stepaudio-3-realtime) | StepFun | `WEBSOCKET /v1/realtime` | [models/stepaudio-3-realtime](models/stepaudio-3-realtime) |
| [StepAudio 3 TTS](https://empiriolabs.ai/models/stepaudio-3-tts) | StepFun | `POST /v1/audio/speech` | [models/stepaudio-3-tts](models/stepaudio-3-tts) |
| [TTS 1.5 Max](https://empiriolabs.ai/models/tts-1-5-max) | Inworld | `POST /v1/audio/speech` | [models/tts-1-5-max](models/tts-1-5-max) |
| [TTS 1.5 Mini](https://empiriolabs.ai/models/tts-1-5-mini) | Inworld | `POST /v1/audio/speech` | [models/tts-1-5-mini](models/tts-1-5-mini) |
| [TTS 2](https://empiriolabs.ai/models/tts-2) | Inworld | `POST /v1/audio/speech` | [models/tts-2](models/tts-2) |
| [TTS 2 Flash](https://empiriolabs.ai/models/tts-2-flash) | Inworld | `POST /v1/audio/speech` | [models/tts-2-flash](models/tts-2-flash) |

### Decision Models (1)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [Aplomb 1](https://empiriolabs.ai/models/aplomb-1) | EmpirioLabs | `POST /v1/decisions` | [models/aplomb-1](models/aplomb-1) |

### Document OCR (1)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [LightOnOCR-3 4B](https://empiriolabs.ai/models/lightonocr-3-4b) | LightOn | `POST /v1/ocr` | [models/lightonocr-3-4b](models/lightonocr-3-4b) |

### Embeddings (4)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [Skylark Embedding Vision](https://empiriolabs.ai/models/skylark-embedding-vision) | ByteDance | `POST /v1/embeddings` | [models/skylark-embedding-vision](models/skylark-embedding-vision) |
| [Text Embedding v4](https://empiriolabs.ai/models/text-embedding-v4) | Alibaba Cloud | `POST /v1/embeddings` | [models/text-embedding-v4](models/text-embedding-v4) |
| [Tongyi Embedding Vision Flash](https://empiriolabs.ai/models/tongyi-embedding-vision-flash) | Alibaba Cloud | `POST /v1/embeddings` | [models/tongyi-embedding-vision-flash](models/tongyi-embedding-vision-flash) |
| [Tongyi Embedding Vision Plus](https://empiriolabs.ai/models/tongyi-embedding-vision-plus) | Alibaba Cloud | `POST /v1/embeddings` | [models/tongyi-embedding-vision-plus](models/tongyi-embedding-vision-plus) |

### Image Generation (18)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [FLUX.2 Klein 4B](https://empiriolabs.ai/models/flux-2-klein-4b) | Black Forest Labs | `POST /v1/images/generations` | [models/flux-2-klein-4b](models/flux-2-klein-4b) |
| [GPT Image 2](https://empiriolabs.ai/models/gpt-image-2) | OpenAI | `POST /v1/images/generations` | [models/gpt-image-2](models/gpt-image-2) |
| [Grok Imagine Image 2.0](https://empiriolabs.ai/models/grok-imagine-image-2-0) | xAI | `POST /v1/images/generations` | [models/grok-imagine-image-2-0](models/grok-imagine-image-2-0) |
| [Hunyuan Image 3](https://empiriolabs.ai/models/hunyuan-image-3) | Tencent | `POST /v1/images/generations` | [models/hunyuan-image-3](models/hunyuan-image-3) |
| [MOSS-Image Turbo](https://empiriolabs.ai/models/moss-image-turbo) | OpenMOSS | `POST /v1/images/generations` | [models/moss-image-turbo](models/moss-image-turbo) |
| [Qwen Image 2.0](https://empiriolabs.ai/models/qwen-image-2-0) | Alibaba Cloud | `POST /v1/images/generations` | [models/qwen-image-2-0](models/qwen-image-2-0) |
| [Qwen Image 2.1](https://empiriolabs.ai/models/qwen-image-2-1) | Alibaba Cloud | `POST /v1/images/generations` | [models/qwen-image-2-1](models/qwen-image-2-1) |
| [Qwen Image 3.0](https://empiriolabs.ai/models/qwen-image-3-0) | Alibaba Cloud | `POST /v1/images/generations` | [models/qwen-image-3-0](models/qwen-image-3-0) |
| [Seedream 4.0](https://empiriolabs.ai/models/seedream-4-0) | ByteDance | `POST /v1/images/generations` | [models/seedream-4-0](models/seedream-4-0) |
| [Seedream 4.5](https://empiriolabs.ai/models/seedream-4-5) | ByteDance | `POST /v1/images/generations` | [models/seedream-4-5](models/seedream-4-5) |
| [Seedream 5.0 Flash](https://empiriolabs.ai/models/seedream-5-0-flash) | ByteDance | `POST /v1/images/generations` | [models/seedream-5-0-flash](models/seedream-5-0-flash) |
| [Seedream 5.0 Lite](https://empiriolabs.ai/models/seedream-5-0-lite) | ByteDance | `POST /v1/images/generations` | [models/seedream-5-0-lite](models/seedream-5-0-lite) |
| [Seedream 5.0 Pro](https://empiriolabs.ai/models/seedream-5-0-pro) | ByteDance | `POST /v1/images/generations` | [models/seedream-5-0-pro](models/seedream-5-0-pro) |
| [Seedream 5.5](https://empiriolabs.ai/models/seedream-5-5) | ByteDance | `POST /v1/images/generations` | [models/seedream-5-5](models/seedream-5-5) |
| [Wan2.1 Image](https://empiriolabs.ai/models/wan2-1-image) | Alibaba Cloud | `POST /v1/images/generations` | [models/wan2-1-image](models/wan2-1-image) |
| [Wan2.2 Image](https://empiriolabs.ai/models/wan2-2-image) | Alibaba Cloud | `POST /v1/images/generations` | [models/wan2-2-image](models/wan2-2-image) |
| [Wan2.5 Image](https://empiriolabs.ai/models/wan2-5-image) | Alibaba Cloud | `POST /v1/images/generations` | [models/wan2-5-image](models/wan2-5-image) |
| [Wan2.7 Image](https://empiriolabs.ai/models/wan2-7-image) | Alibaba Cloud | `POST /v1/images/generations` | [models/wan2-7-image](models/wan2-7-image) |

### Rerankers (1)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [Qwen3 Rerank](https://empiriolabs.ai/models/qwen3-rerank) | Alibaba Cloud | `POST /v1/reranks` | [models/qwen3-rerank](models/qwen3-rerank) |

### Research & Search (13)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [Exa Answer](https://empiriolabs.ai/models/exa-answer) | Exa | `POST /v1/chat/completions` | [models/exa-answer](models/exa-answer) |
| [Exa Search](https://empiriolabs.ai/models/exa-search) | Exa | `POST /v1/search` | [models/exa-search](models/exa-search) |
| [Linkup Deep Search](https://empiriolabs.ai/models/linkup-deep-search) | Linkup | `POST /v1/chat/completions` | [models/linkup-deep-search](models/linkup-deep-search) |
| [Linkup Standard](https://empiriolabs.ai/models/linkup-standard) | Linkup | `POST /v1/chat/completions` | [models/linkup-standard](models/linkup-standard) |
| [Perplexity Advanced Deep Research](https://empiriolabs.ai/models/perplexity-advanced-deep-research) | Perplexity | `POST /v1/chat/completions` | [models/perplexity-advanced-deep-research](models/perplexity-advanced-deep-research) |
| [Perplexity Deep Research](https://empiriolabs.ai/models/perplexity-deep-research) | Perplexity | `POST /v1/chat/completions` | [models/perplexity-deep-research](models/perplexity-deep-research) |
| [Perplexity Pro Search](https://empiriolabs.ai/models/perplexity-pro-search) | Perplexity | `POST /v1/chat/completions` | [models/perplexity-pro-search](models/perplexity-pro-search) |
| [Perplexity Search](https://empiriolabs.ai/models/perplexity-search) | Perplexity | `POST /v1/search` | [models/perplexity-search](models/perplexity-search) |
| [Perplexity Sonar](https://empiriolabs.ai/models/perplexity-sonar) | Perplexity | `POST /v1/chat/completions` | [models/perplexity-sonar](models/perplexity-sonar) |
| [Perplexity Sonar Pro](https://empiriolabs.ai/models/perplexity-sonar-pro) | Perplexity | `POST /v1/chat/completions` | [models/perplexity-sonar-pro](models/perplexity-sonar-pro) |
| [Perplexity Sonar Reasoning Pro](https://empiriolabs.ai/models/perplexity-sonar-reasoning-pro) | Perplexity | `POST /v1/chat/completions` | [models/perplexity-sonar-reasoning-pro](models/perplexity-sonar-reasoning-pro) |
| [Tavily Research](https://empiriolabs.ai/models/tavily-research) | Tavily | `POST /v1/research` | [models/tavily-research](models/tavily-research) |
| [Tavily Search](https://empiriolabs.ai/models/tavily-search) | Tavily | `POST /v1/search` | [models/tavily-search](models/tavily-search) |

### Text Generation (73)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [DeepReasoning](https://empiriolabs.ai/models/deepreasoning) | WinFunc | `POST /v1/chat/completions` | [models/deepreasoning](models/deepreasoning) |
| [DeepSeek V4 Flash 0731](https://empiriolabs.ai/models/deepseek-v4-flash-0731) | DeepSeek | `POST /v1/chat/completions` | [models/deepseek-v4-flash-0731](models/deepseek-v4-flash-0731) |
| [DeepSeek V4 Pro](https://empiriolabs.ai/models/deepseek-v4-pro) | DeepSeek | `POST /v1/chat/completions` | [models/deepseek-v4-pro](models/deepseek-v4-pro) |
| [DeepSeek V4 Pro 0813](https://empiriolabs.ai/models/deepseek-v4-pro-0813) | DeepSeek | `POST /v1/chat/completions` | [models/deepseek-v4-pro-0813](models/deepseek-v4-pro-0813) |
| [DeepSeek V4.1 Flash 1017](https://empiriolabs.ai/models/deepseek-v4-1-flash-1017) | DeepSeek | `POST /v1/chat/completions` | [models/deepseek-v4-1-flash-1017](models/deepseek-v4-1-flash-1017) |
| [Fugu Max](https://empiriolabs.ai/models/fugu-max) | Sakana AI | `POST /v1/chat/completions` | [models/fugu-max](models/fugu-max) |
| [Fugu Ultra v1.0](https://empiriolabs.ai/models/fugu-ultra-v1-0) | Sakana AI | `POST /v1/chat/completions` | [models/fugu-ultra-v1-0](models/fugu-ultra-v1-0) |
| [Fugu Ultra v1.1](https://empiriolabs.ai/models/fugu-ultra-v1-1) | Sakana AI | `POST /v1/chat/completions` | [models/fugu-ultra-v1-1](models/fugu-ultra-v1-1) |
| [Fugu Ultra v2.0](https://empiriolabs.ai/models/fugu-ultra-v2-0) | Sakana AI | `POST /v1/chat/completions` | [models/fugu-ultra-v2-0](models/fugu-ultra-v2-0) |
| [Gemma 4 26B-A4B](https://empiriolabs.ai/models/gemma-4-26b-a4b) | Google | `POST /v1/chat/completions` | [models/gemma-4-26b-a4b](models/gemma-4-26b-a4b) |
| [GLM 4.5 Flash](https://empiriolabs.ai/models/glm-4-5-flash) | Z.ai | `POST /v1/chat/completions` | [models/glm-4-5-flash](models/glm-4-5-flash) |
| [GLM 4.6V Flash](https://empiriolabs.ai/models/glm-4-6v-flash) | Z.ai | `POST /v1/chat/completions` | [models/glm-4-6v-flash](models/glm-4-6v-flash) |
| [GLM 4.6V FlashX](https://empiriolabs.ai/models/glm-4-6v-flashx) | Z.ai | `POST /v1/chat/completions` | [models/glm-4-6v-flashx](models/glm-4-6v-flashx) |
| [GLM 4.7 Flash](https://empiriolabs.ai/models/glm-4-7-flash) | Z.ai | `POST /v1/chat/completions` | [models/glm-4-7-flash](models/glm-4-7-flash) |
| [GLM 4.7 FlashX](https://empiriolabs.ai/models/glm-4-7-flashx) | Z.ai | `POST /v1/chat/completions` | [models/glm-4-7-flashx](models/glm-4-7-flashx) |
| [GLM 5.1](https://empiriolabs.ai/models/glm-5-1) | Z.ai | `POST /v1/chat/completions` | [models/glm-5-1](models/glm-5-1) |
| [GLM 5.2](https://empiriolabs.ai/models/glm-5-2) | Z.ai | `POST /v1/chat/completions` | [models/glm-5-2](models/glm-5-2) |
| [GLM 5.3](https://empiriolabs.ai/models/glm-5-3) | Z.ai | `POST /v1/chat/completions` | [models/glm-5-3](models/glm-5-3) |
| [GLM 5.3 Flash](https://empiriolabs.ai/models/glm-5-3-flash) | Z.ai | `POST /v1/chat/completions` | [models/glm-5-3-flash](models/glm-5-3-flash) |
| [Kimi K2.6](https://empiriolabs.ai/models/kimi-k2-6) | Moonshot AI | `POST /v1/chat/completions` | [models/kimi-k2-6](models/kimi-k2-6) |
| [Kimi K2.7 Code](https://empiriolabs.ai/models/kimi-k2-7-code) | Moonshot AI | `POST /v1/chat/completions` | [models/kimi-k2-7-code](models/kimi-k2-7-code) |
| [Kimi K2.7 Code Highspeed](https://empiriolabs.ai/models/kimi-k2-7-code-highspeed) | Moonshot AI | `POST /v1/chat/completions` | [models/kimi-k2-7-code-highspeed](models/kimi-k2-7-code-highspeed) |
| [Kimi K3](https://empiriolabs.ai/models/kimi-k3) | Moonshot AI | `POST /v1/chat/completions` | [models/kimi-k3](models/kimi-k3) |
| [Kimi K3.1 Pro](https://empiriolabs.ai/models/kimi-k3-1-pro) | Moonshot AI | `POST /v1/chat/completions` | [models/kimi-k3-1-pro](models/kimi-k3-1-pro) |
| [MiMo V2.6 Flash](https://empiriolabs.ai/models/mimo-v2-6-flash) | Xiaomi | `POST /v1/chat/completions` | [models/mimo-v2-6-flash](models/mimo-v2-6-flash) |
| [MiMo V2.6 Pro](https://empiriolabs.ai/models/mimo-v2-6-pro) | Xiaomi | `POST /v1/chat/completions` | [models/mimo-v2-6-pro](models/mimo-v2-6-pro) |
| [MiMo V2.6 Pro UltraSpeed](https://empiriolabs.ai/models/mimo-v2-6-pro-ultraspeed) | Xiaomi | `POST /v1/chat/completions` | [models/mimo-v2-6-pro-ultraspeed](models/mimo-v2-6-pro-ultraspeed) |
| [MiniMax M3](https://empiriolabs.ai/models/minimax-m3) | MiniMax | `POST /v1/chat/completions` | [models/minimax-m3](models/minimax-m3) |
| [MiniMax M3.1 Flash](https://empiriolabs.ai/models/minimax-m3-1-flash) | MiniMax | `POST /v1/chat/completions` | [models/minimax-m3-1-flash](models/minimax-m3-1-flash) |
| [Mistral Small 3.1](https://empiriolabs.ai/models/mistral-small-3-1) | Mistral AI | `POST /v1/chat/completions` | [models/mistral-small-3-1](models/mistral-small-3-1) |
| [Mistral Small 4](https://empiriolabs.ai/models/mistral-small-4) | Mistral AI | `POST /v1/chat/completions` | [models/mistral-small-4](models/mistral-small-4) |
| [Muse Glimmer 30B](https://empiriolabs.ai/models/muse-glimmer-30b) | Meta AI | `POST /v1/chat/completions` | [models/muse-glimmer-30b](models/muse-glimmer-30b) |
| [Muse Spark 1.1](https://empiriolabs.ai/models/muse-spark-1-1) | Meta AI | `POST /v1/chat/completions` | [models/muse-spark-1-1](models/muse-spark-1-1) |
| [Muse Spark 1.2](https://empiriolabs.ai/models/muse-spark-1-2) | Meta AI | `POST /v1/chat/completions` | [models/muse-spark-1-2](models/muse-spark-1-2) |
| [Muse Spark 1.3](https://empiriolabs.ai/models/muse-spark-1-3) | Meta AI | `POST /v1/chat/completions` | [models/muse-spark-1-3](models/muse-spark-1-3) |
| [Nova Lite 1.0](https://empiriolabs.ai/models/nova-lite-1-0) | Amazon | `POST /v1/chat/completions` | [models/nova-lite-1-0](models/nova-lite-1-0) |
| [Nova Lite 2](https://empiriolabs.ai/models/nova-lite-2) | Amazon | `POST /v1/chat/completions` | [models/nova-lite-2](models/nova-lite-2) |
| [Nova Micro 1.0](https://empiriolabs.ai/models/nova-micro-1-0) | Amazon | `POST /v1/chat/completions` | [models/nova-micro-1-0](models/nova-micro-1-0) |
| [Nova Pro 1.0](https://empiriolabs.ai/models/nova-pro-1-0) | Amazon | `POST /v1/chat/completions` | [models/nova-pro-1-0](models/nova-pro-1-0) |
| [Qwen3.5 122B-A10B](https://empiriolabs.ai/models/qwen3-5-122b-a10b) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-122b-a10b](models/qwen3-5-122b-a10b) |
| [Qwen3.5 27B](https://empiriolabs.ai/models/qwen3-5-27b) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-27b](models/qwen3-5-27b) |
| [Qwen3.5 35B-A3B](https://empiriolabs.ai/models/qwen3-5-35b-a3b) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-35b-a3b](models/qwen3-5-35b-a3b) |
| [Qwen3.5 397B-A17B](https://empiriolabs.ai/models/qwen3-5-397b-a17b) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-397b-a17b](models/qwen3-5-397b-a17b) |
| [Qwen3.5 4B](https://empiriolabs.ai/models/qwen3-5-4b) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-4b](models/qwen3-5-4b) |
| [Qwen3.5 9B](https://empiriolabs.ai/models/qwen3-5-9b) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-9b](models/qwen3-5-9b) |
| [Qwen3.5 Flash](https://empiriolabs.ai/models/qwen3-5-flash) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-flash](models/qwen3-5-flash) |
| [Qwen3.5 Omni Flash](https://empiriolabs.ai/models/qwen3-5-omni-flash) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-omni-flash](models/qwen3-5-omni-flash) |
| [Qwen3.5 Omni Plus](https://empiriolabs.ai/models/qwen3-5-omni-plus) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-omni-plus](models/qwen3-5-omni-plus) |
| [Qwen3.5 Plus](https://empiriolabs.ai/models/qwen3-5-plus) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-5-plus](models/qwen3-5-plus) |
| [Qwen3.6 27B](https://empiriolabs.ai/models/qwen3-6-27b) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-6-27b](models/qwen3-6-27b) |
| [Qwen3.6 35B A3B](https://empiriolabs.ai/models/qwen3-6-35b-a3b) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-6-35b-a3b](models/qwen3-6-35b-a3b) |
| [Qwen3.6 Flash](https://empiriolabs.ai/models/qwen3-6-flash) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-6-flash](models/qwen3-6-flash) |
| [Qwen3.6 Plus](https://empiriolabs.ai/models/qwen3-6-plus) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-6-plus](models/qwen3-6-plus) |
| [Qwen3.7 Flash](https://empiriolabs.ai/models/qwen3-7-flash) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-7-flash](models/qwen3-7-flash) |
| [Qwen3.7 Max](https://empiriolabs.ai/models/qwen3-7-max) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-7-max](models/qwen3-7-max) |
| [Qwen3.7 Plus](https://empiriolabs.ai/models/qwen3-7-plus) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-7-plus](models/qwen3-7-plus) |
| [Qwen3.8 27B](https://empiriolabs.ai/models/qwen3-8-27b) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-8-27b](models/qwen3-8-27b) |
| [Qwen3.8 Flash](https://empiriolabs.ai/models/qwen3-8-flash) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-8-flash](models/qwen3-8-flash) |
| [Qwen3.8 Max](https://empiriolabs.ai/models/qwen3-8-max) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-8-max](models/qwen3-8-max) |
| [Qwen3.8 Max 0902](https://empiriolabs.ai/models/qwen3-8-max-0902) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-8-max-0902](models/qwen3-8-max-0902) |
| [Qwen3.8 Omni Flash](https://empiriolabs.ai/models/qwen3-8-omni-flash) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen3-8-omni-flash](models/qwen3-8-omni-flash) |
| [Qwen4 Max](https://empiriolabs.ai/models/qwen4-max) | Alibaba Cloud | `POST /v1/chat/completions` | [models/qwen4-max](models/qwen4-max) |
| [Seed 2.0 Code](https://empiriolabs.ai/models/seed-2-0-code) | ByteDance | `POST /v1/chat/completions` | [models/seed-2-0-code](models/seed-2-0-code) |
| [Seed 2.0 Lite](https://empiriolabs.ai/models/seed-2-0-lite) | ByteDance | `POST /v1/chat/completions` | [models/seed-2-0-lite](models/seed-2-0-lite) |
| [Seed 2.0 Mini](https://empiriolabs.ai/models/seed-2-0-mini) | ByteDance | `POST /v1/chat/completions` | [models/seed-2-0-mini](models/seed-2-0-mini) |
| [Seed 2.0 Pro](https://empiriolabs.ai/models/seed-2-0-pro) | ByteDance | `POST /v1/chat/completions` | [models/seed-2-0-pro](models/seed-2-0-pro) |
| [Seed 2.1 Turbo](https://empiriolabs.ai/models/seed-2-1-turbo) | ByteDance | `POST /v1/chat/completions` | [models/seed-2-1-turbo](models/seed-2-1-turbo) |
| [Step 3.5 Flash](https://empiriolabs.ai/models/step-3-5-flash) | StepFun | `POST /v1/chat/completions` | [models/step-3-5-flash](models/step-3-5-flash) |
| [Step 3.5 Flash 2603](https://empiriolabs.ai/models/step-3-5-flash-2603) | StepFun | `POST /v1/chat/completions` | [models/step-3-5-flash-2603](models/step-3-5-flash-2603) |
| [Step 3.7 Flash](https://empiriolabs.ai/models/step-3-7-flash) | StepFun | `POST /v1/chat/completions` | [models/step-3-7-flash](models/step-3-7-flash) |
| [Step 5 Preview](https://empiriolabs.ai/models/step-5-preview) | StepFun | `POST /v1/chat/completions` | [models/step-5-preview](models/step-5-preview) |
| [StepAudio 2.5 Chat](https://empiriolabs.ai/models/stepaudio-2-5-chat) | StepFun | `POST /v1/chat/completions` | [models/stepaudio-2-5-chat](models/stepaudio-2-5-chat) |
| [StepAudio 3 Chat](https://empiriolabs.ai/models/stepaudio-3-chat) | StepFun | `POST /v1/chat/completions` | [models/stepaudio-3-chat](models/stepaudio-3-chat) |

### Tools & Agents (2)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [GPTZero](https://empiriolabs.ai/models/gptzero) | GPTZero | `POST /v1/chat/completions` | [models/gptzero](models/gptzero) |
| [Manus](https://empiriolabs.ai/models/manus) | Manus | `POST /v1/agents/run` | [models/manus](models/manus) |

### Transcription (13)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [Deepgram Nova-3](https://empiriolabs.ai/models/deepgram-nova-3) | Deepgram | `POST /v1/audio/transcriptions` | [models/deepgram-nova-3](models/deepgram-nova-3) |
| [Deepgram Nova-3 Stream](https://empiriolabs.ai/models/deepgram-nova-3-stream) | Deepgram | `WEBSOCKET /v1/realtime` | [models/deepgram-nova-3-stream](models/deepgram-nova-3-stream) |
| [OpenAI Whisper 1](https://empiriolabs.ai/models/openai-whisper-1) | OpenAI | `POST /v1/audio/transcriptions` | [models/openai-whisper-1](models/openai-whisper-1) |
| [Qwen Audio 3.0 ASR](https://empiriolabs.ai/models/qwen-audio-3-0-asr) | Alibaba Cloud | `POST /v1/audio/transcriptions` | [models/qwen-audio-3-0-asr](models/qwen-audio-3-0-asr) |
| [Qwen Audio 3.0 ASR Stream](https://empiriolabs.ai/models/qwen-audio-3-0-asr-stream) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen-audio-3-0-asr-stream](models/qwen-audio-3-0-asr-stream) |
| [Qwen Audio 3.1 ASR](https://empiriolabs.ai/models/qwen-audio-3-1-asr) | Alibaba Cloud | `POST /v1/audio/transcriptions` | [models/qwen-audio-3-1-asr](models/qwen-audio-3-1-asr) |
| [Qwen Audio 3.1 ASR Message](https://empiriolabs.ai/models/qwen-audio-3-1-asr-message) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen-audio-3-1-asr-message](models/qwen-audio-3-1-asr-message) |
| [Qwen Audio 3.1 ASR Stream](https://empiriolabs.ai/models/qwen-audio-3-1-asr-stream) | Alibaba Cloud | `WEBSOCKET /v1/realtime` | [models/qwen-audio-3-1-asr-stream](models/qwen-audio-3-1-asr-stream) |
| [Sonilo Proofread](https://empiriolabs.ai/models/sonilo-proofread) | Sonilo | `POST /v1/audio/transcriptions` | [models/sonilo-proofread](models/sonilo-proofread) |
| [StepAudio 2.5 ASR](https://empiriolabs.ai/models/stepaudio-2-5-asr) | StepFun | `POST /v1/audio/transcriptions` | [models/stepaudio-2-5-asr](models/stepaudio-2-5-asr) |
| [StepAudio 2.5 ASR Stream](https://empiriolabs.ai/models/stepaudio-2-5-asr-stream) | StepFun | `WEBSOCKET /v1/realtime` | [models/stepaudio-2-5-asr-stream](models/stepaudio-2-5-asr-stream) |
| [StepAudio 3 ASR Max](https://empiriolabs.ai/models/stepaudio-3-asr-max) | StepFun | `POST /v1/audio/transcriptions` | [models/stepaudio-3-asr-max](models/stepaudio-3-asr-max) |
| [Whisper Large v3 Turbo](https://empiriolabs.ai/models/whisper-large-v3-turbo) | OpenAI | `POST /v1/audio/transcriptions` | [models/whisper-large-v3-turbo](models/whisper-large-v3-turbo) |

### Video Generation (37)

| Model | Provider | Endpoint | Examples |
| --- | --- | --- | --- |
| [Grok Imagine Video 1.5](https://empiriolabs.ai/models/grok-imagine-video-1-5) | xAI | `POST /v1/videos/generations` | [models/grok-imagine-video-1-5](models/grok-imagine-video-1-5) |
| [HappyHorse 1.0](https://empiriolabs.ai/models/happyhorse-1-0) | Alibaba Cloud | `POST /v1/videos/generations` | [models/happyhorse-1-0](models/happyhorse-1-0) |
| [HappyHorse 1.1](https://empiriolabs.ai/models/happyhorse-1-1) | Alibaba Cloud | `POST /v1/videos/generations` | [models/happyhorse-1-1](models/happyhorse-1-1) |
| [Hunyuan Video 1.5](https://empiriolabs.ai/models/hunyuan-video-1-5) | Tencent | `POST /v1/videos/generations` | [models/hunyuan-video-1-5](models/hunyuan-video-1-5) |
| [Kling 3.0 Turbo](https://empiriolabs.ai/models/kling-3-0-turbo) | Kling AI | `POST /v1/videos/generations` | [models/kling-3-0-turbo](models/kling-3-0-turbo) |
| [Kling 4.0](https://empiriolabs.ai/models/kling-4-0) | Kling AI | `POST /v1/videos/generations` | [models/kling-4-0](models/kling-4-0) |
| [Kling 4.0 Flash](https://empiriolabs.ai/models/kling-4-0-flash) | Kling AI | `POST /v1/videos/generations` | [models/kling-4-0-flash](models/kling-4-0-flash) |
| [Kling O3](https://empiriolabs.ai/models/kling-o3) | Kling AI | `POST /v1/videos/generations` | [models/kling-o3](models/kling-o3) |
| [Kling V3](https://empiriolabs.ai/models/kling-v3) | Kling AI | `POST /v1/videos/generations` | [models/kling-v3](models/kling-v3) |
| [Kling v3 Motion Control](https://empiriolabs.ai/models/kling-v3-motion-control) | Kling AI | `POST /v1/videos/generations` | [models/kling-v3-motion-control](models/kling-v3-motion-control) |
| [MiniMax H3](https://empiriolabs.ai/models/minimax-h3) | MiniMax | `POST /v1/videos/generations` | [models/minimax-h3](models/minimax-h3) |
| [MiniMax H3 Highspeed](https://empiriolabs.ai/models/minimax-h3-highspeed) | MiniMax | `POST /v1/videos/generations` | [models/minimax-h3-highspeed](models/minimax-h3-highspeed) |
| [MiniMax H3 Lite](https://empiriolabs.ai/models/minimax-h3-lite) | MiniMax | `POST /v1/videos/generations` | [models/minimax-h3-lite](models/minimax-h3-lite) |
| [MOSS Video and Audio](https://empiriolabs.ai/models/moss-video-and-audio) | OpenMOSS | `POST /v1/videos/generations` | [models/moss-video-and-audio](models/moss-video-and-audio) |
| [Pixverse Avatar](https://empiriolabs.ai/models/pixverse-avatar) | PixVerse | `POST /v1/videos/generations` | [models/pixverse-avatar](models/pixverse-avatar) |
| [Pixverse C1](https://empiriolabs.ai/models/pixverse-c1) | PixVerse | `POST /v1/videos/generations` | [models/pixverse-c1](models/pixverse-c1) |
| [Pixverse Edit](https://empiriolabs.ai/models/pixverse-edit) | PixVerse | `POST /v1/videos/generations` | [models/pixverse-edit](models/pixverse-edit) |
| [Pixverse Lip Sync](https://empiriolabs.ai/models/pixverse-lipsync) | PixVerse | `POST /v1/videos/generations` | [models/pixverse-lipsync](models/pixverse-lipsync) |
| [Pixverse v5](https://empiriolabs.ai/models/pixverse-v5) | PixVerse | `POST /v1/videos/generations` | [models/pixverse-v5](models/pixverse-v5) |
| [Pixverse v5.6](https://empiriolabs.ai/models/pixverse-v5-6) | PixVerse | `POST /v1/videos/generations` | [models/pixverse-v5-6](models/pixverse-v5-6) |
| [Pixverse v6](https://empiriolabs.ai/models/pixverse-v6) | PixVerse | `POST /v1/videos/generations` | [models/pixverse-v6](models/pixverse-v6) |
| [PixVerse V6 Max](https://empiriolabs.ai/models/pixverse-v6-max) | PixVerse | `POST /v1/videos/generations` | [models/pixverse-v6-max](models/pixverse-v6-max) |
| [Seedance 2.0 Fast](https://empiriolabs.ai/models/seedance-2-0-fast) | ByteDance | `POST /v1/videos/generations` | [models/seedance-2-0-fast](models/seedance-2-0-fast) |
| [Seedance 2.0 Mini](https://empiriolabs.ai/models/seedance-2-0-mini) | ByteDance | `POST /v1/videos/generations` | [models/seedance-2-0-mini](models/seedance-2-0-mini) |
| [Seedance 2.0 Pro](https://empiriolabs.ai/models/seedance-2-0-pro) | ByteDance | `POST /v1/videos/generations` | [models/seedance-2-0-pro](models/seedance-2-0-pro) |
| [Seedance 2.5](https://empiriolabs.ai/models/seedance-2-5) | ByteDance | `POST /v1/videos/generations` | [models/seedance-2-5](models/seedance-2-5) |
| [Seedance 2.5 Flash](https://empiriolabs.ai/models/seedance-2-5-flash) | ByteDance | `POST /v1/videos/generations` | [models/seedance-2-5-flash](models/seedance-2-5-flash) |
| [Sonilo Video Analysis](https://empiriolabs.ai/models/sonilo-video-analysis) | Sonilo | `POST /v1/chat/completions` | [models/sonilo-video-analysis](models/sonilo-video-analysis) |
| [Sonilo Video to Video](https://empiriolabs.ai/models/sonilo-video-to-video) | Sonilo | `POST /v1/videos/generations` | [models/sonilo-video-to-video](models/sonilo-video-to-video) |
| [Sonilo Video Translation](https://empiriolabs.ai/models/sonilo-video-translation) | Sonilo | `POST /v1/videos/generations` | [models/sonilo-video-translation](models/sonilo-video-translation) |
| [SVI 2.0 Pro](https://empiriolabs.ai/models/svi-2-0-pro) | VITA-Group / EPFL | `POST /v1/videos/generations` | [models/svi-2-0-pro](models/svi-2-0-pro) |
| [Wan 2.1](https://empiriolabs.ai/models/wan-2-1) | Alibaba Cloud | `POST /v1/videos/generations` | [models/wan-2-1](models/wan-2-1) |
| [Wan 2.2](https://empiriolabs.ai/models/wan-2-2) | Alibaba Cloud | `POST /v1/videos/generations` | [models/wan-2-2](models/wan-2-2) |
| [Wan 2.5](https://empiriolabs.ai/models/wan-2-5) | Alibaba Cloud | `POST /v1/videos/generations` | [models/wan-2-5](models/wan-2-5) |
| [Wan 2.6](https://empiriolabs.ai/models/wan-2-6) | Alibaba Cloud | `POST /v1/videos/generations` | [models/wan-2-6](models/wan-2-6) |
| [Wan 2.7](https://empiriolabs.ai/models/wan-2-7) | Alibaba Cloud | `POST /v1/videos/generations` | [models/wan-2-7](models/wan-2-7) |
| [Wan 3.0](https://empiriolabs.ai/models/wan-3-0) | Alibaba Cloud | `POST /v1/videos/generations` | [models/wan-3-0](models/wan-3-0) |

## How this repository is generated

A scheduled workflow reads the public examples feed (https://catalog.empiriolabs.ai/examples.json) every hour, regenerates `README.md` and `models/` with `scripts/build_examples.py`, and commits any change. Edits to those files are overwritten; to report a problem with an example, open an issue.

## More from EmpirioLabs AI

- [Documentation](https://docs.empiriolabs.ai)
- [Model catalog and pricing](https://empiriolabs.ai/models)
- [Playground](https://platform.empiriolabs.ai/dashboard/playground)
- [Agent skills](https://github.com/EmpirioLabs-AI/skills)
- [Remote MCP server](https://github.com/EmpirioLabs-AI/mcp)

## License

MIT No Attribution (MIT-0): copy the code into your own projects without attribution. See [LICENSE](LICENSE).
