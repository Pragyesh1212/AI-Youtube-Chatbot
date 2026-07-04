from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str):
    """
    Extract video ID from a YouTube URL or return
    the input if it's already a video ID.
    """

    if len(url) == 11:
        return url

    parsed = urlparse(url)

    if parsed.hostname == "youtu.be":
        return parsed.path[1:]

    if parsed.hostname in [
        "www.youtube.com",
        "youtube.com",
        "m.youtube.com",
    ]:
        query = parse_qs(parsed.query)

        if "v" in query:
            return query["v"][0]

    raise ValueError("Invalid YouTube URL")


def get_thumbnail_url(video_id: str):
    return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"