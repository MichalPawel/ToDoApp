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


while user_choice != 5:
    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        task = input("Type task name: ")
        tasks.append(task)
        print('Task added: ' + task)
    if user_choice == 3:
        id_to_be_deleted_plus_1 = input("Type number of task to be deleted: ")
        print("Deleted task: " + tasks.pop(int(id_to_be_deleted_plus_1) - 1))
    print()
    print('1. Show tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Save changes')
    print('5. Exit')
    user_choice = int(input("Select number: "))
