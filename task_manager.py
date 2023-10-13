"""
Module with functions
This module provides functions for basic task management.
It includes functionalities for adding, displaying, deleting,
and marking tasks as completed, as well as saving and loading tasks from a file.
"""

from exception import InvalidInput, InvalidLength


class TaskManager:
    def __init__(self):
        self.user_tasks = []
        self.completed_user_tasks = []

    def add_task(self):
        """
            Adds a task to the given tasks list.

            Raises:
                ValueError: If the user input is a numeric value.
                InvalidLength: If the user input is empty.

            Returns:
                None
            """
        try:
            task_from_user = input('Add a task: ')
            if task_from_user.isnumeric():
                raise ValueError('Your task cannot be a number')
            if len(task_from_user) > 0:
                self.user_tasks.append(task_from_user)
            else:
                raise InvalidLength("You haven't added any task")
        except ValueError as error:
            print(error)
        except InvalidLength as error:
            print(error)

    def display_tasks(self):
        """
        Displays the tasks in the given tasks list.

        Returns:
            str: A formatted string containing the tasks or a message if the list is empty.
        """
        if self.user_tasks:
            print('Your tasks are:')
            for i, task in enumerate(self.user_tasks, 1):
                print(f'{i}. {task}')
        else:
            print('You don\'t have any tasks on the list.')

    def delete_task(self):
        """
        Deletes a task from the specified tasks list.

        Raises:
            InvalidTask: If the task does not exist in the list.

        Returns:
            None
        """
        user_task_to_delete = input('Enter the task you want to delete: ')

        if user_task_to_delete in self.user_tasks:
            self.user_tasks.remove(user_task_to_delete)
            print('Task has been deleted')
        else:
            print('Task does not exist')

    def mark_completed_task(self):
        """
        Moves a task to the completed tasks list.

        Raises:
            ValueError: If the user input is a numeric value.
            InvalidLength: If the user input is empty.
            InvalidInput: If the task does not exist in the user_tasks list.

        Returns:
            None
        """
        completed_task = input('Enter the completed task: ')
        try:
            if completed_task.isnumeric():
                raise ValueError('Your task cannot be a number')
            if len(completed_task) < 1:
                raise InvalidLength("You haven't added any taks")
            if completed_task not in self.user_tasks and len(completed_task) > 0:
                raise InvalidInput("You don't have such a task on your list")
            self.user_tasks.remove(completed_task)
            self.completed_user_tasks.append(completed_task)
            print('Task has been moved to completed tasks')
        except ValueError as error:
            print(error)
        except InvalidLength as error:
            print(error)
        except InvalidInput as error:
            print(error)

    def save_task_to_file(self):
        """
        Saves a task from the given tasks list to a file.

        Raises:
            InvalidInput: If the task does not exist in the list.

        Returns:
            None
        """
        if self.user_tasks:
            print(f'Your tasks: {self.user_tasks}')
            user_task_to_file = input('Choose the task you want to add to the file: ')
            try:
                if user_task_to_file in self.user_tasks:
                    with open('tasks.txt', 'a', encoding='utf8') as file:
                        file.write(f'{user_task_to_file}\n')
                    print('Task has been saved to the file')
                    self.user_tasks.remove(user_task_to_file)
                else:
                    raise InvalidInput("You don't have such a task on your list")
            except InvalidInput as error:
                print(error)
        else:
            print("You don't have any tasks on the list")

    @staticmethod
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
