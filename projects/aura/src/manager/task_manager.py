from src.agent.agent import Agent

class TaskManager:
    def __init__(self):
        self.agent = Agent()
        self.is_initialized = False

    def initialize(self):
        if not self.is_initialized:
            self.agent.initialize()
            self.is_initialized = True

    def execute_task(self, task: str) -> str:
        if not self.is_initialized:
            self.initialize()
        return self.agent.run(task)

    def is_exit_command(self, command: str) -> bool:
        return command.lower() in ['exit', 'quit', 'stop']

    def is_valid_command(self, command: str) -> bool:
        return bool(command and command.strip())