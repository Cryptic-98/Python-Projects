import math


def root():
    num1 = float(input('Enter base number: '))
    num2 = float(input('Enter root number: '))
    if num2 == 2:
        result = math.sqrt(num1)
        print(f'The square root of {num1} = {result}')
    elif num2 > 2:
        result = num1 ** (1 / num2)
        print(f'The {num2}th root of {num1} = {result}')
