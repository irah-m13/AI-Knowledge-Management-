from app.src.models.base_record import BaseRecord
from app.src.database_conf.database import DatabaseConnection

class GPTRecord(BaseRecord):
    def __init__(self, question, timestamp):
        self.question = question
        self.timestamp = timestamp

    def save(self):
        conn = DatabaseConnection().connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO gpt_record (UserQuestion, Timestamp) VALUES (?, ?)",
            (self.question, self.timestamp)
        )
        conn.commit()
