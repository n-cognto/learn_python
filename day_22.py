""" Day 22: Creating and Using Custom Modules """

import sys
import os
from pathlib import Path

# Add the current directory to Python path for custom imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

def create_utility_module():
    """Create a comprehensive utility module"""
    module_content = '''"""
Custom utility module for mathematical and string operations
"""

import math
import random
from typing import List, Union

# Module constants
VERSION = "1.0.0"
AUTHOR = "Python Learner"

def greet(name: str) -> str:
    """
    Greet a person by name
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to custom modules!"

def calculate_area(shape: str, **kwargs) -> float:
    """
    Calculate area of different shapes
    
    Args:
        shape (str): The shape type ('rectangle', 'circle', 'triangle')
        **kwargs: Shape-specific parameters
        
    Returns:
        float: The calculated area
    """
    shape = shape.lower()
    
    if shape == 'rectangle':
        return kwargs.get('length', 0) * kwargs.get('width', 0)
    elif shape == 'circle':
        radius = kwargs.get('radius', 0)
        return math.pi * radius * radius
    elif shape == 'triangle':
        base = kwargs.get('base', 0)
        height = kwargs.get('height', 0)
        return 0.5 * base * height
    else:
        raise ValueError(f"Unknown shape: {shape}")

def generate_password(length: int = 12, include_special: bool = True) -> str:
    """
    Generate a random password
    
    Args:
        length (int): Length of the password (default: 12)
        include_special (bool): Include special characters (default: True)
        
    Returns:
        str: Generated password
    """
    import string
    
    chars = string.ascii_letters + string.digits
    if include_special:
        chars += "!@#$%^&*"
    
    return ''.join(random.choice(chars) for _ in range(length))

def analyze_text(text: str) -> dict:
    """
    Analyze text and return statistics
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Text analysis results
    """
    words = text.split()
    return {
        'character_count': len(text),
        'word_count': len(words),
        'sentence_count': text.count('.') + text.count('!') + text.count('?'),
        'average_word_length': sum(len(word) for word in words) / len(words) if words else 0,
        'longest_word': max(words, key=len) if words else '',
        'unique_words': len(set(word.lower() for word in words))
    }

def fibonacci(n: int) -> List[int]:
    """
    Generate Fibonacci sequence up to n terms
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        List[int]: Fibonacci sequence
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

def is_prime(num: int) -> bool:
    """
    Check if a number is prime
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if prime, False otherwise
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(limit: int) -> List[int]:
    """
    Get all prime numbers up to a limit
    
    Args:
        limit (int): Upper limit for prime search
        
    Returns:
        List[int]: List of prime numbers
    """
    return [num for num in range(2, limit + 1) if is_prime(num)]

class Calculator:
    """A simple calculator class"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """Get calculation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()

# Module-level variables
PI = 3.14159
E = 2.71828

# Module initialization
def _initialize():
    """Initialize the module"""
    print(f"Custom Utils Module v{VERSION} by {AUTHOR} loaded successfully!")

# This runs when the module is imported
if __name__ != "__main__":
    _initialize()

# This runs when the module is executed directly
if __name__ == "__main__":
    print("Running custom_utils module directly...")
    print(f"Module version: {VERSION}")
    print(f"Greeting: {greet('Direct Runner')}")
    print(f"Rectangle area (5x3): {calculate_area('rectangle', length=5, width=3)}")
    print(f"Circle area (radius=2): {calculate_area('circle', radius=2)}")
    print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
    print(f"Primes up to 20: {get_primes(20)}")
'''
    
    # Write the module to a file
    with open('custom_utils.py', 'w') as f:
        f.write(module_content)
    
    print("Created custom_utils.py module")

def demonstrate_module_usage():
    """Demonstrate using the custom module"""
    print("\n=== Custom Module Usage Demo ===")
    
    try:
        # Import the custom module
        import custom_utils
        
        # Use module functions
        print(f"Greeting: {custom_utils.greet('Python Learner')}")
        print(f"Module version: {custom_utils.VERSION}")
        print(f"Module author: {custom_utils.AUTHOR}")
        
        # Test mathematical functions
        print(f"\nMathematical Functions:")
        print(f"Rectangle area (4x6): {custom_utils.calculate_area('rectangle', length=4, width=6)}")
        print(f"Circle area (radius=3): {custom_utils.calculate_area('circle', radius=3):.2f}")
        print(f"Triangle area (base=8, height=5): {custom_utils.calculate_area('triangle', base=8, height=5)}")
        
        # Test utility functions
        print(f"\nUtility Functions:")
        password = custom_utils.generate_password(8, False)
        print(f"Generated password: {password}")
        
        # Test text analysis
        sample_text = "Python is amazing! It's powerful and easy to learn."
        analysis = custom_utils.analyze_text(sample_text)
        print(f"\nText Analysis for: '{sample_text}'")
        for key, value in analysis.items():
            print(f"  {key}: {value}")
        
        # Test mathematical sequences
        print(f"\nFibonacci sequence (8 terms): {custom_utils.fibonacci(8)}")
        print(f"Prime numbers up to 30: {custom_utils.get_primes(30)}")
        
        # Test the Calculator class
        calc = custom_utils.Calculator()
        print(f"\nCalculator Demo:")
        print(f"5 + 3 = {calc.add(5, 3)}")
        print(f"10 - 4 = {calc.subtract(10, 4)}")
        print(f"7 * 6 = {calc.multiply(7, 6)}")
        print(f"15 / 3 = {calc.divide(15, 3)}")
        print(f"History: {calc.get_history()}")
        
    except ImportError as e:
        print(f"Error importing custom module: {e}")
    except Exception as e:
        print(f"Error using custom module: {e}")

def demonstrate_import_variations():
    """Demonstrate different ways to import from custom modules"""
    print("\n=== Import Variations Demo ===")
    
    try:
        # Method 1: Import entire module
        import custom_utils
        print(f"Method 1 - Full import: {custom_utils.greet('User1')}")
        
        # Method 2: Import specific functions
        from custom_utils import greet, fibonacci
        print(f"Method 2 - Specific import: {greet('User2')}")
        print(f"Fibonacci (5): {fibonacci(5)}")
        
        # Method 3: Import with alias
        from custom_utils import calculate_area as calc_area
        print(f"Method 3 - Alias import: {calc_area('circle', radius=5):.2f}")
        
        # Method 4: Import class
        from custom_utils import Calculator
        my_calc = Calculator()
        print(f"Method 4 - Class import: {my_calc.add(10, 20)}")
        
    except ImportError as e:
        print(f"Import error: {e}")

def create_package_structure():
    """Create a sample package structure"""
    print("\n=== Package Structure Demo ===")
    
    # Create a package directory
    package_dir = Path("my_package")
    package_dir.mkdir(exist_ok=True)
    
    # Create __init__.py
    init_content = '''"""
My Package - A sample Python package
"""

__version__ = "1.0.0"
__author__ = "Python Learner"

from .math_utils import add, multiply
from .string_utils import reverse_string, count_words

# Package-level function
def package_info():
    return f"My Package v{__version__} by {__author__}"
'''
    
    with open(package_dir / "__init__.py", "w") as f:
        f.write(init_content)
    
    # Create math_utils.py
    math_utils_content = '''"""
Mathematical utility functions
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def power(base, exponent):
    """Calculate base raised to exponent"""
    return base ** exponent
'''
    
    with open(package_dir / "math_utils.py", "w") as f:
        f.write(math_utils_content)
    
    # Create string_utils.py
    string_utils_content = '''"""
String utility functions
"""

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_words(text):
    """Count words in a text"""
    return len(text.split())

def capitalize_words(text):
    """Capitalize each word"""
    return text.title()
'''
    
    with open(package_dir / "string_utils.py", "w") as f:
        f.write(string_utils_content)
    
    print("Created package structure:")
    print("my_package/")
    print("  __init__.py")
    print("  math_utils.py")
    print("  string_utils.py")
    
    # Demonstrate package usage
    try:
        import my_package
        print(f"\nPackage info: {my_package.package_info()}")
        print(f"Add function: {my_package.add(5, 3)}")
        print(f"Multiply function: {my_package.multiply(4, 7)}")
        print(f"Reverse string: {my_package.reverse_string('Python')}")
        print(f"Count words: {my_package.count_words('Hello World Python')}")
        
    except ImportError as e:
        print(f"Package import error: {e}")

def module_best_practices():
    """Demonstrate module best practices"""
    print("\n=== Module Best Practices ===")
    
    practices = [
        "✓ Use descriptive module names (snake_case)",
        "✓ Include docstrings for modules, functions, and classes",
        "✓ Use __init__.py for packages",
        "✓ Handle imports gracefully with try/except",
        "✓ Use if __name__ == '__main__': for module testing",
        "✓ Keep modules focused on a single responsibility",
        "✓ Use type hints for better code documentation",
        "✓ Include version information in modules",
        "✓ Group related functions into classes when appropriate",
        "✓ Use relative imports within packages"
    ]
    
    for practice in practices:
        print(practice)

def main():
    """Main function to run all demonstrations"""
    create_utility_module()
    demonstrate_module_usage()
    demonstrate_import_variations()
    create_package_structure()
    module_best_practices()

if __name__ == "__main__":
    main()

# EXERCISES:
# 1. Create a module called 'student_manager.py' with a Student class and functions to manage students
# 2. Build a 'file_utilities.py' module with functions for reading, writing, and processing files
# 3. Create a 'data_analyzer.py' module with functions for statistical analysis
# 4. Build a package called 'web_scraper' with modules for different scraping tasks
# 5. Create a 'game_utils.py' module with functions for a simple text-based game
# 6. Build a 'crypto_utils.py' module with functions for encryption and decryption
# 7. Create a 'date_utilities.py' module with functions for date manipulation and formatting
# 8. Build a package for a library management system with separate modules
# 9. Create a 'network_utils.py' module with functions for network operations
# 10. Build a complete project using multiple custom modules and packages