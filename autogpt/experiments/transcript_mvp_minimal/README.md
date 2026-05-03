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

## How to run

**Step 1 — Get a free Supadata API key:**

Go to [supadata.ai](https://supadata.ai) → Sign up free → Copy your API key.
100 requests/month, no credit card required.

**Step 2 — Set the environment variable:**

Windows:
```
set SUPADATA_API_KEY=your_key_here
```

Mac/Linux:
```
export SUPADATA_API_KEY=your_key_here
```

**Step 3 — Clone and run:**

Option A — Already have the AutoGPT repo:
```bash
git checkout feature/transcript-mvp-minimal
pip install requests
python autogpt/experiments/transcript_mvp_minimal/main.py
```

Option B — Clone this branch only:
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

## Next step

Full block integration: `autogpt_platform/backend/backend/blocks/youtube_summarizer.py`
See branch: `feature/transcript-mvp`
