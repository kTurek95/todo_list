user_tasks = []
completed_user_tasks = []


def add_task():
    user_task = input('Add a task: ')
    if len(user_task) > 0:
        user_tasks.append(user_task)
    else:
        print("You haven't added any task")


def display_tasks(tasks: list):
    if len(tasks) > 0:
        tasks_string = 'Your tasks are:\n' + '\n'.join(tasks)
        return tasks_string
    else:
        return "You don't have any tasks on the list."


def delete_task(task: str, tasks_list: list):
    if task in tasks_list:
        tasks_list.remove(task)
    else:
        return "Task does not exist"


def mark_task_completed():
    completed_tasks = input('Enter the completed task: ')
    user_tasks.remove(completed_tasks)
    completed_user_tasks.append(completed_tasks)
    print('Task has been moved to completed tasks')


def save_task_to_file():
    user_task_to_file = input('Enter the task you want to add to the file: ')
    with open('tasks.txt', 'w') as file:
        file.write(user_task_to_file)
    print('Task has been saved to the file')


def load_tasks_from_file():
    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())


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
            add_task()
        elif user_choice == '2':
            print(display_tasks(user_tasks))
        elif user_choice == '3':
            user_task_to_delete = input('Enter the task you want to delete: ')
            delete_task(user_task_to_delete, user_tasks)
        elif user_choice == '4':
            mark_task_completed()
        elif user_choice == '5':
            save_task_to_file()
        elif user_choice == '6':
            load_tasks_from_file()
        else:
            print('Invalid option')
            break
