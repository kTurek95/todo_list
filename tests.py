import unittest
from unittest.mock import mock_open, patch
import function as fn


class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.user_tasks = []

    def test_add_task(self):
        with patch('builtins.input', return_value='Test Task'):
            fn.add_task(self.user_tasks)
        self.assertIn('Test Task', self.user_tasks)

    def test_display_tasks_with_tasks(self):
        tasks = ['Task 1', 'Task 2', 'Task 3']
        result = fn.display_tasks(tasks)
        expected = "Your tasks are:\nTask 1\nTask 2\nTask 3"
        self.assertEqual(result, expected)

    def test_display_tasks_without_tasks(self):
        tasks = []
        result = fn.display_tasks(tasks)
        expected = "You don't have any tasks on the list."
        self.assertEqual(result, expected)

    def test_delete_task(self):
        user_tasks = ['take out the trash', 'wash the car']
        task_to_delete = 'wash the car'
        fn.delete_task(task_to_delete, user_tasks)
        self.assertNotIn(task_to_delete, user_tasks)

    def test_delete_task_empty_list(self):
        user_tasks = []
        task_to_delete = 'wash the car'
        output = fn.delete_task(task_to_delete, user_tasks)
        expected_output = 'Task does not exist'
        self.assertEqual(expected_output, output)

    def test_mark_completed_task(self):
        user_tasks = []
        fn.user_tasks.append('Test Task')
        with patch('builtins.input', return_value='Test Task'):
            fn.mark_completed_task()
        self.assertIn('Test Task', fn.completed_user_tasks)
        self.assertNotIn('Test Task', user_tasks)

    @patch('builtins.input', return_value='Test Task')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_task_to_file(self, mock_file_open, mock_input):
        fn.save_task_to_file()
        mock_file_open.assert_called_once_with('tasks.txt', 'a', encoding='utf8')
        mock_file_open().write.assert_called_once_with('Test Task\n')

    @patch('builtins.open', new_callable=mock_open, read_data='Task 1\nTask 2\nTask 3\n')
    def test_load_tasks_from_file(self, mock_file_open):
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
