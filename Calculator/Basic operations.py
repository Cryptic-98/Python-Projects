def arithmetic_operations():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    operator = input('Enter an operator (+, -, *:, /): ')
    while operator != '+' or operator != '-' or operator != '*' or operator != '/':
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
        division = num1 / num2
        print(f'{num1} ÷ {num2} = {division}')

