import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from config import (
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    FAISS_CACHE,
)


def create_vector_store(transcript, video_id):

    os.makedirs(FAISS_CACHE, exist_ok=True)

    db_path = os.path.join(
        FAISS_CACHE,
        video_id
    )

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    if os.path.exists(db_path):

        return FAISS.load_local(
            db_path,
            embeddings,
            allow_dangerous_deserialization=True
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    docs = splitter.create_documents([transcript])

    db = FAISS.from_documents(
        docs,
        embeddings
    )

    db.save_local(db_path)

    return db