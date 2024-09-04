tasks = []


def add_task():
    task = input('Add a task: ')
    tasks.append(task)
    print('New Task added.\n')


def view_tasks():
    if not tasks:
        print('No tasks to show.')
    else:
        print('Tasks:')
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')
    input('Press R to return: ')


def done_task():
    view_tasks()
    if tasks:
        try:
            item_chosen = int(input('Choose item to mark done: ')) - 1
            if 0 <= item_chosen < len(tasks):
                tasks.pop(item_chosen)
                print('Task marked as done.\n')
            else:
                print('Invalid task number.')
        except ValueError:
            print('Invalid input. Please enter a number.')
    input('Press R to return: ')


def main():
    print('Welcome to the Simple To Do List "App"')
    while True:
        print('\n1. Add Tasks')
        print('2. View Tasks')
        print('3. Mark Task as DONE')
        print('PRESS Q TO QUIT')

        user_choice = input('Choose (1, 2, 3 or Q): ').strip().upper()

        if user_choice == '1':
            add_task()
        elif user_choice == '2':
            view_tasks()
        elif user_choice == '3':
            done_task()
        elif user_choice == 'Q':
            print('Bye Bye...')
            break
        else:
            print('Invalid Entry!')


if __name__ == "__main__":
    main()

