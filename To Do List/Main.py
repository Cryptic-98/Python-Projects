tasks = []


def add_task():
    add = input('Add a task: ')
    tasks.append(add)
    print('New Task added. \n')
    main()


def view_tasks():
    print('Tasks:')
    num = 1
    for x in tasks:
        print(f'{num}. {x}')
        num += 1
    return_to_menu = input('Press R to return: ')
    while return_to_menu.lower() != 'r':
        print('Wrong key!')
        return_to_menu = input('Press R to return: ')
    else:
        main()


"""
def done_task():
    print(view_tasks())
    print('Tasks:')
    num = 1
    for x in tasks:
        print(f'{num}. {x}')
        num += 1
    item_chosen = int(input('Choose item to mark done: '))
    if item_chosen == num:
        removed = tasks.remove()
    return_to_menu = input('Press R to return: ')
    while return_to_menu.lower() != 'r':
        print('Wrong key!')
        return_to_menu = input('Press R to return: ')
    else:
        main()
"""


def main():
    print('Welcome to the Simple To Do List "App"')
    print('1. Add Tasks')
    print('2. View Tasks')
    print('3. Mark Task as DONE')
    print('PRESS Q TO QUIT')
    user_choice = ''
    while user_choice != 'Q':
        user_choice = input('Choose (1, 2, 3 or Q): ').strip().upper()
        if user_choice == '1':
            add_task()
        elif user_choice == '2':
            view_tasks()
        elif user_choice == '3':
            done_task()
        elif user_choice == 'Q':
            print('Bye Bye...')
        else:
            print('Invalid Entry!')


main()
