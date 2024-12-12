from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class AzureLLM:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            model="gpt-35-turbo-16k",
            deployment_name="gpt-35-turbo-16k",
            api_key=os.getenv("AZURE_API_KEY"),
            azure_endpoint=os.getenv("AZURE_ENDPOINT"),
            api_version=os.getenv("AZURE_API_VERSION"),
        )

    def get_llm(self):
        return self.llm
