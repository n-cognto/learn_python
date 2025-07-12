# 🚀 Python Performance Tips & Tricks

> **Master these techniques to write faster, more efficient Python code!**

Welcome to the ultimate collection of Python performance optimizations and coding best practices. These tips will help you write cleaner, faster, and more Pythonic code.

---

## 📊 Table of Contents

- [🏃‍♂️ Performance Optimization](#️-performance-optimization)
- [🔧 Memory Management](#-memory-management)
- [🎯 Pythonic Code Patterns](#-pythonic-code-patterns)
- [🐛 Debugging & Profiling](#-debugging--profiling)
- [📚 Advanced Techniques](#-advanced-techniques)

---

## 🏃‍♂️ Performance Optimization

### 1. **List Comprehensions - Lightning Fast**
List comprehensions are significantly faster than traditional loops.

```python
# ✅ FAST - List comprehension
numbers = [x**2 for x in range(100000) if x % 2 == 0]

# ❌ SLOW - Traditional loop
numbers = []
for x in range(100000):
    if x % 2 == 0: 
        numbers.append(x**2)

# 📊 Performance gain: ~2-3x faster
```

### 2. **Leverage Built-In Functions**
Python's built-in functions are implemented in C and are much faster than pure Python solutions.

```python
# ✅ FAST - Built-in functions
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
length = len(numbers)

# ❌ SLOW - Manual implementation
total = 0
for num in numbers:
    total += num

# 📊 Performance gain: ~5-10x faster
```

### 3. **Function Calls Are Expensive**
Minimize function calls inside loops by moving iterations inside functions.

```python
# ✅ FAST - Iterate inside function
def process_data(data):
    results = []
    for item in data:
        # Process each item
        results.append(item * 2 + 1)
    return results

# ❌ SLOW - Function call per iteration
def process_item(item):
    return item * 2 + 1

results = [process_item(item) for item in data]

# 📊 Performance gain: ~20-30% faster
```

### 4. **Lazy Module Importing**
Import only what you need to reduce overhead.

```python
# ✅ FAST - Specific imports
from time import sleep
from os.path import join, exists
from collections import defaultdict

# ❌ SLOW - Full module imports
import time
import os
import collections

# Then using: time.sleep(), os.path.join(), etc.

# 📊 Performance gain: Faster startup time
```

### 5. **Harness the Power of NumPy**
NumPy operations are implemented in C and are incredibly fast for numerical computations.

```python
import numpy as np

# ✅ FAST - NumPy operations
arr = np.array(range(1000000))
result = np.sqrt(arr) * 2 + 1

# ❌ SLOW - Pure Python
import math
result = [math.sqrt(x) * 2 + 1 for x in range(1000000)]

# 📊 Performance gain: ~50-100x faster for large datasets
```

### 6. **Multiprocessing for CPU-Bound Tasks**
Use multiprocessing to leverage multiple CPU cores.

```python
from multiprocessing import Pool
import time

def cpu_intensive_task(n):
    return sum(i * i for i in range(n))

# ✅ FAST - Multiprocessing
def parallel_processing():
    with Pool() as pool:
        results = pool.map(cpu_intensive_task, [100000] * 4)
    return results

# ❌ SLOW - Single process
def sequential_processing():
    results = [cpu_intensive_task(100000) for _ in range(4)]
    return results

# 📊 Performance gain: ~4x faster on 4-core machine
```

### 7. **Be Mindful of Library Overhead**
Choose lightweight libraries when performance matters.

```python
# ✅ FAST - Lightweight alternatives
import ujson as json  # Faster than standard json
import orjson  # Even faster JSON library

# For simple HTTP requests
import httpx  # Async-capable, modern
# vs
import requests  # Heavier, synchronous

# 📊 Choose based on your specific needs
```

### 8. **Avoid Global Variables**
Local variable access is faster than global variable access.

```python
# ✅ FAST - Local variables
def process_data():
    local_config = {"threshold": 100}
    data = [1, 2, 3, 4, 5]
    
    return [x for x in data if x > local_config["threshold"]]

# ❌ SLOW - Global variables
GLOBAL_CONFIG = {"threshold": 100}
GLOBAL_DATA = [1, 2, 3, 4, 5]

def process_data_slow():
    return [x for x in GLOBAL_DATA if x > GLOBAL_CONFIG["threshold"]]

# 📊 Performance gain: ~10-15% faster
```

### 9. **Algorithm and Approach Optimization**
Sometimes a completely different approach yields better performance.

```python
# ✅ FAST - Set intersection
list1 = list(range(10000))
list2 = list(range(5000, 15000))
common = list(set(list1) & set(list2))

# ❌ SLOW - Nested loops
common = []
for item in list1:
    if item in list2:
        common.append(item)

# 📊 Performance gain: ~100x faster for large lists
```

### 10. **Choose the Right Data Structure**
Data structure choice dramatically impacts performance.

```python
# ✅ FAST - Dictionary/Set lookup O(1)
lookup_dict = {i: True for i in range(10000)}
result = 5000 in lookup_dict  # Instant

# ❌ SLOW - List lookup O(n)
lookup_list = list(range(10000))
result = 5000 in lookup_list  # Linear search

# 📊 Performance gain: ~1000x faster for large collections
```

---

## 🔧 Memory Management

### 11. **Use Generators for Large Datasets**
Generators are memory-efficient for processing large amounts of data.

```python
# ✅ MEMORY EFFICIENT - Generator
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# ❌ MEMORY INTENSIVE - List
def fibonacci_list(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# 📊 Memory savings: Constant vs O(n) memory usage
```

### 12. **Use __slots__ for Memory-Intensive Classes**
Reduce memory usage for classes with many instances.

```python
# ✅ MEMORY EFFICIENT
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ❌ MEMORY INTENSIVE
class PointRegular:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 📊 Memory savings: ~40-50% less memory per instance
```

### 13. **String Concatenation Optimization**
Use join() for multiple string concatenations.

```python
# ✅ FAST - join() method
words = ['Python', 'is', 'awesome', 'and', 'fast']
sentence = ' '.join(words)

# ❌ SLOW - String concatenation
sentence = ''
for word in words:
    sentence += word + ' '

# 📊 Performance gain: ~10x faster for many strings
```

---

## 🎯 Pythonic Code Patterns

### 14. **Use enumerate() Instead of range(len())**
More readable and potentially faster.

```python
# ✅ PYTHONIC
items = ['apple', 'banana', 'cherry']
for i, item in enumerate(items):
    print(f"{i}: {item}")

# ❌ UNPYTHONIC
for i in range(len(items)):
    print(f"{i}: {items[i]}")
```

### 15. **Dictionary get() with Defaults**
Avoid KeyError exceptions and simplify code.

```python
# ✅ PYTHONIC
config = {'timeout': 30}
timeout = config.get('timeout', 60)  # Default to 60
retries = config.get('retries', 3)   # Default to 3

# ❌ VERBOSE
if 'timeout' in config:
    timeout = config['timeout']
else:
    timeout = 60
```

### 16. **Use any() and all() for Boolean Operations**
Clean and efficient boolean testing.

```python
# ✅ PYTHONIC
numbers = [2, 4, 6, 8, 10]
all_even = all(n % 2 == 0 for n in numbers)
any_large = any(n > 100 for n in numbers)

# ❌ VERBOSE
all_even = True
for n in numbers:
    if n % 2 != 0:
        all_even = False
        break
```

### 17. **F-Strings for String Formatting**
Fastest and most readable string formatting method.

```python
# ✅ FAST & READABLE - f-strings (Python 3.6+)
name = "Alice"
age = 30
message = f"Hello {name}, you are {age} years old"

# ❌ SLOWER - .format() method
message = "Hello {}, you are {} years old".format(name, age)

# ❌ SLOWEST - % formatting
message = "Hello %s, you are %d years old" % (name, age)

# 📊 Performance: f-strings > .format() > % formatting
```

### 18. **Context Managers for Resource Management**
Always use context managers for file operations and resource cleanup.

```python
# ✅ SAFE & PYTHONIC
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed

# Custom context manager
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        print(f"Execution time: {time.time() - start:.2f}s")

with timer():
    # Your code here
    time.sleep(1)
```

---

## 🐛 Debugging & Profiling

### 19. **Use cProfile for Performance Analysis**
Identify bottlenecks in your code.

```python
import cProfile
import pstats

def slow_function():
    return sum(i**2 for i in range(100000))

# Profile your code
cProfile.run('slow_function()', 'profile_output.prof')

# Analyze results
stats = pstats.Stats('profile_output.prof')
stats.sort_stats('cumulative').print_stats(10)
```

### 20. **Use timeit for Micro-benchmarks**
Accurately measure small code snippets.

```python
import timeit

# Compare different approaches
setup = "data = list(range(1000))"

method1 = "result = [x*2 for x in data]"
method2 = "result = list(map(lambda x: x*2, data))"

time1 = timeit.timeit(method1, setup=setup, number=10000)
time2 = timeit.timeit(method2, setup=setup, number=10000)

print(f"List comprehension: {time1:.4f}s")
print(f"Map function: {time2:.4f}s")
```

### 21. **Logging Instead of Print**
Use logging for better debugging and production code.

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def process_data(data):
    logger.info(f"Processing {len(data)} items")
    try:
        result = [x * 2 for x in data]
        logger.info("Processing completed successfully")
        return result
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        raise
```

---

## 📚 Advanced Techniques

### 22. **Memoization for Expensive Function Calls**
Cache results of expensive function calls.

```python
from functools import lru_cache

# ✅ OPTIMIZED - With memoization
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# ❌ SLOW - Without memoization (exponential time)
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# 📊 Performance gain: Exponential to linear time complexity
```

### 23. **Use deque for Queue Operations**
More efficient than lists for queue-like operations.

```python
from collections import deque

# ✅ FAST - deque for queues
queue = deque([1, 2, 3, 4, 5])
queue.appendleft(0)  # O(1)
queue.pop()          # O(1)

# ❌ SLOW - list for queues
queue = [1, 2, 3, 4, 5]
queue.insert(0, 0)   # O(n)
queue.pop()          # O(1)

# 📊 Performance: deque operations are O(1) vs list O(n)
```

### 24. **Itertools for Efficient Iteration**
Use itertools for memory-efficient iterations.

```python
import itertools

# Efficient combinations and permutations
data = [1, 2, 3, 4]

# All combinations of length 2
combinations = list(itertools.combinations(data, 2))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# Infinite sequences
counter = itertools.count(start=1, step=2)  # 1, 3, 5, 7, ...
cycler = itertools.cycle(['A', 'B', 'C'])  # A, B, C, A, B, C, ...

# Chain multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = itertools.chain(list1, list2)  # 1, 2, 3, 4, 5, 6
```

### 25. **Dataclasses for Simple Classes**
Reduce boilerplate code with dataclasses.

```python
from dataclasses import dataclass, field
from typing import List

# ✅ CLEAN - dataclass
@dataclass
class Person:
    name: str
    age: int
    skills: List[str] = field(default_factory=list)
    
    def add_skill(self, skill: str):
        self.skills.append(skill)

# ❌ VERBOSE - traditional class
class PersonTraditional:
    def __init__(self, name: str, age: int, skills: List[str] = None):
        self.name = name
        self.age = age
        self.skills = skills or []
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, skills={self.skills})"
    
    def __eq__(self, other):
        if not isinstance(other, PersonTraditional):
            return False
        return (self.name, self.age, self.skills) == (other.name, other.age, other.skills)
```

---

## 🎯 **Quick Reference Checklist**

### ⚡ **Performance Essentials**
- [ ] Use list comprehensions instead of loops
- [ ] Leverage built-in functions (sum, max, min, len)
- [ ] Choose the right data structure (dict/set for lookups)
- [ ] Use generators for large datasets
- [ ] Profile code with cProfile and timeit

### 🧠 **Memory Optimization**
- [ ] Use generators instead of lists when possible
- [ ] Implement __slots__ for memory-intensive classes
- [ ] Use deque for queue operations
- [ ] Employ lazy evaluation with itertools

### 🔧 **Code Quality**
- [ ] Use f-strings for formatting
- [ ] Implement proper error handling
- [ ] Use context managers for resources
- [ ] Apply type hints for better code documentation
- [ ] Follow PEP 8 style guidelines

### 🚀 **Advanced Patterns**
- [ ] Implement memoization for expensive functions
- [ ] Use dataclasses for simple data containers
- [ ] Apply functional programming with map/filter/reduce
- [ ] Utilize multiprocessing for CPU-bound tasks

---

## 🏆 **Remember**

> **"Premature optimization is the root of all evil"** - Donald Knuth

1. **Profile first** - Identify actual bottlenecks before optimizing
2. **Readability matters** - Maintainable code is often more valuable than micro-optimizations
3. **Test thoroughly** - Ensure optimizations don't break functionality
4. **Consider trade-offs** - Sometimes memory vs speed, sometimes simplicity vs performance

---

**Happy optimizing! 🐍✨**

*Keep learning, keep optimizing, and most importantly - keep coding!*