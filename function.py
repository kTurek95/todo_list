from Exception import InvalidInput, InvalidLength
user_tasks = []
completed_user_tasks = []


def add_task(tasks: list):
    try:
        user_task = input('Add a task: ')
        if user_task.isnumeric():
            raise ValueError('Your task cannot be a number')
        elif len(user_task) > 0:
            tasks.append(user_task)
        else:
            raise InvalidLength("You haven't added any task")
    except ValueError as e:
        print(e)
    except InvalidLength as e:
        print(e)


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
    try:
        completed_tasks = input('Enter the completed task: ')
        if completed_tasks.isnumeric():
            raise ValueError('Your task cannot be a number')
        elif len(completed_tasks) < 1:
            raise InvalidLength("You haven't added any taks")
        elif completed_tasks not in user_tasks and len(completed_tasks) > 0:
            raise InvalidInput("You don't have such a task on your list")
        else:
            user_tasks.remove(completed_tasks)
            completed_user_tasks.append(completed_tasks)
            print('Task has been moved to completed tasks')
    except ValueError as e:
        print(e)
    except InvalidLength as e:
        print(e)
    except InvalidInput as e:
        print(e)


def save_task_to_file():
    print(f'Your tasks: {user_tasks}')
    user_task_to_file = input('Choose the task you want to add to the file: ')
    try:
        if user_task_to_file in user_tasks:
            with open('tasks.txt', 'a', encoding='utf8') as file:
                file.write(f'{user_task_to_file}\n')
            print('Task has been saved to the file')
            user_tasks.remove(user_task_to_file)
        else:
            raise InvalidInput("You don't have such a task on your list")
    except InvalidInput as e:
        print(e)


def load_tasks_from_file():
    with open('tasks.txt', 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
