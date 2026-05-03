# Standalone MVP prototype — NOT production code.
# Purpose: proof-of-concept for YouTube transcript fetching.
# This script is isolated and does not touch any AutoGPT core files.
#
# Note: Uses Supadata API (hardcoded key) for demo purposes only.
# YouTube blocks direct transcript requests from most server/local IPs.
# Production implementation will use proper credential management.
#
# Dependency: pip install requests
# Run: python autogpt/experiments/transcript_mvp_minimal/main.py

import re
import sys
import requests

# Demo API key for MVP testing only — not for production use.
# Get a free key at https://supadata.ai (100 requests/month, no credit card)
SUPADATA_API_KEY = "sd_c5133ff7df29f63070a3e5d90703a096"
SUPADATA_ENDPOINT = "https://api.supadata.ai/v1/transcript"

# Ensure UTF-8 output on all platforms (including Windows terminals)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def extract_video_id(url: str) -> str:
    """Extract 11-character video ID from a YouTube URL."""
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11})",
        r"youtu\.be\/([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract video ID from: {url}")


def fetch_transcript(video_id: str) -> str:
    """Fetch transcript via Supadata API and return as plain text."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(
        SUPADATA_ENDPOINT,
        params={"url": url, "text": "true", "lang": "en"},
        headers={"x-api-key": SUPADATA_API_KEY},
        timeout=15,
    )
    if not response.ok:
        raise RuntimeError(f"Supadata API error {response.status_code}: {response.text[:200]}")
    return response.json().get("content", "")


def main():
    url = input("Enter YouTube URL: ").strip()

    print("Extracting video ID...")
    video_id = extract_video_id(url)
    print(f"Video ID: {video_id}")

    print("Fetching transcript...")
    try:
        transcript = fetch_transcript(video_id)
    except Exception as e:
        print(f"Error: {e}")
        return

    print(f"\nTranscript ({len(transcript)} characters):\n")
    print(transcript)


if __name__ == "__main__":
    main()
