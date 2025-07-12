# Python Foundations - Phase 1 Complete Guide

"""
Welcome to Python! This guide covers all the fundamental concepts you need
to start your Python journey. By the end, you'll understand:

1. Core Syntax & Concepts
2. Control Flow (if statements, loops)
3. Basic problem-solving with Python

Let's start building your Python foundation! 🐍
"""

print("🐍 WELCOME TO PYTHON FOUNDATIONS!")
print("="*50)

# ============================================================================
# CORE SYNTAX & CONCEPTS
# ============================================================================

print("\n1. VARIABLES AND DATA TYPES")
print("-" * 30)

# Variables - containers for storing data
# Python is dynamically typed (you don't need to declare types)

# Integers (whole numbers)
age = 25
year = 2024
temperature = -5
big_number = 1000000

print(f"Age: {age} (type: {type(age)})")
print(f"Year: {year}")
print(f"Temperature: {temperature}")
print(f"Big number: {big_number:,}")  # Comma separator for readability

# Floats (decimal numbers)
price = 19.99
pi = 3.14159
scientific = 1.5e-4  # Scientific notation (0.00015)

print(f"Price: ${price}")
print(f"Pi: {pi}")
print(f"Scientific notation: {scientific}")

# Strings (text)
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multiline string
that spans several lines"""

print(f"Name: {name}")
print(f"Message: {message}")
print("Multiline string:")
print(multiline)

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
greeting = f"Hello, {first_name}!"  # f-string (modern way)

print(f"Full name: {full_name}")
print(f"Greeting: {greeting}")

# Booleans (True/False)
is_student = True
is_graduated = False
has_job = True

print(f"Is student: {is_student}")
print(f"Is graduated: {is_graduated}")
print(f"Has job: {has_job}")

# Variable naming rules and conventions
"""
GOOD variable names:
- age, first_name, total_price
- user_id, max_speed, is_valid

BAD variable names:
- 1age (can't start with number)
- first-name (no hyphens)
- class (reserved keyword)

Python naming conventions:
- Use lowercase with underscores: my_variable
- Constants in UPPERCASE: MAX_SIZE = 100
- Classes use PascalCase: MyClass
"""

print("\n2. BASIC OPERATORS")
print("-" * 30)

# Arithmetic operators
a = 10
b = 3

print("Arithmetic Operations:")
print(f"{a} + {b} = {a + b}")      # Addition
print(f"{a} - {b} = {a - b}")      # Subtraction
print(f"{a} * {b} = {a * b}")      # Multiplication
print(f"{a} / {b} = {a / b}")      # Division (float result)
print(f"{a} // {b} = {a // b}")    # Floor division (integer result)
print(f"{a} % {b} = {a % b}")      # Modulus (remainder)
print(f"{a} ** {b} = {a ** b}")    # Exponentiation (power)

# Comparison operators
x = 5
y = 10

print(f"\nComparison Operations (x={x}, y={y}):")
print(f"x == y: {x == y}")    # Equal to
print(f"x != y: {x != y}")    # Not equal to
print(f"x < y: {x < y}")      # Less than
print(f"x > y: {x > y}")      # Greater than
print(f"x <= y: {x <= y}")    # Less than or equal to
print(f"x >= y: {x >= y}")    # Greater than or equal to

# Logical operators
p = True
q = False

print(f"\nLogical Operations (p={p}, q={q}):")
print(f"p and q: {p and q}")   # Both must be True
print(f"p or q: {p or q}")     # At least one must be True
print(f"not p: {not p}")       # Opposite of p

# Practical logical operations
age = 20
has_license = True
print(f"\nCan drive? {age >= 18 and has_license}")

score = 85
print(f"Passed? {score >= 60}")
print(f"Honor roll? {score >= 90}")

print("\n3. INPUT AND OUTPUT")
print("-" * 30)

# Output with print()
print("Hello, World!")
print("Python", "is", "awesome!")  # Multiple items
print("Name:", "Alice", "Age:", 25)

# Different ways to format output
name = "Bob"
age = 30
city = "New York"

print("Old style: My name is %s and I'm %d years old" % (name, age))
print("Format method: My name is {} and I'm {} years old".format(name, age))
print(f"f-string (modern): My name is {name} and I'm {age} years old")

# Print with different separators and endings
print("A", "B", "C", sep="-")        # Custom separator
print("Loading", end="...")          # Custom ending
print(" Done!")                      # Continues on same line

# Input from user
print("\n--- Interactive Input Example ---")
print("# Uncomment these lines to test interactively:")
print("# user_name = input('What is your name? ')")
print("# user_age = input('What is your age? ')")
print("# print(f'Hello {user_name}, you are {user_age} years old!')")

# Note: input() always returns a string!
print("# user_number = int(input('Enter a number: '))")  # Convert to integer
print("# user_price = float(input('Enter a price: '))")  # Convert to float

print("\n4. COMMENTS AND DOCUMENTATION")
print("-" * 30)

# This is a single-line comment
x = 5  # You can also put comments at the end of lines

"""
This is a multi-line comment (actually a string)
You can write multiple lines here
Useful for longer explanations
"""

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Documentation best practices
# - Explain WHY, not just WHAT
# - Use clear, descriptive variable names
# - Add docstrings to functions and classes

print("Area calculation function defined with proper documentation")

print("\n5. PYTHON INTERACTIVE SHELL")
print("-" * 30)

print("""
Python Interactive Shell (REPL - Read-Eval-Print Loop):

To start:
1. Open terminal/command prompt
2. Type 'python' or 'python3'
3. You'll see >>> prompt

Example session:
>>> 2 + 3
5
>>> name = "Alice"
>>> print(f"Hello, {name}")
Hello, Alice
>>> exit()

Useful interactive commands:
- help(function_name) - Get help
- dir(object) - List attributes/methods
- type(variable) - Check variable type
- exit() or quit() - Exit Python shell
""")

print("\n" + "="*50)
print("CONTROL FLOW")
print("="*50)

print("\n1. CONDITIONAL STATEMENTS (if, elif, else)")
print("-" * 40)

# Basic if statement
age = 18
if age >= 18:
    print("You are an adult!")

# if-else statement
temperature = 75
if temperature > 80:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# if-elif-else statement
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Multiple conditions
age = 25
has_license = True
has_car = False

if age >= 18 and has_license:
    if has_car:
        print("You can drive your own car!")
    else:
        print("You can drive, but need to borrow a car.")
else:
    print("You cannot drive yet.")

# Practical examples
print("\n--- Practical Conditional Examples ---")

# Password strength checker
password = "MySecurePass123!"
length = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*" for c in password)

if length >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong password!")
elif length >= 6:
    print("Medium strength password")
else:
    print("Weak password")

# BMI Calculator
weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.1f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

print("\n2. LOOPS")
print("-" * 20)

# FOR LOOPS - iterate over sequences
print("For Loops:")

# Loop through a range of numbers
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# Loop through a string
name = "Python"
print(f"Letters in '{name}':")
for letter in name:
    print(f"- {letter}")

# Loop through a list
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits in our list:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop with index using enumerate
print("Fruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Loop through a range with step
print("Even numbers from 0 to 10:")
for num in range(0, 11, 2):
    print(num, end=" ")
print()  # New line

# WHILE LOOPS - repeat while condition is True
print("\nWhile Loops:")

# Basic while loop
count = 1
print("Counting with while loop:")
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Same as count = count + 1

# While loop with user input simulation
print("Guessing game simulation:")
secret_number = 7
guess = 0
attempts = 0

# Simulating guesses instead of actual input
guesses = [3, 10, 7]  # Simulated user guesses
guess_index = 0

while guess != secret_number and guess_index < len(guesses):
    guess = guesses[guess_index]
    attempts += 1
    print(f"Attempt {attempts}: Guessed {guess}")
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")
    
    guess_index += 1

print("\n3. BREAK, CONTINUE, AND PASS STATEMENTS")
print("-" * 40)

# BREAK - exit the loop early
print("Using break to find first even number:")
numbers = [1, 3, 7, 8, 9, 12, 15]
for num in numbers:
    print(f"Checking {num}")
    if num % 2 == 0:
        print(f"Found first even number: {num}")
        break
    print(f"{num} is odd, continuing...")

# CONTINUE - skip the rest of current iteration
print("\nUsing continue to skip negative numbers:")
numbers = [-2, 5, -1, 8, -3, 10]
positive_sum = 0
for num in numbers:
    if num < 0:
        print(f"Skipping negative number: {num}")
        continue
    positive_sum += num
    print(f"Added {num}, sum is now {positive_sum}")

print(f"Sum of positive numbers: {positive_sum}")

# PASS - placeholder for future code
print("\nUsing pass as placeholder:")
for i in range(3):
    if i == 1:
        pass  # TODO: Add special handling later
    else:
        print(f"Processing item {i}")

print("\n4. NESTED LOOPS AND CONDITIONS")
print("-" * 35)

# Nested loops - loops inside loops
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result:2d}", end="  ")
    print()  # New line after each row

# Pattern printing
print("\nStar pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # New line

# Nested conditions
print("\nStudent grade analysis:")
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 17, "grade": 92},
    {"name": "Charlie", "age": 19, "grade": 78},
    {"name": "Diana", "age": 21, "grade": 95}
]

for student in students:
    name = student["name"]
    age = student["age"]
    grade = student["grade"]
    
    print(f"\nAnalyzing {name}:")
    
    # Age category
    if age >= 21:
        age_category = "Senior"
    elif age >= 18:
        age_category = "Adult"
    else:
        age_category = "Minor"
    
    # Grade category
    if grade >= 90:
        grade_category = "Excellent"
        if age >= 18:
            print(f"  {name} is an {age_category} with {grade_category} performance!")
        else:
            print(f"  {name} is a {age_category} with {grade_category} performance!")
    elif grade >= 80:
        grade_category = "Good"
        print(f"  {name} has {grade_category} performance")
    else:
        grade_category = "Needs Improvement"
        print(f"  {name} {grade_category}")

print("\n" + "="*50)
print("PRACTICAL EXAMPLES & EXERCISES")
print("="*50)

# Example 1: Simple Calculator
print("\n1. SIMPLE CALCULATOR")
print("-" * 20)

def simple_calculator():
    """Demonstrates basic concepts with a calculator"""
    print("Simple Calculator Demo")
    
    # Simulated user input (in real program, use input())
    num1 = 10
    operator = "+"
    num2 = 5
    
    print(f"Calculating: {num1} {operator} {num2}")
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
    else:
        result = "Error: Invalid operator!"
    
    print(f"Result: {result}")

simple_calculator()

# Example 2: Number Guessing Game Logic
print("\n2. NUMBER GUESSING GAME LOGIC")
print("-" * 30)

import random

def guessing_game_demo():
    """Demonstrates loops and conditions"""
    secret = random.randint(1, 10)
    max_attempts = 3
    attempts = 0
    won = False
    
    print(f"I'm thinking of a number between 1 and 10...")
    print(f"Secret number is {secret} (for demo purposes)")
    
    # Simulate some guesses
    demo_guesses = [5, 7, secret]
    
    for guess in demo_guesses:
        attempts += 1
        print(f"\nAttempt {attempts}: Guessing {guess}")
        
        if guess == secret:
            print("🎉 Congratulations! You guessed it!")
            won = True
            break
        elif guess < secret:
            print("📈 Too low!")
        else:
            print("📉 Too high!")
        
        if attempts >= max_attempts:
            break
    
    if not won:
        print(f"💔 Game over! The number was {secret}")

guessing_game_demo()

# Example 3: Grade Statistics
print("\n3. GRADE STATISTICS")
print("-" * 20)

def grade_statistics():
    """Demonstrates working with lists and calculations"""
    grades = [85, 92, 78, 96, 88, 76, 94, 89, 82, 91]
    
    print(f"Grades: {grades}")
    
    # Calculate statistics
    total = 0
    count = 0
    highest = grades[0]
    lowest = grades[0]
    
    for grade in grades:
        total += grade
        count += 1
        
        if grade > highest:
            highest = grade
        if grade < lowest:
            lowest = grade
    
    average = total / count
    
    print(f"Total students: {count}")
    print(f"Average grade: {average:.1f}")
    print(f"Highest grade: {highest}")
    print(f"Lowest grade: {lowest}")
    
    # Count grade ranges
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0
    
    for grade in grades:
        if grade >= 90:
            a_count += 1
        elif grade >= 80:
            b_count += 1
        elif grade >= 70:
            c_count += 1
        elif grade >= 60:
            d_count += 1
        else:
            f_count += 1
    
    print(f"\nGrade Distribution:")
    print(f"A (90-100): {a_count} students")
    print(f"B (80-89):  {b_count} students")
    print(f"C (70-79):  {c_count} students")
    print(f"D (60-69):  {d_count} students")
    print(f"F (0-59):   {f_count} students")

grade_statistics()

print("\n" + "="*50)
print("🎉 PHASE 1 COMPLETE!")
print("="*50)

print("""
Congratulations! You've mastered Python foundations! 🐍✨

✅ CONCEPTS LEARNED:
   • Variables and data types (int, float, str, bool)
   • Operators (arithmetic, comparison, logical)
   • Input/output with print() and input()
   • Comments and documentation
   • Conditional statements (if, elif, else)
   • Loops (for, while)
   • Control flow (break, continue, pass)
   • Nested structures

🚀 WHAT'S NEXT:
   Ready to move on to Phase 2: Intermediate Programming!
   You'll learn about:
   • Functions and scope
   • File handling
   • Object-oriented programming
   • Modules and packages

💡 PRACTICE EXERCISES:
   1. Create a temperature converter (Celsius ↔ Fahrenheit)
   2. Build a simple menu-driven program
   3. Make a times table generator
   4. Create a password strength checker
   5. Build a basic text-based adventure game

Keep coding and have fun! 🎯
""")