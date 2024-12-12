from fastapi import APIRouter
from app.src.service.question_service import QuestionService

router = APIRouter()
question_service = QuestionService()

@router.get("/ask-KM-question")
async def ask_question(question: str):
    return {"response": question_service.process_question(question)}

@router.get("/display-KM-questions")
async def display_questions():
    return question_service.db_service.fetch_all_questions()

@router.get("/delete-KM-question")
async def delete_question(index: int):
    return question_service.db_service.delete_question(index)
