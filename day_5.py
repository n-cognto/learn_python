""" 
Day 5: String Operations and Advanced Text Processing
===================================================

Learning Objectives:
- Master string methods and operations
- Understand string slicing and indexing
- Learn advanced string formatting techniques
- Practice text processing and manipulation
- Work with escape characters and raw strings
"""

# ========================
# STRING BASICS REVIEW
# ========================

text = "python"  

# Basic string operations
print("=== BASIC STRING OPERATIONS ===")
print(f"Original text: '{text}'")
print(f"Uppercase: {text.upper()}")  # Convert to uppercase
print(f"Length: {len(text)} characters")  # P y t h o n

# String testing methods
print(f"Is alphabetic: {text.isalpha()}")  # Check if all characters are alphabetic
print(f"Is digit: {text.isdigit()}")  # Check if all characters are digits
print(f"Is alphanumeric: {text.isalnum()}")  # Check if all characters are alphanumeric
print(f"Is lowercase: {text.islower()}")  # Check if all characters are lowercase

# Case conversion methods
print(f"Lowercase: {text.lower()}")  # Convert to lowercase
print(f"Title case: {text.title()}")  # Convert to title case
print(f"Capitalized: {text.capitalize()}")  # Capitalize the first letter
print(f"Swapcase: {text.swapcase()}")  # Swap case (lower to upper and vice versa)

# ========================
# STRING INDEXING AND SLICING
# ========================

"""
String indexing:
   P  y  t  h  o  n
   0  1  2  3  4  5   (positive indexing)
  -6 -5 -4 -3 -2 -1   (negative indexing)

Slicing syntax: string[start:end:step]
- start: starting index (inclusive)
- end: ending index (exclusive)
- step: step size (default 1)
"""

print("\n=== STRING INDEXING AND SLICING ===")
sample_text = "Python Programming"
print(f"Sample text: '{sample_text}'")

# Basic indexing
print(f"First character: '{sample_text[0]}'")  # Access first character
print(f"Last character: '{sample_text[-1]}'")  # Access last character
print(f"Character at index 7: '{sample_text[7]}'")

# Basic slicing
print(f"Slice [1:4]: '{sample_text[1:4]}'")  # Slice from index 1 to 3 (exclusive)
print(f"Slice [1:]: '{sample_text[1:]}'")  # Slice from index 1 to end
print(f"Slice [:6]: '{sample_text[:6]}'")  # Slice from start to index 5 (exclusive)

# Advanced slicing
print(f"Every 2nd character: '{sample_text[::2]}'")  # Slice with step of 2
print(f"Reversed string: '{sample_text[::-1]}'")  # Reverse the string
print(f"Every 3rd char from index 2: '{sample_text[2::3]}'")

# ========================
# STRING SEARCH AND REPLACE
# ========================

print("\n=== STRING SEARCH AND REPLACE ===")
sentence = "Python is powerful. Python is versatile. Python is fun!"
print(f"Original: '{sentence}'")

# Searching methods
print(f"Count 'Python': {sentence.count('Python')}")  # Count occurrences
print(f"Count 'is': {sentence.count('is')}")
print(f"Find 'powerful': {sentence.find('powerful')}")  # Find index (returns -1 if not found)
print(f"Find 'java': {sentence.find('java')}")  # Returns -1 for not found

# Using index() vs find()
try:
    print(f"Index of 'Python': {sentence.index('Python')}")  # Raises ValueError if not found
    # print(sentence.index('java'))  # This would raise ValueError
except ValueError as e:
    print(f"Error: {e}")

# Replace operations
print(f"Replace 'Python' with 'Java': '{sentence.replace('Python', 'Java')}'")
print(f"Replace first 2 'Python': '{sentence.replace('Python', 'Java', 2)}'")

# ========================
# STRING SPLITTING AND JOINING
# ========================

print("\n=== STRING SPLITTING AND JOINING ===")

# Splitting strings
data = "apple,banana,orange,grape"
fruits = data.split(',')
print(f"CSV data: '{data}'")
print(f"Split by comma: {fruits}")

text_with_spaces = "  Hello   world   from   Python  "
words = text_with_spaces.split()  # Split by whitespace (default)
print(f"Text with spaces: '{text_with_spaces}'")
print(f"Split by whitespace: {words}")

# Advanced splitting
email = "user@example.com"
username, domain = email.split('@')
print(f"Email: {email}")
print(f"Username: {username}, Domain: {domain}")

# Joining strings
print(f"Join with ' | ': '{' | '.join(fruits)}'")
print(f"Join with newlines:\\n{chr(10).join(fruits)}")

# ========================
# STRING CLEANING AND VALIDATION
# ========================

print("\n=== STRING CLEANING AND VALIDATION ===")

messy_text = "   Hello World!   "
print(f"Messy text: '{messy_text}'")
print(f"Stripped: '{messy_text.strip()}'")  # Remove leading/trailing whitespace
print(f"Left strip: '{messy_text.lstrip()}'")  # Remove leading whitespace
print(f"Right strip: '{messy_text.rstrip()}'")  # Remove trailing whitespace

# Custom character removal
custom_text = "xxxHello Worldxxx"
print(f"Strip 'x' characters: '{custom_text.strip('x')}'")

# String validation methods
test_strings = ["Hello123", "12345", "Hello", "hello world", "HELLO", ""]

print("\nString validation tests:")
for s in test_strings:
    print(f"'{s}': alpha={s.isalpha()}, digit={s.isdigit()}, alnum={s.isalnum()}, "
          f"upper={s.isupper()}, lower={s.islower()}, title={s.istitle()}")

# Start/end checking
url = "https://www.python.org"
print(f"URL: {url}")
print(f"Starts with 'https': {url.startswith('https')}")
print(f"Ends with '.org': {url.endswith('.org')}")
print(f"Ends with ('.com', '.org'): {url.endswith(('.com', '.org'))}")

# ========================
# ESCAPE CHARACTERS AND RAW STRINGS
# ========================

print("\n=== ESCAPE CHARACTERS AND RAW STRINGS ===")

# Common escape characters
print("Escape characters:")
print("Tab separated\\tvalues")
print("Line 1\\nLine 2")
print("Quote: \\"Hello\\"")
print("Backslash: \\\\")
print("Unicode heart: \\u2764")

# Raw strings (prefix with r)
file_path = r"C:\\Users\\Documents\\file.txt"
regex_pattern = r"\\d+\\.\\d+"
print(f"Raw string file path: {file_path}")
print(f"Raw regex pattern: {regex_pattern}")

# ========================
# ADVANCED STRING FORMATTING
# ========================

print("\n=== ADVANCED STRING FORMATTING ===")

name = "Alice"
age = 30
salary = 75000.50
pi = 3.14159265359

# f-string formatting (Python 3.6+)
print("=== F-STRING FORMATTING ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Salary: ${salary:,.2f}")  # Comma separator and 2 decimals
print(f"Pi: {pi:.3f}")  # 3 decimal places
print(f"Pi scientific: {pi:.2e}")  # Scientific notation

# Alignment and padding
print(f"Left aligned: '{name:<10}'")
print(f"Right aligned: '{name:>10}'")
print(f"Center aligned: '{name:^10}'")
print(f"Zero padded: '{age:05d}'")

# .format() method
print("\\n=== .FORMAT() METHOD ===")
template = "Hello {}, you are {} years old and earn ${:,.2f}"
print(template.format(name, age, salary))

# Named placeholders
template2 = "Hello {name}, you are {age} years old"
print(template2.format(name=name, age=age))

# ========================
# STRING METHODS FOR TEXT PROCESSING
# ========================

print("\\n=== TEXT PROCESSING METHODS ===")

# Text analysis
text_sample = "The quick brown fox jumps over the lazy dog"
print(f"Sample text: '{text_sample}'")

# Word processing
words = text_sample.split()
print(f"Word count: {len(words)}")
print(f"Character count: {len(text_sample)}")
print(f"Character count (no spaces): {len(text_sample.replace(' ', ''))}")

# Letter frequency
letter_count = {}
for char in text_sample.lower():
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1

print("Letter frequencies:")
for letter in sorted(letter_count.keys()):
    print(f"  {letter}: {letter_count[letter]}")

# ========================
# PRACTICAL EXAMPLES
# ========================

print("\\n=== PRACTICAL EXAMPLE: TEXT PROCESSOR ===")

def text_analyzer(text):
    """Analyze text and return statistics"""
    # Clean the text
    cleaned = text.strip().lower()
    
    # Basic stats
    char_count = len(text)
    char_count_no_spaces = len(text.replace(' ', ''))
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Vocabulary analysis
    words = cleaned.replace('.', '').replace(',', '').replace('!', '').replace('?', '').split()
    unique_words = set(words)
    
    return {
        'character_count': char_count,
        'character_count_no_spaces': char_count_no_spaces,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'unique_words': len(unique_words),
        'vocabulary_ratio': len(unique_words) / len(words) if words else 0
    }

# Test the analyzer
sample_paragraph = """
Python is a high-level programming language. It's known for its simplicity and readability.
Python is used in web development, data science, and artificial intelligence!
"""

stats = text_analyzer(sample_paragraph)
print("Text Analysis Results:")
print("-" * 25)
for key, value in stats.items():
    if isinstance(value, float):
        print(f"{key.replace('_', ' ').title()}: {value:.2f}")
    else:
        print(f"{key.replace('_', ' ').title()}: {value}")

# ========================
# STRING MANIPULATION EXERCISES
# ========================

"""
PRACTICE EXERCISES:

1. Password Validator:
   - At least 8 characters long
   - Contains uppercase and lowercase letters
   - Contains at least one digit
   - Contains at least one special character

2. Text Cleaner:
   - Remove extra whitespace
   - Convert to proper title case
   - Remove special characters except periods and commas

3. Email Validator:
   - Contains exactly one @ symbol
   - Has valid domain extension
   - No spaces or special characters except @ and .

4. Word Counter:
   - Count unique words in a text
   - Find the most common word
   - Calculate average word length
"""

# Example solution for Exercise 1: Password Validator
def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    if not has_lower:
        return False, "Password must contain at least one lowercase letter"
    if not has_digit:
        return False, "Password must contain at least one digit"
    if not has_special:
        return False, "Password must contain at least one special character"
    
    return True, "Password is strong"

# Test password validator
test_passwords = ["weak", "StrongPass1!", "nospecial123", "NOLOWER123!"]
print("\\n=== PASSWORD VALIDATION TESTS ===")
for pwd in test_passwords:
    is_valid, message = validate_password(pwd)
    print(f"'{pwd}': {'✓' if is_valid else '✗'} {message}")

# ========================
# KEY TAKEAWAYS
# ========================

"""
SUMMARY:
1. Strings are immutable - methods return new strings
2. Use appropriate methods for different text operations:
   - Searching: find(), index(), count()
   - Cleaning: strip(), replace()
   - Splitting: split(), rsplit(), partition()
   - Validation: startswith(), endswith(), is*() methods
3. String slicing is powerful for text manipulation
4. f-strings provide the most readable formatting
5. Raw strings (r"") are useful for regex and file paths
6. Consider performance for large text processing tasks
7. Always validate and clean user input

BEST PRACTICES:
- Use f-strings for string formatting in Python 3.6+
- Use raw strings for regex patterns and file paths
- Validate and sanitize user input
- Consider using string methods chaining for complex operations
- Use meaningful variable names for text processing
- Handle edge cases (empty strings, None values)

NEXT: Day 6 - We'll explore operators and expressions in detail!
"""



