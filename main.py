from function import add_task, display_tasks, delete_task, user_tasks, mark_completed_task, save_task_to_file, \
    load_tasks_from_file


def main():
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
            add_task(user_tasks)
        elif user_choice == '2':
            print(display_tasks(user_tasks))
        elif user_choice == '3':
            user_task_to_delete = input('Enter the task you want to delete: ')
            delete_task(user_task_to_delete, user_tasks)
        elif user_choice == '4':
            mark_completed_task()
        elif user_choice == '5':
            save_task_to_file(user_tasks)
        elif user_choice == '6':
            load_tasks_from_file()
        else:
            print('Invalid option')
            break


if __name__ == '__main__':
    main()
