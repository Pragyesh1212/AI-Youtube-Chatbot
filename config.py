import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# API
# ==========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ==========================
# Models
# ==========================

LLM_MODEL = "llama-3.3-70b-versatile"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================
# Chunking
# ==========================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ==========================
# Retrieval
# ==========================

TOP_K = 6

# ==========================
# Cache
# ==========================

TRANSCRIPT_CACHE = "data/transcripts"
FAISS_CACHE = "data/faiss"