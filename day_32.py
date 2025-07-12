""" Day 32: Advanced Decorators and Closures - Function Enhancement Patterns """

# ============================================================================
# SECTION 1: UNDERSTANDING CLOSURES
# ============================================================================
print("=== CLOSURES ===")

def outer_function(message):
    """Outer function that creates a closure"""
    
    def inner_function():
        """Inner function that 'closes over' the message variable"""
        print(f"Message from closure: {message}")
    
    return inner_function

# Creating closures
hello_closure = outer_function("Hello from closure!")
goodbye_closure = outer_function("Goodbye from closure!")

# Each closure remembers its own message
hello_closure()
goodbye_closure()

# ============================================================================
# SECTION 2: PRACTICAL CLOSURE EXAMPLES
# ============================================================================
print("\n=== PRACTICAL CLOSURES ===")

def make_multiplier(factor):
    """Factory function that creates multiplier closures"""
    def multiplier(number):
        return number * factor
    return multiplier

def make_counter(start=0):
    """Factory function that creates counter closures"""
    count = start
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    def reset():
        nonlocal count
        count = start
    
    def get_count():
        return count
    
    # Return multiple functions as a dictionary
    return {
        'count': counter,
        'reset': reset,
        'get': get_count
    }

# Using closure factories
double = make_multiplier(2)
triple = make_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 4: {triple(4)}")

# Counter closure example
counter1 = make_counter(10)
counter2 = make_counter(100)

print(f"Counter1: {counter1['count']()} {counter1['count']()} {counter1['count']()}")
print(f"Counter2: {counter2['count']()} {counter2['count']()}")
print(f"Counter1 current: {counter1['get']()}")

# ============================================================================
# SECTION 3: DECORATOR FUNDAMENTALS
# ============================================================================
print("\n=== DECORATOR FUNDAMENTALS ===")

def my_decorator(func):
    """Basic decorator that wraps a function"""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Function with decorator applied"""
    return f"Hello, {name}!"

# Using decorated function
message = greet("Alice")
print(f"Result: {message}")

# ============================================================================
# SECTION 4: ADVANCED DECORATORS
# ============================================================================
print("\n=== ADVANCED DECORATORS ===")

import time
import functools

def timer(func):
    """Decorator that measures function execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def retry(max_attempts=3, delay=1):
    """Decorator with parameters that retries function calls"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_attempts - 1:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed")
                        raise
        return wrapper
    return decorator

def cache(func):
    """Simple memoization decorator"""
    cached_results = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cached_results:
            print(f"Cache hit for {func.__name__}")
            return cached_results[key]
        
        print(f"Computing {func.__name__}")
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result
    
    return wrapper

# Using advanced decorators
@timer
@cache
def fibonacci(n):
    """Recursive Fibonacci with timing and caching"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@retry(max_attempts=3, delay=0.1)
def unreliable_function():
    """Function that sometimes fails"""
    import random
    if random.random() < 0.7:
        raise Exception("Random failure!")
    return "Success!"

# Testing decorators
print("Testing fibonacci with cache and timer:")
print(f"fib(10) = {fibonacci(10)}")
print(f"fib(10) = {fibonacci(10)}")  # Should hit cache

print("\nTesting retry decorator:")
try:
    result = unreliable_function()
    print(f"Result: {result}")
except Exception as e:
    print(f"Final failure: {e}")

# ============================================================================
# SECTION 5: CLASS-BASED DECORATORS
# ============================================================================
print("\n=== CLASS-BASED DECORATORS ===")

class CallCounter:
    """Decorator class that counts function calls"""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)
    
    def reset_count(self):
        self.count = 0

class RateLimiter:
    """Decorator class that limits function call rate"""
    
    def __init__(self, max_calls=5, time_window=60):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = []
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove old calls outside the time window
            self.calls = [call_time for call_time in self.calls 
                         if now - call_time < self.time_window]
            
            if len(self.calls) >= self.max_calls:
                raise Exception(f"Rate limit exceeded: {self.max_calls} calls per {self.time_window} seconds")
            
            self.calls.append(now)
            return func(*args, **kwargs)
        return wrapper

# Using class-based decorators
@CallCounter
def say_hello(name):
    return f"Hello, {name}!"

@RateLimiter(max_calls=3, time_window=5)
def limited_function():
    return "This function is rate limited"

# Testing class decorators
print("Testing call counter:")
print(say_hello("Alice"))
print(say_hello("Bob"))
print(say_hello("Charlie"))

# ============================================================================
# SECTION 6: DECORATOR PATTERNS AND BEST PRACTICES
# ============================================================================
print("\n=== DECORATOR PATTERNS ===")

def validate_types(**expected_types):
    """Decorator that validates function argument types"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Validate types
            for arg_name, expected_type in expected_types.items():
                if arg_name in bound_args.arguments:
                    value = bound_args.arguments[arg_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(f"{arg_name} must be {expected_type.__name__}, got {type(value).__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def log_calls(logger=None):
    """Decorator that logs function calls"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_str = ', '.join(repr(arg) for arg in args)
            kwargs_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
            all_args = ', '.join(filter(None, [args_str, kwargs_str]))
            
            log_message = f"Calling {func.__name__}({all_args})"
            if logger:
                logger.info(log_message)
            else:
                print(f"LOG: {log_message}")
            
            try:
                result = func(*args, **kwargs)
                if logger:
                    logger.info(f"{func.__name__} returned {result!r}")
                else:
                    print(f"LOG: {func.__name__} returned {result!r}")
                return result
            except Exception as e:
                if logger:
                    logger.error(f"{func.__name__} raised {e!r}")
                else:
                    print(f"LOG: {func.__name__} raised {e!r}")
                raise
        return wrapper
    return decorator

# Using advanced decorator patterns
@validate_types(name=str, age=int)
@log_calls()
def create_person(name, age=0):
    """Create a person with validation and logging"""
    if age < 0:
        raise ValueError("Age cannot be negative")
    return {"name": name, "age": age}

# Testing advanced patterns
print("Testing type validation and logging:")
try:
    person1 = create_person("Alice", 25)
    person2 = create_person("Bob")  # Uses default age
    # This will raise a type error:
    # person3 = create_person("Charlie", "twenty")
except Exception as e:
    print(f"Error: {e}")

# ============================================================================
# SECTION 7: DECORATOR UTILITIES
# ============================================================================
print("\n=== DECORATOR UTILITIES ===")

def compose(*decorators):
    """Compose multiple decorators into one"""
    def decorator(func):
        for dec in reversed(decorators):
            func = dec(func)
        return func
    return decorator

def conditional_decorator(condition, decorator):
    """Apply decorator only if condition is True"""
    def actual_decorator(func):
        if condition:
            return decorator(func)
        return func
    return actual_decorator

# Example usage
DEBUG = True

@compose(
    timer,
    conditional_decorator(DEBUG, cache),
    log_calls()
)
def complex_calculation(n):
    """Function with composed decorators"""
    return sum(i * i for i in range(n))

print("Testing composed decorators:")
result = complex_calculation(1000)
print(f"Result: {result}")

# ============================================================================
# SECTION 8: EXERCISES
# ============================================================================
print("\n=== EXERCISES ===")

print("""
Try these exercises:

1. Create a decorator that measures memory usage of a function
2. Write a decorator that automatically retries on specific exceptions
3. Implement a decorator that caches results to a file
4. Create a decorator that limits concurrent executions
5. Build a decorator that validates function return types
6. Write a decorator that implements simple access control
""")

# Exercise example: Access control decorator
def require_permission(permission):
    """Decorator that checks user permissions"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # In a real application, this would check actual user permissions
            user_permissions = kwargs.get('user_permissions', set())
            if permission not in user_permissions:
                raise PermissionError(f"Access denied: requires '{permission}' permission")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_permission('admin')
def delete_user(user_id, user_permissions=None):
    return f"User {user_id} deleted"

# Testing access control
try:
    result = delete_user(123, user_permissions={'admin', 'read'})
    print(f"Success: {result}")
except PermissionError as e:
    print(f"Access denied: {e}")

print("\n" + "="*50)
print("Decorators and Closures completed!")
print("Next: Study context managers and advanced Python features")
print("="*50)