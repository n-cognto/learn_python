# Python Data Structures Complete Guide

## 1. LISTS - Ordered, Mutable Collections

**Lists are the most versatile data structure in Python**

- **Ordered**: Items maintain their position
- **Mutable**: Can be changed after creation
- **Allow duplicates**
- **Can store different data types**

### Creating Lists

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty_list = []
list_from_range = list(range(5))  # [0, 1, 2, 3, 4]

print("Original fruits:", fruits)
```

### Accessing Elements (Indexing)

```python
print("First fruit:", fruits[0])        # apple
print("Last fruit:", fruits[-1])        # cherry
print("Second to last:", fruits[-2])    # banana
```

### Slicing [start:end:step]

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Slice [2:6]:", numbers[2:6])     # [2, 3, 4, 5]
print("Every 2nd item:", numbers[::2])  # [0, 2, 4, 6, 8]
print("Reverse list:", numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### Modifying Lists

```python
fruits[1] = "blueberry"  # Change item
print("After modification:", fruits)
```

### List Methods

```python
fruits.append("orange")           # Add to end
fruits.insert(1, "grape")        # Insert at position
fruits.extend(["kiwi", "mango"])  # Add multiple items
print("After additions:", fruits)

removed = fruits.pop()            # Remove and return last item
fruits.remove("grape")            # Remove first occurrence
print("After removals:", fruits)
print("Removed item:", removed)
```

### List Operations

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2         # Concatenation
repeated = list1 * 3             # Repetition
print("Combined:", combined)
print("Repeated:", repeated)
```

### Useful List Functions

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))
numbers.sort()  # Sorts in place
print("After sort():", numbers)
```

### List Membership

```python
print("Is 5 in numbers?", 5 in numbers)
print("Index of 4:", numbers.index(4))
print("Count of 1:", numbers.count(1))
```

---

## 2. TUPLES - Ordered, Immutable Collections

**Tuples are like lists but cannot be changed after creation**

- **Ordered**: Items maintain their position
- **Immutable**: Cannot be changed after creation
- **Allow duplicates**
- **Faster than lists for read operations**
- **Used for data that shouldn't change**

### Creating Tuples

```python
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Comma needed for single item
empty_tuple = ()
mixed_tuple = (1, "hello", 3.14, True)

print("Coordinates:", coordinates)
print("Colors:", colors)
```

### Accessing Elements (same as lists)

```python
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])
print("First color:", colors[0])
```

### Tuple Unpacking

```python
x, y = coordinates
print(f"x = {x}, y = {y}")

# Multiple assignment
name, age, city = ("Alice", 25, "New York")
print(f"Name: {name}, Age: {age}, City: {city}")
```

### Tuple Methods (only 2!)

```python
numbers_tuple = (1, 2, 3, 2, 2, 4)
print("Count of 2:", numbers_tuple.count(2))
print("Index of 3:", numbers_tuple.index(3))
```

### When to use tuples

```python
def get_name_age():
    return "Bob", 30  # Returns a tuple

name, age = get_name_age()
print(f"Function returned: {name}, {age}")

# Tuples as dictionary keys (because they're immutable)
locations = {
    (0, 0): "origin",
    (1, 1): "northeast",
    (-1, -1): "southwest"
}
print("Location at (1,1):", locations[(1, 1)])
```

---

## 3. DICTIONARIES - Key-Value Pairs

**Dictionaries store data as key-value pairs** *(Python 3.7+ maintains insertion order)*

- **Keys must be unique and immutable** (strings, numbers, tuples)
- **Values can be any data type**
- **Fast lookups by key**
- **Mutable**

### Creating Dictionaries

```python
student = {"name": "Alice", "age": 20, "grade": "A"}
empty_dict = {}
dict_constructor = dict(name="Bob", age=25)
from_lists = dict(zip(["a", "b", "c"], [1, 2, 3]))

print("Student:", student)
print("From constructor:", dict_constructor)
print("From lists:", from_lists)
```

### Accessing Values

```python
print("Student name:", student["name"])
print("Student age:", student.get("age"))
print("GPA (default):", student.get("gpa", "Not found"))
```

### Modifying Dictionaries

```python
student["major"] = "Computer Science"  # Add new key-value
student["age"] = 21                    # Update existing
print("After modifications:", student)
```

### Dictionary Methods

```python
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Removing items
removed_grade = student.pop("grade")
print("Removed grade:", removed_grade)
print("After removal:", student)
```

### Dictionary Comprehension

```python
squares = {x: x**2 for x in range(5)}
print("Squares:", squares)
```

### Nested Dictionaries

```python
classroom = {
    "student1": {"name": "Alice", "grade": 85},
    "student2": {"name": "Bob", "grade": 92},
    "student3": {"name": "Charlie", "grade": 78}
}
print("Alice's grade:", classroom["student1"]["grade"])
```

### Dictionary Membership

```python
print("Is 'name' in student?", "name" in student)
print("Is 'Alice' in student values?", "Alice" in student.values())
```

---

## 4. SETS - Unordered Collections of Unique Elements

**Sets store unique elements with no duplicates**

- **Unordered**: No indexing or slicing
- **Mutable**: Can add/remove elements
- **No duplicates allowed**
- **Fast membership testing**
- **Mathematical set operations**

### Creating Sets

```python
fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 4, 4, 5])  # Duplicates removed
empty_set = set()  # Note: {} creates empty dict, not set

print("Fruits set:", fruits_set)
print("From list (duplicates removed):", from_list)
```

### Adding and Removing

```python
fruits_set.add("orange")
fruits_set.update(["kiwi", "mango"])  # Add multiple
print("After additions:", fruits_set)

fruits_set.remove("banana")  # Raises error if not found
fruits_set.discard("grape")  # No error if not found
print("After removals:", fruits_set)
```

### Set Operations

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)
print("Union (|):", set1 | set2)                    # All elements
print("Intersection (&):", set1 & set2)             # Common elements
print("Difference (-):", set1 - set2)               # In set1 but not set2
print("Symmetric Difference (^):", set1 ^ set2)     # In either but not both
```

### Set Membership (very fast)

```python
print("Is 3 in set1?", 3 in set1)
print("Is set1 subset of {1,2,3,4,5,6}?", set1.issubset({1,2,3,4,5,6}))
```

### Practical Use Cases

#### 1. Remove duplicates from list
```python
original_list = [1, 2, 2, 3, 3, 4, 5, 5]
unique_list = list(set(original_list))
print("Remove duplicates:", unique_list)
```

#### 2. Find common elements
```python
list_a = ["apple", "banana", "cherry"]
list_b = ["banana", "cherry", "date"]
common = list(set(list_a) & set(list_b))
print("Common fruits:", common)
```

---

## Choosing the Right Data Structure

### 📋 LISTS
**When to use:**
- Need ordered data
- Need to modify elements
- Need indexing/slicing
- Allow duplicates

**Examples:** Shopping cart items, scores

### 📦 TUPLES
**When to use:**
- Need ordered, unchangeable data
- Dictionary keys
- Return multiple values from functions
- Coordinates, RGB values

**Examples:** (latitude, longitude), database records

### 🗂️ DICTIONARIES
**When to use:**
- Need key-value relationships
- Fast lookups by unique identifier

**Examples:** Student records, configuration settings

### 🎯 SETS
**When to use:**
- Need unique elements only
- Fast membership testing
- Mathematical set operations

**Examples:** Unique visitors, tags, permissions

---

## Performance Comparison Example

```python
import time

# List vs Set membership testing
large_list = list(range(10000))
large_set = set(range(10000))

# Test if 9999 is in collection
start = time.time()
9999 in large_list
list_time = time.time() - start

start = time.time()
9999 in large_set
set_time = time.time() - start

print(f"List membership test: {list_time:.6f} seconds")
print(f"Set membership test: {set_time:.6f} seconds")
print(f"Set is {list_time/set_time:.1f}x faster!")
```

---

## 🎯 Practice Exercises

Try these exercises to reinforce your learning:

1. **Create a list** of your top 5 favorite foods
2. **Add 2 more foods**, then remove the first one
3. **Create a tuple** with your (name, birth_year, favorite_color)
4. **Create a dictionary** with at least 3 friends and their ages
5. **Create a set** of unique numbers from this list: `[1,2,2,3,3,3,4,4,4,4]`
6. **Find common elements** between two lists using sets
7. **Create a nested dictionary** representing a simple gradebook
