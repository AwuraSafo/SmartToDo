# todo.py
# Team Project: Smart To-Do List / Task Manager

import json

FILENAME = "tasks.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    name = input("Enter task name: ")
    description = input("Enter description: ")
    while True:
        try:
            priority = int(input("Enter priority (1-5): "))
            if 1 <= priority <= 5:
                break
            else:
                print("Priority must be 1-5")
        except ValueError:
            print("Enter a valid number")
    task = {"name": name, "description": description, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['name']} - Priority: {task['priority']} - {task['description']}")

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions:\n1. Add task\n2. View tasks\n3. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye! Keep organizing your tasks.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
