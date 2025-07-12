"""
Day 6: Arithmetic and Assignment Operators
==========================================

Learning Objectives:
- Understand arithmetic operators in Python
- Master assignment operators and their shortcuts
- Apply operators in real-world scenarios
- Practice with hands-on exercises
"""

print("=" * 50)
print("Day 6: Arithmetic and Assignment Operators")
print("=" * 50)

# ============================================================================
# SECTION 1: ARITHMETIC OPERATORS
# ============================================================================
print("\n1. ARITHMETIC OPERATORS")
print("-" * 30)

a = 10
b = 3

print(f"Given: a = {a}, b = {b}")
print()

# Basic arithmetic operations
print("Addition (+):")
print(f"a + b = {a + b}")

print("\nSubtraction (-):")
print(f"a - b = {a - b}")

print("\nMultiplication (*):")
print(f"a * b = {a * b}")

print("\nDivision (/):")
print(f"a / b = {a / b}")

print("\nFloor Division (//):")
print(f"a // b = {a // b}  # Returns only the quotient (whole number part)")

print("\nModulus (%):")
print(f"a % b = {a % b}   # Returns only the remainder")

print("\nExponentiation (**):")
print(f"a ** b = {a ** b}  # a raised to the power of b")

# ============================================================================
# SECTION 2: PRACTICAL APPLICATIONS OF FLOOR DIVISION AND MODULUS
# ============================================================================
print("\n\n2. PRACTICAL APPLICATIONS")
print("-" * 30)

# Time conversion example
print("Example 1: Time Conversion")
total_minutes = 125
hours = total_minutes // 60      # Get full hours
remaining_minutes = total_minutes % 60  # Get leftover minutes
print(f"{total_minutes} minutes = {hours} hours and {remaining_minutes} minutes")

print("\nExample 2: Pagination")
items_per_page = 10
total_items = 47
total_pages = (total_items + items_per_page - 1) // items_per_page  # Round up
print(f"Need {total_pages} pages for {total_items} items")

print("\nExample 3: Finding Middle Element")
my_list = [1, 2, 3, 4, 5, 6, 7]
middle_index = len(my_list) // 2
print(f"List: {my_list}")
print(f"Middle element: {my_list[middle_index]} (at index {middle_index})")

# ============================================================================
# SECTION 3: ASSIGNMENT OPERATORS
# ============================================================================
print("\n\n3. ASSIGNMENT OPERATORS")
print("-" * 30)

# Reset variables for demonstration
x = 10
y = 3

print(f"Starting values: x = {x}, y = {y}")
print()

# Addition assignment
x += y  # equivalent to: x = x + y
print(f"After x += y: x = {x}")

# Subtraction assignment
x -= y  # equivalent to: x = x - y
print(f"After x -= y: x = {x}")

# Multiplication assignment
x *= y  # equivalent to: x = x * y
print(f"After x *= y: x = {x}")

# Division assignment
x /= y  # equivalent to: x = x / y
print(f"After x /= y: x = {x}")

# Floor division assignment
x //= y  # equivalent to: x = x // y
print(f"After x //= y: x = {x}")

# Reset x for modulus example
x = 10
x %= y  # equivalent to: x = x % y
print(f"After x %= y (x=10): x = {x}")

# Exponentiation assignment
x = 2
x **= 3  # equivalent to: x = x ** 3
print(f"After x **= 3 (x=2): x = {x}")

# ============================================================================
# SECTION 4: ASSIGNMENT OPERATORS WITH OTHER DATA TYPES
# ============================================================================
print("\n\n4. ASSIGNMENT OPERATORS WITH STRINGS AND LISTS")
print("-" * 50)

# String concatenation
text = "Hello"
text += " World"
print(f"String concatenation: '{text}'")

text *= 2
print(f"String repetition: '{text}'")

# List operations
numbers = [1, 2, 3]
print(f"Original list: {numbers}")

numbers += [4, 5]  # List concatenation
print(f"After adding [4, 5]: {numbers}")

numbers *= 2  # List repetition
print(f"After multiplying by 2: {numbers}")

# ============================================================================
# SECTION 5: PRACTICE EXERCISES
# ============================================================================
print("\n\n5. PRACTICE EXERCISES")
print("-" * 30)
print("Try solving these problems:")

print("\nExercise 1: Time Calculator")
print("Convert 3725 seconds to hours, minutes, and seconds format")
print("Hint: Use // and % operators")

print("\nExercise 2: Shopping Calculator")
print("If you have 47 dollars and each item costs 8 dollars:")
print("- How many items can you buy?")
print("- How much money will you have left?")

print("\nExercise 3: Grade Calculator")
print("A student scored 847 points out of 1000.")
print("Calculate the percentage using assignment operators.")

print("\nExercise 4: List Manipulation")
print("Start with list [1, 2, 3]")
print("- Double the list using *=")
print("- Add [7, 8, 9] using +=")
print("- Print the final result")

# ============================================================================
# SECTION 6: SOLUTIONS (Uncomment to see solutions)
# ============================================================================
print("\n\n6. EXERCISE SOLUTIONS")
print("-" * 30)

# Solution 1: Time Calculator
print("Solution 1:")
total_seconds = 3725
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")

# Solution 2: Shopping Calculator
print("\nSolution 2:")
money = 47
item_cost = 8
items_can_buy = money // item_cost
money_left = money % item_cost
print(f"Can buy {items_can_buy} items, ${money_left} left over")

# Solution 3: Grade Calculator
print("\nSolution 3:")
score = 847
total = 1000
percentage = score * 100
percentage /= total
print(f"Percentage: {percentage}%")

# Solution 4: List Manipulation
print("\nSolution 4:")
my_list = [1, 2, 3]
print(f"Original: {my_list}")
my_list *= 2
print(f"After doubling: {my_list}")
my_list += [7, 8, 9]
print(f"Final result: {my_list}")

# ============================================================================
# SECTION 7: CHALLENGE PROBLEMS
# ============================================================================
print("\n\n7. CHALLENGE PROBLEMS")
print("-" * 30)
print("Try these on your own:")

print("\nChallenge 1: Digital Clock")
print("Write code to convert 86400 seconds to days, hours, minutes, seconds")

print("\nChallenge 2: Pizza Party")
print("25 people, each pizza serves 8 people. How many pizzas needed?")
print("Use ceiling division: (people + slices_per_pizza - 1) // slices_per_pizza")

print("\nChallenge 3: Bank Account")
print("Start with $1000, use assignment operators to:")
print("- Add a $200 deposit")
print("- Subtract a $50 withdrawal")
print("- Apply 2% interest (multiply by 1.02)")
print("- Show final balance")

print("\n" + "=" * 50)
print("End of Day 6 - Great job learning operators!")
print("=" * 50)