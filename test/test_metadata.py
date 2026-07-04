from services.metadata import get_video_metadata

url = "https://www.youtube.com/watch?v=aircAruvnKk"

info = get_video_metadata(url)

print(info)