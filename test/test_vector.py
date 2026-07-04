from transcript import get_transcript
from vector_store import create_vector_store

video_id = "etnLX7m2MiA"

print("Downloading transcript...")

text = get_transcript(video_id)

print("Creating vector database...")

db = create_vector_store(text)

print("Done!")

docs = db.similarity_search(
    "What is the video about?",
    k=2
)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(docs, 1):
    print(f"Document {i}")
    print("-" * 40)
    print(doc.page_content)
    print()