""" 
Day 18: Error Handling with try, except, else, finally 
=======================================================

Error handling is crucial for creating robust programs that can gracefully handle
unexpected situations and provide meaningful feedback to users.
"""

# ========================================
# 1. BASIC EXCEPTION HANDLING
# ========================================

print("=== Basic Exception Handling ===")

# Simple try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Catching specific exceptions
try:
    number = int("hello")
except ValueError as e:
    print(f"ValueError caught: {e}")

# Multiple exception types
try:
    numbers = [1, 2, 3]
    print(numbers[10])  # IndexError
except (IndexError, ValueError) as e:
    print(f"List or value error: {e}")

print()

# ========================================
# 2. TRY-EXCEPT-ELSE-FINALLY
# ========================================

print("=== Try-Except-Else-Finally Structure ===")

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Invalid types for division!")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Division operation completed")

# Test the function
safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("10", 2)
print()

# ========================================
# 3. NESTED EXCEPTION HANDLING
# ========================================

print("=== Nested Exception Handling ===")

def process_data(data):
    try:
        # Outer try block
        for item in data:
            try:
                # Inner try block
                processed = int(item) * 2
                print(f"Processed: {item} -> {processed}")
            except ValueError:
                print(f"Skipping invalid item: {item}")
            except Exception as e:
                print(f"Unexpected error with {item}: {e}")
    except TypeError:
        print("Error: Data must be iterable")

# Test nested handling
test_data = ["1", "2", "hello", "4", None, "5"]
process_data(test_data)
process_data("not a list")  # This will cause TypeError
print()

# ========================================
# 4. CUSTOM EXCEPTIONS
# ========================================

print("=== Custom Exceptions ===")

class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

class ValidationError(CustomError):
    """Raised when validation fails"""
    def __init__(self, message, error_code=None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

class AgeError(ValidationError):
    """Raised when age is invalid"""
    pass

def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer", "TYPE_ERROR")
    if age < 0:
        raise AgeError("Age cannot be negative", "NEGATIVE_AGE")
    if age > 150:
        raise AgeError("Age seems unrealistic", "UNREALISTIC_AGE")
    return True

# Test custom exceptions
ages_to_test = [25, -5, 200, "twenty", 30.5]

for age in ages_to_test:
    try:
        validate_age(age)
        print(f"Age {age} is valid")
    except AgeError as e:
        print(f"Age Error: {e.message} (Code: {e.error_code})")
    except ValidationError as e:
        print(f"Validation Error: {e.message} (Code: {e.error_code})")

print()

# ========================================
# 5. FILE HANDLING WITH ERROR MANAGEMENT
# ========================================

print("=== File Handling with Error Management ===")

def safe_file_operations():
    # Writing to file with error handling
    try:
        with open("test_file.txt", "w") as file:
            file.write("Hello, World!\nThis is a test file.")
        print("File written successfully")
    except IOError as e:
        print(f"Error writing file: {e}")
    
    # Reading from file with error handling
    try:
        with open("test_file.txt", "r") as file:
            content = file.read()
        print(f"File content: {content}")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except IOError as e:
        print(f"Error reading file: {e}")
    
    # Attempting to read non-existent file
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Expected error: {e}")

safe_file_operations()
print()

# ========================================
# 6. PRACTICAL EXAMPLES
# ========================================

print("=== Practical Examples ===")

# Example 1: Safe input handling
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer!")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            return None

# Example 2: Safe dictionary access
def safe_dict_access(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Key '{key}' not found, returning default value")
        return default
    except TypeError:
        print("Error: Invalid dictionary or key type")
        return default

# Test safe dictionary access
test_dict = {"name": "Alice", "age": 30}
print(safe_dict_access(test_dict, "name"))
print(safe_dict_access(test_dict, "email", "Not provided"))

# Example 3: API call simulation with error handling
import json

def simulate_api_call(data):
    try:
        # Simulate JSON processing
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        
        json_data = json.dumps(data)
        parsed_data = json.loads(json_data)
        
        # Simulate processing
        if "required_field" not in parsed_data:
            raise KeyError("Required field missing")
        
        return {"status": "success", "data": parsed_data}
    
    except json.JSONEncodeError as e:
        return {"status": "error", "message": f"JSON encoding error: {e}"}
    except json.JSONDecodeError as e:
        return {"status": "error", "message": f"JSON decoding error: {e}"}
    except KeyError as e:
        return {"status": "error", "message": f"Missing required field: {e}"}
    except TypeError as e:
        return {"status": "error", "message": f"Type error: {e}"}
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {e}"}

# Test API simulation
test_cases = [
    {"required_field": "value", "optional": "data"},
    {"optional": "data"},  # Missing required field
    "invalid data",  # Invalid type
    {"required_field": "value"}  # Valid case
]

for i, case in enumerate(test_cases):
    result = simulate_api_call(case)
    print(f"Test case {i+1}: {result}")

print()

# ========================================
# 7. CHALLENGES AND EXERCISES
# ========================================

print("=== CHALLENGES AND EXERCISES ===")
print("Try to complete these challenges:")
print()

print("Challenge 1: Safe Calculator")
print("-" * 30)

def safe_calculator():
    """
    Create a calculator that handles all possible errors gracefully.
    Should support +, -, *, / operations and handle:
    - Invalid input types
    - Division by zero
    - Invalid operations
    - Keyboard interrupts
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ZeroDivisionError("Division by zero"))
    }
    
    try:
        # Get first number
        num1 = float(input("Enter first number: "))
        
        # Get operation
        op = input("Enter operation (+, -, *, /): ").strip()
        if op not in operations:
            raise ValueError(f"Invalid operation: {op}")
        
        # Get second number
        num2 = float(input("Enter second number: "))
        
        # Perform calculation
        result = operations[op](num1, num2)
        print(f"Result: {num1} {op} {num2} = {result}")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except ZeroDivisionError as e:
        print(f"Math error: {e}")
    except KeyboardInterrupt:
        print("\nCalculation cancelled")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Uncomment to test the calculator
# safe_calculator()

print("\nChallenge 2: Data Validator")
print("-" * 30)

class DataValidationError(Exception):
    pass

def validate_user_data(user_data):
    """
    Validate user data dictionary with the following rules:
    - Must have 'name' (string, not empty)
    - Must have 'email' (string, contains @)
    - Must have 'age' (integer, 0-120)
    - Optional 'phone' (string, digits only)
    
    Raise appropriate custom exceptions for each validation failure.
    """
    try:
        # Check if data is dictionary
        if not isinstance(user_data, dict):
            raise DataValidationError("User data must be a dictionary")
        
        # Validate name
        if 'name' not in user_data:
            raise DataValidationError("Name is required")
        if not isinstance(user_data['name'], str) or not user_data['name'].strip():
            raise DataValidationError("Name must be a non-empty string")
        
        # Validate email
        if 'email' not in user_data:
            raise DataValidationError("Email is required")
        if not isinstance(user_data['email'], str) or '@' not in user_data['email']:
            raise DataValidationError("Email must be a valid email address")
        
        # Validate age
        if 'age' not in user_data:
            raise DataValidationError("Age is required")
        if not isinstance(user_data['age'], int) or not (0 <= user_data['age'] <= 120):
            raise DataValidationError("Age must be an integer between 0 and 120")
        
        # Validate optional phone
        if 'phone' in user_data:
            if not isinstance(user_data['phone'], str) or not user_data['phone'].isdigit():
                raise DataValidationError("Phone must contain digits only")
        
        return True
    
    except DataValidationError:
        raise  # Re-raise custom exceptions
    except Exception as e:
        raise DataValidationError(f"Unexpected validation error: {e}")

# Test cases for data validation
test_users = [
    {"name": "John Doe", "email": "john@example.com", "age": 25},  # Valid
    {"name": "", "email": "john@example.com", "age": 25},  # Invalid name
    {"name": "Jane", "email": "invalid-email", "age": 30},  # Invalid email
    {"name": "Bob", "email": "bob@test.com", "age": 150},  # Invalid age
    {"name": "Alice", "email": "alice@test.com", "age": 25, "phone": "abc123"},  # Invalid phone
    "not a dictionary",  # Invalid data type
]

for i, user in enumerate(test_users):
    try:
        validate_user_data(user)
        print(f"User {i+1}: Valid ✓")
    except DataValidationError as e:
        print(f"User {i+1}: Invalid - {e}")

print()

print("Challenge 3: Robust File Processor")
print("-" * 35)

def robust_file_processor(filename):
    """
    Create a function that:
    1. Reads a file safely
    2. Processes each line (convert to uppercase)
    3. Writes to a new file with '_processed' suffix
    4. Handles all possible file-related errors
    5. Provides detailed error reporting
    """
    processed_filename = filename.rsplit('.', 1)[0] + '_processed.txt'
    
    try:
        # Read original file
        with open(filename, 'r') as input_file:
            lines = input_file.readlines()
        
        # Process lines
        processed_lines = []
        for i, line in enumerate(lines):
            try:
                processed_lines.append(line.upper())
            except Exception as e:
                print(f"Warning: Could not process line {i+1}: {e}")
                processed_lines.append(line)  # Keep original if processing fails
        
        # Write processed file
        with open(processed_filename, 'w') as output_file:
            output_file.writelines(processed_lines)
        
        return {"status": "success", "processed_file": processed_filename, "lines_processed": len(processed_lines)}
    
    except FileNotFoundError:
        return {"status": "error", "message": f"File '{filename}' not found"}
    except PermissionError:
        return {"status": "error", "message": f"Permission denied accessing '{filename}'"}
    except IOError as e:
        return {"status": "error", "message": f"IO error: {e}"}
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {e}"}

# Create a test file for processing
try:
    with open("sample.txt", "w") as f:
        f.write("Hello World\nPython Programming\nError Handling\n")
    
    result = robust_file_processor("sample.txt")
    print(f"File processing result: {result}")
    
    # Test with non-existent file
    result = robust_file_processor("nonexistent.txt")
    print(f"Non-existent file result: {result}")
    
except Exception as e:
    print(f"Could not create test file: {e}")

print()

# ========================================
# 8. PRACTICE EXERCISES
# ========================================

print("=== PRACTICE EXERCISES ===")
print("Complete these exercises to master error handling:")
print()

print("Exercise 1: Enhanced Input Validator")
print("Create a function that gets user input and validates it according to specific criteria")
print("- Should retry on invalid input")
print("- Should handle keyboard interrupts gracefully")
print("- Should provide helpful error messages")
print()

print("Exercise 2: Safe Data Converter")
print("Create a function that converts data between different types safely:")
print("- String to integer/float")
print("- List to set")
print("- Dictionary value extraction")
print("- Handle all conversion errors")
print()

print("Exercise 3: Error Logging System")
print("Create a simple error logging system that:")
print("- Catches exceptions")
print("- Logs them to a file with timestamps")
print("- Categorizes errors by type")
print("- Provides error statistics")
print()

print("Exercise 4: Network Request Simulator")
print("Simulate network requests with random failures:")
print("- Timeout errors")
print("- Connection errors")
print("- Invalid response errors")
print("- Implement retry logic with exponential backoff")
print()

# ========================================
# 9. BEST PRACTICES SUMMARY
# ========================================

print("=== ERROR HANDLING BEST PRACTICES ===")
print("1. Be specific with exception types")
print("2. Use custom exceptions for domain-specific errors")
print("3. Always clean up resources (use 'with' statements)")
print("4. Log errors appropriately")
print("5. Provide meaningful error messages")
print("6. Don't ignore exceptions silently")
print("7. Use finally blocks for cleanup")
print("8. Consider the user experience when handling errors")
print()

print("=== DAY 18 COMPLETE ===")
print("You've learned comprehensive error handling in Python!")
print("Practice the challenges and exercises to reinforce your understanding.")