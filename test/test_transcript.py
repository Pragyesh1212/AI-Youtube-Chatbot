from transcript import get_transcript

video_id = "etnLX7m2MiA"

text = get_transcript(video_id)

print("\nTranscript Length:", len(text))
print("\nPreview:\n")
print(text[:1000])