n = int(input())
N = 5 + (2 * (n - 1))
M = N
for i in range(N):
    if i == 0 or i == (N-1) or (i - ((N-1)/2)) == 0:
        print('X' * M)
    else:
        print('X' + ' ' * n + 'X' + ' ' * n + 'X')