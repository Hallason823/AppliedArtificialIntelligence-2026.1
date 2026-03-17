from src.manager.task_manager import TaskManager

def main():
    print("=" * 50)
    print("AURA - Intelligent Agent")
    print("=" * 50)
    print("Initializing agent...")
    manager = TaskManager()
    manager.initialize()
    print("Agent ready! Type 'exit' or 'quit' to stop.\n")
    while True:
        user_input = input("You: ").strip()
        if manager.is_exit_command(user_input):
            print("Goodbye!")
            break
        if not manager.is_valid_command(user_input):
            continue
        try:
            response = manager.execute_task(user_input)
            print(f"\nAgent: {response}\n")
        except Exception as error:
            print(f"\nERROR: {str(error)}\n")

if __name__ == "__main__":
    main()