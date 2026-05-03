# Standalone MVP prototype — NOT production code.
# Purpose: proof-of-concept for YouTube transcript fetching.
# This script is isolated and does not touch any AutoGPT core files.
#
# Dependency: pip install youtube-transcript-api
# Run: python autogpt/experiments/transcript_mvp_minimal/main.py

import re
import sys

# Ensure UTF-8 output on all platforms (including Windows terminals)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    CouldNotRetrieveTranscript,
    NoTranscriptFound,
    TranscriptsDisabled,
)


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
    """Fetch transcript for a YouTube video and return as plain text."""
    api = YouTubeTranscriptApi()
    fetched = api.fetch(video_id)
    return " ".join(snippet.text for snippet in fetched)


def main():
    url = input("Enter YouTube URL: ").strip()

    print("Extracting video ID...")
    video_id = extract_video_id(url)
    print(f"Video ID: {video_id}")

    print("Fetching transcript...")
    try:
        transcript = fetch_transcript(video_id)
    except TranscriptsDisabled:
        print("Error: Transcripts are disabled for this video.")
        return
    except NoTranscriptFound:
        print("Error: No transcript found for this video.")
        return
    except CouldNotRetrieveTranscript as e:
        print(f"Error: {e}")
        return

    print(f"\nTranscript ({len(transcript)} characters):\n")
    print(transcript)


if __name__ == "__main__":
    main()
