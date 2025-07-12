"""
Day 7: Conditional Statements (if, else, elif)
==============================================

Learning Objectives:
- Master if, else, and elif statements
- Understand comparison and logical operators
- Apply conditional logic in real-world scenarios
- Learn about guard clauses and best practices
- Practice with hands-on exercises
"""

print("=" * 50)
print("Day 7: Conditional Statements")
print("=" * 50)

# ============================================================================
# SECTION 1: BASIC CONDITIONAL STATEMENTS
# ============================================================================
print("\n1. BASIC IF-ELSE STATEMENTS")
print("-" * 30)

# Simple if statement
age = 18
print(f"Age: {age}")

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Multiple conditions with elif
score = 85
print(f"\nScore: {score}")

if score >= 90:
    print("Grade: A (Excellent!)")
elif score >= 80:
    print("Grade: B (Good job!)")
elif score >= 70:
    print("Grade: C (Satisfactory)")
elif score >= 60:
    print("Grade: D (Needs improvement)")
else:
    print("Grade: F (Study harder!)")

# ============================================================================
# SECTION 2: COMPARISON OPERATORS
# ============================================================================
print("\n\n2. COMPARISON OPERATORS")
print("-" * 30)

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}  # Equal to")
print(f"x != y: {x != y}  # Not equal to")
print(f"x < y:  {x < y}   # Less than")
print(f"x > y:  {x > y}   # Greater than")
print(f"x <= y: {x <= y}  # Less than or equal to")
print(f"x >= y: {x >= y}  # Greater than or equal to")

# ============================================================================
# SECTION 3: LOGICAL OPERATORS
# ============================================================================
print("\n\n3. LOGICAL OPERATORS")
print("-" * 30)

# AND operator
print("AND operator (both conditions must be True):")
temperature = 25
humidity = 60
print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

if temperature > 20 and humidity < 70:
    print("Perfect weather for outdoor activities!")
else:
    print("Weather conditions are not ideal")

# OR operator
print("\nOR operator (at least one condition must be True):")
day = "Saturday"
holiday = False
print(f"Day: {day}, Holiday: {holiday}")

if day == "Saturday" or day == "Sunday" or holiday:
    print("It's a day off!")
else:
    print("It's a working day")

# NOT operator
print("\nNOT operator (reverses the boolean value):")
raining = False
print(f"Raining: {raining}")

if not raining:
    print("Great day for a picnic!")
else:
    print("Better stay indoors")

# ============================================================================
# SECTION 4: PRACTICAL EXAMPLES
# ============================================================================
print("\n\n4. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Number classification
print("Example 1: Number Classification")
number = -5
print(f"Number: {number}")

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Example 2: Leap year checker
print("\nExample 2: Leap Year Checker")
year = 2024
print(f"Year: {year}")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Example 3: Password strength checker
print("\nExample 3: Password Strength Checker")
password = "MyPassword123!"
length = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*" for c in password)

print(f"Password: {password}")
print(f"Length: {length}, Uppercase: {has_upper}, Lowercase: {has_lower}")
print(f"Digits: {has_digit}, Special chars: {has_special}")

if length >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong password!")
elif length >= 6 and (has_upper or has_lower) and has_digit:
    print("Medium strength password")
else:
    print("Weak password - needs improvement")

# ============================================================================
# SECTION 5: GUARD CLAUSES AND BEST PRACTICES
# ============================================================================
print("\n\n5. GUARD CLAUSES AND BEST PRACTICES")
print("-" * 40)

# Guard clauses - early return conditions
print("Guard Clauses Example:")
numbers = [1, 2, 3, 4, 5]

# Check if list is empty first
if not numbers:
    print("Cannot process: List is empty")
else:
    # Check if all items are numbers
    if all(isinstance(num, (int, float)) for num in numbers):
        print("All items are valid numbers")
        average = sum(numbers) / len(numbers)
        print(f"Average: {average}")
    else:
        print("Error: List contains non-numeric values")

# Nested vs flattened conditions
print("\nBetter approach - flattened conditions:")
if not numbers:
    print("Cannot process: List is empty")
elif not all(isinstance(num, (int, float)) for num in numbers):
    print("Error: List contains non-numeric values")
else:
    print("Processing valid numeric list...")
    average = sum(numbers) / len(numbers)
    print(f"Average: {average}")

# ============================================================================
# SECTION 6: FAMOUS PROGRAMMING CHALLENGES
# ============================================================================
print("\n\n6. FAMOUS PROGRAMMING CHALLENGES")
print("-" * 40)

# FizzBuzz Challenge
print("FizzBuzz Challenge (1-20):")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()  # New line after FizzBuzz

# ============================================================================
# SECTION 7: PRACTICE EXERCISES
# ============================================================================
print("\n\n7. PRACTICE EXERCISES")
print("-" * 30)
print("Try solving these problems:")

print("\nExercise 1: Age Category")
print("Write code to categorize age:")
print("- 0-12: Child")
print("- 13-19: Teenager") 
print("- 20-59: Adult")
print("- 60+: Senior")

print("\nExercise 2: Triangle Type")
print("Given three sides, determine triangle type:")
print("- Equilateral: all sides equal")
print("- Isosceles: two sides equal")
print("- Scalene: all sides different")
print("- Invalid: cannot form triangle")

print("\nExercise 3: BMI Calculator")
print("Calculate BMI and categorize:")
print("- Underweight: BMI < 18.5")
print("- Normal: 18.5 <= BMI < 25")
print("- Overweight: 25 <= BMI < 30")
print("- Obese: BMI >= 30")

print("\nExercise 4: Rock Paper Scissors")
print("Create a game that determines winner:")
print("- Rock beats Scissors")
print("- Scissors beats Paper")
print("- Paper beats Rock")

# ============================================================================
# SECTION 8: EXERCISE SOLUTIONS
# ============================================================================
print("\n\n8. EXERCISE SOLUTIONS")
print("-" * 30)

# Solution 1: Age Category
print("Solution 1: Age Category")
age = 25
if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

# Solution 2: Triangle Type
print("\nSolution 2: Triangle Type")
a, b, c = 5, 5, 8
print(f"Sides: {a}, {b}, {c}")

# Check if it's a valid triangle
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid triangle")

# Solution 3: BMI Calculator
print("\nSolution 3: BMI Calculator")
weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# Solution 4: Rock Paper Scissors
print("\nSolution 4: Rock Paper Scissors")
player1 = "rock"
player2 = "scissors"
print(f"Player 1: {player1}, Player 2: {player2}")

if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "scissors" and player2 == "paper") or \
     (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")

# ============================================================================
# SECTION 9: ADVANCED CHALLENGES
# ============================================================================
print("\n\n9. ADVANCED CHALLENGES")
print("-" * 30)
print("Try these on your own:")

print("\nChallenge 1: Grade Point Average")
print("Convert letter grades to GPA points and calculate average")
print("A=4.0, B=3.0, C=2.0, D=1.0, F=0.0")

print("\nChallenge 2: Password Validator")
print("Create a comprehensive password validator:")
print("- Minimum 8 characters")
print("- At least one uppercase, lowercase, digit, special char")
print("- No common passwords (password, 123456, etc.)")

print("\nChallenge 3: Date Validator")
print("Check if a date (day/month/year) is valid:")
print("- Consider leap years")
print("- Different days per month")
print("- Reasonable year range")

print("\n" + "=" * 50)
print("End of Day 7 - Master of Conditional Logic!")
print("=" * 50)