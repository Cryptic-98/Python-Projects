import math


def trigonometry():
    num1 = float('Enter number: ')
    function = input('(S)in, (C)os, (T)an: ')
    while function != 's' and function != 'S' and function != 'c' and function != 'C' and function != 't' and function != 'T':
        print('Invalid entry')
        function = input('(S)in, (C)os, (T)an: ')
    if function == 's' or function == 'S':
        answer = math.sin(num1)
        print(f'sin({num1}) = {answer}')
    elif function == 'c' or function == 'C':
        answer = math.cos(num1)
        print(f'cos({num1}) = {answer}')
    else:
        answer = math.tan(num1)
        print(f'tan({num1}) = {answer}')
