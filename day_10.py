""" Day 10: Looping with for Loops """

# COMPREHENSIVE GUIDE TO FOR LOOPS IN PYTHON

# 1. Basic For Loop with Range
print("--- BASIC FOR LOOP WITH RANGE ---")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# 2. For Loop with Different Range Parameters
print("\n--- RANGE PARAMETERS ---")
print("Range with start, stop:")
for i in range(1, 6):  # start at 1, stop before 6
    print(i, end=" ")
print()

print("Range with step:")
for i in range(0, 10, 2):  # start at 0, stop before 10, step by 2
    print(i, end=" ")
print()

print("Range with negative step (countdown):")
for i in range(10, 0, -1):  # start at 10, stop before 0, step by -1
    print(i, end=" ")
print()

# 3. Looping Through Different Data Structures
print("\n--- LOOPING THROUGH DATA STRUCTURES ---")

# Loop through a string
name = "Python"
print(f"Letters in '{name}':")
for letter in name:
    print(f"- {letter}")

# Loop through a list
fruits = ["apple", "banana", "cherry", "date"]
print("\nFruits in our list:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop through a tuple
coordinates = (10, 20, 30)
print("\nCoordinates:")
for coord in coordinates:
    print(f"- {coord}")

# Loop through a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print("\nPerson dictionary keys:")
for key in person:
    print(f"- {key}: {person[key]}")

print("\nPerson dictionary items:")
for key, value in person.items():
    print(f"- {key}: {value}")

# 4. Loop with Enumeration
print("\n--- ENUMERATION ---")
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Starting enumeration at a different number
print("\nFruits with custom starting index:")
for index, fruit in enumerate(fruits, start=101):
    print(f"{index}. {fruit}")

# 5. Nested Loops
print("\n--- NESTED LOOPS ---")
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

# 6. Loop Control Statements
print("\n--- LOOP CONTROL STATEMENTS ---")

# Break - exit the loop early
print("Using break to find first even number:")
numbers = [1, 3, 7, 8, 9, 12, 15]
for num in numbers:
    print(f"Checking {num}")
    if num % 2 == 0:
        print(f"Found first even number: {num}")
        break
    print(f"{num} is odd, continuing...")

# Continue - skip the rest of current iteration
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

# Pass - placeholder for future code
print("\nUsing pass as placeholder:")
for i in range(3):
    if i == 1:
        pass  # TODO: Add special handling later
    else:
        print(f"Processing item {i}")

# 7. For Loops with Zip - Combining Iterables
print("\n--- USING ZIP TO COMBINE ITERABLES ---")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Boston", "Chicago"]

print("People information:")
for name, age, city in zip(names, ages, cities):
    print(f"- {name} is {age} years old and lives in {city}")

# 8. List Comprehension - Compact For Loops
print("\n--- LIST COMPREHENSION ---")
numbers = list(range(1, 11))
print("Original numbers:", numbers)

# Using a for loop to create a new list
squares_loop = []
for num in numbers:
    squares_loop.append(num ** 2)
print("Squares (using loop):", squares_loop)

# Using list comprehension
squares_comprehension = [num ** 2 for num in numbers]
print("Squares (using comprehension):", squares_comprehension)

# List comprehension with condition
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print("Even squares:", even_squares)

# 9. Common Patterns
print("\n--- COMMON PATTERNS ---")

# Finding the sum
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers}: {total}")
# (Note: Could also use sum(numbers))

# Finding max/min
numbers = [7, 3, 9, 2, 5]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print(f"Maximum of {numbers}: {max_value}")
# (Note: Could also use max(numbers))

# Filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers in {numbers}: {even_numbers}")
# (Note: Could also use list comprehension or filter())

# 10. Generator Expressions - Memory Efficient Iteration
print("\n--- GENERATOR EXPRESSIONS ---")
numbers = range(1, 1000001)  # A large range

# This doesn't create a full list in memory
squares_generator = (x**2 for x in numbers)
print(f"Type of generator: {type(squares_generator)}")

# Calculate sum without storing all values
import time
start = time.time()
total = sum(squares_generator)
end = time.time()
print(f"Sum of squares from 1 to 1,000,000: {total}")
print(f"Time taken: {end - start:.4f} seconds")

# PRACTICE EXERCISES
print("\n--- PRACTICE EXERCISES ---")
print("""
1. Create a for loop that prints the first 10 multiples of 3
2. Use a for loop to calculate the factorial of 5 (5!)
3. Create a loop that iterates over a string and counts the vowels
4. Print a pattern of numbers like:
   1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5
5. Create a list of tuples with student names and grades, then use a for loop
   to find the student with the highest grade
6. Use nested for loops to generate all combinations of two dice rolls
7. Create a list comprehension that generates a list of the first 10 perfect squares
""")

# Exercise solutions (try on your own first!)
print("\n--- EXERCISE SOLUTIONS ---")

# 1. First 10 multiples of 3
print("First 10 multiples of 3:")
for i in range(1, 11):
    print(f"3 × {i} = {3 * i}")

# 2. Factorial of 5
factorial = 1
for i in range(1, 6):
    factorial *= i
print(f"5! = {factorial}")

# 3. Count vowels in a string
text = "Hello, how are you today?"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"Vowels in '{text}': {vowel_count}")

# 4. Number pattern
print("\nNumber pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 5. Find student with highest grade
students = [("Alice", 92), ("Bob", 84), ("Charlie", 96), ("Diana", 88)]
best_student = students[0]  # Start with first student
for student in students:
    if student[1] > best_student[1]:
        best_student = student
print(f"Student with highest grade: {best_student[0]} ({best_student[1]})")

# 6. Dice combinations
print("\nAll possible dice combinations:")
for die1 in range(1, 7):
    for die2 in range(1, 7):
        print(f"({die1}, {die2})", end=" ")
    print()

# 7. Perfect squares using list comprehension
perfect_squares = [x**2 for x in range(1, 11)]
print(f"First 10 perfect squares: {perfect_squares}")

# CHALLENGE: FizzBuzz
print("\n--- FIZZBUZZ CHALLENGE ---")
print("FizzBuzz from 1 to 20:")
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
