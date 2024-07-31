import math

def log():
    num = float(input('Enter number: '))
    answer = math.log(num)
    while num < 1:
        print('Invalid Entry')
        num = float(input('Enter number: '))
    else:
        return f'Answer = {answer}'
def logBase10():
    num = float(input('Enter number: '))
    answer = math.log10(num)
    return f'Answer = {answer}'

