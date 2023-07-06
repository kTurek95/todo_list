import unittest
import function as fn


class TestAddTask(unittest.TestCase):
    def test_one_task(self):
        user_tasks = []
        user_task = 'take out the trash'
        user_tasks.append(user_task)
        self.assertEqual(user_tasks, ['take out the trash'])

    def test_add_multiple_task(self):
        user_tasks = []
        user_task = 'take out the trash'
        user_task1 = 'wash the car'
        user_tasks.append(user_task)
        user_tasks.append(user_task1)
        self.assertEqual(user_tasks, ['take out the trash', 'wash the car'])

    def test_empty_task(self):
        pass


class TestDisplayTask(unittest.TestCase):
    def test_one_task(self):
        user_tasks = []
        user_task = 'wash the car'
        user_tasks.append(user_task)
        self.assertEqual(user_tasks, ['wash the car'])

    def test_few_tasks(self):
        user_tasks = ['take out the trash', 'wash the car']
        expected_output = "Your tasks are:\ntake out the trash\nwash the car"
        output = fn.display_tasks(user_tasks)
        self.assertEqual(output, expected_output)

    def test_empty_task(self):
        user_tasks = []
        expected_output = "You don't have any tasks on the list."
        output = fn.display_tasks(user_tasks)
        self.assertEqual(expected_output, output)


class TestDeleteTask(unittest.TestCase):
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


class TestMarkTaskCompleted(unittest.TestCase):
    pass


class TestSaveTaskToFile(unittest.TestCase):
    pass


class TestLoadTaskFromFile(unittest.TestCase):
    pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()

