""" Day 21: Built-in Functions (len, range, sum, etc.) """

def string_functions_demo():
    """Demonstrate built-in functions with strings"""
    print("=== String Functions Demo ===")
    
    text = "Python Programming"
    print(f"Original text: '{text}'")
    print(f"Length: {len(text)}")
    print(f"All characters: {list(text)}")
    print(f"Reversed: {''.join(reversed(text))}")
    
    # String methods vs built-in functions
    words = text.split()
    print(f"Words: {words}")
    print(f"Number of words: {len(words)}")
    print(f"Longest word: {max(words, key=len)}")
    print(f"Shortest word: {min(words, key=len)}")

def numeric_functions_demo():
    """Demonstrate built-in functions with numbers"""
    print("\n=== Numeric Functions Demo ===")
    
    numbers = [1, 5, 3, 9, 2, 8, 4, 7, 6]
    print(f"Numbers: {numbers}")
    print(f"Length: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    
    # Range function
    print(f"\nRange examples:")
    print(f"range(5): {list(range(5))}")
    print(f"range(2, 8): {list(range(2, 8))}")
    print(f"range(0, 10, 2): {list(range(0, 10, 2))}")
    print(f"range(10, 0, -1): {list(range(10, 0, -1))}")

def type_conversion_demo():
    """Demonstrate type conversion functions"""
    print("\n=== Type Conversion Demo ===")
    
    # String to number conversions
    str_num = "42"
    str_float = "3.14"
    print(f"String '{str_num}' to int: {int(str_num)}")
    print(f"String '{str_float}' to float: {float(str_float)}")
    
    # Number to string conversions
    num = 123
    print(f"Number {num} to string: '{str(num)}'")
    
    # Boolean conversions
    print(f"bool(0): {bool(0)}")
    print(f"bool(1): {bool(1)}")
    print(f"bool(''): {bool('')}")
    print(f"bool('hello'): {bool('hello')}")
    print(f"bool([]): {bool([])}")
    print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")

def sequence_functions_demo():
    """Demonstrate functions that work with sequences"""
    print("\n=== Sequence Functions Demo ===")
    
    # List operations
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"Fruits: {fruits}")
    print(f"Length: {len(fruits)}")
    print(f"Sorted: {sorted(fruits)}")
    print(f"Reversed: {list(reversed(fruits))}")
    print(f"Enumerated: {list(enumerate(fruits))}")
    
    # Zip function
    colors = ["red", "yellow", "dark red", "brown"]
    fruit_colors = list(zip(fruits, colors))
    print(f"Zipped fruits and colors: {fruit_colors}")
    
    # Any and all functions
    numbers = [2, 4, 6, 8, 10]
    print(f"\nNumbers: {numbers}")
    print(f"All even: {all(n % 2 == 0 for n in numbers)}")
    print(f"Any greater than 5: {any(n > 5 for n in numbers)}")

def advanced_functions_demo():
    """Demonstrate advanced built-in functions"""
    print("\n=== Advanced Functions Demo ===")
    
    # Map function
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(f"Numbers: {numbers}")
    print(f"Squared: {squared}")
    
    # Filter function
    filtered = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {filtered}")
    
    # Abs function
    values = [-5, -3, 0, 2, 4]
    absolute_values = list(map(abs, values))
    print(f"Values: {values}")
    print(f"Absolute values: {absolute_values}")
    
    # Round function
    pi_values = [3.14159, 2.71828, 1.41421]
    rounded = [round(x, 2) for x in pi_values]
    print(f"Original: {pi_values}")
    print(f"Rounded to 2 decimals: {rounded}")

def practical_examples():
    """Practical examples using built-in functions"""
    print("\n=== Practical Examples ===")
    
    # Example 1: Process a CSV-like string
    csv_data = "name,age,city\nAlice,25,New York\nBob,30,Los Angeles"
    lines = csv_data.split('\n')
    header = lines[0].split(',')
    print(f"CSV Header: {header}")
    
    for line in lines[1:]:
        values = line.split(',')
        person_data = dict(zip(header, values))
        print(f"Person: {person_data}")
    
    # Example 2: Grade calculator
    grades = [85, 92, 78, 96, 88]
    print(f"\nGrades: {grades}")
    print(f"Average: {sum(grades) / len(grades):.1f}")
    print(f"Highest: {max(grades)}")
    print(f"Lowest: {min(grades)}")
    print(f"Total points: {sum(grades)}")

def main():
    """Main function to run all demonstrations"""
    string_functions_demo()
    numeric_functions_demo()
    type_conversion_demo()
    sequence_functions_demo()
    advanced_functions_demo()
    practical_examples()

if __name__ == "__main__":
    main()

# EXERCISES:
# 1. Create a function that takes a list of numbers and returns statistics (min, max, sum, average)
# 2. Write a program that reads a sentence and counts vowels using built-in functions
# 3. Use map() and filter() to process a list of temperatures (convert and filter)
# 4. Write a function that validates user input for different data types
# 5. Create a text analyzer that counts words, characters, and sentences
# 6. Use zip() to combine multiple lists into a dictionary
# 7. Write a program that finds the most frequent character in a string
# 8. Create a function that sorts a list of dictionaries by a specific key
# 9. Build a simple number guessing game using input() and range()
# 10. Create a grade book system that uses all the built-in functions learned