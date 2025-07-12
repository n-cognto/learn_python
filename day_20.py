""" Day 20: Modules and import Statement """

import math
import random
import os
import sys
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import json

def basic_imports_demo():
    """Demonstrate basic import usage"""
    print("=== Basic Imports Demo ===")
    
    # Math module
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Pi value: {math.pi}")
    print(f"Ceiling of 4.2: {math.ceil(4.2)}")
    print(f"Floor of 4.8: {math.floor(4.8)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    
    # Random module
    print(f"\nRandom integer 1-10: {random.randint(1, 10)}")
    print(f"Random float 0-1: {random.random()}")
    colors = ["red", "blue", "green", "yellow"]
    print(f"Random choice: {random.choice(colors)}")
    
    # OS module
    print(f"\nCurrent working directory: {os.getcwd()}")
    print(f"Operating system: {os.name}")
    print(f"Environment PATH exists: {'PATH' in os.environ}")

def import_variations_demo():
    """Demonstrate different import methods"""
    print("\n=== Import Variations Demo ===")
    
    # 1. Basic import
    import time
    print(f"Current timestamp: {time.time()}")
    
    # 2. Import with alias
    import numpy as np  # This would work if numpy is installed
    # print(f"NumPy version: {np.__version__}")
    
    # 3. Import specific functions
    from math import sin, cos, tan, pi
    print(f"sin(π/2): {sin(pi/2)}")
    print(f"cos(π): {cos(pi)}")
    
    # 4. Import all (generally not recommended)
    # from math import *  # Avoid this in production code
    
    # 5. Import with different name
    from datetime import datetime as dt
    print(f"Current time: {dt.now()}")

def working_with_collections():
    """Demonstrate collections module"""
    print("\n=== Collections Module Demo ===")
    
    # Counter
    text = "hello world"
    letter_count = Counter(text)
    print(f"Letter frequency in '{text}': {letter_count}")
    print(f"Most common letter: {letter_count.most_common(1)}")
    
    # defaultdict
    dd = defaultdict(list)
    dd['fruits'].append('apple')
    dd['fruits'].append('banana')
    dd['vegetables'].append('carrot')
    print(f"DefaultDict: {dict(dd)}")

def datetime_module_demo():
    """Demonstrate datetime module usage"""
    print("\n=== DateTime Module Demo ===")
    
    now = datetime.now()
    print(f"Current date and time: {now}")
    print(f"Current date: {now.date()}")
    print(f"Current time: {now.time()}")
    
    # Date arithmetic
    tomorrow = now + timedelta(days=1)
    print(f"Tomorrow: {tomorrow.date()}")
    
    # Formatting
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Formatted: {formatted}")

def json_module_demo():
    """Demonstrate JSON module"""
    print("\n=== JSON Module Demo ===")
    
    # Python object to JSON
    data = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "coding"]
    }
    
    json_string = json.dumps(data, indent=2)
    print("JSON string:")
    print(json_string)
    
    # JSON to Python object
    parsed_data = json.loads(json_string)
    print(f"\nParsed back: {parsed_data['name']} is {parsed_data['age']} years old")

def sys_module_demo():
    """Demonstrate sys module"""
    print("\n=== Sys Module Demo ===")
    
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print(f"Python executable: {sys.executable}")
    print(f"Module search path (first 3): {sys.path[:3]}")

def module_best_practices():
    """Demonstrate module best practices"""
    print("\n=== Module Best Practices ===")
    
    # 1. Import at the top of the file
    print("✓ Import all modules at the top of your file")
    
    # 2. Use specific imports when possible
    print("✓ Use 'from module import function' for specific functions")
    
    # 3. Use aliases for long module names
    print("✓ Use aliases: import numpy as np")
    
    # 4. Avoid import * (star imports)
    print("✗ Avoid 'from module import *'")
    
    # 5. Group imports properly
    print("✓ Group imports: standard library, third-party, local")

def create_sample_module():
    """Create a sample module file"""
    module_content = '''"""
Sample utility module for demonstration
"""

def greet(name):
    """Greet a person by name"""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Calculate area of a rectangle"""
    return length * width

def get_random_quote():
    """Return a random motivational quote"""
    quotes = [
        "The only way to do great work is to love what you do.",
        "Innovation distinguishes between a leader and a follower.",
        "Stay hungry, stay foolish.",
        "Code is poetry."
    ]
    import random
    return random.choice(quotes)

# Module-level variable
PI = 3.14159

if __name__ == "__main__":
    print("This module is being run directly!")
    print(greet("Module User"))
'''
    
    try:
        with open("sample_utils.py", "w") as f:
            f.write(module_content)
        print("Created sample_utils.py module")
        
        # Now import and use it
        import sample_utils
        print(f"Greeting: {sample_utils.greet('Python Learner')}")
        print(f"Area: {sample_utils.calculate_area(5, 3)}")
        print(f"Quote: {sample_utils.get_random_quote()}")
        print(f"PI value: {sample_utils.PI}")
        
    except Exception as e:
        print(f"Error creating module: {e}")

def main():
    """Main function to run all demonstrations"""
    basic_imports_demo()
    import_variations_demo()
    working_with_collections()
    datetime_module_demo()
    json_module_demo()
    sys_module_demo()
    module_best_practices()
    create_sample_module()

if __name__ == "__main__":
    main()

# EXERCISES:
# 1. Create a module called 'calculator.py' with functions for basic math operations
# 2. Import and use the os module to list all files in the current directory
# 3. Use the random module to create a number guessing game
# 4. Create a module for date utilities that can format dates in different ways
# 5. Use the json module to save and load a dictionary to/from a file
# 6. Explore the statistics module and calculate mean, median, mode of a list
# 7. Create a module with classes and import specific classes from it
# 8. Use the pathlib module (modern alternative to os.path) for file operations
# 9. Create a package (directory with __init__.py) containing multiple modules
# 10. Use the importlib module to dynamically import modules at runtime
