from fastapi import APIRouter, Query
from app.src.service.llm_service import LLMService

router = APIRouter()

@router.get("/")
async def get_answer(question: str = Query(...), keyword: str = Query("chatgpt")):
    return LLMService().generate_answer(question, keyword)
