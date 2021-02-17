N, M = input().split()
M = int(M)
N = int(N)
A = [0] * N
for i in range (M):
    print(A)
    for i in range (1, N):
        A[i] += 1*i
