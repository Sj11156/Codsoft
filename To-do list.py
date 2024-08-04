import json
import os

TODO_FILE = "todo_list.json"

def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return {"tasks": [], "completed": []}

def save_todo_list(todo_list):
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file, indent=4)

def display_todo_list(todo_list, completed=False):
    if completed:
        tasks = todo_list["completed"]
        print("\nCompleted Tasks:")
    else:
        tasks = todo_list["tasks"]
        print("\nTo-Do List:")
    
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(todo_list):
    task = input("Enter a new task: ")
    todo_list["tasks"].append(task)
    save_todo_list(todo_list)
    print("Task added.")

def remove_task(todo_list):
    display_todo_list(todo_list)
    if todo_list["tasks"]:
        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(todo_list["tasks"]):
                removed_task = todo_list["tasks"].pop(task_index)
                save_todo_list(todo_list)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_task_completed(todo_list):
    display_todo_list(todo_list)
    if todo_list["tasks"]:
        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(todo_list["tasks"]):
                completed_task = todo_list["tasks"].pop(task_index)
                todo_list["completed"].append(completed_task)
                save_todo_list(todo_list)
                print(f"Task '{completed_task}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def undo_task_completed(todo_list):
    display_todo_list(todo_list, completed=True)
    if todo_list["completed"]:
        try:
            task_index = int(input("Enter the completed task number to undo: ")) - 1
            if 0 <= task_index < len(todo_list["completed"]):
                undone_task = todo_list["completed"].pop(task_index)
                todo_list["tasks"].append(undone_task)
                save_todo_list(todo_list)
                print(f"Task '{undone_task}' marked as incomplete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\n1. View To-Do List")
        print("2. View Completed Tasks")
        print("3. Add Task")
        print("4. Remove Task")
        print("5. Mark Task as Completed")
        print("6. Undo Completed Task")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            display_todo_list(todo_list, completed=True)
        elif choice == "3":
            add_task(todo_list)
        elif choice == "4":
            remove_task(todo_list)
        elif choice == "5":
            mark_task_completed(todo_list)
        elif choice == "6":
            undo_task_completed(todo_list)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()