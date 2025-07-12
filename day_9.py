""" Day 9: Working with Lists """



# COMPREHENSIVE GUIDE TO PYTHON LISTS

# 1. Creating Lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  #Boolean
empty_list = []
list_from_range = list(range(5))  # [0, 1, 2, 3, 4]

print("Original fruits:", fruits)
print("Mixed data types:", mixed)
print("List from range:", list_from_range)


# 2. Accessing Elements (Indexing)
print("\n--- ACCESSING ELEMENTS ---")
print("First fruit:", fruits[0])         # apple
print("Last fruit:", fruits[-1])         # cherry
print("Second to last:", fruits[-2])     # banana

# 3. Slicing [start:end:step]
print("\n--- SLICING ---")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original numbers:", numbers)
print("Slice [2:6]:", numbers[2:6])      # [2, 3, 4, 5]
print("Every 2nd item:", numbers[::2])   # [0, 2, 4, 6, 8]
print("Reverse list:", numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# 4. Modifying Lists
print("\n--- MODIFYING LISTS ---")
fruits = ["apple", "banana", "cherry"]
print("Original fruits:", fruits)
fruits[1] = "blueberry"  # Change item
print("After modification:", fruits)

# 5. List Methods
print("\n--- LIST METHODS ---")
fruits = ["apple", "banana", "cherry"]
print("Original fruits:", fruits)

# Adding elements
fruits.append("orange")                # Add to end
print("After append:", fruits)
fruits.insert(1, "grape")              # Insert at position
print("After insert:", fruits)
fruits.extend(["kiwi", "mango"])       # Add multiple items
print("After extend:", fruits)

# Removing elements
removed = fruits.pop()                 # Remove and return last item
print("Removed item:", removed)
print("After pop():", fruits)
fruits.remove("grape")                 # Remove first occurrence
print("After remove('grape'):", fruits)
# fruits.clear()                       # Remove all items
# print("After clear():", fruits)

# 6. List Operations
print("\n--- LIST OPERATIONS ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2               # Concatenation
print("Combined:", combined)
repeated = list1 * 3                   # Repetition
print("Repeated:", repeated)

# 7. Useful List Functions
print("\n--- USEFUL LIST FUNCTIONS ---")
numbers = [3, 1, 4, 1, 5, 9, 2]
print("Original numbers:", numbers)
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))      # Returns new sorted list
numbers.sort()                         # Sorts in place
print("After sort():", numbers)
numbers.reverse()                      # Reverses in place
print("After reverse():", numbers)


# use of sorted() function to reverse a list
# Use sorted() to reverse a list
reversed_list = sorted(numbers, reverse=True)


# 8. List Membership
print("\n--- LIST MEMBERSHIP ---")
fruits = ["apple", "banana", "cherry"]
print("Is 'apple' in fruits?", "apple" in fruits)
print("Is 'mango' in fruits?", "mango" in fruits)
print("Index of 'cherry':", fruits.index("cherry"))
print("Count of 'apple':", fruits.count("apple"))

# 9. Nested Lists (Lists of Lists)
print("\n--- NESTED LISTS ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:", matrix)
print("First row:", matrix[0])
print("Element at row 1, col 2:", matrix[1][2])  # 6

# 10. List Comprehensions
print("\n--- LIST COMPREHENSIONS ---")
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)

# PRACTICE EXERCISES
print("\n--- PRACTICE EXERCISES ---")
print("""
1. Create a list of 5 countries you'd like to visit
2. Use slicing to get the first 3 countries
3. Add a new country to the beginning of the list
4. Remove the last country from the list
5. Sort the countries alphabetically
6. Create a list of lists with country-capital pairs
7. Use a list comprehension to create a list of country names in uppercase
""")

# Exercise solutions (try on your own first!)
countries = ["Japan", "Italy", "Australia", "Brazil", "Egypt"]
print("Countries:", countries)
print("First 3 countries:", countries[:3])
countries.insert(0, "Canada")
print("After adding Canada:", countries)
removed_country = countries.pop()
print("Removed:", removed_country)
print("After removing last country:", countries)
countries.sort()
print("Sorted countries:", countries)

country_capitals = [
    ["Japan", "Tokyo"],
    ["Italy", "Rome"],
    ["Australia", "Canberra"]
]
print("Country-capital pairs:", country_capitals)

uppercase_countries = [country.upper() for country in countries]
print("Uppercase countries:", uppercase_countries)

# CHALLENGE: Create a function that finds all common elements between two lists
def common_elements(list1, list2):
    """Find all elements that appear in both lists"""
    return [item for item in list1 if item in list2]

fruits1 = ["apple", "banana", "cherry", "orange"]
fruits2 = ["banana", "kiwi", "orange", "pear"]
print("\nCommon fruits:", common_elements(fruits1, fruits2))  # ['banana', 'orange']


