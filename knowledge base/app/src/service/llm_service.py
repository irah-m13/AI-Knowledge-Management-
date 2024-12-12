from app.src.ai_service.azure_model import AzureAIModel
from app.src.service.database_service import DatabaseService

class LLMService:
    def __init__(self):
        self.model = AzureAIModel()
        self.db_service = DatabaseService()

    def generate_answer(self, question: str, keyword: str):
        self.db_service.insert_question(question)
        return self.model.generate_response(question)
