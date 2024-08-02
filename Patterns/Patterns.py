# I kept some of the code that i though would help but just messed things up

for x in range(6):
    print('*', end='')
    for y in range(6 - 1):
        if x == y:
            print('*', end='')
        else:
            print(' ', end='')
    print('*')

for x in range(5):
    char = ord('A') + x
    for y in range(x, 5):
        print(' ', end=' ')
    for y in range(x):
        print(chr(char), end=' ')
    for y in range(x + 1):
        print(chr(char), end=' ')
    for y in range(x, 5):
        print(' ', end=' ')
    #     for y in range(x, 5):
    #         print('', end='')
    for y in range(x, 5):
        print(' ', end=' ')
    #     for y in range(x, 5):
    #         print('', end='')
    for y in range(x):
        print(chr(char), end=' ')
    for y in range(x + 1):
        print(chr(char), end=' ')
    print()


for x in range(7):
    p = 2 ** x
    for y in range(x + 1):
        print(p, end=' ')
        # p = p - 2
    print()

char = ord('A')
for x in range(7):
    for y in range(x + 1):
        print(chr(char), end=' ')
        char = char + 1
    print()
