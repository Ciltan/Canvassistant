"""
rag.py — RAG pipeline: semantic search over ChromaDB + GPT-4o-mini generation.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_DIR = Path(__file__).parent / "chroma_db"

# ── Shared model instances ──────────────────────────────────────────

_embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=OPENAI_API_KEY,
)

_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    openai_api_key=OPENAI_API_KEY,
)


def _get_vectorstore() -> Chroma:
    """Load the ChromaDB vector store."""
    return Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=_embeddings,
        collection_name="canvas_docs",
    )


def _get_retriever(k: int = 6, course_name: str | None = None):
    """Return a retriever, optionally filtered by course name."""
    vs = _get_vectorstore()
    search_kwargs = {"k": k}
    if course_name:
        search_kwargs["filter"] = {"course_name": course_name}
    return vs.as_retriever(search_kwargs=search_kwargs)


def _format_sources(docs: list) -> list[dict]:
    """Convert LangChain Document objects to serializable source dicts."""
    sources = []
    seen = set()
    for doc in docs:
        key = (doc.metadata.get("file_name"), doc.metadata.get("page_number"))
        if key not in seen:
            seen.add(key)
            sources.append({
                "course": doc.metadata.get("course_name", "Unknown"),
                "file": doc.metadata.get("file_name", "Unknown"),
                "page": doc.metadata.get("page_number", "?"),
                "snippet": doc.page_content[:200],
            })
    return sources


# ── Public API ───────────────────────────────────────────────────────


async def query(question: str, course_name: str | None = None) -> dict:
    """Answer a free-form question using RAG."""
    retriever = _get_retriever(k=6, course_name=course_name)
    docs = retriever.invoke(question)

    context = "\n\n---\n\n".join(doc.page_content for doc in docs)

    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are a helpful university study assistant. "
            "Answer the student's question based ONLY on the provided course materials. "
            "If the answer is not in the materials, say so. "
            "Be concise and clear. Use bullet points where helpful."
        )),
        ("human", (
            "Course Materials:\n{context}\n\n"
            "Question: {question}"
        )),
    ])

    chain = prompt | _llm
    response = chain.invoke({"context": context, "question": question})

    return {
        "answer": response.content,
        "sources": _format_sources(docs),
    }


async def get_topics(course_name: str | None = None) -> dict:
    """Analyze course material and return likely exam topics."""
    retriever = _get_retriever(k=20, course_name=course_name)
    search_query = f"key topics and important concepts for {course_name}" if course_name else "key topics and important concepts"
    docs = retriever.invoke(search_query)

    context = "\n\n---\n\n".join(doc.page_content for doc in docs)

    # Group by course
    courses_in_docs = set(doc.metadata.get("course_name", "Unknown") for doc in docs)

    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an expert university tutor. Based on the course materials provided, "
            "identify the most likely exam topics. For each topic, provide:\n"
            "1. Topic name\n"
            "2. Why it's likely to appear (frequency in materials, emphasis, etc.)\n"
            "3. Key concepts to study\n\n"
            "Group topics by course. Be specific and actionable."
        )),
        ("human", "Course Materials:\n{context}"),
    ])

    chain = prompt | _llm
    response = chain.invoke({"context": context})

    return {
        "topics": response.content,
        "courses_analyzed": list(courses_in_docs),
        "chunks_analyzed": len(docs),
    }


async def get_practice(course_name: str | None = None, topic: str | None = None) -> dict:
    """Generate 5 practice questions with answers from course material."""
    search_query = topic or course_name or "important exam concepts"
    retriever = _get_retriever(k=10, course_name=course_name)
    docs = retriever.invoke(search_query)

    context = "\n\n---\n\n".join(doc.page_content for doc in docs)

    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are a university tutor creating a practice quiz. "
            "Based on the course materials, generate exactly 5 practice questions.\n\n"
            "For each question, provide:\n"
            "1. The question\n"
            "2. The model answer\n"
            "3. Which lecture/file it's based on\n\n"
            "Mix question types: multiple-choice, short answer, and explain-type questions. "
            "Make them exam-realistic."
        )),
        ("human", (
            "Course Materials:\n{context}\n\n"
            "Focus area: {topic}"
        )),
    ])

    chain = prompt | _llm
    response = chain.invoke({
        "context": context,
        "topic": topic or course_name or "general review",
    })

    return {
        "questions": response.content,
        "sources": _format_sources(docs),
    }


async def get_summary(course_name: str) -> dict:
    """Summarize all lecture slides for a given course."""
    retriever = _get_retriever(k=20, course_name=course_name)
    docs = retriever.invoke(f"complete overview and summary of {course_name}")

    if not docs:
        return {
            "summary": f"No materials found for course '{course_name}'.",
            "sources": [],
        }

    context = "\n\n---\n\n".join(doc.page_content for doc in docs)

    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are a university study assistant. Provide a comprehensive but concise summary "
            "of the course materials provided. Structure your summary as:\n"
            "1. Course overview (2-3 sentences)\n"
            "2. Key topics covered (bulleted list)\n"
            "3. Important concepts and definitions\n"
            "4. Relationships between topics\n\n"
            "Be thorough but concise. A student should be able to use this for quick revision."
        )),
        ("human", "Course Materials for {course_name}:\n{context}"),
    ])

    chain = prompt | _llm
    response = chain.invoke({"context": context, "course_name": course_name})

    return {
        "summary": response.content,
        "course": course_name,
        "chunks_analyzed": len(docs),
        "sources": _format_sources(docs),
    }


def get_available_courses() -> list[str]:
    """Return a list of unique course names from the vector store."""
    try:
        vs = _get_vectorstore()
        collection = vs._collection
        result = collection.get(include=["metadatas"])
        courses = set()
        for meta in result["metadatas"]:
            if meta and "course_name" in meta:
                courses.add(meta["course_name"])
        return sorted(courses)
    except Exception:
        return []
