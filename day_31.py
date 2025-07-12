""" Day 31: Iterators and Generators - Advanced Iteration Patterns """

# ============================================================================
# SECTION 1: UNDERSTANDING ITERATORS
# ============================================================================
print("=== ITERATORS ===")

# Every iterable has an iterator
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print(f"List: {my_list}")
print(f"Iterator type: {type(my_iterator)}")

# Using next() to get values one by one
print(f"First value: {next(my_iterator)}")
print(f"Second value: {next(my_iterator)}")
print(f"Third value: {next(my_iterator)}")

# When iterator is exhausted, it raises StopIteration
try:
    while True:
        value = next(my_iterator)
        print(f"Value: {value}")
except StopIteration:
    print("Iterator exhausted")

# ============================================================================
# SECTION 2: CREATING CUSTOM ITERATORS
# ============================================================================
print("\n=== CUSTOM ITERATORS ===")

class NumberSequence:
    """Custom iterator that generates numbers from start to end"""
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

# Using custom iterator
print("Custom iterator example:")
numbers = NumberSequence(1, 5)
for num in numbers:
    print(f"Number: {num}")

# ============================================================================
# SECTION 3: GENERATORS WITH YIELD
# ============================================================================
print("\n=== GENERATORS ===")

def fibonacci_generator(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Using generator
print("Fibonacci generator:")
fib_gen = fibonacci_generator(10)
print(f"Generator type: {type(fib_gen)}")

for i, fib_num in enumerate(fib_gen):
    print(f"F({i}): {fib_num}")

# Generators are memory efficient
def large_range_generator(n):
    """Generate large range without storing in memory"""
    i = 0
    while i < n:
        yield i
        i += 1

# This doesn't consume memory for all values
large_gen = large_range_generator(1000000)
print(f"\nLarge generator created (memory efficient)")
print(f"First few values: {[next(large_gen) for _ in range(5)]}")

# ============================================================================
# SECTION 4: GENERATOR EXPRESSIONS
# ============================================================================
print("\n=== GENERATOR EXPRESSIONS ===")

# Generator expression (like list comprehension but with parentheses)
squares_gen = (x**2 for x in range(10))
print(f"Generator expression: {squares_gen}")
print(f"First 5 squares: {[next(squares_gen) for _ in range(5)]}")

# Memory comparison
import sys

# List comprehension (stores all values)
squares_list = [x**2 for x in range(1000)]
squares_gen = (x**2 for x in range(1000))

print(f"\nMemory usage:")
print(f"List size: {sys.getsizeof(squares_list)} bytes")
print(f"Generator size: {sys.getsizeof(squares_gen)} bytes")

# ============================================================================
# SECTION 5: ADVANCED GENERATOR PATTERNS
# ============================================================================
print("\n=== ADVANCED GENERATOR PATTERNS ===")

def file_reader_generator(filename):
    """Generator that reads file line by line"""
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                yield line_num, line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return

def pipeline_generator(data, *functions):
    """Generator that applies multiple functions in pipeline"""
    for item in data:
        result = item
        for func in functions:
            result = func(result)
        yield result

# Example: Text processing pipeline
def to_upper(text):
    return text.upper()

def add_prefix(text):
    return f">>> {text}"

def add_suffix(text):
    return f"{text} <<<"

# Using pipeline
words = ["hello", "world", "python"]
processed = pipeline_generator(words, to_upper, add_prefix, add_suffix)

print("Pipeline processing:")
for word in processed:
    print(word)

# ============================================================================
# SECTION 6: GENERATOR METHODS
# ============================================================================
print("\n=== GENERATOR METHODS ===")

def countdown_generator():
    """Generator with send(), throw(), and close() examples"""
    try:
        count = 10
        while count > 0:
            # yield returns a value and can receive a value via send()
            received = yield count
            if received is not None:
                count = received
            else:
                count -= 1
    except GeneratorExit:
        print("Generator is closing...")
    except Exception as e:
        print(f"Exception in generator: {e}")

# Using generator methods
countdown = countdown_generator()
print(f"Initial: {next(countdown)}")  # Start the generator
print(f"Next: {next(countdown)}")
print(f"Sending 5: {countdown.send(5)}")  # Send a value
print(f"Next: {next(countdown)}")

# Close the generator
countdown.close()

# ============================================================================
# SECTION 7: PRACTICAL APPLICATIONS
# ============================================================================
print("\n=== PRACTICAL APPLICATIONS ===")

def batch_processor(data, batch_size):
    """Process data in batches using generator"""
    batch = []
    for item in data:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:  # Yield remaining items
        yield batch

# Example usage
large_dataset = list(range(100))
print("Batch processing:")
for i, batch in enumerate(batch_processor(large_dataset, 10)):
    print(f"Batch {i + 1}: {batch[:3]}...{batch[-3:]} (size: {len(batch)})")
    if i >= 2:  # Show only first 3 batches
        break

def prime_generator():
    """Infinite generator for prime numbers"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Get first 10 prime numbers
primes = prime_generator()
first_10_primes = [next(primes) for _ in range(10)]
print(f"\nFirst 10 prime numbers: {first_10_primes}")

# ============================================================================
# SECTION 8: EXERCISES
# ============================================================================
print("\n=== EXERCISES ===")

print("""
Try these exercises:

1. Create a custom iterator for even numbers in a range
2. Write a generator that yields powers of 2
3. Implement a generator that reads CSV files row by row
4. Create a generator that filters and transforms data
5. Build an infinite sequence generator (like Fibonacci)
6. Write a generator that yields running averages
""")

# Exercise solutions
def even_numbers_iterator(start, end):
    """Generator for even numbers in range"""
    current = start if start % 2 == 0 else start + 1
    while current < end:
        yield current
        current += 2

def powers_of_two():
    """Infinite generator for powers of 2"""
    power = 0
    while True:
        yield 2 ** power
        power += 1

def running_average_generator(numbers):
    """Generator that yields running averages"""
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
        yield total / count

# Test exercise solutions
print("\nExercise solutions:")
print(f"Even numbers 1-10: {list(even_numbers_iterator(1, 10))}")

powers = powers_of_two()
print(f"First 8 powers of 2: {[next(powers) for _ in range(8)]}")

test_numbers = [1, 2, 3, 4, 5]
averages = list(running_average_generator(test_numbers))
print(f"Running averages of {test_numbers}: {averages}")

print("\n" + "="*50)
print("Iterators and Generators completed!")
print("Next: Study decorators and closures for advanced function patterns")
print("="*50)