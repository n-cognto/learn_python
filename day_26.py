""" Day 26: Working with External Libraries (math, random, datetime, os) """

import math
import random
import datetime
import os
import statistics
from collections import Counter

# =============================================================================
# MATH MODULE - Mathematical Functions
# =============================================================================

def demonstrate_math_module():
    """Demonstrate various functions from the math module"""
    print("=== MATH MODULE DEMONSTRATIONS ===")
    
    # Basic mathematical operations
    numbers = [16, 25, 100, 144]
    print("Square roots:")
    for num in numbers:
        print(f"√{num} = {math.sqrt(num)}")
    
    # Power functions
    print(f"\nPower functions:")
    print(f"2^8 = {math.pow(2, 8)}")
    print(f"e^2 = {math.exp(2):.4f}")
    print(f"log(100) = {math.log10(100)}")
    print(f"ln(e) = {math.log(math.e):.4f}")
    
    # Trigonometric functions (angles in radians)
    angles_degrees = [0, 30, 45, 60, 90]
    print(f"\nTrigonometric functions:")
    for angle in angles_degrees:
        radians = math.radians(angle)
        print(f"{angle}°: sin={math.sin(radians):.4f}, cos={math.cos(radians):.4f}, tan={math.tan(radians):.4f}")
    
    # Rounding functions
    values = [3.2, 3.7, -2.3, -2.8]
    print(f"\nRounding functions:")
    for val in values:
        print(f"{val}: ceil={math.ceil(val)}, floor={math.floor(val)}")
    
    # Constants
    print(f"\nMath constants:")
    print(f"π (pi) = {math.pi:.6f}")
    print(f"e = {math.e:.6f}")
    print(f"τ (tau) = {math.tau:.6f}")


# =============================================================================
# RANDOM MODULE - Random Number Generation
# =============================================================================

def demonstrate_random_module():
    """Demonstrate various functions from the random module"""
    print("\n=== RANDOM MODULE DEMONSTRATIONS ===")
    
    # Basic random numbers
    print("Random integers:")
    for i in range(5):
        print(f"Random int (1-10): {random.randint(1, 10)}")
    
    print(f"\nRandom floats:")
    for i in range(3):
        print(f"Random float (0-1): {random.random():.4f}")
        print(f"Random float (1-100): {random.uniform(1, 100):.2f}")
    
    # Random choices from sequences
    colors = ['red', 'blue', 'green', 'yellow', 'purple']
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    print(f"\nRandom choices:")
    print(f"Random color: {random.choice(colors)}")
    print(f"Random fruit: {random.choice(fruits)}")
    
    # Multiple random choices
    print(f"3 random colors (with replacement): {random.choices(colors, k=3)}")
    print(f"3 random fruits (without replacement): {random.sample(fruits, 3)}")
    
    # Shuffle a list
    deck = ['A', 'K', 'Q', 'J', '10', '9', '8', '7']
    print(f"\nOriginal deck: {deck}")
    random.shuffle(deck)
    print(f"Shuffled deck: {deck}")
    
    # Random with weights
    weighted_choices = ['common', 'uncommon', 'rare', 'legendary']
    weights = [50, 30, 15, 5]  # Probability weights
    print(f"\nWeighted random choices:")
    for i in range(5):
        choice = random.choices(weighted_choices, weights=weights, k=1)[0]
        print(f"Random item: {choice}")


# =============================================================================
# DATETIME MODULE - Date and Time Operations
# =============================================================================

def demonstrate_datetime_module():
    """Demonstrate various functions from the datetime module"""
    print("\n=== DATETIME MODULE DEMONSTRATIONS ===")
    
    # Current date and time
    now = datetime.datetime.now()
    today = datetime.date.today()
    current_time = datetime.time(now.hour, now.minute, now.second)
    
    print(f"Current datetime: {now}")
    print(f"Today's date: {today}")
    print(f"Current time: {current_time}")
    
    # Formatting dates
    print(f"\nFormatted dates:")
    print(f"ISO format: {now.isoformat()}")
    print(f"Readable format: {now.strftime('%B %d, %Y at %I:%M %p')}")
    print(f"Custom format: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Date arithmetic
    print(f"\nDate arithmetic:")
    tomorrow = today + datetime.timedelta(days=1)
    last_week = today - datetime.timedelta(weeks=1)
    next_month = today + datetime.timedelta(days=30)
    
    print(f"Tomorrow: {tomorrow}")
    print(f"Last week: {last_week}")
    print(f"Next month (approx): {next_month}")
    
    # Age calculator
    def calculate_age(birth_date):
        """Calculate age from birth date"""
        age = today - birth_date
        return age.days // 365
    
    birthday = datetime.date(1990, 5, 15)
    age = calculate_age(birthday)
    print(f"\nIf born on {birthday}, current age: {age} years")
    
    # Specific dates
    new_year = datetime.date(2026, 1, 1)
    days_until_new_year = (new_year - today).days
    print(f"Days until New Year 2026: {days_until_new_year}")


# =============================================================================
# OS MODULE - Operating System Interface
# =============================================================================

def demonstrate_os_module():
    """Demonstrate various functions from the os module"""
    print("\n=== OS MODULE DEMONSTRATIONS ===")
    
    # Current working directory
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")
    
    # Environment variables
    print(f"\nSome environment variables:")
    env_vars = ['HOME', 'USER', 'PATH']
    for var in env_vars:
        value = os.environ.get(var, 'Not found')
        if len(str(value)) > 50:  # Truncate long paths
            value = str(value)[:50] + "..."
        print(f"{var}: {value}")
    
    # Path operations
    file_path = "/home/user/documents/example.txt"
    print(f"\nPath operations for: {file_path}")
    print(f"Directory: {os.path.dirname(file_path)}")
    print(f"Filename: {os.path.basename(file_path)}")
    print(f"File extension: {os.path.splitext(file_path)[1]}")
    
    # Join paths (cross-platform)
    joined_path = os.path.join("folder", "subfolder", "file.txt")
    print(f"Joined path: {joined_path}")
    
    # List directory contents (current directory)
    print(f"\nFiles in current directory:")
    try:
        files = os.listdir('.')
        for i, file in enumerate(files[:10], 1):  # Show first 10 files
            print(f"{i}. {file}")
        if len(files) > 10:
            print(f"... and {len(files) - 10} more files")
    except PermissionError:
        print("Permission denied to list directory")


# =============================================================================
# STATISTICS MODULE - Statistical Functions
# =============================================================================

def demonstrate_statistics_module():
    """Demonstrate functions from the statistics module"""
    print("\n=== STATISTICS MODULE DEMONSTRATIONS ===")
    
    # Sample data
    test_scores = [85, 92, 78, 96, 88, 76, 94, 82, 90, 87]
    temperatures = [22.5, 24.1, 23.8, 25.2, 21.9, 26.0, 24.5, 23.1, 25.8, 22.7]
    
    print(f"Test scores: {test_scores}")
    print(f"Temperatures (°C): {temperatures}")
    
    # Central tendency
    print(f"\nCentral tendency measures:")
    print(f"Mean score: {statistics.mean(test_scores):.2f}")
    print(f"Median score: {statistics.median(test_scores)}")
    print(f"Mode score: {statistics.mode(test_scores) if len(set(test_scores)) < len(test_scores) else 'No mode'}")
    
    # Spread measures
    print(f"\nSpread measures:")
    print(f"Standard deviation: {statistics.stdev(test_scores):.2f}")
    print(f"Variance: {statistics.variance(test_scores):.2f}")
    
    # Temperature statistics
    print(f"\nTemperature statistics:")
    print(f"Average temperature: {statistics.mean(temperatures):.1f}°C")
    print(f"Temperature range: {min(temperatures):.1f}°C - {max(temperatures):.1f}°C")


# =============================================================================
# COLLECTIONS MODULE - Counter
# =============================================================================

def demonstrate_collections_module():
    """Demonstrate Counter from collections module"""
    print("\n=== COLLECTIONS MODULE - Counter ===")
    
    # Count characters in text
    text = "hello world python programming"
    char_count = Counter(text)
    print(f"Character frequency in '{text}':")
    for char, count in char_count.most_common(10):
        if char != ' ':  # Skip spaces
            print(f"'{char}': {count}")
    
    # Count words
    words = text.split()
    word_count = Counter(words)
    print(f"\nWord frequency:")
    for word, count in word_count.most_common():
        print(f"'{word}': {count}")
    
    # Count random numbers
    random_numbers = [random.randint(1, 6) for _ in range(50)]
    number_count = Counter(random_numbers)
    print(f"\nDice roll simulation (50 rolls):")
    for number in sorted(number_count.keys()):
        print(f"{number}: {'■' * number_count[number]} ({number_count[number]})")


# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def password_generator(length=12, include_symbols=True):
    """Generate a secure random password"""
    import string
    
    chars = string.ascii_letters + string.digits
    if include_symbols:
        chars += "!@#$%^&*"
    
    password = ''.join(random.choices(chars, k=length))
    return password


def dice_rolling_game():
    """Simple dice rolling game"""
    print("\n=== DICE ROLLING GAME ===")
    
    total_score = 0
    rolls = 0
    
    while True:
        input("\nPress Enter to roll the dice (or Ctrl+C to quit)...")
        try:
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            roll_total = die1 + die2
            rolls += 1
            total_score += roll_total
            
            print(f"🎲 Roll {rolls}: [{die1}] [{die2}] = {roll_total}")
            print(f"Total score: {total_score} | Average: {total_score/rolls:.2f}")
            
            if roll_total == 12:
                print("🎉 Double sixes! Lucky roll!")
            elif roll_total == 2:
                print("😅 Snake eyes! Better luck next time!")
                
        except KeyboardInterrupt:
            print(f"\n\nGame over! Final stats:")
            print(f"Total rolls: {rolls}")
            print(f"Total score: {total_score}")
            if rolls > 0:
                print(f"Average roll: {total_score/rolls:.2f}")
            break


# =============================================================================
# DEMONSTRATION
# =============================================================================

def main():
    """Run all demonstrations"""
    demonstrate_math_module()
    demonstrate_random_module()
    demonstrate_datetime_module()
    demonstrate_os_module()
    demonstrate_statistics_module()
    demonstrate_collections_module()
    
    # Practical examples
    print("\n=== PRACTICAL APPLICATIONS ===")
    print(f"Generated password: {password_generator()}")
    print(f"Generated password (no symbols): {password_generator(8, False)}")
    
    # Uncomment the line below to play the dice game
    # dice_rolling_game()


# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================

def print_concepts():
    """Print key concepts about external libraries"""
    print("\n=== KEY CONCEPTS LEARNED ===")
    print("1. import: Load external modules into your program")
    print("2. math: Mathematical functions and constants")
    print("3. random: Generate random numbers and make random choices")
    print("4. datetime: Work with dates, times, and time calculations")
    print("5. os: Interface with the operating system")
    print("6. statistics: Statistical calculations (mean, median, etc.)")
    print("7. collections: Specialized data structures like Counter")
    print("8. Standard Library: Built-in modules that come with Python")


# Run the demonstration
if __name__ == "__main__":
    main()
    print_concepts()
