""" Day 14: Dictionaries (Key-Value Pairs) """

"""
Dictionaries are mutable collections of key-value pairs.
- Keys must be immutable (strings, numbers, tuples)
- Values can be any data type
- Use curly braces {} with key: value pairs
- Very efficient for lookups by key
"""

# ===== CREATING DICTIONARIES =====
print("=== CREATING DICTIONARIES ===")

person = {
    "name": "Alice", 
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"]
}

# Alternative ways to create dictionaries
empty_dict = {}
dict_from_constructor = dict(name="Bob", age=25)
dict_from_tuples = dict([("x", 1), ("y", 2)])

print(f"Person: {person}")
print(f"From constructor: {dict_from_constructor}")
print(f"From tuples: {dict_from_tuples}")

# ===== ACCESSING VALUES =====
print("\n=== ACCESSING VALUES ===")

print(f"Name: {person['name']}")
print(f"Age using get(): {person.get('age')}")
print(f"Country (with default): {person.get('country', 'Unknown')}")

# Safe access with get() vs direct access
# person["country"]  # This would raise KeyError
print(f"Safe access: {person.get('country', 'Not specified')}")

# ===== MODIFYING DICTIONARIES =====
print("\n=== MODIFYING DICTIONARIES ===")

# Adding/updating values
person["country"] = "USA"
person["age"] = 31  # Update existing key
person.update({"email": "alice@email.com", "phone": "123-456-7890"})

print(f"After updates: {person}")

# Removing items
removed_phone = person.pop("phone")
print(f"Removed phone: {removed_phone}")
print(f"After removing phone: {person}")

# ===== DICTIONARY METHODS =====
print("\n=== DICTIONARY METHODS ===")

print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Check if key exists
print(f"Has 'name': {'name' in person}")
print(f"Has 'salary': {'salary' in person}")

# ===== ITERATING THROUGH DICTIONARIES =====
print("\n=== ITERATING THROUGH DICTIONARIES ===")

# Iterate through key-value pairs
print("Key-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Iterate through keys only
print("\nKeys only:")
for key in person:  # Same as person.keys()
    print(f"  {key}")

# Iterate through values only
print("\nValues only:")
for value in person.values():
    print(f"  {value}")

# ===== NESTED DICTIONARIES =====
print("\n=== NESTED DICTIONARIES ===")

company = {
    "employees": {
        "alice": {"age": 30, "department": "Engineering"},
        "bob": {"age": 25, "department": "Marketing"},
        "charlie": {"age": 35, "department": "Sales"}
    },
    "departments": ["Engineering", "Marketing", "Sales", "HR"]
}

print(f"Alice's department: {company['employees']['alice']['department']}")
print(f"All departments: {company['departments']}")

# ===== DICTIONARY COMPREHENSIONS =====
print("\n=== DICTIONARY COMPREHENSIONS ===")

# Create a dictionary of squares
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares_dict}")

# Filter dictionary based on condition
high_performers = {name: info for name, info in company["employees"].items() 
                  if info["age"] >= 30}
print(f"Employees 30+: {high_performers}")

# Transform values
upper_departments = {name: info["department"].upper() 
                    for name, info in company["employees"].items()}
print(f"Uppercase departments: {upper_departments}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===")

# Word frequency counter
text = "hello world hello python world"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word frequency: {word_count}")

# Using dictionary as a lookup table
grade_scale = {
    90: "A", 85: "B+", 80: "B", 75: "C+", 
    70: "C", 65: "D+", 60: "D", 0: "F"
}

def get_letter_grade(score):
    for min_score in sorted(grade_scale.keys(), reverse=True):
        if score >= min_score:
            return grade_scale[min_score]
    return "F"

test_scores = [95, 87, 73, 68, 55]
for score in test_scores:
    print(f"Score {score}: Grade {get_letter_grade(score)}")

# Grouping data
students = [
    {"name": "Alice", "grade": "A", "subject": "Math"},
    {"name": "Bob", "grade": "B", "subject": "Math"},
    {"name": "Charlie", "grade": "A", "subject": "Science"},
    {"name": "Alice", "grade": "B+", "subject": "Science"}
]

# Group by subject
subjects_dict = {}
for student in students:
    subject = student["subject"]
    if subject not in subjects_dict:
        subjects_dict[subject] = []
    subjects_dict[subject].append(student)

print(f"\nGrouped by subject: {subjects_dict}")

# ========== EXERCISES AND CHALLENGES ==========
print("\n" + "="*50)
print("EXERCISES AND CHALLENGES")
print("="*50)

print("\n=== EXERCISE 1: Basic Dictionary Operations ===")

# Student grade management system
student_grades = {
    "Alice": [85, 92, 78, 96],
    "Bob": [76, 88, 82, 90],
    "Charlie": [92, 95, 89, 93],
    "Diana": [68, 75, 72, 80]
}

# 1. Calculate average grades
print("1. Student averages:")
for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    print(f"   {student}: {average:.1f}")

# 2. Find highest and lowest performing students
averages = {student: sum(grades)/len(grades) for student, grades in student_grades.items()}
top_student = max(averages, key=averages.get)
lowest_student = min(averages, key=averages.get)
print(f"2. Top performer: {top_student} ({averages[top_student]:.1f})")
print(f"2. Needs improvement: {lowest_student} ({averages[lowest_student]:.1f})")

# 3. Add new student and update existing grades
student_grades["Eve"] = [88, 91, 85, 89]
student_grades["Alice"].append(89)  # Alice took a makeup exam
print(f"3. Updated Alice's grades: {student_grades['Alice']}")
print(f"3. New student Eve added: {student_grades['Eve']}")

print("\n=== EXERCISE 2: Inventory Management ===")

# Store inventory with nested dictionaries
inventory = {
    "electronics": {
        "laptop": {"price": 999, "stock": 5, "brand": "Dell"},
        "mouse": {"price": 25, "stock": 20, "brand": "Logitech"},
        "keyboard": {"price": 75, "stock": 15, "brand": "Corsair"}
    },
    "books": {
        "python_guide": {"price": 45, "stock": 10, "author": "John Doe"},
        "data_science": {"price": 60, "stock": 7, "author": "Jane Smith"},
        "algorithms": {"price": 55, "stock": 3, "author": "Bob Johnson"}
    }
}

# 1. Calculate total inventory value
total_value = 0
for category, items in inventory.items():
    category_value = sum(item["price"] * item["stock"] for item in items.values())
    print(f"1. {category.capitalize()} total value: ${category_value}")
    total_value += category_value
print(f"1. Total inventory value: ${total_value}")

# 2. Find items with low stock (< 5)
print("2. Low stock items:")
for category, items in inventory.items():
    for item_name, details in items.items():
        if details["stock"] < 5:
            print(f"   {category}/{item_name}: {details['stock']} units")

# 3. Update inventory after sales
sales = {
    ("electronics", "laptop"): 2,
    ("books", "python_guide"): 3,
    ("electronics", "mouse"): 5
}

for (category, item), quantity_sold in sales.items():
    if item in inventory[category]:
        inventory[category][item]["stock"] -= quantity_sold
        print(f"3. Sold {quantity_sold} {item}(s), remaining: {inventory[category][item]['stock']}")

print("\n=== EXERCISE 3: Text Analysis ===")

# Analyze word frequency in text
text = """
Python is a powerful programming language. It is widely used for web development,
data analysis, artificial intelligence, and scientific computing. Python's syntax
is clean and readable, making it an excellent choice for beginners and experts alike.
Python has a vast ecosystem of libraries and frameworks.
"""

# 1. Word frequency counter
words = text.lower().replace('\n', ' ').replace(',', '').replace('.', '').split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("1. Word frequency (words appearing more than once):")
frequent_words = {word: count for word, count in word_freq.items() if count > 1}
for word, count in sorted(frequent_words.items(), key=lambda x: x[1], reverse=True):
    print(f"   {word}: {count}")

# 2. Character frequency
char_freq = {}
for char in text.lower():
    if char.isalpha():
        char_freq[char] = char_freq.get(char, 0) + 1

most_common_char = max(char_freq, key=char_freq.get)
print(f"2. Most common letter: '{most_common_char}' appears {char_freq[most_common_char]} times")

# 3. Word length distribution
length_dist = {}
for word in words:
    length = len(word)
    length_dist[length] = length_dist.get(length, 0) + 1

print("3. Word length distribution:")
for length in sorted(length_dist.keys()):
    print(f"   {length} letters: {length_dist[length]} words")

print("\n=== CHALLENGE 1: Customer Database ===")

# Customer relationship management system
customers = {
    "C001": {
        "name": "Alice Johnson",
        "email": "alice@email.com",
        "phone": "555-0123",
        "orders": [
            {"id": "O001", "date": "2024-01-15", "total": 150.00, "items": ["laptop_case", "mouse"]},
            {"id": "O002", "date": "2024-02-20", "total": 75.50, "items": ["keyboard"]}
        ],
        "loyalty_points": 450
    },
    "C002": {
        "name": "Bob Smith",
        "email": "bob@email.com",
        "phone": "555-0456",
        "orders": [
            {"id": "O003", "date": "2024-01-28", "total": 299.99, "items": ["monitor"]},
            {"id": "O004", "date": "2024-03-10", "total": 45.00, "items": ["cables", "adapter"]}
        ],
        "loyalty_points": 690
    },
    "C003": {
        "name": "Charlie Brown",
        "email": "charlie@email.com",
        "phone": "555-0789",
        "orders": [
            {"id": "O005", "date": "2024-02-05", "total": 125.75, "items": ["speakers", "headphones"]}
        ],
        "loyalty_points": 251
    }
}

# 1. Calculate total revenue and average order value
total_revenue = 0
total_orders = 0
for customer_id, customer in customers.items():
    customer_total = sum(order["total"] for order in customer["orders"])
    total_revenue += customer_total
    total_orders += len(customer["orders"])
    print(f"1. {customer['name']}: ${customer_total:.2f} ({len(customer['orders'])} orders)")

average_order_value = total_revenue / total_orders if total_orders > 0 else 0
print(f"1. Total revenue: ${total_revenue:.2f}")
print(f"1. Average order value: ${average_order_value:.2f}")

# 2. Find VIP customers (loyalty points > 500)
vip_customers = {cid: customer for cid, customer in customers.items() 
                if customer["loyalty_points"] > 500}
print("2. VIP Customers:")
for cid, customer in vip_customers.items():
    print(f"   {customer['name']}: {customer['loyalty_points']} points")

# 3. Most popular items
item_popularity = {}
for customer in customers.values():
    for order in customer["orders"]:
        for item in order["items"]:
            item_popularity[item] = item_popularity.get(item, 0) + 1

print("3. Most popular items:")
sorted_items = sorted(item_popularity.items(), key=lambda x: x[1], reverse=True)
for item, count in sorted_items[:3]:
    print(f"   {item}: ordered {count} times")

# 4. Customer contact directory
print("4. Customer contact directory:")
contact_dir = {customer["name"]: {"email": customer["email"], "phone": customer["phone"]} 
              for customer in customers.values()}
for name, contact in contact_dir.items():
    print(f"   {name}: {contact['email']}, {contact['phone']}")

print("\n=== CHALLENGE 2: Grade Book System ===")

# Comprehensive gradebook with multiple subjects
gradebook = {
    "Math": {
        "Alice": {"assignments": [85, 90, 78], "midterm": 88, "final": 92},
        "Bob": {"assignments": [76, 82, 85], "midterm": 80, "final": 85},
        "Charlie": {"assignments": [92, 95, 89], "midterm": 94, "final": 96}
    },
    "Science": {
        "Alice": {"assignments": [92, 88, 95], "midterm": 90, "final": 94},
        "Bob": {"assignments": [78, 85, 80], "midterm": 82, "final": 79},
        "Diana": {"assignments": [89, 92, 87], "midterm": 91, "final": 88}
    },
    "English": {
        "Bob": {"assignments": [88, 90, 85], "midterm": 87, "final": 89},
        "Charlie": {"assignments": [85, 88, 92], "midterm": 89, "final": 91},
        "Diana": {"assignments": [90, 87, 94], "midterm": 92, "final": 95}
    }
}

# 1. Calculate final grades (assignments 40%, midterm 30%, final 30%)
def calculate_final_grade(grades):
    avg_assignments = sum(grades["assignments"]) / len(grades["assignments"])
    return (avg_assignments * 0.4) + (grades["midterm"] * 0.3) + (grades["final"] * 0.3)

print("1. Final grades by subject:")
final_grades = {}
for subject, students in gradebook.items():
    print(f"   {subject}:")
    final_grades[subject] = {}
    for student, grades in students.items():
        final_grade = calculate_final_grade(grades)
        final_grades[subject][student] = final_grade
        print(f"     {student}: {final_grade:.1f}")

# 2. Calculate GPA for each student
def letter_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

grade_points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

print("2. Student GPAs:")
all_students = set()
for subject_grades in final_grades.values():
    all_students.update(subject_grades.keys())

for student in sorted(all_students):
    total_points = 0
    total_subjects = 0
    for subject, student_grades in final_grades.items():
        if student in student_grades:
            letter = letter_grade(student_grades[student])
            total_points += grade_points[letter]
            total_subjects += 1
    
    gpa = total_points / total_subjects if total_subjects > 0 else 0
    print(f"   {student}: GPA {gpa:.2f}")

# 3. Subject averages
print("3. Subject averages:")
for subject, student_grades in final_grades.items():
    subject_avg = sum(student_grades.values()) / len(student_grades)
    print(f"   {subject}: {subject_avg:.1f}")

print("\n=== CHALLENGE 3: Configuration Manager ===")

# Application configuration with nested settings
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db",
        "credentials": {
            "username": "admin",
            "password": "secret123"
        },
        "pool_size": 10,
        "timeout": 30
    },
    "api": {
        "base_url": "https://api.myapp.com",
        "version": "v1",
        "rate_limit": 1000,
        "endpoints": {
            "users": "/users",
            "orders": "/orders",
            "products": "/products"
        }
    },
    "logging": {
        "level": "INFO",
        "file": "app.log",
        "max_size": "10MB",
        "backup_count": 5
    }
}

# 1. Flatten configuration for environment variables
def flatten_dict(d, prefix=""):
    flattened = {}
    for key, value in d.items():
        new_key = f"{prefix}_{key}".upper() if prefix else key.upper()
        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key))
        else:
            flattened[new_key] = value
    return flattened

flat_config = flatten_dict(config)
print("1. Flattened configuration (first 10 items):")
for i, (key, value) in enumerate(flat_config.items()):
    if i < 10:
        print(f"   {key}={value}")

# 2. Update configuration values
print("2. Updating configuration...")
config["database"]["port"] = 5433
config["api"]["rate_limit"] = 1500
config["logging"]["level"] = "DEBUG"

# Add new endpoint
config["api"]["endpoints"]["analytics"] = "/analytics"

print("   Updated database port:", config["database"]["port"])
print("   Updated rate limit:", config["api"]["rate_limit"])
print("   Updated logging level:", config["logging"]["level"])
print("   Added new endpoint:", config["api"]["endpoints"]["analytics"])

# 3. Configuration validation
def validate_config(config):
    errors = []
    
    # Check required fields
    if config["database"]["port"] <= 0:
        errors.append("Database port must be positive")
    
    if config["api"]["rate_limit"] <= 0:
        errors.append("API rate limit must be positive")
    
    if config["logging"]["level"] not in ["DEBUG", "INFO", "WARNING", "ERROR"]:
        errors.append("Invalid logging level")
    
    return errors

validation_errors = validate_config(config)
if validation_errors:
    print("3. Configuration errors:")
    for error in validation_errors:
        print(f"   - {error}")
else:
    print("3. Configuration is valid!")

print("\n" + "="*50)
print("END OF EXERCISES - Try creating your own!")
print("="*50)

