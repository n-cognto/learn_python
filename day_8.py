""" Day 8: Complete Operators Guide - Comparison, Logical, Bitwise, Identity & Membership """

# ============================================================================
# SECTION 1: COMPARISON AND LOGICAL OPERATORS (REVIEW)
# ============================================================================
print("=== COMPARISON AND LOGICAL OPERATORS ===")

a = 5
b = 10
print(f"a = {a}, b = {b}")

# Comparison operators
print(f"a < b: {a < b}")
print(f"a > b: {a > b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")

# Logical operators
nums = [1, 2, 3]
print(f"a < b and b > 0: {a < b and b > 0}")
print(f"a > b or b < 0: {a > b or b < 0}")
print(f"not (a == b): {not (a == b)}")

if not nums:
    print("List is empty")
else:
    print("List has items")

# ============================================================================
# SECTION 2: BITWISE OPERATORS
# ============================================================================
print("\n=== BITWISE OPERATORS ===")

x = 12  # Binary: 1100
y = 8   # Binary: 1000

print(f"x = {x} (binary: {bin(x)})")
print(f"y = {y} (binary: {bin(y)})")

print(f"x & y (AND): {x & y} (binary: {bin(x & y)})")  # 8
 
print(f"x ^ y (XOR): {x ^ y} (binary: {bin(x ^ y)})")  # 4
print(f"~x (NOT): {~x} (binary: {bin(~x & 0xFF)})")    # -13
print(f"x << 2 (Left Shift): {x << 2} (binary: {bin(x << 2)})")  # 48
print(f"x >> 2 (Right Shift): {x >> 2} (binary: {bin(x >> 2)})") # 3

# Practical bitwise example: Permissions
READ = 4    # 100 in binary
WRITE = 2   # 010 in binary  
EXECUTE = 1 # 001 in binary

permissions = READ | WRITE  # Combine permissions
print(f"\nPermissions example:")
print(f"READ permission: {permissions & READ != 0}")
print(f"WRITE permission: {permissions & WRITE != 0}")
print(f"EXECUTE permission: {permissions & EXECUTE != 0}")

# ============================================================================
# SECTION 3: IDENTITY OPERATORS
# ============================================================================
print("\n=== IDENTITY OPERATORS ===")

# 'is' checks if two variables point to the same object in memory
# '==' checks if two variables have the same value

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")

print(f"list1 == list2: {list1 == list2}")  # True (same values)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)
print(f"list1 is list3: {list1 is list3}")  # True (same object)

# Special case with small integers and strings (Python optimization)
a = 256
b = 256
print(f"a = 256, b = 256")
print(f"a is b: {a is b}")  # True for small integers

a = 257
b = 257
print(f"a = 257, b = 257")
print(f"a is b: {a is b}")  # May be False for larger integers

# None comparison - always use 'is'
value = None
print(f"value is None: {value is None}")      # Correct way
print(f"value == None: {value == None}")      # Works but not recommended

# ============================================================================
# SECTION 4: MEMBERSHIP OPERATORS
# ============================================================================
print("\n=== MEMBERSHIP OPERATORS ===")

fruits = ["apple", "banana", "cherry"]
text = "Python Programming"
numbers = {1, 2, 3, 4, 5}

print(f"fruits: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

print(f"\ntext: '{text}'")
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")

print(f"\nnumbers: {numbers}")
print(f"3 in numbers: {3 in numbers}")
print(f"10 not in numbers: {10 not in numbers}")

# Dictionary membership checks keys by default
student = {"name": "Alice", "age": 20, "grade": "A"}
print(f"\nstudent: {student}")
print(f"'name' in student: {'name' in student}")
print(f"'Alice' in student.values(): {'Alice' in student.values()}")

# ============================================================================
# SECTION 5: OPERATOR PRECEDENCE
# ============================================================================
print("\n=== OPERATOR PRECEDENCE ===")

# Operator precedence from highest to lowest:
# 1. Parentheses
# 2. Exponentiation (**)
# 3. Unary +, -, not
# 4. *, /, //, %
# 5. +, -
# 6. <<, >>
# 7. &
# 8. ^
# 9. |
# 10. Comparisons (==, !=, <, >, etc.)
# 11. is, is not
# 12. in, not in
# 13. not
# 14. and
# 15. or

result1 = 2 + 3 * 4  # = 2 + 12 = 14 (not 20)
result2 = (2 + 3) * 4  # = 5 * 4 = 20

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")

# Complex example
x = 5
y = 10
z = 15
result = x < y and y < z or x > z
print(f"x < y and y < z or x > z = {result}")  # True

# ============================================================================
# SECTION 6: PRACTICAL EXERCISES
# ============================================================================
print("\n=== EXERCISES ===")

print("Exercise 1: Create a simple permission system using bitwise operators")
print("Exercise 2: Write a function to check if a number is a power of 2 using bitwise AND")
print("Exercise 3: Use identity operators to check for singleton objects")
print("Exercise 4: Create a text search function using membership operators")

# Solution examples
def is_power_of_two(n):
    """Check if n is a power of 2 using bitwise AND"""
    return n > 0 and (n & (n - 1)) == 0

def check_permissions(user_perms, required_perm):
    """Check if user has required permission"""
    return (user_perms & required_perm) != 0

print(f"\nSolutions:")
print(f"is_power_of_two(8): {is_power_of_two(8)}")  # True
print(f"is_power_of_two(6): {is_power_of_two(6)}")  # False

user_permissions = READ | WRITE  # User has read and write
print(f"User can read: {check_permissions(user_permissions, READ)}")
print(f"User can execute: {check_permissions(user_permissions, EXECUTE)}")