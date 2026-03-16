class Calculator:
    def __init__(self, numbers : tuple[float, float] = (0.0, 0.0)):
        self.set_numbers(numbers)
    
    def set_numbers(self, numbers : tuple[float, float]):
        self.numbers = numbers

    def calculate(self, operation: str = "addition") -> float:
        if operation == "addition":
            return self.numbers[0]+self.numbers[1]
        elif operation == "subtraction":
            return self.numbers[0]-self.numbers[1]
        elif operation == "multiplication":
            return self.numbers[0]*self.numbers[1]
        elif operation == "division":
            if self.numbers[1] == 0:
                print("ERROR: UNDEFINED DIVISION BY ZERO!")
                return 0.0
            return self.numbers[0]/self.numbers[1]
        print("ERROR: INVALID OPERATION.")
        return 0.0