""" Day 29: Basic Project: To-Do List Manager """

import json
import os
from datetime import datetime
from typing import List, Dict

class TodoManager:
    """A comprehensive to-do list manager"""
    
    def __init__(self, filename: str = "todos.json"):
        self.filename = filename
        self.tasks: List[Dict] = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
                print(f"Loaded {len(self.tasks)} tasks from {self.filename}")
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error loading tasks. Starting with empty list.")
                self.tasks = []
        else:
            print("No existing task file found. Starting fresh!")
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.tasks, f, indent=2)
            print(f"Tasks saved to {self.filename}")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, description: str, priority: str = "medium"):
        """Add a new task"""
        if not description.strip():
            print("Task description cannot be empty!")
            return
        
        task = {
            "id": len(self.tasks) + 1,
            "description": description.strip(),
            "completed": False,
            "priority": priority.lower(),
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        
        self.tasks.append(task)
        print(f"Task '{description}' added successfully!")
    
    def view_tasks(self, show_completed: bool = True):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found!")
            return
        
        print("\n" + "="*60)
        print("YOUR TO-DO LIST")
        print("="*60)
        
        for task in self.tasks:
            if not show_completed and task["completed"]:
                continue
            
            status = "✓" if task["completed"] else "○"
            priority = task["priority"].upper()
            
            print(f"{status} [{task['id']}] {task['description']}")
            print(f"    Priority: {priority} | Created: {task['created_at'][:10]}")
            
            if task["completed"] and task["completed_at"]:
                print(f"    Completed: {task['completed_at'][:10]}")
            print()
    
    def complete_task(self, task_id: int):
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print(f"Task '{task['description']}' is already completed!")
                else:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().isoformat()
                    print(f"Task '{task['description']}' marked as completed!")
                return
        
        print(f"Task with ID {task_id} not found!")
    
    def delete_task(self, task_id: int):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                description = task["description"]
                del self.tasks[i]
                print(f"Task '{description}' deleted successfully!")
                return
        
        print(f"Task with ID {task_id} not found!")
    
    def get_stats(self):
        """Display task statistics"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["completed"])
        pending = total - completed
        
        print(f"\n=== TASK STATISTICS ===")
        print(f"Total tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"Completion rate: {completion_rate:.1f}%")

def get_valid_input(prompt: str, valid_options: List[str]) -> str:
    """Get valid input from user"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        print(f"Please enter one of: {', '.join(valid_options)}")

def main():
    """Main function to run the to-do list manager"""
    todo_manager = TodoManager()
    
    print("Welcome to the To-Do List Manager!")
    
    while True:
        print("\n" + "="*40)
        print("TO-DO LIST MANAGER")
        print("="*40)
        print("1. Add task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. Complete task")
        print("5. Delete task")
        print("6. View statistics")
        print("7. Save and exit")
        print("8. Exit without saving")
        
        choice = input("\nChoose an option (1-8): ").strip()
        
        if choice == '1':
            description = input("Enter task description: ")
            priority = get_valid_input(
                "Enter priority (high/medium/low): ", 
                ["high", "medium", "low"]
            )
            todo_manager.add_task(description, priority)
        
        elif choice == '2':
            todo_manager.view_tasks(show_completed=True)
        
        elif choice == '3':
            todo_manager.view_tasks(show_completed=False)
        
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to complete: "))
                todo_manager.complete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID!")
        
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to delete: "))
                confirm = input("Are you sure? (y/n): ").lower()
                if confirm == 'y':
                    todo_manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID!")
        
        elif choice == '6':
            todo_manager.get_stats()
        
        elif choice == '7':
            todo_manager.save_tasks()
            print("Goodbye!")
            break
        
        elif choice == '8':
            confirm = input("Exit without saving? (y/n): ").lower()
            if confirm == 'y':
                print("Goodbye!")
                break
        
        else:
            print("Invalid choice! Please select 1-8.")

if __name__ == "__main__":
    main()

# EXERCISES:
# 1. Add due dates to tasks and sort by deadline
# 2. Implement task categories/tags (work, personal, shopping, etc.)
# 3. Add a search function to find tasks by keyword
# 4. Create a feature to edit existing task descriptions
# 5. Add recurring tasks (daily, weekly, monthly)
# 6. Implement task reminders with notifications
# 7. Add the ability to export tasks to CSV or text file
# 8. Create a web interface using Flask for the to-do manager