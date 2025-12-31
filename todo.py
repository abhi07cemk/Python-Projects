# File where tasks are stored
FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                task_no = int(input("Enter task number to delete: "))
                removed = tasks.pop(task_no - 1)
                save_tasks(tasks)
                print(f"Deleted task: {removed}")
            except (ValueError, IndexError):
                print("Invalid task number!")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
