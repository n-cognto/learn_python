""" Day 16: Function Arguments and Return Values """

# ========== BASIC FUNCTION ARGUMENTS ==========

def greet(name, greeting="Hello"):
    """Function with default argument"""
    return f"{greeting}, {name}!"

print("=== Basic Function Arguments ===")
print(greet("Alice"))  # Uses default greeting
print(greet("Bob", "Hi"))  # Custom greeting


# ========== POSITIONAL AND KEYWORD ARGUMENTS ==========

def create_profile(name, age, city="Unknown", country="Unknown"):
    """Function demonstrating positional and keyword arguments"""
    return {
        "name": name,
        "age": age,
        "city": city,
        "country": country
    }

print("\n=== Positional and Keyword Arguments ===")
# Positional arguments
profile1 = create_profile("John", 25)
print(f"Profile 1: {profile1}")

# Mixed positional and keyword arguments
profile2 = create_profile("Jane", 30, country="USA")
print(f"Profile 2: {profile2}")

# All keyword arguments
profile3 = create_profile(name="Mike", age=35, city="New York", country="USA")
print(f"Profile 3: {profile3}")


# ========== *ARGS AND **KWARGS ==========

def sum_numbers(*args):
    """Function that accepts variable number of arguments"""
    return sum(args)

def display_info(**kwargs):
    """Function that accepts variable keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n=== *args and **kwargs ===")
print(f"Sum of 1, 2, 3: {sum_numbers(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_numbers(1, 2, 3, 4, 5)}")

print("\nUser Info:")
display_info(name="Alice", age=28, occupation="Engineer", hobby="Reading")


# ========== RETURN VALUES ==========

def calculate_stats(numbers):
    """Function returning multiple values"""
    if not numbers:
        return None, None, None
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    
    return total, average, maximum

def is_even_odd(number):
    """Function returning boolean and string"""
    is_even = number % 2 == 0
    result = "even" if is_even else "odd"
    return is_even, result

print("\n=== Return Values ===")
numbers = [10, 20, 30, 40, 50]
total, avg, max_val = calculate_stats(numbers)
print(f"Numbers: {numbers}")
print(f"Total: {total}, Average: {avg}, Maximum: {max_val}")

is_even, result = is_even_odd(7)
print(f"7 is {result} (is_even: {is_even})")


# ========== IMPROVED CALCULATOR ==========

def calculator(x, y, operation):
    """Enhanced calculator with better error handling"""
    operations = {
        'add': lambda a, b: a + b,
        'subtract': lambda a, b: a - b,
        'multiply': lambda a, b: a * b,
        'divide': lambda a, b: a / b if b != 0 else None,
        'power': lambda a, b: a ** b,
        'modulo': lambda a, b: a % b if b != 0 else None
    }
    
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    
    result = operations[operation](x, y)
    if result is None:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return result

def get_calculator_input():
    """Function to get user input for calculator"""
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Available operations: add, subtract, multiply, divide, power, modulo")
        operation = input("Enter operation: ").lower()
        return x, y, operation
    except ValueError:
        print("Invalid number entered!")
        return None, None, None

print("\n=== Enhanced Calculator ===")
# Uncomment the following lines for interactive calculator
# x, y, operation = get_calculator_input()
# if x is not None:
#     try:
#         result = calculator(x, y, operation)
#         print(f"Result: {result}")
#     except (ValueError, ZeroDivisionError) as e:
#         print(f"Error: {e}")

# Example usage without user input
try:
    print(f"10 + 5 = {calculator(10, 5, 'add')}")
    print(f"10 / 2 = {calculator(10, 2, 'divide')}")
    print(f"2 ** 3 = {calculator(2, 3, 'power')}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")


# ========== EXERCISES AND CHALLENGES ==========
print("\n" + "="*50)
print("EXERCISES AND CHALLENGES")
print("="*50)

print("\n=== EXERCISE 1: Parameter Types Practice ===")

# 1. Function with all parameter types
def order_pizza(size, *toppings, crust="thin", **details):
    """Order a pizza with various customization options"""
    order = {
        "size": size,
        "crust": crust,
        "toppings": list(toppings),
        "details": details
    }
    
    # Calculate price
    base_price = {"small": 10, "medium": 15, "large": 20}[size]
    topping_price = len(toppings) * 2
    crust_price = 3 if crust == "stuffed" else 0
    
    order["total_price"] = base_price + topping_price + crust_price
    return order

# Test pizza ordering function
pizza1 = order_pizza("large", "pepperoni", "mushrooms", crust="stuffed", 
                    delivery=True, phone="555-1234")
pizza2 = order_pizza("medium", "cheese", "olives", "peppers")

print("1. Pizza orders:")
print(f"   Order 1: {pizza1}")
print(f"   Order 2: {pizza2}")

# 2. Function with keyword-only arguments
def create_user_profile(name, email, *, age=None, city=None, subscribe_newsletter=False):
    """Create user profile with keyword-only arguments"""
    profile = {
        "name": name,
        "email": email,
        "age": age,
        "city": city,
        "newsletter": subscribe_newsletter,
        "created_at": "2024-06-19"  # Using provided date
    }
    return profile

# Test user profile creation
user1 = create_user_profile("Alice", "alice@email.com", age=30, city="NYC")
user2 = create_user_profile("Bob", "bob@email.com", subscribe_newsletter=True)

print("2. User profiles:")
print(f"   User 1: {user1}")
print(f"   User 2: {user2}")

print("\n=== EXERCISE 2: Advanced Return Values ===")

# 1. Function returning different types based on input
def analyze_number(num):
    """Analyze a number and return comprehensive information"""
    if not isinstance(num, (int, float)):
        return {"error": "Input must be a number"}
    
    analysis = {
        "original": num,
        "absolute": abs(num),
        "is_positive": num > 0,
        "is_negative": num < 0,
        "is_zero": num == 0,
        "is_integer": isinstance(num, int) or num.is_integer(),
        "is_even": int(num) % 2 == 0 if isinstance(num, int) else None,
        "square": num ** 2,
        "square_root": num ** 0.5 if num >= 0 else None
    }
    
    return analysis

# Test number analysis
numbers = [42, -7, 0, 3.14, "invalid"]
print("1. Number analysis results:")
for num in numbers:
    result = analyze_number(num)
    if "error" in result:
        print(f"   {num}: {result['error']}")
    else:
        print(f"   {num}: positive={result['is_positive']}, even={result['is_even']}, square={result['square']}")

# 2. Function with conditional return types
def process_data(data, return_format="dict"):
    """Process data and return in different formats"""
    if not data:
        return None
    
    # Process the data
    processed = {
        "count": len(data),
        "sum": sum(data) if all(isinstance(x, (int, float)) for x in data) else None,
        "average": sum(data) / len(data) if all(isinstance(x, (int, float)) for x in data) else None,
        "min": min(data) if data else None,
        "max": max(data) if data else None
    }
    
    if return_format == "dict":
        return processed
    elif return_format == "tuple":
        return (processed["count"], processed["sum"], processed["average"])
    elif return_format == "list":
        return [processed["count"], processed["sum"], processed["average"], processed["min"], processed["max"]]
    elif return_format == "string":
        return f"Count: {processed['count']}, Sum: {processed['sum']}, Avg: {processed['average']:.2f}"
    else:
        raise ValueError("Invalid return format")

# Test data processing with different return formats
test_data = [10, 20, 30, 40, 50]
print("2. Data processing with different return formats:")
print(f"   Dict format: {process_data(test_data, 'dict')}")
print(f"   Tuple format: {process_data(test_data, 'tuple')}")
print(f"   List format: {process_data(test_data, 'list')}")
print(f"   String format: {process_data(test_data, 'string')}")

print("\n=== EXERCISE 3: Error Handling in Functions ===")

# 1. Function with comprehensive error handling
def safe_division(a, b, precision=2):
    """Perform division with comprehensive error handling"""
    try:
        # Type checking
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return {"error": "Both arguments must be numbers", "result": None}
        
        # Zero division check
        if b == 0:
            return {"error": "Division by zero is not allowed", "result": None}
        
        # Perform division
        result = a / b
        
        # Round to specified precision
        result = round(result, precision)
        
        return {"error": None, "result": result, "operation": f"{a} / {b}"}
    
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}", "result": None}

# Test safe division function
division_tests = [(10, 2), (7, 0), (15, 4), ("10", 2), (9, 3)]
print("1. Safe division tests:")
for a, b in division_tests:
    result = safe_division(a, b)
    if result["error"]:
        print(f"   {a} / {b}: ERROR - {result['error']}")
    else:
        print(f"   {a} / {b} = {result['result']}")

# 2. Function with input validation
def validate_and_process_user_input(**kwargs):
    """Validate user input and process if valid"""
    required_fields = ["name", "email", "age"]
    errors = []
    
    # Check required fields
    for field in required_fields:
        if field not in kwargs:
            errors.append(f"Missing required field: {field}")
        elif not kwargs[field]:
            errors.append(f"Field '{field}' cannot be empty")
    
    if errors:
        return {"valid": False, "errors": errors, "data": None}
    
    # Validate specific fields
    name = kwargs["name"]
    email = kwargs["email"]
    age = kwargs["age"]
    
    if not isinstance(name, str) or len(name) < 2:
        errors.append("Name must be a string with at least 2 characters")
    
    if not isinstance(email, str) or "@" not in email:
        errors.append("Email must be a valid email address")
    
    if not isinstance(age, int) or age < 0 or age > 150:
        errors.append("Age must be an integer between 0 and 150")
    
    if errors:
        return {"valid": False, "errors": errors, "data": None}
    
    # Process valid data
    processed_data = {
        "name": name.title(),
        "email": email.lower(),
        "age": age,
        "age_group": "child" if age < 18 else "adult" if age < 65 else "senior"
    }
    
    return {"valid": True, "errors": [], "data": processed_data}

# Test input validation
test_inputs = [
    {"name": "alice", "email": "ALICE@EMAIL.COM", "age": 25},
    {"name": "b", "email": "invalid-email", "age": 30},
    {"name": "Charlie", "email": "charlie@email.com"},  # Missing age
    {"name": "Diana", "email": "diana@email.com", "age": -5}
]

print("2. Input validation tests:")
for i, input_data in enumerate(test_inputs, 1):
    result = validate_and_process_user_input(**input_data)
    print(f"   Test {i}: {'VALID' if result['valid'] else 'INVALID'}")
    if result['valid']:
        print(f"     Processed: {result['data']}")
    else:
        print(f"     Errors: {result['errors']}")

print("\n=== CHALLENGE 1: Function Factory ===")

# 1. Functions that return other functions
def create_multiplier(factor):
    """Create a multiplier function with a specific factor"""
    def multiplier(x):
        return x * factor
    return multiplier

def create_validator(min_val, max_val):
    """Create a validator function for a specific range"""
    def validator(value):
        return min_val <= value <= max_val
    return validator

def create_formatter(template):
    """Create a formatter function with a specific template"""
    def formatter(**kwargs):
        try:
            return template.format(**kwargs)
        except KeyError as e:
            return f"Missing key: {e}"
    return formatter

# Test function factories
print("1. Function factory examples:")

# Create specific multiplier functions
double = create_multiplier(2)
triple = create_multiplier(3)
print(f"   Double 5: {double(5)}")
print(f"   Triple 4: {triple(4)}")

# Create specific validators
age_validator = create_validator(0, 150)
score_validator = create_validator(0, 100)
print(f"   Age 25 valid: {age_validator(25)}")
print(f"   Score 105 valid: {score_validator(105)}")

# Create specific formatters
email_formatter = create_formatter("Hello {name}, your email is {email}")
address_formatter = create_formatter("{street}, {city}, {state} {zip}")

print(f"   Email format: {email_formatter(name='Alice', email='alice@email.com')}")
print(f"   Address format: {address_formatter(street='123 Main St', city='NYC', state='NY', zip='10001')}")

print("\n=== CHALLENGE 2: Configuration System ===")

# 2. Advanced configuration handling with defaults
def create_config_manager(default_config=None):
    """Create a configuration manager with default values"""
    if default_config is None:
        default_config = {}
    
    def get_config(user_config=None, **kwargs):
        """Get configuration by merging defaults, user config, and kwargs"""
        if user_config is None:
            user_config = {}
        
        # Start with defaults
        final_config = default_config.copy()
        
        # Update with user config
        final_config.update(user_config)
        
        # Update with keyword arguments (highest priority)
        final_config.update(kwargs)
        
        return final_config
    
    return get_config

# Test configuration system
default_db_config = {
    "host": "localhost",
    "port": 5432,
    "database": "myapp",
    "timeout": 30,
    "ssl": False
}

get_db_config = create_config_manager(default_db_config)

# Different ways to get configuration
config1 = get_db_config()  # Just defaults
config2 = get_db_config({"host": "production.db.com", "ssl": True})  # With user config
config3 = get_db_config(port=3306, database="production")  # With kwargs
config4 = get_db_config({"host": "staging.db.com"}, port=5433, ssl=True)  # Both

print("2. Configuration system results:")
print(f"   Default config: {config1}")
print(f"   With user config: {config2}")
print(f"   With kwargs: {config3}")
print(f"   Mixed config: {config4}")

print("\n=== CHALLENGE 3: Data Pipeline Functions ===")

# 3. Advanced data processing pipeline
def create_data_processor(*processors):
    """Create a data processor that applies multiple processing functions"""
    def process(data, **options):
        """Process data through the pipeline"""
        result = data
        processing_log = []
        
        for i, processor in enumerate(processors):
            try:
                if callable(processor):
                    # Simple function
                    before_count = len(result) if hasattr(result, '__len__') else 'N/A'
                    result = processor(result)
                    after_count = len(result) if hasattr(result, '__len__') else 'N/A'
                    
                    processing_log.append({
                        "step": i + 1,
                        "processor": processor.__name__,
                        "before_count": before_count,
                        "after_count": after_count,
                        "success": True
                    })
                else:
                    # Assume it's a tuple of (function, args, kwargs)
                    func, args, kwargs = processor
                    before_count = len(result) if hasattr(result, '__len__') else 'N/A'
                    result = func(result, *args, **kwargs)
                    after_count = len(result) if hasattr(result, '__len__') else 'N/A'
                    
                    processing_log.append({
                        "step": i + 1,
                        "processor": func.__name__,
                        "before_count": before_count,
                        "after_count": after_count,
                        "success": True
                    })
            except Exception as e:
                processing_log.append({
                    "step": i + 1,
                    "processor": getattr(processor, '__name__', str(processor)),
                    "error": str(e),
                    "success": False
                })
                if not options.get("continue_on_error", False):
                    break
        
        return {
            "result": result,
            "log": processing_log,
            "success": all(step["success"] for step in processing_log)
        }
    
    return process

# Data processing functions
def remove_duplicates(data):
    """Remove duplicate items from data"""
    if isinstance(data, list):
        return list(dict.fromkeys(data))  # Preserves order
    return data

def filter_positive_numbers(data):
    """Filter out negative numbers"""
    if isinstance(data, list):
        return [x for x in data if isinstance(x, (int, float)) and x > 0]
    return data

def normalize_strings(data):
    """Normalize string data to lowercase"""
    if isinstance(data, list):
        return [x.lower() if isinstance(x, str) else x for x in data]
    return data

def apply_threshold(data, threshold=10):
    """Filter data based on threshold"""
    if isinstance(data, list):
        return [x for x in data if isinstance(x, (int, float)) and x >= threshold]
    return data

# Create and test data processors
simple_processor = create_data_processor(
    remove_duplicates,
    filter_positive_numbers,
    normalize_strings
)

advanced_processor = create_data_processor(
    remove_duplicates,
    filter_positive_numbers,
    (apply_threshold, [], {"threshold": 5})  # Function with arguments
)

# Test data
test_data = [1, 2, 2, -3, 4, "HELLO", "hello", 15, -8, 7, "WORLD"]

print("3. Data pipeline processing:")
result1 = simple_processor(test_data)
print(f"   Simple processor result: {result1['result']}")
print(f"   Processing steps: {len(result1['log'])}")

result2 = advanced_processor(test_data)
print(f"   Advanced processor result: {result2['result']}")
print(f"   Success: {result2['success']}")

# Show processing log
print("   Processing log for advanced processor:")
for step in result2['log']:
    if step['success']:
        print(f"     Step {step['step']}: {step['processor']} ({step['before_count']} -> {step['after_count']})")
    else:
        print(f"     Step {step['step']}: {step['processor']} FAILED - {step['error']}")

print("\n" + "="*50)
print("END OF EXERCISES - Try creating your own!")
print("="*50)