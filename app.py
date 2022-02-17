import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


user_choice = -1
tasks = []


def show_tasks():
    task_index = 0
    cls()
    print("Current tasks: ")
    if len(tasks) < 1:
        print("No taks")
    for task in tasks:
        print(str(task_index + 1) + ". " + task)
        task_index += 1


def add_task():
    task = input("Type task name: ")
    tasks.append(task)
    cls()
    print('Task added: ' + task)


def delete_task():
    id_to_be_deleted_plus_1 = input("Type number of task to be deleted: ")
    try:
        cls()
        print("Deleted task: " + tasks.pop(int(id_to_be_deleted_plus_1) - 1))
    except:
        cls()
        print('Oops Something went wrong. Make sure you put a correct task number')


def show_menu():
    print()
    print('1. Show tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Save changes')
    print('5. Exit')
    global user_choice
    user_choice = int(input("Select number: "))


def tasks_to_file():
    try:
        file = open('tasks.txt', 'w+')
        for task in tasks:
            file.write(task + "\n")
        cls()
        print("Tasks saved successfully")
    except:
        cls()
        print("Error - tasks NOT saved")
    finally:
        file.close()


def read_tasks_from_file():
    try:
        file = open('tasks.txt')
        for line in file.readlines():
            tasks.append(line.strip())
    except:
        print("File not loaded")
    finally:
        file.close()


read_tasks_from_file()

while user_choice != 5:
    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        add_task()
    if user_choice == 3:
        delete_task()
    if user_choice == 4:
        tasks_to_file()
    show_menu()
