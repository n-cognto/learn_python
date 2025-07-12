""" Day 13: Tuples and Sets """

"""
TUPLES:
- Ordered, immutable collections
- Allow duplicate values
- Use parentheses () or just comma separation
- Useful for data that shouldn't change

SETS:
- Unordered, mutable collections
- No duplicate values allowed
- Use curly braces {} or set() function
- Useful for removing duplicates and set operations
"""

# ===== TUPLES =====
print("=== TUPLES ===")

# Creating tuples
my_tuple = (1, 1, 3, 2, 5, 4, 2, 3)
coordinates = (10.5, 20.3)
single_item_tuple = (42,)  # Note the comma for single item
empty_tuple = ()

print(f"Original tuple: {my_tuple}")
print(f"Coordinates: {coordinates}")
print(f"Single item tuple: {single_item_tuple}")

# Tuple operations
print(f"Length: {len(my_tuple)}")
print(f"Count of 1: {my_tuple.count(1)}")
print(f"Index of 3: {my_tuple.index(3)}")
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Slice [1:4]: {my_tuple[1:4]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked coordinates: x={x}, y={y}")

# Multiple assignment with tuples
name, age, city = ("Alice", 30, "New York")
print(f"Name: {name}, Age: {age}, City: {city}")

# ===== SETS =====
print("\n=== SETS ===")

# Creating sets
cleaned_my_tuple = set(my_tuple)  # Remove duplicates from tuple
my_set = {1, 2, 2, 3}  # Duplicates automatically removed
colors_set = {"red", "green", "blue", "red"}

print(f"Set from tuple (duplicates removed): {cleaned_my_tuple}")
print(f"Set with duplicates: {my_set}")
print(f"Colors set: {colors_set}")

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (A | B): {set_a | set_b}")
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")
print(f"Symmetric difference (A ^ B): {set_a ^ set_b}")

# Set methods
fruits = {"apple", "banana", "cherry"}
print(f"Original fruits: {fruits}")

fruits.add("orange")
print(f"After adding orange: {fruits}")

fruits.update(["mango", "grape"])
print(f"After updating with list: {fruits}")

fruits.discard("banana")  # Won't raise error if not found
print(f"After discarding banana: {fruits}")

# Practical example: Finding common elements
student_a_subjects = {"math", "physics", "chemistry", "biology"}
student_b_subjects = {"math", "chemistry", "english", "history"}

common_subjects = student_a_subjects & student_b_subjects
unique_to_a = student_a_subjects - student_b_subjects
all_subjects = student_a_subjects | student_b_subjects

print(f"\nStudent A subjects: {student_a_subjects}")
print(f"Student B subjects: {student_b_subjects}")
print(f"Common subjects: {common_subjects}")
print(f"Unique to A: {unique_to_a}")
print(f"All subjects: {all_subjects}")

# Converting between data types
numbers_list = [1, 2, 3, 2, 1, 4, 5, 4]
unique_numbers = list(set(numbers_list))  # Remove duplicates and convert back
print(f"Original list: {numbers_list}")
print(f"Unique numbers: {unique_numbers}")

# ========== EXERCISES AND CHALLENGES ==========
print("\n" + "="*50)
print("EXERCISES AND CHALLENGES")
print("="*50)

print("\n=== EXERCISE 1: Basic Tuple Operations ===")

# 1. Create tuples for RGB color values
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = (red, green, blue)

print(f"1. Color tuples: {colors}")

# 2. Unpack color values
r, g, b = red
print(f"2. Red color - R: {r}, G: {g}, B: {b}")

# 3. Find tuple with maximum sum (brightest color)
brightest = max(colors, key=sum)
print(f"3. Brightest color: {brightest} (sum: {sum(brightest)})")

print("\n=== EXERCISE 2: Set Operations ===")

# Programming languages known by developers
dev1_languages = {"Python", "JavaScript", "Java", "C++"}
dev2_languages = {"Python", "C#", "JavaScript", "Go"}
dev3_languages = {"Java", "C++", "Rust", "Python"}

# 1. Find common languages
common_languages = dev1_languages & dev2_languages & dev3_languages
print(f"1. Languages known by all: {common_languages}")

# 2. Find all unique languages
all_languages = dev1_languages | dev2_languages | dev3_languages
print(f"2. All unique languages: {all_languages}")

# 3. Languages unique to dev1
unique_to_dev1 = dev1_languages - dev2_languages - dev3_languages
print(f"3. Unique to dev1: {unique_to_dev1}")

print("\n=== CHALLENGE 1: Data Analysis ===")

# Student data with subjects
student_data = [
    ("Alice", 20, {"Math", "Physics", "Chemistry"}),
    ("Bob", 19, {"Biology", "Chemistry", "English"}),
    ("Charlie", 21, {"Math", "Computer Science", "Physics"}),
    ("Diana", 20, {"English", "History", "Art"})
]

# 1. Find students taking Math
math_students = [name for name, age, subjects in student_data if "Math" in subjects]
print(f"1. Math students: {math_students}")

# 2. All unique subjects
all_subjects = set()
for _, _, subjects in student_data:
    all_subjects |= subjects
print(f"2. All subjects offered: {all_subjects}")

# 3. Subject popularity
subject_counts = {}
for _, _, subjects in student_data:
    for subject in subjects:
        subject_counts[subject] = subject_counts.get(subject, 0) + 1

print("3. Subject enrollment:")
for subject, count in sorted(subject_counts.items()):
    print(f"   {subject}: {count} students")

print("\n=== CHALLENGE 2: Social Network ===")

# Friend relationships
friendships = {
    "Alice": {"Bob", "Charlie", "Diana"},
    "Bob": {"Alice", "Charlie"},
    "Charlie": {"Alice", "Bob", "Eve"},
    "Diana": {"Alice"},
    "Eve": {"Charlie"}
}

# 1. Find mutual friends
def find_mutual_friends(person1, person2):
    return friendships.get(person1, set()) & friendships.get(person2, set())

mutual_alice_bob = find_mutual_friends("Alice", "Bob")
print(f"1. Mutual friends of Alice and Bob: {mutual_alice_bob}")

# 2. Friend suggestions (friends of friends)
def suggest_friends(person):
    direct_friends = friendships.get(person, set())
    friends_of_friends = set()
    
    for friend in direct_friends:
        friends_of_friends |= friendships.get(friend, set())
    
    return friends_of_friends - direct_friends - {person}

alice_suggestions = suggest_friends("Alice")
print(f"2. Friend suggestions for Alice: {alice_suggestions}")

print("\n" + "="*50)
print("END OF EXERCISES - Try creating your own!")
print("="*50)



