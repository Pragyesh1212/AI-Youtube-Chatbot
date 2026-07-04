from transcript import get_transcript
from vector_store import create_vector_store
from rag import build_rag_chain

video = "etnLX7m2MiA"

print("Downloading transcript...")
text = get_transcript(video)

print("Creating vector database...")
db = create_vector_store(text)

print("Loading Groq...")
chain = build_rag_chain(db)

print()

while True:

    question = input("You : ")

    if question.lower() == "exit":
        break

    answer = chain.invoke(question)

    print()
    print(answer)
    print()