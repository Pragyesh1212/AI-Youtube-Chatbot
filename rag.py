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

    Use ONLY the transcript context below to answer the user's question.

    IMPORTANT LANGUAGE RULE:
    - If the user's question is in English, answer entirely in English.
    - If the user's question is in Hindi, answer entirely in Hindi.
    - If the user's question is a mixture of Hindi and English (Hinglish), answer in the same mixed style.
    - Do not unnecessarily translate the user's question or transcript.
    - Keep technical terms such as Python, API, FAISS, RAG, Time Complexity, Big-O, etc. in their standard English form when appropriate.

    IMPORTANT ACCURACY RULE:
    - Answer only using information available in the transcript context.
    - Do not add information from your general knowledge.
    - If the transcript does not contain the answer, say:
    "I couldn't find that information in the video's transcript."

    ANSWER STYLE:
    - For simple questions, give a concise answer.
    - For summary questions, provide clear bullet points.
    - For detailed questions, explain the answer with relevant details from the transcript.
    - Avoid unnecessary repetition.

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