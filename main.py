user_tasks = []
completed_user_tasks = []

while True:
    print('-----ToDoList Application-----')
    print('1. Add task')
    print('2. Display tasks')
    print('3. Remove task from the list')
    print('4. Mark task as completed')
    print('5. Save tasks to a file')
    print('6. Load tasks from a file')

    user_choice = input('Choose what you want to do: ')

    if user_choice == '1':
        user_task = input('Add a task: ')
        user_tasks.append(user_task)
    elif user_choice == '2':
        print(f'Your tasks are: {user_tasks}')
    elif user_choice == '3':
        user_task_to_delete = input('Enter the task you want to delete: ')
        user_tasks.remove(user_task_to_delete)
    elif user_choice == '4':
        completed_tasks = input('Enter the completed task: ')
        user_tasks.remove(completed_tasks)
        completed_user_tasks.append(completed_tasks)
        print('Task has been moved to completed tasks')
    elif user_choice == '5':
        user_task_to_file = input('Enter the task you want to add to the file: ')
        with open('tasks.txt', 'w') as file:
            file.write(user_task_to_file)
        print('Task has been saved to the file')
    elif user_choice == '6':
        with open('tasks.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    else:
        print('Invalid option')
        break
