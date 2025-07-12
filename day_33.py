""" Day 33: Context Managers, Threading, and Python Internals """

# ============================================================================
# SECTION 1: CONTEXT MANAGERS AND THE WITH STATEMENT
# ============================================================================
print("=== CONTEXT MANAGERS ===")

# Basic context manager usage
print("File handling with context manager:")
try:
    with open("test_file.txt", "w") as file:
        file.write("Hello, World!")
        file.write("\nThis is a test file.")
    # File is automatically closed here
    print("File written and closed automatically")
except Exception as e:
    print(f"Error: {e}")

# Reading with context manager
try:
    with open("test_file.txt", "r") as file:
        content = file.read()
        print(f"File content:\n{content}")
except FileNotFoundError:
    print("Test file not found - that's okay for this demo")

# ============================================================================
# SECTION 2: CREATING CUSTOM CONTEXT MANAGERS
# ============================================================================
print("\n=== CUSTOM CONTEXT MANAGERS ===")

class DatabaseConnection:
    """Custom context manager for database connections"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing database connection: {self.db_name}")
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
        self.connection = None
        return False  # Don't suppress exceptions

# Using custom context manager
with DatabaseConnection("myapp_db") as conn:
    print(f"Using connection: {conn}")
    print("Performing database operations...")

# ============================================================================
# SECTION 3: CONTEXT MANAGERS WITH CONTEXTLIB
# ============================================================================
print("\n=== CONTEXTLIB MODULE ===")

from contextlib import contextmanager, closing
import time

@contextmanager
def timer_context(operation_name):
    """Context manager for timing operations"""
    print(f"Starting {operation_name}...")
    start_time = time.time()
    try:
        yield start_time
    finally:
        end_time = time.time()
        print(f"{operation_name} completed in {end_time - start_time:.4f} seconds")

@contextmanager
def temporary_setting(setting_name, new_value):
    """Context manager for temporarily changing a setting"""
    # In real code, this might modify a global configuration
    old_value = f"old_{setting_name}_value"
    print(f"Changing {setting_name} from {old_value} to {new_value}")
    try:
        yield new_value
    finally:
        print(f"Restoring {setting_name} to {old_value}")

# Using contextlib decorators
with timer_context("Data processing"):
    time.sleep(0.1)  # Simulate work
    print("Processing data...")

with temporary_setting("debug_mode", True):
    print("Running in debug mode")
    print("Doing debug operations...")

# ============================================================================
# SECTION 4: THREADING FUNDAMENTALS
# ============================================================================
print("\n=== THREADING BASICS ===")

import threading
import queue

def worker_function(name, work_queue, result_queue):
    """Worker function that processes items from a queue"""
    while True:
        try:
            item = work_queue.get(timeout=1)
            if item is None:
                break
            
            print(f"Worker {name} processing item: {item}")
            # Simulate work
            time.sleep(0.1)
            result = f"Processed {item} by {name}"
            result_queue.put(result)
            work_queue.task_done()
            
        except queue.Empty:
            break

# Threading example
work_q = queue.Queue()
result_q = queue.Queue()

# Add work items
for i in range(5):
    work_q.put(f"Task-{i+1}")

# Create and start threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker_function, args=(f"Thread-{i+1}", work_q, result_q))
    t.start()
    threads.append(t)

# Wait for work to complete
work_q.join()

# Signal threads to stop
for _ in threads:
    work_q.put(None)

# Wait for threads to finish
for t in threads:
    t.join()

# Collect results
print("\nResults:")
while not result_q.empty():
    print(f"  {result_q.get()}")

# ============================================================================
# SECTION 5: THREAD SYNCHRONIZATION
# ============================================================================
print("\n=== THREAD SYNCHRONIZATION ===")

class SharedCounter:
    """Thread-safe counter using locks"""
    
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def get_value(self):
        with self._lock:
            return self._value

def increment_counter(counter, name, count):
    """Function that increments counter multiple times"""
    for i in range(count):
        counter.increment()
        print(f"{name} incremented to {counter.get_value()}")
        time.sleep(0.01)

# Demonstration of thread-safe counter
shared_counter = SharedCounter()
thread1 = threading.Thread(target=increment_counter, args=(shared_counter, "Thread-1", 3))
thread2 = threading.Thread(target=increment_counter, args=(shared_counter, "Thread-2", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Final counter value: {shared_counter.get_value()}")

# ============================================================================
# SECTION 6: ASYNC/AWAIT BASICS
# ============================================================================
print("\n=== ASYNC/AWAIT INTRODUCTION ===")

import asyncio

async def async_task(name, delay):
    """Asynchronous task that simulates work"""
    print(f"Task {name} starting...")
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay} seconds")
    return f"Result from {name}"

async def main_async():
    """Main async function that runs multiple tasks concurrently"""
    print("Starting async tasks...")
    
    # Run tasks concurrently
    tasks = [
        async_task("A", 0.1),
        async_task("B", 0.2),
        async_task("C", 0.15)
    ]
    
    results = await asyncio.gather(*tasks)
    print(f"All tasks completed. Results: {results}")

# Run async example (would work in Python 3.7+)
print("Async/await would run here in a proper async environment")
print("Tasks would execute concurrently, not sequentially")

# ============================================================================
# SECTION 7: PYTHON INTERNALS AND MEMORY MANAGEMENT
# ============================================================================
print("\n=== PYTHON INTERNALS ===")

# Understanding object identity and memory
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a: {a}, id: {id(a)}")
print(f"b: {b}, id: {id(b)}")
print(f"c: {c}, id: {id(c)}")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")

# Mutable vs Immutable objects
str1 = "hello"
str2 = "hello"
print(f"\nString interning:")
print(f"str1 is str2: {str1 is str2}")  # True due to string interning

# Integer caching (for small integers)
int1 = 100
int2 = 100
int3 = 300
int4 = 300
print(f"\nInteger caching:")
print(f"100 is 100: {int1 is int2}")  # True (cached)
print(f"300 is 300: {int3 is int4}")  # May be False (not cached)

# ============================================================================
# SECTION 8: THE __NAME__ == "__MAIN__" PATTERN
# ============================================================================
print("\n=== __NAME__ == '__MAIN__' PATTERN ===")

def main():
    """Main function of the script"""
    print("This is the main function")
    print("Script is being run directly")

def utility_function():
    """Utility function that can be imported"""
    return "This function can be imported"

# This pattern allows the script to be both imported and run directly
if __name__ == "__main__":
    print("Script is being executed directly")
    main()
else:
    print("Script is being imported as a module")

# ============================================================================
# SECTION 9: DEBUGGING AND PROFILING BASICS
# ============================================================================
print("\n=== DEBUGGING BASICS ===")

def buggy_function(numbers):
    """Function with a potential bug for debugging demonstration"""
    result = []
    for i, num in enumerate(numbers):
        try:
            # This might cause division by zero
            calculated = 100 / (num - 5)
            result.append(calculated)
        except ZeroDivisionError:
            print(f"Warning: Division by zero at index {i}, value {num}")
            result.append(0)
    return result

# Debugging example
test_numbers = [10, 7, 5, 3, 1]
print("Testing buggy function:")
results = buggy_function(test_numbers)
print(f"Results: {results}")

# Using assertions for debugging
def validate_input(value):
    """Function that uses assertions for validation"""
    assert isinstance(value, (int, float)), f"Expected number, got {type(value)}"
    assert value >= 0, f"Expected non-negative number, got {value}"
    return value * 2

try:
    print(f"Validate 5: {validate_input(5)}")
    # This would raise AssertionError:
    # print(f"Validate -1: {validate_input(-1)}")
except AssertionError as e:
    print(f"Assertion error: {e}")

# ============================================================================
# SECTION 10: PRACTICAL EXERCISES
# ============================================================================
print("\n=== EXERCISES ===")

print("""
Try these exercises:

1. Create a context manager for timing code execution
2. Build a thread-safe queue for producer-consumer pattern
3. Write an async function that fetches data from multiple sources
4. Implement a simple object pool using context managers
5. Create a debugging decorator that prints function call traces
6. Build a simple cache with thread safety
""")

# Exercise example: Simple thread-safe cache
class ThreadSafeCache:
    """Simple thread-safe cache implementation"""
    
    def __init__(self, max_size=100):
        self._cache = {}
        self._max_size = max_size
        self._lock = threading.RLock()
    
    def get(self, key):
        with self._lock:
            return self._cache.get(key)
    
    def set(self, key, value):
        with self._lock:
            if len(self._cache) >= self._max_size:
                # Simple eviction: remove first item
                first_key = next(iter(self._cache))
                del self._cache[first_key]
            self._cache[key] = value
    
    def clear(self):
        with self._lock:
            self._cache.clear()

# Testing thread-safe cache
cache = ThreadSafeCache(max_size=3)
cache.set("key1", "value1")
cache.set("key2", "value2")
print(f"Cache get key1: {cache.get('key1')}")

print("\n" + "="*50)
print("Advanced Python Topics completed!")
print("You now have comprehensive coverage of:")
print("• Context managers and resource management")
print("• Threading and synchronization")  
print("• Async/await fundamentals")
print("• Python internals and memory management")
print("• Debugging patterns and best practices")
print("="*50)