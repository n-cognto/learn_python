""" 
Day 2: Basic Python Syntax, Printing, and Comments
=================================================

Learning Objectives:
- Master Python's print function and its features
- Understand different types of comments in Python
- Learn Python's basic syntax rules and conventions
- Practice proper variable naming conventions
"""

# ========================
# PRINTING IN PYTHON
# ========================

# Basic print statement
print("Hello, World!")

# Print multiple items
print("Hello,", "Python", "World!")

# Print with different separators
print("Python", "is", "awesome", sep="-")  # Output: Python-is-awesome
print("Learning", "Python", "today", sep=" | ")  # Output: Learning | Python | today

# Print with custom end character (default is newline)
print("This is line 1", end=" ")
print("This continues on the same line")

# Print with formatting
name = "Alice"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")  # f-string (Python 3.6+)
print("Hello, my name is {} and I am {} years old.".format(name, age))  # .format() method
print("Hello, my name is %s and I am %d years old." % (name, age))  # % formatting (older style)

# ========================
# COMMENTS IN PYTHON
# ========================

# This is a single-line comment
# Comments help explain your code to others (and your future self!)

"""
This is a multi-line comment (docstring)
You can write multiple lines here
Often used for documentation at the top of files or functions
"""

'''
You can also use single quotes for multi-line comments
But triple double quotes are more commonly used
'''

# Inline comments - use sparingly and only when necessary
x = 5  # This stores the value 5 in variable x

# TODO: Add error handling here
# FIXME: This function needs optimization
# NOTE: Remember to update this when the API changes

# ========================
# PYTHON SYNTAX RULES
# ========================

"""
INDENTATION:
Python uses indentation (spaces or tabs) to define code blocks.
Most Python developers use 4 spaces per indentation level.
"""

# Example of indentation (we'll learn more about if statements later)
temperature = 75
if temperature > 70:
    print("It's warm outside!")  # This line is indented
    print("Perfect weather!")    # This line is also indented
print("This line is not indented, so it's outside the if block")

"""
CASE SENSITIVITY:
Python is case-sensitive, meaning 'Variable' and 'variable' are different.
"""
Variable = "This is different from..."
variable = "...this variable"
print(Variable)  # Output: This is different from...
print(variable)  # Output: ...this variable

"""
LINE CONTINUATION:
Long lines can be broken using backslash (\) or parentheses.
"""
# Using backslash
long_string = "This is a very long string that we want to " + \
              "break across multiple lines for better readability"

# Using parentheses (preferred method)
long_calculation = (10 + 20 + 30 + 40 + 50 + 
                   60 + 70 + 80 + 90 + 100)

# ========================
# VARIABLE NAMING CONVENTIONS
# ========================

"""
VALID VARIABLE NAMES:
✅ Good Examples:
"""
age = 25
first_name = "John"
user_id = 12345
is_valid = True
total_price = 99.99
MAX_SIZE = 1000  # Constants in UPPERCASE

"""
❌ INVALID VARIABLE NAMES:
"""
# 1age = 25        # Can't start with a number
# first-name = ""  # Can't use hyphens
# class = "Math"   # Can't use reserved keywords
# my var = 5       # Can't have spaces

"""
NAMING CONVENTIONS:
1. snake_case: Use lowercase with underscores (recommended for variables and functions)
2. UPPER_CASE: Use for constants
3. PascalCase: Use for class names (we'll learn about classes later)
4. _private: Leading underscore indicates internal use
"""

# Examples of different naming conventions
snake_case_variable = "This follows Python convention"
CONSTANT_VALUE = 3.14159
_internal_variable = "This suggests internal use"

# ========================
# RESERVED KEYWORDS
# ========================

"""
Python has reserved keywords that cannot be used as variable names:
and, as, assert, break, class, continue, def, del, elif, else, except, 
finally, for, from, global, if, import, in, is, lambda, nonlocal, not, 
or, pass, raise, return, try, while, with, yield, True, False, None
"""

# You can see all keywords using:
import keyword
print("Python keywords:", keyword.kwlist)

# ========================
# PRACTICAL EXAMPLES
# ========================

# Good variable naming examples
student_name = "Emma Watson"
student_age = 20
student_grade = 95.5
is_enrolled = True

print(f"Student: {student_name}")
print(f"Age: {student_age}")
print(f"Grade: {student_grade}%")
print(f"Enrolled: {is_enrolled}")

# ========================
# EXERCISES
# ========================

"""
TRY THESE EXERCISES:

1. Create variables for your personal information:
   - Your name
   - Your age
   - Your favorite programming language
   - Whether you enjoy coding (True/False)

2. Print all the information using f-strings

3. Try different print separators and end characters

4. Write comments explaining what each variable stores
"""

# Example solution:
my_name = "Python Learner"  # Stores the learner's name
my_age = 22  # Stores the learner's age
favorite_language = "Python"  # Obviously Python!
enjoys_coding = True  # Boolean indicating coding enjoyment

# Print the information nicely formatted
print("=" * 30)
print("PERSONAL INFORMATION")
print("=" * 30)
print(f"Name: {my_name}")
print(f"Age: {my_age} years old")
print(f"Favorite Language: {favorite_language}")
print(f"Enjoys Coding: {enjoys_coding}")
print("=" * 30)

# ========================
# KEY TAKEAWAYS
# ========================

"""
SUMMARY:
1. print() function can display text, variables, and formatted strings
2. Use comments to explain your code - your future self will thank you!
3. Python uses indentation to define code blocks
4. Follow snake_case naming convention for variables
5. Avoid reserved keywords as variable names
6. Python is case-sensitive
7. Use meaningful variable names that describe what they store

NEXT: Day 3 - We'll dive deeper into variables and explore all Python data types!
"""