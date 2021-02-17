N = int(input())
A = [ ]*N
A = input().split(' ')
count = 0
for i in range(N):
    A[i] = int(A[i])
    if (A[i] % 5 != 0):
        count += 1
print(count)