""" Day 27: Introduction to JSON and APIs """

import json
import requests
from typing import Dict, Any

def json_basics():
    """Demonstrate basic JSON operations"""
    print("=== JSON Basics ===")
    
    # Creating and converting data
    data = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland",
        "is_student": False,
        "hobbies": ["reading", "coding", "gaming"],
        "address": {
            "street": "123 Main St",
            "zip": "12345"
        }
    }
    
    # Convert to JSON string
    json_string = json.dumps(data, indent=2)
    print("JSON String:")
    print(json_string)
    
    # Parse JSON string back to Python object
    parsed_data = json.loads(json_string)
    print(f"\nParsed back: {parsed_data['name']} is {parsed_data['age']} years old")
    
    # Save to file
    with open('user_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("\nData saved to user_data.json")
    
    # Load from file
    with open('user_data.json', 'r') as f:
        loaded_data = json.load(f)
    print(f"Loaded from file: {loaded_data['city']}")

def api_example():
    """Demonstrate basic API usage"""
    print("\n=== API Example ===")
    
    try:
        # Simple API call (JSONPlaceholder - fake REST API)
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        
        if response.status_code == 200:
            user_data = response.json()
            print(f"User: {user_data['name']}")
            print(f"Email: {user_data['email']}")
            print(f"Company: {user_data['company']['name']}")
        else:
            print(f"Error: {response.status_code}")
            
    except requests.RequestException as e:
        print(f"Network error: {e}")

def main():
    json_basics()
    api_example()

if __name__ == "__main__":
    main()

# EXERCISES:
# 1. Create a JSON file with your personal information (name, age, favorite foods, etc.)
# 2. Write a function that reads the JSON file and formats it nicely
# 3. Use the JSONPlaceholder API to get all users and display their names and cities
# 4. Create a function that saves API data to a JSON file
# 5. Handle different HTTP status codes (404, 500, etc.) in your API calls