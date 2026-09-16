tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['task']}")

    elif choice == "3":
        if not tasks:
            print("No tasks to complete.")
        else:
            number = int(input("Enter task number to complete: "))
            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                deleted = tasks.pop(number - 1)
                print(f"Deleted: {deleted['task']}")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
