tasks = []
done_tasks = []

try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except FileNotFoundError:
    pass

try:
    file = open("done_tasks.txt", "r")
    for line in file:
        done_tasks.append(line.strip())
    file.close()
except FileNotFoundError:
    pass

def show_tasks():
    print("List of tasks:")
    for number, task in enumerate(tasks, start=1):
        print(number, "-", task)
def show_done_tasks():
    print("List of done tasks:")
    for number, task in enumerate(done_tasks, start=1):
        print(number, "-", task)    
def add_task():
    task = input("Enter the task to add:")
    if task == "":
        print("Task cannot be empty. Please try again.")
    else:
        tasks.append(task)
def remove_task():
    task = input("Enter the task to remove:")
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully.")
    else:
        print("Task not found in the list. Please try again.")
def mark_task_done():
    task = input("Enter the task to mark as done: ")
    if task in tasks:
        tasks.remove(task)
        done_tasks.append(task)
        print("Done!")
    else:
        print("Task not found in the list. Please try again.")

while True:
    print("1-Show the list of tasks:")
    print("2-Add a task:")
    print("3-Remove a task:")
    print("4-Mark a task as done:")
    print("5-Show the list of done tasks:")
    print("6-Exit")
    choice = input("choose the task:")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_task_done()
    elif choice == "5":
        show_done_tasks()
    elif choice == "6":
        print("Goodbye!")
        file = open("tasks.txt", "w")
        for task in tasks:
            file.write(task + "\n")
        file.close()
        file = open("done_tasks.txt", "w")
        for task in done_tasks:
            file.write(task + "\n")
        file.close()
        break

    else:
        print("Invalid option. Please try again.")