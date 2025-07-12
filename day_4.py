""" 
Day 4: Input and Output Operations in Python
==========================================

Learning Objectives:
- Master the input() function for user interaction
- Learn different ways to handle and validate user input
- Understand type conversion for input data
- Practice formatting output for better user experience
- Handle common input/output errors gracefully
"""

# ========================
# BASIC INPUT OPERATIONS
# ========================

"""
The input() function:
- Always returns a string, regardless of what the user types
- Displays a prompt message to the user
- Waits for user to press Enter
- Can be combined with type conversion functions
"""

# Basic input example
print("=== BASIC INPUT EXAMPLE ===")
user_name = input("Enter your name: ")
print(f"Hello, {user_name}! Welcome to Python programming.")
print(f"Your name has {len(user_name)} characters.")

# ========================
# INPUT WITH TYPE CONVERSION
# ========================

"""
Converting input to different data types:
- int(input()) for integers
- float(input()) for decimal numbers
- Always handle potential conversion errors
"""

print("\n=== NUMERIC INPUT EXAMPLES ===")

# Integer input
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
    print(f"Next year you will be {age + 1} years old.")
except ValueError:
    print("Please enter a valid number for age.")

# Float input
try:
    height = float(input("Enter your height in meters (e.g., 1.75): "))
    print(f"Your height is {height:.2f} meters.")
    print(f"That's {height * 100:.0f} centimeters.")
except ValueError:
    print("Please enter a valid decimal number for height.")

# ========================
# MULTIPLE INPUTS
# ========================

"""
Handling multiple inputs:
1. Separate input() calls
2. Single input with split() method
3. List comprehensions for type conversion
"""

print("\n=== MULTIPLE INPUT METHODS ===")

# Method 1: Separate inputs
print("Method 1: Separate inputs")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Full name: {first_name} {last_name}")

# Method 2: Space-separated input
print("\nMethod 2: Space-separated input")
print("Enter three numbers separated by spaces:")
try:
    numbers_input = input("Numbers: ")
    numbers = [int(x) for x in numbers_input.split()]
    print(f"You entered: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
except ValueError:
    print("Please enter valid numbers separated by spaces.")

# Method 3: Comma-separated input
print("\nMethod 3: Comma-separated input")
print("Enter your favorite colors separated by commas:")
colors_input = input("Colors: ")
colors = [color.strip() for color in colors_input.split(",")]
print(f"Your favorite colors are: {', '.join(colors)}")

# ========================
# INPUT VALIDATION
# ========================

"""
Input validation ensures users provide correct data format
"""

print("\n=== INPUT VALIDATION EXAMPLES ===")

# Validate positive integer
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid integer.")

# Validate yes/no input
def get_yes_no(prompt):
    while True:
        response = input(prompt).lower().strip()
        if response in ['yes', 'y', '1', 'true']:
            return True
        elif response in ['no', 'n', '0', 'false']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Example usage of validation functions
print("Validation Example:")
student_count = get_positive_integer("How many students are in your class? ")
has_experience = get_yes_no("Do you have programming experience? (yes/no): ")

print(f"Class size: {student_count} students")
print(f"Programming experience: {'Yes' if has_experience else 'No'}")

# ========================
# ADVANCED OUTPUT FORMATTING
# ========================

"""
Python offers multiple ways to format output:
1. f-strings (modern, preferred)
2. .format() method
3. % formatting (older style)
"""

print("\n=== OUTPUT FORMATTING EXAMPLES ===")

name = "Alice"
score = 87.5
total = 100

# f-string formatting (Python 3.6+)
print(f"Student: {name}")
print(f"Score: {score}/{total}")
print(f"Percentage: {score/total:.1%}")
print(f"Grade: {score:.0f} points")

# Format with alignment
print(f"{'Name':<10} {'Score':<8} {'Grade':<5}")
print(f"{name:<10} {score:<8.1f} {'B+':<5}")

# Number formatting
pi = 3.14159265359
print(f"Pi rounded to 2 decimals: {pi:.2f}")
print(f"Pi in scientific notation: {pi:.2e}")
print(f"Large number with commas: {1234567:,}")

# ========================
# PRACTICAL EXAMPLES
# ========================

"""
Real-world input/output scenarios
"""

print("\n=== PRACTICAL EXAMPLE: GRADE CALCULATOR ===")

def grade_calculator():
    print("Grade Calculator")
    print("-" * 20)
    
    try:
        # Get student information
        student_name = input("Student name: ")
        
        # Get number of assignments
        num_assignments = get_positive_integer("Number of assignments: ")
        
        # Collect grades
        grades = []
        for i in range(num_assignments):
            while True:
                try:
                    grade = float(input(f"Grade for assignment {i+1} (0-100): "))
                    if 0 <= grade <= 100:
                        grades.append(grade)
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")
        
        # Calculate results
        average = sum(grades) / len(grades)
        
        # Determine letter grade
        if average >= 90:
            letter_grade = "A"
        elif average >= 80:
            letter_grade = "B"
        elif average >= 70:
            letter_grade = "C"
        elif average >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
        
        # Display results
        print("\n" + "=" * 30)
        print("GRADE REPORT")
        print("=" * 30)
        print(f"Student: {student_name}")
        print(f"Assignments: {num_assignments}")
        print(f"Grades: {grades}")
        print(f"Average: {average:.1f}")
        print(f"Letter Grade: {letter_grade}")
        print("=" * 30)
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

# Uncomment to run the grade calculator
# grade_calculator()

# ========================
# WORKING WITH FILES (Preview)
# ========================

"""
Python can also read from files and write to files
(We'll cover this in detail in later lessons)
"""

print("\n=== FILE I/O PREVIEW ===")

# Writing to a file
def save_user_data():
    name = input("Enter your name to save: ")
    age = input("Enter your age: ")
    
    with open("user_data.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
    
    print("Data saved to user_data.txt")

# Reading from a file
def read_user_data():
    try:
        with open("user_data.txt", "r") as file:
            content = file.read()
            print("Data from file:")
            print(content)
    except FileNotFoundError:
        print("No saved data found.")

# Uncomment to test file operations
# save_user_data()
# read_user_data()

# ========================
# COMMAND LINE ARGUMENTS
# ========================

"""
Programs can also receive input from command line arguments
"""

import sys

print(f"\nCommand line arguments: {sys.argv}")
print(f"Script name: {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"Additional arguments: {sys.argv[1:]}")
else:
    print("No additional command line arguments provided.")

# ========================
# EXERCISES
# ========================

"""
PRACTICE EXERCISES:

1. Create a simple calculator that:
   - Takes two numbers as input
   - Asks for an operation (+, -, *, /)
   - Displays the result with proper formatting

2. Build a personal information collector that:
   - Gets name, age, city, and hobby
   - Validates age is a positive integer
   - Saves the information to a file

3. Create a number guessing game that:
   - Generates a random number 1-100
   - Takes user guesses as input
   - Provides "higher" or "lower" hints
   - Counts the number of attempts

4. Build a shopping list program that:
   - Takes items as comma-separated input
   - Displays them as a numbered list
   - Calculates total if prices are provided
"""

# Example solution for Exercise 1: Simple Calculator
def simple_calculator():
    print("\n=== SIMPLE CALCULATOR ===")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                return
        else:
            print("Error: Invalid operator!")
            return
        
        print(f"\nResult: {num1} {operator} {num2} = {result:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

# Uncomment to run the calculator
# simple_calculator()

# ========================
# KEY TAKEAWAYS
# ========================

"""
SUMMARY:
1. input() always returns a string - convert types as needed
2. Use try/except blocks to handle conversion errors
3. Validate user input to ensure data quality
4. Use f-strings for modern, readable string formatting
5. Consider user experience when designing input prompts
6. Handle edge cases and errors gracefully
7. Multiple inputs can be processed using split() method
8. File I/O provides persistent data storage

BEST PRACTICES:
- Always validate user input
- Provide clear prompts and error messages
- Use meaningful variable names
- Handle exceptions appropriately
- Format output for readability
- Test your programs with various inputs

NEXT: Day 5 - We'll explore string operations and advanced formatting techniques!
"""

