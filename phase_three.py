# Python Advanced Programming - Phase 3 Guide

"""
This guide covers key advanced Python topics to master after completing the fundamentals (Phase 1)
and intermediate concepts (Phase 2).

PHASE 3 TOPICS:
1. Advanced Data Structures
2. Algorithm Techniques 
3. Functional Programming
4. Advanced OOP & Design Patterns
5. Concurrency & Parallelism
"""

print("="*70)
print("1. ADVANCED DATA STRUCTURES")
print("="*70)

# ============================================================================
# ADVANCED COLLECTIONS
# ============================================================================

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

print("\n--- COUNTER ---")
# Counter: specialized dictionary for counting hashable objects
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
word_counts = Counter(words)
print(f"Word counts: {word_counts}")
print(f"Most common 2 words: {word_counts.most_common(2)}")
print(f"Count of 'apple': {word_counts['apple']}")

print("\n--- DEFAULTDICT ---")
# defaultdict: dictionary with default value for missing keys
fruit_colors = defaultdict(list)  # Default value is an empty list
fruit_colors['apple'].append('red')  # No KeyError even though 'apple' doesn't exist yet
fruit_colors['apple'].append('green')
fruit_colors['banana'].append('yellow')
print(f"Fruit colors: {dict(fruit_colors)}")

print("\n--- DEQUE (DOUBLE-ENDED QUEUE) ---")
# deque: efficient appends and pops from both ends
queue = deque(['task1', 'task2', 'task3'])
queue.append('task4')  # Add to right
queue.appendleft('task0')  # Add to left
print(f"Queue: {queue}")
print(f"Popped from right: {queue.pop()}")
print(f"Popped from left: {queue.popleft()}")
print(f"Final queue: {queue}")

print("\n--- NAMEDTUPLE ---")
# namedtuple: factory function for creating tuple subclasses with named fields
Person = namedtuple('Person', ['name', 'age', 'job'])
alice = Person('Alice', 30, 'Engineer')
print(f"Person: {alice}")
print(f"Name: {alice.name}, Age: {alice.age}, Job: {alice.job}")
# Can also access by index: alice[0], alice[1], alice[2]

print("\n--- ORDEREDDICT ---")
# OrderedDict: dictionary that remembers insertion order
# Note: In Python 3.7+, regular dict also maintains insertion order
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(f"OrderedDict: {od}")
od.move_to_end('first')  # Move to end
print(f"After moving 'first' to end: {od}")

# ============================================================================
# HEAPS
# ============================================================================

import heapq

print("\n--- HEAPS (PRIORITY QUEUE) ---")
# Heaps: binary tree structure that maintains heap property
# Min heap: parent is smaller than children
numbers = [10, 5, 8, 1, 7, 3]
print(f"Original numbers: {numbers}")

# heapify: transform list into a heap in-place
heapq.heapify(numbers)
print(f"After heapify (min heap): {numbers}")

# heappush: add element to heap
heapq.heappush(numbers, 2)
print(f"After pushing 2: {numbers}")

# heappop: remove and return smallest element
smallest = heapq.heappop(numbers)
print(f"Popped smallest: {smallest}")
print(f"Heap after pop: {numbers}")

# nlargest, nsmallest: get n largest/smallest elements
nums = [10, 5, 8, 1, 7, 3, 2, 9, 4, 6]
print(f"Original list: {nums}")
print(f"3 largest: {heapq.nlargest(3, nums)}")
print(f"3 smallest: {heapq.nsmallest(3, nums)}")

# ============================================================================
# ADVANCED DICTIONARIES AND SETS
# ============================================================================

print("\n--- DICTIONARY COMPREHENSIONS ---")
# Dictionary comprehension
squares = {x: x**2 for x in range(6)}
print(f"Squares dictionary: {squares}")

# Conditional dictionary comprehension
even_squares = {x: x**2 for x in range(11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

print("\n--- ADVANCED SET OPERATIONS ---")
# Advanced set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {1, 5, 9}

print(f"A: {A}, B: {B}, C: {C}")
print(f"A | B (union): {A | B}")
print(f"A & B (intersection): {A & B}")
print(f"A - B (difference): {A - B}")
print(f"A ^ B (symmetric difference): {A ^ B}")
print(f"A.issubset(B): {A.issubset(B)}")
print(f"A.issuperset(C): {A.issuperset(C)}")

print("="*70)
print("2. ALGORITHM TECHNIQUES")
print("="*70)

# ============================================================================
# TWO-POINTER TECHNIQUE
# ============================================================================

print("\n--- TWO-POINTER TECHNIQUE ---")
# Two-pointer technique for efficient array operations

def is_palindrome(s):
    """Check if string is a palindrome using two pointers"""
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(f"'madam' is palindrome: {is_palindrome('madam')}")
print(f"'hello' is palindrome: {is_palindrome('hello')}")

def two_sum_sorted(numbers, target):
    """Find pair that sums to target in sorted array"""
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]  # No solution

sorted_array = [1, 2, 5, 8, 13]
print(f"Indices of pair summing to 13: {two_sum_sorted(sorted_array, 13)}")

def remove_duplicates(nums):
    """Remove duplicates from sorted array in-place"""
    if not nums:
        return 0
    
    # Position to place the next unique element
    write_pos = 1
    
    # Iterate through array starting from second element
    for read_pos in range(1, len(nums)):
        if nums[read_pos] != nums[read_pos - 1]:
            nums[write_pos] = nums[read_pos]
            write_pos += 1
    
    return write_pos  # New length

nums = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(nums)
print(f"After removing duplicates: {nums[:new_length]}")

# ============================================================================
# SLIDING WINDOW
# ============================================================================

print("\n--- SLIDING WINDOW TECHNIQUE ---")
# Sliding window for subarray/substring problems

def max_sum_subarray(arr, k):
    """Find maximum sum subarray of size k"""
    n = len(arr)
    if n < k:
        return None
    
    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window and update max_sum
    for i in range(k, n):
        # Add next element and remove first element of previous window
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 3
print(f"Maximum sum subarray of size {k}: {max_sum_subarray(arr, k)}")

def longest_substring_without_repeating_chars(s):
    """Find longest substring without repeating characters"""
    if not s:
        return 0
    
    char_set = set()
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # If character already in window, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to window
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(f"Longest substring without repeats in 'abcabcbb': {longest_substring_without_repeating_chars('abcabcbb')}")
print(f"Longest substring without repeats in 'bbbbb': {longest_substring_without_repeating_chars('bbbbb')}")

# ============================================================================
# DYNAMIC PROGRAMMING
# ============================================================================

print("\n--- DYNAMIC PROGRAMMING ---")
# Using memoization and tabulation for optimization

def fibonacci_memoization(n, memo={}):
    """Compute nth Fibonacci number using memoization"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

print("Fibonacci using memoization:")
for i in range(10):
    print(f"F({i}) = {fibonacci_memoization(i)}")

def fibonacci_tabulation(n):
    """Compute nth Fibonacci number using tabulation"""
    if n <= 1:
        return n
    
    # Initialize table
    dp = [0] * (n + 1)
    dp[1] = 1
    
    # Fill table bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print("\nFibonacci using tabulation:")
for i in range(10):
    print(f"F({i}) = {fibonacci_tabulation(i)}")

print("="*70)
print("3. FUNCTIONAL PROGRAMMING")
print("="*70)

# ============================================================================
# HIGHER-ORDER FUNCTIONS
# ============================================================================

print("\n--- HIGHER-ORDER FUNCTIONS ---")
# Functions that take functions as arguments or return functions

# map: apply function to all items in iterable
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}, Squared: {squared}")

# filter: filter items based on function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# reduce: apply function cumulatively to items
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of all numbers: {product}")

# sorted with key function
students = [
    ("Alice", 92),
    ("Bob", 85),
    ("Charlie", 90),
    ("David", 88)
]
sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Students sorted by grade: {sorted_by_grade}")

# ============================================================================
# LAMBDA FUNCTIONS AND COMPREHENSIONS
# ============================================================================

print("\n--- ADVANCED COMPREHENSIONS ---")
# List, set, and dictionary comprehensions

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
print(f"Original matrix: {matrix}")
print(f"Flattened: {flattened}")

# Transposing a matrix
transposed = [[row[i] for row in matrix] for i in range(3)]
print(f"Transposed: {transposed}")

# Set comprehension
sentence = "hello world hello python"
unique_chars = {char for char in sentence if char.isalpha()}
print(f"Unique characters: {unique_chars}")

# ============================================================================
# CLOSURES AND DECORATORS
# ============================================================================

print("\n--- CLOSURES AND DECORATORS ---")
# Functions that remember their enclosing scope

def make_multiplier(factor):
    """Closure that creates a function that multiplies by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")

# Advanced decorator with parameters
def repeat(n):
    """Decorator that runs function n times"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"

result = greet("Alice")
print(f"Result: {result}")

print("="*70)
print("4. ADVANCED OOP & DESIGN PATTERNS")
print("="*70)

# ============================================================================
# MAGIC METHODS
# ============================================================================

print("\n--- MAGIC METHODS ---")
# Special methods for customizing class behavior

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        """Official string representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        """Informal string representation"""
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        """Vector addition with + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Vector subtraction with - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Scalar multiplication with * operator"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Equality comparison with == operator"""
        return self.x == other.x and self.y == other.y
    
    def __abs__(self):
        """Absolute value (magnitude) with abs() function"""
        return (self.x**2 + self.y**2)**0.5
    
    def __bool__(self):
        """Boolean conversion with bool() function"""
        return self.x != 0 or self.y != 0

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"abs(v1): {abs(v1)}")
print(f"bool(v1): {bool(v1)}")
print(f"bool(Vector(0, 0)): {bool(Vector(0, 0))}")

# ============================================================================
# DESIGN PATTERNS
# ============================================================================

print("\n--- DESIGN PATTERNS ---")
# Reusable solutions to common problems

# Singleton pattern
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = 0
        return cls._instance

s1 = Singleton()
s1.value = 5
s2 = Singleton()
print(f"s1.value: {s1.value}, s2.value: {s2.value}")
print(f"s1 is s2: {s1 is s2}")

# Factory pattern
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_factory(animal_type):
    """Factory function to create animals"""
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError(f"Unknown animal type: {animal_type}")

dog = animal_factory("dog")
cat = animal_factory("cat")
print(f"Dog says: {dog.speak()}")
print(f"Cat says: {cat.speak()}")

print("="*70)
print("5. CONCURRENCY & PARALLELISM")
print("="*70)

# ============================================================================
# THREADING
# ============================================================================

print("\n--- THREADING ---")
# Multiple threads for concurrent execution

import threading
import time

def worker(name, delay):
    """Thread worker function"""
    print(f"{name} starting")
    for i in range(3):
        time.sleep(delay)
        print(f"{name} working... ({i+1})")
    print(f"{name} finished")

print("Creating threads...")
t1 = threading.Thread(target=worker, args=("Thread-1", 0.5))
t2 = threading.Thread(target=worker, args=("Thread-2", 0.7))

print("Starting threads...")
t1.start()
t2.start()

print("Waiting for threads to complete...")
t1.join()
t2.join()
print("All threads completed")

# ============================================================================
# MULTIPROCESSING
# ============================================================================

print("\n--- MULTIPROCESSING ---")
# Multiple processes for parallel execution

import multiprocessing

def process_worker(name, numbers, result_queue):
    """Process worker function"""
    print(f"{name} processing {len(numbers)} numbers")
    result = sum(numbers)
    result_queue.put(result)
    print(f"{name} finished: sum = {result}")

def demonstrate_multiprocessing():
    # Create a queue to share results
    result_queue = multiprocessing.Queue()
    
    # Create processes
    p1 = multiprocessing.Process(target=process_worker, 
                                args=("Process-1", list(range(10)), result_queue))
    p2 = multiprocessing.Process(target=process_worker, 
                                args=("Process-2", list(range(10, 20)), result_queue))
    
    # Start processes
    p1.start()
    p2.start()
    
    # Wait for processes to complete
    p1.join()
    p2.join()
    
    # Get results from queue
    results = [result_queue.get() for _ in range(2)]
    print(f"Total sum from all processes: {sum(results)}")

# Note: On some platforms, this demonstration needs to be run in a __main__ block
# But for our guide, we'll just print the explanation
print("In a full program, multiprocessing would allow parallel execution across CPU cores.")
print("Each process would run independently with its own memory space.")
print("Results could be shared via Queue, Pipe, or shared memory.")

# ============================================================================
# ASYNCIO
# ============================================================================

print("\n--- ASYNCIO ---")
# Asynchronous I/O for concurrent execution

import asyncio

async def async_task(name, delay):
    """Asynchronous task"""
    print(f"{name} starting")
    for i in range(3):
        await asyncio.sleep(delay)
        print(f"{name} working... ({i+1})")
    print(f"{name} finished")
    return f"{name} result"

async def main():
    """Main async function"""
    print("Creating tasks...")
    task1 = asyncio.create_task(async_task("Task-1", 0.5))
    task2 = asyncio.create_task(async_task("Task-2", 0.7))
    
    print("Waiting for tasks to complete...")
    results = await asyncio.gather(task1, task2)
    print(f"All tasks completed with results: {results}")

# For simplicity in our guide, we'll just explain asyncio
print("In a full program, asyncio would allow concurrent execution of I/O-bound tasks.")
print("Tasks would cooperatively yield control during waiting periods.")
print("This is ideal for network operations, file I/O, and other waiting-heavy tasks.")

# ============================================================================
# CONCLUSION
# ============================================================================

print("\n" + "="*70)
print("PHASE 3 COMPLETE!")
print("="*70)

print("""
🎉 Congratulations! You've explored Python's advanced topics!

Key concepts mastered:
✅ Advanced data structures like Counter, defaultdict, heapq
✅ Algorithm techniques like two-pointer and sliding window
✅ Functional programming with higher-order functions and comprehensions
✅ Advanced OOP with magic methods and design patterns
✅ Concurrency and parallelism with threading, multiprocessing, and asyncio

Next steps:
1. Practice these concepts by building real-world projects
2. Explore specific domains like web development, data science, or machine learning
3. Contribute to open-source Python projects
4. Prepare for technical interviews with algorithm challenges

Remember: The best way to master these advanced concepts is through practice!
""")