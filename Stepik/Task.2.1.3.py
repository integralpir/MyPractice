N = int(input())
A = [ ]*N
A = input().split(' ')
for i in range(N):
    A[i] = int(A[i])
print(min(A))