from youtube_transcript_api import YouTubeTranscriptApi
from fastapi import HTTPException
from utils.helpers import extract_video_id
from core.config import settings


def get_youtube_transcript(url: str) -> str:
    video_id = extract_video_id(url)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id,
            languages=["en"],
            proxies={
                "http": "http://" + settings.PROXY_URL,
                "https": "https://" + settings.PROXY_URL,
            },
        )
        full_transcript = " ".join([entry["text"] for entry in transcript])
        return full_transcript
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to fetch transcript: {str(e)}"
        )