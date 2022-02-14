user_choice = -1
tasks = []


def show_tasks():
    task_index = 0
    print()
    print("Current tasks: ")
    if len(tasks) < 1:
        print("No taks")
    for task in tasks:
        print(str(task_index + 1) + ". " + task)
        task_index += 1


def tasks_to_file():
    try:
        file = open('tasks.txt', 'w+')
        for task in tasks:
            file.write(task + "\n")
        print()
        print("Tasks saved successfully")
    except:
        print()
        print("Error - tasks NOT saved")
    finally:
        file.close()


while user_choice != 5:
    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        task = input("Type task name: ")
        tasks.append(task)
        print('Task added: ' + task)
    if user_choice == 3:
        id_to_be_deleted_plus_1 = input("Type number of task to be deleted: ")
        try:
            print()
            print("Deleted task: " + tasks.pop(int(id_to_be_deleted_plus_1) - 1))
        except:
            print()
            print('Oops Something went wrong. Make sure you put a correct task number')
    if user_choice == 4:
        tasks_to_file()
    print()
    print('1. Show tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Save changes')
    print('5. Exit')
    user_choice = int(input("Select number: "))
