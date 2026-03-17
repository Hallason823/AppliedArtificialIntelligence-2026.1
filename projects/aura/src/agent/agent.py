from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from src.model.model import LLM
from src.tools.calculator_tool import calculator_tool

class Agent:
    def __init__(self):
        self.model = LLM()
        self.llm = None
        self.executor = None
        self.memory = ConversationBufferMemory(memory_key="chat_history")

    def initialize(self):
        self.llm = self.model.get_llm()
        self.executor = initialize_agent(tools=[calculator_tool], llm=self.llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                         verbose=True, memory=self.memory, handle_parsing_errors=True)
        return self

    def run(self, command: str) -> str:
        if self.executor is None:
            self.initialize()
        response = self.executor.run(command)
        return response