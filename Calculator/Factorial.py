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
