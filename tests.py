"""
Module with tests for the function module.

This module contains unit tests for the functions in the function module.

Usage:
    Run this module to perform the unit tests.

Classes:
    - TestAddTask: A test case class for testing the functions in the function module.
"""

import unittest
import io
from unittest.mock import mock_open, patch
import function as fn


class TestAddTask(unittest.TestCase):
    """
    A test case class for testing the functions in the function module.
    """
    def setUp(self):
        """
        Set up a clean user_tasks list before each test.
        """
        self.user_tasks = []

    def test_add_task(self):
        """
        Test the add_task function.

        It checks if the function correctly adds a task to the user_tasks list.
        """
        with patch('builtins.input', return_value='Test Task'):
            fn.add_task(self.user_tasks)
        self.assertIn('Test Task', self.user_tasks)

    def test_display_tasks_with_tasks(self):
        """
        Test the display_tasks function with tasks in the list.

        It verifies if the function correctly formats and returns the list of tasks.
        """
        tasks = ['Task 1', 'Task 2', 'Task 3']
        result = fn.display_tasks(tasks)
        expected = "Your tasks are:\nTask 1\nTask 2\nTask 3"
        self.assertEqual(result, expected)

    def test_display_tasks_without_tasks(self):
        """
        Test the display_tasks function without tasks in the list.

        It checks if the function returns the correct message when there are no tasks.
        """
        tasks = []
        result = fn.display_tasks(tasks)
        expected = "You don't have any tasks on the list."
        self.assertEqual(result, expected)

    def test_delete_task(self):
        """
        Test the delete_task function.

        It verifies if the function correctly removes a task from the user_tasks list.
        """
        user_tasks = ['take out the trash', 'wash the car']
        task_to_delete = 'wash the car'
        fn.delete_task(task_to_delete, user_tasks)
        self.assertNotIn(task_to_delete, user_tasks)

    def test_delete_task_empty_list(self):
        """
        Test the delete_task function with an empty user_tasks list.

        It checks if the function handles the case when the list is empty
        and returns the correct message.
        """

        user_tasks = []
        task_to_delete = 'wash the car'
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            fn.delete_task(task_to_delete, user_tasks)
            self.assertEqual(mock_stdout.getvalue(), 'Task does not exist\n')

    def test_mark_completed_task(self):
        """
        Test the mark_completed_task function.

        It checks if the function correctly moves a task to the completed_user_tasks list.
        """
        user_tasks = []
        fn.user_tasks.append('Test Task')
        with patch('builtins.input', return_value='Test Task'):
            fn.mark_completed_task()
        self.assertIn('Test Task', fn.completed_user_tasks)
        self.assertNotIn('Test Task', user_tasks)

    @patch('builtins.input', return_value='Test Task')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_task_to_file(self, mock_file_open, mock_input):
        """
        Test the save_task_to_file function.

        It checks if the function correctly saves a task to a file.
        """
        tasks = ['Test Task']
        fn.save_task_to_file(tasks)
        mock_file_open.assert_called_once_with('tasks.txt', 'a', encoding='utf8')
        mock_file_open().write.assert_called_once_with('Test Task\n')

    @patch('builtins.open', new_callable=mock_open, read_data='Task 1\nTask 2\nTask 3\n')
    def test_load_tasks_from_file(self, mock_file_open):
        """
        Test the load_tasks_from_file function.

        It verifies if the function correctly loads tasks from a file and displays them.
        """
        with patch('builtins.print') as mock_print:
            fn.load_tasks_from_file()

        mock_file_open.assert_called_once_with('tasks.txt', 'r', encoding='utf8')
        mock_print.assert_has_calls([
            unittest.mock.call('Task 1'),
            unittest.mock.call('Task 2'),
            unittest.mock.call('Task 3')
        ], any_order=False)


if __name__ == '__main__':
    unittest.main()
