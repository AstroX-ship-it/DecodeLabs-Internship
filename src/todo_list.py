# ============================================================
# PROJECT 1 - TO-DO LIST
# ============================================================


# ============================================================
# 1. DATA STORAGE
# ============================================================

tasks = []


# ============================================================
# 2. ADD TASK
# ============================================================

def add_task():
    task = input("Enter your task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append(task)

    print("Task added successfully!")


# ============================================================
# 3. VIEW TASKS
# ============================================================

def view_tasks():

    if len(tasks) == 0:
        print("\nYour To-Do List is empty.")
        return

    print("\n========== YOUR TO-DO LIST ==========")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

    print("=====================================")


# ============================================================
# 4. MAIN MENU
# ============================================================

def main():

    while True:

        print("\n=====================================")
        print("          PYTHON TO-DO LIST")
        print("=====================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("\nThank you for using the To-Do List!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice.")
            print("Please enter 1, 2, or 3.")


# ============================================================
# 5. PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()