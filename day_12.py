""" Day 12: List Comprehensions """

"""
List comprehensions provide a concise way to create lists.
Syntax: [expression for item in iterable if condition]
"""

# ========== BASIC LIST COMPREHENSIONS ==========
print("=== BASIC LIST COMPREHENSIONS ===")

# Basic list comprehension
squares = [x*x for x in range(5)]
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x*x for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Working with strings
names = ["alice", "bob", "charlie", "diana"]
capitalized_names = [name.capitalize() for name in names]
print(f"Capitalized names: {capitalized_names}")

# Filtering with conditions
long_names = [name for name in names if len(name) > 4]
print(f"Names longer than 4 characters: {long_names}")

# ========== ADVANCED LIST COMPREHENSIONS ==========
print("\n=== ADVANCED LIST COMPREHENSIONS ===")

# Nested list comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Flattening a matrix
flattened = [item for row in matrix for item in row]
print(f"Flattened matrix: {flattened}")

# Converting nested loops to list comprehension
# Traditional approach:
result_traditional = []
for x in range(3):
    for y in range(3):
        if x != y:
            result_traditional.append((x, y))

# List comprehension approach:
result_comprehension = [(x, y) for x in range(3) for y in range(3) if x != y]
print(f"Traditional approach: {result_traditional}")
print(f"List comprehension: {result_comprehension}")

# ========== PRACTICAL EXAMPLES ==========
print("\n=== PRACTICAL EXAMPLES ===")

# Processing data
temperatures_celsius = [0, 20, 30, 40]
temperatures_fahrenheit = [c * 9/5 + 32 for c in temperatures_celsius]
print(f"Celsius: {temperatures_celsius}")
print(f"Fahrenheit: {temperatures_fahrenheit}")

# String processing
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words]
long_words = [word.upper() for word in words if len(word) > 4]
print(f"Words: {words}")
print(f"Word lengths: {word_lengths}")
print(f"Long words (uppercase): {long_words}")

# Working with functions in comprehensions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 30) if is_prime(x)]
print(f"Prime numbers under 30: {primes}")

# ========== OTHER COMPREHENSIONS ==========
print("\n=== OTHER COMPREHENSIONS ===")

# Dictionary comprehension
word_lengths_dict = {word: len(word) for word in names}
print(f"Word lengths dict: {word_lengths_dict}")

# Conditional dictionary comprehension
long_words_dict = {word: len(word) for word in names if len(word) > 4}
print(f"Long words dict: {long_words_dict}")

# Set comprehension
unique_lengths = {len(word) for word in names}
print(f"Unique word lengths: {unique_lengths}")

# Generator expression (memory efficient)
squares_gen = (x*x for x in range(1000000))  # Doesn't create list immediately
first_five_squares = [next(squares_gen) for _ in range(5)]
print(f"First 5 squares from generator: {first_five_squares}")

# ========== PERFORMANCE COMPARISON ==========
print("\n=== PERFORMANCE COMPARISON ===")
import time

def time_function(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

def traditional_loop(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i * i)
    return result

def list_comp(n):
    return [i * i for i in range(n) if i % 2 == 0]

n = 10000
result1, time1 = time_function(traditional_loop, n)
result2, time2 = time_function(list_comp, n)

print(f"Traditional loop time: {time1:.6f} seconds")
print(f"List comprehension time: {time2:.6f} seconds")
print(f"List comprehension is {time1/time2:.2f}x faster")

# ========== EXERCISES AND CHALLENGES ==========
print("\n" + "="*50)
print("EXERCISES AND CHALLENGES")
print("="*50)

print("\n=== EXERCISE 1: Basic Comprehensions ===")
# Create list comprehensions for the following:

# 1. Cubes of numbers from 1 to 10
cubes = [x**3 for x in range(1, 11)]
print(f"1. Cubes 1-10: {cubes}")

# 2. Even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"2. Even numbers 1-20: {evens}")

# 3. Length of each word in a sentence
sentence_ex = "Python is an amazing programming language"
word_lengths_ex = [len(word) for word in sentence_ex.split()]
print(f"3. Word lengths: {word_lengths_ex}")

print("\n=== EXERCISE 2: String Processing ===")
# Work with this list of emails
emails = ["john@gmail.com", "jane@yahoo.com", "bob@gmail.com", "alice@hotmail.com"]

# 1. Extract usernames (part before @)
usernames = [email.split('@')[0] for email in emails]
print(f"1. Usernames: {usernames}")

# 2. Extract domains (part after @)
domains = [email.split('@')[1] for email in emails]
print(f"2. Domains: {domains}")

# 3. Filter Gmail addresses only
gmail_users = [email for email in emails if email.endswith('@gmail.com')]
print(f"3. Gmail users: {gmail_users}")

# 4. Create display names (capitalize usernames)
display_names = [email.split('@')[0].capitalize() for email in emails]
print(f"4. Display names: {display_names}")

print("\n=== EXERCISE 3: Number Processing ===")
# Work with this list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 1. Squares of odd numbers
odd_squares = [x**2 for x in numbers if x % 2 == 1]
print(f"1. Squares of odd numbers: {odd_squares}")

# 2. Numbers divisible by 3
div_by_3 = [x for x in numbers if x % 3 == 0]
print(f"2. Divisible by 3: {div_by_3}")

# 3. Apply different operations based on conditions
processed = [x**2 if x % 2 == 0 else x**3 for x in numbers[:5]]
print(f"3. Square if even, cube if odd: {processed}")

print("\n=== EXERCISE 4: Nested Comprehensions ===")
# Work with 2D data

# 1. Create a multiplication table (5x5)
mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("1. Multiplication table 5x5:")
for row in mult_table:
    print(f"   {row}")

# 2. Extract diagonal elements
diagonal = [mult_table[i][i] for i in range(len(mult_table))]
print(f"2. Diagonal elements: {diagonal}")

# 3. Flatten and filter (elements > 10)
flat_filtered = [item for row in mult_table for item in row if item > 10]
print(f"3. Flattened and filtered (>10): {flat_filtered}")

print("\n=== EXERCISE 5: Dictionary and Set Comprehensions ===")
# Work with student data
students = [
    ("Alice", 85), ("Bob", 92), ("Charlie", 78), 
    ("Diana", 96), ("Eve", 73), ("Frank", 88)
]

# 1. Create grade dictionary
grades_dict = {name: grade for name, grade in students}
print(f"1. Grades dictionary: {grades_dict}")

# 2. High performers (grade >= 85)
high_performers = {name: grade for name, grade in students if grade >= 85}
print(f"2. High performers: {high_performers}")

# 3. Unique grade ranges (A, B, C based on grades)
def get_grade_letter(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    else: return 'D'

grade_letters = {get_grade_letter(grade) for _, grade in students}
print(f"3. Unique grade letters: {grade_letters}")

print("\n=== CHALLENGE 1: Data Processing ===")
# Process sales data
sales_data = [
    {"product": "laptop", "price": 1200, "quantity": 3},
    {"product": "mouse", "price": 25, "quantity": 10},
    {"product": "keyboard", "price": 80, "quantity": 5},
    {"product": "monitor", "price": 300, "quantity": 2}
]

# 1. Calculate total value for each item
item_totals = [{**item, "total": item["price"] * item["quantity"]} for item in sales_data]
print("1. Items with totals:")
for item in item_totals:
    print(f"   {item}")

# 2. Products with total value > 200
high_value = [item for item in item_totals if item["total"] > 200]
print("2. High value items:")
for item in high_value:
    print(f"   {item['product']}: ${item['total']}")

# 3. Product names in uppercase
product_names = [item["product"].upper() for item in sales_data]
print(f"3. Product names (uppercase): {product_names}")

print("\n=== CHALLENGE 2: Text Analysis ===")
# Analyze this text
text = """
Python is a high-level programming language. 
It is known for its simplicity and readability.
Python supports multiple programming paradigms.
"""

# Clean and split text
words = [word.strip('.,').lower() for word in text.split() if word.strip('.,')]
print(f"1. Cleaned words: {words[:10]}...")  # Show first 10

# 2. Words longer than 5 characters
long_words = [word for word in words if len(word) > 5]
print(f"2. Words longer than 5 chars: {long_words}")

# 3. Count word frequencies using dict comprehension
from collections import Counter
word_freq = dict(Counter(words))
frequent_words = {word: count for word, count in word_freq.items() if count > 1}
print(f"3. Words appearing more than once: {frequent_words}")

# 4. Words starting with specific letters
p_words = [word for word in words if word.startswith('p')]
print(f"4. Words starting with 'p': {p_words}")

print("\n=== CHALLENGE 3: Mathematical Operations ===")
# Complex mathematical operations

# 1. Generate Fibonacci sequence using comprehension with helper function
def fibonacci_generator(n):
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(n-2)]
    return fib[:n]

fib_10 = fibonacci_generator(10)
print(f"1. First 10 Fibonacci numbers: {fib_10}")

# 2. Prime factorization helper
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Prime factors for numbers 10-20
factors_dict = {n: prime_factors(n) for n in range(10, 21)}
print("2. Prime factors for numbers 10-20:")
for num, factors in factors_dict.items():
    print(f"   {num}: {factors}")

# 3. Perfect squares and their square roots
perfect_squares = [(x, x**2) for x in range(1, 11)]
print(f"3. Perfect squares: {perfect_squares}")

print("\n=== BONUS CHALLENGE: Real-world Scenario ===")
# Student management system
student_records = [
    {"name": "Alice", "subjects": ["Math", "Physics", "Chemistry"], "scores": [85, 92, 78]},
    {"name": "Bob", "subjects": ["Math", "Biology", "English"], "scores": [90, 85, 88]},
    {"name": "Charlie", "subjects": ["Physics", "Chemistry", "Biology"], "scores": [82, 79, 91]},
    {"name": "Diana", "subjects": ["Math", "English", "History"], "scores": [95, 87, 92]}
]

# 1. Calculate average score for each student
student_averages = [
    {
        "name": student["name"],
        "average": sum(student["scores"]) / len(student["scores"])
    }
    for student in student_records
]
print("1. Student averages:")
for student in student_averages:
    print(f"   {student['name']}: {student['average']:.1f}")

# 2. Find students taking Math
math_students = [student["name"] for student in student_records 
                if "Math" in student["subjects"]]
print(f"2. Students taking Math: {math_students}")

# 3. Subject-wise highest scores
all_subjects = {subject for student in student_records for subject in student["subjects"]}
subject_best_scores = {}

for subject in all_subjects:
    scores_for_subject = []
    for student in student_records:
        if subject in student["subjects"]:
            subject_index = student["subjects"].index(subject)
            scores_for_subject.append((student["name"], student["scores"][subject_index]))
    
    if scores_for_subject:
        best_student, best_score = max(scores_for_subject, key=lambda x: x[1])
        subject_best_scores[subject] = {"student": best_student, "score": best_score}

print("3. Best score in each subject:")
for subject, info in subject_best_scores.items():
    print(f"   {subject}: {info['student']} ({info['score']})")

print("\n" + "="*50)
print("END OF EXERCISES - Try creating your own!")
print("="*50)
