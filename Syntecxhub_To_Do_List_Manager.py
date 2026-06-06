import json

FILE_NAME = "tasks.json"


# File Handling Functions
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Task Functions
def add_task(tasks):
    task = input("Enter task: ")
    tag = input("Enter tag: ")
    due_date = input("Enter due date: ")

    tasks.append({
        "task": task,
        "tag": tag,
        "due_date": due_date,
        "done": False
    })

    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n----- TASKS -----")

    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"

        print(
            f"{i}. {task['task']} | "
            f"Tag: {task['tag']} | "
            f"Due: {task['due_date']} | "
            f"Status: {status}"
        )


def mark_task_done(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number: "))

        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print("Deleted:", removed["task"])
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Menu Function
def menu():
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


# Main Program
def main():
    tasks = load_tasks()

    while True:
        menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_task_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Tasks saved successfully.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
