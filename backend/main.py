"""
main.py — FastAPI backend for Canvas Study AI.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

import rag

load_dotenv()

app = FastAPI(
    title="Canvas Study AI",
    description="AI-powered study assistant for NUS Canvas courses",
    version="1.0.0",
)

# ── CORS — allow Chrome extension & local dev ───────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Request / Response models ───────────────────────────────────────

class QueryRequest(BaseModel):
    question: str
    course_name: str | None = None


class TopicsRequest(BaseModel):
    course_name: str | None = None


class PracticeRequest(BaseModel):
    course_name: str | None = None
    topic: str | None = None


class SummarizeRequest(BaseModel):
    course_name: str


# ── Endpoints ────────────────────────────────────────────────────────

@app.get("/")
async def root():
    return {
        "message": "Canvas Study AI API is running",
        "endpoints": ["/query", "/topics", "/practice", "/summarize", "/courses"],
    }


@app.get("/courses")
async def list_courses():
    """Return a list of available courses in the vector store."""
    courses = rag.get_available_courses()
    return {"courses": courses}


@app.post("/query")
async def query_endpoint(req: QueryRequest):
    """Free-form Q&A over course materials."""
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    try:
        result = await rag.query(req.question, req.course_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/topics")
async def topics_endpoint(req: TopicsRequest):
    """Analyze material and return likely exam topics."""
    try:
        result = await rag.get_topics(req.course_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/practice")
async def practice_endpoint(req: PracticeRequest):
    """Generate practice questions from course material."""
    try:
        result = await rag.get_practice(req.course_name, req.topic)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summarize")
async def summarize_endpoint(req: SummarizeRequest):
    """Summarize a course's lecture slides."""
    if not req.course_name.strip():
        raise HTTPException(status_code=400, detail="Course name cannot be empty.")
    try:
        result = await rag.get_summary(req.course_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
