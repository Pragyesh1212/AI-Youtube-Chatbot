import yt_dlp


def get_video_metadata(video_url: str):
    """
    Fetch metadata for a YouTube video.
    """

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(video_url, download=False)

    return {
        "title": info.get("title"),
        "channel": info.get("uploader"),
        "thumbnail": info.get("thumbnail"),
        "duration": info.get("duration"),
        "upload_date": info.get("upload_date"),
    }