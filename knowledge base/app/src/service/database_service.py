from app.src.models.gpt_record import GPTRecord
from datetime import datetime

class DatabaseService:
    def insert_question(self, question):
        record = GPTRecord(question, datetime.now())
        record.save()

    def get_question_history(self):
        # Retrieve history from the database
        pass
