from langchain.tools import Tool
from .calculator import Calculator

def execute_calculation(user_input: str) -> str:
    try:
        parts = user_input.split()
        if len(parts) != 3:
            return "ERROR: Format should be 'number1 operation number2'"
        left_operand = float(parts[0])
        operation_type = parts[1]
        right_operand = float(parts[2])
        calculator = Calculator((left_operand, right_operand))
        result = calculator.calculate(operation_type)
        return str(result)
    except Exception as error:
        return f"ERROR: {str(error)}"

calculator_tool = Tool(name="Calculator",
                       func=execute_calculation,
                       description="Useful for mathematical calculations. Input format: 'number1 operation number2'. Operations: addition, subtraction, multiplication, division. Example: '5 addition 3'")