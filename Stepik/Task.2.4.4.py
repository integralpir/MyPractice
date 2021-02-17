A = [ ]
even = 0
A = input().split(' ')
N = len(A)
for i in range(N):
    A[i] = int(A[i])
    if A[i] % 2 == 0:
        A[i] = even
print(even)        