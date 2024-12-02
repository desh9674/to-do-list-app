import json
import os

def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{idx + 1}. {task['task']} - {status}")

def remove_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task removed.")
    else:
        print("Invalid task number.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete.")
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
            mark_task_complete(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
