import re


def extract_video_id(url: str) -> str:
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"
    match = re.match(regex, url)
    return match.group(1) if match else ""