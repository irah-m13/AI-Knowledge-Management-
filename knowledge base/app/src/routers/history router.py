from fastapi import APIRouter
from app.src.service.database_service import DatabaseService

router = APIRouter()

@router.get("/")
async def get_history():
    return DatabaseService().get_question_history()
