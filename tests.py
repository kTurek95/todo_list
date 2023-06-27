import unittest


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


def main():
    unittest.main()


if __name__ == '__main__':
    main()

