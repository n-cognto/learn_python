""" 
Day 3: Variables and Data Types in Python
=======================================

Learning Objectives:
- Master Python's built-in data types
- Understand type conversion and type checking
- Practice working with different data structures
- Learn when to use each data type effectively
"""

# ========================
# VARIABLES FUNDAMENTALS
# ========================

"""
Variables in Python:
- Containers that store data values
- Created when you first assign a value to them
- Can change type after creation (dynamic typing)
- No need to declare variable type explicitly
"""

# Variable assignment examples
name = "Alice"           # String
age = 25                # Integer
height = 5.6            # Float
is_student = True       # Boolean

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Is Student: {is_student} (type: {type(is_student).__name__})")

# ========================
# NUMERIC DATA TYPES
# ========================

"""
1. INTEGER (int): Whole numbers, positive or negative
"""
positive_int = 42
negative_int = -17
zero = 0
large_number = 1_000_000  # Underscores for readability

print(f"Integers: {positive_int}, {negative_int}, {zero}, {large_number}")

"""
2. FLOAT (float): Decimal numbers
"""
pi = 3.14159
temperature = -2.5
scientific_notation = 1.5e-4  # 1.5 × 10^-4 = 0.00015

print(f"Floats: {pi}, {temperature}, {scientific_notation}")

"""
3. COMPLEX (complex): Numbers with real and imaginary parts
"""
complex_num = 3 + 4j
another_complex = complex(2, -3)  # 2 - 3j

print(f"Complex numbers: {complex_num}, {another_complex}")

# ========================
# STRING DATA TYPE
# ========================

"""
STRING (str): Sequence of characters enclosed in quotes
"""

# Different ways to create strings
single_quotes = 'Hello, World!'
double_quotes = "Python is awesome!"
triple_quotes = """This is a
multi-line string
that preserves formatting."""

# String operations
greeting = "Hello"
name = "Python"
full_greeting = greeting + ", " + name + "!"  # Concatenation
repeated = "Python! " * 3  # Repetition

print(f"Concatenation: {full_greeting}")
print(f"Repetition: {repeated}")

# String methods (we'll learn more later)
text = "python programming"
print(f"Original: {text}")
print(f"Capitalized: {text.capitalize()}")
print(f"Upper case: {text.upper()}")
print(f"Title case: {text.title()}")
print(f"Length: {len(text)} characters")

# ========================
# BOOLEAN DATA TYPE
# ========================

"""
BOOLEAN (bool): Represents True or False values
"""

is_sunny = True
is_raining = False
is_weekend = True

# Boolean operations
print(f"Sunny and Weekend: {is_sunny and is_weekend}")
print(f"Sunny or Raining: {is_sunny or is_raining}")
print(f"Not raining: {not is_raining}")

# Values that evaluate to False (Falsy values)
falsy_values = [False, 0, 0.0, "", [], {}, None]
for value in falsy_values:
    print(f"{repr(value)} is falsy: {not bool(value)}")

# ========================
# SEQUENCE TYPES
# ========================

"""
1. LIST: Ordered, mutable (changeable) collection
"""
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["Python", 3.14, True, 42]

print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")  # Indexing starts at 0
print(f"Last fruit: {fruits[-1]}")  # Negative indexing

# List operations
fruits.append("mango")  # Add item
print(f"After adding mango: {fruits}")

fruits.remove("banana")  # Remove specific item
print(f"After removing banana: {fruits}")

"""
2. TUPLE: Ordered, immutable (unchangeable) collection
"""
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_item_tuple = (42,)  # Note the comma!

print(f"Coordinates: {coordinates}")
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

"""
3. RANGE: Sequence of numbers
"""
range_obj = range(5)        # 0 to 4
range_from_to = range(2, 8) # 2 to 7
range_with_step = range(0, 10, 2)  # 0, 2, 4, 6, 8

print(f"Range(5): {list(range_obj)}")
print(f"Range(2, 8): {list(range_from_to)}")
print(f"Range(0, 10, 2): {list(range_with_step)}")

# ========================
# MAPPING TYPE
# ========================

"""
DICTIONARY (dict): Collection of key-value pairs
"""
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "is_enrolled": True
}

print(f"Student info: {student}")
print(f"Student name: {student['name']}")
print(f"Student GPA: {student.get('gpa', 'N/A')}")  # Safe access

# Adding/modifying dictionary items
student["graduation_year"] = 2025
student["age"] = 21  # Update existing key

print(f"Updated student: {student}")

# Dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")

# ========================
# SET TYPES
# ========================

"""
1. SET: Unordered collection of unique elements
"""
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = set(numbers_with_duplicates)
print(f"Original list: {numbers_with_duplicates}")
print(f"Unique numbers: {unique_numbers}")

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (A ∪ B): {set_a | set_b}")
print(f"Intersection (A ∩ B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")

"""
2. FROZENSET: Immutable version of set
"""
immutable_set = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {immutable_set}")

# ========================
# NONE TYPE
# ========================

"""
NONE: Represents the absence of a value
"""
result = None
user_input = None

print(f"Result: {result}")
print(f"Is result None? {result is None}")

# Common use case: default function parameters
def greet(name=None):
    if name is None:
        return "Hello, Anonymous!"
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))

# ========================
# TYPE CONVERSION
# ========================

"""
Converting between data types (Type Casting)
"""

# String to number conversion
str_number = "42"
int_from_str = int(str_number)
float_from_str = float(str_number)

print(f"String: '{str_number}' -> Int: {int_from_str}, Float: {float_from_str}")

# Number to string conversion
number = 123
str_from_int = str(number)
print(f"Number: {number} -> String: '{str_from_int}'")

# List/Tuple conversion
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)

print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")
print(f"Back to list: {back_to_list}")

# ========================
# PRACTICAL EXAMPLES
# ========================

"""
Real-world example: Student grade calculator
"""
# Student data
student_data = {
    "name": "Emma Wilson",
    "grades": [85, 92, 78, 96, 88],
    "subjects": ["Math", "Science", "English", "History", "Art"],
    "is_honor_student": False
}

# Calculate average grade
total_grades = sum(student_data["grades"])
average_grade = total_grades / len(student_data["grades"])

# Determine honor student status
student_data["is_honor_student"] = average_grade >= 90

print("=" * 40)
print("STUDENT GRADE REPORT")
print("=" * 40)
print(f"Name: {student_data['name']}")
print(f"Subjects: {', '.join(student_data['subjects'])}")
print(f"Grades: {student_data['grades']}")
print(f"Average: {average_grade:.1f}")
print(f"Honor Student: {student_data['is_honor_student']}")

# ========================
# EXERCISES
# ========================

"""
PRACTICE EXERCISES:

1. Create a dictionary representing a book with:
   - title, author, year_published, pages, is_available

2. Create a list of your top 5 favorite movies

3. Use a set to find unique characters in your name

4. Convert the string "3.14159" to a float and then to an integer

5. Create a tuple with your personal info and unpack it into variables
"""

# Example solutions:

# Exercise 1: Book dictionary
book = {
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "year_published": 2019,
    "pages": 544,
    "is_available": True
}

# Exercise 2: Top movies list
top_movies = [
    "The Matrix",
    "Inception", 
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction"
]

# Exercise 3: Unique characters in name
my_name = "Python Programmer"
unique_chars = set(my_name.lower())
print(f"Unique characters in '{my_name}': {sorted(unique_chars)}")

# Exercise 4: Type conversion
pi_string = "3.14159"
pi_float = float(pi_string)
pi_int = int(pi_float)
print(f"String: {pi_string} -> Float: {pi_float} -> Int: {pi_int}")

# Exercise 5: Personal tuple
personal_info = ("John", "Doe", 25, "Engineer")
first_name, last_name, age, profession = personal_info
print(f"Name: {first_name} {last_name}, Age: {age}, Profession: {profession}")

# ========================
# KEY TAKEAWAYS
# ========================

"""
SUMMARY:
1. Python has many built-in data types for different purposes
2. Numbers: int, float, complex
3. Text: str (strings)
4. Boolean: bool (True/False)
5. Sequences: list (mutable), tuple (immutable), range
6. Mapping: dict (key-value pairs)
7. Sets: set (mutable), frozenset (immutable)
8. None: represents absence of value
9. Use type() to check data type
10. Convert between types using int(), float(), str(), etc.

CHOOSING THE RIGHT DATA TYPE:
- Use lists for ordered, changeable collections
- Use tuples for ordered, unchangeable collections
- Use dictionaries for key-value relationships
- Use sets for unique collections
- Use strings for text data
- Use appropriate numeric types for calculations

NEXT: Day 4 - We'll explore operators and expressions to manipulate these data types!
"""