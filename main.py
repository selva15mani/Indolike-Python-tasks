tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added: {task}")

def remove_task():
    show_tasks()
    try:
        num = int(input("Enter the task number to remove: "))
        removed = tasks.pop(num - 1)
        print(f"Removed: {removed}")
    except (IndexError, ValueError):
        print("Invalid number!")

def menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Show tasks\n2. Add task\n3. Remove task\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

menu()