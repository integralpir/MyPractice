N =int(input())
M = N
for i in range(1, N+1):
    if i == 1 or i == N:
        print("X" * M)
    else:
        print("X" + " " * (N - 2) + "X")
