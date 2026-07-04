from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from langchain_groq import ChatGroq

from config import (
    GROQ_API_KEY,
    LLM_MODEL,
    TOP_K,
)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def build_rag_chain(vector_store):

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 6,
            "fetch_k": 20,
            "lambda_mult": 0.7,
        },
    )

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=LLM_MODEL,
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert YouTube AI assistant.

Use ONLY the transcript context below.

If the transcript does not contain the answer, say:

"I couldn't find that information in the video's transcript."

Transcript:

{context}

Question:

{question}

Answer:
"""
    )

    chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain