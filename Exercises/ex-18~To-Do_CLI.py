import os
os.system('cls' if os.name == 'nt' else 'clear')

tasks = []

def view_tasks(tasks):
    if len(tasks) == 0: # if the task list is empty then we inform
        print("No tasks yet!") 
        return
    else:
        print("\n Your To-Do list:") 
        for task in tasks: # looping thru the task list
            status = "✅" if task["done"] else "❌" # we check for each task if the task's done attribute is true or false
            print(f"{(tasks.index(task))+1}. {task['task']} - {status}")

def add_task(tasks):
    task_name = input("Enter task: ").strip()

    if task_name == "":
        print("Task cannot be empty")
        return
    tasks.append({"task": task_name, "done": False}) # In lists we can append items such as other lists, sets, tuples and even dicts
    print(f"\nTask '{task_name}' added successfully!")

def mark_task(tasks):
    if not tasks:
        print("\nNo tasks to mark!")
        return
    else:
        view_tasks(tasks)
        try:
            task_num = int(input("Enter the task number to mark as done: "))

            if 1 <= task_num <= len(tasks):
                tasks[task_num-1]["done"] = True
                print(f"Task '{tasks[task_num-1]['task']}' marked as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Enter a valid integer!")

def edit_task(tasks):
    if not tasks:
        print("\nNo tasks to delete")
        return
    else:
        view_tasks(tasks)
        try:
            task_num = int(input("Enter task number to edit: "))
            if 1<= task_num <= len(tasks):
                tasks[task_num-1]['task'] = input("Edit Task: ")
                tasks[task_num-1]['done'] = False
                print(f"Your new task at {task_num} is '{tasks[task_num-1]['task']}'!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Enter a number!")


def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete!")
    else:
        view_tasks(tasks)
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num-1)
                print(f"Task '{removed['task']}' removed")
            else:
                print("Invalid task number")
        except ValueError:
            print("Enter a valid number!")

while True:
    print("\nTo-Do List App")
    print("===============")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Edit task")
    print("5. Delete Task")
    print("6. Exit")
    try:
        print("===============")
        choice = int(input("Enter your choice (1-6): "))
        if choice == 6:
            print("Goodbye!")
            break
        elif choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            mark_task(tasks)
        elif choice == 4:
            edit_task(tasks)
        elif choice == 5:
            delete_task(tasks)
    except Exception as e:
        print("Invalid choice ",e)
    