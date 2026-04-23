import json

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def mark_completed():
    view_tasks()
    num = int(input("Enter task number completed: "))
    if 1 <= num <= len(tasks):
        tasks[num - 1]["completed"] = True
        print("Task marked completed.")
    else:
        print("Invalid task number.")

def menu():
    load_tasks()

    while True:
        print("\n--- TO DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Completed")
        print("5. Save and Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            save_tasks()
            print("Tasks saved. Goodbye.")
            break
        else:
            print("Invalid choice.")

menu()