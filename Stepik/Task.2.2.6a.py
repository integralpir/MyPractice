N =int(input())
M = N
for i in range(N):
    if i != (N-1):
        print(' ' * i + "X" + " " * ((N - 2) - i) + "X")
    else:
        print('X' * M)