from langchain.agents import initialize_agent, AgentType
from src.model.model import LLM
from src.tools.calculator_tool import calculator_tool
import os

class Agent:
    def __init__(self):
        self.model = LLM()
        self.llm = None
        self.executor = None
        self.prompt = self._load_prompt()

    def _load_prompt(self):
        prompt_path = os.path.join(os.path.dirname(__file__), "../../data/prompt")
        try:
            with open(prompt_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "You are a helpful assistant."

    def initialize(self):
        self.llm = self.model.get_llm()
        self.executor = initialize_agent(
            tools=[calculator_tool],
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3,
            early_stopping_method="generate",
            agent_kwargs={
                "prefix": self.prompt,
                "format_instructions": "Use this exact format:\nThought: what to do\nAction: Calculator\nAction Input: number operation number\nObservation: result\nFinal Answer: answer"
            }
        )
        return self

    def run(self, command: str) -> str:
        if self.executor is None:
            self.initialize()
        response = self.executor.run(command)
        return response