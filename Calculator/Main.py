import math


def basic_operations():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    operator = input('Enter an operator (+, -, *:, /): ')
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
        division = num1 / num2
        print(f'{num1} ÷ {num2} = {division}')


def power():
    num1 = float(input('Enter base number: '))
    num2 = float(input('Enter exponent: '))
    answer = num1 ** num2
    print(f'{num1} to the power of {num2} = {answer}')


def factorial():
    num = int(input('Enter a number to be factorized: '))
    fact = 1
    while num > 2:
        print('Invalid Entry: factor of 0 does not exist')
        num = int(input('Enter a number to be factorized: '))
    for x in range(1, num + 1):
        fact = fact * x
    print(f'The factorial of {num} = {fact}')


def root():
    num1 = float(input('Enter base number: '))
    num2 = float(input('Enter root number: '))
    if num2 == 2:
        result = math.sqrt(num1)
        print(f'The square root of {num1} = {result}')
    elif num2 > 2:
        result = num1 ** (1 / num2)
        print(f'The {num2}th root of {num1} = {result}')


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


def log():
    num = float(input('Enter number: '))
    answer = math.log(num)
    while num < 1:
        print('Invalid Entry')
        num = float(input('Enter number: '))
    else:
        return f'Answer = {answer}'


def base():
    num = float(input('Enter number: '))
    answer = math.log10(num)
    return f'Answer = {answer}'


print("1. Basic operations")
print("2. Power function")
print("3. Factorial")
print("4. Root calculations")
print("5. Trigonometric functions")
print("6. Logarithm")
print("7. Logarithm Base10")
option = input("Enter option: ")
while option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6" and option != "7":
    print('Invalid option')
    print("1. Basic operations")
    print("2. Power function")
    print("3. Factorial")
    print("4. Root calculations")
    print("5. Trigonometric functions")
    print("6. Logarithm")
    print("7. Logarithm Base10\n\n")
    option = input("Enter option: ")

if option == "1":
    basic_operations()
elif option == "2":
    power()
elif option == "3":
    factorial()
elif option == "4":
    root()
elif option == "5":
    trigonometry()
elif option == "6":
    log()
else:
    base()
input()
