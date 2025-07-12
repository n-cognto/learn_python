""" Day 28: Basic Project: Command-line Calculator """

class Calculator:
    """A comprehensive calculator class with error handling"""
    
    def __init__(self, a: float, b: float):
        """Initialize calculator with two numbers"""
        self.a = a
        self.b = b
    
    def add(self) -> float:
        """Addition: a + b"""
        return self.a + self.b
    
    def subtract(self) -> float:
        """Subtraction: a - b"""
        return self.a - self.b
    
    def multiply(self) -> float:
        """Multiplication: a * b"""
        return self.a * self.b
    
    def divide(self) -> str | float:
        """Division: a / b"""
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b
    
    def floor_divide(self) -> str | int:
        """Floor division: a // b"""
        if self.b == 0:
            return "Error: Division by zero"
        return self.a // self.b
    
    def modulus(self) -> str | float:
        """Modulus: a % b"""
        if self.b == 0:
            return "Error: Division by zero"
        return self.a % self.b
    
    def power(self) -> float:
        """Exponentiation: a ** b"""
        try:
            return self.a ** self.b
        except OverflowError:
            return "Error: Result too large"
    
    def get_all_operations(self) -> dict:
        """Return all operations as a dictionary"""
        return {
            "Addition": self.add(),
            "Subtraction": self.subtract(),
            "Multiplication": self.multiply(),
            "Division": self.divide(),
            "Floor Division": self.floor_divide(),
            "Modulus": self.modulus(),
            "Exponentiation": self.power()
        }

def get_number(prompt: str) -> float:
    """Get a number from user with error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def interactive_calculator():
    """Interactive calculator mode"""
    print("=== Command-line Calculator ===")
    print("Available operations: +, -, *, /, //, %, **")
    
    while True:
        try:
            a = get_number("Enter first number: ")
            operation = input("Enter operation (+, -, *, /, //, %, **): ").strip()
            b = get_number("Enter second number: ")
            
            calc = Calculator(a, b)
            
            operations = {
                '+': calc.add(),
                '-': calc.subtract(),
                '*': calc.multiply(),
                '/': calc.divide(),
                '//': calc.floor_divide(),
                '%': calc.modulus(),
                '**': calc.power()
            }
            
            if operation in operations:
                result = operations[operation]
                print(f"Result: {a} {operation} {b} = {result}")
            else:
                print("Invalid operation! Please use: +, -, *, /, //, %, **")
            
            if input("\nContinue? (y/n): ").lower() != 'y':
                break
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

def demo_all_operations():
    """Demonstrate all calculator operations"""
    print("\n=== Calculator Demo ===")
    
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    
    calc = Calculator(a, b)
    results = calc.get_all_operations()
    
    print(f"\nResults for {a} and {b}:")
    print("-" * 30)
    for operation, result in results.items():
        print(f"{operation:15}: {result}")

def main():
    """Main function to run the calculator"""
    while True:
        print("\n1. Interactive Calculator")
        print("2. Demo All Operations")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            interactive_calculator()
        elif choice == '2':
            demo_all_operations()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

# EXERCISES:
# 1. Add trigonometric functions (sin, cos, tan) to the calculator
# 2. Implement a square root function with error handling for negative numbers
# 3. Create a history feature that stores previous calculations
# 4. Add support for calculating with more than two numbers
# 5. Implement a scientific calculator mode with logarithms and advanced functions
# 6. Add the ability to save and load calculations from a file