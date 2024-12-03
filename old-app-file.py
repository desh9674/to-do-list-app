import json
import os
from datetime import datetime

# Function to load tasks from a JSON file
def load_tasks(filename='tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

# Function to save tasks to a JSON file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to calculate the number of days remaining
def calculate_days_remaining(created_date, due_date):
    if due_date:
        created_date_obj = datetime.strptime(created_date, "%Y-%m-%d %H:%M:%S")
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        return (due_date_obj - created_date_obj).days
    return None

# Function to display tasks in a formatted way
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    print("\n--- To-Do List ---")
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task['completed'] else "Pending"
        due_date = f" | Due: {task['due_date']}" if task['due_date'] else ""
        days_remaining = calculate_days_remaining(task['created_date'], task['due_date'])
        days_remaining_str = f" | Days Remaining: {days_remaining}" if days_remaining is not None else ""
        print(f"{idx}. {task['description']} (Created: {task['created_date']}){due_date}{days_remaining_str} | Status: {status}")
    print("-------------------\n")

# Function to add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    due_date = input("Enter due date (optional, format YYYY-MM-DD, leave blank if none): ")
    
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Task not added.\n")
            return
    
    task = {
        'description': description,
        'created_date': created_date,
        'due_date': due_date if due_date else None,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

# Function to edit a task
def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to edit: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            new_description = input(f"Enter new description (current: {task['description']}): ")
            new_due_date = input(f"Enter new due date (current: {task['due_date']}, format YYYY-MM-DD, leave blank to keep the same): ")
            new_status = input(f"Is the task completed? (yes/no, current: {'yes' if task['completed'] else 'no'}): ")

            if new_due_date:
                try:
                    datetime.strptime(new_due_date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Task not updated.\n")
                    return

            task['description'] = new_description or task['description']
            task['due_date'] = new_due_date or task['due_date']
            task['completed'] = new_status.lower() == 'yes'
            
            save_tasks(tasks)
            print("Task updated successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            save_tasks(tasks)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to display the main menu and handle user input
def main_menu():
    tasks = load_tasks()
    while True:
        print("To-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
