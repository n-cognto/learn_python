""" Day 15: Functions (Defining and Calling) """

"""
Functions are reusable blocks of code that perform specific tasks.
Key concepts:
- Parameters: inputs to the function (defined in function signature)
- Arguments: actual values passed to the function when called
- Return values: output from the function
- Scope: where variables can be accessed
"""

# ===== BASIC FUNCTION DEFINITION =====
print("=== BASIC FUNCTIONS ===")

def greet(name):
    """Simple function that takes one parameter and returns a string."""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Function with multiple parameters."""
    area = length * width
    return area

# Function calls
greeting = greet("Alice")
print(greeting)

area = calculate_area(5, 3)
print(f"Area: {area}")

# ===== FUNCTION ARGUMENTS TYPES =====
print("\n=== FUNCTION ARGUMENT TYPES ===")

def comprehensive_function(pos_arg, default_arg="default", *args, **kwargs):
    """
    Demonstrates all types of function arguments:
    - pos_arg: positional argument (required)
    - default_arg: default argument (optional)
    - *args: variable positional arguments (tuple)
    - **kwargs: variable keyword arguments (dictionary)
    """
    print(f"Positional: {pos_arg}")
    print(f"Default: {default_arg}")
    print(f"Extra positional (*args): {args}")
    print(f"Keyword (**kwargs): {kwargs}")
    print("-" * 30)

# Different ways to call the function:
print("1. Positional arguments only:")
comprehensive_function("Hello")

print("\n2. Keyword arguments:")
comprehensive_function(pos_arg="Hello", default_arg="Custom")

print("\n3. Mixed usage:")
comprehensive_function("Hello", "Custom", "extra1", "extra2", name="Grace", age=25)

# ===== RETURN VALUES =====
print("\n=== RETURN VALUES ===")

def no_return():
    """Function with no explicit return (returns None)."""
    print("This function doesn't return anything")

def single_return(x):
    """Function returning a single value."""
    return x * 2

def multiple_return(a, b):
    """Function returning multiple values (as a tuple)."""
    return a + b, a - b, a * b, a / b if b != 0 else None

# Examples of return values
result1 = no_return()  # Returns None
print(f"No return result: {result1}")

result2 = single_return(5)
print(f"Single return: {result2}")

# Unpacking multiple return values
sum_val, diff_val, prod_val, div_val = multiple_return(10, 3)
print(f"Multiple returns: sum={sum_val}, diff={diff_val}, prod={prod_val}, div={div_val}")

# ===== SCOPE AND VARIABLES =====
print("\n=== SCOPE AND VARIABLES ===")

global_var = "I'm global"

def scope_example():
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")
    
    # Modifying global variable
    global global_var
    global_var = "Modified global"

print(f"Before function call: {global_var}")
scope_example()
print(f"After function call: {global_var}")

# ===== LAMBDA FUNCTIONS =====
print("\n=== LAMBDA FUNCTIONS ===")

# Simple lambda functions
square = lambda x: x ** 2
add = lambda a, b: a + b

print(f"Square of 5: {square(5)}")
print(f"Add 3 and 7: {add(3, 7)}")

# Lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")
print(f"Even numbers: {even_numbers}")

# ===== FUNCTION DECORATORS (BASIC) =====
print("\n=== BASIC DECORATORS ===")

def timer_decorator(func):
    """A simple decorator that prints when a function is called."""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper

@timer_decorator
def slow_function():
    """Function with decorator applied."""
    import time
    time.sleep(0.1)  # Simulate slow operation
    return "Task completed"

result = slow_function()
print(f"Result: {result}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===")

def validate_email(email):
    """Simple email validation function."""
    return "@" in email and "." in email.split("@")[-1]

def calculate_grade(scores):
    """Calculate average grade and letter grade."""
    if not scores:
        return 0, "F"
    
    average = sum(scores) / len(scores)
    
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    
    return average, letter

def fibonacci(n):
    """Generate fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

# Test practical functions
emails = ["test@example.com", "invalid-email", "user@domain.org"]
for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")

student_scores = [85, 92, 78, 96, 88]
avg, letter = calculate_grade(student_scores)
print(f"Scores: {student_scores}")
print(f"Average: {avg:.1f}, Grade: {letter}")

fib_numbers = fibonacci(10)
print(f"First 10 Fibonacci numbers: {fib_numbers}")

# ===== FUNCTION CALLING OTHER FUNCTIONS =====
print("\n=== FUNCTIONS CALLING OTHER FUNCTIONS ===")

def format_name(first, last):
    """Format a person's name."""
    return f"{first.title()} {last.title()}"

def create_email(first, last, domain="company.com"):
    """Create an email address from name components."""
    formatted_name = format_name(first, last)
    email = f"{first.lower()}.{last.lower()}@{domain}"
    return formatted_name, email

def process_employee(first, last, scores):
    """Process employee data: format name, create email, calculate grade."""
    name, email = create_email(first, last)
    avg_score, grade = calculate_grade(scores)
    
    return {
        "name": name,
        "email": email,
        "average_score": avg_score,
        "grade": grade
    }

# Example usage
employee_data = process_employee("john", "doe", [88, 92, 85, 90])
print("Employee processed:")
for key, value in employee_data.items():
    print(f"  {key}: {value}")

# ===== RECURSIVE FUNCTIONS =====
print("\n=== RECURSIVE FUNCTIONS ===")

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def countdown(n):
    """Countdown function using recursion."""
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

print(f"Factorial of 5: {factorial(5)}")
print("Countdown from 5:")
countdown(5)

# ========== EXERCISES AND CHALLENGES ==========
print("\n" + "="*50)
print("EXERCISES AND CHALLENGES")
print("="*50)

print("\n=== EXERCISE 1: Basic Function Creation ===")

# 1. Temperature converter functions
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

# Test temperature converters
temps_c = [0, 25, 100]
print("1. Temperature conversions:")
for temp in temps_c:
    f_temp = celsius_to_fahrenheit(temp)
    print(f"   {temp}°C = {f_temp:.1f}°F")

print(f"   32°F = {fahrenheit_to_celsius(32):.1f}°C")
print(f"   273.15K = {kelvin_to_celsius(273.15):.1f}°C")

# 2. Mathematical utility functions
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Find greatest common divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Find least common multiple"""
    return abs(a * b) // gcd(a, b)

# Test mathematical functions
test_numbers = [17, 18, 19, 20, 21]
print("2. Prime number check:")
for num in test_numbers:
    print(f"   {num} is {'prime' if is_prime(num) else 'not prime'}")

print(f"   GCD(48, 18) = {gcd(48, 18)}")
print(f"   LCM(12, 8) = {lcm(12, 8)}")

print("\n=== EXERCISE 2: Functions with Multiple Parameters ===")

# 1. Grade calculator with weights
def calculate_weighted_grade(assignments, midterm, final, assignment_weight=0.4, midterm_weight=0.3, final_weight=0.3):
    """Calculate weighted grade from different components"""
    if abs(assignment_weight + midterm_weight + final_weight - 1.0) > 0.001:
        raise ValueError("Weights must sum to 1.0")
    
    avg_assignments = sum(assignments) / len(assignments) if assignments else 0
    return (avg_assignments * assignment_weight + 
            midterm * midterm_weight + 
            final * final_weight)

def get_letter_grade(score):
    """Convert numeric score to letter grade"""
    if score >= 97: return "A+"
    elif score >= 93: return "A"
    elif score >= 90: return "A-"
    elif score >= 87: return "B+"
    elif score >= 83: return "B"
    elif score >= 80: return "B-"
    elif score >= 77: return "C+"
    elif score >= 73: return "C"
    elif score >= 70: return "C-"
    elif score >= 67: return "D+"
    elif score >= 63: return "D"
    elif score >= 60: return "D-"
    else: return "F"

# Test grade calculator
student_assignments = [85, 90, 78, 88, 92]
student_midterm = 87
student_final = 91

final_score = calculate_weighted_grade(student_assignments, student_midterm, student_final)
letter = get_letter_grade(final_score)
print(f"1. Student final score: {final_score:.1f} ({letter})")

# 2. Distance and area calculators
def distance_2d(x1, y1, x2, y2):
    """Calculate distance between two 2D points"""
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def triangle_area(base, height):
    """Calculate area of triangle"""
    return 0.5 * base * height

def circle_area(radius):
    """Calculate area of circle"""
    import math
    return math.pi * radius**2

def rectangle_area(length, width):
    """Calculate area of rectangle"""
    return length * width

# Test geometry functions
print(f"2. Distance from (0,0) to (3,4): {distance_2d(0, 0, 3, 4):.2f}")
print(f"   Triangle area (base=10, height=5): {triangle_area(10, 5):.2f}")
print(f"   Circle area (radius=3): {circle_area(3):.2f}")
print(f"   Rectangle area (5x8): {rectangle_area(5, 8):.2f}")

print("\n=== EXERCISE 3: Functions with *args and **kwargs ===")

# 1. Statistical functions
def calculate_stats(*numbers):
    """Calculate various statistics for a set of numbers"""
    if not numbers:
        return {"count": 0, "sum": 0, "mean": 0, "min": 0, "max": 0}
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "range": max(numbers) - min(numbers)
    }

def print_report(**data):
    """Print a formatted report from keyword arguments"""
    print("   === REPORT ===")
    for key, value in data.items():
        formatted_key = key.replace('_', ' ').title()
        if isinstance(value, float):
            print(f"   {formatted_key}: {value:.2f}")
        else:
            print(f"   {formatted_key}: {value}")
    print("   ==============")

# Test statistical functions
test_data = [85, 92, 78, 96, 88, 73, 91, 87]
stats = calculate_stats(*test_data)
print("1. Statistics for test data:")
print_report(**stats)

# 2. Flexible logging function
def log_message(level, message, **kwargs):
    """Log a message with optional metadata"""
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{timestamp}] {level.upper()}: {message}"
    
    if kwargs:
        metadata = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        log_entry += f" | {metadata}"
    
    print(f"2. {log_entry}")

# Test logging function
log_message("info", "User logged in", user_id=123, ip_address="192.168.1.1")
log_message("error", "Database connection failed", error_code=500, retry_count=3)
log_message("debug", "Processing completed")

print("\n=== EXERCISE 4: Higher-Order Functions ===")

# 1. Function that takes other functions as parameters
def apply_operation(numbers, operation):
    """Apply an operation function to a list of numbers"""
    return [operation(num) for num in numbers]

def apply_filter(numbers, condition):
    """Filter numbers based on a condition function"""
    return [num for num in numbers if condition(num)]

def apply_reduce(numbers, operation, initial=0):
    """Reduce numbers using an operation function"""
    result = initial
    for num in numbers:
        result = operation(result, num)
    return result

# Test higher-order functions
test_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda functions
squared = apply_operation(test_nums, lambda x: x**2)
evens = apply_filter(test_nums, lambda x: x % 2 == 0)
product = apply_reduce(test_nums[:5], lambda x, y: x * y, 1)

print(f"1. Squared numbers: {squared[:5]}...")
print(f"   Even numbers: {evens}")
print(f"   Product of first 5: {product}")

# 2. Function decorators
def timing_decorator(func):
    """Decorator to measure function execution time"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"   Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def validation_decorator(func):
    """Decorator to validate function inputs"""
    def wrapper(*args, **kwargs):
        # Simple validation: ensure all numeric args are positive
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Function {func.__name__} requires positive numbers")
        return func(*args, **kwargs)
    return wrapper

@timing_decorator
@validation_decorator
def slow_calculation(n):
    """Simulate a slow calculation"""
    import time
    time.sleep(0.1)  # Simulate work
    return sum(range(n))

print("2. Decorated function test:")
result = slow_calculation(1000)
print(f"   Result: {result}")

print("\n=== CHALLENGE 1: Banking System ===")

# Complete banking system with various functions
class BankAccount:
    """Simple bank account implementation using functions"""
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        self._add_transaction("Account opened", initial_balance)
    
    def _add_transaction(self, description, amount):
        """Private method to add transaction to history"""
        import datetime
        self.transaction_history.append({
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": description,
            "amount": amount,
            "balance": self.balance
        })

def create_account(account_holder, initial_balance=0):
    """Factory function to create a new bank account"""
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative")
    return BankAccount(account_holder, initial_balance)

def deposit(account, amount):
    """Deposit money to an account"""
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")
    
    account.balance += amount
    account._add_transaction(f"Deposit", amount)
    return account.balance

def withdraw(account, amount):
    """Withdraw money from an account"""
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > account.balance:
        raise ValueError("Insufficient funds")
    
    account.balance -= amount
    account._add_transaction(f"Withdrawal", -amount)
    return account.balance

def transfer(from_account, to_account, amount):
    """Transfer money between accounts"""
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")
    
    withdraw(from_account, amount)
    deposit(to_account, amount)
    
    from_account._add_transaction(f"Transfer to {to_account.account_holder}", -amount)
    to_account._add_transaction(f"Transfer from {from_account.account_holder}", amount)

def get_account_summary(account):
    """Get account summary"""
    return {
        "account_holder": account.account_holder,
        "current_balance": account.balance,
        "total_transactions": len(account.transaction_history),
        "last_transaction": account.transaction_history[-1] if account.transaction_history else None
    }

# Test banking system
print("1. Banking system demo:")
alice_account = create_account("Alice Johnson", 1000)
bob_account = create_account("Bob Smith", 500)

deposit(alice_account, 200)
withdraw(bob_account, 100)
transfer(alice_account, bob_account, 150)

alice_summary = get_account_summary(alice_account)
bob_summary = get_account_summary(bob_account)

print(f"   Alice's balance: ${alice_summary['current_balance']}")
print(f"   Bob's balance: ${bob_summary['current_balance']}")
print(f"   Alice's transactions: {alice_summary['total_transactions']}")

print("\n=== CHALLENGE 2: Data Processing Pipeline ===")

# Data processing functions that can be chained
def clean_data(data):
    """Remove None values and convert to appropriate types"""
    cleaned = []
    for item in data:
        if item is not None:
            try:
                # Try to convert to number if possible
                if isinstance(item, str) and item.replace('.', '').replace('-', '').isdigit():
                    cleaned.append(float(item) if '.' in item else int(item))
                else:
                    cleaned.append(item)
            except:
                cleaned.append(item)
    return cleaned

def filter_data(data, condition_func):
    """Filter data based on a condition function"""
    return [item for item in data if condition_func(item)]

def transform_data(data, transform_func):
    """Transform data using a transformation function"""
    return [transform_func(item) for item in data]

def aggregate_data(data, aggregation_func):
    """Aggregate data using an aggregation function"""
    return aggregation_func(data)

def create_pipeline(*functions):
    """Create a data processing pipeline"""
    def pipeline(data):
        result = data
        for func in functions:
            if callable(func):
                result = func(result)
            else:
                # Handle partial functions (function with arguments)
                result = func(result)
        return result
    return pipeline

# Test data processing pipeline
raw_data = [1, 2, None, "3", 4.5, None, "6", 7, 8, "9.5", 10]

# Create processing functions
clean_step = clean_data
filter_positive = lambda data: filter_data(data, lambda x: isinstance(x, (int, float)) and x > 0)
square_transform = lambda data: transform_data(data, lambda x: x**2)
sum_aggregate = lambda data: aggregate_data(data, sum)

# Create and run pipeline
data_pipeline = create_pipeline(
    clean_step,
    filter_positive,
    square_transform,
    sum_aggregate
)

result = data_pipeline(raw_data)
print(f"1. Data pipeline result: {result}")

# Alternative: step by step
print("2. Step-by-step processing:")
step1 = clean_data(raw_data)
print(f"   After cleaning: {step1}")

step2 = filter_data(step1, lambda x: isinstance(x, (int, float)) and x > 5)
print(f"   After filtering (>5): {step2}")

step3 = transform_data(step2, lambda x: x * 2)
print(f"   After doubling: {step3}")

print("\n=== CHALLENGE 3: Text Processing Engine ===")

# Advanced text processing functions
def tokenize(text):
    """Split text into tokens (words)"""
    import re
    # Remove punctuation and split
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

def remove_stopwords(tokens, stopwords=None):
    """Remove common stopwords from tokens"""
    if stopwords is None:
        stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'}
    return [token for token in tokens if token not in stopwords]

def calculate_word_frequency(tokens):
    """Calculate frequency of each word"""
    frequency = {}
    for token in tokens:
        frequency[token] = frequency.get(token, 0) + 1
    return frequency

def find_keywords(frequency_dict, min_frequency=2):
    """Find keywords that appear frequently"""
    return {word: freq for word, freq in frequency_dict.items() if freq >= min_frequency}

def analyze_sentiment(text, positive_words=None, negative_words=None):
    """Simple sentiment analysis"""
    if positive_words is None:
        positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love', 'like', 'best', 'awesome'}
    if negative_words is None:
        negative_words = {'bad', 'terrible', 'awful', 'horrible', 'hate', 'dislike', 'worst', 'disappointing', 'poor', 'fail'}
    
    tokens = tokenize(text)
    positive_score = sum(1 for token in tokens if token in positive_words)
    negative_score = sum(1 for token in tokens if token in negative_words)
    
    sentiment_score = positive_score - negative_score
    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return {
        "sentiment": sentiment,
        "score": sentiment_score,
        "positive_words": positive_score,
        "negative_words": negative_score
    }

# Test text processing engine
sample_text = """
Python is an amazing programming language that is great for beginners and experts alike.
The syntax is clean and readable, making it easy to learn and use. Python has excellent
libraries for data science, web development, and artificial intelligence. Many developers
love Python because it allows them to write code quickly and efficiently. However, some
critics argue that Python can be slow for certain applications, but the benefits often
outweigh the drawbacks.
"""

print("1. Text analysis results:")
tokens = tokenize(sample_text)
clean_tokens = remove_stopwords(tokens)
word_freq = calculate_word_frequency(clean_tokens)
keywords = find_keywords(word_freq, min_frequency=2)
sentiment = analyze_sentiment(sample_text)

print(f"   Total tokens: {len(tokens)}")
print(f"   Tokens after stopword removal: {len(clean_tokens)}")
print(f"   Keywords (freq >= 2): {keywords}")
print(f"   Sentiment: {sentiment['sentiment']} (score: {sentiment['score']})")

# 2. Create a text processing pipeline
def create_text_pipeline(text, include_sentiment=True, min_keyword_freq=2):
    """Complete text processing pipeline"""
    tokens = tokenize(text)
    clean_tokens = remove_stopwords(tokens)
    word_freq = calculate_word_frequency(clean_tokens)
    keywords = find_keywords(word_freq, min_keyword_freq)
    
    results = {
        "original_text_length": len(text),
        "total_tokens": len(tokens),
        "unique_tokens": len(set(clean_tokens)),
        "keywords": keywords,
        "most_common_word": max(word_freq, key=word_freq.get) if word_freq else None
    }
    
    if include_sentiment:
        results["sentiment_analysis"] = analyze_sentiment(text)
    
    return results

pipeline_results = create_text_pipeline(sample_text)
print("2. Complete text pipeline results:")
for key, value in pipeline_results.items():
    if isinstance(value, dict) and len(value) > 3:
        print(f"   {key}: {type(value).__name__} with {len(value)} items")
    else:
        print(f"   {key}: {value}")

print("\n" + "="*50)
print("END OF EXERCISES - Try creating your own!")
print("="*50)