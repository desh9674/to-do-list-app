import json
import os
from datetime import datetime

def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Edit Task")
    print("5. Exit")

def add_task(tasks):
    task_desc = input("Enter a task: ")
    due_date = input("Enter a due date (YYYY-MM-DD) or leave blank: ")
    created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"task": task_desc, "completed": False, "created_date": created_date, "due_date": due_date or None})
    save_tasks(tasks)

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Incomplete"
        due_date = task["due_date"] if task["due_date"] else "No due date"
        print(f"{idx + 1}. {task['task']} - {status} - Created: {task['created_date']} - Due: {due_date}")

def remove_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task removed.")
    else:
        print("Invalid task number.")

def edit_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to edit: ")) - 1
    if 0 <= task_num < len(tasks):
        task = tasks[task_num]
        print(f"Editing task: {task['task']}")
        task['task'] = input(f"New description (current: {task['task']}): ") or task['task']
        task['due_date'] = input(f"New due date (current: {task['due_date']}): ") or task['due_date']
        task['completed'] = input(f"Mark as completed? (yes/no, current: {'Completed' if task['completed'] else 'Incomplete'}): ").lower() == 'yes'
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    return []

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
