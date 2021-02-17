import math

n = int(input())

print('X')
if n > 1:
    if n > 2:
        for i in range(n - math.ceil(n/2)):
            print('X' + ' ' * (n - (n-i)) + 'X')

    print('X'+ ' ' * (n-2) + 'X')

    if n > 2:
        for i in range(n - math.ceil(n/2), 0, -1,):
            print('X' + ' ' * (n - (n-i+1)) + 'X')

    print('X')

print(math.ceil(n/2))