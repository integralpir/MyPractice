m, n = map(int, input().split())
for i in range (1, n + 1):
    A = []
    if i % 2 != 0:
        for j in range(1, m + 1):
            A.append(j + m * (i - 1))
    else:
        for j in range(m, 0, -1):
            A.append(j + m * (i - 1))
    print(*A)