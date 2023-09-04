user_tasks = []
completed_user_tasks = []


def add_task(tasks: list):
    user_task = input('Add a task: ')
    if len(user_task) > 0:
        tasks.append(user_task)
        print(tasks)
    else:
        print("You haven't added any task")


def display_tasks(tasks: list):
    if len(tasks) > 0:
        tasks_string = 'Your tasks are:\n' + '\n'.join(tasks)
        return tasks_string

    return "You don't have any tasks on the list."


def delete_task(task: str, tasks_list: list):
    if task in tasks_list:
        tasks_list.remove(task)
    else:
        return 'Task does not exist'


def mark_completed_task():
    completed_tasks = input('Enter the completed task: ')
    user_tasks.remove(completed_tasks)
    completed_user_tasks.append(completed_tasks)
    print('Task has been moved to completed tasks')


def save_task_to_file():
    user_task_to_file = input('Enter the task you want to add to the file: ')
    with open('tasks.txt', 'a', encoding='utf8') as file:
        file.write(f'{user_task_to_file}\n')
    print('Task has been saved to the file')


def load_tasks_from_file():
    with open('tasks.txt', 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
