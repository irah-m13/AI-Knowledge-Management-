import re
from app.src.utils.prompts.km_prompt import SQL_PROMPT_TEMPLATE
from app.src.service.database_service import DatabaseService
from app.src.ai_service.azure_model import AzureLLM

class QuestionService:
    def __init__(self):
        self.db_service = DatabaseService()
        self.llm = AzureLLM().get_llm()
        self.greeting_pattern = re.compile(r"^(hi|hello)$", re.IGNORECASE)

    def insert_question(self, question, index=0):
        return self.db_service.insert_into_database(question, index)

    def process_question(self, question):
        if self.greeting_pattern.match(question.strip()):
            self.insert_question(question)
            return "Hello! How can I assist you today?"
        else:
            prompt = SQL_PROMPT_TEMPLATE.format(query=question)
            return self.llm.run(prompt)
