from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

class LLM:
    def __init__(self, model_name: str = "llama-3.3-70b-versatile"):
        self.model_name = model_name
        self.llm = None

    def load_model(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables. Get one at https://console.groq.com/")
        self.llm = ChatGroq(model=self.model_name, temperature=0.1, groq_api_key=api_key)
        return self.llm

    def get_llm(self):
        if self.llm is None:
            return self.load_model()
        return self.llm