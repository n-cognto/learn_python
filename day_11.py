"""
Day 11: While Loops - Mastering Iterative Control
================================================

Learning Objectives:
- Understand while loop syntax and structure
- Master loop control with break and continue
- Learn best practices for safe loop design
- Apply while loops to real-world problems
- Practice with hands-on exercises and challenges
"""

print("=" * 50)
print("Day 11: While Loops - Mastering Iterative Control")
print("=" * 50)

# ============================================================================
# SECTION 1: BASIC WHILE LOOP STRUCTURE
# ============================================================================
print("\n1. BASIC WHILE LOOP STRUCTURE")
print("-" * 35)

print("Basic counting with while loop:")
count = 0
print(f"Starting count: {count}")

while count < 5:
    print(f"Count is: {count}")
    count += 1  # CRITICAL: Always update the condition variable!

print(f"Final count: {count}")

print("\nCountdown example:")
countdown = 5
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1
print("Blast off! 🚀")

# ============================================================================
# SECTION 2: WHILE LOOP VS FOR LOOP - WHEN TO USE WHICH
# ============================================================================
print("\n\n2. WHILE LOOP VS FOR LOOP")
print("-" * 30)

print("Use FOR loop when you know the number of iterations:")
print("For loop example:")
for i in range(3):
    print(f"For loop iteration: {i}")

print("\nUse WHILE loop when condition-based or unknown iterations:")
print("While loop example:")
user_wants_to_continue = True
iteration = 0
while user_wants_to_continue and iteration < 3:
    print(f"While loop iteration: {iteration}")
    iteration += 1
    user_wants_to_continue = iteration < 2  # Simulate user decision

# ============================================================================
# SECTION 3: LOOP CONTROL - BREAK AND CONTINUE
# ============================================================================
print("\n\n3. LOOP CONTROL: BREAK AND CONTINUE")
print("-" * 40)

print("Using BREAK to exit loop early:")
number = 1
while number <= 10:
    if number == 6:
        print(f"Breaking at {number}")
        break
    print(f"Number: {number}")
    number += 1

print("\nUsing CONTINUE to skip iterations:")
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:  # Skip even numbers
        continue
    print(f"Odd number: {number}")

print("\nCombining BREAK and CONTINUE:")
attempts = 0
while attempts < 5:
    attempts += 1
    if attempts == 2:
        print(f"Skipping attempt {attempts}")
        continue
    if attempts == 4:
        print(f"Success on attempt {attempts}!")
        break
    print(f"Attempt {attempts} failed")

# ============================================================================
# SECTION 4: WHILE TRUE LOOPS AND SAFE PRACTICES
# ============================================================================
print("\n\n4. WHILE TRUE LOOPS AND SAFE PRACTICES")
print("-" * 45)

print("Safe infinite loop with break condition:")
attempts = 0
max_attempts = 3

while True:
    attempts += 1
    print(f"Attempt {attempts}")
    
    if attempts >= max_attempts:
        print("Maximum attempts reached!")
        break
    
    # Simulate some condition that might succeed
    if attempts == 2:
        print("Success!")
        break

print("\nInput validation loop:")
valid_input = False
attempts = 0
max_attempts = 3

while not valid_input and attempts < max_attempts:
    attempts += 1
    user_input = "yes" if attempts == 2 else "maybe"  # Simulate user input
    print(f"Simulated input: '{user_input}'")
    
    if user_input.lower() in ['yes', 'y', 'no', 'n']:
        valid_input = True
        print(f"Valid input received: {user_input}")
    else:
        print("Invalid input. Please enter 'yes' or 'no'")

if not valid_input:
    print("Too many invalid attempts!")

# ============================================================================
# SECTION 5: WHILE LOOP WITH ELSE CLAUSE
# ============================================================================
print("\n\n5. WHILE LOOP WITH ELSE CLAUSE")
print("-" * 35)

print("While-else: else runs if loop completes normally (no break)")

# Example 1: Loop completes normally
search_value = 15
numbers = [1, 5, 10, 20, 25]
index = 0

while index < len(numbers):
    if numbers[index] == search_value:
        print(f"Found {search_value} at index {index}")
        break
    index += 1
else:
    print(f"{search_value} not found in the list")

# Example 2: Loop breaks early
search_value = 10
index = 0

while index < len(numbers):
    if numbers[index] == search_value:
        print(f"Found {search_value} at index {index}")
        break
    index += 1
else:
    print(f"{search_value} not found in the list")

# ============================================================================
# SECTION 6: PRACTICAL APPLICATIONS
# ============================================================================
print("\n\n6. PRACTICAL APPLICATIONS")
print("-" * 30)

print("Application 1: Password Validation")
password_attempts = 0
max_password_attempts = 3
correct_password = "secret123"

while password_attempts < max_password_attempts:
    password_attempts += 1
    # Simulate password input
    entered_password = "secret123" if password_attempts == 2 else "wrong"
    print(f"Password attempt {password_attempts}: '{entered_password}'")
    
    if entered_password == correct_password:
        print("Access granted! ✅")
        break
    else:
        remaining = max_password_attempts - password_attempts
        if remaining > 0:
            print(f"Incorrect password. {remaining} attempts remaining.")
        else:
            print("Account locked! Too many failed attempts. 🔒")

print("\nApplication 2: Number Guessing Game")
secret_number = 7
guess_count = 0
max_guesses = 4
guessed_correctly = False

print(f"Guess the number between 1 and 10! You have {max_guesses} attempts.")

while guess_count < max_guesses and not guessed_correctly:
    guess_count += 1
    # Simulate user guesses
    simulated_guesses = [3, 8, 7, 5]
    guess = simulated_guesses[guess_count - 1] if guess_count <= len(simulated_guesses) else 1
    print(f"Guess {guess_count}: {guess}")
    
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed it in {guess_count} attempts!")
        guessed_correctly = True
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

if not guessed_correctly:
    print(f"😔 Game over! The number was {secret_number}")

print("\nApplication 3: Menu System")
menu_choice = ""
while menu_choice != "4":
    print("\n--- Menu ---")
    print("1. View Profile")
    print("2. Edit Settings")
    print("3. Help")
    print("4. Exit")
    
    # Simulate user choices
    choices = ["1", "2", "3", "4"]
    menu_choice = choices.pop(0) if choices else "4"
    print(f"Selected: {menu_choice}")
    
    if menu_choice == "1":
        print("Displaying profile...")
    elif menu_choice == "2":
        print("Opening settings...")
    elif menu_choice == "3":
        print("Showing help...")
    elif menu_choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")

# ============================================================================
# SECTION 7: COMMON PITFALLS AND HOW TO AVOID THEM
# ============================================================================
print("\n\n7. COMMON PITFALLS AND HOW TO AVOID THEM")
print("-" * 45)

print("❌ PITFALL 1: Infinite loops (forgetting to update condition)")
print("# Bad example:")
print("# count = 0")
print("# while count < 5:")
print("#     print(count)  # Forgot: count += 1")

print("\n✅ SOLUTION: Always update the loop variable")
count = 0
safety_counter = 0
while count < 3 and safety_counter < 10:  # Safety counter prevents infinite loop
    print(f"Safe count: {count}")
    count += 1
    safety_counter += 1

print("\n❌ PITFALL 2: Off-by-one errors")
print("Be careful with <= vs < in conditions")

print("\n❌ PITFALL 3: Modifying list while iterating")
print("Don't modify a list's size while looping through it")

print("\n✅ BEST PRACTICES:")
print("1. Always ensure loop condition will eventually become False")
print("2. Use meaningful variable names")
print("3. Keep loop body focused and simple")
print("4. Consider using for loops when possible")
print("5. Add safety counters for complex conditions")

# ============================================================================
# SECTION 8: PRACTICE EXERCISES
# ============================================================================
print("\n\n8. PRACTICE EXERCISES")
print("-" * 30)
print("Try solving these problems:")

print("\nExercise 1: Sum Calculator")
print("Use a while loop to calculate sum of numbers from 1 to 10")

print("\nExercise 2: Factorial Calculator")
print("Calculate factorial of 5 using while loop")
print("5! = 5 × 4 × 3 × 2 × 1 = 120")

print("\nExercise 3: Digital Root")
print("Find digital root of 9875")
print("Keep summing digits until single digit: 9+8+7+5=29, 2+9=11, 1+1=2")

print("\nExercise 4: Collatz Sequence")
print("Start with 7, if even divide by 2, if odd multiply by 3 and add 1")
print("Continue until reaching 1: 7→22→11→34→17→52→26→13→40→20→10→5→16→8→4→2→1")

print("\nExercise 5: Prime Number Checker")
print("Check if 17 is prime using while loop")

# ============================================================================
# SECTION 9: EXERCISE SOLUTIONS
# ============================================================================
print("\n\n9. EXERCISE SOLUTIONS")
print("-" * 30)

# Solution 1: Sum Calculator
print("Solution 1: Sum Calculator")
total = 0
number = 1
while number <= 10:
    total += number
    number += 1
print(f"Sum of 1 to 10: {total}")

# Solution 2: Factorial Calculator
print("\nSolution 2: Factorial Calculator")
factorial = 1
number = 5
original_number = number
while number > 0:
    factorial *= number
    number -= 1
print(f"{original_number}! = {factorial}")

# Solution 3: Digital Root
print("\nSolution 3: Digital Root")
number = 9875
print(f"Finding digital root of {number}")
while number >= 10:
    digit_sum = 0
    temp = number
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    print(f"{number} → {digit_sum}")
    number = digit_sum
print(f"Digital root: {number}")

# Solution 4: Collatz Sequence
print("\nSolution 4: Collatz Sequence")
number = 7
sequence = [number]
while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    sequence.append(number)
print(f"Collatz sequence for 7: {' → '.join(map(str, sequence))}")

# Solution 5: Prime Number Checker
print("\nSolution 5: Prime Number Checker")
number = 17
is_prime = True
divisor = 2

if number < 2:
    is_prime = False
else:
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

print(f"{number} is {'prime' if is_prime else 'not prime'}")

# ============================================================================
# SECTION 10: ADVANCED CHALLENGES
# ============================================================================
print("\n\n10. ADVANCED CHALLENGES")
print("-" * 30)
print("Try these challenging problems:")

print("\nChallenge 1: Fibonacci Sequence")
print("Generate first 10 Fibonacci numbers using while loop")
print("0, 1, 1, 2, 3, 5, 8, 13, 21, 34...")

print("\nChallenge 2: Perfect Number Finder")
print("Find the first perfect number after 6")
print("Perfect number = sum of its proper divisors (28 = 1+2+4+7+14)")

print("\nChallenge 3: Text Adventure Game")
print("Create a simple room navigation system:")
print("- Player can move north, south, east, west")
print("- Track current position")
print("- End when player reaches treasure room")

print("\nChallenge 4: Binary to Decimal Converter")
print("Convert binary 1101011 to decimal using while loop")

print("\nChallenge 5: Password Generator")
print("Generate random passwords until one meets criteria:")
print("- 8+ characters, uppercase, lowercase, digit, special char")

print("\n" + "=" * 50)
print("End of Day 11 - While Loop Master! 🔄")
print("=" * 50)

# ============================================================================
# BONUS: QUICK REFERENCE
# ============================================================================
print("\n" + "=" * 50)
print("QUICK REFERENCE - WHILE LOOP PATTERNS")
print("=" * 50)

print("""
# Basic Pattern:
while condition:
    # do something
    # update condition variable

# Input Validation:
while not valid_input:
    user_input = get_input()
    valid_input = validate(user_input)

# Counter Pattern:
count = 0
while count < max_count:
    # do something
    count += 1

# Search Pattern:
found = False
index = 0
while index < len(data) and not found:
    if data[index] == target:
        found = True
    else:
        index += 1

# Menu Loop:
choice = ""
while choice != "quit":
    display_menu()
    choice = get_user_choice()
    process_choice(choice)
""")
