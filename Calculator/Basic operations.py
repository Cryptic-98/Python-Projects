def basic_operations():
    num1 = float(input('Enter first number: '))
    operator = input('Enter an operator (+, -, *:, /): ')
    num2 = float(input('Enter second number: '))
    while operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print('Invalid entry')
        operator = input('Enter an operator (+, -, *, /): ')
    if operator == '+':
        addition = num1 + num2
        print(f'{num1} + {num2} = {addition}')
    elif operator == '-':
        subtraction = num1 - num2
        print(f'{num1} - {num2} = {subtraction}')
    elif operator == '*':
        multiplication = num1 * num2
        print(f'{num1} × {num2} = {multiplication}')
    else:
        while num2 == 0:
            print(f'Cannot divide {num2}')
            num2 = float(input('Enter new number: '))
        division = num1 / num2
        print(f'{num1} ÷ {num2} = {division}')


basic_operations()