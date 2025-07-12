"""
Day 19: File Operations - Complete Guide to Reading, Writing, and Processing Files
================================================================================

Learning Objectives:
- Master file reading and writing operations
- Understand file modes and their applications
- Learn context managers for safe file handling
- Work with different file formats (text, binary, CSV, JSON)
- Implement error handling for file operations
- Practice with real-world file processing examples
"""


import os
import json
import csv
from pathlib import Path

print("=" * 60)
print("Day 19: File Operations - Complete Guide")
print("=" * 60)

# ============================================================================
# SECTION 1: BASIC FILE OPERATIONS
# ============================================================================
print("\n1. BASIC FILE OPERATIONS")
print("-" * 30)

# File modes explanation
print("=== FILE MODES ===")
print("""
File Modes:
"r"  - Read (default) - File must exist
"w"  - Write - Creates new file or overwrites existing
"a"  - Append - Creates new file or appends to existing
"x"  - Exclusive creation - Fails if file exists
"b"  - Binary mode (add to other modes: "rb", "wb", "ab")
"t"  - Text mode (default)
"+"  - Read and write (add to other modes: "r+", "w+", "a+")
""")

# Writing to a file
print("\n=== WRITING FILES ===")
try:
    # Create a sample file with different write modes
    with open("sample_write.txt", "w") as file:
        file.write("First line of text\n")
        file.write("Second line of text\n")
        file.writelines(["Third line\n", "Fourth line\n"])
    
    print("✅ File 'sample_write.txt' created successfully")
    
    # Append to the file
    with open("sample_write.txt", "a") as file:
        file.write("Appended line\n")
    
    print("✅ Content appended to file")
    
except Exception as e:
    print(f"❌ Error writing file: {e}")

# Reading from a file
print("\n=== READING FILES ===")
try:
    # Read entire file
    with open("sample_write.txt", "r") as file:
        content = file.read()
        print("Full file content:")
        print(content)
    
    # Read line by line
    print("\nReading line by line:")
    with open("sample_write.txt", "r") as file:
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")
    
    # Read specific number of lines
    print("\nReading first 3 lines:")
    with open("sample_write.txt", "r") as file:
        lines = file.readlines()[:3]
        for i, line in enumerate(lines, 1):
            print(f"  {i}. {line.strip()}")
            
except FileNotFoundError:
    print("❌ File not found")
except Exception as e:
    print(f"❌ Error reading file: {e}")

# ============================================================================
# SECTION 2: ADVANCED FILE OPERATIONS
# ============================================================================
print("\n2. ADVANCED FILE OPERATIONS")
print("-" * 35)

# Working with file positions
print("=== FILE POSITION CONTROL ===")
try:
    with open("sample_write.txt", "r") as file:
        print(f"Initial position: {file.tell()}")
        
        # Read first 10 characters
        first_part = file.read(10)
        print(f"First 10 chars: '{first_part}'")
        print(f"Position after reading: {file.tell()}")
        
        # Move to beginning
        file.seek(0)
        print(f"Position after seek(0): {file.tell()}")
        
        # Read from current position
        remaining = file.read(20)
        print(f"Next 20 chars: '{remaining}'")

except Exception as e:
    print(f"❌ Error with file positions: {e}")

# Binary file operations
print("\n=== BINARY FILE OPERATIONS ===")
try:
    # Write binary data
    binary_data = b"This is binary data\x00\x01\x02\x03"
    with open("sample_binary.bin", "wb") as file:
        file.write(binary_data)
    
    print("✅ Binary file created")
    
    # Read binary data
    with open("sample_binary.bin", "rb") as file:
        read_data = file.read()
        print(f"Binary data: {read_data}")
        print(f"As string: {read_data.decode('utf-8', errors='ignore')}")

except Exception as e:
    print(f"❌ Error with binary files: {e}")

# ============================================================================
# SECTION 3: CSV FILE OPERATIONS
# ============================================================================
print("\n3. CSV FILE OPERATIONS")
print("-" * 25)

# Writing CSV files
print("=== WRITING CSV FILES ===")
try:
    # Sample data
    students_data = [
        ["Name", "Age", "Grade", "Subject"],
        ["Alice Johnson", 20, "A", "Computer Science"],
        ["Bob Smith", 19, "B+", "Mathematics"],
        ["Charlie Brown", 21, "A-", "Physics"],
        ["Diana Prince", 20, "A", "Chemistry"]
    ]
    
    # Write CSV file
    with open("students.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(students_data)
    
    print("✅ CSV file 'students.csv' created")
    
    # Write CSV with DictWriter
    students_dict = [
        {"name": "Eve Wilson", "age": 22, "grade": "B", "subject": "Biology"},
        {"name": "Frank Miller", "age": 19, "grade": "A-", "subject": "Literature"}
    ]
    
    with open("students_dict.csv", "w", newline='', encoding='utf-8') as file:
        fieldnames = ["name", "age", "grade", "subject"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_dict)
    
    print("✅ Dictionary-based CSV file created")

except Exception as e:
    print(f"❌ Error writing CSV: {e}")

# Reading CSV files
print("\n=== READING CSV FILES ===")
try:
    # Read CSV with csv.reader
    print("Students data (using csv.reader):")
    with open("students.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row_num, row in enumerate(reader):
            if row_num == 0:
                print(f"  Headers: {row}")
            else:
                print(f"  Student {row_num}: {row}")
    
    # Read CSV with DictReader
    print("\nStudents data (using DictReader):")
    with open("students.csv", "r", encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for student in reader:
            print(f"  {student['Name']} ({student['Age']}) - Grade: {student['Grade']}")

except Exception as e:
    print(f"❌ Error reading CSV: {e}")

# ============================================================================
# SECTION 4: JSON FILE OPERATIONS
# ============================================================================
print("\n4. JSON FILE OPERATIONS")
print("-" * 25)

# Writing JSON files
print("=== WRITING JSON FILES ===")
try:
    # Sample data structure
    school_data = {
        "school_name": "Python Learning Academy",
        "established": 2020,
        "students": [
            {
                "id": 1,
                "name": "Alice Johnson",
                "courses": ["Python", "Data Science"],
                "grades": {"Python": 95, "Data Science": 88},
                "active": True
            },
            {
                "id": 2,
                "name": "Bob Smith",
                "courses": ["Python", "Web Development"],
                "grades": {"Python": 87, "Web Development": 92},
                "active": True
            }
        ],
        "faculty": {
            "total_count": 10,
            "departments": ["Computer Science", "Mathematics", "Physics"]
        }
    }
    
    # Write JSON file with proper formatting
    with open("school_data.json", "w", encoding='utf-8') as file:
        json.dump(school_data, file, indent=2, ensure_ascii=False)
    
    print("✅ JSON file 'school_data.json' created")

except Exception as e:
    print(f"❌ Error writing JSON: {e}")

# Reading JSON files
print("\n=== READING JSON FILES ===")
try:
    # Read and parse JSON file
    with open("school_data.json", "r", encoding='utf-8') as file:
        loaded_data = json.load(file)
    
    print(f"School: {loaded_data['school_name']}")
    print(f"Established: {loaded_data['established']}")
    print(f"Total students: {len(loaded_data['students'])}")
    
    print("\nStudent details:")
    for student in loaded_data['students']:
        avg_grade = sum(student['grades'].values()) / len(student['grades'])
        print(f"  {student['name']} (ID: {student['id']}) - Average: {avg_grade:.1f}")

except Exception as e:
    print(f"❌ Error reading JSON: {e}")

# ============================================================================
# SECTION 5: ERROR HANDLING AND BEST PRACTICES
# ============================================================================
print("\n5. ERROR HANDLING AND BEST PRACTICES")
print("-" * 40)

def safe_file_operation(filename, operation="read"):
    """Demonstrate comprehensive error handling for file operations"""
    try:
        if operation == "read":
            with open(filename, "r", encoding='utf-8') as file:
                return file.read()
        elif operation == "write":
            with open(filename, "w", encoding='utf-8') as file:
                file.write("Test content")
                return "Write successful"
    
    except FileNotFoundError:
        return f"❌ File '{filename}' not found"
    except PermissionError:
        return f"❌ Permission denied for '{filename}'"
    except UnicodeDecodeError:
        return f"❌ Unicode decode error in '{filename}'"
    except Exception as e:
        return f"❌ Unexpected error: {e}"

# Test error handling
print("=== ERROR HANDLING EXAMPLES ===")
print(safe_file_operation("nonexistent.txt", "read"))
print(safe_file_operation("test_write.txt", "write"))

# File existence checking
print("\n=== FILE EXISTENCE AND PROPERTIES ===")
files_to_check = ["students.csv", "school_data.json", "nonexistent.txt"]

for filename in files_to_check:
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"✅ {filename} exists (Size: {size} bytes)")
    else:
        print(f"❌ {filename} does not exist")

# ============================================================================
# SECTION 6: PATHLIB - MODERN FILE HANDLING
# ============================================================================
print("\n6. PATHLIB - MODERN FILE HANDLING")
print("-" * 35)

print("=== USING PATHLIB ===")
# Modern approach using pathlib
current_dir = Path(".")
print(f"Current directory: {current_dir.absolute()}")

# Create directory structure
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Work with paths
json_file = data_dir / "sample.json"
csv_file = data_dir / "sample.csv"

# Write files using pathlib
sample_data = {"message": "Hello from pathlib!", "timestamp": "2025-06-24"}
json_file.write_text(json.dumps(sample_data, indent=2), encoding='utf-8')

print(f"✅ Created: {json_file}")
print(f"File exists: {json_file.exists()}")
print(f"File size: {json_file.stat().st_size} bytes")

# List files in directory
print("\nFiles in data directory:")
for file_path in data_dir.iterdir():
    if file_path.is_file():
        print(f"  📄 {file_path.name} ({file_path.stat().st_size} bytes)")

# ============================================================================
# SECTION 7: PRACTICAL EXAMPLES AND EXERCISES
# ============================================================================
print("\n7. PRACTICAL EXAMPLES")
print("-" * 25)

# Example 1: Log file processor
def create_sample_log():
    """Create a sample log file for processing"""
    log_entries = [
        "2025-06-24 10:00:01 INFO User login successful - user123",
        "2025-06-24 10:05:15 WARNING Failed login attempt - user456",
        "2025-06-24 10:10:30 ERROR Database connection failed",
        "2025-06-24 10:15:45 INFO File upload completed - document.pdf",
        "2025-06-24 10:20:00 ERROR Memory usage critical - 95%",
        "2025-06-24 10:25:15 INFO User logout - user123"
    ]
    
    with open("application.log", "w") as file:
        file.write("\n".join(log_entries))

def analyze_log_file(filename):
    """Analyze log file and extract statistics"""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        
        stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        
        for line in lines:
            for level in stats.keys():
                if level in line:
                    stats[level] += 1
                    break
        
        return stats
    except Exception as e:
        return f"Error analyzing log: {e}"

# Create and analyze log file
print("=== LOG FILE ANALYSIS EXAMPLE ===")
create_sample_log()
log_stats = analyze_log_file("application.log")
print("Log file statistics:")
for level, count in log_stats.items():
    print(f"  {level}: {count}")

# Example 2: Configuration file handler
def create_config_file():
    """Create a sample configuration file"""
    config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp_db"
        },
        "api": {
            "base_url": "https://api.example.com",
            "timeout": 30,
            "retries": 3
        },
        "features": {
            "enable_caching": True,
            "debug_mode": False,
            "max_file_size": 10485760
        }
    }
    
    with open("config.json", "w") as file:
        json.dump(config, file, indent=2)

def load_config(filename):
    """Load and validate configuration"""
    try:
        with open(filename, "r") as file:
            config = json.load(file)
        
        # Basic validation
        required_sections = ["database", "api", "features"]
        for section in required_sections:
            if section not in config:
                raise ValueError(f"Missing required section: {section}")
        
        return config
    except Exception as e:
        return f"Error loading config: {e}"

print("\n=== CONFIGURATION FILE EXAMPLE ===")
create_config_file()
config_data = load_config("config.json")
if isinstance(config_data, dict):
    print("✅ Configuration loaded successfully")
    print(f"Database host: {config_data['database']['host']}")
    print(f"API timeout: {config_data['api']['timeout']}s")
else:
    print(config_data)

# ============================================================================
# SECTION 8: EXERCISES AND CHALLENGES
# ============================================================================
print("\n8. EXERCISES AND CHALLENGES")
print("-" * 35)

print("""
Practice Exercises:

1. **Text File Processor**
   - Read a text file and count words, lines, and characters
   - Find the most common word
   - Create a summary report

2. **CSV Data Analyzer**
   - Load student grades from CSV
   - Calculate statistics (average, min, max)
   - Generate a grade distribution report

3. **Log File Monitor**
   - Process log files for error patterns
   - Extract timestamp ranges
   - Generate alert summaries

4. **Configuration Manager**
   - Create a class to manage JSON configurations
   - Support default values and validation
   - Implement save/load functionality

5. **File Backup System**
   - Create backups of important files
   - Implement versioning with timestamps
   - Add compression support

6. **Data Migration Tool**
   - Convert between different file formats (CSV ↔ JSON)
   - Handle encoding issues
   - Validate data integrity

""")

# Example solution for Exercise 1
def analyze_text_file(filename):
    """Analyze text file and return statistics"""
    try:
        with open(filename, "r", encoding='utf-8') as file:
            content = file.read()
        
        lines = content.split('\n')
        words = content.split()
        
        # Word frequency
        word_freq = {}
        for word in words:
            clean_word = word.lower().strip('.,!?";')
            word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
        
        # Find most common word
        most_common = max(word_freq.items(), key=lambda x: x[1]) if word_freq else ("", 0)
        
        return {
            "lines": len(lines),
            "words": len(words),
            "characters": len(content),
            "most_common_word": most_common[0],
            "word_frequency": most_common[1]
        }
    
    except Exception as e:
        return f"Error analyzing file: {e}"

print("\n=== TEXT ANALYSIS EXAMPLE ===")
if os.path.exists("sample_write.txt"):
    analysis = analyze_text_file("sample_write.txt")
    if isinstance(analysis, dict):
        print(f"Lines: {analysis['lines']}")
        print(f"Words: {analysis['words']}")
        print(f"Characters: {analysis['characters']}")
        print(f"Most common word: '{analysis['most_common_word']}' ({analysis['word_frequency']} times)")

# ============================================================================
# SECTION 9: CLEANUP AND BEST PRACTICES
# ============================================================================
print("\n9. CLEANUP AND BEST PRACTICES")
print("-" * 35)

print("""
File Handling Best Practices:

1. **Always use context managers (with statements)**
   - Ensures files are properly closed
   - Handles exceptions gracefully

2. **Specify encoding explicitly**
   - Use encoding='utf-8' for text files
   - Prevents encoding-related issues

3. **Handle exceptions appropriately**
   - FileNotFoundError, PermissionError, etc.
   - Provide meaningful error messages

4. **Use pathlib for modern path handling**
   - More readable and cross-platform
   - Better error handling

5. **Validate file operations**
   - Check file existence before operations
   - Verify file permissions

6. **Choose appropriate file modes**
   - Understand the difference between modes
   - Use binary mode for non-text files

7. **Consider memory usage**
   - Use generators for large files
   - Process files in chunks when needed

8. **Implement proper logging**
   - Log file operations for debugging
   - Track file access patterns
""")

# Clean up example files (optional)
cleanup_files = [
    "sample_write.txt", "sample_binary.bin", "students.csv", 
    "students_dict.csv", "school_data.json", "application.log", 
    "config.json", "test_write.txt"
]

print(f"\n📁 Created {len(cleanup_files)} example files for learning")
print("💡 Tip: Review the generated files to understand the different formats")

print("\n" + "=" * 60)
print("Day 19 Complete! 🎉")
print("Next: Day 20 - Modules and Imports")
print("=" * 60)