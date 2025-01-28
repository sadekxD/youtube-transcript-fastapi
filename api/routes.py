from fastapi import APIRouter, HTTPException
from services.youtube_services import get_youtube_transcript
from core.logging import logger
router = APIRouter()


@router.get("/youtube-transcript")
async def get_youtube_transcript_route(url: str):
    try:
        transcript = get_youtube_transcript(url)
        return transcript
    except Exception as e:
        logger.error(f"Error in get_youtube_transcript_route: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
