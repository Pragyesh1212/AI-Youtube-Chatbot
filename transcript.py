import os

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

from config import TRANSCRIPT_CACHE

...
# keep the imports above from youtube_transcript_api
...


def get_transcript(video_id):

    os.makedirs(TRANSCRIPT_CACHE, exist_ok=True)

    cache_file = os.path.join(
        TRANSCRIPT_CACHE,
        f"{video_id}.txt"
    )

    # Load cached transcript
    if os.path.exists(cache_file):

        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()

    api = YouTubeTranscriptApi()

    transcript_list = api.list(video_id)

    transcript = None

    for lang in ["en", "en-US", "hi"]:

        try:
            transcript = transcript_list.find_transcript([lang])
            break
        except:
            pass

    if transcript is None:
        transcript = next(iter(transcript_list))

    fetched = transcript.fetch()

    text = " ".join(
        chunk.text if hasattr(chunk, "text")
        else chunk["text"]
        for chunk in fetched
    )

    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(text)

    return text