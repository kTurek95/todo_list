user_tasks = []
completed_user_tasks = []


def add_task():
    user_task = input('Add a task: ')
    user_tasks.append(user_task)


def display_tasks():
    if len(user_tasks) > 0:
        print('Your task are:')
        for task in user_tasks:
            print(task)
    else:
        print("You don't have any tasks on the list.")


def delete_task():
    user_task_to_delete = input('Enter the task you want to delete: ')
    user_tasks.remove(user_task_to_delete)


def mark_task_completed():
    completed_tasks = input('Enter the completed task: ')
    user_tasks.remove(completed_tasks)
    completed_user_tasks.append(completed_tasks)
    print('Task has been moved to completed tasks')


def save_task_to_file():
    user_task_to_file = input('Enter the task you want to add to the file: ')
    with open('tasks.txt', 'w') as file:
        file.write(user_task_to_file)
    print('Task has been saved to the file')


def load_tasks_from_file():
    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())


while True:
    print('-----ToDoList Application-----')
    print('1. Add task')
    print('2. Display tasks')
    print('3. Remove task from the list')
    print('4. Mark task as completed')
    print('5. Save tasks to a file')
    print('6. Load tasks from a file')
    print('Press any other key to exit.')

    user_choice = input('Choose what you want to do: ')

    if user_choice == '1':
        add_task()
    elif user_choice == '2':
        display_tasks()
    elif user_choice == '3':
        delete_task()
    elif user_choice == '4':
        mark_task_completed()
    elif user_choice == '5':
        save_task_to_file()
    elif user_choice == '6':
        load_tasks_from_file()
    else:
        print('Invalid option')
        break
