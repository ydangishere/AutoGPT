# YouTube Transcript MVP — Minimal Prototype

This is a **standalone proof-of-concept** for fetching YouTube transcripts.
It is isolated under `autogpt/experiments/` and does not touch any AutoGPT core files.

## Purpose

Demonstrate the core idea: **YouTube URL → fetch transcript → print text.**
This MVP is shared for maintainer feedback before building the full block integration.

## Why Supadata API?

YouTube actively blocks direct transcript requests from most IPs (local machines,
servers, Docker containers). This is a known limitation of `youtube-transcript-api`
and similar libraries in non-browser environments.

[Supadata](https://supadata.ai) is a dedicated API that reliably fetches YouTube
transcripts from any environment — no proxy, no cookies, no browser required.

**The API key in this file is a demo key for MVP testing only.**
It is not hardcoded in production. The full block (`youtube_summarizer.py`) exposes
the key as a user-configurable field with clear setup instructions.

## How to run

**Option 1 — Already have the AutoGPT repo:**
```bash
git checkout feature/transcript-mvp-minimal
pip install requests
python autogpt/experiments/transcript_mvp_minimal/main.py
```

**Option 2 — Clone this branch only (no need to clone the full repo):**
```bash
git clone --single-branch --branch feature/transcript-mvp-minimal https://github.com/ydangishere/AutoGPT.git
cd AutoGPT
pip install requests
python autogpt/experiments/transcript_mvp_minimal/main.py
```

Enter any public YouTube URL when prompted. The script prints the transcript text.

## What this is NOT

- Not production code
- Not integrated into the AutoGPT block system
- Not a final implementation
- The hardcoded API key is for demo only — production uses proper credential management

## Next step

Full block integration: `autogpt_platform/backend/backend/blocks/youtube_summarizer.py`
See branch: `feature/transcript-mvp`
