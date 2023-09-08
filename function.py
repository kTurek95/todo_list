"""
Module with functions
This module provides functions for basic task management.
It includes functionalities for adding, displaying, deleting,
and marking tasks as completed, as well as saving and loading tasks from a file.
"""

from exception import InvalidInput, InvalidLength
user_tasks = []
completed_user_tasks = []


def add_task(tasks: list):
    """
    Adds a task to the given tasks list.

    Args:
        tasks (list): The list to which the task will be added.

    Raises:
        ValueError: If the user input is a numeric value.
        InvalidLength: If the user input is empty.

    Returns:
        None
    """
    try:
        user_task = input('Add a task: ')
        if user_task.isnumeric():
            raise ValueError('Your task cannot be a number')
        if len(user_task) > 0:
            tasks.append(user_task)
        else:
            raise InvalidLength("You haven't added any task")
    except ValueError as error:
        print(error)
    except InvalidLength as error:
        print(error)


def display_tasks(tasks: list):
    """
    Displays the tasks in the given tasks list.

    Args:
        tasks (list): The list of tasks to be displayed.

    Returns:
        str: A formatted string containing the tasks or a message if the list is empty.
    """
    if len(tasks) > 0:
        tasks_string = 'Your tasks are:\n' + '\n'.join(tasks)
        return tasks_string

    return "You don't have any tasks on the list."


def delete_task(task: str, tasks_list: list):
    """
    Deletes a task from the specified tasks list.

    Args:
        task (str): The task to be deleted.
        tasks_list (list): The list from which the task will be removed.

    Raises:
        InvalidTask: If the task does not exist in the list.

    Returns:
        None
    """

    if task in tasks_list:
        tasks_list.remove(task)
    else:
        print('Task does not exist')


def mark_completed_task():
    """
    Moves a task to the completed tasks list.

    Raises:
        ValueError: If the user input is a numeric value.
        InvalidLength: If the user input is empty.
        InvalidInput: If the task does not exist in the user_tasks list.

    Returns:
        None
    """
    try:
        completed_tasks = input('Enter the completed task: ')
        if completed_tasks.isnumeric():
            raise ValueError('Your task cannot be a number')
        if len(completed_tasks) < 1:
            raise InvalidLength("You haven't added any taks")
        if completed_tasks not in user_tasks and len(completed_tasks) > 0:
            raise InvalidInput("You don't have such a task on your list")
        user_tasks.remove(completed_tasks)
        completed_user_tasks.append(completed_tasks)
        print('Task has been moved to completed tasks')
    except ValueError as error:
        print(error)
    except InvalidLength as error:
        print(error)
    except InvalidInput as error:
        print(error)


def save_task_to_file(tasks: list):
    """
    Saves a task from the given tasks list to a file.

    Args:
        tasks (list): The list of tasks.

    Raises:
        InvalidInput: If the task does not exist in the list.

    Returns:
        None
    """
    print(f'Your tasks: {tasks}')
    user_task_to_file = input('Choose the task you want to add to the file: ')
    try:
        if user_task_to_file in tasks:
            with open('tasks.txt', 'a', encoding='utf8') as file:
                file.write(f'{user_task_to_file}\n')
            print('Task has been saved to the file')
            tasks.remove(user_task_to_file)
        else:
            raise InvalidInput("You don't have such a task on your list")
    except InvalidInput as error:
        print(error)


def load_tasks_from_file():
    """
    Loads tasks from a file and displays them.

    Returns:
        None
    """
    try:
        with open('tasks.txt', 'r', encoding='utf8') as file:
            print("Your tasks from file:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("You don't have any tasks in your file")
