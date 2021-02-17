N = int(input())
S = 0
A = [ ]*N
A = input().split(' ')
for i in range(N):
    A[i] = int(A[i])
    if A[i] % 2 == 0:
        S += A[i]
print(S)
        


    