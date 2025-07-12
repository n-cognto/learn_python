# Python Intermediate Programming - Phase 2 Complete Guide

"""
This guide covers all Phase 2 topics:
1. Functions & Scope
2. File Handling & Error Management  
3. Object-Oriented Programming
4. Modules & Packages
"""

print("="*60)
print("1. FUNCTIONS & SCOPE")
print("="*60)

# ============================================================================
# FUNCTION DEFINITION AND CALLING
# ============================================================================

def greet():
    """Simple function with no parameters"""
    print("Hello, World!")

def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

def greet_with_message(name, message="Nice to meet you!"):
    """Function with default parameter"""
    print(f"Hello, {name}! {message}")

# Calling functions
greet()
greet_person("Alice")
greet_with_message("Bob")
greet_with_message("Charlie", "How are you?")

# ============================================================================
# PARAMETERS, ARGUMENTS, AND RETURN VALUES
# ============================================================================

def add_numbers(x, y):
    """Function that returns a value"""
    return x + y

def calculate_rectangle_area(length, width):
    """Function with multiple parameters"""
    area = length * width
    return area

def get_user_info(name, age, city="Unknown"):
    """Function returning multiple values"""
    info = f"Name: {name}, Age: {age}, City: {city}"
    return name.upper(), age * 365, info  # Returns tuple

# Using return values
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

area = calculate_rectangle_area(10, 5)
print(f"Rectangle area: {area}")

upper_name, days_lived, info_string = get_user_info("Alice", 25, "New York")
print(f"Upper name: {upper_name}")
print(f"Days lived: {days_lived}")
print(f"Info: {info_string}")

# *args and **kwargs
def sum_all(*args):
    """Function accepting variable number of arguments"""
    return sum(args)

def print_info(**kwargs):
    """Function accepting keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
print("Person info:")
print_info(name="Alice", age=25, city="New York", job="Engineer")

# ============================================================================
# LOCAL VS GLOBAL SCOPE
# ============================================================================

# Global variable
global_var = "I'm global"

def scope_demo():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error!

# Modifying global variables
counter = 0

def increment_counter():
    global counter  # Need global keyword to modify
    counter += 1
    print(f"Counter inside function: {counter}")

increment_counter()
print(f"Counter outside function: {counter}")

# Nested function scope
def outer_function(x):
    def inner_function(y):
        return x + y  # x is from enclosing scope
    return inner_function

add_five = outer_function(5)
result = add_five(10)
print(f"Nested function result: {result}")

# ============================================================================
# LAMBDA FUNCTIONS
# ============================================================================

# Basic lambda functions
square = lambda x: x ** 2
add = lambda x, y: x + y
greet_lambda = lambda name: f"Hello, {name}!"

print(f"Square of 5: {square(5)}")
print(f"Add 3 and 7: {add(3, 7)}")
print(greet_lambda("Bob"))

# Lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original numbers: {numbers}")
print(f"Squared: {squared}")
print(f"Even numbers: {even_numbers}")

# Lambda for sorting
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
students_by_grade = sorted(students, key=lambda student: student[1])
print(f"Students by grade: {students_by_grade}")

# ============================================================================
# DECORATORS (BASIC UNDERSTANDING)
# ============================================================================

def my_decorator(func):
    """Basic decorator that adds functionality to a function"""
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Alice")

# Practical decorator example - timing functions
import time
import functools

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(0.1)  # Simulate slow operation
    return "Done!"

result = slow_function()

print("\n" + "="*60)
print("2. FILE HANDLING & ERROR MANAGEMENT")
print("="*60)

# ============================================================================
# READING AND WRITING FILES
# ============================================================================

# Writing to a text file
def write_text_file():
    with open("sample.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.\n")
        file.write("Python file handling is easy!")

# Reading from a text file
def read_text_file():
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found. Creating it first...")
        write_text_file()
        read_text_file()

read_text_file()

# Reading line by line
def read_lines():
    try:
        with open("sample.txt", "r") as file:
            lines = file.readlines()
            print("\nReading line by line:")
            for i, line in enumerate(lines, 1):
                print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print("File not found!")

read_lines()

# ============================================================================
# WORKING WITH DIFFERENT FILE FORMATS
# ============================================================================

import json
import csv

# JSON file handling
def json_example():
    # Data to save
    data = {
        "students": [
            {"name": "Alice", "age": 20, "grade": 85},
            {"name": "Bob", "age": 22, "grade": 90},
            {"name": "Charlie", "age": 21, "grade": 78}
        ]
    }
    
    # Write JSON
    with open("students.json", "w") as file:
        json.dump(data, file, indent=2)
    
    # Read JSON
    with open("students.json", "r") as file:
        loaded_data = json.load(file)
        print("\nJSON Data:")
        for student in loaded_data["students"]:
            print(f"Name: {student['name']}, Grade: {student['grade']}")

json_example()

# CSV file handling
def csv_example():
    # Write CSV
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Subject", "Grade"])  # Header
        writer.writerow(["Alice", "Math", 85])
        writer.writerow(["Bob", "Math", 90])
        writer.writerow(["Charlie", "Math", 78])
    
    # Read CSV
    print("\nCSV Data:")
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    
    # Read CSV as dictionary
    print("\nCSV as dictionary:")
    with open("grades.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Name']} scored {row['Grade']} in {row['Subject']}")

csv_example()

# ============================================================================
# EXCEPTION HANDLING
# ============================================================================

def division_example():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print("Division completed successfully!")
    finally:
        print("Division operation finished.")

# Uncomment to test interactively
# division_example()

# Multiple exception types
def safe_list_access(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return "Index out of range"
    except TypeError:
        return "Invalid index type"

test_list = [1, 2, 3, 4, 5]
print(f"List[2]: {safe_list_access(test_list, 2)}")
print(f"List[10]: {safe_list_access(test_list, 10)}")
print(f"List['a']: {safe_list_access(test_list, 'a')}")

# Custom exceptions
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative!")
    elif age > 150:
        raise CustomError("Age seems unrealistic!")
    else:
        return f"Age {age} is valid"

try:
    print(check_age(25))
    print(check_age(-5))
except CustomError as e:
    print(f"Custom error: {e.message}")

print("\n" + "="*60)
print("3. OBJECT-ORIENTED PROGRAMMING")
print("="*60)

# ============================================================================
# CLASSES AND OBJECTS
# ============================================================================

class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age, breed):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self.breed = breed
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"
    
    # String representation
    def __str__(self):
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"

# Creating objects
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "German Shepherd")

print(dog1.bark())
print(dog2.get_info())
print(f"Dog1: {dog1}")
print(f"Species: {Dog.species}")

# ============================================================================
# INHERITANCE AND POLYMORPHISM
# ============================================================================

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        pass  # To be overridden by subclasses
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

class Cat(Animal):
    def __init__(self, name, age, indoor=True):
        super().__init__(name, age)  # Call parent constructor
        self.indoor = indoor
    
    def make_sound(self):
        return f"{self.name} says Meow!"
    
    def climb(self):
        return f"{self.name} climbs the tree!"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def make_sound(self):
        return f"{self.name} says Woof!"
    
    def fetch(self):
        return f"{self.name} fetches the ball!"

# Polymorphism in action
animals = [
    Cat("Whiskers", 2),
    Dog("Buddy", 3, "Labrador"),
    Cat("Shadow", 4, False)
]

print("\nPolymorphism example:")
for animal in animals:
    print(animal.make_sound())  # Different behavior for each type
    print(animal.get_info())

# ============================================================================
# ENCAPSULATION AND ABSTRACTION
# ============================================================================

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance  # Protected attribute
        self.__transaction_history = []  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__transaction_history.append(f"Deposited: ${amount}")
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return self._balance
    
    def get_transaction_history(self):
        return self.__transaction_history.copy()  # Return copy, not original
    
    def __str__(self):
        return f"Account {self.account_number}: Balance ${self._balance}"

# Using the BankAccount class
account = BankAccount("123456", 1000)
print(account)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Current balance: ${account.get_balance()}")
print(f"Transaction history: {account.get_transaction_history()}")

# ============================================================================
# SPECIAL METHODS (MAGIC METHODS)
# ============================================================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation for users"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Point(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Enable + operator"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        """Enable == operator"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Enable len() function"""
        return int((self.x**2 + self.y**2)**0.5)

# Using special methods
p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"Point 1: {p1}")
print(f"Point 1 + Point 2: {p1 + p2}")
print(f"p1 == p2? {p1 == p2}")
print(f"p1 == p3? {p1 == p3}")
print(f"Distance from origin for p1: {len(p1)}")

print("\n" + "="*60)
print("4. MODULES & PACKAGES")
print("="*60)

# ============================================================================
# IMPORTING MODULES
# ============================================================================

# Different ways to import
import math
from datetime import datetime, date
from random import randint, choice
import os as operating_system

# Using imported modules
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Current time: {datetime.now()}")
print(f"Today's date: {date.today()}")
print(f"Random number: {randint(1, 10)}")
print(f"Random choice: {choice(['apple', 'banana', 'cherry'])}")
print(f"Current directory: {operating_system.getcwd()}")

# ============================================================================
# CREATING YOUR OWN MODULES
# ============================================================================

# This would typically be in a separate file called 'my_utilities.py'
"""
Contents of my_utilities.py:

def greet(name):
    return f"Hello, {name}!"

def calculate_area(length, width):
    return length * width

def is_even(number):
    return number % 2 == 0

PI = 3.14159

class Calculator:
    def add(self, x, y):
        return x + y
    
    def multiply(self, x, y):
        return x * y

if __name__ == "__main__":
    print("This module is being run directly")
    print(greet("World"))
else:
    print("This module is being imported")
"""

# To use the module:
# import my_utilities
# print(my_utilities.greet("Alice"))
# calc = my_utilities.Calculator()
# print(calc.add(5, 3))

# ============================================================================
# UNDERSTANDING __name__ == "__main__"
# ============================================================================

def main():
    """Main function to run when script is executed directly"""
    print("This script is being run directly!")
    
    # Test our functions
    dog = Dog("Test Dog", 2, "Beagle")
    print(dog.bark())
    
    account = BankAccount("TEST123", 100)
    print(account.deposit(50))

if __name__ == "__main__":
    # This code runs only when the script is executed directly
    # Not when it's imported as a module
    main()
else:
    print("This module has been imported")

# ============================================================================
# PACKAGE STRUCTURE EXAMPLE
# ============================================================================

"""
Package structure example:

my_package/
    __init__.py          # Makes it a package
    math_utils.py        # Module with math functions
    string_utils.py      # Module with string functions
    subpackage/
        __init__.py      # Makes subpackage
        advanced.py      # Advanced functions

__init__.py contents:
from .math_utils import add, multiply
from .string_utils import capitalize_words
from .subpackage.advanced import complex_function

math_utils.py contents:
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

Usage:
import my_package
result = my_package.add(5, 3)

or:

from my_package import add, multiply
result = add(5, 3)
"""

# ============================================================================
# VIRTUAL ENVIRONMENTS
# ============================================================================

"""
Virtual Environment Commands (run in terminal):

# Create virtual environment
python -m venv myenv

# Activate virtual environment
# Windows:
myenv\\Scripts\\activate
# macOS/Linux:
source myenv/bin/activate

# Install packages
pip install requests numpy pandas

# List installed packages
pip list

# Save requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate virtual environment
deactivate

Benefits of virtual environments:
1. Isolate project dependencies
2. Avoid conflicts between different projects
3. Easy to share project requirements
4. Clean development environment
"""

print("\n" + "="*60)
print("PHASE 2 COMPLETE!")
print("="*60)

print("""
🎉 Congratulations! You've completed Phase 2: Intermediate Programming!

Key concepts mastered:
✅ Functions with parameters, returns, and scope
✅ Lambda functions and basic decorators
✅ File handling (TXT, JSON, CSV)
✅ Exception handling and error management
✅ Object-oriented programming fundamentals
✅ Classes, inheritance, and polymorphism
✅ Modules, packages, and virtual environments

Next steps:
1. Practice creating your own classes and modules
2. Build a small project using these concepts
3. Experiment with file operations and error handling
4. Try creating a simple package structure

Ready for Phase 3: Intermediate-Advanced topics?
""")